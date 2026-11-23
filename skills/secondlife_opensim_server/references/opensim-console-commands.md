# OpenSim Console Commands Reference (generated from opensim/opensim source)

Extracted 36 console commands registered in the OpenSim source, with their registered help text and the file that registers them. Run them from the region console or the ROBUST console as noted by the registering module.


## alert

- Help: alert <message>

- Registered in: `OpenSim/Region/CoreModules/Avatar/Dialog/DialogModule.cs`


## alert-user

- Help: alert-user <first> <last> <message>

- Registered in: `OpenSim/Region/CoreModules/Avatar/Dialog/DialogModule.cs`


## appearance find

- Help: appearance find <uuid-or-start-of-uuid>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Appearance/AppearanceInfoModule.cs`


## appearance rebake

- Help: appearance rebake <first-name> <last-name>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Appearance/AppearanceInfoModule.cs`


## appearance send

- Help: appearance send [<first-name> <last-name>]

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Appearance/AppearanceInfoModule.cs`


## appearance show

- Help: appearance show [<first-name> <last-name>]

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Appearance/AppearanceInfoModule.cs`


## bypass permissions

- Help: bypass permissions <true / false>

- Registered in: `OpenSim/Region/CoreModules/World/Permissions/PermissionsModule.cs`


## clear image queues

- Help: clear image queues <first-name> <last-name>

- Registered in: `OpenSim/Region/OptionalModules/Agent/UDP/Linden/LindenUDPInfoModule.cs`


## debug attachments log

- Help: debug attachments log [0|1]

- Registered in: `OpenSim/Region/CoreModules/Avatar/Attachments/AttachmentsModule.cs`


## debug attachments status

- Help: debug attachments status

- Registered in: `OpenSim/Region/CoreModules/Avatar/Attachments/AttachmentsModule.cs`


## debug groups messaging verbose

- Help: debug groups messaging verbose <true|false>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/XmlRpcGroups/GroupsMessagingModule.cs`


## debug groups verbose

- Help: debug groups verbose <true|false>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/XmlRpcGroups/GroupsModule.cs`


## debug permissions

- Help: debug permissions <true / false>

- Registered in: `OpenSim/Region/CoreModules/World/Permissions/PermissionsModule.cs`


## debug scene get

- Help: debug scene get

- Registered in: `OpenSim/Region/OptionalModules/World/SceneCommands/SceneCommandsModule.cs`


## debug scene set

- Help: debug scene set <param> <value>

- Registered in: `OpenSim/Region/OptionalModules/World/SceneCommands/SceneCommandsModule.cs`


## export-map

- Help: export-map [<path>]

- Registered in: `OpenSim/Region/CoreModules/World/WorldMap/WorldMapModule.cs`


## force permissions

- Help: force permissions <true / false>

- Registered in: `OpenSim/Region/CoreModules/World/Permissions/PermissionsModule.cs`


## friends show

- Help: friends show [--cache] <first-name> <last-name>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Friends/FriendsCommandsModule.cs`


## generate map

- Help: generate map

- Registered in: `OpenSim/Region/CoreModules/World/WorldMap/WorldMapModule.cs`


## jsonstore stats

- Help: jsonstore stats

- Registered in: `OpenSim/Region/OptionalModules/Scripting/JsonStore/JsonStoreCommands.cs`


## load iar

- Help: load iar [-m|--merge] <first> <last> <inventory path> <password> [<IAR path>]

- Registered in: `OpenSim/Region/CoreModules/Avatar/Inventory/Archiver/InventoryArchiverModule.cs`


## monitor report

- Help: monitor report

- Registered in: `OpenSim/Region/CoreModules/Framework/Monitoring/MonitorModule.cs`


## save iar

- Help: save iar [-h|--home=<url>] [--noassets | --skipbadassets] <first> <last> <inventory path> <password> [<IAR path>] [-c|--creators] [-e|--exclude=<name/uuid>] [-f|--excludefolder=<foldername/uuid>] [-v|--verbose]

- Registered in: `OpenSim/Region/CoreModules/Avatar/Inventory/Archiver/InventoryArchiverModule.cs`


## show animations

- Help: show animations [<first-name> <last-name>]

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Animations/AnimationsCommandModule.cs`


## show appearance

- Help: show appearance [<first-name> <last-name>]

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Appearance/AppearanceInfoModule.cs`


## show image queues

- Help: show image queues <first-name> <last-name>

- Registered in: `OpenSim/Region/OptionalModules/Agent/UDP/Linden/LindenUDPInfoModule.cs`


## show pqueues

- Help: show pqueues [full]

- Registered in: `OpenSim/Region/OptionalModules/Agent/UDP/Linden/LindenUDPInfoModule.cs`


## show queues

- Help: show queues [full]

- Registered in: `OpenSim/Region/OptionalModules/Agent/UDP/Linden/LindenUDPInfoModule.cs`


## show throttles

- Help: show throttles [full]

- Registered in: `OpenSim/Region/OptionalModules/Agent/UDP/Linden/LindenUDPInfoModule.cs`


## sit user name

- Help: sit user name [--regex] <first-name> <last-name>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/SitStand/SitStandCommandsModule.cs`


## stand user name

- Help: stand user name [--regex] <first-name> <last-name>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/SitStand/SitStandCommandsModule.cs`


## terrain modify

- Help: terrain modify <operation> <value> [<area>] [<taper>]

- Registered in: `OpenSim/Region/CoreModules/World/Terrain/TerrainModule.cs`


## wearables check

- Help: wearables check <first-name> <last-name>

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Appearance/AppearanceInfoModule.cs`


## wearables show

- Help: wearables show [<first-name> <last-name>]

- Registered in: `OpenSim/Region/OptionalModules/Avatar/Appearance/AppearanceInfoModule.cs`


## wind

- Help: 

- Registered in: `OpenSim/Region/CoreModules/World/Wind/WindModule.cs`


## wind base wind_update_rate

- Help: wind base wind_update_rate [<value>]

- Registered in: `OpenSim/Region/CoreModules/World/Wind/WindModule.cs`
