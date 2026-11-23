# Second Life RLV and RLVa Command & Architecture Reference

Derived from Marine Kelley's Restrained Love Viewer (RLV) specification, Kitty Barnett's Restrained Love API (`RLVa`) as shipped in `FirestormViewer/phoenix-firestorm` release branches (`indra/newview/rlv*.cpp`, `rlv*.h` — LGPL-2.1), `cinderblocks/libremetaverse` (`LibreMetaverse.RLV` and `LibreMetaverse.Tests/RLV` — BSD-3), and `Kaleaon/react-linkpoint` (`src/linkpoint/rlv*.ts`) / `Kaleaon/Linkpoint`.

**Repository verification discipline:** Never invent a GitHub URL for **Catznip** (RLVa origin by Kitty Barnett) or Marine Kelley's **Restrained Love viewer** — neither has a verified canonical GitHub repository. Always cite the [Third Party Viewer Directory](https://wiki.secondlife.com/wiki/Third_Party_Viewer_Directory) for their current source code links, reuse C++ viewer code only from `FirestormViewer/phoenix-firestorm` **release branches** under LGPL-2.1, and prefer `LibreMetaverse.RLV` (BSD-3) when porting clean-room TypeScript or Kotlin implementations.

---

## 1. Security Boundary & Inbound Wire Gate

RLV/RLVa grants in-world LSL scripts sweeping control over movement, chat, camera, teleportation, and attachments. Breaking the inbound packet gate turns public chat into a remote avatar hijack vector.

### Mandatory 4-Point Gate

Process an `@`-prefixed string as RLVa **if and only if all four checks pass**:

1. **User opt-in enabled:** The viewer's RLVa setting (`RestrainedLove` in Firestorm `settings.xml`, default `false`) is explicitly enabled by the user.
2. **Exact transport packet:** The message arrives via `ChatFromSimulator` (`Low 139`, wire ID `0xFFFF008B`, `Trusted`, `Unencoded` — or `ChatFromSimulator` packaged inside `EventQueueGet` / relay bridge only where explicitly authorised). Never parse outbound chat or generic UI toast strings as RLV.
3. **Exact `ChatType == CHAT_TYPE_OWNER (8)`:** In `ChatFromSimulator.ChatData`, `ChatType` (`U8`) **must equal `8`** (`llOwnerSay`), which the simulator restricts to scripts inside objects currently owned by the receiving agent (`SourceType == CHAT_SOURCE_OBJECT (2)`).
   - Ignore `0` (`Whisper`), `1` (`Normal`), `2` (`Shout`), `4` (`StartTyping`), `5` (`StopTyping`), `6` (`Debug`), and `7` (`RegionSay`).
   - Never execute `@` commands from public, group, or avatar IM chat (`ImprovedInstantMessage` `Low 254` is used only for specific `llInstantMessage` query/version edge cases if `EnableInstantMessageProcessing` is explicitly supported for trusted relays — never for arbitrary strangers imposing `@` restrictions).
4. **`@` prefix & chat suppression:** `Message` (UTF-8 decoded from `Variable 2`, null-terminator stripped) starts with `"@"` and has at least one command body character. Suppress valid executed `@` command lines from the visible local chat transcript unless `RestrainedLoveDebug` is enabled.

### `ChatFromSimulator` (`Low 139 = 0xFFFF008B`, `Trusted`, `Unencoded`)

```text
ChatData Single:
  FromName    Variable 1   // 1-byte length + UTF-8 object name
  SourceID    LLUUID       // 16B — MUST be used as sourceObjectId key!
  OwnerID     LLUUID       // 16B — agent UUID for llOwnerSay
  SourceType  U8           // 1 = Agent, 2 = Object, 0 = System
  ChatType    U8           // MUST == 8 (CHAT_TYPE_OWNER)
  Audible     U8           // 1 = Audible
  Position    LLVector3    // 12B little-endian
  Message     Variable 2   // 2-byte length + UTF-8 text (strip trailing 0x00)
```

---

## 2. Command Grammar, Synonym Trap & Per-Object State Machine

### 2.1 Syntax & Multi-Command Batching

A single `llOwnerSay` line may contain multiple comma-separated commands executed **left-to-right in order**:

```text
@<behaviour>[:<option>]=<param>[,<behaviour2>[:<option2>]=<param2>...]
```

Special bare command without `=`:
- `@clear` (no `=` and no `:option`) is valid and clears **all** restrictions held by `SourceID`.
- Filter clearing appears in the wild in both forms — `@clear=<filter>` (canonical RLV spec) and `@clear:<filter>` (common script shorthand, or `@clear:<filter>=y`). Strip any leading `@` on chained segments (`@unsit=n,@tploc=n` and `@unsit=n,tploc=n` both occur in LSL scripts), normalise `<behaviour>` and `<param>` (`n`, `y`, `add`, `rem`, `force`) to lowercase, and preserve case sensitivity only where folder paths require it.

### 2.2 The `=n` / `=add` and `=y` / `=rem` Synonym Rule

**Classic implementation bug:** In the RLV specification, **`=add` is an exact synonym of `=n`**, and **`=rem` is an exact synonym of `=y`**.
- `@detach=n` and `@detach=add` **both** add a detach lock!
- `@tplure:<uuid>=n` and `@tplure:<uuid>=add` **both** add a teleport-lure *exception* for `<uuid>`!
- `@redirchat:345=n` and `@redirchat:345=add` **both** add channel `345` as a chat redirection target!
- `@detach=y` and `@detach=rem` **both** lift that object's detach lock!

Whether a rule restricts an action or grants an exception is determined by `(behaviour, hasOption)` in the command definition table — **never** by branching differently on `"n"` versus `"add"`.

### 2.3 Per-Source-Object Restriction Multimap & Lifecycle Cleanup

Store active rules as a set of tuples `(sourceObjectId: UUID, behaviour: string, option: string)` (or `Map<UUID, Set<RuleKey>>`):
- **Adding (`=n` / `=add`):** Insert `(sourceObjectId, behaviour, option ?? "")`. Multiple distinct objects may hold `@unsit=n` simultaneously.
- **Removing (`=y` / `=rem`):** Remove `(sourceObjectId, behaviour, option ?? "")` **for that `sourceObjectId` only**. The behaviour remains restricted if any other `sourceObjectId` still holds it!
- **`@clear` / `@clear=<filter>` / `@clear:<filter>`:** Remove all rules (or rules whose `behaviour` or `behaviour:option` contains `<filter>` case-insensitively) **for `sourceObjectId` only** — never wipe rules held by other objects.
- **Attachment detach auto-cleanup:** Subscribe to object kill / attachment detach events (`KillObject` `High 16` and `ObjectUpdate` attachment-point transitions to `0`). Whenever an attached object detaches, automatically call `removeRestrictionsForObject(primId)` (see `LibreMetaverse.RLV.RlvRestrictionManager.RemoveRestrictionsForObjectsAsync` and `rlvhandler.cpp` GC) so detached collars/HUDs never leave permanent orphan locks on the session.
- **Session disconnect:** Clear all ephemeral restrictions and session trust caches on logout.

---

## 3. Positive-Channel Queries & `ChatFromViewer` Wire Format

Query commands take an integer `<channel>` as `<param>` (e.g. `@versionnew=471122`).

### Channel Validation Rule
- Parse `<param>` as a signed 32-bit integer (`S32`).
- **Strictly enforce `channel > 0`:** Never reply on channel `0` (public chat spam / leak) and never reply to standard `@version*` / `@get*` queries on negative channels (`<= 0`).
- *(Note: The RLV Relay specification uses negative channel `-1812221819` for LSL-to-LSL relay messages `cmd_name,target_uuid,@command`, which are spoken by an in-world relay script or viewer relay bridge, separate from standard `@version=<positive_chan>` viewer queries.)*
- Send the reply via `ChatFromViewer` (`Low 80`, wire ID `0xFFFF0050`, `NotTrusted`, **`Zerocoded`**) with `ChatData.Type = 1` (`CHAT_TYPE_NORMAL`) and `ChatData.Channel = channel`.

### `ChatFromViewer` (`Low 80 = 0xFFFF0050`, `NotTrusted`, `Zerocoded`)

```text
AgentData Single:
  AgentID     LLUUID       // 16B
  SessionID   LLUUID       // 16B
ChatData Single:
  Message     Variable 2   // 2-byte little-endian length + UTF-8 reply string
  Type        U8           // 1 (CHAT_TYPE_NORMAL)
  Channel     S32          // 4-byte little-endian positive channel (> 0)
```
*(Remember to set header flag `0x80` `MSG_ZEROCODED` + `0x40` `MSG_RELIABLE` and `ZeroEncode` the packet body, or verify against your circuit's `ChatFromViewer` serializer.)*

### Standard Query Catalogue

| Query command | Reply format | Notes & edge cases |
|---|---|---|
| `@version=<chan>` | `"RestrainedLife viewer v2.9.27 (RLVa 2.4.2)"` (or `"RestrainedLife viewer v2.9.27 (Linkpoint 1.0)"`) | **Legacy spelling `"RestrainedLife"`** is intentional — hundreds of older LSL furniture/collar scripts substring-match `"RestrainedLife viewer v"`! |
| `@versionnew=<chan>` | `"RestrainedLove viewer v2.9.27 (RLVa 2.4.2)"` | Modern spelling `"RestrainedLove viewer v..."` introduced in RLV 1.22+ |
| `@versionnum=<chan>` | `"2092700"` (7-digit integer `MMmmppbb`, e.g. `2.09.27.00` → `2092700` or `3.04.03.00` → `3040300`) | Pure digits only; scripts cast directly via `(integer)message` |
| `@getstatus[:<filter>][;<sep>]=<chan>` | `"/unsit/tploc/sendchat"` (leading `"/"` per rule, or `""` if none) | Returns active rules held **by the querying `SourceID` only** (use `@getstatusall` for all objects). Optional `<filter>` filters by substring; optional `;<sep>` overrides the `"/"` separator |
| `@getoutfit[:<part>]=<chan>` | 16-char `"0"`/`"1"` bitstring (e.g. `"0111100111111000"`) or single `"0"`/`"1"` if `:<part>` named | Exact 16-slot wearable order in Section 3.1 below |
| `@getattach[:<point>]=<chan>` | `"0"`/`"1"` bitstring starting at index `0` (`"0"` for `none`) through attachment points, or single `"0"`/`"1"` if `:<point>` named | Exact attachment point index & RLV lowercase name table in Section 3.2 below |
| `@getsitid=<chan>` | `"<seat-prim-uuid>"` or `"00000000-0000-0000-0000-000000000000"` | Returns the `UUID` of the prim the agent is currently sitting on, or `NULL_KEY` if standing / ground-sitting |

### 3.1 Canonical `@getoutfit` Wearable Slot Order (16 Slots)

When `@getoutfit=<chan>` is called with no `:<part>` option, build a 16-character string of `'1'` (at least one wearable worn on that layer) or `'0'` (none worn) in this **exact** order:

| Index | RLV `<part>` name | SL `LLWearableType` (`WT_*`) | Notes |
|---|---|---|---|
| 0 | `gloves` | `WT_GLOVES (9)` | Clothing |
| 1 | `jacket` | `WT_JACKET (8)` | Clothing |
| 2 | `pants` | `WT_PANTS (5)` | Clothing |
| 3 | `shirt` | `WT_SHIRT (4)` | Clothing |
| 4 | `shoes` | `WT_SHOES (6)` | Clothing |
| 5 | `skirt` | `WT_SKIRT (11)` | Clothing |
| 6 | `socks` | `WT_SOCKS (7)` | Clothing |
| 7 | `underpants` | `WT_UNDERPANTS (10)` | Clothing |
| 8 | `undershirt` | `WT_UNDERSHIRT (12)` | Clothing |
| 9 | `skin` | `WT_SKIN (1)` | Body part (normally `'1'`; cannot be stripped without replacement) |
| 10 | `eyes` | `WT_EYES (3)` | Body part (normally `'1'`) |
| 11 | `hair` | `WT_HAIR (2)` | Body part (normally `'1'`) |
| 12 | `shape` | `WT_SHAPE (0)` | Body part (normally `'1'`) |
| 13 | `alpha` | `WT_ALPHA (13)` | Added in RLV 1.23+ |
| 14 | `tattoo` | `WT_TATTOO (14)` | Added in RLV 1.23+ |
| 15 | `physics` | `WT_PHYSICS (15)` | Added in RLV 2.x (`universal` = `WT_UNIVERSAL (16)` is supported as `@getoutfit:universal=<chan>` / `@remoutfit:universal=force` in RLVa 2.2+, excluded from the legacy 16-char base string unless extended) |

### 3.2 Canonical `@getattach` Attachment Point Order & RLV Names

Index `0` is always `'0'` (unattached sentinel). Indices `1..55` map to Second Life attachment point IDs:

| Slot ID | RLV `<point>` name | LSL Constant | Slot ID | RLV `<point>` name | LSL Constant |
|---|---|---|---|---|---|
| `0` | `none` | *(always `'0'`)* | `28` | `belly` | `ATTACH_BELLY` |
| `1` | `chest` | `ATTACH_CHEST` | `29` | `left pec` (`rpec` legacy) | `ATTACH_LPEC` |
| `2` | `skull` | `ATTACH_HEAD` | `30` | `right pec` (`lpec` legacy) | `ATTACH_RPEC` |
| `3` | `left shoulder` | `ATTACH_LSHOULDER` | `31` | `center 2` | `ATTACH_HUD_CENTER_2` |
| `4` | `right shoulder` | `ATTACH_RSHOULDER` | `32` | `top right` | `ATTACH_HUD_TOP_RIGHT` |
| `5` | `left hand` | `ATTACH_LHAND` | `33` | `top` | `ATTACH_HUD_TOP_CENTER` |
| `6` | `right hand` | `ATTACH_RHAND` | `34` | `top left` | `ATTACH_HUD_TOP_LEFT` |
| `7` | `left foot` | `ATTACH_LFOOT` | `35` | `center` | `ATTACH_HUD_CENTER_1` |
| `8` | `right foot` | `ATTACH_RFOOT` | `36` | `bottom left` | `ATTACH_HUD_BOTTOM_LEFT` |
| `9` | `spine` | `ATTACH_BACK` | `37` | `bottom` | `ATTACH_HUD_BOTTOM` |
| `10` | `pelvis` | `ATTACH_PELVIS` | `38` | `bottom right` | `ATTACH_HUD_BOTTOM_RIGHT` |
| `11` | `mouth` | `ATTACH_MOUTH` | `39` | `neck` | `ATTACH_NECK` |
| `12` | `chin` | `ATTACH_CHIN` | `40` | `root` (`avatar center`) | `ATTACH_AVATAR_CENTER` |
| `13` | `left ear` | `ATTACH_LEAR` | `41` | `left ring finger` | `ATTACH_LHAND_RING1` |
| `14` | `right ear` | `ATTACH_REAR` | `42` | `right ring finger` | `ATTACH_RHAND_RING1` |
| `15` | `left eyeball` | `ATTACH_LEYE` | `43` | `tail base` | `ATTACH_TAIL_BASE` |
| `16` | `right eyeball` | `ATTACH_REYE` | `44` | `tail tip` | `ATTACH_TAIL_TIP` |
| `17` | `nose` | `ATTACH_NOSE` | `45` | `left wing` | `ATTACH_LWING` |
| `18` | `r upper arm` | `ATTACH_RUARM` | `46` | `right wing` | `ATTACH_RWING` |
| `19` | `r forearm` | `ATTACH_RLARM` | `47` | `jaw` | `ATTACH_FACE_JAW` |
| `20` | `l upper arm` | `ATTACH_LUARM` | `48` | `alt left ear` | `ATTACH_FACE_LEAR` |
| `21` | `l forearm` | `ATTACH_LLARM` | `49` | `alt right ear` | `ATTACH_FACE_REAR` |
| `22` | `right hip` | `ATTACH_RHIP` | `50` | `alt left eye` | `ATTACH_FACE_LEYE` |
| `23` | `r upper leg` | `ATTACH_RULEG` | `51` | `alt right eye` | `ATTACH_FACE_REYE` |
| `24` | `r lower leg` | `ATTACH_RLLEG` | `52` | `tongue` | `ATTACH_FACE_TONGUE` |
| `25` | `left hip` | `ATTACH_LHIP` | `53` | `groin` | `ATTACH_GROIN` |
| `26` | `l upper leg` | `ATTACH_LULEG` | `54` | `left hind foot` | `ATTACH_HIND_LFOOT` |
| `27` | `l lower leg` | `ATTACH_LLLEG` | `55` | `right hind foot` | `ATTACH_HIND_RFOOT` |

---

## 4. Core Behavioural Restrictions, Exceptions & `=force` Actions

### 4.1 Teleportation

| Command | Kind | Viewer behaviour |
|---|---|---|
| `@tploc=n\|y` | Restriction | Blocks teleporting via World Map, SLURLs, coordinate entry, or double-click teleport |
| `@tplm=n\|y` | Restriction | Blocks teleporting via Inventory Landmarks and Favourites |
| `@tplure=n\|y` | Restriction | Blocks accepting teleport lures (`StartLure` / `TeleportLureRequest`) from other avatars unless exempted |
| `@tplure:<agent_uuid>=add\|rem` | Exception | Permits teleport lures from `<agent_uuid>` even while `@tplure=n` is active |
| `@sittp[:<max_dist>]=n\|y` | Restriction | Blocks click-to-sit on objects beyond `1.5m` (default when no `:<max_dist>` given) or beyond `<max_dist>` metres (prevents sit-teleporting out of traps) |
| `@accepttp[:<agent_uuid>]=add\|rem` | Auto-accept | Automatically accepts teleport lures (from anyone if no UUID, or specifically from `<agent_uuid>`) without confirmation dialog and bypasses `@tplure=n` for that sender |
| `@tpto:<X>/<Y>/<Z>[=<lookat>]=force` or `@tpto:<Region>/<X>/<Y>/<Z>=force` | Force action | Immediately initiates teleport to global `(X, Y, Z)` metres (RLV global coordinates) or named `<Region>/<x>/<y>/<z>` unless blocked by `@tploc=n` from *another* object (in RLVa, `@tpto=force` is typically blocked if `@unsit=n` prevents standing first, unless the same sessionunsits) |

### 4.2 Chat & Instant Messaging

| Command | Kind | Viewer behaviour |
|---|---|---|
| `@sendchat=n\|y` | Restriction | Garbles outbound public channel `0` speech to `"..."`:<br>• `/me ` emotes **remain allowed** (up to emote length cap, stripping `"..."` injection tricks unless `@emote` restricts)<br>• `(( ... ))` OOC chat remains allowed when `RestrainedLoveCanOOC` (`true`) is set<br>• Non-zero `/123` slash channels remain allowed unless `@sendchannel` restricts them |
| `@chatshout=n\|y` | Restriction | Downgrades outbound `Shout` (`2`, 100m) on channel `0` to `Normal` (`1`, 20m) |
| `@chatnormal=n\|y` | Restriction | Downgrades outbound `Normal` (`1`, 20m) and `Shout` (`2`) on channel `0` to `Whisper` (`0`, 10m) |
| `@chatwhisper=n\|y` | Restriction | Upgrades `Whisper` (`0`) to `Normal` (`1`) unless `@chatnormal=n` is also active (if both `@chatnormal=n` and `@chatwhisper=n` are held, mutes speech to `"..."`) |
| `@redirchat:<chan>=add\|rem` | Redirect | When outbound channel `0` public chat would be blocked/garbled (or redirected), silently send the raw ungarbled spoken text on positive script channel `<chan>` (`> 0`) via `ChatFromViewer` (`Low 80`) to every active `@redirchat` channel (skipping `/me` emotes unless `@rediremote:<chan>=add` is also set, and skipping `((OOC))`) |
| `@sendchannel[:<chan>]=n\|y` / `add\|rem` | Restriction + Exception | `@sendchannel=n` blocks outbound chat on **all** non-zero slash channels (`/<chan> text`); `@sendchannel:<chan>=add` (`@sendchannel_except:<chan>=add` in RLVa) exempts `<chan>` (or restricts `<chan>` specifically when `@sendchannel=n` is not set — check `LibreMetaverse.RLV.RlvPermissionsService.CanChat` semantics!) |
| `@recvchat=n\|y` & `@recvchat:<uuid>=add\|rem` | Restriction + Exception | Hides incoming avatar public chat (replacing text with `"..."` if `RestrainedLoveShowEllipsis` is true, except `/me` emotes and `((OOC))`), unless sender `<uuid>` holds a `@recvchat:<uuid>=add` exception |
| `@recvemote=n\|y` & `@recvemote:<uuid>=add\|rem` | Restriction + Exception | Suppresses incoming `/me` emotes unless `<uuid>` is exempted |
| `@sendim=n\|y` & `@sendim:<uuid_or_group>=add\|rem` | Restriction + Exception | Replaces outbound IM / group chat text with `"..."` unless recipient `<uuid>` (or `"allgroups"` / group UUID) is exempted |
| `@recvim=n\|y` & `@recvim:<uuid_or_group>=add\|rem` | Restriction + Exception | Blocks incoming IMs (auto-replying `"The Resident you messaged is prevented from reading your instant messages at the moment, please try again later."` for P2P IMs) unless sender `<uuid>` is exempted |

### 4.3 Movement & Sitting

| Command | Kind | Viewer behaviour |
|---|---|---|
| `@sit=n\|y` | Restriction | Blocks all user-initiated sitting on prims or ground |
| `@sit:<prim_uuid>=force` | Force action | Sends `AgentRequestSit` (`High 6`) + `AgentSit` (`High 7`) targeting `<prim_uuid>` if `<prim_uuid>` exists in scene, is within sit range (respecting `@sittp`), and sitting is not blocked |
| `@sitground=force` | Force action | Sits the avatar on the ground (`AGENT_CONTROL_SIT_ON_GROUND`) |
| `@unsit=n\|y` | Restriction | Disables the Stand Up button and blocks user-initiated standing (`AGENT_CONTROL_STAND_UP`) while seated |
| `@unsit=force` | Force action | Forces the avatar to stand up **unless** *another* object holds `@unsit=n` (note: in RLV/RLVa, even `@unsit=force` is blocked if any object currently enforces `@unsit=n`, so scripts must release their own `@unsit=y` before issuing `@unsit=force`!) |
| `@fly=n\|y`, `@temprun=n\|y`, `@alwaysrun=n\|y` | Restriction | Disables flying (`AGENT_CONTROL_FLY`) and running modes |

### 4.4 Attachments, Wearables, Inventory & World Interaction

| Command | Kind | Viewer behaviour |
|---|---|---|
| `@detach=n\|y` | Lock | issued with **no option**: locks **only the issuing attachment itself** (`SourceID`) against user detach! |
| `@detach:<attachpt_or_folder>=n\|y` | Restriction | Locks the named attachment point (e.g. `@detach:chest=n`) or `#RLV` subfolder against detaching |
| `@detach[:<attachpt_or_folder>]=force` | Force action | Detaches unlocked attachments at `<attachpt>` or inside `#RLV/<folder>` (skipping any item locked by `@detach=n` / `@remattach=n`) |
| `@addattach[:<attachpt>]=n\|y` & `@remattach[:<attachpt>]=n\|y` | Restriction | Prevents attaching new items to (or detaching items from) all attachment points or `<attachpt>` |
| `@attach:<folder>=force` / `@attachover:<folder>=force` | Force action | Attaches items from `#RLV/<folder>` (replacing vs stacking according to command or `+` folder prefix) |
| `@addoutfit[:<part>]=n\|y` & `@remoutfit[:<part>]=n\|y` | Restriction | Prevents wearing (`@addoutfit`) or taking off (`@remoutfit`) all wearable layers or specific `<part>` (`gloves`, `shirt`, `pants`, etc.) |
| `@remoutfit[:<part>]=force` | Force action | Strips unlocked clothing wearables (never body parts `shape`, `skin`, `eyes`, `hair`) matching `<part>` (or all clothing if omitted) |
| `@showinv=n\|y` | Restriction | Blocks opening the Inventory floater/tab (preventing manual detach or landmark use via inventory) |
| `@viewnote=n\|y`, `@viewscript=n\|y`, `@viewtexture=n\|y` | Restriction | Blocks opening Notecard, LSL Script, or Texture preview modals |
| `@edit=n\|y` & `@edit:<obj_uuid>=add\|rem` | Restriction + Exception | Closes Build/Edit tools and blocks editing/moving/taking objects unless exempted |
| `@rez=n\|y` | Restriction | Blocks rezzing objects from inventory or creating new prims |
| `@touchall=n\|y`, `@touchworld=n\|y`, `@touchattach=n\|y`, `@touchhud=n\|y` | Restriction | Blocks `ObjectGrab` / touch interactions by object category (`@touchworld:<uuid>=add` exempts specific prims; `@fartouch[:<dist>]=n` caps touch distance to `1.5m` or `<dist>`) |
| `@shownames=n\|y` (`@shownametags=n\|y`) | Restriction | Anonymises overhead 3D avatar nametags, radar names, and nearby chat sender names (replacing with dummy/blurred names except in `((OOC))`) |
| `@showloc=n\|y`, `@showworldmap=n\|y`, `@showminimap=n\|y` | Restriction | Hides region/parcel/coordinates in the top telemetry bar, SLURL copy actions, World Map, and Minimap |

---

## 5. Reference TypeScript Parser & Restriction Engine (`src/linkpoint/rlv*.ts` pattern)

```ts
export const CHAT_TYPE_OWNER = 8;

export interface RlvRule {
  sourceId: string;
  sourceName: string;
  behaviour: string;
  option: string; // "" when no :option was provided
}

export interface ParsedRlvToken {
  behaviour: string;
  option: string;
  param: string; // "" for bare @clear
}

export function parseRlvLine(rawMessage: string): ParsedRlvToken[] {
  const trimmed = rawMessage.trim();
  if (!trimmed.startsWith("@") || trimmed.length < 2) return [];

  const out: ParsedRlvToken[] = [];
  for (const rawSegment of trimmed.slice(1).split(",")) {
    const seg = rawSegment.trim().replace(/^@+/, "");
    if (!seg) continue;

    // Bare @clear or @clear:<filter> without '='
    const eqIdx = seg.indexOf("=");
    if (eqIdx === -1) {
      const colonIdx = seg.indexOf(":");
      const cmd = (colonIdx >= 0 ? seg.slice(0, colonIdx) : seg).toLowerCase();
      const opt = colonIdx >= 0 ? seg.slice(colonIdx + 1) : "";
      if (cmd === "clear") {
        out.push({ behaviour: "clear", option: opt, param: "" });
      }
      continue;
    }

    const lhs = seg.slice(0, eqIdx);
    const param = seg.slice(eqIdx + 1).trim();
    const colonIdx = lhs.indexOf(":");
    const behaviour = (colonIdx >= 0 ? lhs.slice(0, colonIdx) : lhs).trim().toLowerCase();
    const option = colonIdx >= 0 ? lhs.slice(colonIdx + 1).trim() : "";
    if (!behaviour) continue;
    out.push({ behaviour, option, param });
  }
  return out;
}

export class RlvRestrictionStore {
  private readonly rulesByObject = new Map<string, Map<string, RlvRule>>();

  private keyOf(behaviour: string, option: string): string {
    return option ? `${behaviour}:${option.toLowerCase()}` : behaviour;
  }

  add(sourceId: string, sourceName: string, behaviour: string, option = ""): void {
    // For bare @detach=n, bind the lock to sourceId itself
    const normalizedOpt = behaviour === "detach" && !option ? sourceId.toLowerCase() : option;
    let map = this.rulesByObject.get(sourceId);
    if (!map) {
      map = new Map();
      this.rulesByObject.set(sourceId, map);
    }
    map.set(this.keyOf(behaviour, normalizedOpt), {
      sourceId,
      sourceName,
      behaviour,
      option: normalizedOpt,
    });
  }

  remove(sourceId: string, behaviour: string, option = ""): void {
    const normalizedOpt = behaviour === "detach" && !option ? sourceId.toLowerCase() : option;
    const map = this.rulesByObject.get(sourceId);
    if (!map) return;
    map.delete(this.keyOf(behaviour, normalizedOpt));
    if (map.size === 0) this.rulesByObject.delete(sourceId);
  }

  clearObject(sourceId: string, filter = ""): void {
    if (!filter) {
      this.rulesByObject.delete(sourceId);
      return;
    }
    const map = this.rulesByObject.get(sourceId);
    if (!map) return;
    const needle = filter.toLowerCase();
    for (const [k] of map) {
      if (k.includes(needle)) map.delete(k);
    }
    if (map.size === 0) this.rulesByObject.delete(sourceId);
  }

  hasBehaviour(behaviour: string, option?: string): boolean {
    const targetKey = option !== undefined ? this.keyOf(behaviour, option) : null;
    for (const [, map] of this.rulesByObject) {
      if (targetKey !== null) {
        if (map.has(targetKey)) return true;
      } else {
        for (const rule of map.values()) {
          if (rule.behaviour === behaviour && rule.option === "") return true;
        }
      }
    }
    return false;
  }

  formatGetStatus(sourceId: string, filter = "", separator = "/"): string {
    const map = this.rulesByObject.get(sourceId);
    if (!map || map.size === 0) return "";
    const needle = filter.toLowerCase();
    const matched: string[] = [];
    for (const [k, rule] of map) {
      const token = rule.option && !(rule.behaviour === "detach" && rule.option === sourceId.toLowerCase())
        ? `${rule.behaviour}:${rule.option}`
        : rule.behaviour;
      if (!needle || k.includes(needle) || token.toLowerCase().includes(needle)) {
        matched.push(token);
      }
    }
    return matched.length > 0 ? separator + matched.join(separator) : "";
  }
}

export function transformPublicChatForSendchat(
  rawText: string,
  sendchatRestricted: boolean,
  allowOoc = true
): {garbledText: string; isEmote: boolean; isOoc: boolean} {
  const isEmote = /^\/me(\s|$)/i.test(rawText);
  const trimmed = rawText.trim();
  const isOoc = allowOoc && trimmed.startsWith("((") && trimmed.endsWith("))") && trimmed.length >= 4;
  if (!sendchatRestricted || isEmote || isOoc) {
    return { garbledText: rawText, isEmote, isOoc };
  }
  return { garbledText: "...", isEmote: false, isOoc: false };
}
```

---

## 6. Upstream File & Test Vector Cross-Check Index

### `cinderblocks/libremetaverse` (`LibreMetaverse.RLV`, BSD-3) — Primary Clean-Room Oracle
- `LibreMetaverse.RLV/RlvService.cs`: Top-level `ProcessMessageAsync`, `ReportItemDetachedAsync`, `ReportSitAsync`, `ReportUnsitAsync`, `Enabled` gate.
- `LibreMetaverse.RLV/RlvCommandProcessor.cs` & `RlvGetRequestHandler.cs`: Command tokeniser, `=n`/`=add` and `=y`/`=rem` handling, `@version`/`@versionnew`/`@versionnum`/`@getstatus`/`@getoutfit`/`@getattach`/`@getsitid` formatters.
- `LibreMetaverse.RLV/RlvRestrictionManager.cs` & `RlvPermissionsService.cs`: Per-prim restriction tracking, `RemoveRestrictionsForObjectsAsync`, `#RLV` `InventoryMap` locked-folder resolution, `CanChat`, `CanTpLoc`, `CanTpLm`, `CanUnsit`, `CanSitTp`.
- `LibreMetaverse.Tests/RLV/`: **150+ unit test files** across `Commands/` (20), `Exceptions/` (26), `Queries/` (17), and `Restrictions/` (80) — port these test vectors directly into Vitest / JUnit suites!

### `FirestormViewer/phoenix-firestorm` (Release Branches Only, LGPL-2.1)
- `indra/newview/rlvhandler.cpp` & `rlvhandler.h`: `RlvHandler::onAddRemCommand`, `processCommand`, `onChatFromSimulator` owner-say gate, attachment GC.
- `indra/newview/rlvactions.cpp`, `rlvlocks.cpp`, `rlvinventory.cpp`, `rlvui.cpp`, `rlvfloaters.cpp`: Behavioural hooks across teleport, chat garbling, attachment/wearable locks, `#RLV` shared folder, and `floater_rlv_behaviours.xml` / `floater_rlv_locks.xml` active-restriction inspectors.
- `indra/newview/app_settings/settings.xml` (Firestorm): `RestrainedLove` (`0`), `RestrainedLoveCanOOC` (`1`), `RestrainedLoveShowEllipsis` (`1`), `RestrainedLoveDebug` (`0`), `RestrainedLoveNoSetEnv` (`0`), `RestrainedLoveForbidGiveToRLV` (`0`), `RestrainedLoveStackWhenFolderBeginsWith` (`"+"`).
