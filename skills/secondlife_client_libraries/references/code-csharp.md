# Second Life in C# — Complete LibreMetaverse Worked Programs

Canonical source: `cinderblocks/libremetaverse` — https://github.com/cinderblocks/libremetaverse (C#, BSD-3, .NET 8/9/10, NuGet `LibreMetaverse` 3.x). This file is the *worked programs* companion to the generated API catalogue (`skills/secondlife_client_libraries/references/libremetaverse-api.md` in this repo): the catalogue tells you what exists, these programs show complete, runnable-shaped uses of it.

Package layout reminder (3.x split — install only what a program uses):

- `LibreMetaverse` — `GridClient`, login, and the managers (Self, Network, Inventory, Objects, Groups, Friends, Assets, Appearance, Parcels).
- `LibreMetaverse.Types` — `UUID`, `Vector3`, `Quaternion`, primitives.
- `LibreMetaverse.StructuredData` — `OSD`, `OSDMap`, `OSDArray`, LLSD serialisers.
- `LibreMetaverse.Protocol` / `.Transport` — packets and the circuit, if you go below `GridClient`.
- `LibreMetaverse.LslTools` — LSL lexer/parser for tooling (program 7).
- `LibreMetaverse.Assets`, `.ModelFormats`, `.Rendering.MeshFoundry` — asset and geometry work.

Conventions in every program:

- Credentials come from the environment, never source. Login hashes are password-equivalent.
- Event handlers in LibreMetaverse fire on network threads. Programs marshal to their own queues/locks instead of doing slow work (console writes are the teaching exception, disk and HTTP work are not).
- API details that changed across the 2.x → 3.x split are called out where they bite. When a name here disagrees with the generated catalogue for the exact 3.x build you reference, the catalogue (scanned from source) wins.
- Test order, as everywhere in this repo: local OpenSim standalone first, then Aditi, then Agni.

```xml
<!-- Shared project file shape for programs 1–6 (adjust the package set per program). -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="LibreMetaverse" Version="3.2.1" />
  </ItemGroup>
</Project>
```

---

## Program 1 — Login bot with reconnect and clean logout

What it demonstrates: `LoginParams` construction, login progress events, the connected/disconnected event pair, a reconnect loop with backoff that distinguishes *auth failure* (never retry) from *transport death* (retry), heartbeat awareness, and a logout that actually sends `LogoutRequest` semantics via `Network.Logout()` instead of just dropping the socket (dropping the socket is how you ghost).

```csharp
// Program1_LoginBot.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program1
{
    private static GridClient Client = null!;
    private static string _first = "", _last = "", _password = "";
    private static volatile bool _intentionalLogout;
    private static int _reconnectAttempts;

    private static async Task Main()
    {
        _first = Env("SL_FIRST");
        _last = Env("SL_LAST");
        _password = Env("SL_PASSWORD");
        var loginUri = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                       ?? GridClient.DEFAULT_LOGIN_URI; // Agni; set SL_LOGIN_URI for OpenSim/Aditi

        Console.CancelKeyPress += (_, e) =>
        {
            e.Cancel = true;
            _intentionalLogout = true;
            Client?.Network.Logout();
        };

        while (!_intentionalLogout)
        {
            Client = new GridClient();
            WireEvents();
            var ok = await LoginOnce(loginUri);
            if (!ok)
            {
                // LoginOnce returns false only for non-retryable outcomes
                // (bad credentials, MFA required, TOS). Transport failures
                // after a successful login arrive via OnDisconnected.
                Console.WriteLine("[bot] non-retryable login outcome; stopping.");
                return;
            }

            // Park until the circuit dies or the user interrupts. The
            // client's own threads drive events; Main just waits.
            var tcs = new TaskCompletionSource();
            Client.Network.Disconnected += (_, _) => tcs.TrySetResult();
            await tcs.Task;

            if (_intentionalLogout) break;
            _reconnectAttempts++;
            var delay = TimeSpan.FromSeconds(Math.Min(60, 5 * _reconnectAttempts));
            Console.WriteLine($"[bot] disconnected; reconnect #{_reconnectAttempts} in {delay.TotalSeconds:0}s");
            await Task.Delay(delay);
        }
    }

    private static void WireEvents()
    {
        Client.Network.LoginProgress += (_, e) =>
        {
            // LoginStatus: Connecting, Redirecting, ReadingResponse,
            // Success, Failed. On Failed, e.Message carries the simulator's
            // reason string — surface it verbatim; it distinguishes bad
            // password from MFA from grid maintenance.
            Console.WriteLine($"[login] {e.Status}: {e.Message}");
            if (e.Status == LoginStatus.Failed)
            {
                Console.WriteLine("[login] failed — check reason above; " +
                                  "MFA accounts need the token flow, not a retry.");
            }
        };
        Client.Network.Connected += (_, _) =>
        {
            _reconnectAttempts = 0;
            Console.WriteLine($"[bot] connected to {Client.Network.CurrentSim?.Name} " +
                              $"as {Client.Self.Name}");
        };
    }

    private static async Task<bool> LoginOnce(string loginUri)
    {
        var loginParams = Client.Network.DefaultLoginParams(_first, _last, _password);
        loginParams.URI = loginUri;
        loginParams.Channel = "LibreMetaverseBot";
        loginParams.Version = "1.0.0";
        loginParams.Start = "last";
        // Login is synchronous-shaped in the classic API; run it off the
        // calling thread so progress events and timeouts behave.
        return await Task.Run(() => Client.Network.Login(loginParams));
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name} in the environment");
}
```

Reconnect design notes:

- **Backoff with a cap, and reset on success.** The counter resets in the Connected handler, not after login returns — a login that "succeeds" and immediately drops is a failing reconnect loop, not a fresh start.
- **Auth failures are terminal.** Bad password, MFA challenge, and TOS/maintenance responses will not heal by retrying; hammering the login server is also how accounts get rate-limited. Parse the failure reason, report, stop.
- **State does not survive reconnect.** Inventory caches, object tracking, group sessions, and the Event Queue all belong to the dead session. Rebuild them from the new login (program 3 and 4 structures are written to be re-runnable for exactly this reason).

---

## Program 2 — Chat and IM responder

What it demonstrates: nearby chat via `Self.Chat`, IM via `Self.IM` event subscription (`InstantMessage`), the dialog-code branch (plain message vs inventory offer vs teleport offer vs group notice), offline-IM awareness, typing/state flags, and an auto-reply policy that will not get the bot muted: reply once per sender per cooldown, never to itself, never to offline bursts, never to group notices.

```csharp
// Program2_ChatResponder.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program2
{
    private static GridClient Client = null!;
    private static readonly Dictionary<UUID, DateTime> _lastReply = new();
    private static readonly TimeSpan ReplyCooldown = TimeSpan.FromMinutes(5);

    private static void Main()
    {
        Client = new GridClient();
        Client.Settings.LOGIN_SERVER = GridClient.DEFAULT_LOGIN_URI;
        // For OpenSim: Client.Settings.LOGIN_SERVER = "http://127.0.0.1:9000/";

        Client.Self.Chat += OnChat;
        Client.Self.IM += OnInstantMessage;

        var loginParams = Client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        if (!Client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + Client.Network.LoginMessage);
            return;
        }
        Console.WriteLine($"[responder] in-world as {Client.Self.Name}. Ctrl+C to quit.");
        Console.ReadLine();
        Client.Network.Logout();
    }

    // ---- Nearby chat (ChatFromSimulator under the hood) ----
    private static void OnChat(object? sender, ChatEventArgs e)
    {
        // e.SourceType: Agent / Object / System. Objects "saying" things are
        // scripted content, not conversation — a responder that answers
        // objects will loop with every vending machine in the region.
        if (e.SourceType != ChatSourceType.Agent) return;
        if (e.FromName == Client.Self.Name) return; // never answer yourself

        Console.WriteLine($"[chat] {e.FromName}: {e.Message}");
        var text = e.Message.Trim();
        if (text.Equals("ping", StringComparison.OrdinalIgnoreCase))
        {
            Client.Self.Chat("pong", 0, ChatType.Normal);
        }
        else if (text.StartsWith("echo ", StringComparison.OrdinalIgnoreCase))
        {
            // Echo is capped: public chat is a shared space, and an
            // unbounded echo bot is a griefing tool with extra steps.
            var payload = text[5..];
            if (payload.Length <= 200) Client.Self.Chat(payload, 0, ChatType.Normal);
        }
        else if (text.Equals("time", StringComparison.OrdinalIgnoreCase))
        {
            Client.Self.Chat($"It is {DateTime.UtcNow:HH:mm:ss} UTC.", 0, ChatType.Normal);
        }
    }

    // ---- Instant messages (ImprovedInstantMessage + Event Queue paths) ----
    private static void OnInstantMessage(object? sender, InstantMessageEventArgs e)
    {
        var im = e.IM;
        // Dialog decides what this is. The plain-message case is only one
        // of many; treating every IM as conversation is the classic bug.
        switch (im.Dialog)
        {
            case InstantMessageDialog.MessageBox:
            case InstantMessageDialog.MessageFromAgent:
                HandleConversation(im);
                break;

            case InstantMessageDialog.InventoryOffered:
                // BinaryBucket carries the offered item/folder details.
                // Policy here: decline politely and log. Auto-accepting
                // inventory from strangers fills the account with junk and
                // can be used to plant misleadingly-named objects.
                Console.WriteLine($"[im] inventory offer from {im.FromName}; declining.");
                Client.Self.InstantMessage(
                    im.FromAgentID, "Thanks, I don't accept inventory automatically.",
                    im.IMSessionID, InstantMessageDialog.InventoryDeclined,
                    InstantMessageOnline.Online, Vector3.Zero, Client.Network.AgentID);
                break;

            case InstantMessageDialog.RequestTeleport:
                Console.WriteLine($"[im] teleport offer from {im.FromName} — ignored by policy.");
                break;

            case InstantMessageDialog.GroupNotice:
                // Group notices are one-to-many announcements, not chat.
                Console.WriteLine($"[group notice] {im.FromName}: {im.Message}");
                break;

            case InstantMessageDialog.SessionSend:
                // Group/conference session traffic arrives with the session
                // ID set; route it to the group handler (program 6), not
                // the 1:1 responder.
                Console.WriteLine($"[session {im.IMSessionID}] {im.FromName}: {im.Message}");
                break;

            default:
                Console.WriteLine($"[im] dialog={im.Dialog} from {im.FromName}: {im.Message}");
                break;
        }
    }

    private static void HandleConversation(InstantMessage im)
    {
        // Offline IMs (delivered in a burst at login) have Offline ==
        // Offline. Replying to them en masse is spammy and usually
        // pointless; log and skip.
        if (im.Offline == InstantMessageOnline.Offline)
        {
            Console.WriteLine($"[im/offline] {im.FromName}: {im.Message}");
            return;
        }
        Console.WriteLine($"[im] {im.FromName}: {im.Message}");

        lock (_lastReply)
        {
            if (_lastReply.TryGetValue(im.FromAgentID, out var last)
                && DateTime.UtcNow - last < ReplyCooldown)
            {
                return; // cooldown: one auto-reply per sender per window
            }
            _lastReply[im.FromAgentID] = DateTime.UtcNow;
        }

        var reply = im.Message.Trim().ToLowerInvariant() switch
        {
            "hi" or "hello" or "hey" => $"Hello, {im.FromName}. I am an automated assistant. " +
                                        "Say 'help' for what I can do.",
            "help" => "I can answer 'time' in nearby chat, echo short text, and confirm I received your IM.",
            _ => "Received. Say 'help' if you need the automated options.",
        };
        // For 1:1 IM the session ID matters: use the event's IMSessionID so
        // the reply lands in the same conversation thread.
        Client.Self.InstantMessage(im.FromAgentID, reply, im.IMSessionID);
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Responder policy, stated as code review rules: cooldown per sender (done above), a hard cap on reply length, no replies to objects/system chat, no replies to offline bursts, and a visible "I am automated" disclosure in the greeting. Bots that hide that they are bots get reported; bots that spam get banned; both outcomes are policy failures, not technical ones.

---

## Program 3 — Inventory explorer: FetchInventory2 reads, AIS3 writes

What it demonstrates: waiting for the inventory skeleton from login, folder-at-a-time fetching over the HTTP inventory caps (the manager does `FetchInventoryDescendents2` for you), item vs folder vs link handling, permission inspection, and the AIS3-shaped write operations the manager exposes (create folder, move item, create a link in the Current Outfit Folder). The explorer prints a tree, finds items by name, and — in its write demo — creates a folder and a COF link, the two operations that break most often in hand-rolled clients.

Key model facts the code relies on:

- `item_id`, `asset_id`, and `folder_id` are three different UUIDs. A link item has its own `item_id`, points at a target item, and has no asset of its own.
- Asset type and inventory type are separate enums; an item whose inventory type is `Object` usually carries an asset whose asset type is also object-ish, but wearables, gestures, and landmarks all diverge — print both, always.
- The Current Outfit Folder (COF) is a real folder under the inventory root's system folders; outfit changes are link operations inside it, versioned by the simulator (the AIS3 `IncrementCOFVersion` behaviour the C++ viewer does in `llaisapi.cpp`).

```csharp
// Program3_InventoryExplorer.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program3
{
    private static GridClient Client = null!;

    private static void Main(string[] args)
    {
        Client = new GridClient();
        var loginParams = Client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!Client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + Client.Network.LoginMessage);
            return;
        }

        // The inventory skeleton arrives with login, but folder *contents*
        // are fetched on demand. InventoryManager exposes the root and the
        // store; FetchFolder below drives the caps fetch per folder.
        var inv = Client.Inventory;
        var root = inv.RootFolder;
        Console.WriteLine($"Inventory root: {root.Name} ({root.UUID})");

        PrintTree(root, maxDepth: 2);

        if (args.Length > 0)
        {
            var needle = string.Join(' ', args);
            Console.WriteLine($"\n--- searching for '{needle}' ---");
            foreach (var hit in FindByName(root, needle))
            {
                Console.WriteLine($"{hit.Path}  item={hit.Item.UUID} asset={hit.Item.AssetUUID} " +
                                  $"invType={hit.Item.InventoryType} assetType={hit.Item.AssetType}");
            }
        }

        DemonstrateWrites(root);
        Client.Network.Logout();
    }

    // ---- reading ----
    private static void PrintTree(InventoryFolder folder, int maxDepth, int depth = 0)
    {
        var indent = new string(' ', depth * 2);
        Console.WriteLine($"{indent}[{folder.Name}] ({folder.UUID})");
        if (depth >= maxDepth) return;

        // EnsureContents / FetchFolderContents in the manager performs the
        // FetchInventoryDescendents2 cap call and populates folder's store
        // entries. It is async-shaped in 3.x; block at this teaching seam.
        Client.Inventory.FetchFolderContents(folder.UUID,
            Client.Self.AgentID, true, true, InventorySortOrder.ByDate)
            .Wait(TimeSpan.FromSeconds(30));

        foreach (var node in folder)
        {
            switch (node)
            {
                case InventoryFolder child:
                    PrintTree(child, maxDepth, depth + 1);
                    break;
                case InventoryItem item:
                    Console.WriteLine($"{indent}  - {item.Name} " +
                                      $"(inv={item.InventoryType}, asset={item.AssetType}, " +
                                      $"assetUUID={item.AssetUUID})");
                    break;
            }
        }
    }

    private sealed record Hit(string Path, InventoryItem Item);

    private static IEnumerable<Hit> FindByName(InventoryFolder root, string needle)
    {
        // Depth-first, fetching contents folder by folder. On a large
        // account this is thousands of cap calls if done naively against
        // the whole tree; scope the search (a start folder, a depth cap)
        // in real tools. The explorer caps depth at 8 for that reason.
        var stack = new Stack<(InventoryFolder Folder, string Path, int Depth)>();
        stack.Push((root, root.Name, 0));
        while (stack.Count > 0)
        {
            var (folder, path, depth) = stack.Pop();
            Client.Inventory.FetchFolderContents(folder.UUID, Client.Self.AgentID,
                true, true, InventorySortOrder.ByDate).Wait(TimeSpan.FromSeconds(30));
            foreach (var node in folder)
            {
                if (node is InventoryItem item &&
                    item.Name.Contains(needle, StringComparison.OrdinalIgnoreCase))
                {
                    yield return new Hit(path + "/" + item.Name, item);
                }
                else if (node is InventoryFolder child && depth < 8)
                {
                    stack.Push((child, path + "/" + child.Name, depth + 1));
                }
            }
        }
    }

    // ---- writing (AIS3 under the manager) ----
    private static void DemonstrateWrites(InventoryFolder root)
    {
        var inv = Client.Inventory;

        // 1) Create a folder. The manager issues the AIS3 create call and
        //    returns the new folder's UUID via callback/task in 3.x.
        var folderName = "LibreMetaverse Demo " + DateTime.UtcNow.ToString("yyyyMMdd");
        Console.WriteLine($"\nCreating folder '{folderName}' under root...");
        var newFolderId = inv.CreateFolder(root.UUID, folderName);
        Console.WriteLine($"  -> {newFolderId}");

        // 2) Permissions sanity print for the first object item we can find:
        //    creator, owner, and the base/next-owner masks decide what a
        //    client is even allowed to offer to do with an item. UIs that
        //    show operations the permissions forbid generate support mail.
        var firstObject = FindByName(root, "").FirstOrDefault(h => h.Item is InventoryItem);
        // (FindByName with an empty needle yields everything; a real tool
        // would take the first InventoryObject item directly.)

        // 3) COF link creation: find the Current Outfit folder, then link
        //    an existing wearable/body item into it. This is the operation
        //    whose LLSD shape (link create with target item id, in the COF,
        //    with version increment) hand-rolled clients most often get
        //    wrong — the manager's CreateLink / outfit APIs exist precisely
        //    so you do not hand-roll it.
        var cof = inv.GetCurrentOutfitFolder();
        if (cof != null)
        {
            Console.WriteLine($"Current Outfit Folder: {cof.UUID} " +
                              $"({cof.Count} entries at login)");
            Console.WriteLine("  (link creation demo skipped: pass a wearable item id " +
                              "to inv.CreateLink(cof.UUID, itemId, name, description))");
        }
        else
        {
            Console.WriteLine("No COF found — the account may predate COF, or the " +
                              "skeleton has not fully arrived. Wait and retry; do not " +
                              "create a folder *named* like the COF as a substitute.");
        }
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Inventory pitfalls this program is structured to avoid:

- **Fetching everything.** Folder-at-a-time, depth-capped, with the fetch awaited per folder. The manager will happily let you request the whole tree; the simulator will happily take minutes and the account holder will happily close your app.
- **Treating links as items.** A link's `AssetUUID` is meaningless; follow `InventoryType == Link` to its target item before offering wear/copy operations.
- **Writing via the read path.** Fetch caps cannot create or move anything. If a "move" implementation is issuing fetches and hoping, it is not moving anything — writes are AIS3 (or legacy UDP for the shrinking set of operations AIS does not cover, per `llaisapi.cpp`).

---

## Program 4 — Object radar with ObjectUpdate events

What it demonstrates: subscribing to object updates from the Objects manager, distinguishing avatars from prims from attachments in the update stream, maintaining a live radar table keyed by local ID and UUID, handling `KillObject`, terse updates (the manager decodes them — your job is to not re-quantise), simulator switching (a teleport invalidates every local ID), and distance-ordered reporting like Radegast's radar.

Local IDs are per-simulator and per-session. UUIDs are forever. Key your durable state by UUID, your per-frame state by (simulator, local ID), and clear the whole table on teleport — stale local IDs after a region change are the #1 radar bug.

```csharp
// Program4_ObjectRadar.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program4
{
    private static GridClient Client = null!;
    private static readonly Dictionary<uint, RadarEntry> _byLocalId = new();
    private static readonly object _lock = new();

    private sealed class RadarEntry
    {
        public uint LocalId;
        public UUID Id;
        public bool IsAvatar;
        public bool IsAttachment;
        public Vector3 Position;       // region-local
        public string Name = "";       // avatars: via name lookup; prims: often empty until properties arrive
        public DateTime LastSeen = DateTime.UtcNow;
    }

    private static void Main()
    {
        Client = new GridClient();
        // Object tracking must be enabled or the manager discards updates.
        Client.Settings.ALWAYS_DECODE_OBJECTS = true;
        Client.Settings.ALWAYS_REQUEST_OBJECTS = true;

        Client.Objects.ObjectUpdate += OnObjectUpdate;
        Client.Objects.KillObject += OnKillObject;
        Client.Network.SimChanged += (_, _) =>
        {
            // Teleport / region cross: every local ID is meaningless now.
            lock (_lock) _byLocalId.Clear();
            Console.WriteLine("[radar] simulator changed; radar cleared.");
        };
        Client.Avatars.ViewerEffectPointAt += (_, _) => { }; // (example of a neighbouring event family)

        var loginParams = Client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!Client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + Client.Network.LoginMessage);
            return;
        }
        Console.WriteLine("[radar] running. Commands: 'list', 'avatars', 'quit'");

        string? line;
        while ((line = Console.ReadLine()) != null)
        {
            switch (line.Trim().ToLowerInvariant())
            {
                case "list": PrintRadar(avatarsOnly: false); break;
                case "avatars": PrintRadar(avatarsOnly: true); break;
                case "quit": Client.Network.Logout(); return;
            }
        }
    }

    private static void OnObjectUpdate(object? sender, PrimEventArgs e)
    {
        // e.Prim is a Primitive for objects, or an Avatar when the update
        // describes an agent. e.Simulator identifies the region — updates
        // also arrive for neighbour regions (child agents' views), which a
        // radar should either label or filter; this program keeps only the
        // current simulator's objects.
        if (e.Simulator != Client.Network.CurrentSim) return;

        lock (_lock)
        {
            if (e.Prim is Avatar avatar)
            {
                _byLocalId[avatar.LocalID] = new RadarEntry
                {
                    LocalId = avatar.LocalID,
                    Id = avatar.ID,
                    IsAvatar = true,
                    Position = avatar.Position,
                    Name = avatar.Name,
                    LastSeen = DateTime.UtcNow,
                };
            }
            else
            {
                var prim = e.Prim;
                if (!_byLocalId.TryGetValue(prim.LocalID, out var entry))
                {
                    entry = new RadarEntry { LocalId = prim.LocalID, Id = prim.ID };
                    _byLocalId[prim.LocalID] = entry;
                }
                entry.Position = prim.Position;
                // Attachments have a non-zero ParentID pointing at an avatar
                // (or a linkset root) and an AttachPoint when worn.
                entry.IsAttachment = prim.ParentID != 0;
                entry.LastSeen = DateTime.UtcNow;
                // Prim *names* do not ride ObjectUpdate; they arrive via
                // ObjectProperties replies after a RequestObjectProperties
                // call. A radar that shows blank names is not broken — it
                // has not asked yet. Ask selectively (visible/near objects),
                // never for the whole region at once.
            }
        }
    }

    private static void OnKillObject(object? sender, KillObjectEventArgs e)
    {
        lock (_lock)
        {
            foreach (var localId in e.Objects)
                _byLocalId.Remove(localId);
        }
    }

    private static void PrintRadar(bool avatarsOnly)
    {
        var me = Client.Self.SimPosition;
        List<RadarEntry> rows;
        lock (_lock) rows = _byLocalId.Values.ToList();
        var ordered = rows
            .Where(r => !avatarsOnly || r.IsAvatar)
            .Select(r => (Entry: r, Distance: Vector3.Distance(me, r.Position)))
            .OrderBy(x => x.Distance)
            .Take(30);
        foreach (var (entry, distance) in ordered)
        {
            var kind = entry.IsAvatar ? "AVATAR" : entry.IsAttachment ? "attach" : "prim";
            var label = entry.IsAvatar ? entry.Name : entry.Id.ToString()[..8];
            Console.WriteLine($"  [{kind}] {label}  {distance:0.0} m  local={entry.LocalId}");
        }
        Console.WriteLine($"  ({rows.Count} objects tracked)");
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Radar notes:

- **Request object properties sparingly.** Names, owners, and descriptions come from `ObjectProperties` replies. Requesting them for every object in a busy region is a packet flood the simulator will throttle; Radegast requests on selection/visibility, and so should you.
- **Terse updates move things without full updates.** If your radar only handles full `ObjectUpdate` shapes at your own protocol layer you will miss movement; at the `GridClient` layer the manager has already merged terse updates into the same event — one of the strongest reasons to build radars on the manager instead of raw packets.
- **Attachments are not scene objects for most purposes.** Filter them out of "objects near me" counts unless the user asked about worn items specifically.

---

## Program 5 — Texture downloader via caps (GetTexture), with JPEG2000 notes

What it demonstrates: asking the simulator for its cap map through the client's network layer, fetching a texture asset over the `GetTexture` HTTP cap instead of the legacy UDP image path, handling the 404-means-missing case by UUID, writing the raw J2C codestream to disk untouched, and — as a second half — decoding it with the imaging stack to a PNG while recording discard-level information. Textures are the highest-volume asset class; a downloader that re-fetches on every run or that "helpfully" transcodes the stored copy destroys both bandwidth and fidelity.

```csharp
// Program5_TextureDownloader.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program5
{
    private static async Task Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("Usage: TextureDownloader <texture-uuid> [out-dir]");
            return;
        }
        var textureId = new UUID(args[0]);
        var outDir = args.Length > 1 ? args[1] : "textures";
        Directory.CreateDirectory(outDir);

        var client = new GridClient();
        var loginParams = client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + client.Network.LoginMessage);
            return;
        }

        var j2cPath = Path.Combine(outDir, textureId + ".j2c");
        if (File.Exists(j2cPath))
        {
            // Assets are immutable by UUID: if you have the bytes for a
            // UUID, you have THE bytes, forever. Never re-download.
            Console.WriteLine($"[tex] cache hit: {j2cPath}");
        }
        else
        {
            // Assets.DownloadAsset / RequestAsset in the manager routes
            // through the GetTexture cap when the region grants it and
            // falls back to the legacy path when it does not — the same
            // request-and-check-with-fallback pattern the viewer uses.
            var received = new ManualResetEventSlim(false);
            AssetDownload? result = null;
            client.Assets.RequestAsset(textureId, AssetType.Texture,
                true, (_, download) =>
                {
                    result = download;
                    received.Set();
                });
            if (!received.Wait(TimeSpan.FromSeconds(60)))
            {
                Console.WriteLine("[tex] timed out waiting for the asset service.");
                client.Network.Logout();
                return;
            }
            if (result is not { Success: true })
            {
                // Missing asset: log the UUID. There is no name to log —
                // the asset system does not know one.
                Console.WriteLine($"[tex] asset {textureId} not delivered " +
                                  $"(status={result?.Status.ToString() ?? "null"}).");
                client.Network.Logout();
                return;
            }
            await File.WriteAllBytesAsync(j2cPath, result!.AssetData);
            Console.WriteLine($"[tex] saved {result.AssetData.Length} bytes -> {j2cPath}");
        }

        // Optional decode: J2C -> PNG via the imaging package
        // (LibreMetaverse.Imaging, CSJ2K lineage). Decoding is lossy in
        // time, not in data: keep the .j2c as the archival copy and treat
        // the PNG as a view. A partial/corrupt codestream decodes to a
        // partially grey image with some decoders and throws with others;
        // either outcome must be reported, not hidden.
        try
        {
            var bytes = await File.ReadAllBytesAsync(j2cPath);
            var managed = LibreMetaverse.Imaging.ManagedImage.FromBytes(bytes);
            var pngPath = Path.Combine(outDir, textureId + ".png");
            using var fs = File.Create(pngPath);
            managed.ExportPng(fs); // (imaging API shape per the 3.x Imaging package)
            Console.WriteLine($"[tex] decoded {managed.Width}x{managed.Height} -> {pngPath}");
            Console.WriteLine("[tex] note: OpenJPEG/Kakadu-class decoders differ on " +
                              "partial codestreams; a grey lower half usually means a " +
                              "truncated download, not a corrupt asset on the grid.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[tex] decode failed: {ex.GetType().Name}: {ex.Message}");
        }

        client.Network.Logout();
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Downloader rules worth encoding in any asset tool:

- **UUID-keyed cache, immutable forever.** Content addressing means the cache never needs invalidation — only eviction.
- **Store the codestream, derive the views.** Transcoding on ingest loses the original discard structure and makes later codec comparisons impossible.
- **Range/discard awareness.** The `GetTexture` cap supports HTTP range requests so viewers pull progressive discard levels. A batch downloader that wants full assets should say so (whole-asset request, as here); a preview tool should request the low-discard prefix instead of downloading 2 MB to show a thumbnail.

---

## Program 6 — Group manager: list, members, notices, and session chat

What it demonstrates: reading the agent's group list after login (`Groups` manager + the current-groups reply), fetching a group's member roster, sending a group notice (with the permissions check that must precede it — notice rights are a group role ability, not a membership default), and joining/sending to the group chat session via the session flow (start session → session ID → `InstantMessage` with the session dialog). Everything here is an operation hand-rolled clients most often implement against the wrong plane: group *data* is caps/UDP manager traffic, group *chat* is a session, group *notices* are their own message with an optional attached item.

```csharp
// Program6_GroupManager.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program6
{
    private static GridClient Client = null!;
    private static readonly ManualResetEventSlim _groupsReady = new(false);
    private static Dictionary<UUID, Group> _groups = new();

    private static void Main()
    {
        Client = new GridClient();
        Client.Groups.CurrentGroups += (_, e) =>
        {
            _groups = e.Groups;
            _groupsReady.Set();
        };
        Client.Groups.GroupMembersReply += OnGroupMembers;

        var loginParams = Client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!Client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + Client.Network.LoginMessage);
            return;
        }

        Client.Groups.RequestCurrentGroups();
        if (!_groupsReady.Wait(TimeSpan.FromSeconds(30)))
        {
            Console.WriteLine("Group list did not arrive in time.");
            Client.Network.Logout();
            return;
        }

        Console.WriteLine($"Member of {_groups.Count} groups:");
        foreach (var group in _groups.Values)
        {
            Console.WriteLine($"  {group.Name}  ({group.ID})  " +
                              $"title='{group.MyTitle}' powers={group.MyPowers}");
        }

        var first = _groups.Values.FirstOrDefault();
        if (first != null)
        {
            Console.WriteLine($"\nRequesting members of {first.Name}...");
            Client.Groups.RequestGroupMembers(first.ID);
            Thread.Sleep(3000); // teaching seam: await the reply event properly in real code

            SendNoticeIfAllowed(first);
            JoinAndSayInGroupChat(first);
        }

        Client.Network.Logout();
    }

    private static void OnGroupMembers(object? sender, GroupMembersReplyEventArgs e)
    {
        Console.WriteLine($"[members] {e.Members.Count} members in group {e.GroupID}:");
        foreach (var member in e.Members.Values.Take(20))
        {
            Console.WriteLine($"    {member.Title}  agent={member.AgentID}  " +
                              $"powers={member.Powers}");
        }
        if (e.Members.Count > 20) Console.WriteLine("    ... (truncated)");
    }

    private static void SendNoticeIfAllowed(Group group)
    {
        // Group notices require the SendNotices ability in the sender's
        // role for that group. Check the powers bit first and explain a
        // refusal — a notice call without the ability fails silently at
        // the simulator, which reads to users as 'the tool is broken'.
        const GroupPowers noticePower = GroupPowers.SendNotices;
        if ((group.MyPowers & noticePower) == 0)
        {
            Console.WriteLine($"[notice] skipped: no SendNotices ability in {group.Name}.");
            return;
        }
        // Notices can carry one attached inventory item (by item UUID);
        // pass UUID.Zero for a text-only notice.
        Client.Groups.SendGroupNotice(group.ID,
            "LibreMetaverse demo notice",
            "Sent from Program6_GroupManager. No attachment.",
            UUID.Zero);
        Console.WriteLine($"[notice] sent to {group.Name}.");
    }

    private static void JoinAndSayInGroupChat(Group group)
    {
        // Group chat is a session: request the session, wait for the
        // start/invitation events, then send with the session's ID and the
        // session-send dialog. Sending an IM 'to the group UUID' without
        // a session is the classic no-op.
        Client.Self.IM += (_, e) =>
        {
            if (e.IM.Dialog == InstantMessageDialog.SessionSend
                || e.IM.Dialog == InstantMessageDialog.SessionGroupStart)
            {
                Console.WriteLine($"[groupchat:{group.Name}] {e.IM.FromName}: {e.IM.Message}");
            }
        };

        Client.Groups.RequestGroupChatSession(group.ID);
        // In a full client you now wait for the session-start confirmation
        // event carrying the session ID, then:
        //   Client.Self.InstantMessage(group.ID, "hello group", sessionID,
        //       InstantMessageDialog.SessionSend, ...);
        // The teaching build logs the request and leaves the session open;
        // the session closes on logout or after the simulator's idle rules.
        Console.WriteLine($"[groupchat] session requested for {group.Name}; " +
                          "send once the start event confirms the session ID.");
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Group pitfalls:

- **Powers are per-group and per-role.** The same account can send notices in one group and be a plain member in another. Always branch on `MyPowers` for the group in question.
- **Notices vs chat vs IM are three different features** sharing one word ("group message") in user language. Map the user's words to the right mechanism before writing code.
- **Member lists are paginated in effect if not in form.** A 40,000-member group's roster reply is a flood; request it on demand, stream it, and never block login on it.

---

## Program 7 — LSL tools: lexing and parsing LSL with LslTools

What it demonstrates: using the `LibreMetaverse.LslTools` package (the LSL lexer/parser that ships with the LibreMetaverse family) as a *tooling* front-end: tokenise a script, report token statistics, flag the constructs that break ports (Firestorm preprocessor directives, `os*` calls that will not compile on Agni, deprecated functions), and extract the function-call inventory of a script. This is the .NET counterpart of the `tailslide`/`lslint` approach — a front-end for analysis, not a compiler; the simulator compiles scripts, never the client.

The exact LslTools type names have moved between releases; the program is written against the package's lexer-first surface and isolates it behind one adapter method (`Lex`) so a rename touches one place. Canonical signatures for what counts as an LSL function/event/constant come from `secondlife/lsl-definitions` — the checker below loads the function name set from that YAML's exported list (here: a plain text file, one name per line, generated from `lsl_definitions.yaml`).

```csharp
// Program7_LslToolsCheck.cs
// Extra package: LibreMetaverse.LslTools (see the package's current API;
// the Lex() adapter below is the only place that touches it directly).
using System.Text.RegularExpressions;

internal static class Program7
{
    private static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("Usage: LslCheck <script.lsl> [known-functions.txt]");
            return;
        }
        var source = File.ReadAllText(args[0]);
        var knownFunctions = args.Length > 1
            ? new HashSet<string>(File.ReadAllLines(args[1])
                .Select(l => l.Trim()).Where(l => l.Length > 0))
            : DefaultKnownFunctions();

        Console.WriteLine($"Script: {args[0]} ({source.Length} chars)");

        var tokens = Lex(source);
        Console.WriteLine($"Tokens: {tokens.Count} " +
                          $"(identifiers={tokens.Count(t => t.Kind == "ident")}, " +
                          $"strings={tokens.Count(t => t.Kind == "string")}, " +
                          $"numbers={tokens.Count(t => t.Kind == "number")})");

        CheckPreprocessor(source);
        CheckCalls(source, knownFunctions);
        CheckEvents(source);
        EstimateMemoryPressure(source);
    }

    // ---- lexer adapter -------------------------------------------------
    private sealed record Token(string Kind, string Text, int Line);

    private static List<Token> Lex(string source)
    {
        // Adapter over LslTools' lexer. If the referenced build exposes
        // its lexer under a different type name, this is the one method
        // to adjust; everything downstream consumes Token records.
        var lexerType = typeof(LibreMetaverse.LslTools.LSLLexer);
        // (Reflection-free in production: call the lexer directly once the
        // package version is pinned. The shape consumed is: a stream of
        // (kind, text, line) triples, with comments stripped and string
        // literals delivered whole.)
        _ = lexerType; // keep the reference explicit for the reader
        return FallbackLex(source);
    }

    /// <summary>
    /// A small self-contained LSL lexer used when running this checker
    /// without the LslTools package restored. It understands the token
    /// classes the checks below need — identifiers, strings with escapes,
    /// numbers, comments (// and /* */), and punctuation — and nothing
    /// else. It is a lexer, not a parser: it will happily tokenise
    /// syntactically invalid LSL, which is fine for lint-style checks.
    /// </summary>
    private static List<Token> FallbackLex(string source)
    {
        var tokens = new List<Token>();
        var i = 0;
        var line = 1;
        while (i < source.Length)
        {
            var c = source[i];
            if (c == '\n') { line++; i++; continue; }
            if (char.IsWhiteSpace(c)) { i++; continue; }
            if (c == '/' && i + 1 < source.Length && source[i + 1] == '/')
            {
                while (i < source.Length && source[i] != '\n') i++;
                continue;
            }
            if (c == '/' && i + 1 < source.Length && source[i + 1] == '*')
            {
                i += 2;
                while (i + 1 < source.Length && !(source[i] == '*' && source[i + 1] == '/'))
                {
                    if (source[i] == '\n') line++;
                    i++;
                }
                i += 2;
                continue;
            }
            if (c == '"')
            {
                var start = i++;
                while (i < source.Length && source[i] != '"')
                {
                    if (source[i] == '\\') i++; // skip escaped char
                    i++;
                }
                i++; // closing quote
                tokens.Add(new Token("string", source[start..i], line));
                continue;
            }
            if (char.IsDigit(c))
            {
                var start = i;
                while (i < source.Length && (char.IsDigit(source[i]) || source[i] == '.')) i++;
                tokens.Add(new Token("number", source[start..i], line));
                continue;
            }
            if (char.IsLetter(c) || c == '_')
            {
                var start = i;
                while (i < source.Length && (char.IsLetterOrDigit(source[i]) || source[i] == '_')) i++;
                tokens.Add(new Token("ident", source[start..i], line));
                continue;
            }
            tokens.Add(new Token("punct", c.ToString(), line));
            i++;
        }
        return tokens;
    }

    // ---- checks ----------------------------------------------------------
    private static void CheckPreprocessor(string source)
    {
        // Firestorm's in-viewer editor accepts a C-style preprocessor and
        // extensions (switch, lazy list indexing). Stock editors and
        // OpenSim do not. Any leading-# directive is a port blocker.
        foreach (Match m in Regex.Matches(source, @"^\s*#\s*(\w+)", RegexOptions.Multiline))
        {
            Console.WriteLine($"[preprocessor] line directive '#{m.Groups[1].Value}' — " +
                              "Firestorm preprocessor construct; expand it before " +
                              "compiling in the stock editor or OpenSim.");
        }
        if (Regex.IsMatch(source, @"\bswitch\s*\("))
        {
            Console.WriteLine("[extension] 'switch' is a Firestorm preprocessor " +
                              "extension, not stock LSL.");
        }
    }

    private static void CheckCalls(string source, HashSet<string> knownFunctions)
    {
        var calls = Regex.Matches(source, @"\b(ll|os|mod|wl)[A-Z]\w*\s*\(")
            .Select(m => m.Value.TrimEnd(' ', '(')).Distinct().OrderBy(x => x);
        Console.WriteLine("\nFunction calls found:");
        foreach (var call in calls)
        {
            var tag = call.StartsWith("ll")
                ? (knownFunctions.Contains(call) ? "lsl" : "lsl? (not in definitions — check spelling/age)")
                : call.StartsWith("os") ? "OSSL — OpenSim only, compile error on Agni"
                : call.StartsWith("mod") ? "mod* — OpenSim module call, grid-specific"
                : "wl* — LightShare, OpenSim only";
            Console.WriteLine($"  {call}  [{tag}]");
        }
    }

    private static void CheckEvents(string source)
    {
        string[] events =
        {
            "state_entry", "state_exit", "touch_start", "touch", "touch_end",
            "collision_start", "collision", "collision_end", "listen",
            "sensor", "no_sensor", "timer", "money", "attach", "changed",
            "http_request", "http_response", "dataserver", "link_message",
            "moving_start", "moving_end", "object_rez", "on_rez",
            "run_time_permissions", "control", "at_target", "not_at_target",
            "at_rot_target", "not_at_rot_target", "land_collision_start",
            "land_collision", "land_collision_end", "email",
            "experience_permissions", "experience_permissions_denied",
        };
        var found = events.Where(e => Regex.IsMatch(source, $@"\b{e}\s*\(")).ToList();
        Console.WriteLine($"\nEvents handled ({found.Count}): {string.Join(", ", found)}");
        if (found.Count == 0)
        {
            Console.WriteLine("[warn] no event handlers found — is this a library " +
                              "include rather than a complete script?");
        }
        if (found.Contains("timer") && !source.Contains("llSetTimerEvent"))
        {
            Console.WriteLine("[warn] timer() handler without llSetTimerEvent — " +
                              "the timer will never fire.");
        }
    }

    private static void EstimateMemoryPressure(string source)
    {
        // Crude but honest heuristic, labelled as such: Mono scripts have
        // 64 KB total. String literal volume and list-building in loops
        // are the usual killers; this flags the visible half of the risk.
        var stringBytes = Regex.Matches(source, @"""([^""\\]|\\.)*""")
            .Sum(m => m.Length);
        var listOps = Regex.Matches(source, @"llList2\w+|llDumpList2String|\+ \[").Count;
        Console.WriteLine($"\nMemory pressure (heuristic): ~{stringBytes} chars of string " +
                          $"literals, {listOps} list-conversion sites. Mono limit is 65536 " +
                          "bytes for stack+heap combined; profile with llGetObjectMemory " +
                          "in-world before shipping.");
    }

    private static HashSet<string> DefaultKnownFunctions() => new()
    {
        // Abridged fallback set (the full set belongs in the generated
        // known-functions.txt from lsl_definitions.yaml — 529 names).
        "llSay", "llWhisper", "llShout", "llOwnerSay", "llListen",
        "llSetText", "llSetPrimitiveParams", "llGetPrimitiveParams",
        "llRequestPermissions", "llGetPermissions", "llSetTimerEvent",
        "llSensor", "llSensorRepeat", "llDetectedKey", "llGetOwner",
        "llGetPos", "llSetPos", "llGetRot", "llSetRot", "llRezObject",
        "llGiveInventory", "llHTTPRequest", "llJsonGetValue",
        "llJsonSetValue", "llList2String", "llGetListLength",
        "llStringLength", "llGetSubString", "llKey2Name", "llGetDisplayName",
        "llInstantMessage", "llTeleportAgent", "llAttachToAvatar",
        "llStartAnimation", "llStopAnimation", "llPlaySound",
    };
}
```

## Closing notes for the C# stack

- **GridClient is a session object.** One client, one login, one region at a time (plus neighbour visibility). Programs that need fleets of bots create one client per bot and accept the per-bot thread/memory cost; sharing a client across "bots" is not a thing.
- **Events are the API.** Every program above is structured as: configure → subscribe → login → react → logout. Polling-style code fought the library at every step in the libOpenMetaverse era and still does; if you find yourself writing a `while` loop that inspects manager state, look for the event first (the generated catalogue's per-class Event entries are the index).
- **The 2.x → 3.x split is the migration that matters.** Old samples use `OpenMetaverse.*` namespaces and monolithic packages; 3.x uses `LibreMetaverse.*` with the package split listed at the top of this file. Port by namespace and package first, then by the handful of renamed managers — and let the generated API catalogue, not a decade of blog posts, arbitrate names.
- **OpenSim quirks are settings, not forks.** `GridClient` against an OpenSim login URI mostly just works; where behaviour differs (caps subsets, AIS coverage, group features), the difference is data the program should detect (cap presence, SimulatorFeatures) rather than a build flag.

---

## Program 8 — Teleport handling and appearance/COF basics

What it demonstrates: offering and accepting teleports (`Self.Teleport`, teleport event outcomes), the session rebuild obligations after a successful teleport (object radar clears, group sessions die, Event Queue restarts — the managers handle the transport half, your state is yours), and the appearance flow at manager level: find wearables in inventory, wear by item, and understand what the COF link operations from program 3 are *for* — an outfit is a set of links in the COF plus the appearance message the simulator bakes from them (Bakes on Mesh means the *server* composites system layers; the client sends the right wearable set and appearance parameters, it does not composite textures itself).

```csharp
// Program8_TeleportAppearance.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program8
{
    private static GridClient Client = null!;
    private static readonly ManualResetEventSlim _teleportDone = new(false);
    private static bool _teleportOk;

    private static async Task Main()
    {
        Client = new GridClient();
        Client.Self.TeleportProgress += (_, e) =>
        {
            // TeleportStatus: Start, Progress, Failed, Complete.
            // Progress messages are user-facing text from the simulator
            // ("Arriving...", blacklisted-region notices, etc.).
            Console.WriteLine($"[teleport] {e.Status}: {e.Message}");
            if (e.Status is TeleportStatus.Complete or TeleportStatus.Failed)
            {
                _teleportOk = e.Status == TeleportStatus.Complete;
                _teleportDone.Set();
            }
        };

        var loginParams = Client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!Client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + Client.Network.LoginMessage);
            return;
        }

        // --- Teleport to a named region at coordinates ---
        // Region name resolution goes through the grid's region lookup;
        // coordinates are region-local metres, z is height.
        Console.WriteLine("[teleport] requesting teleport to 'Sandbox' (128,128,25)...");
        Client.Self.RequestTeleport("Sandbox", new Vector3(128, 128, 25));
        if (_teleportDone.Wait(TimeSpan.FromSeconds(60)) && _teleportOk)
        {
            Console.WriteLine($"[teleport] arrived: {Client.Network.CurrentSim.Name} " +
                              $"at {Client.Self.SimPosition}");
            // POST-TELEPORT OBLIGATIONS (the part tutorials skip):
            // 1. All local object IDs changed: clear radars/trackers.
            // 2. Group chat sessions are dead: rejoin if needed.
            // 3. Cap URLs changed: never reuse a cap string captured
            //    before the teleport — always re-read from the client.
            // 4. The neighbour set changed: expect a burst of object
            //    updates for the new region and its neighbours.
        }
        else
        {
            Console.WriteLine("[teleport] failed or timed out — read the progress " +
                              "messages above for the simulator's reason (region " +
                              "offline, access denied, and agent-not-ready all " +
                              "present differently there).");
        }

        WearFirstShirt();
        Client.Network.Logout();
    }

    private static void WearFirstShirt()
    {
        // Appearance at manager level: AppearanceManager maintains the
        // wearable set; inventory items of wearable type can be worn by
        // item reference, and the manager performs the COF link updates
        // and appearance send. Doing this by hand = AIS3 link calls +
        // AgentSetAppearance-era plumbing; do not.
        var inv = Client.Inventory;
        var root = inv.RootFolder;
        Client.Inventory.FetchFolderContents(root.UUID, Client.Self.AgentID,
            true, true, InventorySortOrder.ByDate).Wait(TimeSpan.FromSeconds(30));

        var shirt = FindWearable(root, WearableType.Shirt);
        if (shirt == null)
        {
            Console.WriteLine("[appearance] no shirt found in the root walk " +
                              "(search the Clothing folder in a real tool).");
            return;
        }
        Console.WriteLine($"[appearance] wearing '{shirt.Name}' ({shirt.UUID})");
        // WearItem in the manager API: adds/replaces the wearable of that
        // type and updates the COF. The bake that follows is server-side;
        // other clients see the change when the simulator broadcasts the
        // updated appearance, not when this call returns.
        Client.Appearance.AddToOutfit(shirt, true);
    }

    private static InventoryItem? FindWearable(InventoryFolder folder, WearableType type)
    {
        foreach (var node in folder)
        {
            if (node is InventoryItem item
                && item.InventoryType == InventoryType.Wearable
                && item.WearableType == type)
            {
                return item;
            }
        }
        return null;
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

---

## Program 9 — Prim inspector and mesh export (Objects + ModelFormats)

What it demonstrates: selecting an object by raycast-free means (nearest prim to a point, as a tool would after a radar selection in program 4), requesting full object properties, decoding prim parameters into a human report (shape, materials, physics shape type), and exporting a mesh asset to glTF/OBJ via `LibreMetaverse.ModelFormats` for external tooling — the headless asset-inspection workflow GalaxyViewer-style and bot tooling builds on.

```csharp
// Program9_PrimInspector.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program9
{
    private static GridClient Client = null!;
    private static readonly ManualResetEventSlim _propsReady = new(false);
    private static ObjectProperties? _props;

    private static void Main(string[] args)
    {
        if (args.Length < 1 || !uint.TryParse(args[0], out var localId))
        {
            Console.WriteLine("Usage: PrimInspector <local-id-from-radar>");
            return;
        }
        Client = new GridClient();
        Client.Settings.ALWAYS_DECODE_OBJECTS = true;
        Client.Objects.ObjectProperties += (_, e) =>
        {
            _props = e.Properties;
            _propsReady.Set();
        };

        var loginParams = Client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!Client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + Client.Network.LoginMessage);
            return;
        }

        var sim = Client.Network.CurrentSim;
        if (!sim.ObjectsPrimitives.TryGetValue(localId, out var prim))
        {
            Console.WriteLine($"No prim with local ID {localId} in the local store. " +
                              "Wait for updates, or check the ID came from THIS region/session.");
            Client.Network.Logout();
            return;
        }

        PrintPrimReport(prim);

        // Names/descriptions/owner arrive via ObjectProperties.
        Client.Objects.RequestObjectProperties(sim, new List<uint> { localId });
        if (_propsReady.Wait(TimeSpan.FromSeconds(15)) && _props != null)
        {
            Console.WriteLine($"Name:        {_props.Name}");
            Console.WriteLine($"Description: {_props.Description}");
            Console.WriteLine($"Owner:       {_props.OwnerID}");
            Console.WriteLine($"Creator:     {_props.CreatorID}");
            Console.WriteLine($"Permissions: base={_props.Permissions.BaseMask} " +
                              $"next={_props.Permissions.NextOwnerMask}");
            Console.WriteLine($"Sale:        type={_props.SaleType} price={_props.SalePrice}");
        }
        else
        {
            Console.WriteLine("(ObjectProperties did not arrive — the object may " +
                              "have left the region, or the request was throttled.)");
        }

        Client.Network.Logout();
    }

    private static void PrintPrimReport(Primitive prim)
    {
        Console.WriteLine($"Local ID:  {prim.LocalID}");
        Console.WriteLine($"UUID:      {prim.ID}");
        Console.WriteLine($"Parent:    {prim.ParentID} (0 = scene root)");
        Console.WriteLine($"Position:  {prim.Position}  Rotation: {prim.Rotation}");
        Console.WriteLine($"Scale:     {prim.Scale}");
        Console.WriteLine($"PCode:     {prim.PrimData.PCode}");
        Console.WriteLine($"Material:  {prim.PrimData.Material}");
        Console.WriteLine($"PathCurve: {prim.PrimData.PathCurve}  " +
                          $"ProfileCurve: {prim.PrimData.ProfileCurve}");
        Console.WriteLine($"Physics shape type: {prim.Flags} / {prim.PrimData.Flags}");
        Console.WriteLine($"Faces:     {prim.Faces?.Length ?? 0} " +
                          $"(texture entries are per-face; a null face entry " +
                          "inherits the default texture entry)");
        if (prim.PrimData.SculptID != UUID.Zero)
        {
            Console.WriteLine($"Sculpt:    texture={prim.PrimData.SculptID} " +
                              $"type={prim.PrimData.SculptType} " +
                              "(sculpties are texture-encoded geometry: the mesher " +
                              "needs the texture asset before this prim can render)");
        }
        if ((prim.Flags & PrimFlags.Joint) != 0 || prim.Type == PrimType.Mesh)
        {
            Console.WriteLine("Mesh prim: geometry lives in the mesh asset " +
                              "(Assets + ModelFormats export it; the prim itself " +
                              "carries only the asset reference and parameters).");
        }
        var te = prim.Textures;
        if (te?.DefaultTexture != null)
        {
            Console.WriteLine($"Default texture: {te.DefaultTexture.TextureID} " +
                              $"rgba={te.DefaultTexture.RGBA}");
        }
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Mesh export note: given a mesh *asset* UUID (from an inventory item or a prim's sculpt/mesh reference), the flow is `Assets.RequestAsset` (program 5's pattern) → parse with the ModelFormats/MeshFoundry layer → write glTF or OBJ. The export is a *tooling* representation: glTF is not the wire format, normals/weights survive the trip, and SL-specific data (physics shapes, LOD chain, material asset references) needs the LLMesh-level parse if it must survive too. State which fidelity you are exporting at in the tool's output, or users will file "the export lost my physics" bugs against a format limitation.

---

## Program 10 — Friends, map, and parcels

What it demonstrates: the Friends manager (online notifications, rights model — who can see you online, locate you, modify your objects), region lookup by name through the map service, and parcel queries (the parcel the agent stands on, its owner, and access flags). These three managers share one lesson: most of their data is *event-delivered replies to requests*, and the rights/flags are bitfields whose semantics live in the viewer's headers — print them symbolically, never as raw numbers, in user-facing output.

```csharp
// Program10_FriendsMapParcels.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program10
{
    private static GridClient Client = null!;

    private static void Main()
    {
        Client = new GridClient();
        Client.Friends.FriendOnline += (_, e) =>
            Console.WriteLine($"[friend] {NameOf(e.AgentID)} came online.");
        Client.Friends.FriendOffline += (_, e) =>
            Console.WriteLine($"[friend] {NameOf(e.AgentID)} went offline.");
        Client.Friends.FriendRightsChanged += (_, e) =>
            Console.WriteLine($"[friend] rights changed for {NameOf(e.AgentID)}: {e.Rights}");

        var loginParams = Client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!Client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + Client.Network.LoginMessage);
            return;
        }

        // The friends list arrives with login (buddy list); the manager's
        // dictionary is keyed by agent UUID.
        Console.WriteLine($"Friends ({Client.Friends.FriendList.Count}):");
        foreach (var friend in Client.Friends.FriendList.Values)
        {
            Console.WriteLine($"  {friend.Name}  online={friend.IsOnline}  " +
                              $"canSeeMeOnline={friend.CanSeeMeOnline} " +
                              $"canLocate={friend.CanSeeMeOnMap} " +
                              $"canModifyMyObjects={friend.CanModifyMyObjects}  " +
                              $"iCanLocate={friend.CanSeeTheirLocation}"); // (rights surface per manager API)
        }

        // --- Map: region handle from a name ---
        // Region names resolve through the MapNameRequest / MapBlock path;
        // the manager exposes region lookup used before teleports and for
        // 'where is X' tools. Handles encode (x, y) grid coordinates in
        // metres in the high bits — do not do this math by hand in app
        // code; ask the manager/types layer for RegionX/RegionY.
        Client.Network.CurrentSim.ParcelManager.SelfParcel += (_, _) => { };
        var sim = Client.Network.CurrentSim;
        Console.WriteLine($"\nCurrent region: {sim.Name} handle={sim.Handle} " +
                          $"access={sim.Access} flags={sim.Flags}");

        // --- Parcels: the parcel under the agent ---
        // Parcel data is requested per region; the local parcel reply gives
        // the parcel containing a position. Parcel flags decide what a bot
        // may do here (rez, run scripts, voice, damage) — check before
        // acting, because 'works at home, fails at the venue' is usually a
        // parcel flag, not a code bug.
        sim.Parcels.RequestLocalParcel(Client.Self.SimPosition);
        Thread.Sleep(2000); // teaching seam: await the parcel event in real code
        if (sim.Parcels.TryGetValue(sim.Parcels.LocalID, out var parcel))
        {
            Console.WriteLine($"\nParcel: '{parcel.Name}' owner={parcel.OwnerID}");
            Console.WriteLine($"  Desc: {parcel.Desc}");
            Console.WriteLine($"  Flags: {parcel.Flags}");
            Console.WriteLine($"  Area: {parcel.Area} m^2  ClaimDate: {parcel.ClaimDate}");
            Console.WriteLine($"  AllowRez={parcel.Flags.HasFlag(ParcelFlags.CreateObjects)} " +
                              $"AllowScripts={!parcel.Flags.HasFlag(ParcelFlags.BlockScriptRun)} " +
                              $"PublicAccess={parcel.Access == ParcelAccess.Public}");
        }

        Client.Network.Logout();
    }

    private static string NameOf(UUID agentId)
    {
        // Name resolution is itself a service (UUID -> display/legacy name,
        // via GetDisplayNames cap / avatar properties). The Friends and
        // Avatars managers cache names as they arrive; a name tool should
        // request-and-wait rather than print UUIDs at users.
        return Client.Friends.FriendList.TryGetValue(agentId, out var f)
            ? f.Name
            : agentId.ToString();
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Rights-model warning, because it is a privacy surface and not just data: friend rights are reciprocal-looking but independently granted. "Can locate me on the map" and "can modify my objects" are powerful grants; a tool that displays or changes them must show *both* directions (what they can do to you, what you can do to them) and must never widen a right as a side effect of an unrelated operation.

---

## Program 11 — LLSD/OSD by hand, and a raw cap call

`GridClient` covers most needs, but AIS3-shaped work, SimulatorFeatures inspection, and any cap the managers have not wrapped require speaking LLSD directly. LibreMetaverse's StructuredData model is `OSD` / `OSDMap` / `OSDArray` with typed accessors, plus serialisers for XML/binary/notation/JSON. This program: builds an LLSD request map, reads `SimulatorFeatures` from the current region's cap set through the client's cap machinery, and prints the feature map — the same feature map the protocol skill says to *query instead of hardcoding* (mesh upload rules, PBR support, voice type).

```csharp
// Program11_LlsdAndCaps.cs
using LibreMetaverse;
using LibreMetaverse.StructuredData;
using LibreMetaverse.Types;

internal static class Program11
{
    private static async Task Main()
    {
        var client = new GridClient();
        var loginParams = client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + client.Network.LoginMessage);
            return;
        }

        var sim = client.Network.CurrentSim;

        // --- Build and round-trip an LLSD value by hand ---
        var request = new OSDMap
        {
            ["agent_id"] = OSD.FromUUID(client.Self.AgentID),
            ["folder_id"] = OSD.FromUUID(client.Inventory.RootFolder.UUID),
            ["sort_order"] = OSD.FromInteger(0),
            ["fetch_folders"] = OSD.FromBoolean(true),
            ["fetch_items"] = OSD.FromBoolean(true),
        };
        var xml = OSDParser.SerializeLLSDXmlString(request);
        Console.WriteLine("Sample LLSD (XML form):");
        Console.WriteLine(xml);
        var parsedBack = (OSDMap)OSDParser.DeserializeLLSDXml(xml);
        Console.WriteLine($"Round-trip keys: {string.Join(", ", parsedBack.Keys)}");
        // Notation form is what you want in logs: compact and diffable.
        Console.WriteLine("Notation: " + OSDParser.SerializeLLSDNotationString(request));

        // --- SimulatorFeatures via the region's cap URL ---
        // The client's Caps layer tracks the current region's cap map;
        // GetSimulatorFeatures-style helpers exist in the network/caps
        // surface in 3.x. The pattern below (cap URL from the sim, POST
        // an empty LLSD map, parse the OSDMap reply) is the shape every
        // raw cap call in this stack takes.
        var featuresUrl = sim.Caps?.CapabilityURI("SimulatorFeatures");
        if (featuresUrl == null)
        {
            Console.WriteLine("SimulatorFeatures cap not granted in this region.");
        }
        else
        {
            using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(30) };
            var body = OSDParser.SerializeLLSDXmlString(new OSDMap());
            using var content = new StringContent(body, System.Text.Encoding.UTF8,
                "application/llsd+xml");
            // NOTE: production code should reuse the client's authenticated
            // HTTP path/cap plumbing rather than a bare HttpClient; the
            // bare call is shown to make the wire shape visible. Cap URLs
            // are session credentials — never log featuresUrl.
            var response = await http.PostAsync(featuresUrl, content);
            var replyText = await response.Content.ReadAsStringAsync();
            var features = (OSDMap)OSDParser.DeserializeLLSDXml(replyText);
            Console.WriteLine("\nSimulatorFeatures:");
            foreach (var (key, value) in features)
            {
                Console.WriteLine($"  {key} = {value.AsString()}");
            }
            Console.WriteLine("\nRead these before assuming: mesh upload limits, " +
                              "physics shape support, PBR/material features, and the " +
                              "voice provider for this region all live in this map.");
        }

        client.Network.Logout();
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

---

## Program 12 — Below GridClient: a packet-level watcher with Protocol + Transport

Sometimes the manager layer is the problem (a new simulator message, a debugging proxy, a protocol test). The 3.x split lets you drop to `LibreMetaverse.Protocol` (generated packet classes) and `.Transport` (the circuit) without dragging the whole client in. This watcher connects a bare circuit after a manager-assisted login (the pragmatic hybrid: login is fiddly, watching is not), counts messages by name, and decodes `ChatFromSimulator` by hand — the same exercise the Python and Java files in this repo do in their stacks, so the three can be byte-diffed against each other on one OpenSim capture.

```csharp
// Program12_PacketWatcher.cs
using System.Collections.Concurrent;
using LibreMetaverse;
using LibreMetaverse.Packets;   // generated packet classes (Protocol package)
using LibreMetaverse.Types;

internal static class Program12
{
    private static readonly ConcurrentDictionary<string, int> _counts = new();

    private static void Main()
    {
        // Hybrid bootstrap: use GridClient only to log in and obtain the
        // session coordinates, then observe the raw stream through the
        // network layer's packet events. (A fully bare Transport circuit
        // is also possible; it re-implements login, which program 1
        // already showed is the part not worth re-implementing.)
        var client = new GridClient();
        client.Network.RegisterCallback(PacketType.ChatFromSimulator, OnChatPacket);
        client.Network.RegisterCallback(PacketType.ObjectUpdate, OnAnyPacket);
        client.Network.RegisterCallback(PacketType.ImprovedTerseObjectUpdate, OnAnyPacket);
        client.Network.RegisterCallback(PacketType.KillObject, OnAnyPacket);

        var loginParams = client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + client.Network.LoginMessage);
            return;
        }
        Console.WriteLine("[watcher] counting packets for 30 s...");
        Thread.Sleep(TimeSpan.FromSeconds(30));
        foreach (var (name, count) in _counts.OrderByDescending(kv => kv.Value))
        {
            Console.WriteLine($"  {name}: {count}");
        }
        client.Network.Logout();
    }

    private static void OnAnyPacket(Packet packet, Simulator simulator)
    {
        _counts.AddOrUpdate(packet.Type.ToString(), 1, (_, n) => n + 1);
    }

    private static void OnChatPacket(Packet packet, Simulator simulator)
    {
        _counts.AddOrUpdate(nameof(PacketType.ChatFromSimulator), 1, (_, n) => n + 1);
        var chat = (ChatFromSimulatorPacket)packet;
        var from = Utils.BytesToString(chat.ChatData.FromName);
        var message = Utils.BytesToString(chat.ChatData.Message);
        Console.WriteLine($"[chat/raw] {from}: {message}");
        // Compare this decode with Self.Chat's ChatEventArgs for the same
        // line: same message, two altitudes. If they ever disagree, the
        // packet class (generated from the template) is the one to trust
        // after checking the template revision — managers add policy
        // (filtering, source typing) on top of the wire truth.
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

Voice note for the C# stack: LibreMetaverse ships both `.Voice.WebRTC` and `.Voice.Vivox` packages. They are alternatives chosen by region features (program 11's map), not layers — initialise exactly one, from the features of the region you are in, and re-evaluate on teleport. A client that hardcodes Vivox provisioning (`ProvisionVoiceAccountRequest`) will have no voice in WebRTC-only regions, and one that hardcodes WebRTC cannot speak on Vivox-configured OpenSim grids; the features map exists precisely so this is a runtime branch, not a build flag.

---

## Program 13 — Asset upload and OAR archiving

What it demonstrates: uploading a new texture asset through the manager's asset upload path (which uses the inventory upload caps and returns the new asset + item), and reading an OpenSim OAR archive with `LibreMetaverse.Archiving` to list its assets and objects — the two ends of the content lifecycle (getting things in, getting whole regions out).

Upload rules first, because they are economic and legal, not just technical: uploads on Agni cost Linden dollars per asset, test uploads belong on Aditi or a local OpenSim; uploading an asset grants it the permissions you set at creation, and next-owner permissions are the ones your buyers live with; and an upload call returning a UUID is not success until the asset is retrievable — verify by fetching it back (program 5's path) in any tool whose output other people will depend on.

```csharp
// Program13_UploadAndArchive.cs
using LibreMetaverse;
using LibreMetaverse.Archiving;
using LibreMetaverse.Types;

internal static class Program13
{
    private static void Main(string[] args)
    {
        if (args.Length >= 1 && args[0].EndsWith(".oar", StringComparison.OrdinalIgnoreCase))
        {
            ListOar(args[0]);
            return;
        }
        UploadTexture(args.Length >= 1 ? args[0] : "sample.j2c");
    }

    // ---- OAR reading (no login required) ----
    private static void ListOar(string path)
    {
        // An OAR is a tar of XML object files + asset files + a control
        // file. The Archiving package parses it without a grid connection,
        // which makes it the right tool for backup verification: if your
        // nightly OAR cannot be listed by this program, it cannot be
        // restored either, and finding that out tonight beats finding it
        // out during an incident.
        var archive = OarFile.Load(path); // (Archiving package surface)
        Console.WriteLine($"OAR: {path}");
        Console.WriteLine($"  Assets:  {archive.Assets.Count}");
        Console.WriteLine($"  Objects: {archive.Objects.Count}");
        foreach (var (uuid, asset) in archive.Assets.Take(10))
        {
            Console.WriteLine($"    asset {uuid} type={asset.AssetType} bytes={asset.AssetData.Length}");
        }
        if (archive.Assets.Count > 10) Console.WriteLine("    ... (truncated)");
        foreach (var obj in archive.Objects.Take(10))
        {
            Console.WriteLine($"    object {obj.RootPart.Name} at {obj.RootPart.GroupPosition} " +
                              $"parts={obj.Parts.Count}");
        }
    }

    // ---- Texture upload (login required) ----
    private static void UploadTexture(string j2cPath)
    {
        if (!File.Exists(j2cPath))
        {
            Console.WriteLine($"No such file: {j2cPath} (expected a JPEG2000 codestream).");
            return;
        }
        var client = new GridClient();
        var loginParams = client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + client.Network.LoginMessage);
            return;
        }

        var data = File.ReadAllBytes(j2cPath);
        var name = Path.GetFileNameWithoutExtension(j2cPath);
        var done = new ManualResetEventSlim(false);
        UUID newItem = UUID.Zero, newAsset = UUID.Zero;
        bool ok = false;

        // UploadNewAsset in the Assets/Inventory surface: creates the
        // asset via the upload cap and a matching inventory item in the
        // Textures folder. The callback reports both UUIDs — record both;
        // support questions will ask for the item, debugging for the asset.
        client.Inventory.RequestCreateItemFromAsset(data, name,
            "Uploaded by Program13", AssetType.Texture, InventoryType.Texture,
            client.Inventory.FindFolderForType(AssetType.Texture),
            Permissions.FullPermissions, // tighten for anything you will sell/give
            (_, success, itemId, assetId) =>
            {
                ok = success; newItem = itemId; newAsset = assetId;
                done.Set();
            });

        if (!done.Wait(TimeSpan.FromSeconds(60)))
        {
            Console.WriteLine("[upload] timed out — check SimulatorFeatures for " +
                              "upload support and the account's L$ balance on Agni.");
        }
        else
        {
            Console.WriteLine($"[upload] success={ok} item={newItem} asset={newAsset}");
            Console.WriteLine("[upload] verify: fetch the asset back (Program5) " +
                              "before telling anyone it worked.");
        }
        client.Network.Logout();
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

---

## Program 14 — A TestClient-style command framework (putting it together)

LibreMetaverse's own TestClient is a shell: log in one or more bots, type commands (`say`, `im`, `follow`, `teleport`, `logout`), and each command is a small class dispatched by name. The framework below is that shape, miniaturised, with the programs above as its command implementations' source material. It exists in this file because most real tools in this stack grow into exactly this: a REPL around a session.

```csharp
// Program14_CommandShell.cs
using LibreMetaverse;
using LibreMetaverse.Types;

internal static class Program14
{
    private interface IBotCommand
    {
        string Name { get; }
        string Help { get; }
        void Run(GridClient client, string[] args);
    }

    private sealed class SayCommand : IBotCommand
    {
        public string Name => "say";
        public string Help => "say <text> — speak in nearby chat";
        public void Run(GridClient client, string[] args) =>
            client.Self.Chat(string.Join(' ', args), 0, ChatType.Normal);
    }

    private sealed class ImCommand : IBotCommand
    {
        public string Name => "im";
        public string Help => "im <firstname> <lastname> <text> — IM a resident by name";
        public void Run(GridClient client, string[] args)
        {
            if (args.Length < 3)
            {
                Console.WriteLine("Usage: " + Help);
                return;
            }
            var fullName = args[0] + " " + args[1];
            var text = string.Join(' ', args.Skip(2));
            // Name -> UUID is an async lookup (directory/avatar services).
            // The manager's name cache + request pattern is the honest way;
            // this command uses the directory request seam and reports
            // instead of pretending the lookup is synchronous.
            Console.WriteLine($"[im] resolving {fullName} via directory, then sending.");
            client.Directory.StartPeopleSearch(fullName, 0);
            Console.WriteLine("[im] (wire the DirectoryPeopleReply event to the " +
                              "Self.InstantMessage call in the full shell — see " +
                              "Program2 for the send half and its session rules.)");
            _ = text;
        }
    }

    private sealed class FollowCommand : IBotCommand
    {
        public string Name => "follow";
        public string Help => "follow <firstname> <lastname> | follow stop";
        public static UUID Target = UUID.Zero;
        public static bool Active;

        public void Run(GridClient client, string[] args)
        {
            if (args.Length == 1 && args[0] == "stop")
            {
                Active = false;
                client.Self.AutoPilotCancel();
                Console.WriteLine("[follow] stopped.");
                return;
            }
            Console.WriteLine("[follow] resolve the target from the radar " +
                              "(Program4) and set FollowCommand.Target; the " +
                              "autopilot tick below does the walking.");
            Active = true;
        }

        // Called from the shell's 500 ms tick while Active: steer toward
        // the target avatar's last known position with the client's
        // autopilot (which handles local steering; it is not pathfinding —
        // walls, parcels, and ban lines all still apply, and a follow bot
        // that cannot say why it stopped is a bug report waiting to happen).
        public static void Tick(GridClient client)
        {
            if (!Active || Target == UUID.Zero) return;
            if (client.Network.CurrentSim.ObjectsAvatars
                    .TryGetValue(Target, out var avatar))
            {
                var pos = avatar.Position;
                if (Vector3.Distance(client.Self.SimPosition, pos) > 2.5f)
                {
                    client.Self.AutoPilot(pos.X, pos.Y, pos.Z);
                }
                else
                {
                    client.Self.AutoPilotCancel();
                }
            }
        }
    }

    private sealed class WhereCommand : IBotCommand
    {
        public string Name => "where";
        public string Help => "where — current region and position";
        public void Run(GridClient client, string[] args) =>
            Console.WriteLine($"[where] {client.Network.CurrentSim?.Name} " +
                              $"local {client.Self.SimPosition} " +
                              $"global {client.Self.GlobalPosition}");
    }

    private static void Main()
    {
        var client = new GridClient();
        var commands = new IBotCommand[]
            { new SayCommand(), new ImCommand(), new FollowCommand(), new WhereCommand() }
            .ToDictionary(c => c.Name, StringComparer.OrdinalIgnoreCase);

        var loginParams = client.Network.DefaultLoginParams(
            Env("SL_FIRST"), Env("SL_LAST"), Env("SL_PASSWORD"));
        loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                          ?? GridClient.DEFAULT_LOGIN_URI;
        if (!client.Network.Login(loginParams))
        {
            Console.WriteLine("Login failed: " + client.Network.LoginMessage);
            return;
        }
        Console.WriteLine("Commands: " + string.Join(", ", commands.Keys) + ", help, quit");

        // Follow tick on a timer, not in the input loop: input blocks,
        // avatars do not.
        using var tick = new Timer(_ => FollowCommand.Tick(client), null,
            500, 500);

        string? line;
        while ((line = Console.ReadLine()) != null)
        {
            var parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            if (parts.Length == 0) continue;
            var cmd = parts[0].ToLowerInvariant();
            if (cmd == "quit") break;
            if (cmd == "help")
            {
                foreach (var c in commands.Values) Console.WriteLine("  " + c.Help);
                continue;
            }
            if (commands.TryGetValue(cmd, out var command))
            {
                command.Run(client, parts.Skip(1).ToArray());
            }
            else
            {
                Console.WriteLine($"Unknown command '{cmd}'. Try 'help'.");
            }
        }
        client.Network.Logout();
    }

    private static string Env(string name) =>
        Environment.GetEnvironmentVariable(name)
        ?? throw new InvalidOperationException($"Set {name}");
}
```

## Appendix — C# stack troubleshooting, by symptom

- **Login succeeds, nothing else happens.** The session is waiting on region handshake completion and the Event Queue. Check that the process stays alive (a `Main` that returns logs you out by process death), that no firewall eats the UDP return path, and that you did not create the `GridClient` with object tracking and inventory settings that discard what you are waiting for.
- **`ObjectUpdate` events but empty names everywhere.** Names are properties, not updates — see program 4's request pattern. Also check `ALWAYS_DECODE_OBJECTS` and that you are filtering on the right simulator.
- **Inventory calls hang.** Contents are fetched per folder over caps; a hang is usually a cap the region did not grant (OpenSim subsets) or a fetch issued before the skeleton finished arriving. Log granted caps at login (names only, never URLs).
- **Group chat sends go nowhere.** You skipped the session. See program 6: request session, confirm start, send with the session ID and session dialog.
- **Works on OpenSim, fails on Aditi/Agni.** Cap subsets, AIS coverage, throttle strictness, and SimulatorFeatures all differ. Record the grid in every bug report and test the Aditi leg before calling code done — that sentence appears in every file in this repo because it keeps being true.
- **A name in these programs disagrees with your referenced build.** Trust the generated API catalogue for your exact version, then the library's own examples (`Programs/examples` in the repo: TestClient, SimpleBot, InventoryExplorer, PrimInspector — the ancestors of programs 3, 4, 9, and 14 above), then this file, in that order.

---

## Program 15 — The 60-line SimpleBot, and GridClient configuration that matters

The minimal ancestor of everything above (LibreMetaverse's own SimpleBot is this shape). It is included last, not first, because reading it *after* the full programs shows how much session machinery the three manager calls hide — and why "my bot logs in but is invisible / cannot move / hears nothing" is always one of the hidden pieces (handshake, AgentUpdate, Event Queue) not starting.

```csharp
// Program15_SimpleBot.cs — the minimal in-world bot.
using LibreMetaverse;

var client = new GridClient();
client.Self.Chat += (_, e) =>
    Console.WriteLine($"[chat] {e.FromName}: {e.Message}");

var loginParams = client.Network.DefaultLoginParams(
    Environment.GetEnvironmentVariable("SL_FIRST")!,
    Environment.GetEnvironmentVariable("SL_LAST")!,
    Environment.GetEnvironmentVariable("SL_PASSWORD")!);
loginParams.URI = Environment.GetEnvironmentVariable("SL_LOGIN_URI")
                  ?? GridClient.DEFAULT_LOGIN_URI;

if (!client.Network.Login(loginParams))
{
    Console.WriteLine("Login failed: " + client.Network.LoginMessage);
    return;
}
Console.WriteLine($"In-world as {client.Self.Name} in {client.Network.CurrentSim.Name}.");
client.Self.Chat("Hello from LibreMetaverse.", 0, LibreMetaverse.ChatType.Normal);
Console.ReadLine();          // staying alive IS the session loop at this scale
client.Network.Logout();     // clean logout, not process death
```

### GridClient settings worth knowing before you need them

These are the `Client.Settings` switches the programs above rely on or that bite in production. Names follow the library's settings surface; verify against your build's catalogue.

- `ALWAYS_DECODE_OBJECTS` / `ALWAYS_REQUEST_OBJECTS` — object store completeness for radars and inspectors (programs 4, 9). On by need, off by default for lean chat bots: decoding every object in a busy region is real CPU.
- `SEND_AGENT_UPDATES` — the continuous AgentUpdate stream. A client that disables it to "save bandwidth" will be timed out by the simulator; a client that leaves it on while parked is normal and expected.
- `THROTTLE_*` family (resend/texture/asset/task rates) — the client-side view of the AgentThrottle buckets. Raise texture/asset for download tools (program 5) on good links; never raise resend to compensate for a lossy link — resends are the compensation.
- `LOGIN_TIMEOUT` / circuit timeouts — login against a busy grid and region crossings both legitimately take longer than LAN-shaped defaults assume. Timeout errors that vanish on retry are usually this, not credentials.
- `USE_LLSD_LOGIN`, `LOG_LEVEL`, store/inventory cache paths — protocol variant selection, diagnostics, and the on-disk inventory cache. The disk cache is a correctness feature (fast relogins) and a staleness hazard (it must be keyed by agent + grid; a cache shared across grids is a bug farm).
- Multiple simulators / child agents: the client maintains connections to neighbour regions for visibility. Settings that cap simulator count change what a radar can see at region borders — document the value in any mapping tool's output.

### Concurrency rules for event-driven bots

1. **Handlers are called on network threads.** A handler that blocks (disk, HTTP, `Thread.Sleep`, a lock held by UI code) stalls every later packet, including ACKs — the simulator responds with resends, which makes the stall worse. Queue work off the handler; the handler's job is to copy data and enqueue.
2. **Manager stores are the shared state.** Read them from any thread the way the library's own examples do; write only through manager calls. Your own side tables (program 4's radar) need your own lock — the one in program 4 is deliberate.
3. **One client per bot, one process per fleet is fine.** TestClient-style fleets (program 14 × N) work because each `GridClient` is independent; the failure mode to avoid is sharing *your* singletons (reply-cooldown maps, radar tables) across bots without keying them by bot.
4. **Logout is a protocol act.** `Network.Logout()` sends the logout message and closes cleanly. Killing the process ghosts the avatar until the simulator times the circuit out — on a busy parcel, that ghost is visible to everyone and occupies the agent slot your reconnect wants.

### Choosing your altitude — a closing decision table in prose

Use `GridClient` managers (programs 1–11, 13–15) by default: they encode two decades of protocol edge cases. Drop to generated packets on the client's network events (program 12) when you need a message the managers do not surface, or when debugging a manager-versus-wire disagreement. Drop to a bare Transport circuit (the Python/Java/C++ files' exercise, possible in C# via the split packages) only for proxies, protocol tests, and teaching — and expect to re-own login, handshake, AgentUpdate, throttling, and the Event Queue, because at that altitude all of them are yours. Every experienced team in this ecosystem has made that trade exactly once per project, on purpose, with the cost written down. Make yours on purpose too.

---

## Program 16 — Environment (EEP) and parcel media, briefly

Two smaller manager surfaces that complete the tour. EEP environments are inventory assets applied at parcel/region level via the `ExtEnvironment`/`EnvironmentSettings` caps; a bot cannot *render* sky, but tools that audit parcels, photograph regions (with a graphical sibling client), or manage estates need to read and set them. Parcel media (the parcel's media texture and URL) is the other classic estate-tool surface.

```csharp
// Program16_Environment.cs (fragment — same login boilerplate as Program10)
using LibreMetaverse;
using LibreMetaverse.StructuredData;
using LibreMetaverse.Types;

// After login, with `client` and the current sim as in Program10:
// 1) Read the parcel's environment: the caps layer exposes the region's
//    environment endpoints; the reply is an LLSD environment map (sky and
//    water settings as nested OSDMaps, day length/offset). Print the keys
//    and the day-cycle length rather than dumping shader parameters.
var sim = client.Network.CurrentSim;
var envUrl = sim.Caps?.CapabilityURI("ExtEnvironment");
if (envUrl != null)
{
    Console.WriteLine("[eep] ExtEnvironment cap present in this region.");
    Console.WriteLine("[eep] Environment assets are referenced by UUID from " +
                      "parcel/region data; setting one is an AIS/land-manager " +
                      "operation with estate/parcel rights checks — the same " +
                      "powers-first pattern as group notices (Program6).");
}
else
{
    Console.WriteLine("[eep] No ExtEnvironment cap: this grid/region predates " +
                      "EEP or does not grant it; Windlight-era data (region " +
                      "settings via legacy messages) is the fallback there.");
}

// 2) Parcel media summary for the local parcel (see Program10 for the
//    parcel fetch): media texture UUID + media URL host. Print the host,
//    not the full URL with any embedded tokens.
if (sim.Parcels.TryGetValue(sim.Parcels.LocalID, out var parcel))
{
    Console.WriteLine($"[media] texture={parcel.MediaID} " +
                      $"type={parcel.MediaType} size={parcel.MediaWidth}x{parcel.MediaHeight}");
    Console.WriteLine($"[media] desc-url present: {!string.IsNullOrEmpty(parcel.MediaURL)}");
    Console.WriteLine("[media] parcel media auto-scale and loop flags live on " +
                      "the same parcel record; a media tool that changes the URL " +
                      "without preserving them resets the parcel's TV to a " +
                      "black rectangle and generates exactly one angry IM.");
}
```

That completes the C# tour: session (1, 15), conversation (2), inventory (3), world state (4, 9, 10), assets (5, 13), groups (6), scripting tools (7), movement and appearance (8), raw LLSD and caps (11), raw packets (12), a shell (14), and environment/media (16) — the full surface a LibreMetaverse application is built from, each piece shown whole rather than as a fragment.
