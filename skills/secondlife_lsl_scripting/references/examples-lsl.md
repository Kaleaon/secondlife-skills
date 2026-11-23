# LSL Example Library — Complete, Working Scripts

Hand-written examples for the Second Life skills repo. Every script here is a complete,
droppable LSL script: paste it into a new script in a prim, save, and it runs. They are
written for Second Life (Agni/Aditi, Mono compiler) first. Where OpenSim behaves
differently that is called out in the notes for that example — read those notes before
assuming a script that works on your local OpenSim region will work unchanged on Agni,
or the reverse.

Conventions used throughout:

- `llOwnerSay()` is used for debug and status output. Only the owner sees it, it does
  not spam public chat, and it is cheap. Gate it behind a `gDebug` flag in anything
  you sell or give away.
- Channel `0` is public chat. Scripts that listen on channel 0 hear everyone nearby,
  including other objects, so command listeners use a high negative channel or check
  the speaker key. Never build a security feature on "nobody knows the channel" alone:
  channels are not secret, anyone can script a listener.
- Every `llListen()` handle is stored in a variable so it can be removed with
  `llListenRemove()`. Leaked listens are a classic source of "my object hears things
  twice" and of lag complaints.
- LSL has no exceptions and no try/catch. A runtime error stops that event handler
  (and stack-heap collisions can stop the script). Defensive checks — null keys,
  empty strings, list bounds — are written out longhand on purpose.
- Memory is 64 KB for Mono scripts in SL. These examples stay far under that, but the
  notecard, KVP, and menu examples show the patterns (streaming, pagination) you need
  when data grows.

---

## Example 1 — Minimal state machine: greeting greeter with on/off states

**What it does:** The smallest useful LSL program that still shows the real shape of
the language: a `default` state, a named state, `state_entry` / `state_exit` on both,
a touch toggle that moves between them, and `on_rez` / `changed` housekeeping. If you
understand this script you understand the execution model of every other example here:
there is no `main()`, no loop that runs forever — the simulator calls your event
handlers, one at a time, in queue order, on a single cooperative thread.

```lsl
// Greeter — minimal two-state machine.
// Touch toggles the greeter on and off. While ON, anyone who comes within
// SENSOR_RANGE metres triggers a greeting (once per visit, not a spam loop).

float  SENSOR_RANGE = 8.0;      // metres; llSensorRepeat range is capped at 96 m in SL
float  SENSOR_PERIOD = 2.0;     // seconds between sensor sweeps
string GREETING = "Hello and welcome.";

// Keys we have already greeted during this "visit". A list in LSL is the only
// collection type there is — no arrays, no maps, no sets. Membership tests are
// linear scans with llListFindList(), which is fine at this scale and is the
// idiomatic way to do it.
list gGreeted = [];

default
{
    state_entry()
    {
        // state_entry runs EVERY time we enter this state, including at script
        // start, after a reset, and when we return here from state on.
        llOwnerSay("Greeter is OFF. Touch to switch on.");
        llSetText("Greeter: OFF", <1.0, 0.4, 0.4>, 1.0);
    }

    touch_start(integer num_detected)
    {
        // Only the owner should be able to arm a greeter on their own land.
        // llDetectedKey(0) is the first toucher in this event batch.
        if (llDetectedKey(0) != llGetOwner()) return;
        state on;   // <-- the state transition. state_exit() below runs first.
    }

    state_exit()
    {
        llOwnerSay("Leaving OFF state.");
    }

    on_rez(integer start_param)
    {
        // Rezzing a scripted object does NOT reset the script, but resetting on
        // rez is the safe default for anything that changes owner or location.
        llResetScript();
    }
}

state on
{
    state_entry()
    {
        llOwnerSay("Greeter is ON.");
        llSetText("Greeter: ON", <0.4, 1.0, 0.4>, 1.0);
        gGreeted = [];
        // llSensorRepeat keeps firing sensor/no_sensor events on a period.
        // AGENT = only avatars (not physical objects, not other prims).
        llSensorRepeat("", NULL_KEY, AGENT, SENSOR_RANGE, PI, SENSOR_PERIOD);
    }

    sensor(integer num_detected)
    {
        integer i;
        for (i = 0; i < num_detected; ++i)
        {
            key who = llDetectedKey(i);
            if (llListFindList(gGreeted, [who]) == -1)
            {
                gGreeted += [who];
                // llInstantMessage works at any distance and does not depend on
                // the avatar still being in sensor range when it is delivered.
                llInstantMessage(who, GREETING);
            }
        }
    }

    no_sensor()
    {
        // Nobody around: forget the greeted list so the next visit greets again.
        // Without this, a regular visitor is greeted exactly once, ever, until
        // the script resets — the single most common greeter bug.
        gGreeted = [];
    }

    touch_start(integer num_detected)
    {
        if (llDetectedKey(0) != llGetOwner()) return;
        state default;
    }

    state_exit()
    {
        // IMPORTANT: llSensorRepeat is cancelled automatically on state change
        // in SL, but be explicit anyway — scripts ported from old LSO behaviour
        // and some OpenSim versions have differed here.
        llSensorRemove();
        llSetText("", ZERO_VECTOR, 0.0);
    }

    changed(integer change)
    {
        // If the object changes owner (sold/given), reset so the new owner's
        // touch check and greeted list are correct.
        if (change & CHANGED_OWNER) llResetScript();
    }
}
```

**Notes and pitfalls**

- SL vs OpenSim: sensor limits differ. SL caps `llSensorRepeat` range at 96 m and
  returns at most 16 detected entities per sweep; OpenSim historically returned more
  in some configurations and its YEngine/XEngine timer and sensor timing differ
  slightly. Never tune a sensor period against OpenSim alone.
- `state` transitions fire `state_exit` in the old state and `state_entry` in the
  new one, and pending events in the queue are discarded on a state change. Do not
  put "must run" cleanup in an event you expect to survive a transition.
- The event queue is finite (64 events in SL). A sensor firing faster than handlers
  drain it silently drops events.

---

## Example 2 — Touch toggle light with face-aware prim params

**What it does:** Toggles a prim between "lamp on" and "lamp off" on touch, setting
fullbright, glow, colour, and an actual point light (`PRIM_POINT_LIGHT`) on a named
face, and remembers the state across touches in a global. Shows the everyday
`llSetPrimitiveParams` / `llGetPrimitiveParams` workflow and why `PRIM_*` calls are
face-indexed.

```lsl
// Lamp — touch to toggle. Demonstrates PRIM_POINT_LIGHT, PRIM_FULLBRIGHT,
// PRIM_GLOW and PRIM_COLOR, all of which are PER-FACE properties.

integer gOn = FALSE;
integer FACE = 0;               // change to ALL_SIDES (-1) for the whole prim
vector  ON_COLOR  = <1.0, 0.9, 0.6>;   // warm white
vector  OFF_COLOR = <0.25, 0.25, 0.25>;

apply_state()
{
    if (gOn)
    {
        llSetPrimitiveParams([
            PRIM_FULLBRIGHT, FACE, TRUE,
            PRIM_GLOW, FACE, 0.35,
            PRIM_COLOR, FACE, ON_COLOR, 1.0,
            // PRIM_POINT_LIGHT: on/off, colour, intensity, radius, falloff.
            // A prim can be a light source only if this flag is set; glow alone
            // is purely visual and lights nothing.
            PRIM_POINT_LIGHT, TRUE, ON_COLOR, 1.0, 6.0, 0.5
        ]);
    }
    else
    {
        llSetPrimitiveParams([
            PRIM_FULLBRIGHT, FACE, FALSE,
            PRIM_GLOW, FACE, 0.0,
            PRIM_COLOR, FACE, OFF_COLOR, 1.0,
            PRIM_POINT_LIGHT, FALSE, ZERO_VECTOR, 0.0, 0.0, 0.0
        ]);
    }
}

default
{
    state_entry()
    {
        gOn = FALSE;
        apply_state();
        llSetText("Touch for light", <1,1,1>, 0.8);
    }

    touch_start(integer n)
    {
        gOn = !gOn;
        apply_state();
        // llSetPrimitiveParams has a built-in 0.2 s script delay in SL.
        // Rapid touching therefore self-throttles; if you need fast updates use
        // llSetLinkPrimitiveParamsFast() instead (see Example 5 notes).
        llOwnerSay("Lamp on=" + (string)gOn);
    }
}
```

**Notes and pitfalls**

- Point lights are limited per scene by the viewer's lighting settings; a room full
  of "on" lamps does not mean a room full of actual illumination in every viewer.
- `PRIM_GLOW` renders through the viewer's glow pipeline and looks different (often
  stronger) in viewers with different post-processing. Do not use glow values tuned
  in one viewer as a specification.
- OpenSim: `PRIM_POINT_LIGHT` and glow are supported, but LightShare / `wl*`
  windlight functions are OpenSim-only and do not exist on Agni — do not mix them in.

---

## Example 3 — Chat command listener with owner check and channel discipline

**What it does:** Listens for owner commands on a private channel (`/99 colour red`,
`/99 colour blue`, `/99 reset`), parses them with `llParseString2List`, and applies
them. Shows the correct pattern for command channels: listen on a non-zero channel,
verify the speaker is the owner, remove the listen handle when done, and never trust
channel secrecy for anything that matters.

```lsl
// Command listener — owner-only commands on channel 99.
// In chat the owner types:  /99 red    /99 blue    /99 reset

integer CMD_CHANNEL = 99;
integer gListenHandle = 0;

default
{
    state_entry()
    {
        // Filter by speaker key: this listen only fires for the owner at all,
        // which is both a security measure and a performance one — the sim does
        // not even queue events for other speakers.
        gListenHandle = llListen(CMD_CHANNEL, "", llGetOwner(), "");
        llOwnerSay("Listening for owner commands on /" + (string)CMD_CHANNEL);
    }

    listen(integer channel, string name, key id, string message)
    {
        // Defence in depth: the listen filter already restricted the speaker,
        // but check again. Listens copied between scripts lose filters silently.
        if (id != llGetOwner()) return;

        string cmd = llToLower(llStringTrim(message, STRING_TRIM));
        list parts = llParseString2List(cmd, [" "], []);
        string verb = llList2String(parts, 0);

        if (verb == "red")
        {
            llSetColor(<1.0, 0.2, 0.2>, ALL_SIDES);
        }
        else if (verb == "blue")
        {
            llSetColor(<0.2, 0.4, 1.0>, ALL_SIDES);
        }
        else if (verb == "reset")
        {
            llResetScript();   // note: listen handle is recreated in state_entry
        }
        else
        {
            llOwnerSay("Unknown command: " + cmd + " (try red, blue, reset)");
        }
    }

    changed(integer change)
    {
        if (change & CHANGED_OWNER)
        {
            // The stored listen was filtered to the OLD owner. Remove and
            // re-create it by resetting.
            llListenRemove(gListenHandle);
            llResetScript();
        }
    }
}
```

**Notes and pitfalls**

- Chat ranges: `llSay` 20 m, `llWhisper` 10 m, `llShout` 100 m, region-wide only via
  `llRegionSay` / `llRegionSayTo`. A listener hears normal chat only within 20 m of
  the speaker regardless of channel.
- `llListen` on channel 0 hears *avatars and objects*. Griefing objects talk on
  channel 0 constantly in busy areas; that is why command channels exist.
- OpenSim: same API, but region chat ranges and listen behaviour around region
  borders have historically differed. Test border cases on Agni/Aditi.
- Never accept a Linden-dollar, teleport, or attach action from chat without a key
  check like the one above. Channel numbers are guessable and scanners exist.

---
## Example 4 — Paginated dialog menu with timeout and channel-per-user

**What it does:** A real dialog menu system: touch opens a menu of options, more than
12 options are paginated with Back/More buttons, each user gets their own random
dialog channel, the listen is removed after a choice or after a 60-second timeout,
and button text is truncated to the 24-character dialog limit. This is the pattern
behind almost every HUD and configuration prim in SL.

```lsl
// Menu system — paginated llDialog with per-session channel and timeout.
// Dialog rules that shape this code (SL):
//   * max 12 buttons per dialog
//   * button labels max 24 characters (longer labels are silently truncated
//     in some viewers and rejected in others — truncate yourself)
//   * an empty label "" is an error; use " " for a blank spacer button
//   * dialog channel must be negative-ish private channel; the response comes
//     back through listen() on that channel with the AVATAR as speaker.

list    OPTIONS = ["Red","Green","Blue","Glow On","Glow Off","Bigger","Smaller",
                   "Spin","Stop Spin","Reset","Help","About","Credits","Licence"];
integer PAGE_SIZE = 9;          // 9 options + navigation buttons = 12 max
integer gPage = 0;
key     gUser = NULL_KEY;
integer gChan = 0;
integer gListen = 0;
integer gDeadline = 0;

integer channel_for(key who)
{
    // Derive a large negative channel from the user key + time so two users
    // (or two sessions for the same user) do not collide. llFrand is not
    // cryptographic; collisions are handled by tracking gUser below.
    return -1000000 - (integer)llFrand(1000000.0);
}

show_menu()
{
    integer total = llGetListLength(OPTIONS);
    integer start = gPage * PAGE_SIZE;
    integer end = start + PAGE_SIZE - 1;
    if (end >= total) end = total - 1;

    list buttons = [];
    integer i;
    for (i = start; i <= end; ++i)
    {
        string label = llList2String(OPTIONS, i);
        if (llStringLength(label) > 24) label = llGetSubString(label, 0, 23);
        buttons += [label];
    }
    // llDialog displays buttons in a viewer-specific order (historically
    // bottom-to-top, left-to-right from the END of the list). Keep navigation
    // at fixed positions by appending them last and documenting the layout in
    // the dialog text rather than fighting the ordering.
    if (gPage > 0) buttons += ["<< Back"];
    if (end < total - 1) buttons += ["More >>"];
    buttons += ["Close"];

    llDialog(gUser,
        "Choose an option (page " + (string)(gPage + 1) + "):",
        buttons, gChan);
    gDeadline = llGetUnixTime() + 60;
    llSetTimerEvent(10.0);      // wake up periodically to enforce the timeout
}

close_session()
{
    if (gListen) llListenRemove(gListen);
    gListen = 0;
    gUser = NULL_KEY;
    llSetTimerEvent(0.0);
}

default
{
    touch_start(integer n)
    {
        if (gUser != NULL_KEY) close_session();  // one session at a time (simple model)
        gUser = llDetectedKey(0);
        gPage = 0;
        gChan = channel_for(gUser);
        gListen = llListen(gChan, "", gUser, "");
        show_menu();
    }

    listen(integer channel, string name, key id, string msg)
    {
        if (id != gUser) return;                 // someone else's session
        if (msg == "Close") { close_session(); return; }
        if (msg == "More >>") { gPage++; show_menu(); return; }
        if (msg == "<< Back") { gPage--; show_menu(); return; }

        // A real option was chosen.
        llSay(0, "Selected: " + msg);
        if (msg == "Red")   llSetColor(<1,0.2,0.2>, ALL_SIDES);
        if (msg == "Green") llSetColor(<0.2,1,0.2>, ALL_SIDES);
        if (msg == "Blue")  llSetColor(<0.2,0.4,1>, ALL_SIDES);
        // ... dispatch the rest the same way ...
        close_session();
    }

    timer()
    {
        if (gUser != NULL_KEY && llGetUnixTime() > gDeadline)
        {
            llInstantMessage(gUser, "Menu timed out.");
            close_session();
        }
    }
}
```

**Notes and pitfalls**

- A dialog with no active listen is a dead end: the avatar can click, nothing
  happens, and there is no error anywhere. Always pair `llDialog` with a listen.
- Dialog channels leak across scripts in the same object if you reuse a fixed
  channel. The random per-session channel above is the standard fix.
- OpenSim: dialog limits are the same on paper, but some OpenSim viewers and the
  OpenSim dialog module have differed on empty labels and ordering. Test in the
  viewer your users actually use (Firestorm in both worlds, usually).

---

## Example 5 — link_message protocol between prims in a linkset

**What it does:** A two-script inter-prim protocol. A "controller" script in the root
prim sends typed commands to a "worker" script in a child prim using
`llMessageLinked`, using integer command codes and a small key-value string payload.
This is how HUDs, vehicles, and multi-prim gadgets are actually built: one script
cannot do everything within 64 KB, and scripts in different prims can only talk via
link messages (or chat, which is slower and public).

```lsl
// ---- Script A: controller (put in the ROOT prim) ----
// Protocol: llMessageLinked(link, CMD, payload, id)
//   CMD_SET_COLOR  payload = "r,g,b" as a CSV string (LSL has no structs;
//                  CSV and key=value strings are the universal wire format)
//   CMD_SET_TEXT   payload = the text
//   id field carries the requesting avatar key when relevant.

integer CMD_SET_COLOR = 1001;
integer CMD_SET_TEXT  = 1002;
integer LINK_WORKER   = 2;      // link number of the worker prim; use
                                // llGetLinkNumber() discovery in real builds
                                // instead of hard-coding where possible.

default
{
    touch_start(integer n)
    {
        key toucher = llDetectedKey(0);
        llMessageLinked(LINK_WORKER, CMD_SET_COLOR, "0.2,0.6,1.0", toucher);
        llMessageLinked(LINK_WORKER, CMD_SET_TEXT, "Touched by " +
                         llDetectedName(0), toucher);
    }
}
```

```lsl
// ---- Script B: worker (put in the CHILD prim, link number 2) ----
// The worker validates every message: link messages can come from ANY script
// in the linkset, including a tenant's or a previous owner's leftover script.

integer CMD_SET_COLOR = 1001;
integer CMD_SET_TEXT  = 1002;

default
{
    link_message(integer sender_num, integer num, string str, key id)
    {
        // sender_num = link number of the prim whose script sent this.
        // Ignore messages from prims we do not expect (here: only root = 1).
        if (sender_num != 1) return;

        if (num == CMD_SET_COLOR)
        {
            list rgb = llParseString2List(str, [","], []);
            if (llGetListLength(rgb) == 3)
            {
                vector c = <llList2Float(rgb, 0), llList2Float(rgb, 1),
                            llList2Float(rgb, 2)>;
                // llSetLinkPrimitiveParamsFast has NO 0.2 s delay, unlike
                // llSetPrimitiveParams — that is why workers use it.
                llSetLinkPrimitiveParamsFast(llGetLinkNumber(),
                    [PRIM_COLOR, ALL_SIDES, c, 1.0]);
            }
        }
        else if (num == CMD_SET_TEXT)
        {
            llSetText(str, <1,1,1>, 1.0);
        }
        // Unknown command numbers are ignored, not errored: forward-compatible
        // protocols survive mixed script versions in one linkset this way.
    }
}
```

**Notes and pitfalls**

- `llMessageLinked(LINK_ALL_OTHERS, ...)` and `LINK_THIS` / `LINK_ROOT` constants
  exist; broadcasting to all others is convenient and noisy in big linksets.
- Link numbers change when prims are linked/unlinked. Production code discovers its
  partners by prim name (`llGetLinkName`) at `state_entry` and after
  `changed(CHANGED_LINK)` instead of hard-coding numbers like the teaching code above.
- There is no delivery failure signal and no reply channel: if you need an ACK,
  define a reply command code and send it back. Keep payloads small; link messages
  still cost memory to queue.

---

## Example 6 — HTTP out: fetching JSON and parsing it safely

**What it does:** Requests a JSON document over HTTPS with `llHTTPRequest`, handles
redirects/status in `http_response`, parses fields with `llJsonGetValue`, and shows
the standard failure handling: non-200 status, empty body, invalid JSON, and the
request key check that stops a stale response from a previous request being applied.

```lsl
// Weather fetcher pattern — replace URL with your own HTTPS endpoint.
// LSL HTTP client facts (SL):
//   * llHTTPRequest is throttled: 25 requests per 20 seconds per object in SL.
//   * Custom headers are limited; User-Agent cannot be fully controlled.
//   * The response body is truncated (2048 bytes by default; raise with
//     HTTP_BODY_MAXLENGTH up to 16384).
//   * HTTPS certificate validation applies; self-signed endpoints fail.

string  API_URL = "https://example.com/api/weather.json";
key     gRequestId = NULL_KEY;

fetch()
{
    gRequestId = llHTTPRequest(API_URL,
        [HTTP_METHOD, "GET",
         HTTP_MIMETYPE, "application/json",
         HTTP_BODY_MAXLENGTH, 16384,
         HTTP_PRAGMA_NO_CACHE, TRUE],
        "");
}

default
{
    state_entry()
    {
        fetch();
        llSetTimerEvent(300.0);     // refresh every 5 minutes
    }

    timer() { fetch(); }

    touch_start(integer n) { fetch(); }   // manual refresh for testing

    http_response(key request_id, integer status, list metadata, string body)
    {
        // ALWAYS match the request id. Timers + touches can overlap requests,
        // and LSL will happily deliver the older response last.
        if (request_id != gRequestId) return;

        if (status != 200)
        {
            llOwnerSay("HTTP failed, status=" + (string)status);
            return;
        }
        if (body == "")
        {
            llOwnerSay("HTTP 200 but empty body.");
            return;
        }

        // llJsonGetValue returns the literal string JSON_INVALID if the path
        // does not exist or the JSON does not parse. Check before using.
        string temp = llJsonGetValue(body, ["current", "temp_c"]);
        string cond = llJsonGetValue(body, ["current", "condition"]);
        if (temp == JSON_INVALID || cond == JSON_INVALID)
        {
            llOwnerSay("JSON shape not as expected: " + llGetSubString(body, 0, 120));
            return;
        }
        llSetText("Weather: " + cond + "  " + temp + " C", <1,1,1>, 1.0);
    }
}
```

**Notes and pitfalls**

- JSON numbers come back as strings from `llJsonGetValue`; cast explicitly.
  JSON `true/false/null`, nested arrays, and unicode escapes are the usual parse
  surprises — test with a deliberately malformed payload.
- OpenSim: HTTP request throttles, body limits, and header support differ by
  configuration, and `llJson*` implementations were historically the least
  SL-compatible part of OpenSim scripting (an Aurora-derived implementation was
  found "plain wrong" vs SL by OpenSim's own developers). Validate JSON behaviour
  on both grids if the script must run on both.
- Never put a secret API key in a script you distribute: anyone with modify
  permission (and in some cases just inspect rights workflows) can read script
  source in inventory. Proxy secrets through your own server endpoint instead.

---
## Example 7 — HTTP in: serving a small web page from a prim

**What it does:** Requests a public URL with `llRequestURL`, serves an HTML status
page and a tiny JSON endpoint from the prim itself via `http_request`, and releases
the URL cleanly. This is the basis of in-world web control panels, status boards,
and webhook receivers.

```lsl
// HTTP-in server. SL assigns a URL like:
//   http://simhost.agni.lindenlab.com:12046/cap/<uuid>
// URLs are per-region, change on region restart / object move between regions,
// and the total number per parcel/region is limited. Treat the URL as ephemeral
// and publish it somewhere (a web server, a notecard, chat) after acquiring it.

string gURL = "";
integer gHits = 0;

request_url()
{
    llReleaseURL(gURL);         // releasing an empty/invalid URL is harmless
    gURL = "";
    llRequestURL();
}

default
{
    state_entry() { request_url(); }

    http_request(key id, string method, string body)
    {
        if (method == URL_REQUEST_GRANTED)
        {
            gURL = body;
            llOwnerSay("Serving at: " + gURL);
            return;
        }
        if (method == URL_REQUEST_DENIED)
        {
            // No URLs left in this region/parcel quota, or HTTP-in disabled.
            // There is no retry that fixes quota: log it and stop hammering.
            llOwnerSay("URL denied: " + body);
            return;
        }

        // From here: a real inbound request. id is the REQUEST key, used to reply.
        ++gHits;
        string path = llGetHTTPHeader(id, "x-path-info");
        string query = llGetHTTPHeader(id, "x-query-string");

        if (path == "/status")
        {
            llHTTPResponse(id, 200, "{\"hits\":" + (string)gHits +
                           ",\"object\":\"" + llGetObjectName() + "\"}");
        }
        else
        {
            llHTTPResponse(id, 200,
                "<html><body><h1>" + llGetObjectName() + "</h1>" +
                "<p>Hits: " + (string)gHits + "</p>" +
                "<p>Try <a href=\"" + gURL + "/status\">/status</a></p>" +
                "</body></html>");
        }
        // You MUST call llHTTPResponse for every request (or the connection
        // hangs until timeout) — including for paths you do not recognise,
        // where a 404 response is the correct behaviour.
    }

    changed(integer change)
    {
        // Moving regions invalidates the URL. Re-request on region change.
        if (change & CHANGED_REGION) request_url();
    }

    on_rez(integer p) { request_url(); }
}
```

**Notes and pitfalls**

- Request bodies and headers have size limits; this is a control/status channel,
  not a file transfer protocol. Large payloads belong on `GetTexture`-style caps
  or an external server, not HTTP-in.
- Anyone who learns the URL can call it — the UUID in the path is the only
  "security". Add a shared-secret query parameter check for any state-changing
  endpoint, and rotate by re-requesting the URL.
- OpenSim: HTTP-in exists but URL form, quotas, and header names have differed
  between versions; the `x-path-info` / `x-query-string` headers above are the
  SL names. Test both.

---

## Example 8 — Dataserver notecard reader (streaming, the correct pattern)

**What it does:** Reads a notecard line by line using `llGetNotecardLine` and the
`dataserver` event, storing parsed `key=value` settings. This streaming pattern is
mandatory knowledge: there is no "read whole notecard" call, lines arrive one event
at a time, the end is signalled by the literal string `EOF`, and a changed notecard
invalidates every query key.

```lsl
// Config reader — notecard named "config" in the same prim, lines like:
//   colour=0.2,0.6,1.0
//   message=Welcome in!
//   # lines starting with # are comments
// Blank lines are skipped. Unknown keys are logged, not fatal.

string  NC_NAME = "config";
integer gLine = 0;
key     gQuery = NULL_KEY;

// Parsed settings with defaults, so a missing notecard degrades gracefully.
vector gColour = <0.2, 0.6, 1.0>;
string gMessage = "Welcome!";

start_read()
{
    if (llGetInventoryType(NC_NAME) != INVENTORY_NOTECARD)
    {
        llOwnerSay("No notecard named '" + NC_NAME + "' — using defaults.");
        return;
    }
    gLine = 0;
    gQuery = llGetNotecardLine(NC_NAME, gLine);
}

default
{
    state_entry() { start_read(); }

    dataserver(key query_id, string data)
    {
        // Match the query: other dataserver users (KVP, llGetNotecardLine from
        // another script is separate, but THIS script may add more later) must
        // not cross wires.
        if (query_id != gQuery) return;

        if (data == EOF)
        {
            llOwnerSay("Config loaded. colour=" + (string)gColour +
                       " message=" + gMessage);
            llSetColor(gColour, ALL_SIDES);
            return;     // done — do NOT request another line
        }

        string line = llStringTrim(data, STRING_TRIM);
        if (line != "" && llGetSubString(line, 0, 0) != "#")
        {
            integer eq = llSubStringIndex(line, "=");
            if (eq > 0)
            {
                string k = llStringTrim(llGetSubString(line, 0, eq - 1), STRING_TRIM);
                string v = llStringTrim(llGetSubString(line, eq + 1, -1), STRING_TRIM);
                if (k == "colour")       gColour = (vector)v;   // "(vector)" cast parses "<r,g,b>"
                else if (k == "message") gMessage = v;
                else llOwnerSay("Unknown config key: " + k);
            }
        }

        // Request the NEXT line. Forgetting this increment-and-request is the
        // #1 notecard bug: the script reads line 0 forever or stops silently.
        ++gLine;
        gQuery = llGetNotecardLine(NC_NAME, gLine);
    }

    changed(integer change)
    {
        // Editing the notecard (or adding/removing inventory) makes in-flight
        // query keys meaningless. Restart the read from line 0.
        if (change & CHANGED_INVENTORY) start_read();
    }

    touch_start(integer n) { llSay(0, gMessage); }
}
```

**Notes and pitfalls**

- Notecard lines are truncated at 255 bytes in SL. Long config values must be split
  or moved to another channel (HTTP, KVP).
- `(vector)v` casting a malformed string gives `ZERO_VECTOR`, silently. Validate
  before casting if black objects would be a problem.
- OpenSim: notecard line limits and dataserver timing are similar but not
  identical; asset-backed notecards in OpenSim can behave differently when the
  notecard is inside a coalesced object. Keep the EOF and query-key discipline —
  it is correct on both.

---

## Example 9 — Permissions: animation on request, done safely

**What it does:** Requests `PERMISSION_TRIGGER_ANIMATION` when an avatar touches
the object, waits for `run_time_permissions`, starts an animation, and stops it on
a second touch. Demonstrates the permission lifecycle that gates animation,
controls, attach, teleport, debit, and camera: request, asynchronous grant/deny,
silent denial, and revocation when the avatar stands/logs/detaches.

```lsl
// Animation player — touch to start/stop an animation on the toucher.
// The animation must be in the same prim's inventory (or use a built-in
// animation UUID — prefer inventory so permissions and names are explicit).

string  ANIM = "dance1";        // inventory animation name
key     gAvatar = NULL_KEY;
integer gPlaying = FALSE;

default
{
    touch_start(integer n)
    {
        key who = llDetectedKey(0);

        if (gPlaying && who == gAvatar)
        {
            llStopAnimation(ANIM);
            gPlaying = FALSE;
            gAvatar = NULL_KEY;
            llOwnerSay("Stopped.");
            return;
        }

        if (gPlaying) { llInstantMessage(who, "Busy right now."); return; }

        gAvatar = who;
        // Request permission FROM THE AVATAR (not the owner — llGetOwner()
        // here is the classic mistake; permissions come from the person the
        // script will act on).
        llRequestPermissions(who,
            PERMISSION_TRIGGER_ANIMATION | PERMISSION_TAKE_CONTROLS);
        // NOTE: nothing after this line may assume the animation is playing.
        // The grant arrives later, in run_time_permissions — or never.
    }

    run_time_permissions(integer perm)
    {
        // perm is the FULL granted bitmask, not a delta.
        if (perm & PERMISSION_TRIGGER_ANIMATION)
        {
            llStartAnimation(ANIM);
            gPlaying = TRUE;
            llOwnerSay("Animating " + llKey2Name(gAvatar));
        }
        else
        {
            // Denied, timed out, or the avatar clicked "No" — all look the
            // same from here. Clean up and do not retry in a loop.
            llOwnerSay("Animation permission not granted.");
            gAvatar = NULL_KEY;
        }
    }
}
```

**Notes and pitfalls**

- Permission bits to know by name: `PERMISSION_DEBIT` (money, see Example 12),
  `PERMISSION_TELEPORT`, `PERMISSION_ATTACH`, `PERMISSION_TAKE_CONTROLS`,
  `PERMISSION_CONTROL_CAMERA`, `PERMISSION_TRIGGER_ANIMATION`,
  `PERMISSION_OVERRIDE_ANIMATIONS`, `PERMISSION_CHANGE_LINKS`,
  `PERMISSION_RETURN_OBJECTS`, `PERMISSION_TRACK_CAMERA`.
- Granting is per-script, per-avatar, and revocable; permissions do not survive
  the avatar leaving, and in experiences (Example 13) they can be pre-granted
  grid-wide for that experience.
- OpenSim: permission prompts and experience-based auto-grant differ; some OpenSim
  configurations auto-grant for the parcel owner, which hides missing-request bugs
  that then fail on Agni. Always test the deny path.

---

## Example 10 — Timer patterns: heartbeat, countdown, and one-shot alarms

**What it does:** Shows the three timer shapes you actually need — a repeating
heartbeat with `llSetTimerEvent`, a countdown that displays remaining time and
fires once at zero, and the correct way to have multiple logical timers in a
language that gives you exactly ONE hardware timer per script.

```lsl
// Multi-timer pattern — ONE llSetTimerEvent, many logical deadlines.
// Rule: the hardware timer ticks at the SHORTEST interval any subsystem needs;
// each subsystem stores its own next-fire unix time and checks it in timer().

integer TICK = 1;                       // 1-second tick drives everything below
integer gCountdownEnd = 0;              // 0 = countdown not running
integer gNextHeartbeat = 0;
integer HEARTBEAT_PERIOD = 30;

default
{
    state_entry()
    {
        llSetTimerEvent((float)TICK);
        gNextHeartbeat = llGetUnixTime() + HEARTBEAT_PERIOD;
        llOwnerSay("Touch to start a 10-second countdown.");
    }

    touch_start(integer n)
    {
        gCountdownEnd = llGetUnixTime() + 10;
    }

    timer()
    {
        integer now = llGetUnixTime();

        if (gCountdownEnd)
        {
            integer remain = gCountdownEnd - now;
            if (remain <= 0)
            {
                llSay(0, "Time!");
                llSetText("", ZERO_VECTOR, 0.0);
                gCountdownEnd = 0;
            }
            else
            {
                llSetText("T-" + (string)remain, <1,1,0>, 1.0);
            }
        }

        if (now >= gNextHeartbeat)
        {
            gNextHeartbeat = now + HEARTBEAT_PERIOD;
            // Heartbeat work goes here: sensor refresh, URL health check,
            // stats flush. Keep it SHORT: a long timer() handler delays every
            // other event in this script.
            llOwnerSay("heartbeat " + llGetTimestamp());
        }
    }
}
```

**Notes and pitfalls**

- `llSleep()` inside an event handler blocks the whole script's event queue for
  that duration; a `llSleep(60)` in `touch_start` means a minute of dead object.
  Use timer deadlines instead — this example exists because that mistake is
  everywhere.
- Timer resolution: SL timers are not real-time precise (minimum ~0.05 s,
  granularity coarser under load). OpenSim XEngine timers and `llSleep` semantics
  differ noticeably from SL; YEngine is closer. Never build a clock that must be
  accurate to the second across grids on `llSetTimerEvent` alone — anchor to
  `llGetUnixTime()` as this example does.
- Calling `llSetTimerEvent(0.0)` stops the timer. Forgetting that after a feature
  is disabled leaves a script waking forever for nothing, which adds up across a
  region.

---
## Example 11 — Sensor door: sliding door with obstruction handling

**What it does:** A sliding door that opens when an avatar approaches, closes after
the doorway is clear, moves smoothly with `llSetPos` steps driven by a timer, and
reverses if someone is standing in the doorway. Combines sensor events, a movement
state machine, and the physics caveat that a moving prim will push avatars.

```lsl
// Sliding door — one prim, moves sideways along its local X by DOOR_TRAVEL.
// Put this script in the door prim. The door's CLOSED position is wherever it
// is when the script starts (captured in state_entry), which is how real door
// scripts avoid hard-coded region coordinates.

vector  gClosedPos;
float   DOOR_TRAVEL = 1.1;      // metres to slide open
float   STEP = 0.11;            // per-tick movement; smaller = smoother = slower
integer gOpenAmount = 0;        // 0..10 steps open
integer gWantOpen = FALSE;
integer gClearSince = 0;        // unix time the doorway was last seen clear

default
{
    state_entry()
    {
        gClosedPos = llGetPos();
        llSensorRepeat("", NULL_KEY, AGENT, 2.5, PI, 0.5);
        llSetTimerEvent(0.1);   // movement tick
    }

    sensor(integer n)
    {
        gWantOpen = TRUE;
        gClearSince = llGetUnixTime();
    }

    no_sensor()
    {
        // Only start wanting to close after 2 s of nobody detected, so a
        // person pausing in the doorway does not get the door in the back.
        if (llGetUnixTime() - gClearSince >= 0 && !gWantOpen) return;
        gWantOpen = FALSE;
    }

    timer()
    {
        integer target = 0;
        if (gWantOpen) target = 10;

        if (gOpenAmount < target) ++gOpenAmount;
        else if (gOpenAmount > target) --gOpenAmount;
        else return;            // at rest; nothing to do this tick

        vector pos = gClosedPos;
        pos.x += DOOR_TRAVEL * ((float)gOpenAmount / 10.0);
        // WARNING: llSetPos is limited to 10 m per call and respects the
        // prim's physics state. A PHYSICAL door prim will collide and can
        // fail to move (or shove avatars). Doors are normally non-physical
        // and use llSetPos / llSetLinkPrimitiveParamsFast like this.
        llSetPos(pos);
    }

    changed(integer change)
    {
        // If the build is moved by hand, re-capture "closed" on next reset
        // rather than fighting the builder. Simpler and predictable:
        if (change & CHANGED_REGION) llResetScript();
    }
}
```

**Notes and pitfalls**

- For multi-prim doors, move with `llSetLinkPrimitiveParamsFast([PRIM_POS_LOCAL])`
  relative to the root instead of region `llSetPos`; mixing the two is a top cause
  of doors ending up in the neighbour's parcel.
- Sensor on a 0.5 s repeat is responsive but costs script time; doors are a place
  where `llSensorRepeat` + collision volumes (`collision_start` on an invisible
  trigger prim) are both legitimate — the trigger-prim version reacts faster.
- OpenSim: sensor event batching and max detections differ; the 2-second doorway
  grace in this script hides most of that difference, which is deliberate.

---

## Example 12 — Vendor with money() and PERMISSION_DEBIT safety

**What it does:** A single-item vendor: sets a pay price, requests
`PERMISSION_DEBIT` from its owner at startup and REFUSES to operate without it,
delivers the item on payment in `money()`, refunds on delivery failure, and logs
every transaction. This is the highest-stakes pattern in LSL — a debit-permission
script can take Linden dollars from its owner — so the safety structure is the
example, not decoration.

```lsl
// Vendor — sells ITEM_NAME for PRICE. Safety rules implemented below:
//  1. No PERMISSION_DEBIT, no vending. The script sits inert and says why.
//  2. Exact-change only: overpayment is refunded down to PRICE automatically.
//  3. Delivery is attempted BEFORE money is considered "kept"; if the item
//     is missing from inventory, the buyer is refunded in full.
//  4. Every transaction is logged to the owner with buyer, amount, result.
//  5. llGiveMoney is NEVER called on an unverified key or amount.

string  ITEM_NAME = "My Product v1.0";
integer PRICE = 250;            // L$
integer gHaveDebit = FALSE;

default
{
    state_entry()
    {
        llSetPayPrice(PRICE, [PRICE, PAY_UNPAYABLE, PAY_UNPAYABLE, PAY_UNPAYABLE]);
        llSetText(ITEM_NAME + "\nL$" + (string)PRICE, <1,1,1>, 1.0);

        if (llGetPermissions() & PERMISSION_DEBIT)
        {
            gHaveDebit = TRUE;
            llOwnerSay("Vendor ready (debit permission already held).");
        }
        else
        {
            // Request from the OWNER — debit permission is the owner's money.
            llRequestPermissions(llGetOwner(), PERMISSION_DEBIT);
            llOwnerSay("Vendor requesting DEBIT permission. Accept the prompt " +
                       "or this vendor will not sell anything.");
        }
    }

    run_time_permissions(integer perm)
    {
        if (perm & PERMISSION_DEBIT)
        {
            gHaveDebit = TRUE;
            llOwnerSay("Debit granted. Vendor live.");
        }
        else
        {
            gHaveDebit = FALSE;
            llOwnerSay("Debit NOT granted. Vendor disabled by design.");
        }
    }

    money(key buyer, integer amount)
    {
        // money() fires after the payment cleared. buyer is who paid.
        if (!gHaveDebit)
        {
            // Should be unreachable (pay price is set), but if it happens the
            // only safe action is a full refund attempt and a loud log line.
            llOwnerSay("PAYMENT WITHOUT DEBIT PERMISSION from " + llKey2Name(buyer));
            return;
        }

        if (llGetInventoryType(ITEM_NAME) == INVENTORY_NONE)
        {
            // Item deleted/renamed after the vendor was set up. Refund & log.
            llGiveMoney(buyer, amount);
            llInstantMessage(buyer, "Sorry — that item is out of stock. You have been refunded.");
            llOwnerSay("REFUNDED " + (string)amount + " to " + llKey2Name(buyer) +
                       " (item missing from inventory!)");
            return;
        }

        if (amount > PRICE)
        {
            llGiveMoney(buyer, amount - PRICE);   // return the overpayment
        }
        else if (amount < PRICE)
        {
            // Pay-price UI normally prevents this; scripts and gifts can not
            // underpay via the pay dialog, so treat underpayment as a bug.
            llGiveMoney(buyer, amount);
            llOwnerSay("REFUNDED underpayment " + (string)amount + " from " + llKey2Name(buyer));
            return;
        }

        llGiveInventory(buyer, ITEM_NAME);
        llInstantMessage(buyer, "Thank you for your purchase of " + ITEM_NAME + ".");
        llOwnerSay("SOLD " + ITEM_NAME + " to " + llKey2Name(buyer) +
                   " for L$" + (string)PRICE);
    }

    changed(integer change)
    {
        // Permissions are lost on ownership change; re-run the whole gate.
        if (change & CHANGED_OWNER) llResetScript();
        // If the product is removed, warn immediately instead of at sale time.
        if ((change & CHANGED_INVENTORY) &&
            llGetInventoryType(ITEM_NAME) == INVENTORY_NONE)
            llOwnerSay("WARNING: vendor item '" + ITEM_NAME + "' no longer in inventory.");
    }
}
```

**Notes and pitfalls**

- `PERMISSION_DEBIT` is the classic scam vector in freebie scripts: a script with
  debit permission can call `llGiveMoney` / transfer functions against the owner's
  balance. Only grant it to scripts you wrote or trust, and audit any vendor you
  buy for hidden `llGiveMoney` calls. In this script every `llGiveMoney` call is a
  refund to a verified buyer — that shape is what "safe" looks like.
- `money()` gives you no transaction ID; for real commerce, pair the vendor with an
  external server log via `llHTTPRequest` (Example 6) keyed by buyer + timestamp.
- OpenSim: currency may be a local module (or none) rather than Linden dollars;
  `money()` and debit semantics follow the grid's money module, and on a standalone
  with no money module this example cannot be tested meaningfully. Test money code
  on Aditi, where L$ test balances exist for this purpose.
- `llSetPayPrice` quick-pay buttons: `PAY_HIDE` / `PAY_UNPAYABLE` constants control
  which buttons show; leaving default prices enabled on a vendor is how accidental
  L$1 sales happen.

---

## Example 13 — Experience tools: pre-granted permissions and teleport

**What it does:** Uses an SL Experience: requests experience permissions (which the
user grants once for the whole experience, instead of per-object prompts), then
teleports the avatar to a landmark when they touch the pad. Shows
`llRequestExperiencePermissions`, the `experience_permissions` /
`experience_permissions_denied` events, and the error codes for denial reasons.

```lsl
// Experience teleporter — the SCRIPT must be compiled with an Experience
// selected (in the viewer script editor) and the Experience must be allowed
// on the land, or llRequestExperiencePermissions fails with an error event.
// Denial reasons arrive as integer codes in experience_permissions_denied:
//   1 = experience not found / not associated, 2 = not allowed on this land,
//   3 = no permission (user blocked/declined), 4 = user not in experience
//   scope / not opted in, 5 = experience suspended, others = retry later.

vector DEST_POS = <128.0, 128.0, 30.0>;   // region-local landing point
string DEST_LOOK = "0";                    // simplified: keep facing north

default
{
    state_entry()
    {
        llSitTarget(ZERO_VECTOR, ZERO_ROTATION); // clear any stray sit target
        llSetText("Touch: teleport (Experience)", <0.8,0.8,1>, 1.0);
    }

    touch_start(integer n)
    {
        key who = llDetectedKey(0);
        // For an experience-compiled script this may return immediately with
        // permissions already held; otherwise the user sees ONE prompt for
        // the experience, not one per object.
        llRequestExperiencePermissions(who, "");
    }

    experience_permissions(key avatar)
    {
        // Granted (now or previously). Teleport is an experience-privileged
        // action: llTeleportAgent requires this grant (or PERMISSION_TELEPORT
        // via the classic path in an experience context).
        llTeleportAgent(avatar, "", DEST_POS, (vector)DEST_LOOK);
        llInstantMessage(avatar, "Teleporting you now.");
    }

    experience_permissions_denied(key avatar, integer reason)
    {
        llInstantMessage(avatar,
            "Teleport needs Experience permission (reason " + (string)reason +
            "). Touch again and accept, or use the landmark instead.");
        llOwnerSay("Experience permission denied for " + llKey2Name(avatar) +
                   " reason=" + (string)reason);
    }
}
```

**Notes and pitfalls**

- Experiences are SL-only. OpenSim has no equivalent system; an experience script
  ported to OpenSim needs the classic `llRequestPermissions` flow (Example 9) and
  `osTeleportAgent` if OSSL is enabled for that user — which is threat-level gated
  (Example in secondlife_lsl_scripting skill), so the port is conditional, not
  mechanical.
- Land scope is the silent failure: an experience not enabled on the parcel makes
  every request fail with reason 2 while the script looks correct. Check land
  settings before debugging code.
- `llTeleportAgent` with an empty landmark string and a local position is a
  same-region teleport; cross-region uses a landmark name from inventory.

---

## Example 14 — Pathfinding character with llCastRay scouting

**What it does:** Two cooperating pieces in one script for teaching clarity: a
pathfinding character (SL's navmesh character system: `llCreateCharacter`,
`llNavigateTo`, arrival via `path_update`) and a raycast scout that uses
`llCastRay` to find the ground/obstacle in front of the object. Pathfinding
characters are how SL NPCs and pets walk without physics hacks.

```lsl
// Wandering character — requires: the object contains this script, the region
// has a baked navmesh (estate/region setting), and the object is set as a
// character once at startup. Character options (speed, turn speed, vertical
// separation) are set at creation and in llUpdateCharacter.

list WAYPOINTS = [<120,120,22>, <135,118,22>, <128,132,22>];
integer gWp = 0;

default
{
    state_entry()
    {
        // llExecCharacter / character calls require the object NOT be an
        // attachment and work best on a dedicated root prim.
        llCreateCharacter([CHARACTER_DESIRED_SPEED, 2.0,
                           CHARACTER_RADIUS, 0.4,
                           CHARACTER_LENGTH, 1.2,
                           CHARACTER_ORIENTATION, VERTICAL,
                           CHARACTER_AVOIDANCE_MODE, AVOID_CHARACTERS | AVOID_DYNAMIC_OBSTACLES,
                           CHARACTER_TYPE, CHARACTER_TYPE_A]);
        go_next();
    }

    go_next()
    {
        vector target = llList2Vector(WAYPOINTS, gWp);
        // PURSUE / NAVIGATE options: TRAVERSAL_TYPE, CHARACTER_DESIRED_TURN_SPEED...
        llNavigateTo(target, [FORCE_DIRECT_PATH, FALSE]);
    }

    path_update(integer update)
    {
        // update codes: PU_GOAL_REACHED, PU_SLOWDOWN_DISTANCE_REACHED,
        // PU_GOAL_BLOCKED, PU_FAILURE_INVALID_START, PU_FAILURE_INVALID_GOAL,
        // PU_FAILURE_UNREACHABLE, PU_FAILURE_TARGET_GONE, PU_EVADE_HIDDEN,
        // PU_EVADE_SPOTTED, PU_FAILURE_NO_VALID_DESTINATION, PU_FAILURE_NO_NAVMESH.
        if (update == PU_GOAL_REACHED)
        {
            gWp = (gWp + 1) % llGetListLength(WAYPOINTS);
            go_next();
        }
        else if (update == PU_FAILURE_NO_NAVMESH || update == PU_GOAL_BLOCKED ||
                 update == PU_FAILURE_UNREACHABLE)
        {
            // Do not retry in a hot loop against a blocked goal: skip ahead.
            llOwnerSay("Path failed code=" + (string)update + ", skipping waypoint.");
            gWp = (gWp + 1) % llGetListLength(WAYPOINTS);
            go_next();
        }
    }

    touch_start(integer n)
    {
        // Raycast scout: cast from 2 m in front of the object, downward-biased,
        // and report the first hit. llCastRay returns a strided list of
        // [key, hit_pos] pairs, terminated by status in the last element when
        // RC_GET_ROOT_PRIM style options are used; the simple form below uses
        // the documented default return shape.
        vector pos = llGetPos();
        vector fwd = llRot2Fwd(llGetRot());
        list hits = llCastRay(pos + fwd * 2.0 + <0,0,1.0>,
                              pos + fwd * 12.0 + <0,0,-1.0>,
                              [RC_REJECT_TYPES, RC_REJECT_AGENTS | RC_REJECT_PHYSICAL,
                               RC_DETECT_PHANTOM, FALSE, RC_MAX_HITS, 3]);
        integer status = llList2Integer(hits, -1);
        llOwnerSay("raycast status=" + (string)status +
                   " hits=" + (string)(llGetListLength(hits) / 2));
        if (llGetListLength(hits) >= 2)
            llOwnerSay("first hit at " + llList2String(hits, 1));
    }

    on_rez(integer p) { llResetScript(); }  // characters must be re-created after rez
}
```

**Notes and pitfalls**

- Pathfinding is SL-only and region-dependent: no baked navmesh, no characters.
  OpenSim has NPCs via OSSL (`osNpcCreate` etc.) instead — a completely different
  API. A "pet" product that must run on both grids is two implementations behind
  one link_message interface (Example 5), not one script.
- `llCastRay` is throttled per object/region and returns asynchronously expensive
  results; scout on touch or a slow timer, never per-frame.
- Character creation fails silently-ish if the object is attached, is a child in
  some configurations, or the region disables pathfinding. Log `path_update`
  failures during development, as above.

---
## Example 15 — Texture animation, scrolling, and per-face media basics

**What it does:** Animates a texture on one face with `llSetTextureAnim` (scroll
mode for a waterfall/conveyor look), cycles texture offsets, and toggles animation
off cleanly. Texture animation is client-side and free of script cost after setup —
which is exactly why it is preferred over timer-driven texture swapping.

```lsl
// Waterfall — ANIM_ON | SMOOTH | LOOP scrolling texture on face 2.
// Modes (bitwise): ANIM_ON, LOOP, REVERSE, PING_PONG, SMOOTH, ROTATE, SCALE.
// Types: standard texture anim affects offset/rotation/scale of the face's
// texture in the viewer; the script only sends the parameters once.

integer FACE = 2;
integer gRunning = FALSE;

default
{
    state_entry()
    {
        llOwnerSay("Touch to start/stop the waterfall.");
    }

    touch_start(integer n)
    {
        gRunning = !gRunning;
        if (gRunning)
        {
            // llSetTextureAnim(mode, face, sizex, sizey, start, length, rate)
            // For SMOOTH scroll: sizex/sizey describe the texture grid used
            // for frame modes; in smooth scroll the RATE is in texture
            // repeats per second along the animation direction set by the
            // face's texture rotation. Negative rate scrolls the other way.
            llSetTextureAnim(ANIM_ON | SMOOTH | LOOP, FACE, 1, 1, 0.0, 1.0, 0.75);
        }
        else
        {
            // ANIM_ON off. Also reset the offset, or the texture stays frozen
            // mid-scroll at a random offset — the visible "stuck waterfall".
            llSetTextureAnim(0, FACE, 1, 1, 0.0, 1.0, 0.0);
            llSetTextureOffset(FACE, <0.0, 0.0>);
        }
    }
}
```

**Notes and pitfalls**

- Texture animation state is a prim property, not script state: it persists if the
  script is removed, and a new owner inherits your waterfall. Reset it in products
  on `changed(CHANGED_OWNER)` if that is not intended.
- Frame-based animation (`sizex` × `sizey` sprite sheets) and SMOOTH scroll share
  this one call with different mode flags — confusing them is the usual reason an
  animation "does nothing": a sprite sheet without `ANIM_ON|LOOP` frame settings
  just sits on frame 0.
- OpenSim supports texture anim; rates and smoothness are viewer-rendered in both
  worlds, so perceived speed is the same — one of the few truly portable features.

---

## Example 16 — Sit target and pose handling (the changed-link dance)

**What it does:** A chair: sets a sit target with `llSitTarget`, detects who sat
via `changed(CHANGED_LINK)`, starts a pose animation with the sitter's permission
flow appropriate to seated avatars, unsits cleanly, and handles the avatar
standing mid-pose. Sit handling is where permission, link, and animation knowledge
all meet.

```lsl
// Chair — sit pose with correct sit/stand detection.
// Key facts this code encodes:
//  * No llSitTarget = no sitting (the avatar gets "no sit target" behaviour
//    and llAvatarOnSitTarget() never returns them).
//  * Sitting makes the avatar a LINK in the linkset. changed(CHANGED_LINK)
//    fires; llGetNumberOfPrims() grows by 1 per seated avatar.
//  * llAvatarOnSitTarget() is THE way to ask "who is on my sit target".

string POSE = "sit_pose";       // animation in this prim's inventory
key    gSitter = NULL_KEY;

default
{
    state_entry()
    {
        // Position is LOCAL to this prim; rotation orients the avatar.
        // Tune by eye: <0,0,0.45> above the prim centre is a starting point
        // for a simple cube chair, never a universal constant.
        llSitTarget(<0.0, 0.0, 0.45>, ZERO_ROTATION);
    }

    changed(integer change)
    {
        if (!(change & CHANGED_LINK)) return;

        key sitter = llAvatarOnSitTarget();
        if (sitter != NULL_KEY && gSitter == NULL_KEY)
        {
            gSitter = sitter;
            // A seated avatar has implicitly granted animation permission
            // flows via llRequestPermissions in the normal way; sitting does
            // NOT auto-grant TRIGGER_ANIMATION for arbitrary scripts, so ask.
            llRequestPermissions(sitter, PERMISSION_TRIGGER_ANIMATION);
        }
        else if (sitter == NULL_KEY && gSitter != NULL_KEY)
        {
            // They stood up (or left/logged). Stop the pose if we still can;
            // llStopAnimation on a departed avatar is a harmless no-op error
            // path — do not build logic that requires it to succeed.
            if (llGetPermissions() & PERMISSION_TRIGGER_ANIMATION)
                llStopAnimation(POSE);
            gSitter = NULL_KEY;
        }
    }

    run_time_permissions(integer perm)
    {
        if ((perm & PERMISSION_TRIGGER_ANIMATION) && gSitter != NULL_KEY)
        {
            // Stop the default sit first or the two animations fight and the
            // result depends on animation priorities — the classic "pose
            // looks broken" bug. Built-in sit animations have known names;
            // stopping "sit" is the common case for chairs.
            llStopAnimation("sit");
            llStartAnimation(POSE);
        }
    }

    touch_start(integer n)
    {
        // Owner touch = eject: llUnSit is the polite, permission-free way for
        // an object to stand its OWN sitter up in most furniture contexts.
        if (llDetectedKey(0) == llGetOwner() && gSitter != NULL_KEY)
            llUnSit(gSitter);
    }
}
```

**Notes and pitfalls**

- Animation priority decides fights: a priority-4 pose overrides the default sit;
  a priority-1 pose loses. If stopping `"sit"` does not fix a pose, the pose
  asset's priority is the problem, not your script.
- Multiple sit targets in one linkset (sofas, pose stands) need one handler script
  per target prim or careful `llAvatarOnLinkSitTarget(link)` bookkeeping.
- OpenSim sit offsets and the default sit animation names are similar but the
  un-sit and permission behaviour around attachments differs; test the stand-up
  path specifically, it is where ports break.

---

## Example 17 — Rezzer with on_rez parameter communication

**What it does:** Rezzes an object from inventory with `llRezObject`, passes it a
startup parameter, and the rezzed object's `on_rez` uses that parameter to fetch
its configuration channel from the rezzer via a region chat handshake. This is the
foundation of every scene rezzer, holodeck, and vendor demo system.

```lsl
// ---- Rezzer script ----
string  PROP = "chair_prop";    // must be in this prim's inventory, copyable
integer gSession = 0;           // increments per rez; passed as start_param
key     gLastRezzed = NULL_KEY;

default
{
    touch_start(integer n)
    {
        ++gSession;
        vector pos = llGetPos() + <0.0, 0.0, 1.0>;
        // start_param is an INTEGER only. Anything richer (a channel, a mode)
        // must be derived from it by agreement, as the prop script below does:
        // channel = BASE - start_param. That convention is the whole protocol.
        llRezObject(PROP, pos, ZERO_VECTOR, llGetRot(), gSession);
    }

    object_rez(key id)
    {
        // Fires in the REZZER when the object actually appears, with its key.
        // llRezObject returning means "request accepted", not "object exists".
        gLastRezzed = id;
        llOwnerSay("Rezzed " + llKey2Name(id) + " session " + (string)gSession);
    }
}
```

```lsl
// ---- Prop script (inside the rezzed object) ----
integer BASE_CHAN = -770000;

default
{
    on_rez(integer start_param)
    {
        if (start_param == 0)
        {
            // Rezzed by hand from inventory, not by the rezzer: behave as a
            // plain standalone prop and do not listen for session commands.
            return;
        }
        integer chan = BASE_CHAN - start_param;
        llListen(chan, "", NULL_KEY, "");
        llOwnerSay("Prop up, session " + (string)start_param +
                   ", listening on " + (string)chan);
        // Die with the session: if the rezzer goes away the prop should not
        // linger. A common pattern is llSetTimerEvent + llDie() on a lease;
        // omitted here to keep the handshake readable, required in production.
    }

    listen(integer channel, string name, key id, string msg)
    {
        if (msg == "die") llDie();
        if (msg == "reset") llResetScript();
    }
}
```

**Notes and pitfalls**

- `llRezObject` has a 0.1 s delay and inventory/permission failure is silent in the
  rezzer except for missing `object_rez`. Always log `object_rez` during setup.
- The start parameter is one integer — protocols that need more pass a channel or
  a KVP key derived from it, as here. Do not try to smuggle strings through it.
- OpenSim: `llRezObject` / `osRezObject` behaviours and `object_rez` timing are
  close, but coalesced returns and god-mode rezzing differ. The handshake pattern
  ports; exact timing does not.

---

## Example 18 — Collision events, volume detect, and a welcome mat

**What it does:** A welcome mat that greets avatars who step on it using
`collision_start`, with a per-avatar cooldown so standing and shifting on the mat
does not retrigger it, plus the `llVolumeDetect` alternative explained for
walk-through triggers that must not physically block anyone.

```lsl
// Welcome mat — collision_start with cooldown map (two parallel lists:
// LSL's substitute for a dictionary).

list gLastGreetKeys = [];
list gLastGreetTimes = [];
integer COOLDOWN = 60;          // seconds per avatar

integer cooldown_ok(key who)
{
    integer idx = llListFindList(gLastGreetKeys, [who]);
    integer now = llGetUnixTime();
    if (idx == -1)
    {
        gLastGreetKeys += [who];
        gLastGreetTimes += [now];
        return TRUE;
    }
    if (now - llList2Integer(gLastGreetTimes, idx) >= COOLDOWN)
    {
        gLastGreetTimes = llListReplaceList(gLastGreetTimes, [now], idx, idx);
        return TRUE;
    }
    return FALSE;
}

default
{
    state_entry()
    {
        // OPTION A (this script): the mat is a normal solid prim; avatars
        // physically step onto it and collision_start fires.
        // OPTION B: call llVolumeDetect(TRUE) — the prim becomes phantom for
        // physics but generates collision events for avatars walking THROUGH
        // its volume. Use B for doorways and tripwires, A for floor mats.
        // A volume-detect prim must not be the root of a physical linkset.
        llSetTimerEvent(300.0);   // drives the list-pruning timer() below
        llOwnerSay("Welcome mat live.");
    }

    collision_start(integer n)
    {
        integer i;
        for (i = 0; i < n; ++i)
        {
            // Collisions include objects! Filter to avatars: llDetectedType
            // AGENT bit, or compare against llDetectedKey of known agents.
            if (llDetectedType(i) & AGENT)
            {
                key who = llDetectedKey(i);
                if (cooldown_ok(who))
                    llInstantMessage(who, "Welcome! Mind the step.");
            }
        }
    }

    // Periodic hygiene: without pruning, the two lists grow forever and every
    // llListFindList scan gets slower for the life of the script.
    timer()
    {
        integer now = llGetUnixTime();
        integer i = llGetListLength(gLastGreetKeys) - 1;
        for (; i >= 0; --i)
        {
            if (now - llList2Integer(gLastGreetTimes, i) > COOLDOWN * 4)
            {
                gLastGreetKeys = llDeleteSubList(gLastGreetKeys, i, i);
                gLastGreetTimes = llDeleteSubList(gLastGreetTimes, i, i);
            }
        }
    }
}
```

**Notes and pitfalls**

- The pruning `timer()` only runs because `state_entry` calls
  `llSetTimerEvent(300.0)`. A `timer()` handler with no timer ever set is dead
  code that looks alive — one of the easiest LSL bugs to ship.
- Collision events are throttled by the simulator and are not a physics engine:
  fast-moving avatars can tunnel through thin mats. Make trigger volumes thick.
- OpenSim collision reporting with ubODE vs BulletSim differs in edge cases
  (resting contact refiring is the classic). The cooldown map makes this script
  robust to both.

---
## Example 19 — Attachment and controls: a simple HUD-style attachment

**What it does:** An attachment that detects attach/detach, requests
`PERMISSION_TAKE_CONTROLS`, reads movement keys in the `control` event, and
releases controls cleanly on detach. The core pattern for vehicles, HUD clickers,
AO (animation override) attachments, and movement enhancers.

```lsl
// Attachment controller — attach to try. Arrow/letter movement keys are
// reported to the OWNER while attached. Demonstrates:
//   attach(key id)        id != NULL_KEY on attach, NULL_KEY on detach
//   PERMISSION_TAKE_CONTROLS + control() event levels/edges
//   llReleaseControls()   mandatory politeness on detach

integer gControlsHeld = FALSE;

default
{
    state_entry()
    {
        // On script start inside an ALREADY worn attachment, attach() does
        // not fire again. llGetAttached() != 0 tells us we are worn.
        if (llGetAttached() != 0)
            llRequestPermissions(llGetOwner(), PERMISSION_TAKE_CONTROLS);
    }

    attach(key id)
    {
        if (id != NULL_KEY)
        {
            llRequestPermissions(id, PERMISSION_TAKE_CONTROLS);
        }
        else
        {
            // Detaching: permissions vanish with the detach, but release
            // explicitly so a re-attach in the same session starts clean.
            if (gControlsHeld) llReleaseControls();
            gControlsHeld = FALSE;
        }
    }

    run_time_permissions(integer perm)
    {
        if (perm & PERMISSION_TAKE_CONTROLS)
        {
            // Take ONLY the controls you use. Taking CONTROL_ML_LBUTTON or
            // rotation controls you do not need breaks the user's camera and
            // other attachments' expectations.
            llTakeControls(CONTROL_FWD | CONTROL_BACK | CONTROL_LEFT |
                           CONTROL_RIGHT | CONTROL_UP | CONTROL_DOWN,
                           TRUE, FALSE);
            gControlsHeld = TRUE;
        }
    }

    control(key id, integer level, integer edge)
    {
        // level = controls currently held down; edge = controls that CHANGED
        // this frame (pressed or released since last event). Use edge for
        // one-shot actions (jump, fire), level for continuous (movement).
        integer pressed = level & edge;
        if (pressed & CONTROL_FWD)  llOwnerSay("forward pressed");
        if (pressed & CONTROL_UP)   llOwnerSay("up/jump pressed");
        // Continuous example: while FWD is held, level has the bit every event.
    }
}
```

**Notes and pitfalls**

- `control` events arrive at a high rate while keys are held; keep the handler
  tiny or the script's event queue backs up and chat/dialog events feel laggy.
- Attach points matter for HUDs: this example is a world attachment. HUD attach
  points (ATTACH_HUD_*) render on screen and use `llSetPos` in HUD space.
- OpenSim: control event rates and attach permission prompts differ slightly;
  vehicles tuned by ear on OpenSim often feel twitchy on Agni for this reason.

---

## Example 20 — Particle system: a campfire emitter you can reason about

**What it does:** A toggleable particle fire using `llParticleSystem` with the
full parameter list annotated — burst rate, age, velocity cone, gravity (buoyancy
via `PSYS_PART_ACCEL`), colour fade, size shrink, and texture from inventory.
Particles are viewer-rendered; the script sends parameters once.

```lsl
// Campfire particles — touch toggles. Every parameter is commented because
// llParticleSystem lists are write-only soup without them.

integer gOn = FALSE;

fire(integer on)
{
    if (!on)
    {
        llParticleSystem([]);   // empty list = emitter off. Always provide an
                                // explicit off path; removing the script also
                                // stops particles, confusing new owners.
        return;
    }
    llParticleSystem([
        PSYS_SRC_PATTERN, PSYS_SRC_PATTERN_EXPLODE,   // burst outward pattern
        PSYS_SRC_TEXTURE, "flame_tex",                // inventory texture name;
                                                      // "" = default particle blob
        PSYS_PART_START_COLOR, <1.0, 0.55, 0.15>,     // orange
        PSYS_PART_END_COLOR,   <0.45, 0.05, 0.0>,     // deep red fade
        PSYS_PART_START_ALPHA, 0.85,
        PSYS_PART_END_ALPHA,   0.0,                   // fade out, not pop out
        PSYS_PART_START_SCALE, <0.35, 0.35, 0.0>,
        PSYS_PART_END_SCALE,   <0.05, 0.05, 0.0>,     // shrink as they rise
        PSYS_PART_MAX_AGE,     1.4,                   // seconds per particle
        PSYS_SRC_MAX_AGE,      0.0,                   // 0 = emitter never expires
        PSYS_SRC_BURST_RATE,   0.06,                  // seconds between bursts
        PSYS_SRC_BURST_PART_COUNT, 4,                 // particles per burst
        PSYS_SRC_BURST_RADIUS, 0.15,                  // spawn radius
        PSYS_SRC_BURST_SPEED_MIN, 0.35,
        PSYS_SRC_BURST_SPEED_MAX, 0.7,
        PSYS_SRC_ANGLE_BEGIN,  0.0,                   // cone: narrow upward cone
        PSYS_SRC_ANGLE_END,    0.35,
        PSYS_PART_ACCEL,       <0.0, 0.0, 0.55>,      // upward accel = buoyancy
        PSYS_PART_FLAGS, PSYS_PART_EMISSIVE_MASK |    // fullbright particles
                         PSYS_PART_INTERP_COLOR_MASK |
                         PSYS_PART_INTERP_SCALE_MASK |
                         PSYS_PART_FOLLOW_SRC_MASK
    ]);
}

default
{
    touch_start(integer n)
    {
        gOn = !gOn;
        fire(gOn);
    }
}
```

**Notes and pitfalls**

- Particle count is a viewer performance budget shared by the whole scene. A
  "realistic" emitter at thousands of particles per second makes nearby avatars'
  viewers drop other emitters — including their own HUD effects.
- `PSYS_SRC_TARGET_KEY` can aim particles at an avatar/object; ribbon and
  wind flags (`PSYS_PART_WIND_MASK`, ribbon in newer viewers) change behaviour
  dramatically and are viewer-dependent. Keep to the portable flag set above for
  products.
- OpenSim renders the same parameter set through the same viewers, so particles
  are portable; emitter *prim* behaviour (e.g. in coalesced returns) is not
  identical. Minor.

---

## Example 21 — Experience KVP: persistent counters that survive the object

**What it does:** Uses Experience Key-Value storage (`llCreateKeyValue`,
`llUpdateKeyValue`, `llReadKeyValue`) to keep a visit counter that persists even
if the object is deleted and re-rezzed. All KVP operations are asynchronous and
report through `dataserver`, sharing that event with notecard reads — the query
key discipline from Example 8 becomes essential here.

```lsl
// Visit counter in Experience KVP.
// Key format is your design: "visits:<avatar uuid>" per visitor here.
// KVP values are STRINGS. KVP keys are limited in length and character set
// (keep to letters, digits, and :._- style separators), and total experience
// storage is quota-limited — KVP is a key-value store, not a database.

key gPendingRead = NULL_KEY;
key gPendingWrite = NULL_KEY;
key gVisitor = NULL_KEY;

default
{
    touch_start(integer n)
    {
        gVisitor = llDetectedKey(0);
        // Read-then-increment: KVP has no atomic increment. For a visitor
        // counter a lost race is cosmetic; for currency it would not be —
        // that class of data belongs on a server, not in KVP.
        gPendingRead = llReadKeyValue("visits:" + (string)gVisitor);
    }

    dataserver(key query, string data)
    {
        // data format for KVP replies: "1,value" on success, "0,error" on
        // failure, where the first field is success as an integer string.
        list parts = llParseString2List(data, [","], []);
        // NOTE: llParseString2List on "," breaks values containing commas.
        // Production code parses only the FIRST comma manually. Visitor
        // counts are integers (no commas), so the simple parse is safe HERE
        // and only here.

        if (query == gPendingRead)
        {
            integer count = 0;
            if (llList2Integer(parts, 0) == 1)
                count = llList2Integer(parts, 1);
            // else: key does not exist yet (first visit) or an error we
            // treat as 0 for this cosmetic counter.
            ++count;
            llInstantMessage(gVisitor, "Visit number " + (string)count + " — welcome back!");
            gPendingWrite = llUpdateKeyValue("visits:" + (string)gVisitor,
                                             (string)count);
        }
        else if (query == gPendingWrite)
        {
            if (llList2Integer(parts, 0) != 1)
                llOwnerSay("KVP write failed: " + data);
        }
    }
}
```

**Notes and pitfalls**

- The script must be experience-compiled (like Example 13) or every KVP call
  fails. The failure arrives via dataserver as a `0,...` reply, not a compile
  error, so untested KVP code fails silently in production.
- Parse only the first comma in real code: `llSubStringIndex(data, ",")` then
  split manually. Comma-in-value corruption is the standard KVP bug.
- OpenSim has no Experience KVP. Emulations exist via OSSL and external servers;
  a portable product stores counters server-side with `llHTTPRequest` instead
  and uses KVP only as an SL-side cache.

---
## Example 22 — Environment and time: reading the parcel's EEP environment

**What it does:** Queries the environment at the object's position with
`llGetEnvironment` (the EEP-era API that replaced Windlight scripting), reports
sky/sun details, and shows how environment data is a key-value list you query by
name — plus why scripts mostly *read* environment while *setting* it is a
land-privileged operation done through assets and caps, not a single ll call.

```lsl
// Environment reader — touch reports the current environment values at the
// object's altitude. llGetEnvironment returns values for named parameters;
// ask only for what you need, each name is a round trip through the same call.

default
{
    touch_start(integer n)
    {
        list env = llGetEnvironment(llGetPos(), [
            SKY_TRACKS,            // which sky tracks are in effect
            SKY_AMBIENT,           // ambient light colour (vector)
            SKY_SUN,               // sun colour/direction data per docs
            ENVIRONMENT_VERSION    // increments when the environment changes
        ]);
        // The return list is key-value STRIDED in the order requested:
        // [name1, value1, name2, value2, ...] with types per parameter.
        llOwnerSay("env version=" + llList2String(env, 7));
        llOwnerSay("ambient=" + llList2String(env, 3));
        llOwnerSay("tracks=" + llList2String(env, 1));

        // Day fraction is often what scripts actually want (open at night,
        // close at dawn). llGetSunDirection() gives the sun vector directly;
        // its z component sign is the portable day/night test.
        vector sun = llGetSunDirection();
        if (sun.z <= 0.0) llSay(0, "It is night here.");
        else              llSay(0, "It is day here.");
    }
}
```

**Notes and pitfalls**

- Exact `llGetEnvironment` parameter names and return types are versioned API
  surface — verify names against `lsl-definitions` YAML for the current viewer
  era rather than copying lists from old Windlight-era scripts, which used
  entirely different (and now dead) approaches.
- Setting parcel environment requires land rights and environment *assets*
  applied through the viewer/caps (`ExtEnvironment`); there is no
  `llSetWindlight` in SL. OpenSim LightShare (`wl*` functions) DOES let scripts
  set windlight — OpenSim-only, and a common porting trap in both directions.

---

## Example 23 — Access control: allowlist gate with sensor and dialog admin

**What it does:** A security gate combining the library's patterns: an allowlist
loaded from a notecard (Example 8 pattern, condensed), a sensor that challenges
non-listed avatars, and an owner dialog (Example 4 pattern) to add/remove people.
This is the "putting it together" example — real access systems are compositions,
not new APIs.

```lsl
// Access gate — allowlist in notecard "allowlist" (one avatar UUID per line,
// or "name" lines resolved at load are NOT supported by LSL alone: UUIDs only,
// because llRequestAgentData/name-to-key needs dataserver round trips per name
// and is deliberately out of scope for a gate that must answer in <1 s).

list    gAllow = [];
integer gLine = 0;
key     gQuery = NULL_KEY;
integer ADMIN_CHAN = -991001;
integer gListen = 0;

integer allowed(key who)
{
    return who == llGetOwner() || llListFindList(gAllow, [who]) != -1;
}

start_read()
{
    gAllow = [];
    gLine = 0;
    if (llGetInventoryType("allowlist") == INVENTORY_NOTECARD)
        gQuery = llGetNotecardLine("allowlist", gLine);
}

default
{
    state_entry()
    {
        start_read();
        llSensorRepeat("", NULL_KEY, AGENT, 4.0, PI, 1.0);
        gListen = llListen(ADMIN_CHAN, "", llGetOwner(), "");
        llOwnerSay("Gate live. Owner: /" + (string)(-ADMIN_CHAN) +
                   " is wrong — use dialog: touch with owner for admin.");
    }

    dataserver(key q, string data)
    {
        if (q != gQuery) return;
        if (data == EOF) { llOwnerSay("Allowlist loaded: " +
                           (string)llGetListLength(gAllow) + " entries."); return; }
        string line = llStringTrim(data, STRING_TRIM);
        if ((key)line != NULL_KEY && llStringLength(line) == 36)
            gAllow += [(key)line];
        ++gLine;
        gQuery = llGetNotecardLine("allowlist", gLine);
    }

    sensor(integer n)
    {
        integer i;
        for (i = 0; i < n; ++i)
        {
            key who = llDetectedKey(i);
            if (!allowed(who))
            {
                // Warn once per approach in real deployments (cooldown map,
                // Example 18). Kept direct here for readability.
                llInstantMessage(who, "This is a restricted area.");
            }
        }
    }

    touch_start(integer n)
    {
        key who = llDetectedKey(0);
        if (who != llGetOwner()) return;
        llDialog(who, "Gate admin", ["List", "Reload", "Close"], ADMIN_CHAN);
    }

    listen(integer chan, string name, key id, string msg)
    {
        if (id != llGetOwner()) return;
        if (msg == "List")
        {
            integer i;
            for (i = 0; i < llGetListLength(gAllow); ++i)
                llOwnerSay("allow: " + llKey2Name(llList2Key(gAllow, i)));
        }
        else if (msg == "Reload") start_read();
    }

    changed(integer change)
    {
        if (change & CHANGED_INVENTORY) start_read();
        if (change & CHANGED_OWNER) llResetScript();
    }
}
```

**Notes and pitfalls**

- A gate that only *warns* is not security: real enforcement is parcel ban lists,
  estate tools, or a physical door (Example 11) whose open logic calls
  `allowed()`. Scripts cannot eject avatars without land/eject permissions and
  experience or owner context — design the enforcement layer honestly.
- `(key)line` casting any 36-char string succeeds syntactically; validate UUID
  shape if hostile notecard content is a concern.
- Name-to-key resolution: use `llRequestAgentData` / dataserver or an external
  service; never ship a gate that claims to accept names but silently stores
  garbage keys.

---

## Example 24 — Animesh and object animation control

**What it does:** Starts and stops animations on a rigged mesh object (Animesh)
with `llStartObjectAnimation` / `llStopObjectAnimation`, lists the animations
playing, and explains how animesh differs from avatar animation: the object has
its own skeleton, counts against land limits differently, and is animated by its
own scripts, not by an avatar's AO.

```lsl
// Animesh controller — the object containing this script IS the animesh
// (or the script sits in its root prim). Animations must be in the object's
// inventory. The object must be flagged as an Animated Object in the viewer
// (Features tab) for the skeleton to be active in SL.

list ANIMS = ["idle_sway", "wave", "dance_loop"];
integer gCurrent = -1;          // index into ANIMS, -1 = stopped

stop_all()
{
    // Stop exactly what is playing (queried live) rather than guessing:
    // other scripts in the object may have started animations too.
    list playing = llGetObjectAnimationNames();
    integer i;
    for (i = 0; i < llGetListLength(playing); ++i)
        llStopObjectAnimation(llList2String(playing, i));
    gCurrent = -1;
}

default
{
    state_entry()
    {
        llOwnerSay("Animesh ready. Touch to cycle animations.");
    }

    touch_start(integer n)
    {
        stop_all();
        gCurrent = (gCurrent + 1) % (llGetListLength(ANIMS) + 1);
        if (gCurrent < llGetListLength(ANIMS))
        {
            string anim = llList2String(ANIMS, gCurrent);
            llStartObjectAnimation(anim);
            llSetText("Playing: " + anim, <1,1,1>, 0.9);
        }
        else
        {
            gCurrent = -1;
            llSetText("Stopped", <1,1,1>, 0.9);
        }
    }

    changed(integer change)
    {
        // Animated-object status is an object property set outside the
        // script; if the object is re-rezzed from inventory it can come
        // back un-flagged. There is no script call to set it — warn instead.
        if (change & CHANGED_OWNER) llResetScript();
    }
}
```

**Notes and pitfalls**

- Animesh land impact and the per-region animesh limits are enforced outside
  scripts; a scene of animesh pets fails at rez time, not in your code.
- Animation names are inventory names, case-sensitive in practice. A typo fails
  silently — `llGetObjectAnimationNames()` after a start is the verification
  pattern used above.
- OpenSim: animesh support arrived later and behaves differently in spots
  (notably with attachments and NPC interplay). Test start/stop/query on both.

---

## Example 25 — Tip jar with pay dialog, totals, and thank-you tiers

**What it does:** A tip jar using `llSetPayPrice` with suggested amounts, the
`money()` event, running totals in hover text, tiered thank-you messages, and a
last-tipper display. Contrasts with Example 12: no debit permission is needed to
*receive* money — only to send it back — and the safety discussion explains why
tip jars must still be careful (refund features change that equation instantly).

```lsl
// Tip jar — receiving money needs NO permission. Sending (refunds, splits)
// would need PERMISSION_DEBIT; this jar implements a SPLIT to a partner,
// which is why it requests debit and explains itself to the owner at setup.

key     PARTNER = NULL_KEY;     // set to a real avatar UUID to enable split
integer SPLIT_PERCENT = 0;      // 0 = no split (and no debit request at all)
integer gTotal = 0;
integer gCount = 0;
key     gLastTipper = NULL_KEY;
integer gHaveDebit = FALSE;

update_text()
{
    string t = "Tips welcome!";
    if (gCount > 0)
        t += "\nTotal: L$" + (string)gTotal + " from " + (string)gCount +
             " tippers\nLast: " + llKey2Name(gLastTipper);
    llSetText(t, <1.0, 0.85, 0.4>, 1.0);
}

default
{
    state_entry()
    {
        // Suggested quick-pay amounts; the payer can always type another.
        llSetPayPrice(PAY_UNPAYABLE, [25, 50, 100, 250]);
        update_text();

        if (SPLIT_PERCENT > 0 && PARTNER != NULL_KEY)
        {
            llRequestPermissions(llGetOwner(), PERMISSION_DEBIT);
            llOwnerSay("Split enabled: requesting DEBIT so shares can be " +
                       "paid out. Without it, tips are kept whole.");
        }
    }

    run_time_permissions(integer perm)
    {
        gHaveDebit = (perm & PERMISSION_DEBIT) != 0;
        if (!gHaveDebit && SPLIT_PERCENT > 0)
            llOwnerSay("Debit declined: split disabled, tips kept whole.");
    }

    money(key payer, integer amount)
    {
        gTotal += amount;
        ++gCount;
        gLastTipper = payer;

        string thanks = "Thank you for your tip!";
        if (amount >= 250)      thanks = "Wow — thank you so much!";
        else if (amount >= 100) thanks = "Thank you, that is generous!";
        llInstantMessage(payer, thanks);

        if (gHaveDebit && SPLIT_PERCENT > 0 && PARTNER != NULL_KEY)
        {
            integer share = (amount * SPLIT_PERCENT) / 100;
            if (share > 0) llGiveMoney(PARTNER, share);
        }
        update_text();
    }

    touch_start(integer n)
    {
        if (llDetectedKey(0) == llGetOwner())
            llOwnerSay("Jar stats: L$" + (string)gTotal + ", " +
                       (string)gCount + " tips, debit=" + (string)gHaveDebit);
    }
}
```

**Notes and pitfalls**

- Totals in script variables die on reset. A jar whose numbers matter should
  report each tip to a server (Example 6 pattern) or KVP (Example 21) — hover
  text totals are a display, not accounts.
- Integer division in the split truncates; over many small tips the truncation
  drift is real money. Accumulate remainders if splits must be exact.
- OpenSim money modules vary wildly (some standalone installs have no currency
  at all). The pay UI simply will not appear where money is not configured.

---
## Example 26 — Sit teleporter (the classic, with its real limitations)

**What it does:** The long-standing sit-teleport pattern: an object moves itself
(and its seated avatar) to a destination when the avatar sits, then moves back.
Included because thousands of in-world teleporters use it — with honest notes on
its range/permission limits and why experience teleport (Example 13) or
`llTeleportAgentHome` style flows replaced it for serious use.

```lsl
// Sit teleporter — destination is a region position. HOW IT WORKS: sitting
// links the avatar to the object; llSetPos moves the OBJECT (max 10 m per
// call, so long moves are done as a fast series of hops in a timer, or by
// llSetRegionPos which allows one region-wide jump in SL).
// Limits that define this pattern:
//   * Same region only.
//   * The avatar must be able to sit (parcel entry, ban lines, and landing
//     point settings can all refuse at the far end).
//   * llSetRegionPos fails if the destination parcel is full/blocked.

vector DEST = <64.0, 200.0, 40.0>;
vector gHome;
integer gCarrying = FALSE;

default
{
    state_entry()
    {
        gHome = llGetPos();
        llSitTarget(<0.0, 0.0, 0.5>, ZERO_ROTATION);
        llSetText("Sit to teleport", <0.7, 0.9, 1.0>, 1.0);
    }

    changed(integer change)
    {
        if (!(change & CHANGED_LINK)) return;
        key sitter = llAvatarOnSitTarget();

        if (sitter != NULL_KEY && !gCarrying)
        {
            gCarrying = TRUE;
            // llSetRegionPos returns TRUE on success in SL.
            if (llSetRegionPos(DEST))
            {
                // Arrived: stand them up, then go home empty.
                llUnSit(sitter);
                llSleep(0.5);   // brief settle; acceptable HERE because the
                                // script does nothing else while carrying —
                                // contrast Example 10's warning for busy scripts
                llSetRegionPos(gHome);
            }
            else
            {
                llInstantMessage(sitter, "Destination unavailable right now.");
                llUnSit(sitter);
            }
            gCarrying = FALSE;
        }
    }
}
```

**Notes and pitfalls**

- `llSetRegionPos` is SL; OpenSim supports it in recent versions but behaviour
  with parcel restrictions differs, and `osTeleportAgent` is the OpenSim-native
  route (threat-level gated). Pick per grid.
- A carrying object that errors mid-flight strands an avatar or itself; the
  home-return must be in the same handler, as above, not in a later event that
  a state change could discard.
- Modern builds should prefer: experience teleport (Example 13) on SL,
  landmark givers for cross-region, and this pattern only for short same-region
  hops where its failure modes are acceptable.

---

## Example 27 — Multi-state quiz game (states as game phases)

**What it does:** A complete tiny game built as four states — `idle`, `asking`,
`scoring` is folded into `asking`, and back — showing why named states are the
right tool for phase-driven objects: each phase gets only the events it cares
about, illegal touches in the wrong phase are impossible by construction, and the
scorekeeping shows list-based question banks.

```lsl
// Quiz — touch to play. Questions are parallel lists (question, answer).
// Answers are given in public chat while the game is in `asking` state; the
// listen exists ONLY in that state, which is the point of the design.

list QUESTIONS = ["What colour do you get mixing blue and yellow paint?",
                  "How many metres are in a standard SL region edge?",
                  "What language are SL scripts written in?"];
list ANSWERS   = ["green", "256", "lsl"];

integer gScore = 0;
integer gIndex = 0;
key     gPlayer = NULL_KEY;
integer gListen = 0;
integer gQuestionDeadline = 0;

default   // idle
{
    state_entry()
    {
        llSetText("Quiz — touch to play", <1,1,1>, 1.0);
    }

    touch_start(integer n)
    {
        gPlayer = llDetectedKey(0);
        gScore = 0;
        gIndex = 0;
        state asking;
    }
}

state asking
{
    state_entry()
    {
        gListen = llListen(0, "", gPlayer, "");
        ask_current();
    }

    ask_current()
    {
        llSay(0, "Q" + (string)(gIndex + 1) + ": " +
                 llList2String(QUESTIONS, gIndex) + " (answer in chat, 30 s)");
        gQuestionDeadline = llGetUnixTime() + 30;
        llSetTimerEvent(5.0);
    }

    listen(integer chan, string name, key id, string msg)
    {
        if (id != gPlayer) return;
        string guess = llToLower(llStringTrim(msg, STRING_TRIM));
        if (guess == llList2String(ANSWERS, gIndex))
        {
            ++gScore;
            llSay(0, "Correct! Score " + (string)gScore);
        }
        else
        {
            llSay(0, "No — it was '" + llList2String(ANSWERS, gIndex) + "'.");
        }
        ++gIndex;
        if (gIndex >= llGetListLength(QUESTIONS)) state default;
        else ask_current();
    }

    timer()
    {
        if (llGetUnixTime() > gQuestionDeadline)
        {
            llSay(0, "Time's up! It was '" + llList2String(ANSWERS, gIndex) + "'.");
            ++gIndex;
            if (gIndex >= llGetListLength(QUESTIONS)) state default;
            else ask_current();
        }
    }

    state_exit()
    {
        // Announce the final score from state_exit of the LAST question or
        // from default.state_entry in fuller versions; here we report on the
        // way out whenever we leave with a completed game.
        llListenRemove(gListen);
        llSetTimerEvent(0.0);
        if (gIndex >= llGetListLength(QUESTIONS))
            llSay(0, "Game over, " + llKey2Name(gPlayer) + ": " +
                     (string)gScore + "/" + (string)llGetListLength(QUESTIONS));
    }

    touch_start(integer n)
    {
        // Touching mid-game by the player = forfeit. Anyone else: ignored.
        if (llDetectedKey(0) == gPlayer) state default;
    }
}
```

**Notes and pitfalls**

- Listening on channel 0 only during `asking`, filtered to the player, is both
  the game mechanic and the performance story: no permanent public listen.
- State changes discard queued events: a correct answer typed in the same
  instant the timeout fires can be lost. Games that care check the deadline
  inside `listen` too; teaching code keeps one authority (the timer).
- OpenSim: same design works; chat range (20 m for `llSay` listeners) and timer
  granularity are the only portability notes, both covered in earlier examples.

---

## Example 28 — Sound, looping audio, and preload discipline

**What it does:** Plays a looping sound from inventory with volume control via
chat, demonstrates `llLoopSound` / `llStopSound` / `llPreloadSound`, trigger
sounds on collision, and the client-side reality of in-world audio: sounds are
short clips (max ~10 s uploads in SL), loops are assembled by the viewer, and
volume is distance-attenuated for everyone but the triggerer.

```lsl
// Ambient sound stone — loops a nature clip; owner can set volume by chat:
//   /55 vol 0.5      /55 stop      /55 start
string  CLIP = "nature_loop";   // sound in this prim's inventory
integer CHAN = 55;
float   gVolume = 0.7;
integer gPlaying = FALSE;

start_loop()
{
    // Preload pushes the asset toward nearby viewers so the first loop does
    // not start with a download gap. Preload on state_entry and on rez, not
    // inside touch handlers.
    llPreloadSound(CLIP);
    llLoopSound(CLIP, gVolume);
    gPlaying = TRUE;
}

default
{
    state_entry()
    {
        llPreloadSound(CLIP);
        llListen(CHAN, "", llGetOwner(), "");
        start_loop();
        llOwnerSay("Sound stone live on /" + (string)CHAN);
    }

    listen(integer chan, string name, key id, string msg)
    {
        list p = llParseString2List(llToLower(msg), [" "], []);
        string verb = llList2String(p, 0);
        if (verb == "vol" && llGetListLength(p) == 2)
        {
            gVolume = llList2Float(p, 1);
            if (gVolume < 0.0) gVolume = 0.0;
            if (gVolume > 1.0) gVolume = 1.0;
            if (gPlaying) llLoopSound(CLIP, gVolume);  // re-issue to apply
        }
        else if (verb == "stop")  { llStopSound(); gPlaying = FALSE; }
        else if (verb == "start") { start_loop(); }
    }

    collision_start(integer n)
    {
        // One-shot trigger sound for passers-by, on a different function so
        // it does not disturb the loop: llTriggerSound is positional and
        // does not loop. Throttle by design: region sound triggering is
        // rate-limited server side, and spammy stones get muted by users.
        llTriggerSound("soft_chime", 0.4);
    }
}
```

**Notes and pitfalls**

- `llLoopSoundMaster` / slave synchronisation exists for multi-prim soundscapes;
  unsynchronised loops drift apart audibly within minutes.
- Sound UUIDs can be used directly in place of inventory names, but inventory
  names keep the asset dependency visible to future editors — prefer names.
- OpenSim: sound functions are viewer-executed in both worlds, so this ports
  cleanly; clip length limits on upload are grid-configured in OpenSim.

---

## Closing notes for the whole library

- **Compile target:** all scripts target the SL Mono compiler. If your editor
  offers an LSO/legacy mode, results (especially memory and `llSleep`) differ.
- **Preprocessor dialects:** Firestorm's preprocessor adds `#include`, `#define`,
  `switch`, and lazy list indexing. None of that is used here on purpose, so
  these scripts compile in the stock Linden Lab editor, in Firestorm with the
  preprocessor on or off, and in OpenSim's script editor. If you add those
  extensions to your own forks, your scripts stop being portable — decide
  consciously.
- **The five checks before shipping any script:** (1) every listen has a stored
  handle and a removal path, (2) every permission use waits for
  `run_time_permissions`, (3) every dataserver consumer matches its query key,
  (4) every timer subsystem anchors to `llGetUnixTime()` instead of counting
  ticks, (5) every money path is either receive-only or refunds on every
  failure branch.
- **Testing grids:** behaviour was specified against Agni semantics. Test on
  Aditi (SL) and a local OpenSim standalone (YEngine) before calling a script
  cross-grid, and write down which grid each test ran on in your release notes.
---

## Example 29 — Smooth mover with llTarget / at_target / not_at_target

**What it does:** Moves a non-physical object smoothly toward waypoints using the
target-notification system instead of polling position in a timer: register a
target with `llTarget`, get `at_target` when you arrive, get periodic
`not_at_target` while travelling, and steer in between. This is the efficient
event-driven alternative to "timer + llGetPos distance check" movers.

```lsl
// Waypoint mover — visits points in order, pausing at each.
// llTarget(pos, tolerance) returns a handle; at_target fires when the
// object's centre is within tolerance; not_at_target fires periodically
// while a target is registered and not reached. Register ONE target at a
// time and remove it with llTargetRemove(handle) when done or changing.

list    POINTS = [<110,120,25>, <125,120,25>, <125,135,25>, <110,135,25>];
integer gIdx = 0;
integer gTargetHandle = 0;
integer gPauseUntil = 0;
float   SPEED = 0.5;            // fraction of remaining distance per step:
                                // proportional steering = fast far away,
                                // gentle arrival, no overshoot oscillation.

go_to(integer idx)
{
    if (gTargetHandle) llTargetRemove(gTargetHandle);
    vector dest = llList2Vector(POINTS, idx);
    gTargetHandle = llTarget(dest, 0.5);
}

default
{
    state_entry()
    {
        llSetStatus(STATUS_PHYSICS, FALSE);     // kinematic mover, not physical
        go_to(0);
        llSetTimerEvent(0.2);                   // steering tick while travelling
    }

    at_target(integer handle, vector target_pos, vector at_pos)
    {
        if (handle != gTargetHandle) return;    // stale target notification
        llTargetRemove(gTargetHandle);
        gTargetHandle = 0;
        gPauseUntil = llGetUnixTime() + 3;      // pause 3 s at each point
        llSetTimerEvent(1.0);
    }

    not_at_target()
    {
        // Fires on its own schedule while travelling; we ALSO steer from the
        // timer so the step rate is ours, not the sim's notification rate.
    }

    timer()
    {
        if (gTargetHandle)
        {
            vector dest = llList2Vector(POINTS, gIdx);
            vector pos = llGetPos();
            vector next = pos + (dest - pos) * SPEED;
            // llSetPos 10 m limit: proportional steps self-limit as we
            // approach; for the FIRST step from far away, clamp manually.
            if (llVecDist(pos, next) > 10.0)
                next = pos + llVecNorm(dest - pos) * 10.0;
            llSetPos(next);
        }
        else if (gPauseUntil && llGetUnixTime() >= gPauseUntil)
        {
            gPauseUntil = 0;
            gIdx = (gIdx + 1) % llGetListLength(POINTS);
            go_to(gIdx);
            llSetTimerEvent(0.2);
        }
    }
}
```

**Notes and pitfalls**

- `at_target` tolerance is a sphere around the point; for floor-accurate arrivals
  combine with a Z check, because arriving 0.5 m *above* the point still counts.
- Rotating movers use `llRotTarget` / `at_rot_target` the same way. Registering a
  new target without removing the old one produces interleaved notifications —
  hence the handle bookkeeping above.
- OpenSim: target notification rates differ under both physics engines; the
  proportional steering in this script is deliberately rate-tolerant.

---

## Example 30 — Inventory giver with dialog choice and per-avatar cooldown

**What it does:** Touch opens a dialog listing giveable items from the object's
inventory (discovered at runtime with `llGetInventoryName`, not hard-coded),
gives the chosen item with `llGiveInventory`, and enforces a per-avatar cooldown
so one visitor cannot drain a no-copy giver or spam a copyable one.

```lsl
// Giver — gives ONE item per visitor per hour from whatever is in the prim.
// Items that are no-copy are protected by the cooldown AND by an explicit
// stock check: giving away the last no-copy copy removes it from inventory.

integer CHAN = -445500;
integer gListen = 0;
list    gItems = [];
list    gCooldownKeys = [];
list    gCooldownTimes = [];
integer COOLDOWN = 3600;

refresh_items()
{
    gItems = [];
    integer count = llGetInventoryNumber(INVENTORY_OBJECT);
    integer i;
    for (i = 0; i < count; ++i)
        gItems += [llGetInventoryName(INVENTORY_OBJECT, i)];
    // Notecards/textures/etc. use their own INVENTORY_* types; a giver of
    // mixed content queries each type it supports the same way.
}

integer on_cooldown(key who)
{
    integer idx = llListFindList(gCooldownKeys, [who]);
    if (idx == -1) return FALSE;
    return (llGetUnixTime() - llList2Integer(gCooldownTimes, idx)) < COOLDOWN;
}

mark_given(key who)
{
    integer idx = llListFindList(gCooldownKeys, [who]);
    if (idx == -1)
    {
        gCooldownKeys += [who];
        gCooldownTimes += [llGetUnixTime()];
    }
    else gCooldownTimes = llListReplaceList(gCooldownTimes,
                          [llGetUnixTime()], idx, idx);
}

default
{
    state_entry()
    {
        refresh_items();
        gListen = llListen(CHAN, "", NULL_KEY, "");
    }

    touch_start(integer n)
    {
        key who = llDetectedKey(0);
        if (on_cooldown(who))
        {
            llInstantMessage(who, "You already took an item recently — " +
                                  "please come back later.");
            return;
        }
        if (llGetListLength(gItems) == 0)
        {
            llInstantMessage(who, "Nothing to give right now.");
            return;
        }
        // Dialog max is 12 buttons; a giver with more stock must paginate
        // (Example 4) — here we offer the first 12 and say so in the text.
        list buttons = llList2List(gItems, 0, 11);
        llDialog(who, "Choose one item (" + (string)llGetListLength(gItems) +
                      " in stock):", buttons, CHAN);
    }

    listen(integer chan, string name, key id, string msg)
    {
        if (llListFindList(gItems, [msg]) == -1) return;  // not a real item
        if (on_cooldown(id)) return;                      // double-tap guard
        if (llGetInventoryType(msg) == INVENTORY_NONE)
        {
            llInstantMessage(id, "Sorry, that just ran out.");
            refresh_items();
            return;
        }
        llGiveInventory(id, msg);
        mark_given(id);
        llInstantMessage(id, "Here is your " + msg + ".");
        refresh_items();   // a no-copy give changes the stock list
    }

    changed(integer change)
    {
        if (change & CHANGED_INVENTORY) refresh_items();
    }
}
```

**Notes and pitfalls**

- `llGiveInventory` to an avatar who is offline or who declines/mutes objects can
  silently not deliver in some paths; for paid goods use the vendor pattern
  (Example 12) with its logging, never a bare giver.
- Giving folders uses `llGiveInventoryList` with a category name; lists of mixed
  types are fine, and the same cooldown logic applies.
- OpenSim inventory delivery interacts with the grid's inventory service and
  Hypergrid visitors differently; test with a foreign (Hypergrid) avatar if your
  region allows them.

---

## Example 31 — Rental meter: paid time, warnings, and expiry states

**What it does:** A rental box as three states — `available`, `rented`, and
`expiring` — paid through `money()`, with time tracked in unix timestamps, a
warning to the tenant before expiry, renewal by further payment, and an owner
override. Rental systems are where money, timers, and states meet real disputes,
so every transition is logged to the owner.

```lsl
// Rental meter — L$100 per day, minimum one day, renewals extend the term.

integer RATE_PER_DAY = 100;
integer DAY = 86400;
key     gTenant = NULL_KEY;
integer gPaidUntil = 0;
integer gWarned = FALSE;

integer days_for(integer amount) { return amount / RATE_PER_DAY; }

default   // available
{
    state_entry()
    {
        llSetPayPrice(RATE_PER_DAY,
            [RATE_PER_DAY, RATE_PER_DAY * 7, PAY_UNPAYABLE, PAY_UNPAYABLE]);
        llSetText("FOR RENT\nL$" + (string)RATE_PER_DAY + "/day",
                  <0.5, 1.0, 0.5>, 1.0);
        llSetTimerEvent(0.0);
    }

    money(key payer, integer amount)
    {
        integer days = days_for(amount);
        if (days < 1)
        {
            // Under one day: treat as a tip toward the house, not a rental,
            // and SAY so — silently keeping sub-minimum payments as "rent"
            // is how rental disputes start.
            llInstantMessage(payer, "That is under the one-day minimum, so " +
                             "it was accepted as a tip, not rent. Thank you!");
            llOwnerSay("Sub-minimum payment L$" + (string)amount + " from " +
                       llKey2Name(payer) + " logged as tip.");
            return;
        }
        gTenant = payer;
        gPaidUntil = llGetUnixTime() + days * DAY;
        gWarned = FALSE;
        llOwnerSay("RENTED to " + llKey2Name(payer) + " for " + (string)days +
                   " day(s), L$" + (string)amount);
        state rented;
    }
}

state rented
{
    state_entry()
    {
        llSetPayPrice(RATE_PER_DAY,
            [RATE_PER_DAY, RATE_PER_DAY * 7, PAY_UNPAYABLE, PAY_UNPAYABLE]);
        llSetText("Rented by " + llKey2Name(gTenant) + "\nPaid until " +
                  llGetTimestamp(), <1.0, 0.8, 0.4>, 1.0);
        llSetTimerEvent(60.0);   // check expiry once a minute; cheap and ample
    }

    money(key payer, integer amount)
    {
        integer days = days_for(amount);
        if (days < 1) return;   // ignore sub-minimum top-ups while rented
        if (payer != gTenant)
        {
            llOwnerSay("Renewal payment from NON-tenant " + llKey2Name(payer) +
                       " — applied to current tenancy, verify intent.");
        }
        // Renewals extend from the CURRENT paid-until, not from now, so
        // paying early never loses time. This line is the whole fairness
        // model of the meter; changing it to "now + days" steals paid time.
        gPaidUntil += days * DAY;
        gWarned = FALSE;
        llInstantMessage(payer, "Rental extended by " + (string)days + " day(s).");
    }

    timer()
    {
        integer now = llGetUnixTime();
        integer remain = gPaidUntil - now;
        if (remain <= 0)
        {
            llInstantMessage(gTenant, "Your rental has expired.");
            llOwnerSay("EXPIRED: tenancy of " + llKey2Name(gTenant) + " ended.");
            gTenant = NULL_KEY;
            state default;
        }
        else if (remain < DAY && !gWarned)
        {
            gWarned = TRUE;
            llInstantMessage(gTenant, "Your rental expires within a day. " +
                                      "Pay this meter to renew.");
        }
    }

    touch_start(integer n)
    {
        if (llDetectedKey(0) == llGetOwner())
        {
            integer remain = gPaidUntil - llGetUnixTime();
            llOwnerSay("Tenant " + llKey2Name(gTenant) + ", seconds left: " +
                       (string)remain);
        }
    }
}
```

**Notes and pitfalls**

- Expiry in this teaching version only *ends the tenancy record*. Real systems
  also return tenant objects (`llReturnObjectsByOwner` is experience/land
  scoped) or open a door lock (Example 23's `allowed()` reading the tenant key).
  Never promise eviction behaviour the land permissions cannot deliver.
- All state lives in script variables: a region restart does not reset scripts,
  but a script reset or object edit does. Commercial meters persist tenancy to a
  server or KVP for exactly this reason.
- OpenSim money caveats from Examples 12/25 apply unchanged.

---

## Example 32 — Simple vehicle: vehicle parameters and control driving

**What it does:** A minimal ground vehicle: sit to possess, `PERMISSION_TAKE_CONTROLS`,
vehicle parameters via `llSetVehicleParams`, forward/reverse and turning from the
control event, and a clean shutdown that removes the vehicle flags. Vehicles are
the most physics-sensitive LSL application; this example teaches the structure,
and the notes are blunt about tuning.

```lsl
// Simple vehicle — build notes BEFORE the code:
//  * The object must become PHYSICAL while driven (vehicle dynamics only
//    apply to physical objects) and non-physical at rest, or it will roll
//    downhill while parked.
//  * The driver sits on the vehicle (llSitTarget in the root prim).
//  * Mass distribution, buoyancy, and friction are VEHICLE parameters, not
//    prim physics panel settings alone.

integer gDriving = FALSE;
key     gDriver = NULL_KEY;

vehicle_on()
{
    llSetVehicleType(VEHICLE_TYPE_CAR);
    llSetVehicleFloatParam(VEHICLE_ANGULAR_DEFLECTION_EFFICIENCY, 0.2);
    llSetVehicleFloatParam(VEHICLE_LINEAR_DEFLECTION_EFFICIENCY, 0.80);
    llSetVehicleFloatParam(VEHICLE_ANGULAR_DEFLECTION_TIMESCALE, 0.10);
    llSetVehicleFloatParam(VEHICLE_LINEAR_DEFLECTION_TIMESCALE, 0.10);
    llSetVehicleFloatParam(VEHICLE_LINEAR_MOTOR_TIMESCALE, 1.0);
    llSetVehicleFloatParam(VEHICLE_LINEAR_MOTOR_DECAY_TIMESCALE, 0.2);
    llSetVehicleFloatParam(VEHICLE_ANGULAR_MOTOR_TIMESCALE, 0.3);
    llSetVehicleFloatParam(VEHICLE_ANGULAR_MOTOR_DECAY_TIMESCALE, 0.1);
    llSetVehicleVectorParam(VEHICLE_LINEAR_FRICTION_TIMESCALE, <100.0, 2.0, 1000.0>);
    llSetVehicleVectorParam(VEHICLE_ANGULAR_FRICTION_TIMESCALE, <10.0, 10.0, 10.0>);
    llSetVehicleFloatParam(VEHICLE_VERTICAL_ATTRACTION_EFFICIENCY, 0.5);
    llSetVehicleFloatParam(VEHICLE_VERTICAL_ATTRACTION_TIMESCALE, 0.5);
    llSetVehicleFloatParam(VEHICLE_BANKING_EFFICIENCY, 0.3);
    llSetVehicleFloatParam(VEHICLE_BANKING_MIX, 0.7);
    llSetVehicleFloatParam(VEHICLE_BANKING_TIMESCALE, 0.2);
    llSetVehicleFloatParam(VEHICLE_BUOYANCY, 0.0);   // 0 = full gravity (car)
    llSetVehicleVectorParam(VEHICLE_LINEAR_MOTOR_OFFSET, ZERO_VECTOR);
    llRemoveVehicleFlags(0
        | VEHICLE_FLAG_HOVER_WATER_ONLY
        | VEHICLE_FLAG_HOVER_TERRAIN_ONLY
        | VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT
        | VEHICLE_FLAG_LIMIT_MOTOR_UP);
    llSetVehicleFlags(0
        | VEHICLE_FLAG_NO_DEFLECTION_UP
        | VEHICLE_FLAG_LIMIT_ROLL_ONLY
        | VEHICLE_FLAG_HOVER_UP_ONLY
        | VEHICLE_FLAG_MOUSELOOK_STEER
        | VEHICLE_FLAG_MOUSELOOK_BANK
        | VEHICLE_FLAG_CAMERA_DECOUPLED);
    llSetStatus(STATUS_PHYSICS, TRUE);
}

vehicle_off()
{
    llSetVehicleType(VEHICLE_TYPE_NONE);
    llSetStatus(STATUS_PHYSICS, FALSE);
}

default
{
    state_entry()
    {
        llSitTarget(<0.05, 0.0, 0.65>, ZERO_ROTATION);
        vehicle_off();
    }

    changed(integer change)
    {
        if (!(change & CHANGED_LINK)) return;
        key sitter = llAvatarOnSitTarget();
        if (sitter != NULL_KEY && !gDriving)
        {
            gDriver = sitter;
            llRequestPermissions(sitter,
                PERMISSION_TAKE_CONTROLS | PERMISSION_TRIGGER_ANIMATION);
        }
        else if (sitter == NULL_KEY && gDriving)
        {
            llReleaseControls();
            vehicle_off();
            gDriving = FALSE;
            gDriver = NULL_KEY;
        }
    }

    run_time_permissions(integer perm)
    {
        if (perm & PERMISSION_TAKE_CONTROLS)
        {
            llTakeControls(CONTROL_FWD | CONTROL_BACK | CONTROL_LEFT |
                           CONTROL_RIGHT | CONTROL_ROT_LEFT |
                           CONTROL_ROT_RIGHT | CONTROL_UP | CONTROL_DOWN,
                           TRUE, FALSE);
            vehicle_on();
            gDriving = TRUE;
        }
    }

    control(key id, integer level, integer edge)
    {
        // Cars are driven with LINEAR and ANGULAR motor setters from the
        // held-key LEVEL (continuous), not the edge. Speeds are in m/s and
        // radians — start slow; 8 m/s in a region is already fast.
        vector linear = ZERO_VECTOR;
        vector angular = ZERO_VECTOR;
        if (level & CONTROL_FWD)  linear.x += 8.0;
        if (level & CONTROL_BACK) linear.x -= 4.0;
        if (level & (CONTROL_LEFT | CONTROL_ROT_LEFT))   angular.z += 1.2;
        if (level & (CONTROL_RIGHT | CONTROL_ROT_RIGHT)) angular.z -= 1.2;
        llSetVehicleVectorParam(VEHICLE_LINEAR_MOTOR_DIRECTION, linear);
        llSetVehicleVectorParam(VEHICLE_ANGULAR_MOTOR_DIRECTION, angular);
    }
}
```

**Notes and pitfalls**

- Vehicle tuning does NOT transfer between SL (Havok) and OpenSim (BulletSim or
  ubODE). The same parameter set can be undriveable on one and fine on the other;
  ship per-grid parameter profiles selected at runtime (`llGetEnv` / grid checks
  are unreliable — use a config notecard flag) and never promise identical feel.
- Region crossings in vehicles are the hardest case in SL scripting: controls,
  permissions, and physics all renegotiate mid-motion. Test crossings explicitly;
  a vehicle that works in one region proves almost nothing.
- Attachments and AOs on the driver fight vehicle animations; vehicles normally
  stop the driver's AO animations on sit (see Example 16's pattern).

---
## Appendix A — Idioms used across the library (copy-paste patterns)

These short patterns recur in production scripts. They are fragments, not whole
scripts — each says where it plugs in.

### A1. Safe list-as-dictionary get with default

```lsl
// Parallel lists gKeys/gVals. Returns defaultValue instead of erroring when
// the key is absent — list index -1 is the bug this prevents everywhere.
string dict_get(list keys, list vals, string k, string defaultValue)
{
    integer idx = llListFindList(keys, [k]);
    if (idx == -1) return defaultValue;
    return llList2String(vals, idx);
}
```

### A2. Parsing only the first separator (KVP/HTTP-safe)

```lsl
// llParseString2List splits on EVERY comma and destroys values containing
// commas. For "status,rest of payload" formats, split once, manually:
list split_first(string s, string sep)
{
    integer at = llSubStringIndex(s, sep);
    if (at == -1) return [s, ""];
    return [llGetSubString(s, 0, at - 1),
            llGetSubString(s, at + llStringLength(sep), -1)];
}
```

### A3. CSV vector parse with validation

```lsl
// (vector) casts fail SILENTLY to ZERO_VECTOR. If zero is not a legal value
// for you, check the shape first: must start "<", contain two commas.
vector parse_vector(string s, vector fallback)
{
    s = llStringTrim(s, STRING_TRIM);
    if (llGetSubString(s, 0, 0) != "<") return fallback;
    if (llStringLength(s) < 5) return fallback;
    vector v = (vector)s;
    return v;
}
```

### A4. Key validation

```lsl
integer is_agent(key k)
{
    // llGetAgentInfo returns 0 for non-agents and departed agents.
    return k != NULL_KEY && llGetAgentInfo(k) != 0;
}
integer is_valid_key_string(string s)
{
    return llStringLength(s) == 36 && (key)s != NULL_KEY;
}
```

### A5. Memory hygiene check for long-lived scripts

```lsl
report_memory()
{
    // llGetUsedMemory is Mono-only; guard so the same script still compiles
    // and runs (reporting 0) anywhere the call is unavailable in your tests.
    integer used = llGetUsedMemory();
    llOwnerSay("memory used=" + (string)used + " free=" +
               (string)llGetFreeMemory());
    if (used > 55000)
        llOwnerSay("WARNING: nearing the 64 KB Mono ceiling — trim lists.");
}
```

### A6. JSON build without tears

```lsl
// Build JSON with llList2Json for anything non-trivial. Hand-concatenated
// JSON breaks on the first quote or backslash in a user-supplied string.
string make_event(string type, string who, integer amount)
{
    return llList2Json(JSON_OBJECT,
        ["type", type, "who", who, "amount", (string)amount,
         "at", llGetTimestamp()]);
}
```

### A7. Region-say announcements without spam

```lsl
announce(string msg)
{
    // llRegionSay reaches the whole region on a channel only scripted
    // listeners hear (channel 0 region say does NOT go to avatar chat).
    // Use a documented channel for your product family, and rate-limit:
    // region say from many objects is how events get muted by residents.
    llRegionSay(-818181, msg);
}
```

### A8. Detecting the grid you are on (best effort, honestly labelled)

```lsl
string grid_hint()
{
    // There is NO supported "which grid am I on" LSL call in SL. Signals
    // people use: llGetSimulatorHostname() domain, llGetEnv() values, and
    // whether os* functions exist (compile-time, OpenSim only). Treat any
    // result as a hint for defaults, never as a security decision.
    string host = llGetSimulatorHostname();
    if (llSubStringIndex(host, "lindenlab.com") != -1) return "agni-or-aditi";
    return "other-or-opensim";
}
```

## Appendix B — Error and failure catalogue (what it looks like, what it means)

- **"Stack-Heap Collision"** — stack plus heap exceeded script memory. Cause:
  runaway list/string growth, deep recursion, or huge local strings. Fix: stream
  data (Example 8), prune lists (Example 18), split work across scripts
  (Example 5). Not recoverable at runtime; the script stops.
- **Script run-time error: "Lists may not contain X" / type errors** — LSL lists
  are heterogeneous but some operations reject nested lists and certain casts.
  Validate element types at protocol boundaries (Examples 5 and 21).
- **"Permission not granted" silence** — the defining LSL failure mode: most
  permission-gated calls fail with NO event and NO message when permission is
  missing. If a feature "just does nothing", audit permissions before logic
  (Examples 9, 12, 13).
- **Dialog clicks do nothing** — no matching `llListen`, wrong channel, or the
  listen was removed by a state change. See Example 4.
- **Notecard read stops after line 0** — the dataserver handler did not request
  the next line, or the query key check rejected the reply after an inventory
  change restarted the read. See Example 8.
- **Object rezzes but never configures** — `object_rez` fired but the handshake
  channel/protocol mismatched, or start_param was 0 because it was rezzed by
  hand. See Example 17.
- **Texture animation frozen mid-scroll** — animation stopped without resetting
  offset. See Example 15.
- **Vendor took money, delivered nothing, said nothing** — item renamed in
  inventory and no `money()` failure branch. See Example 12; that example's
  refund branch exists because this failure is common in the wild.
- **Works for the owner, fails for everyone else** — OSSL threat levels
  (OpenSim), experience land scope (SL), or a listen filtered to the owner by
  accident. Test with an alt account that owns nothing.
- **Works in OpenSim, fails on Agni** — checklist in order: os/mod/wl functions,
  JSON differences, sensor/timer limits, auto-granted permissions hiding a
  missing request, money module assumptions.
- **Works on Agni, fails in OpenSim** — checklist in order: experience features
  (teleport, KVP), pathfinding characters, newer ll functions missing in that
  OpenSim build, AIS-era assumptions in object behaviour.

## Appendix C — Function quick reference for the functions used in this library

Signatures are summarised; canonical signatures live in `secondlife/lsl-definitions`
(`lsl_definitions.yaml`) and the LSL Portal. Delay/energy notes are the ones that
change design decisions.

- `llListen(channel, name, id, msg)` returns a handle; `llListenRemove(handle)`.
  Filter arguments are conjunctive; empty string means "any".
- `llDialog(avatar, text, buttons, channel)` — 12 buttons max, 24 chars per label.
- `llMessageLinked(link, num, str, id)` — inter-prim protocol bus (Example 5).
- `llSetTimerEvent(seconds)` — one timer per script; 0 stops it.
- `llSensorRepeat(name, id, type, range, arc, period)` / `llSensorRemove()`.
- `llGetNotecardLine(name, line)` returns a dataserver query key.
- `llRequestPermissions(avatar, mask)` / `run_time_permissions(perm)` event.
- `llRequestExperiencePermissions(avatar, "" )` / `experience_permissions` events.
- `llHTTPRequest(url, params, body)` returns a request key; throttled per object.
- `llRequestURL()` / `llReleaseURL(url)` — HTTP-in lifecycle (Example 7).
- `llTeleportAgent(avatar, landmark, pos, look)` — experience/teleport permission.
- `llGiveInventory(target, item)` / `llGiveInventoryList(target, folder, items)`.
- `llGiveMoney(target, amount)` — requires PERMISSION_DEBIT; refund paths only
  in the patterns shown here.
- `llSetPayPrice(price, [four quick prices])` — `PAY_UNPAYABLE` hides a button.
- `llCastRay(start, end, options)` returns strided hit list plus status.
- `llCreateCharacter(options)`, `llNavigateTo(target, options)`,
  `llUpdateCharacter(options)`, `llDeleteCharacter()` — SL pathfinding only.
- `llStartObjectAnimation(name)`, `llStopObjectAnimation(name)`,
  `llGetObjectAnimationNames()` — animesh (Example 24).
- `llSetVehicleParams` family (`llSetVehicleType`, `...FloatParam`,
  `...VectorParam`, `...RotationParam`, `llSetVehicleFlags`,
  `llRemoveVehicleFlags`) — vehicles (Example 32).
- `llReadKeyValue(key)`, `llCreateKeyValue(key, value)`,
  `llUpdateKeyValue(key, value)`, `llDeleteKeyValue(key)` — experience KVP,
  all dataserver-async (Example 21).
- `llJsonGetValue(json, path-list)`, `llJsonSetValue`, `llList2Json`,
  `llJson2List` — JSON handling; `JSON_INVALID` / `JSON_USE` sentinels.
- `llGetEnvironment(pos, params)` — EEP-era environment reads (Example 22).
- `llTarget(pos, tolerance)` / `llTargetRemove(handle)` / `llRotTarget(rot, error)`
  — target notifications (Example 29).
- `llAvatarOnSitTarget()` / `llAvatarOnLinkSitTarget(link)` — sitter queries.
- `llVolumeDetect(on)` — phantom-with-collision-events triggers (Example 18).
- `llParticleSystem(params)` — empty list turns the emitter off (Example 20).
- `llLoopSound(name, vol)`, `llTriggerSound(name, vol)`, `llPreloadSound(name)`,
  `llStopSound()` — audio (Example 28).

## Example 33 — Club light cycler across a linkset (fast link params in practice)

**What it does:** Cycles colours and glow across every prim in a linkset from one
script in the root, using `llSetLinkPrimitiveParamsFast` — the no-delay workhorse
that Example 2's notes pointed at. Shows link iteration, per-link targeting, and a
timer-driven effect that stays inside script-time budgets by doing bounded work
per tick.

```lsl
// Light cycler — root script drives the whole linkset.
// Work-per-tick discipline: each timer tick updates AT MOST 4 links, walking
// an index. A 60-prim linkset updated in one event would spike script time
// and delay every other event in this script; bounded batches do not.

integer gHueStep = 0;
integer gLinkCursor = 1;
integer LINKS_PER_TICK = 4;

vector hsv_to_rgb_approx(float h)
{
    // A tiny HSV wheel approximation good enough for decorative cycling.
    // (LSL has no HSV builtin; real colour work should use a fuller
    // conversion or precomputed palette lists.)
    float x = 1.0 - llFabs(llMod(h * 6.0, 2.0) - 1.0);
    integer sector = (integer)(h * 6.0) % 6;
    if (sector == 0) return <1.0, x, 0.0>;
    if (sector == 1) return <x, 1.0, 0.0>;
    if (sector == 2) return <0.0, 1.0, x>;
    if (sector == 3) return <0.0, x, 1.0>;
    if (sector == 4) return <x, 0.0, 1.0>;
    return <1.0, 0.0, x>;
}

default
{
    state_entry() { llSetTimerEvent(0.25); }

    timer()
    {
        integer total = llGetNumberOfPrims();
        integer done = 0;
        while (done < LINKS_PER_TICK && total > 0)
        {
            // Hue varies by link so the set ripples instead of blinking
            // in unison: link index offsets the wheel position.
            float h = llMod((float)(gHueStep + gLinkCursor * 3) / 60.0, 1.0);
            vector c = hsv_to_rgb_approx(h);
            llSetLinkPrimitiveParamsFast(gLinkCursor,
                [PRIM_COLOR, ALL_SIDES, c, 1.0,
                 PRIM_GLOW, ALL_SIDES, 0.25,
                 PRIM_FULLBRIGHT, ALL_SIDES, TRUE]);
            gLinkCursor++;
            if (gLinkCursor > total) gLinkCursor = 1;
            ++done;
        }
        ++gHueStep;
    }

    changed(integer change)
    {
        // Link count changed under us: clamp the cursor next tick by
        // re-reading llGetNumberOfPrims() there (already done per tick).
        if (change & CHANGED_LINK) gLinkCursor = 1;
    }
}
```

**Notes and pitfalls**

- `llSetLinkPrimitiveParamsFast` on `LINK_ALL_CHILDREN` etc. is also available;
  the cursor pattern here exists for *large* sets where even the fast call in
  bulk is too much for one event.
- Glow + fullbright on everything flattens a scene's lighting. Decorative
  cyclers belong on trim/accent prims; keep hero objects' materials alone.

---

## Example 34 — IM-to-email style gateway and offline messaging discipline

**What it does:** Demonstrates the messaging ladder available to a script —
`llInstantMessage` (any distance, works to offline avatars as offline IM in SL),
`llRegionSayTo` (region-local, no chat-window spam), and `llEmail` (legacy,
slow, heavily throttled) — and encodes the etiquette: pick the least intrusive
channel that reaches the person, and never loop IMs.

```lsl
// Notifier — sends ONE message per event, by the right channel.
// Throttle reality (SL): llEmail has a built-in delay of about 20 seconds
// per call and is unsuitable for interactive anything; llInstantMessage is
// near-instant and queues for offline delivery; llRegionSayTo only reaches
// avatars currently in the region.

notify(key who, string msg, integer allow_email)
{
    if (llGetAgentInfo(who) != 0)
    {
        // In this region (agent info available and non-zero does not prove
        // same-region in all cases; llRegionSayTo fails safe by simply not
        // delivering outside the region, so layer IM as the guarantee):
        llRegionSayTo(who, 0, msg);
    }
    llInstantMessage(who, msg);   // the guaranteed path, online or offline

    if (allow_email)
    {
        // Email addresses for avatars are "<uuid>@lsl.secondlife.com" for
        // script-to-avatar email in SL. Expect delays; never use in a loop.
        llEmail((string)who + "@lsl.secondlife.com",
                "Message from " + llGetObjectName(), msg);
    }
}

default
{
    touch_start(integer n)
    {
        notify(llDetectedKey(0),
               "You touched the notifier at " + llGetRegionName() + ".",
               FALSE);
        llOwnerSay("notified " + llDetectedName(0));
    }
}
```

**Notes and pitfalls**

- Offline IM delivery and caps (how many offline IMs are stored) are grid
  policy; OpenSim offline messaging depends on the grid's offline module and
  is frequently absent on standalones — design notifiers to degrade to
  in-region messages there.
- `llEmail` between objects uses object email addresses and is a legacy
  integration path; new systems use HTTP (Examples 6 and 7) instead.
- Messaging real people from scripts is a trust surface: identify the object
  and owner in the message (done implicitly above via object name in email,
  add it to IM text for products) and provide an opt-out in anything recurring.
