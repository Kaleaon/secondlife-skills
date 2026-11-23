# Client Example Library — LibreMetaverse, TypeScript, and Lumiya-Style Clients

Hand-written client code examples for the Second Life skills repo, in the three
stacks Joe's projects actually use:

- **C# / LibreMetaverse 3.x** — the semantic oracle. If a port disagrees with
  LibreMetaverse, the port is wrong until proven otherwise against viewer code.
- **TypeScript** — node-metaverse and React-Linkpoint patterns for web/React
  Native clients, including hand-rolled LLSD and Event Queue code for the places
  library coverage runs out.
- **Java / Kotlin** — Lumiya-style Android client code: raw UDP circuit, OkHttp
  caps, MFA login, coroutines for the event queue.

Conventions and warnings that apply to every example:

- **Credentials never appear in code.** Examples read passwords from environment
  variables or a secret store. A Second Life password in a source file is a
  compromised password: viewers and clients must never log it, and the TPV
  Policy forbids credential logging/sharing for distributed clients.
- **Grid selection is explicit.** Agni (production), Aditi (beta), and a local
  OpenSim standalone are different grids with different login URIs, inventories,
  and passwords that can diverge. Every example takes the grid as configuration.
- **Error handling is part of the example,** not an afterthought: login can fail
  with MFA challenges, caps can be absent, the UDP circuit can die silently, and
  the Event Queue is a long poll that fails routinely and must be restarted.
- Package and API notes are written against LibreMetaverse 3.x (the split
  packages: `.Protocol`, `.Transport`, `.StructuredData`, `.Assets`, `.Types`,
  `.ModelFormats`, `.Rendering.MeshFoundry`, `.Voice.*`). The old
  `OpenMetaverse.*` 2.x-era monolith APIs differ — where a 3.x name is
  version-sensitive, the comment says what to check in `MIGRATION.md`.

---

# Part 1 — C# with LibreMetaverse

## Example C1 — Login with GridClient, MFA awareness, and clean logout

**What it does:** The complete minimal client lifecycle: configure a
`GridClient`, subscribe to login/network events *before* logging in, log in with
structured status handling (including the failure reasons you actually get:
bad credentials, MFA required, grid maintenance, already logged in), announce
the seed capability and current simulator, and log out cleanly so the avatar
does not ghost in the region.

```csharp
// File: Program.cs  (.NET 8 console; dotnet add package LibreMetaverse)
// LibreMetaverse 3.x note: GridClient lives in the core LibreMetaverse
// package; packet types in LibreMetaverse.Protocol, the UDP circuit in
// LibreMetaverse.Transport, LLSD types (as OSD) in LibreMetaverse.StructuredData.

using System;
using System.Threading;
using System.Threading.Tasks;
using LibreMetaverse;

public static class LoginExample
{
    public static async Task<int> Main()
    {
        // --- Configuration: secrets from the environment, never source. ---
        string first   = Environment.GetEnvironmentVariable("SL_FIRST")   ?? "";
        string last    = Environment.GetEnvironmentVariable("SL_LAST")    ?? "";
        string pass    = Environment.GetEnvironmentVariable("SL_PASS")    ?? "";
        // Default login URI = Agni. For Aditi use the beta grid URI exposed by
        // LibreMetaverse's GridManager, and for a local OpenSim standalone use
        // "http://127.0.0.1:9000/" — the SAME binary can test all three grids
        // purely by configuration, which is the recommended dev loop.
        string loginUri = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? Settings.AGNI_LOGIN_SERVER;

        if (first.Length == 0 || pass.Length == 0)
        {
            Console.Error.WriteLine("Set SL_FIRST / SL_LAST / SL_PASS.");
            return 2;
        }

        var client = new GridClient();

        // Throttle tuning for a desktop/test client on a good link. Mobile
        // ports should lower texture/asset buckets; the simulator enforces
        // its own ceilings regardless of what you ask for.
        client.Throttle.Total = 1_400_000;      // bits-ish aggregate budget
        client.Throttle.Texture = 400_000;
        client.Throttle.Asset = 400_000;

        // --- Subscribe BEFORE Login(): several outcomes are event-only. ---
        var loginDone = new TaskCompletionSource<LoginStatus>();

        client.Network.LoginProgress += (_, e) =>
        {
            // LoginProgress fires for intermediate states (Connecting,
            // Authenticating, initialising inventory...) and the final state.
            Console.WriteLine($"[login] {e.Status}: {e.Message}");
            if (e.Status is LoginStatus.Success or LoginStatus.Failed)
                loginDone.TrySetResult(e.Status);
        };

        client.Network.SimConnected += (_, e) =>
            Console.WriteLine($"[net] connected to simulator {e.Simulator.Name} " +
                              $"({e.Simulator.IP}) handle={e.Simulator.Handle}");
        client.Network.Disconnected += (_, e) =>
            // DisconnectedEventArgs carries the reason: ClientInitiated,
            // ServerInitiated, NetworkTimeout, etc. A NetworkTimeout here with
            // no logout call means the circuit died — see Example C6 for the
            // reconnect policy; do NOT auto-relogin in a tight loop.
            Console.WriteLine($"[net] disconnected: {e.Reason} / {e.Message}");
        client.Network.EventQueueRunning += (_, _) =>
            Console.WriteLine("[net] Event Queue running (caps session live)");

        // --- Login parameters. ---
        var login = new LoginParams
        {
            LoginUri        = loginUri,
            FirstName       = first,
            LastName        = last,          // "Resident" for single-name accounts
            Password        = pass,
            Start           = "home",        // "home" | "last" | custom URI
            Channel         = "LibreMetaverseExample",
            Version         = "1.0.0",
            // MFA: if the account has MFA enabled, the first login attempt
            // fails with a message carrying an MFA challenge. Current
            // LibreMetaverse exposes Token/MFA fields on LoginParams in 3.x;
            // check MIGRATION.md for your exact version. The pattern is:
            // attempt -> detect MFA failure -> prompt user -> retry with the
            // token set. NEVER hard-code or persist the TOTP secret here.
            Token           = Environment.GetEnvironmentVariable("SL_MFA_TOKEN") ?? ""
        };

        bool submitted = client.Network.Login(login);
        if (!submitted)
        {
            Console.Error.WriteLine("Login could not even be submitted " +
                                    "(bad URI or already in progress).");
            return 3;
        }

        LoginStatus status = await loginDone.Task;
        if (status != LoginStatus.Success)
        {
            // Login failure messages from the grid are user-presentable but
            // vague by design (they do not distinguish "no such account" from
            // "wrong password"). Log the message verbatim for diagnosis, show
            // the user a generic credential error, and special-case the MFA
            // wording if you detect it.
            Console.Error.WriteLine($"Login failed. Final message from grid: " +
                                    $"{client.Network.LoginMessage}");
            return 4;
        }

        Console.WriteLine($"Logged in as {client.Self.Name} " +
                          $"agent={client.Self.AgentID}");
        Console.WriteLine($"Seed capability acquired; current sim: " +
                          $"{client.Network.CurrentSim?.Name}");

        // Keep the process alive briefly so Event Queue / object updates flow.
        // A real client runs until the user quits; a test client should still
        // demonstrate the graceful path below rather than being killed.
        await Task.Delay(TimeSpan.FromSeconds(10));

        // --- Clean logout: sends LogoutRequest, closes the circuit, and
        // prevents the "ghost avatar standing in the region for minutes"
        // failure that a killed process causes. ---
        client.Network.Logout();
        Console.WriteLine("Logged out cleanly.");
        return 0;
    }
}
```

**Notes and pitfalls**

- Login is the most version-sensitive surface in the library. Pin your
  LibreMetaverse version, read its `MIGRATION.md` on upgrades, and keep a
  packet-level log of one known-good login (TestClient) to diff against.
- Aditi passwords can diverge from Agni after password changes; "login works on
  Agni, fails on Aditi" is usually that, not your code.
- OpenSim standalone login URI ends at the ROBUST/standalone HTTP listener
  (port 9000 by default); capabilities and inventory behaviour there are
  OpenSim's subset, so a feature working locally can still fail on Agni if the
  cap differs (and vice versa).

---

## Example C2 — Chat and instant messages: listening, replying, and not spamming

**What it does:** Handles local chat (`ChatFromSimulator`), instant messages
including group IM and inventory offers (`ImprovedInstantMessage` surfaced as
IM events), responds to a `!time` command in local chat, and demonstrates the
etiquette baked into code: ignore your own messages, ignore non-chat IM types
unless you handle them, and never auto-reply in a loop to another bot.

```csharp
// Assumes an already logged-in GridClient (Example C1).
using System;
using LibreMetaverse;

public static class ChatExample
{
    public static void Attach(GridClient client)
    {
        // Local chat (say/whisper/shout within chat range of the avatar).
        client.Self.ChatFromSimulator += (_, e) =>
        {
            // ChatFromSimulator also reports YOUR OWN chat (source = you).
            // Bots that answer themselves are the classic first-day bug.
            if (e.SourceID == client.Self.AgentID) return;

            // Audible chat types: Say, Whisper, Shout, plus non-audible
            // types (Typing start/stop, animations). Filter to audible.
            if (e.Type is not (ChatType.Normal or ChatType.Whisper or ChatType.Shout))
                return;

            Console.WriteLine($"[chat] {e.FromName}: {e.Message}");

            if (e.Message.Trim().Equals("!time", StringComparison.OrdinalIgnoreCase))
            {
                // Self.Chat is UDP ChatFromViewer. ChatType.Normal = say.
                client.Self.Chat(DateTime.UtcNow.ToString("u") + " (UTC)",
                                 0, ChatType.Normal);
            }
        };

        // Instant messages: 1:1 IM, group IM, group notices, inventory
        // offers, teleport lures, friendship requests — ALL arrive through
        // the IM pipeline, discriminated by IMDialog. Handling "IM" as if
        // it were only chat is the second classic bug.
        client.Self.InstantMessage += (_, e) =>
        {
            switch (e.IM.Dialog)
            {
                case IMDialog.MessageFromAgent:
                    Console.WriteLine($"[im] {e.IM.FromAgentName}: {e.IM.Message}");
                    if (e.IM.FromAgentID != client.Self.AgentID &&
                        e.IM.Message.Trim() == "!ping")
                    {
                        client.Self.InstantMessage(e.IM.FromAgentID, "pong");
                    }
                    break;

                case IMDialog.InventoryOffered:
                    // An object or avatar is offering an item. e.IM contains
                    // the asset/inventory info; accepting is a separate
                    // inventory operation (Example C3 pattern) and should be
                    // an explicit policy decision in a bot, NOT automatic:
                    // auto-accepting from strangers fills inventory with junk
                    // and can be used to grief. Here: log and decline by
                    // doing nothing beyond this message.
                    Console.WriteLine($"[im] inventory offer from " +
                                      $"{e.IM.FromAgentName}: {e.IM.Message}");
                    break;

                case IMDialog.RequestTeleport:
                    Console.WriteLine($"[im] teleport lure from {e.IM.FromAgentName}");
                    // Accepting = client.Self.Teleport(...) to the lure
                    // location/session in e.IM — only do this for trusted
                    // senders in a real bot.
                    break;

                case IMDialog.GroupNotice:
                case IMDialog.GroupInvitation:
                case IMDialog.MessageFromObject:
                    Console.WriteLine($"[im:{e.IM.Dialog}] {e.IM.FromAgentName}: {e.IM.Message}");
                    break;

                default:
                    // Friendship offers, session invites, etc. Log unknown
                    // dialogs during development; silently ignore in prod.
                    Console.WriteLine($"[im:unhandled {e.IM.Dialog}] from {e.IM.FromAgentName}");
                    break;
            }
        };
    }
}
```

**Notes and pitfalls**

- Group IM sessions are *sessions*: they need a session join via caps
  (`ChatSessionRequest`) in a full client. LibreMetaverse handles much of this
  under the hood, but a from-scratch port must implement it or group chat will
  receive-but-not-send.
- Offline IMs arrive in a burst at login. A bot that answers every queued
  `!ping` from three days ago will spam; timestamp-check IMs you act on.
- OpenSim group chat and offline IM depend on grid modules and can be absent on
  a standalone — feature-detect by behaviour, not by assuming.

---
## Example C3 — Inventory: skeleton, folder walk, and finding an item by name

**What it does:** Waits for the inventory skeleton delivered at login, walks the
folder tree, finds an item by name, and prints its full identity — item ID,
asset ID, parent folder, type — because confusing item IDs with asset IDs is
the most persistent inventory bug across every client ever written.

```csharp
// Assumes a logged-in GridClient. Inventory in LibreMetaverse 3.x lives under
// client.Inventory with a Store rooted at the login skeleton.
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using LibreMetaverse;
using LibreMetaverse.Assets;

public static class InventoryExample
{
    public static async Task WalkAndFind(GridClient client, string wantedName)
    {
        // The skeleton arrives with the login response, but folder CONTENTS
        // are fetched on demand (FetchInventory2 / AIS under the hood).
        // InventoryRoot is null until the skeleton is in: always null-check.
        var root = client.Inventory.Store.RootFolder;
        if (root == null)
        {
            Console.WriteLine("Inventory skeleton not loaded yet.");
            return;
        }

        Console.WriteLine($"Inventory root: {root.Name} ({root.UUID})");

        // Depth-first walk of the local store. This only sees folders/items
        // already fetched; use FetchFolderContents for folders you have not
        // opened yet (see below).
        var stack = new Stack<InventoryFolder>();
        stack.Push(root);
        InventoryItem? found = null;

        while (stack.Count > 0)
        {
            var folder = stack.Pop();
            foreach (var node in client.Inventory.Store.GetContents(folder))
            {
                if (node is InventoryFolder child) stack.Push(child);
                else if (node is InventoryItem item &&
                         item.Name.Equals(wantedName, StringComparison.OrdinalIgnoreCase))
                {
                    found = item;
                }
            }
        }

        if (found == null)
        {
            Console.WriteLine($"'{wantedName}' not found in fetched inventory. " +
                              "It may live in a folder whose contents were " +
                              "never fetched — fetch folders explicitly.");
        }
        else
        {
            // THE distinction, printed so it can never be blurred:
            //   ItemID  (InventoryItem.UUID) — this entry in YOUR inventory.
            //             Two copies of the same object have different item IDs.
            //   AssetID (InventoryItem.AssetUUID) — the underlying asset on
            //             the asset server. Copies can share an asset ID.
            //   ParentID — the folder (item ID space) containing this item.
            // AIS3 operations address items/folders; asset fetches address
            // asset IDs. Sending one where the other belongs is a silent
            // server-side no-result, not an error.
            Console.WriteLine($"Found '{found.Name}'");
            Console.WriteLine($"  item id   : {found.UUID}");
            Console.WriteLine($"  asset id  : {found.AssetUUID}");
            Console.WriteLine($"  parent    : {found.ParentUUID}");
            Console.WriteLine($"  type      : inv={found.InventoryType} asset={found.AssetType}");
            Console.WriteLine($"  perms     : {found.Permissions}");
        }

        // Fetching a folder's contents over the wire (async, caps-based in
        // modern grids). OwnerType distinguishes agent inventory from the
        // shared Library. Await it; fire-and-forget fetches race the walk.
        try
        {
            await client.Inventory.FetchFolderContents(
                root.UUID, client.Self.AgentID,
                true,   // fetch folders
                true,   // fetch items
                InventorySortOrder.ByDate);
            Console.WriteLine("Root folder contents refreshed from server.");
        }
        catch (Exception ex)
        {
            // Fetch failures are routine (cap missing on an old OpenSim,
            // region change mid-fetch). Log and keep the cached skeleton.
            Console.WriteLine($"Folder fetch failed (cached data kept): {ex.Message}");
        }
    }
}
```

**Notes and pitfalls**

- Current Outfit Folder (COF) and links: wearing an item in modern SL creates
  *links* in COF pointing at the real item. Deleting the link is not deleting
  the item; deleting the item breaks the link. Any inventory UI must model
  links (`InventoryItem.IsLink()` style checks in 3.x) or users will destroy
  outfits.
- AIS3 vs legacy UDP inventory: create/update/link operations go through AIS3
  caps on Agni; OpenSim support is partial. LibreMetaverse abstracts most of
  it, but a "works on OpenSim, fails on Agni" inventory bug is often an AIS
  payload shape — diff against viewer `llaisapi.cpp`.
- Fetch is paginated and slow on huge inventories (100k+ items exist). Never
  block a UI thread on a full walk; this example is a console tool.

---

## Example C4 — Object tracking: ObjectUpdate, terse updates, and a live object table

**What it does:** Maintains a dictionary of everything the simulator tells the
client about — full `ObjectUpdate` for new objects, compressed/terse updates
for movement — and prints a coherent picture: prims, avatars, attachments.
This is the data foundation of any radar, renderer, or bot awareness.

```csharp
// Object/scene tracking with the Objects manager (client.Objects).
using System;
using System.Collections.Concurrent;
using LibreMetaverse;

public static class ObjectTrackingExample
{
    // Simulator-scoped: local IDs are only unique PER SIMULATOR. The key
    // below pairs the simulator handle with the local ID. Keying by local ID
    // alone corrupts the table the moment you can see a neighbour region.
    private static readonly ConcurrentDictionary<(ulong, uint), Primitive> Table = new();

    public static void Attach(GridClient client)
    {
        // Full object update: a new object (or a property refresh). Prim
        // carries prim params, textures (Text.Data is the LLSD-ish texture
        // entry blob — decode via the TextureEntry helpers, not by hand),
        // position/rotation/scale, and flags (physics, phantom, etc.).
        client.Objects.ObjectUpdate += (_, e) =>
        {
            var key = (e.Simulator.Handle, e.Prim.LocalID);
            Table[key] = e.Prim;
            if (e.Prim is Avatar av)
                Console.WriteLine($"[obj] avatar {av.Name} at {av.Position}");
        };

        // Terse updates: position/velocity/rotation only, heavily quantised
        // on the wire (see secondlife_protocol). They arrive at a much higher
        // rate than full updates. The handler must be CHEAP: update the
        // stored prim, do no logging, no allocation-heavy work.
        client.Objects.TerseObjectUpdate += (_, e) =>
        {
            var key = (e.Simulator.Handle, e.Prim.LocalID);
            if (Table.TryGetValue(key, out var existing))
            {
                existing.Position = e.Prim.Position;
                existing.Rotation = e.Prim.Rotation;
                existing.Velocity = e.Prim.Velocity;
            }
            else
            {
                // A terse update for an unknown object means we missed (or
                // have not yet received) its full update. Store the stub;
                // the full update will fill it in. Do NOT treat the stub as
                // renderable — it lacks textures and prim params.
                Table[key] = e.Prim;
            }
        };

        // Object killed (left view, derezzed, region crossing cleanup).
        client.Objects.KillObject += (_, e) =>
        {
            foreach (var localId in e.IDs)
                Table.TryRemove((e.Simulator.Handle, localId), out _);
        };

        // Avatars are Prims with Avatar subclass data; sitting avatars are
        // reported with ParentID = the object they sit on. An avatar whose
        // ParentID is another avatar's target etc. is attachment logic —
        // check Prim.ParentID before treating Position as region-absolute:
        // for child prims and attachments Position is LOCAL to the parent.
    }

    public static void DumpSummary()
    {
        int prims = 0, avatars = 0;
        foreach (var p in Table.Values)
        {
            if (p is Avatar) avatars++; else prims++;
        }
        Console.WriteLine($"tracked: {prims} prims, {avatars} avatars");
    }
}
```

**Notes and pitfalls**

- Position semantics: root prims use region coordinates; child prims and
  attachments use parent-local coordinates. Every renderer and radar learns
  this the hard way exactly once.
- Terse quantisation jitter is a *protocol property*, not a bug in your code:
  smoothing/interpolation belongs in the presentation layer.
- ObjectUpdate floods on region entry can be thousands of prims. Backpressure
  (queue + batch processing) is a design requirement for mobile ports.

---

## Example C5 — Teleport, friends, and group basics with event completion

**What it does:** Shows the request/event shape of three social operations that
are *not* synchronous calls: teleport (start/progress/finish/failed), friends
(online notifications, offering friendship), and groups (list, activate).
Each demonstrates the rule: issue the request, await the terminal event, and
always handle the failure event, because teleports fail routinely.

```csharp
using System;
using System.Threading.Tasks;
using LibreMetaverse;

public static class SocialExample
{
    public static async Task<bool> TeleportHome(GridClient client)
    {
        var done = new TaskCompletionSource<bool>();

        void OnTeleport(object? s, TeleportEventArgs e)
        {
            // TeleportStatus: Start, Progress (with message), Finished,
            // Failed. Progress can repeat (multiple region handoffs).
            Console.WriteLine($"[tp] {e.Status}: {e.Message}");
            if (e.Status == TeleportStatus.Finished) done.TrySetResult(true);
            if (e.Status == TeleportStatus.Failed) done.TrySetResult(false);
        }

        client.Self.TeleportProgress += OnTeleport;
        try
        {
            // TeleportHome is the simplest target. Landmark/position
            // teleports use other Self.Teleport overloads (landmark asset,
            // or simulator name + local position).
            client.Self.TeleportHome();
            // Timeout: a teleport that never terminates is a real failure
            // mode (destination region down). Never await forever.
            var finished = await Task.WhenAny(done.Task, Task.Delay(30_000));
            return finished == done.Task && done.Task.Result;
        }
        finally
        {
            client.Self.TeleportProgress -= OnTeleport;
        }
    }

    public static void AttachSocial(GridClient client)
    {
        // Friend online/offline notifications arrive after login and on change.
        client.Friends.FriendOnline += (_, e) =>
            Console.WriteLine($"[friend] {e.Friend.Name} came online");
        client.Friends.FriendOffline += (_, e) =>
            Console.WriteLine($"[friend] {e.Friend.Name} went offline");
        // Offering friendship: client.Friends.OfferFriendship(agentId, msg)
        // Accepting/declining arrives via IM dialog types (Example C2) and
        // friendship caps/UDP in the library internals.

        client.Groups.GroupMembersReply += (_, e) =>
            Console.WriteLine($"[group] {e.GroupID}: {e.Members.Count} members replied");
        // Listing your groups: client.Groups.Groups (dictionary populated
        // from the login/agent data); activating a group tag is a profile
        // update via client.Self / Groups in 3.x — check the version's API,
        // this surface moved between 2.x and 3.x.
    }
}
```

**Notes and pitfalls**

- A teleport invalidates your cap map and circuit: after `Finished`, every cap
  URL from the old region is dead. Clients that cache caps across teleports
  fail with confusing 404s — rebuild from the new seed (the library does this;
  hand-rolled caps code must too, see Example T2).
- Teleport into a full or restarting region returns `Failed` with a message
  meant for the user. Surface it; do not retry in a loop (region-full retries
  are how clients get rate-limited).
- OpenSim teleports between regions on the same grid are similar; Hypergrid
  teleports are a different trust and asset story entirely.

---
## Example C6 — A resilient bot skeleton: reconnect policy, heartbeat, command loop

**What it does:** Wraps C1–C5 into the skeleton of a bot that can run for days:
exponential-backoff relogin (with jitter and a cap), a watchdog that notices a
half-dead circuit, graceful shutdown on cancellation, and a hard rule against
relogin storms. This structure matters more than any single API call.

```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
using LibreMetaverse;

public sealed class ResilientBot
{
    private readonly GridClient _client = new();
    private DateTime _lastPacketUtc = DateTime.UtcNow;
    private int _consecutiveFailures = 0;

    public async Task RunAsync(CancellationToken ct)
    {
        _client.Network.PacketReceived += (_, _) => _lastPacketUtc = DateTime.UtcNow;
        // Attach ChatExample/ObjectTrackingExample handlers here (once —
        // re-subscribing on every reconnect double-fires every handler).

        while (!ct.IsCancellationRequested)
        {
            try
            {
                bool ok = await LoginOnce(ct);
                if (!ok) throw new InvalidOperationException("login failed");

                _consecutiveFailures = 0;
                Console.WriteLine("[bot] online");

                // Supervise loop: exit when disconnected or when the circuit
                // has been silent far longer than the ping interval allows.
                while (!ct.IsCancellationRequested && _client.Network.Connected)
                {
                    await Task.Delay(5_000, ct);
                    if (DateTime.UtcNow - _lastPacketUtc > TimeSpan.FromSeconds(90))
                    {
                        Console.WriteLine("[bot] circuit silent 90s — treating as dead");
                        _client.Network.Logout();
                        break;
                    }
                }
            }
            catch (OperationCanceledException) { break; }
            catch (Exception ex)
            {
                Console.WriteLine($"[bot] session ended: {ex.Message}");
            }

            if (ct.IsCancellationRequested) break;

            // Backoff: 10s, 20s, 40s ... capped at 5 min, plus jitter so a
            // fleet of bots (or a grid-wide outage ending) does not produce
            // a synchronised relogin thundering herd. After repeated failure,
            // STOP and ask a human: persistent login failure is usually
            // credentials, MFA, or a grid ban — all human problems.
            _consecutiveFailures++;
            if (_consecutiveFailures >= 8)
            {
                Console.Error.WriteLine("[bot] 8 consecutive failures — giving up for operator review.");
                break;
            }
            var delay = TimeSpan.FromSeconds(Math.Min(300, 10 * Math.Pow(2, _consecutiveFailures - 1)));
            delay += TimeSpan.FromSeconds(Random.Shared.Next(0, 10));
            Console.WriteLine($"[bot] relogin in {delay.TotalSeconds:F0}s (attempt {_consecutiveFailures})");
            try { await Task.Delay(delay, ct); }
            catch (OperationCanceledException) { break; }
        }

        if (_client.Network.Connected) _client.Network.Logout();
        Console.WriteLine("[bot] stopped");
    }

    private async Task<bool> LoginOnce(CancellationToken ct)
    {
        // Same LoginParams construction as Example C1, factored out in a real
        // project. Returns the terminal LoginStatus == Success as a bool and
        // honours ct so Ctrl-C during a slow login still shuts down.
        var tcs = new TaskCompletionSource<bool>();
        void Handler(object? s, LoginProgressEventArgs e)
        {
            if (e.Status == LoginStatus.Success) tcs.TrySetResult(true);
            else if (e.Status == LoginStatus.Failed) tcs.TrySetResult(false);
        }
        _client.Network.LoginProgress += Handler;
        try
        {
            var p = new LoginParams
            {
                LoginUri = Environment.GetEnvironmentVariable("SL_LOGIN_URI") ?? Settings.AGNI_LOGIN_SERVER,
                FirstName = Environment.GetEnvironmentVariable("SL_FIRST") ?? "",
                LastName = Environment.GetEnvironmentVariable("SL_LAST") ?? "",
                Password = Environment.GetEnvironmentVariable("SL_PASS") ?? "",
                Start = "last",
                Channel = "ResilientBotExample",
                Version = "1.0.0"
            };
            if (!_client.Network.Login(p)) return false;
            using var reg = ct.Register(() => tcs.TrySetCanceled(ct));
            return await tcs.Task;
        }
        finally { _client.Network.LoginProgress -= Handler; }
    }
}
```

**Notes and pitfalls**

- Reconnect policy is grid etiquette, not just engineering: Linden Lab can and
  does throttle or block abusive relogin patterns. Backoff is mandatory.
- Handler subscription leaks are the #1 long-uptime bot bug: after the third
  reconnect the bot answers every chat three times. Subscribe once, or
  subscribe/unsubscribe in matched pairs as in C5.
- A "connected but silent" circuit (NAT timeout, dead sim) is more common than
  a clean disconnect — hence the packet watchdog, not just the Connected flag.

---

## Example C7 — Downloading a texture and a mesh asset by UUID

**What it does:** Fetches a texture asset over the HTTP caps path and decodes
its JPEG2000 discard levels conceptually, then fetches a mesh asset and lists
its LOD sections via ModelFormats/MeshFoundry concepts. Shows the asset-ID
discipline from C3 applied to real fetches, with timeouts.

```csharp
// Asset fetch patterns. Exact helper names vary slightly across 3.x minor
// versions; the SHAPE (request by asset UUID, async result with Success flag,
// timeout) is stable and is what a port must reproduce.
using System;
using System.Threading.Tasks;
using LibreMetaverse;
using LibreMetaverse.Assets;

public static class AssetFetchExample
{
    public static async Task FetchTexture(GridClient client, UUID assetId)
    {
        // Textures are JPEG2000 codestreams. The client library's Assets
        // manager requests them via the GetTexture cap in modern grids and
        // can return progressive discard levels. For a thumbnail, request
        // the lowest useful discard first — on mobile this is the difference
        // between a snappy inventory grid and a slideshow.
        var result = await client.Assets.RequestTexture(assetId);
        if (!result.Success)
        {
            Console.WriteLine($"texture {assetId} failed: {result.Status}");
            return;
        }
        Console.WriteLine($"texture {assetId}: {result.AssetData.Length} bytes (J2C)");
        // Decode with the Imaging stack (LibreMetaverse.Imaging.*, CSJ2K
        // lineage) when you need pixels. Keep the raw codestream if you are
        // caching: re-encoding JPEG2000 is lossy and slow, never transcode
        // the cache copy.
    }

    public static async Task FetchMeshInfo(GridClient client, UUID assetId)
    {
        var result = await client.Assets.RequestMesh(assetId);
        if (!result.Success)
        {
            Console.WriteLine($"mesh {assetId} failed: {result.Status}");
            return;
        }
        // AssetMesh wraps the LLMesh binary: header + per-LOD sections +
        // physics + skin. Parsing it yourself is a solved problem — use
        // LibreMetaverse.ModelFormats / Rendering.MeshFoundry to turn it
        // into geometry instead of reading the binary layout by hand.
        var mesh = result.Asset as AssetMesh;
        Console.WriteLine($"mesh {assetId}: {result.AssetData.Length} bytes, " +
                          $"parsed={(mesh != null)}");
    }
}
```

**Notes and pitfalls**

- Asset fetches fail with "missing asset" for genuinely deleted content and
  for wrong-ID bugs (item ID sent as asset ID) identically. Log which ID space
  you used, or you will chase ghosts.
- Cache by asset UUID forever: assets are immutable. If bytes for a UUID
  change, something is deeply wrong (or you are on an OpenSim grid with
  mutable asset experiments — treat that as a different cache domain).
- OpenSim asset service behaviour (HTTP asset server, negative caching)
  differs from Agni's; a fetch storm that Agni absorbs can crush a small
  standalone. Throttle bulk fetch tools.

---

# Part 2 — TypeScript (node-metaverse and React-Linkpoint patterns)

## Example T1 — LLSD encode/decode in TypeScript without a library

**What it does:** A compact, correct-enough LLSD XML encoder/decoder for the
shapes login and caps actually use — maps, arrays, strings, integers, reals,
booleans, UUIDs, dates, binary (base64), and undef — with the three interop
traps called out in code: 64-bit values vs JS `number`, binary as base64, and
date formatting. In production prefer `@caspertech/llsd` (the maintained
package); this example exists so you understand what it does for you.

```typescript
// llsd.ts — minimal LLSD (XML serialisation) for login/caps payloads.
// Types: LLSDValue mirrors the LLSD type system, NOT plain JSON:
//   - integers are 32-bit; a JS number is fine, a BigInt is not LLSD
//   - reals are doubles (JS number, fine)
//   - binary is a Uint8Array on the wire as base64 in XML
//   - dates are ISO-8601 strings in XML
//   - UUID is a string type distinct from string (tag matters to parsers)

export type LLSDValue =
  | undefined
  | boolean
  | number            // integer or real — see encode note below
  | string
  | Uint8Array        // binary
  | Date
  | LLSDValue[]
  | { [key: string]: LLSDValue };

// Marker wrapper so callers can force integer vs real encoding: LLSD XML
// distinguishes <integer> from <real>, and some simulator endpoints are
// picky. JSON.stringify-style "it's all numbers" loses this.
export class LLSDReal { constructor(public value: number) {} }
export class LLSDUUID { constructor(public value: string) {} }

function escapeXml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

export function encodeLLSD(v: LLSDValue): string {
  return `<?xml version="1.0" encoding="UTF-8"?><llsd>${encodeValue(v)}</llsd>`;
}

function encodeValue(v: LLSDValue): string {
  if (v === undefined) return "<undef/>";
  if (typeof v === "boolean") return `<boolean>${v ? "1" : "0"}</boolean>`;
  if (v instanceof LLSDReal) return `<real>${v.value}</real>`;
  if (v instanceof LLSDUUID) return `<uuid>${v.value}</uuid>`;
  if (typeof v === "number") {
    // Integers must encode as <integer>. A non-integer number here is a
    // caller bug in LLSD-land; encode as real rather than truncating.
    return Number.isInteger(v) ? `<integer>${v}</integer>` : `<real>${v}</real>`;
  }
  if (typeof v === "string") return `<string>${escapeXml(v)}</string>`;
  if (v instanceof Uint8Array) {
    // base64 without line breaks; simulator parsers accept wrapped base64
    // too, but unwrapped is the safe common denominator.
    return `<binary>${Buffer.from(v).toString("base64")}</binary>`;
  }
  if (v instanceof Date) return `<date>${v.toISOString()}</date>`;
  if (Array.isArray(v)) return `<array>${v.map(encodeValue).join("")}</array>`;
  const entries = Object.entries(v)
    .map(([k, val]) => `<key>${escapeXml(k)}</key>${encodeValue(val)}`)
    .join("");
  return `<map>${entries}</map>`;
}

// Decoding real simulator XML needs a real XML parser in production
// (fast-xml-parser or similar, configured to preserve tag names). The shape
// below documents the mapping such a decoder must implement; do not ship a
// regex XML parser — simulator LLSD includes nested maps, empty elements,
// and escaped entities that break regexes in production, not in tests.
//   <undef/>            -> undefined
//   <boolean>1</boolean>-> true
//   <integer>           -> number (check range: LLSD ints are 32-bit)
//   <real>              -> number
//   <string>            -> string (entity-decoded)
//   <uuid>              -> string (keep as its own class if you re-encode)
//   <binary>            -> Uint8Array from base64
//   <date>              -> Date
//   <uri>               -> string
//   <array>/<map>       -> recursive
```

**Notes and pitfalls**

- LLSD has a *binary* serialisation too (used by some endpoints). If an
  endpoint returns binary LLSD and you feed it to an XML decoder you get
  garbage with no error — check Content-Type (`application/llsd+xml` vs
  binary) before decoding.
- The `@caspertech/llsd` package (dependency of node-metaverse) is the
  maintained TS implementation; hand-rolled code like the above is for
  understanding and for tiny embedded uses, and must be fuzz-tested against
  LibreMetaverse.StructuredData outputs before it carries login traffic.
- UUID case: simulators emit lowercase; comparisons should be
  case-insensitive or normalised at parse time.

---
## Example T2 — Seed capability exchange and a typed caps client

**What it does:** Performs the seed-cap POST (LLSD array of wanted cap names →
LLSD map of name to URL), stores the result as the session's cap map, and
wraps two real caps — `SimulatorFeatures` and `FetchInventoryDescendents2`
shape — with absence handling. This is the code every thin client rewrites
once; write it once, correctly.

```typescript
// caps.ts — seed capability exchange + typed cap calls.
// Facts encoded here:
//  * Cap URLs are per-region, per-session, unguessable, and DIE on teleport.
//    This class is rebuilt on every region arrival. Never persist cap URLs.
//  * A requested cap may simply be absent (old sim, OpenSim subset, feature
//    off). Absence is normal control flow, not an exception.
//  * Content type is application/llsd+xml unless viewer code says otherwise.

import { encodeLLSD, type LLSDValue } from "./llsd";

export class CapMap {
  private urls = new Map<string, string>();

  static async fromSeed(seedUrl: string, wanted: string[],
                        fetchFn: typeof fetch = fetch): Promise<CapMap> {
    const body = encodeLLSD(wanted);
    const res = await fetchFn(seedUrl, {
      method: "POST",
      headers: { "Content-Type": "application/llsd+xml" },
      body,
    });
    if (!res.ok) throw new Error(`seed cap POST failed: HTTP ${res.status}`);
    const xml = await res.text();
    const parsed = parseLLSDXml(xml) as Record<string, LLSDValue>;
    const map = new CapMap();
    for (const [name, url] of Object.entries(parsed)) {
      if (typeof url === "string" && url.startsWith("http")) map.urls.set(name, url);
    }
    return map;
  }

  has(name: string): boolean { return this.urls.has(name); }
  url(name: string): string {
    const u = this.urls.get(name);
    if (!u) throw new Error(`capability not granted: ${name}`);
    return u;
  }
  /** POST LLSD to a cap and parse the LLSD reply; returns undefined if absent. */
  async post(name: string, payload: LLSDValue,
             fetchFn: typeof fetch = fetch): Promise<LLSDValue> {
    if (!this.has(name)) return undefined;
    const res = await fetchFn(this.url(name), {
      method: "POST",
      headers: { "Content-Type": "application/llsd+xml" },
      body: encodeLLSD(payload),
    });
    if (!res.ok) throw new Error(`cap ${name} failed: HTTP ${res.status}`);
    return parseLLSDXml(await res.text());
  }
}

// parseLLSDXml: plug in @caspertech/llsd's parser or your platform XML->LLSD
// decoder (see Example T1 for the mapping). Declared here so the example is
// honest about its one external dependency.
declare function parseLLSDXml(xml: string): LLSDValue;

// --- Using it: the caps a thin client requests on region arrival. ---
export const THIN_CLIENT_CAPS = [
  "EventQueueGet",
  "FetchInventory2", "FetchInventoryDescendents2",
  "FetchLib2", "FetchLibDescendents2",
  "InventoryAPIv3", "LibraryAPIv3",          // AIS3
  "GetTexture", "GetMesh", "GetMesh2",
  "SimulatorFeatures",
  "EnvironmentSettings", "ExtEnvironment",   // EEP
  "GetDisplayNames", "ChatSessionRequest",
  "AgentPreferences", "ServerReleaseNotes",
];

export async function querySimulatorFeatures(caps: CapMap) {
  // SimulatorFeatures is a GET-style cap in viewer code (no body). It tells
  // you mesh/PBR/voice limits for THIS region — query it, never hardcode.
  if (!caps.has("SimulatorFeatures")) return undefined;
  const res = await fetch(caps.url("SimulatorFeatures"));
  if (!res.ok) return undefined;
  return parseLLSDXml(await res.text());
}
```

**Notes and pitfalls**

- The wanted-list must be the union of what viewer code requests
  (`llviewerregion.cpp buildCapabilityNames` plus `llaisapi.cpp` for AIS) —
  requesting a cap the sim supports but you forgot is indistinguishable from
  the sim not supporting it.
- React Native / browser fetch: the simulator's cap hosts are plain HTTPS with
  no CORS headers for browsers. Web clients need a proxy or a native network
  layer; React-Linkpoint style apps run caps through the native side or a
  backend, never browser fetch directly. Plan for this before UI work.
- Cap URLs contain a UUID path segment; logging them at debug level leaks a
  session capability. Redact in logs you share.

---

## Example T3 — EventQueueGet long-poll loop (the heartbeat of a thin client)

**What it does:** The complete EQG client loop: POST with the last event id,
parse the events array, dispatch each event by name, ack correctly, back off
on errors, and stop cleanly. Everything a thin client "receives" unsolicited —
teleports, IM-ish events, inventory offers, group notices, lures — arrives
here. If this loop dies, the client looks logged in but is deaf.

```typescript
// eventqueue.ts — EventQueueGet client.
// Protocol shape (from viewer llmessage / Event Queue code):
//   request : LLSD map { ack: <last event id or undef>, done: false }
//   response: LLSD map { id: <new last id>, events: [ {message, body}, ... ] }
// The POST is a LONG POLL: the simulator holds it open until events exist or
// a timeout (tens of seconds). An immediate empty reply is also legal.

import type { CapMap } from "./caps";
import { encodeLLSD, type LLSDValue } from "./llsd";

export type EQEvent = { message: string; body: LLSDValue };
export type EQHandler = (ev: EQEvent) => void | Promise<void>;

export class EventQueue {
  private ack: LLSDValue = undefined;   // undef ack = "start of queue"
  private running = false;

  constructor(private caps: CapMap, private onEvent: EQHandler) {}

  stop(): void { this.running = false; }

  async run(): Promise<void> {
    this.running = true;
    let errorStreak = 0;
    while (this.running) {
      try {
        const url = this.caps.url("EventQueueGet");
        const res = await fetch(url, {
          method: "POST",
          headers: { "Content-Type": "application/llsd+xml" },
          body: encodeLLSD({ ack: this.ack, done: false }),
        });
        if (!res.ok) throw new Error(`EQG HTTP ${res.status}`);
        const data = parseLLSDXml(await res.text()) as {
          id?: LLSDValue; events?: Array<{ message: string; body: LLSDValue }>;
        };
        // Advance the ack BEFORE dispatching: if a handler throws, we must
        // not redeliver the same batch forever. (Trade-off: a crashing
        // handler loses that batch. Log handler errors loudly to compensate.)
        if (data && "id" in data) this.ack = data.id;
        errorStreak = 0;
        for (const ev of data?.events ?? []) {
          try { await this.onEvent(ev); }
          catch (err) { console.error(`[eq] handler failed for ${ev.message}`, err); }
        }
      } catch (err) {
        // Routine failures: long-poll timeouts at proxies, region restarts,
        // teleport (the cap URL is now dead — the owner must rebuild the
        // CapMap and construct a new EventQueue; detect that by checking
        // whether this queue's caps are stale, handled by the caller).
        errorStreak++;
        const backoff = Math.min(30_000, 1000 * 2 ** errorStreak);
        console.warn(`[eq] poll failed (${errorStreak}), retry in ${backoff}ms`, err);
        await new Promise(r => setTimeout(r, backoff));
        if (errorStreak >= 10) throw new Error("EventQueueGet: giving up after 10 failures");
      }
    }
    // Polite shutdown: a final POST with done:true tells the simulator this
    // queue is finished (viewer does this on logout/region departure).
    try {
      await fetch(this.caps.url("EventQueueGet"), {
        method: "POST",
        headers: { "Content-Type": "application/llsd+xml" },
        body: encodeLLSD({ ack: this.ack, done: true }),
      });
    } catch { /* best effort only */ }
  }
}

declare function parseLLSDXml(xml: string): LLSDValue;

// Dispatch table pattern for the caller's onEvent:
//   switch (ev.message) {
//     case "TeleportFinish": ...        // rebuild caps for the new region!
//     case "ChatterBoxInvitation": ...  // group/conference chat session
//     case "ChatterBoxSessionEventReply": ...
//     case "OfferCallingCard": ...
//     case "GroupNotice": ...           // (also arrives via IM in some paths)
//     case "ScriptRunningReply": ...
//     default: log in development, ignore in production.
//   }
```

**Notes and pitfalls**

- Teleport handling is the subtle part: `TeleportFinish` (via EQG and/or UDP)
  means a NEW seed cap, NEW cap map, NEW event queue. Reusing the old queue is
  the classic "everything stops after first teleport" bug.
- Some events exist in both UDP and EQG forms historically; deduplicate by
  content (sender + timestamp + type) if you consume both planes.
- Mobile OS background limits kill long polls. On resume, restart the loop and
  expect a burst of queued events; make handlers idempotent.

---

## Example T4 — UDP packet header parsing and ZeroDecode in TypeScript

**What it does:** Parses the 6-byte UDP packet header, appended ACKs, and
message-ID-by-frequency, and implements ZeroDecode/ZeroEncode — the three
pieces of the wire protocol every from-scratch TS client needs before any
message can be read. Written against the template semantics in
`secondlife_protocol`, with the zerocoded-flag warning in code.

```typescript
// packet.ts — UDP packet framing for the simulator circuit.
// Packet layout:
//   byte 0     : flags  (0x80 Zerocoded, 0x40 Reliable, 0x20 Resent, 0x10 Ack)
//   bytes 1..4 : sequence number, big-endian U32
//   byte 5     : extra header length (usually 0)
//   ...        : extra header bytes, then message body
//   if Ack flag: body is followed by ack count byte + that many U32 sequences
// Message ID is the FIRST body bytes, width by frequency:
//   High: 1 byte (0x01..0xFE) | Medium: 2 bytes (0xFF xx)
//   Low: 4 bytes (0xFF 0xFF xx xx) | Fixed: 4 bytes (0xFF 0xFF 0xFF xx)

export interface PacketHeader {
  zerocoded: boolean; reliable: boolean; resent: boolean; hasAcks: boolean;
  sequence: number; extraLength: number; bodyOffset: number;
  appendedAcks: number[];
}

export function parseHeader(buf: Uint8Array): PacketHeader {
  if (buf.length < 6) throw new Error("packet shorter than header");
  const flags = buf[0];
  const view = new DataView(buf.buffer, buf.byteOffset, buf.byteLength);
  const sequence = view.getUint32(1, false); // big-endian
  const extraLength = buf[5];
  const hasAcks = (flags & 0x10) !== 0;

  const appendedAcks: number[] = [];
  let bodyEnd = buf.length;
  if (hasAcks) {
    const count = buf[buf.length - 1];
    // Acks sit at the very END: count byte last, preceded by count U32s.
    const ackStart = buf.length - 1 - count * 4;
    if (ackStart < 6 + extraLength) throw new Error("ack block overlaps header");
    for (let i = 0; i < count; i++) appendedAcks.push(view.getUint32(ackStart + i * 4, false));
    bodyEnd = ackStart;
  }
  return {
    zerocoded: (flags & 0x80) !== 0,
    reliable: (flags & 0x40) !== 0,
    resent: (flags & 0x20) !== 0,
    hasAcks, sequence, extraLength,
    bodyOffset: 6 + extraLength,
    appendedAcks,
    // (bodyEnd is used by the caller to slice the body; returned in real code)
  } as PacketHeader;
}

/** ZeroDecode: expand 0x00 <count> runs. Applied ONLY to packets/blocks the
 *  message template marks zerocoded — the template has been wrong before
 *  (ChatFromViewer), so this flag must come from a template diffed against
 *  the viewer's shipped copy, not from the master template alone. */
export function zeroDecode(input: Uint8Array): Uint8Array {
  const out: number[] = [];
  for (let i = 0; i < input.length; i++) {
    const b = input[i];
    out.push(b);
    if (b === 0x00 && i + 1 < input.length) {
      const count = input[++i];
      for (let n = 1; n < count; n++) out.push(0x00);
    }
  }
  return new Uint8Array(out);
}

export function zeroEncode(input: Uint8Array): Uint8Array {
  const out: number[] = [];
  let i = 0;
  while (i < input.length) {
    if (input[i] !== 0x00) { out.push(input[i++]); continue; }
    let run = 0;
    while (i < input.length && input[i] === 0x00 && run < 0xff) { run++; i++; }
    out.push(0x00, run);
  }
  return new Uint8Array(out);
}

/** Message number + frequency from the body start. The number is meaningful
 *  only together with its frequency — (Low, 7) and (High, 7) are different
 *  messages. Generated dispatch tables (from message_template.msg) key on
 *  the pair, exactly like LibreMetaverse.Protocol does. */
export function parseMessageId(body: Uint8Array):
  { frequency: "High" | "Medium" | "Low" | "Fixed"; number: number; headerBytes: number } {
  if (body[0] !== 0xff) return { frequency: "High", number: body[0], headerBytes: 1 };
  if (body[1] !== 0xff) return { frequency: "Medium", number: body[1], headerBytes: 2 };
  if (body[2] !== 0xff) {
    return { frequency: "Low", number: (body[2] << 8) | body[3], headerBytes: 4 };
  }
  return { frequency: "Fixed", number: body[3], headerBytes: 4 };
}
```

**Notes and pitfalls**

- Node's `dgram` does not exist in React Native or browsers: the UDP layer is
  a native module (or a WebSocket/WebRTC relay in a hosted architecture).
  This framing code is platform-neutral; the socket under it is not.
- Sequence/ack handling (resend queue, dedup of resent packets) lives in the
  circuit layer above this — see the Java/Kotlin circuit example (J1) for the
  same logic in another stack; port the semantics, not the syntax.
- Never zero-decode the appended-ACK region or the header: zero coding applies
  to the body portions the template specifies. The slice boundaries in
  `parseHeader` exist for exactly this reason.

---
## Example T5 — React-Linkpoint pattern: session store, login, and region state

**What it does:** The front-end architecture pattern for a React/React Native
Second Life client: a single session store (framework-agnostic core shown with
a tiny observable, usable from React via `useSyncExternalStore` or from plain
TS), login orchestration across the native/protocol layer, and region state
that rebuilds caps + event queue on teleport instead of patching them.

```typescript
// session.ts — framework-agnostic session store for a React SL client.
// Design rules this encodes (learned from real mobile viewer work):
//  1. Protocol objects (CapMap, EventQueue, circuit) are NOT React state.
//     They live in the store; React renders snapshots derived from them.
//  2. Teleport = rebuild, never mutate: new seed -> new CapMap -> new EQ.
//  3. Every async boundary reports through one status union, so the UI has
//     exactly four session faces: loggedOut, loggingIn, online, reconnecting.

import { CapMap, THIN_CLIENT_CAPS } from "./caps";
import { EventQueue } from "./eventqueue";

export type SessionStatus =
  | { kind: "loggedOut" }
  | { kind: "loggingIn"; stage: string }
  | { kind: "online"; agentName: string; regionName: string }
  | { kind: "reconnecting"; attempt: number }
  | { kind: "failed"; message: string; mfaRequired?: boolean };

export interface ProtocolBridge {
  // Implemented by the native layer (Android/iOS module) or node-metaverse
  // in a Node host. The store never touches sockets directly.
  login(req: { first: string; last: string; password: string; grid: string;
               mfaToken?: string }):
    Promise<{ agentId: string; agentName: string; seedCapability: string;
              regionName: string }>;
  logout(): Promise<void>;
  onTeleportFinish(cb: (seedCapability: string, regionName: string) => void): void;
}

export class SessionStore {
  private status: SessionStatus = { kind: "loggedOut" };
  private listeners = new Set<() => void>();
  private caps: CapMap | null = null;
  private eq: EventQueue | null = null;

  constructor(private bridge: ProtocolBridge) {
    bridge.onTeleportFinish(async (seed, region) => {
      // The old region's caps/EQ are already dead. Tear down first, then
      // rebuild — in that order, or a late event from the old queue can be
      // dispatched against the new region's state.
      this.eq?.stop(); this.eq = null; this.caps = null;
      await this.enterRegion(seed, region);
    });
  }

  subscribe = (fn: () => void) => { this.listeners.add(fn); return () => this.listeners.delete(fn); };
  getSnapshot = () => this.status;
  private set(status: SessionStatus) {
    this.status = status;
    for (const fn of this.listeners) fn();
  }

  async login(first: string, last: string, password: string,
              grid: string, mfaToken?: string): Promise<void> {
    this.set({ kind: "loggingIn", stage: "authenticating" });
    try {
      const res = await this.bridge.login({ first, last, password, grid, mfaToken });
      this.set({ kind: "loggingIn", stage: "entering region" });
      await this.enterRegion(res.seedCapability, res.regionName);
      this.set({ kind: "online", agentName: res.agentName, regionName: res.regionName });
    } catch (err) {
      // MFA is a first-class outcome, not an error string to grep: the
      // bridge normalises the grid's MFA challenge into this flag so the UI
      // can show a code prompt and retry login() with mfaToken set.
      const e = err as Error & { mfaRequired?: boolean };
      this.set({ kind: "failed", message: e.message, mfaRequired: e.mfaRequired });
    }
  }

  private async enterRegion(seedCapability: string, regionName: string) {
    this.caps = await CapMap.fromSeed(seedCapability, THIN_CLIENT_CAPS);
    this.eq = new EventQueue(this.caps, (ev) => this.dispatch(ev.message, ev.body));
    // Fire and forget with a catch: run() rejects only after 10 failures.
    this.eq.run().catch(err => {
      console.error("[session] event queue died", err);
      if (this.status.kind === "online")
        this.set({ kind: "reconnecting", attempt: 1 });
    });
    void regionName;
  }

  private dispatch(message: string, body: unknown) {
    // Route EQ events into store slices (chat, offers, notices). Kept as a
    // single switch so there is exactly one place that knows event names.
    switch (message) {
      case "ChatterBoxInvitation": /* -> chat slice */ break;
      case "GroupNotice":          /* -> notices slice */ break;
      default: break; // unknown events are ignored, never fatal
    }
    void body;
  }

  async logout(): Promise<void> {
    this.eq?.stop(); this.eq = null; this.caps = null;
    await this.bridge.logout();
    this.set({ kind: "loggedOut" });
  }
}
```

**Notes and pitfalls**

- Password handling in the UI layer: keep it in component state only long
  enough to call `login()`, never in the store snapshot (snapshots get logged,
  persisted, and screenshotted). "Remember me" means the OS keychain via the
  native bridge, not AsyncStorage.
- React re-render storms: object updates at circuit rate must not setState per
  packet. Batch scene updates in the bridge/store at 5–10 Hz for UI, keep the
  full-rate table outside React (same lesson as Example C4's cheap handler).
- The `mfaRequired` flag pattern mirrors the Lumiya MFA fix: parse the
  challenge at the auth layer, surface a distinct UI state, resubmit with the
  token — never treat MFA failure as "wrong password".

---

# Part 3 — Java and Kotlin (Lumiya-style Android clients)

## Example J1 — UDP circuit in Java: send, receive, ACK, resend, ping

**What it does:** A Lumiya-style simulator circuit in plain Java
(`DatagramSocket`): packet send with sequence assignment, a receive loop,
reliable-message tracking with timed resends, piggybacked and standalone
ACKs, and ping-based liveness. This is the layer Lumiya's 477 generated
message classes sit on, and the layer a Kotlin port must reproduce semantically
even when the message classes are regenerated.

```java
// Circuit.java — simulator UDP circuit (teaching version, single simulator).
// Lumiya lineage notes: the original client generated one Java class per
// message from the template; the circuit itself was hand-written, like this.
// Threading model: one receive thread, one resend/ping thread, sends from
// any thread via the synchronized outbox. Android forbids network I/O on the
// main thread — nothing here runs on it.

import java.io.IOException;
import java.net.*;
import java.util.*;
import java.util.concurrent.*;

public final class Circuit {
    public interface Handler { void onPacket(int freq, int number, byte[] body, int off, int len); }

    private static final int FLAG_ZEROCODED = 0x80, FLAG_RELIABLE = 0x40,
                             FLAG_RESENT = 0x20, FLAG_ACK = 0x10;

    private final DatagramSocket socket;
    private final InetAddress simIp; private final int simPort;
    private final Handler handler;
    private int nextSequence = 1;
    private volatile boolean running = false;
    private long lastReceiveMs = System.currentTimeMillis();

    // Unacked reliable packets: sequence -> (bytes, lastSentMs, resends)
    private static final class Pending { byte[] packet; long lastSent; int resends; }
    private final Map<Integer, Pending> unacked = new ConcurrentHashMap<>();
    // Sequences we owe ACKs for (piggybacked on the next outgoing packet,
    // or flushed as a standalone PacketAck when the queue grows).
    private final List<Integer> pendingAcks = new ArrayList<>();

    public Circuit(InetAddress simIp, int simPort, Handler handler) throws SocketException {
        this.socket = new DatagramSocket();
        this.simIp = simIp; this.simPort = simPort; this.handler = handler;
    }

    /** Send one already-encoded message body. Returns the sequence used. */
    public synchronized int send(byte[] body, boolean reliable, boolean zerocoded) throws IOException {
        int seq = nextSequence++;
        // Build packet: 6-byte header + body + optional appended acks.
        List<Integer> acks;
        synchronized (pendingAcks) {
            acks = new ArrayList<>(pendingAcks); pendingAcks.clear();
        }
        int ackBytes = acks.isEmpty() ? 0 : 1 + acks.size() * 4;
        byte[] pkt = new byte[6 + body.length + ackBytes];
        int flags = 0;
        if (zerocoded) flags |= FLAG_ZEROCODED;
        if (reliable) flags |= FLAG_RELIABLE;
        if (!acks.isEmpty()) flags |= FLAG_ACK;
        pkt[0] = (byte) flags;
        pkt[1] = (byte) (seq >>> 24); pkt[2] = (byte) (seq >>> 16);
        pkt[3] = (byte) (seq >>> 8);  pkt[4] = (byte) seq;
        pkt[5] = 0; // extra header length
        System.arraycopy(body, 0, pkt, 6, body.length);
        int p = 6 + body.length;
        for (int a : acks) {
            pkt[p++] = (byte) (a >>> 24); pkt[p++] = (byte) (a >>> 16);
            pkt[p++] = (byte) (a >>> 8);  pkt[p++] = (byte) a;
        }
        if (!acks.isEmpty()) pkt[p] = (byte) acks.size();

        socket.send(new DatagramPacket(pkt, pkt.length, simIp, simPort));
        if (reliable) {
            Pending pd = new Pending(); pd.packet = pkt; pd.lastSent = System.currentTimeMillis();
            unacked.put(seq, pd);
        }
        return seq;
    }

    public void start() {
        running = true;
        Thread rx = new Thread(this::receiveLoop, "circuit-rx"); rx.setDaemon(true); rx.start();
        Thread house = new Thread(this::housekeepingLoop, "circuit-house"); house.setDaemon(true); house.start();
    }

    private void receiveLoop() {
        byte[] buf = new byte[4096]; // simulator packets fit well under this;
                                     // oversized datagrams are a protocol error
        while (running) {
            try {
                DatagramPacket dp = new DatagramPacket(buf, buf.length);
                socket.receive(dp);
                lastReceiveMs = System.currentTimeMillis();
                handlePacket(dp.getData(), dp.getLength());
            } catch (IOException e) {
                if (running) { /* log; a closed socket on shutdown lands here too */ }
            }
        }
    }

    private void handlePacket(byte[] data, int len) {
        int flags = data[0] & 0xFF;
        int seq = ((data[1] & 0xFF) << 24) | ((data[2] & 0xFF) << 16) |
                  ((data[3] & 0xFF) << 8) | (data[4] & 0xFF);
        int extra = data[5] & 0xFF;
        int bodyEnd = len;
        if ((flags & FLAG_ACK) != 0) {
            int count = data[len - 1] & 0xFF;
            bodyEnd = len - 1 - count * 4;
            for (int i = 0; i < count; i++) {
                int o = bodyEnd + i * 4;
                int ackSeq = ((data[o] & 0xFF) << 24) | ((data[o + 1] & 0xFF) << 16) |
                             ((data[o + 2] & 0xFF) << 8) | (data[o + 3] & 0xFF);
                unacked.remove(ackSeq);
            }
        }
        if ((flags & FLAG_RELIABLE) != 0) {
            synchronized (pendingAcks) {
                pendingAcks.add(seq);
                // Flush standalone PacketAck promptly when many are owed:
                // delayed acks make the simulator resend, doubling traffic.
                if (pendingAcks.size() >= 16) flushAcksLocked();
            }
        }
        // Body slice: zero-decode first if flagged (body region only), then
        // dispatch by message id — elided here; see packet.ts (T4) for the
        // identical logic in TypeScript, and Lumiya's generated classes for
        // per-message decode.
        int off = 6 + extra;
        handler.onPacket(0, 0, data, off, Math.max(0, bodyEnd - off));
    }

    private void flushAcksLocked() {
        // PacketAck is a Fixed-frequency message; building its body belongs
        // to the message layer. This teaching circuit sends an empty-body
        // placeholder call so the flush point is visible; production code
        // constructs the real PacketAck body with the queued sequences and
        // clears pendingAcks only after a successful send.
        try { send(new byte[]{(byte)0xFF,(byte)0xFF,(byte)0xFF,(byte)0xFB}, false, false); }
        catch (IOException ignored) { }
        pendingAcks.clear();
    }

    private void housekeepingLoop() {
        while (running) {
            try { Thread.sleep(250); } catch (InterruptedException e) { return; }
            long now = System.currentTimeMillis();
            // Resend unacked reliable packets with a floor on resend count:
            // after ~5 resends over several seconds the circuit is dead, not
            // slow — escalate to the owner (disconnect callback) instead of
            // resending forever into a black hole.
            for (Map.Entry<Integer, Pending> e : unacked.entrySet()) {
                Pending pd = e.getValue();
                if (now - pd.lastSent > 1000) {
                    if (pd.resends >= 5) { unacked.remove(e.getKey()); continue; }
                    try {
                        byte[] copy = pd.packet.clone();
                        copy[0] |= FLAG_RESENT;
                        socket.send(new DatagramPacket(copy, copy.length, simIp, simPort));
                        pd.lastSent = now; pd.resends++;
                    } catch (IOException ignored) { }
                }
            }
            // Liveness: no packets at all for 60 s = dead circuit. The real
            // client also sends StartPingCheck on an interval and measures
            // CompletePingCheck round trips; silence detection is the floor.
            if (now - lastReceiveMs > 60_000) { /* notify owner: circuit dead */ }
        }
    }

    public void close() { running = false; socket.close(); }
}
```

**Notes and pitfalls**

- The standalone-PacketAck body construction is the one place this teaching
  version simplifies: in production, generate it from the template like every
  other message (PacketAck is Fixed frequency, its body is a list of U32
  sequences in a `Packets` block). Do not hand-roll the block layout from
  memory — diff against LibreMetaverse.Protocol's PacketAck.
- Android specifics: hold a `WifiLock`/multicast considerations are not needed
  for plain UDP, but Doze and app standby will starve the receive thread;
  viewers handle this with foreground-service keepalive while in-world.
- NAT rebinding on mobile networks changes your source port mid-session; the
  simulator tolerates some of this via circuit/ping behaviour, but a client
  that recreates its socket casually will be treated as a new circuit.

---
## Example J2 — Caps in Java with OkHttp: seed exchange and GetTexture ranges

**What it does:** The Java/OkHttp twin of Example T2: POST the wanted cap names
as LLSD XML to the seed capability, parse the returned map, and use the
`GetTexture` cap with HTTP range semantics to fetch a texture progressively.
Lumiya used OkHttp for exactly this layer; the example keeps its shape
(synchronous calls on a background executor, never the UI thread).

```java
// Caps.java — OkHttp-based capabilities client.
// LLSD XML is built/parsed with a small dedicated helper (LlsdXml) rather
// than string concatenation in production code; the two call sites below
// show the payload shapes. Lumiya shipped its own LLSD implementation —
// a Kotlin/Java port today should generate or port one and test it against
// LibreMetaverse.StructuredData vectors (see secondlife_protocol).

import java.io.IOException;
import java.util.*;
import java.util.concurrent.*;
import okhttp3.*;

public final class Caps {
    private static final MediaType LLSD = MediaType.parse("application/llsd+xml");
    private final OkHttpClient http;
    private final Map<String, String> urls = new HashMap<>();
    private final ExecutorService exec = Executors.newCachedThreadPool();

    public Caps(OkHttpClient http) { this.http = http; }

    /** Exchange wanted names for URLs at the seed capability. Blocking:
     *  call from a background thread/executor only. */
    public void fromSeed(String seedUrl, List<String> wanted) throws IOException {
        // Request body: LLSD array of strings.
        StringBuilder sb = new StringBuilder("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" +
            "<llsd><array>");
        for (String name : wanted) sb.append("<string>").append(name).append("</string>");
        sb.append("</array></llsd>");

        Request req = new Request.Builder().url(seedUrl)
            .post(RequestBody.create(sb.toString(), LLSD)).build();
        try (Response res = http.newCall(req).execute()) {
            if (!res.isSuccessful())
                throw new IOException("seed cap HTTP " + res.code());
            String xml = res.body() != null ? res.body().string() : "";
            // Parse: LLSD map of string -> string (cap name -> URL).
            // LlsdXml.parseMapOfStrings stands in for the LLSD parser.
            urls.clear();
            urls.putAll(LlsdXml.parseMapOfStrings(xml));
        }
    }

    public boolean has(String name) { return urls.containsKey(name); }
    public String url(String name) {
        String u = urls.get(name);
        if (u == null) throw new IllegalStateException("cap not granted: " + name);
        return u;
    }

    /** Fetch a texture via GetTexture with a byte range. GetTexture serves
     *  the JPEG2000 codestream; range requests let a client grab the header
     *  + low discard levels first (fast thumbnail) and refine later — the
     *  mechanism behind progressive texture loading in every viewer.
     *  The texture UUID is passed per the cap's convention (query/header as
     *  in viewer lltexturefetch code); follow viewer code for your target
     *  grid version rather than assuming a parameter name. */
    public CompletableFuture<byte[]> getTextureRange(String textureId, long from, long to) {
        return CompletableFuture.supplyAsync(() -> {
            String u = url("GetTexture") + "?texture_id=" + textureId;
            Request req = new Request.Builder().url(u)
                .header("Range", "bytes=" + from + "-" + to)
                .header("Accept", "image/x-j2c")
                .build();
            try (Response res = http.newCall(req).execute()) {
                if (res.code() != 200 && res.code() != 206)
                    throw new RuntimeException("GetTexture HTTP " + res.code());
                return res.body() != null ? res.body().bytes() : new byte[0];
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }, exec);
    }

    // Placeholder for the project's LLSD helper (see class comment).
    static final class LlsdXml {
        static Map<String, String> parseMapOfStrings(String xml) {
            throw new UnsupportedOperationException(
                "plug in the project LLSD parser (port of LibreMetaverse.StructuredData semantics)");
        }
    }
}
```

**Notes and pitfalls**

- OkHttp connection pooling is a real advantage for caps: a region session
  makes hundreds of small HTTPS calls to the same sim host. Do not create a
  new client per call.
- GetTexture parameter conventions have changed across simulator versions
  (header-based vs query-based eras). The viewer source for your target era
  is the authority — this is stated in the code because it has burned ports
  before.
- Certificate/hostname issues on OpenSim grids with self-signed certs: handle
  by explicit per-grid trust configuration in development builds only; never
  ship a trust-all hostname verifier in a distributed client.

---

## Example K1 — MFA login in Kotlin: challenge, prompt, resubmit

**What it does:** A Kotlin login flow modelled on the real Lumiya repair work:
the first auth attempt can return a distinct MFA challenge (reason + mfa_hash)
instead of a generic failure; the client raises a UI prompt state, collects a
TOTP code, and resubmits with the token and hash — keeping the hash in memory
only. This structure (sealed result, distinct challenge type) is the point:
MFA must never be flattened into "login failed".

```kotlin
// Auth.kt — MFA-aware login for an Android SL client.
// Background (from the Lumiya modernisation): the viewer persists mfa_hash
// only in an encrypted protected store. A client WITHOUT such a store keeps
// it memory-only for the session — a deliberate, documented deviation, not
// an oversight. Do not write it to SharedPreferences in plain text.

import kotlinx.coroutines.*
import java.security.MessageDigest

sealed interface AuthResult {
    data class Success(
        val agentId: String, val sessionId: String, val secureSessionId: String,
        val simIp: String, val simPort: Int, val circuitCode: Int,
        val seedCapability: String
    ) : AuthResult

    /** The grid wants an MFA code. mfaHash must ride along on the retry. */
    data class MfaChallenge(val mfaHash: String, val reason: String) : AuthResult

    data class Failure(val message: String, val gridMessage: String?) : AuthResult
}

interface AuthTransport {
    /** One login.cgi round trip. Implemented over OkHttp; the request is an
     *  LLSD/XML-RPC login document as in viewer llstartup / Lumiya SLAuth. */
    suspend fun postLogin(fields: Map<String, Any?>): Map<String, Any?>
}

class Auth(private val transport: AuthTransport) {

    private fun md5Hex(s: String): String {
        val digest = MessageDigest.getInstance("MD5").digest(s.toByteArray(Charsets.UTF_8))
        return digest.joinToString("") { "%02x".format(it) }
    }

    /** First attempt (token == null) or MFA retry (token + mfaHash set). */
    suspend fun login(
        first: String, last: String, password: String,
        start: String = "home", channel: String, version: String,
        token: String? = null, mfaHash: String? = null
    ): AuthResult {
        // Historical password form is "$1$" + md5(password); current grids
        // accept the documented login options in viewer code — build the
        // field set in ONE place (here) so a grid change touches one file.
        val fields = mutableMapOf<String, Any?>(
            "first" to first, "last" to last,
            "passwd" to "\$1\$" + md5Hex(password),
            "start" to start, "channel" to channel, "version" to version,
            "agree_to_tos" to true, "read_critical" to true
        )
        if (token != null) {
            fields["token"] = token
            fields["mfa_hash"] = mfaHash
        }

        val reply = try {
            transport.postLogin(fields)
        } catch (e: Exception) {
            return AuthResult.Failure("network: ${e.message}", null)
        }

        val loginFlag = reply["login"] as? String
        if (loginFlag == "true") {
            return AuthResult.Success(
                agentId = reply["agent_id"] as String,
                sessionId = reply["session_id"] as String,
                secureSessionId = reply["secure_session_id"] as String,
                simIp = reply["sim_ip"] as String,
                simPort = (reply["sim_port"] as Number).toInt(),
                circuitCode = (reply["circuit_code"] as Number).toInt(),
                seedCapability = reply["seed_capability"] as String
            )
        }

        // Failure path: the reason field distinguishes MFA from bad
        // credentials in current grids. Lumiya's fix parsed reason/mfa_hash
        // in the auth reply and raised a DISTINCT event for the challenge —
        // reproduce that distinction here, at the earliest layer.
        val reason = reply["reason"] as? String
        val hash = reply["mfa_hash"] as? String
        if (reason == "mfa" && hash != null) {
            return AuthResult.MfaChallenge(mfaHash = hash, reason = reason)
        }
        return AuthResult.Failure(
            message = "login rejected",
            gridMessage = reply["message"] as? String
        )
    }
}

// UI-side orchestration (ViewModel-shaped, framework-light):
class LoginCoordinator(private val auth: Auth) {
    sealed interface UiState {
        data object Idle : UiState
        data object Working : UiState
        data class NeedMfa(val challenge: AuthResult.MfaChallenge) : UiState
        data class Online(val session: AuthResult.Success) : UiState
        data class Error(val message: String) : UiState
    }

    var state: UiState = UiState.Idle
        private set

    suspend fun submit(first: String, last: String, password: String,
                       channel: String, version: String) {
        state = UiState.Working
        when (val r = auth.login(first, last, password, channel = channel, version = version)) {
            is AuthResult.Success -> state = UiState.Online(r)
            is AuthResult.MfaChallenge -> state = UiState.NeedMfa(r)
            is AuthResult.Failure -> state = UiState.Error(r.gridMessage ?: r.message)
        }
        // Keep the credentials in the coordinator ONLY if the MFA retry
        // needs them, and clear on success/failure. In production this is a
        // small, explicitly-managed holder — not the UI state, not logs.
    }

    suspend fun submitMfa(code: String, creds: HeldCredentials) {
        val challenge = (state as? UiState.NeedMfa)?.challenge ?: return
        state = UiState.Working
        when (val r = auth.login(creds.first, creds.last, creds.password,
                                 channel = creds.channel, version = creds.version,
                                 token = code, mfaHash = challenge.mfaHash)) {
            is AuthResult.Success -> state = UiState.Online(r)
            is AuthResult.MfaChallenge -> state = UiState.Error("code rejected — try again")
            is AuthResult.Failure -> state = UiState.Error(r.gridMessage ?: r.message)
        }
    }

    data class HeldCredentials(val first: String, val last: String,
                               val password: String, val channel: String,
                               val version: String)
}
```

**Notes and pitfalls**

- TOTP codes are time-stepped: a code entered at the end of its 30-second
  window can expire in flight. On MFA rejection, re-prompt immediately
  (the code above does) rather than treating it as a credential failure.
- The login reply's field spellings (`agent_id`, `seed_capability`, ...)
  come from the grid; a typo here fails as a Kotlin null-cast crash, which is
  why the parse is concentrated in `Auth` and nowhere else.
- Never log the `fields` map: it contains the password hash and, on retry,
  the live MFA token.

---
## Example K2 — Event Queue and session supervision in Kotlin coroutines

**What it does:** The Kotlin twin of Example T3, structured the way an Android
client should run it: a coroutine-scoped EQG loop on an IO dispatcher, events
delivered on a `SharedFlow`, a supervisor that rebuilds caps + queue on
teleport, and lifecycle hooks that stop the loop when the app backgrounds.
Shows the teleport-rebuild rule enforced by types: a `RegionSession` is
immutable and replaced whole.

```kotlin
// RegionSession.kt — one region visit = one immutable session object.
// When a teleport finishes you do not "update" a session; you close it and
// create the next one. Half of all mobile viewer session bugs are a session
// object that outlived its region.

import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

data class CapUrls(val map: Map<String, String>) {
    fun url(name: String): String =
        map[name] ?: throw IllegalStateException("cap not granted: $name")
    fun has(name: String): Boolean = map.containsKey(name)
}

interface LlsdHttp {
    suspend fun postLlsd(url: String, body: Map<String, Any?>): Map<String, Any?>
    suspend fun exchangeSeed(seedUrl: String, wanted: List<String>): CapUrls
}

class RegionSession(
    val regionName: String,
    val caps: CapUrls,
    private val http: LlsdHttp,
    private val scope: CoroutineScope
) {
    private val _events = MutableSharedFlow<EqEvent>(extraBufferCapacity = 256)
    val events: SharedFlow<EqEvent> = _events.asSharedFlow()

    data class EqEvent(val message: String, val body: Any?)

    private var job: Job? = null
    @Volatile private var stopped = false

    fun start() {
        job = scope.launch(Dispatchers.IO) { pollLoop() }
    }

    private suspend fun pollLoop() {
        var ack: Any? = null
        var errors = 0
        while (!stopped) {
            try {
                val reply = http.postLlsd(
                    caps.url("EventQueueGet"),
                    mapOf("ack" to ack, "done" to false)
                )
                ack = reply["id"]
                errors = 0
                val list = reply["events"] as? List<*> ?: emptyList<Any>()
                for (raw in list) {
                    val ev = raw as? Map<*, *> ?: continue
                    val name = ev["message"] as? String ?: continue
                    if (!_events.tryEmit(EqEvent(name, ev["body"]))) {
                        // Buffer full: the consumer is stalled. Dropping a
                        // chat event is bad; dropping the SESSION on a slow
                        // consumer is worse. Emit on the collector's
                        // dispatcher as a fallback (suspending emit) for
                        // everything except high-frequency noise events.
                        if (name != "CoarseLocationUpdate") _events.emit(EqEvent(name, ev["body"]))
                    }
                }
            } catch (e: CancellationException) {
                throw e
            } catch (e: Exception) {
                errors++
                val backoffMs = minOf(30_000L, 1000L * (1L shl minOf(errors, 5)))
                delay(backoffMs)
                if (errors >= 10) {
                    // Give up: the supervisor decides whether this is a
                    // teleport-in-progress (new session coming) or a death.
                    throw IllegalStateException("EQG failed 10 times", e)
                }
            }
        }
    }

    suspend fun close() {
        stopped = true
        job?.cancelAndJoin()
        // Best-effort done:true (see T3) — a failure here is not an error.
        runCatching {
            http.postLlsd(caps.url("EventQueueGet"), mapOf("ack" to null, "done" to true))
        }
    }
}

/** Owns the current session and the teleport rebuild. */
class SessionSupervisor(private val http: LlsdHttp) {
    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)
    var current: RegionSession? = null
        private set

    suspend fun enterRegion(regionName: String, seedCapability: String): RegionSession {
        current?.close()
        val caps = http.exchangeSeed(seedCapability, WANTED_CAPS)
        val session = RegionSession(regionName, caps, http, scope)
        current = session
        session.start()
        return session
    }

    suspend fun shutdown() {
        current?.close()
        current = null
        scope.cancel()
    }

    companion object {
        val WANTED_CAPS = listOf(
            "EventQueueGet", "FetchInventory2", "FetchInventoryDescendents2",
            "FetchLib2", "FetchLibDescendents2", "InventoryAPIv3", "LibraryAPIv3",
            "GetTexture", "GetMesh", "GetMesh2", "SimulatorFeatures",
            "EnvironmentSettings", "ExtEnvironment", "GetDisplayNames",
            "ChatSessionRequest", "AgentPreferences", "ServerReleaseNotes"
        )
    }
}
```

**Notes and pitfalls**

- Android lifecycle: `close()` the session when the in-world activity stops;
  a leaked EQG loop keeps the radio awake and the avatar's session half-alive
  server-side. Foreground-service rules on modern Android govern how long an
  in-world session may run backgrounded — design for suspension, not denial.
- `tryEmit` dropping: the buffer policy above is a deliberate, documented
  trade-off. The alternative (unbounded buffer) OOMs on a region-entry burst.
- OpenSim EQG exists and is close, but event names and the ack shape have
  differed in edge cases historically — the `as? Map` defensive parsing here
  is there because a strict cast crashed on a real OpenSim reply shape.

---

## Example K3 — Generated-message discipline: a hand-checked message codec in Kotlin

**What it does:** Shows the shape of ONE message (`UseCircuitCode` and
`CompleteAgentMovement`) encoded/decoded by hand in Kotlin, to teach what the
code generator (from `message_template.msg`) produces for all ~477 messages in
a Lumiya-scale client — and why you regenerate rather than hand-edit. Includes
the session-critical fields and the fixed/frequency header writing from
Example T4's rules.

```kotlin
// Messages.kt — hand-written for exactly two messages, as documentation of
// the generated pattern. PRODUCTION RULE: every other message class in the
// client is GENERATED from message_template.msg (diffed against the viewer
// copy) and never edited by hand; a hand edit is overwritten on regeneration
// and silently reverts a fix. Fixes go in the template diff or the generator.

import java.io.ByteArrayOutputStream
import java.nio.ByteBuffer
import java.nio.ByteOrder
import java.util.UUID

object Wire {
    // All multi-byte wire fields are BIG-ENDIAN (network order). LSL/LLSD
    // habits (little-endian anywhere) do not apply on the UDP wire.
    fun u8(v: Int): ByteArray = byteArrayOf(v.toByte())
    fun u32(v: Int): ByteArray = ByteBuffer.allocate(4).order(ByteOrder.BIG_ENDIAN).putInt(v).array()
    fun uuid(u: UUID): ByteArray {
        val bb = ByteBuffer.allocate(16)
        bb.putLong(u.mostSignificantBits); bb.putLong(u.leastSignificantBits)
        return bb.array()
    }
    fun f32(v: Float): ByteArray = ByteBuffer.allocate(4).order(ByteOrder.BIG_ENDIAN).putFloat(v).array()
    /** Vector3 as 3 x F32. Quaternions on the wire are 3 x F32 (scalar
     *  reconstructed as sqrt(1 - x^2 - y^2 - z^2)) — not encoded here. */
    fun vec3(x: Float, y: Float, z: Float): ByteArray =
        f32(x) + f32(y) + f32(z)

    /** Message header by frequency (see T4). Low = FF FF + U16 number. */
    fun lowHeader(number: Int): ByteArray =
        byteArrayOf(0xFF.toByte(), 0xFF.toByte(),
                    (number ushr 8).toByte(), number.toByte())
    fun fixedHeader(number: Int): ByteArray =
        byteArrayOf(0xFF.toByte(), 0xFF.toByte(), 0xFF.toByte(), number.toByte())
}

/** UseCircuitCode — Low frequency, message 3 in the canonical template
 *  numbering (VERIFY against your diffed template copy; numbers are template
 *  data, not constants of nature). Blocks: CircuitCode (Code U32, SessionID
 *  UUID, ID/AgentID UUID). Sent once, first, on the new circuit. */
fun encodeUseCircuitCode(circuitCode: Int, sessionId: UUID, agentId: UUID): ByteArray {
    val out = ByteArrayOutputStream()
    out.write(Wire.lowHeader(3))
    out.write(Wire.u32(circuitCode))
    out.write(Wire.uuid(sessionId))
    out.write(Wire.uuid(agentId))
    return out.toByteArray()
}

/** CompleteAgentMovement — Low frequency. Blocks: AgentData (AgentID,
 *  SessionID, CircuitCode). Sent right after UseCircuitCode; the simulator
 *  answers with RegionHandshake and starts object updates. If this never
 *  arrives, you get a login that "succeeds" and a region that never loads —
 *  the single most recognisable partial-login symptom. */
fun encodeCompleteAgentMovement(agentId: UUID, sessionId: UUID, circuitCode: Int): ByteArray {
    val out = ByteArrayOutputStream()
    out.write(Wire.lowHeader(249)) // template number — verify in your copy
    out.write(Wire.uuid(agentId))
    out.write(Wire.uuid(sessionId))
    out.write(Wire.u32(circuitCode))
    return out.toByteArray()
}
```

**Notes and pitfalls**

- The two "verify in your copy" comments are the lesson: message numbers and
  block layouts are *data from the template*, and the master template has
  been stale before. A codec generated from a diffed template is trustworthy;
  numbers memorised from a blog post are not.
- Zerocoded messages need the T4/J1 zero-encode step applied to the body
  after encoding, per the template flag for that message — neither message
  above should be assumed zerocoded without checking its template entry.
- Lumiya's generated classes also carried per-message `Trusted` /
  `Deprecated` metadata. A generator should preserve those as annotations:
  deprecated messages still parse (old sims send them), trusted flags matter
  for simulator-side work (OpenSim), not for a pure client.

---

## Closing notes for the whole library

- **One oracle rule:** when C#, TS, and Kotlin disagree about the wire, the
  order of authority is viewer code, then the diffed message template, then
  LibreMetaverse, then the port. Wiki pages and old blog posts are not on
  the list.
- **Test matrix worth actually running:** every example here against
  (1) a local OpenSim standalone (breakpointable server, subset behaviour),
  (2) Aditi (real Linden Lab semantics, test L$/inventory), (3) Agni last.
  Record which grid each test ran on; "it logged in" without a grid name is
  not a test result.
- **What was deliberately simplified, and where:** J1's standalone PacketAck
  body and J2's LLSD parser are plugged with project components in real code;
  T1's decoder mapping is documentation for a real XML parser; C7 notes the
  3.x helper names to confirm in your pinned version. Everything else is
  written to run as shown against its stated dependencies.
- **Security floor for anything distributed:** no credential logging, no
  trust-all TLS, no cap URLs in shared logs, passwords only in OS-backed
  storage, and a unique channel/version in login (TPV Policy). Examples C1/K1
  read secrets from the environment for development; production storage is
  the platform keystore, full stop.

---

## Example C8 — Appearance and the Current Outfit Folder (AIS3 link discipline)

**What it does:** Lists the Current Outfit Folder, resolves its links to the
real items, and explains the one rule that prevents outfit corruption: never
delete or rename through a link as if it were the item. Written as a console
inspection tool — the safe first step before any client offers outfit editing.

```csharp
// COF inspection. In LibreMetaverse 3.x the COF is a well-known folder found
// via the inventory store (current outfit folder type). Links appear as
// items whose base/target relationship is exposed on the item; exact helper
// names vary by minor version — the LOGIC below is the portable part.
using System;
using LibreMetaverse;
using LibreMetaverse.Assets;

public static class CofExample
{
    public static void DumpCurrentOutfit(GridClient client)
    {
        var store = client.Inventory.Store;
        // Find the COF by folder type rather than by name: names localise
        // and users rename things; the folder TYPE is the contract.
        InventoryFolder? cof = null;
        foreach (var node in store.GetContents(store.RootFolder))
        {
            // (Folder discovery normally recurses; COF is a top-level
            // well-known folder in the standard skeleton.)
            if (node is InventoryFolder f && f.PreferredType == AssetType.CurrentOutfitFolder)
                cof = f;
        }
        if (cof == null)
        {
            Console.WriteLine("COF not found in fetched skeleton — fetch the " +
                              "agent inventory root first (Example C3).");
            return;
        }

        foreach (var node in store.GetContents(cof))
        {
            if (node is InventoryItem item)
            {
                // A COF entry is normally a LINK: its AssetUUID / linked
                // target identifies the real item elsewhere in inventory.
                // Operations users expect:
                //   "remove from outfit"  -> delete the LINK (this entry)
                //   "delete item"         -> delete the TARGET item (and the
                //                            link dangles; viewers clean up)
                // Confusing the two is how clients delete users' clothing
                // when they meant to undress. Print both IDs so the
                // distinction is visible in the tool's output.
                Console.WriteLine($"COF entry: {item.Name}");
                Console.WriteLine($"   link item id : {item.UUID}");
                Console.WriteLine($"   asset/target : {item.AssetUUID}");
                Console.WriteLine($"   is link      : {item.IsLink()}");
            }
        }
        Console.WriteLine("Reminder: version the COF (IncrementCOFVersion via " +
                          "AIS) after any outfit change or other viewers " +
                          "will show a stale outfit for this agent.");
    }
}
```

**Notes and pitfalls**

- COF versioning is not optional bookkeeping: the simulator and other viewers
  use the COF version to decide whether the appearance they cached is stale.
  Appearance bugs that "only other people see" are usually this.
- Bake failures (grey avatar) are diagnosed from exactly this data: a COF
  full of broken links to missing targets bakes grey while every individual
  system looks healthy. Dump first, theorise second.

---

## Example T6 — Creating an inventory link through AIS3 (TypeScript)

**What it does:** The TS counterpart to C8's rule: create a link in a folder
via the `InventoryAPIv3` cap with the LLSD payload shape viewer `llaisapi.cpp`
uses, including the folder/item identity fields and the success check. Link
creation was the exact operation under repair in the Linkpoint work that
motivated this repo, so it gets its own example.

```typescript
// ais.ts — AIS3 create-link, following the viewer llaisapi.cpp payload shape.
// AIS (Agent Inventory Services v3) operations are LLSD POSTs to the
// InventoryAPIv3 cap URL *suffixed with the target folder's UUID path*:
//     POST {InventoryAPIv3}/category/{folderId}
// with a body describing the new item(s). Confirm the exact suffix/payload
// against the viewer code for your simulator version before shipping —
// AIS is precisely the surface where grids diverge.

import type { CapMap } from "./caps";
import { encodeLLSD, LLSDUUID, type LLSDValue } from "./llsd";

export interface AisResult { ok: boolean; raw: LLSDValue; }

export async function createLink(
  caps: CapMap,
  args: {
    folderId: string;        // folder (item-id space) receiving the link
    targetItemId: string;    // the REAL item being linked to (its item id)
    targetAssetId?: string;  // asset id of the target, when known
    name: string;
    description?: string;
  }
): Promise<AisResult> {
  if (!caps.has("InventoryAPIv3")) {
    // No AIS on this grid/sim: the fallback is the legacy UDP inventory
    // link path, which is a DIFFERENT implementation, not a degraded AIS.
    // Returning a clean "unsupported" beats silently half-creating state.
    throw new Error("AIS3 (InventoryAPIv3) not granted on this region");
  }

  // Payload shape (viewer-derived): a map with an "items" array; each item
  // carries type/asset-type discriminators for a LINK, the linked target id,
  // parent folder, name, and permission/flags fields the server requires.
  // Fields the server computes (creation date, link id) are NOT sent.
  const payload: LLSDValue = {
    items: [{
      type: "link",
      "linked-id": new LLSDUUID(args.targetItemId),
      "parent-id": new LLSDUUID(args.folderId),
      name: args.name,
      desc: args.description ?? "",
      ...(args.targetAssetId ? { "asset-id": new LLSDUUID(args.targetAssetId) } : {}),
    }],
  };

  const url = `${caps.url("InventoryAPIv3")}/category/${args.folderId}`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/llsd+xml" },
    body: encodeLLSD(payload),
  });
  const raw = res.ok ? (await import("./llsd-parse")).parseLLSDXml(await res.text()) : undefined;
  // AIS success is conveyed in the reply body (per-item results), not by
  // HTTP 200 alone: a 200 with a failed item entry is a failed operation.
  // Callers must inspect `raw`; this wrapper surfaces it untouched on
  // purpose rather than inventing a success boolean the protocol lacks.
  return { ok: res.ok, raw };
}
```

**Notes and pitfalls**

- The dynamic `import("./llsd-parse")` stands for the project's LLSD parser
  module (Example T1's mapping). It is written this way to keep the example
  focused on the AIS payload — in the repo this resolves to the same parser
  the caps client uses.
- Link vs copy: creating a link never duplicates the asset. A client that
  implements "duplicate outfit item" as link creation will confuse users
  whose edits then apply to every outfit at once (because there is only one
  real item). Model the user's intent, not the cheapest API.
- After any AIS inventory mutation, refresh the affected folder
  (`FetchInventoryDescendents2`) instead of patching local state by hand:
  the server is the authority and assigns the new item IDs.

---

## Example K4 — Android lifecycle for an in-world session (Kotlin)

**What it does:** Ties K1–K3 together at the Activity level: start the session
when the in-world screen is created, keep the UDP circuit and EQG in a
session-scoped component that survives configuration changes, and shut down
in the right order (EQG close → logout message → circuit close) when the user
leaves. The ordering and the config-change survival are the teachable parts.

```kotlin
// InWorldSession.kt — lifecycle glue, deliberately framework-light so the
// ordering is visible. In the app this lives in a ViewModel-retained holder;
// the Activity only forwards lifecycle calls.

import kotlinx.coroutines.*

class InWorldSession(
    private val supervisor: SessionSupervisor,
    private val circuit: CircuitHandle,
    private val scope: CoroutineScope
) {
    interface CircuitHandle {
        fun start()
        fun sendLogout()
        fun close()
        var onCircuitDead: (() -> Unit)?
    }

    @Volatile private var active = false

    /** Called when the in-world UI becomes visible (onStart / navigation). */
    fun onEnter() {
        if (active) return
        active = true
        circuit.start()
        circuit.onCircuitDead = {
            // Circuit death mid-session: surface to the supervisor, which
            // owns the reconnect decision (K2/C6 policy). The session object
            // itself never silently recreates a circuit — a new circuit is
            // a new login state, with a new seed and new caps.
            scope.launch { supervisor.shutdown() }
        }
    }

    /** Called when the user leaves the in-world UI for good (not rotation). */
    suspend fun onLeave() {
        if (!active) return
        active = false
        // ORDER MATTERS:
        //  1. stop the event queue (no more unsolicited work),
        //  2. tell the simulator we are logging out (LogoutRequest over UDP),
        //  3. close the socket.
        // Skipping step 2 leaves a ghost avatar standing in the region
        // until the simulator times the circuit out — minutes later.
        supervisor.shutdown()
        circuit.sendLogout()
        circuit.close()
    }

    /** Configuration change (rotation, theme): the Activity is recreated
     *  but this holder is retained, so onEnter/onLeave are NOT called —
     *  which is exactly why they live here and not in Activity callbacks.
     *  Anything that must survive rotation (session, circuit, caps) belongs
     *  to the holder; anything visual belongs to the Activity. */
    fun onConfigurationChanged() {
        // Intentionally empty — the method exists to document the rule.
    }
}
```

**Notes and pitfalls**

- Foreground service: a session that must persist while the user is in
  another app needs a foreground service with the appropriate type on modern
  Android, and the user-visible notification that comes with it. A viewer
  that pretends otherwise gets killed by the OS at the worst moment.
- Process death is a logout you did not send: on next launch, expect the
  "already logged in" login response path and handle it (the grid logs the
  old session out when the new login completes).
- The empty `onConfigurationChanged` is deliberate documentation: in code
  review, "where does rotation tear down the socket?" must have a findable
  answer, and this is it.

---

## Example C9 — Resolving avatar names and UUIDs without guessing

**What it does:** The two directions of identity lookup — UUID to display name
(modern `GetDisplayNames` cap behaviour, surfaced in LibreMetaverse through
the Avatars manager) and name to UUID (search) — with caching, because name
resolution is the most over-requested operation in naive clients.

```csharp
// Name resolution. Display names are NOT unique and NOT stable identifiers;
// the UUID is the identity, the name is a label. Code that keys friendships,
// permissions, or blocklists by name is wrong by construction.
using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;
using LibreMetaverse;

public static class NameExample
{
    private static readonly ConcurrentDictionary<UUID, string> Cache = new();

    public static async Task<string> NameOf(GridClient client, UUID agentId)
    {
        if (Cache.TryGetValue(agentId, out var cached)) return cached;

        // Avatars.RequestAvatarName / name events in 3.x: the request is
        // asynchronous — you ask, an event delivers the name. Wrap it in a
        // TaskCompletionSource with a timeout, exactly like teleport (C5).
        var tcs = new TaskCompletionSource<string>();
        void Handler(object? s, AvatarNameEventArgs e)
        {
            if (e.AgentID == agentId) tcs.TrySetResult(e.DisplayName);
        }
        client.Avatars.DisplayNameReply += Handler;
        try
        {
            client.Avatars.RequestAvatarName(agentId);
            var done = await Task.WhenAny(tcs.Task, Task.Delay(10_000));
            string name = done == tcs.Task ? tcs.Task.Result : agentId.ToString();
            // Cache even the fallback briefly? No: cache only real replies,
            // or a transient failure poisons the cache with UUID strings.
            if (done == tcs.Task) Cache[agentId] = name;
            return name;
        }
        finally { client.Avatars.DisplayNameReply -= Handler; }
    }

    // Reverse direction (name -> UUID) is a SEARCH operation (directory /
    // people search caps and packets), returns multiple candidates, and can
    // be rate-limited. A client must present candidates for disambiguation;
    // auto-picking the first result messages the wrong person eventually.
    // Legacy "firstname.lastname" usernames vs display names: the login name
    // (e.g. "joe.graham" / Resident suffix rules) is a third namespace —
    // keep all three (UUID, username, display name) as separate fields in
    // your data model, forever.
}
```

**Notes and pitfalls**

- Display name changes are user-controlled and frequent; a cached name is a
  hint with a TTL in any long-lived UI, even though this example's session
  cache is fine for a console tool.
- OpenSim name services on a standalone know only local users; Hypergrid
  visitors carry foreign names with grid suffixes. Do not parse names for
  structure your grid did not guarantee.
