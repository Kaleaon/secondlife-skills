---
name: secondlife_rlva
description: "Implement Restrained Love (RLV and RLVa) owner-say command parsing, positive-channel queries, per-object restriction maps, exceptions, and force actions safely."
---

# Second Life RLV and RLVa Viewer Behaviour

## Enforce the owner-say security boundary first

- Process `@`-prefixed commands **only** when RLVa is explicitly enabled by the user in viewer preferences and the packet arrives via `ChatFromSimulator` (`Low 139`, `Trusted`, `Unencoded`) with `ChatType == CHAT_TYPE_OWNER (8)` (`llOwnerSay`).

- Ignore `@` strings in whisper (`0`), normal public chat (`1`), shout (`2`), typing indicators (`4`, `5`), debug (`6`), region say (`7`), and arbitrary avatar chat, because allowing non-owner chat to trigger RLV turns public chat into a remote avatar hijack vector.

- Suppress valid executed `@` command lines from visible local chat history unless RLV debug logging (`RestrainedLoveDebug`) is enabled, so collar, HUD, and furniture handshakes do not flood chat tabs.

- Cross-check behaviour in order: `cinderblocks/libremetaverse` (`LibreMetaverse.RLV` and its 150+ unit tests under `LibreMetaverse.Tests/RLV`, BSD-3), `FirestormViewer/phoenix-firestorm` **release branches** (`indra/newview/rlv*.cpp`, LGPL-2.1), and `Kaleaon/react-linkpoint` (`src/linkpoint/rlv*.ts`).

- Never invent a GitHub URL for **Catznip** (Kitty Barnett's RLVa origin) or Marine Kelley's **Restrained Love viewer**, because neither has a verified GitHub repository; always consult the Third Party Viewer Directory source link and keep LGPL-2.1 obligations separate from BSD/MIT client code.

## Parse command batches and track restrictions per object

- Split each `@`-prefixed `llOwnerSay` line on commas left-to-right and parse each token as `@<behaviour>[:<option>]=<param>`, handling bare `@clear` (no `=`) alongside `@clear=<filter>` and `@clear:<filter>`.

- Treat `=add` as an exact synonym of `=n` and `=rem` as an exact synonym of `=y`: whether a command imposes a restriction (`@tplure=n`) or grants an exception (`@tplure:<uuid>=add` or `@tplure:<uuid>=n`) depends on `(behaviour, hasOption)`, never on `n` versus `add`.

- Key every active rule by `(sourceObjectId, behaviour, option)` so `=y` / `=rem` and `@clear[:filter]` lift restrictions **only** for that `sourceObjectId`, leaving identical restrictions held by other attachments intact.

- Subscribe to attachment detach and `KillObject` events so whenever an attached prim detaches, all restrictions held by its `UUID` are automatically garbage-collected (`RemoveRestrictionsForObjectsAsync`), and clear ephemeral session restrictions on logout.

## Reply to queries only on strictly positive channels

- Validate `<param>` as a 32-bit signed integer `channel > 0` for all query commands — never reply on channel `0` (public chat leak) or on `<= 0` channels for standard queries — and send replies via `ChatFromViewer` (`Low 80 = 0xFFFF0050`, `NotTrusted`, `Zerocoded`) with `ChatType = 1`.

- Implement the seven standard handshake and inspection queries scripts rely on first:
  - `@version=<chan>`: legacy `"RestrainedLife viewer v2.9.27 (RLVa 2.4.2)"` spelling preserved for older LSL parsers.
  - `@versionnew=<chan>`: modern `"RestrainedLove viewer v2.9.27 (RLVa 2.4.2)"` string.
  - `@versionnum=<chan>`: 7-digit integer version string such as `"2092700"` or `"3040300"`.
  - `@getstatus[:<filter>][;<sep>]=<chan>`: `"/"`-prefixed active rules held by `sourceObjectId` matching optional `<filter>`.
  - `@getoutfit[:<part>]=<chan>`: `"0"`/`"1"` bitstring across the 16 canonical wearable slots (`gloves` through `physics`), or single `"0"`/`"1"` for `<part>`.
  - `@getattach[:<point>]=<chan>`: `"0"`/`"1"` bitstring starting with `'0'` at index `0` (`none`) through the canonical attachment slots, or single `"0"`/`"1"` for `<point>`.
  - `@getsitid=<chan>`: `UUID` of the prim the avatar is seated on, or `00000000-0000-0000-0000-000000000000` when standing.

## Gate viewer actions across teleport, chat, sitting, and wearables

- Gate teleportation on `@tploc`, `@tplm`, `@tplure` (honouring `@tplure:<uuid>=add` exceptions), `@sittp[:<dist>]` (blocking click-to-sit beyond `1.5m` default or `<dist>`), `@accepttp[:<uuid>]=add` auto-accept lures, and `@tpto:<X>/<Y>/<Z>=force`.

- Gate chat and IM on `@sendchat` (garbling public channel `0` speech to `"..."` while preserving `/me` emotes, `((OOC))` when `RestrainedLoveCanOOC` is on, and slash channels unless `@sendchannel` restricts them), `@chatshout`, `@chatnormal`, `@chatwhisper`, `@redirchat:<chan>`, `@recvchat`, `@sendim`, and `@recvim` (with per-UUID exceptions).

- Gate movement and sitting on `@sit=n`, `@sit:<uuid>=force`, `@unsit=n`, and `@unsit=force` (remembering `@unsit=force` is still blocked if any object currently holds `@unsit=n`).

- Gate attachments, outfits, camera, inventory, and world UI on `@detach[:<pt>]=n` / `=force` (where bare `@detach=n` locks `sourceObjectId` itself), `@addattach`, `@remattach`, `@addoutfit`, `@remoutfit[:<part>]=n` / `=force` (stripping clothing only, never body parts `shape`, `skin`, `eyes`, `hair`), `#RLV` folder commands (`@attach[:<folder>]=force`, `@detachall:<folder>=force` / `@DetachAll`), `@camdistmax:<dist>=n`, `@camunlock=n`, `@showinv`, `@viewnote`, `@edit`, `@rez`, `@fartouch[:<dist>]=n`, `@shownames`, and `@showloc`.

- Always expose a clear active-restrictions inspector in viewer settings showing each holding object's name, UUID, and active rules so residents retain full transparency over what is restricting their client.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for `cinderblocks/libremetaverse`, `FirestormViewer/phoenix-firestorm`, and `Kaleaon/react-linkpoint`.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [LibreMetaverse](https://github.com/cinderblocks/libremetaverse) for `LibreMetaverse.RLV` and `LibreMetaverse.Tests/RLV` (BSD-3 semantic oracle and test suite).

- [Firestorm Viewer](https://github.com/FirestormViewer/phoenix-firestorm) for production C++ RLVa (`indra/newview/rlv*.cpp`) on release branches.

- [LSL Portal — RestrainedLove API](https://wiki.secondlife.com/wiki/LSL_Protocol/RestrainedLove_API) and the [Third Party Viewer Directory](https://wiki.secondlife.com/wiki/Third_Party_Viewer_Directory) for command specs and verified viewer source links.


## RLV versus RLVa and relay nuances in detail

- Marine Kelley's RLV is the original specification; Kitty Barnett's RLVa (originating in Catznip and shipped in Firestorm) re-implemented the engine cleanly for V2/V3 viewers with stricter modifier handling, `@versionnew`, and inspector floaters (`floater_rlv_behaviours.xml`, `floater_rlv_locks.xml`).

- In-world objects not owned by the avatar (such as furniture or traps owned by another resident) cannot emit `llOwnerSay` directly to the victim; instead they speak on negative RLV relay channel `-1812221819` (`cmd_name,victim_uuid,@cmd`) to a worn **RLV Relay** attachment owned by the user, which validates trust/mode and re-emits the `@` command via `llOwnerSay` (`ChatType == 8`).

- `#RLV` shared inventory folder: scripts attach and strip shared outfits via folder paths relative to the top-level `#RLV` inventory folder (`LibreMetaverse.RLV.InventoryMap`), respecting folder-prefix stacking rules (`+` prefix stacks rather than replaces per `RestrainedLoveStackWhenFolderBeginsWith`) and skipping `.private` hidden subfolders.

## Chat garbling and redirection order in detail

- When the user submits public chat on channel `0`, evaluate in order:
  1. Bypass garbling and redirection if the line is `(( ... ))` OOC chat and `RestrainedLoveCanOOC` is true.
  2. Treat `/me ` (and `/me'`) as an emote: allow it under `@sendchat=n` (stripping prohibited punctuation tricks if `@emote=n` is not set), and copy to `@rediremote:<chan>` channels if configured.
  3. For normal speech when `@redirchat:<chan>` channels are active and `@sendchat=n` suppresses public speech, dispatch the raw ungarbled message via `ChatFromViewer` (`Low 80`, `Zerocoded`) onto each active positive `<chan>` and suppress the `"..."` on channel `0`.
  4. For normal speech when `@sendchat=n` is active without `@redirchat`, transmit `"..."` on channel `0`, clamped by `@chatshout=n` / `@chatnormal=n` volume downgrades.

## Debugging playbook

- Symptom furniture or collar never detects RLVa on attach: check that `@version`, `@versionnew`, and `@versionnum` all reply on `channel > 0` via `ChatFromViewer` (`Low 80`, `Zerocoded`), and verify `@version` uses `"RestrainedLife"` while `@versionnew` uses `"RestrainedLove"`.

- Symptom `@tplure:<uuid>=add` blocks lures instead of allowing them: fix the parser so `=add` and `=n` share one code path that checks whether `:<uuid>` option is present (exception) versus absent (base restriction).

- Symptom restrictions stay stuck forever after detaching a collar or teleporting out of a trap: hook `KillObject` and attachment-point detach transitions to purge rules keyed by the detached prim's `SourceID`, and verify `@clear` works both with and without `=`.

- Symptom `@getoutfit` or `@getattach` confuses HUD scripts: return compact `"0"`/`"1"` bitstrings in the exact 16-wearable and `0..55` attachment-slot index orders rather than comma-separated item UUIDs.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/rlva-command-reference.md` (27,709 bytes)
