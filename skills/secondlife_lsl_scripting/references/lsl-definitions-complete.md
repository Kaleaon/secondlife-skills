# LSL Definitions — Complete Canonical Data (from secondlife/lsl-definitions)

The complete structured content of `lsl_definitions.yaml` (MIT, Linden Lab), rendered as JSON per entry for exact lookup: every field upstream ships, including enums, controls, builder rulesets, and per-function fields that the curated references summarise. When a curated reference and this file disagree, this file is the upstream data and the curated file is wrong.


# Section: enums (133 entries)


## enums/AgentData

```json
{
 "type": "enum",
 "prefix": "DATA_",
 "tooltip": ""
}
```


## enums/AgentDataPaymentInfo

```json
{
 "type": "flag",
 "prefix": "PAYMENT_INFO_",
 "tooltip": ""
}
```


## enums/AgentInfo

```json
{
 "type": "flag",
 "prefix": "AGENT_",
 "tooltip": ""
}
```


## enums/AgentListParam

```json
{
 "type": "param-dict",
 "tooltip": "None defined yet"
}
```


## enums/AgentListScope

```json
{
 "type": "flag",
 "prefix": "AGENT_LIST_",
 "tooltip": ""
}
```


## enums/AgentRotFlags

```json
{
 "type": "flag",
 "tooltip": "None defined yet"
}
```


## enums/AlphaMode

```json
{
 "type": "enum",
 "prefix": "PRIM_ALPHA_MODE_",
 "tooltip": ""
}
```


## enums/AssetPermission

```json
{
 "type": "flag",
 "prefix": "PERM_",
 "special-members": [
  "PERM_ALL"
 ],
 "tooltip": ""
}
```


## enums/AssetPermissionCategory

```json
{
 "type": "enum",
 "prefix": "MASK_",
 "tooltip": ""
}
```


## enums/AssetPermissionCategoryFlag

```json
{
 "type": "flag",
 "prefix": "MASK_",
 "tooltip": ""
}
```


## enums/AssetPermissionCategoryOrFlag

```json
{
 "type": "enum+flag",
 "enum": "AssetPermissionCategory",
 "flag": "AssetPermissionCategoryFlag",
 "mask": "0x7",
 "prefix": "MASK_",
 "tooltip": ""
}
```


## enums/AttachPoint

```json
{
 "type": "enum",
 "prefix": "ATTACH_",
 "tooltip": ""
}
```


## enums/AttachedListFilterFlag

```json
{
 "type": "flag",
 "prefix": "FILTER_FLAG_",
 "tooltip": ""
}
```


## enums/AttachedListFilterParam

```json
{
 "type": "param-dict",
 "prefix": "FILTER_",
 "tooltip": ""
}
```


## enums/CameraParam

```json
{
 "type": "param-dict",
 "prefix": "CAMERA_",
 "tooltip": ""
}
```


## enums/ChangeType

```json
{
 "type": "flag",
 "prefix": "CHANGED_",
 "tooltip": ""
}
```


## enums/Channel

```json
{
 "type": "enum",
 "other-values": true,
 "tooltip": ""
}
```


## enums/ChannelNonPublic

```json
{
 "type": "enum",
 "other-values": true,
 "tooltip": ""
}
```


## enums/CharacterAvoidanceMode

```json
{
 "type": "enum",
 "prefix": "AVOID_",
 "tooltip": ""
}
```


## enums/CharacterCommand

```json
{
 "type": "enum",
 "prefix": "CHARACTER_CMD_",
 "tooltip": ""
}
```


## enums/CharacterEvadeParam

```json
{
 "type": "param-dict",
 "tooltip": "No options yet."
}
```


## enums/CharacterFleeFromParam

```json
{
 "type": "param-dict",
 "tooltip": "No options yet."
}
```


## enums/CharacterNavigateParam

```json
{
 "type": "param-dict",
 "tooltip": ""
}
```


## enums/CharacterOrientation

```json
{
 "type": "enum",
 "tooltip": ""
}
```


## enums/CharacterParam

```json
{
 "type": "param-dict",
 "prefix": "CHARACTER_",
 "tooltip": ""
}
```


## enums/CharacterPathUpdateType

```json
{
 "type": "enum",
 "prefix": "PU_",
 "tooltip": ""
}
```


## enums/CharacterPatrolPointsParam

```json
{
 "type": "param-dict",
 "prefix": "PATROL_",
 "tooltip": ""
}
```


## enums/CharacterPursueParam

```json
{
 "type": "param-dict",
 "prefix": "PURSUIT_",
 "tooltip": ""
}
```


## enums/CharacterTraversalType

```json
{
 "type": "enum",
 "prefix": "TRAVERSAL_TYPE_",
 "tooltip": ""
}
```


## enums/CharacterType

```json
{
 "type": "enum",
 "prefix": "CHARACTER_TYPE_",
 "tooltip": ""
}
```


## enums/CharacterWanderWithinParam

```json
{
 "type": "param-dict",
 "prefix": "WANDER_",
 "tooltip": ""
}
```


## enums/ClickAction

```json
{
 "type": "enum",
 "prefix": "CLICK_ACTION_",
 "special-members": [
  "CLICK_ACTION_TOUCH"
 ],
 "tooltip": ""
}
```


## enums/ControlButton

```json
{
 "type": "flag",
 "prefix": "CONTROL_",
 "tooltip": ""
}
```


## enums/DamageType

```json
{
 "type": "enum",
 "prefix": "DAMAGE_TYPE_",
 "other-values": true,
 "tooltip": ""
}
```


## enums/DerezMode

```json
{
 "type": "enum",
 "prefix": "DEREZ_",
 "tooltip": ""
}
```


## enums/DetectType

```json
{
 "type": "flag",
 "special-members": [
  "AGENT_BY_LEGACY_NAME"
 ],
 "tooltip": ""
}
```


## enums/EmailTarget

```json
{
 "type": "enum",
 "prefix": "TARGETED_EMAIL_",
 "tooltip": ""
}
```


## enums/EnvironmentError

```json
{
 "type": "enum",
 "prefix": "ENV_",
 "tooltip": ""
}
```


## enums/EnvironmentParam

```json
{
 "type": "param-list",
 "tooltip": ""
}
```


## enums/EnvironmentParamReadOnly

```json
{
 "type": "param-list",
 "tooltip": ""
}
```


## enums/EstateAccessParam

```json
{
 "type": "enum",
 "prefix": "ESTATE_ACCESS_",
 "tooltip": ""
}
```


## enums/ExperienceError

```json
{
 "type": "enum",
 "prefix": "XP_ERROR_",
 "tooltip": ""
}
```


## enums/Faces

```json
{
 "type": "enum",
 "other-values": true,
 "tooltip": "Operate on one or more face numbers at a time."
}
```


## enums/FindNotecardTextParam

```json
{
 "type": "param-dict",
 "tooltip": "No options yet."
}
```


## enums/GLTFAlphaMode

```json
{
 "type": "enum",
 "prefix": "PRIM_GLTF_ALPHA_MODE_",
 "tooltip": ""
}
```


## enums/GLTFOverride

```json
{
 "type": "param-dict",
 "prefix": "OVERRIDE_GLTF_",
 "tooltip": ""
}
```


## enums/GameControlAxis

```json
{
 "type": "enum",
 "prefix": "GAME_CONTROL_AXIS_",
 "tooltip": ""
}
```


## enums/GameControlButton

```json
{
 "type": "flag",
 "prefix": "GAME_CONTROL_BUTTON_",
 "tooltip": ""
}
```


## enums/GameControlMode

```json
{
 "type": "enum",
 "prefix": "GAME_CONTROL_MODE_",
 "tooltip": ""
}
```


## enums/GetClosestNavPointParam

```json
{
 "type": "param-dict",
 "prefix": "GCNP_",
 "tooltip": ""
}
```


## enums/GetStaticPathParam

```json
{
 "type": "param-dict",
 "tooltip": ""
}
```


## enums/GiveAgentInventoryFlag

```json
{
 "type": "flag",
 "prefix": "TRANSFER_",
 "tooltip": "No flags yet"
}
```


## enums/GiveAgentInventoryParam

```json
{
 "type": "param-dict",
 "prefix": "TRANSFER_",
 "tooltip": ""
}
```


## enums/GroundTextureParam

```json
{
 "type": "param-dict",
 "prefix": "TERRAIN_",
 "tooltip": ""
}
```


## enums/HTTPContentType

```json
{
 "type": "enum",
 "prefix": "CONTENT_TYPE_",
 "tooltip": ""
}
```


## enums/HTTPRequestParam

```json
{
 "type": "param-dict",
 "prefix": "HTTP_",
 "tooltip": ""
}
```


## enums/HTTPResponseError

```json
{
 "type": "param-dict",
 "prefix": "HTTP_",
 "tooltip": ""
}
```


## enums/InventoryType

```json
{
 "type": "enum",
 "prefix": "INVENTORY_",
 "special-members": [
  "INVENTORY_NONE"
 ],
 "tooltip": ""
}
```


## enums/KeyframedMotionCommand

```json
{
 "type": "enum",
 "prefix": "KFM_CMD_",
 "tooltip": ""
}
```


## enums/KeyframedMotionData

```json
{
 "type": "flag",
 "prefix": "KFM_",
 "tooltip": ""
}
```


## enums/KeyframedMotionMode

```json
{
 "type": "enum",
 "prefix": "KFM_",
 "tooltip": ""
}
```


## enums/KeyframedMotionParam

```json
{
 "type": "param-dict",
 "prefix": "KFM_",
 "tooltip": ""
}
```


## enums/Link

```json
{
 "type": "enum",
 "other-values": true,
 "prefix": "LINK_",
 "tooltip": "Operate on one link number at a time."
}
```


## enums/Links

```json
{
 "type": "enum",
 "other-values": true,
 "prefix": "LINK_",
 "tooltip": "Operate on one or more link numbers at a time."
}
```


## enums/LinksetDataAction

```json
{
 "type": "enum",
 "prefix": "LINKSETDATA_",
 "tooltip": ""
}
```


## enums/LinksetDataError

```json
{
 "type": "enum",
 "prefix": "LINKSETDATA_",
 "tooltip": ""
}
```


## enums/ListEntryType

```json
{
 "type": "enum",
 "prefix": "TYPE_",
 "slua-deprecated": true,
 "tooltip": ""
}
```


## enums/ListStatisticsOperation

```json
{
 "type": "enum",
 "prefix": "LIST_STAT_",
 "tooltip": ""
}
```


## enums/MapBeaconParam

```json
{
 "type": "param-dict",
 "prefix": "BEACON_",
 "tooltip": ""
}
```


## enums/ModifyLandAction

```json
{
 "type": "enum",
 "prefix": "LAND_",
 "tooltip": ""
}
```


## enums/ModifyLandBrush

```json
{
 "type": "enum",
 "prefix": "LAND_BRUSH_",
 "tooltip": ""
}
```


## enums/ObjectDetailsParam

```json
{
 "type": "param-dict",
 "prefix": "OBJECT_",
 "tooltip": ""
}
```


## enums/ObjectPathfindingType

```json
{
 "type": "enum",
 "prefix": "OPT_",
 "tooltip": ""
}
```


## enums/ObjectStatusParam

```json
{
 "type": "flag",
 "prefix": "STATUS_",
 "tooltip": ""
}
```


## enums/ParcelDetailsParam

```json
{
 "type": "param-dict",
 "prefix": "PARCEL_DETAILS_",
 "tooltip": ""
}
```


## enums/ParcelFlag

```json
{
 "type": "flag",
 "prefix": "PARCEL_FLAG_",
 "tooltip": ""
}
```


## enums/ParcelMediaCommand

```json
{
 "type": "param-dict",
 "prefix": "PARCEL_MEDIA_COMMAND_",
 "tooltip": ""
}
```


## enums/ParcelMediaQuery

```json
{
 "type": "param-dict",
 "prefix": "PARCEL_MEDIA_COMMAND_",
 "tooltip": ""
}
```


## enums/ParcelPrimCountCategory

```json
{
 "type": "enum",
 "prefix": "PARCEL_COUNT_",
 "tooltip": ""
}
```


## enums/ParcelSaleError

```json
{
 "type": "enum",
 "prefix": "PARCEL_SALE_",
 "tooltip": ""
}
```


## enums/ParcelSaleParam

```json
{
 "type": "param-dict",
 "prefix": "PARCEL_SALE_",
 "tooltip": ""
}
```


## enums/ParcelTeleportRouting

```json
{
 "type": "enum",
 "prefix": "TP_ROUTING_",
 "tooltip": ""
}
```


## enums/ParticleBlendFunc

```json
{
 "type": "enum",
 "prefix": "PSYS_PART_BF_",
 "tooltip": ""
}
```


## enums/ParticleFlag

```json
{
 "type": "flag",
 "prefix": "PSYS_PART_",
 "tooltip": ""
}
```


## enums/ParticleParam

```json
{
 "type": "param-dict",
 "prefix": "PSYS_",
 "tooltip": ""
}
```


## enums/ParticleSourcePattern

```json
{
 "type": "enum",
 "prefix": "PSYS_SRC_PATTERN_",
 "tooltip": ""
}
```


## enums/PassMode

```json
{
 "type": "enum",
 "prefix": "PASS_",
 "tooltip": ""
}
```


## enums/PayButton

```json
{
 "type": "param-list",
 "prefix": "PAY_",
 "other-values": true,
 "tooltip": ""
}
```


## enums/PhysicsMaterialParam

```json
{
 "type": "flag",
 "tooltip": ""
}
```


## enums/PhysicsMaterialPreset

```json
{
 "type": "enum",
 "prefix": "PRIM_MATERIAL_",
 "tooltip": ""
}
```


## enums/PhysicsShapeType

```json
{
 "type": "enum",
 "prefix": "PRIM_PHYSICS_SHAPE_",
 "tooltip": ""
}
```


## enums/PlaySoundFlag

```json
{
 "type": "flag",
 "prefix": "SOUND_",
 "special-members": [
  "SOUND_PLAY"
 ],
 "tooltip": ""
}
```


## enums/PrimBump

```json
{
 "type": "enum",
 "prefix": "PRIM_BUMP_",
 "tooltip": ""
}
```


## enums/PrimMediaControl

```json
{
 "type": "enum",
 "prefix": "PRIM_MEDIA_CONTROLS_",
 "tooltip": ""
}
```


## enums/PrimMediaError

```json
{
 "type": "enum",
 "prefix": "STATUS_",
 "tooltip": ""
}
```


## enums/PrimMediaParam

```json
{
 "type": "param-dict",
 "prefix": "PRIM_MEDIA_",
 "tooltip": ""
}
```


## enums/PrimMediaPerm

```json
{
 "type": "flag",
 "prefix": "PRIM_MEDIA_PERM_",
 "special-members": [
  "PRIM_MEDIA_PERM_NONE"
 ],
 "tooltip": ""
}
```


## enums/PrimParam

```json
{
 "type": "param-list",
 "prefix": "PRIM_",
 "tooltip": ""
}
```


## enums/PrimParamGet

```json
{
 "type": "param-list",
 "prefix": "PRIM_",
 "tooltip": ""
}
```


## enums/PrimShiny

```json
{
 "type": "enum",
 "prefix": "PRIM_SHINY_",
 "tooltip": ""
}
```


## enums/PrimTexgen

```json
{
 "type": "enum",
 "prefix": "PRIM_TEXGEN_",
 "tooltip": ""
}
```


## enums/PrimType

```json
{
 "type": "enum",
 "prefix": "PRIM_TYPE_",
 "tooltip": ""
}
```


## enums/PrimTypeHole

```json
{
 "type": "enum",
 "prefix": "PRIM_HOLE_",
 "tooltip": ""
}
```


## enums/PrimTypeSculpt

```json
{
 "type": "enum+flag",
 "enum": "PrimTypeSculptType",
 "flag": "PrimTypeSculptFlag",
 "mask": "PRIM_SCULPT_TYPE_MASK",
 "prefix": "PRIM_SCULPT_",
 "tooltip": ""
}
```


## enums/PrimTypeSculptFlag

```json
{
 "type": "flag",
 "prefix": "PRIM_SCULPT_FLAG_",
 "tooltip": ""
}
```


## enums/PrimTypeSculptType

```json
{
 "type": "enum",
 "prefix": "PRIM_SCULPT_TYPE_",
 "tooltip": ""
}
```


## enums/RayCastData

```json
{
 "type": "flag",
 "prefix": "RC_GET_",
 "tooltip": ""
}
```


## enums/RayCastError

```json
{
 "type": "enum",
 "prefix": "RCERR_",
 "other-values": true,
 "tooltip": ""
}
```


## enums/RayCastParam

```json
{
 "type": "param-dict",
 "prefix": "RC_",
 "tooltip": ""
}
```


## enums/RayCastRejectType

```json
{
 "type": "flag",
 "prefix": "RC_REJECT_",
 "tooltip": ""
}
```


## enums/ReflectionProbeType

```json
{
 "type": "flag",
 "prefix": "PRIM_REFLECTION_PROBE_",
 "tooltip": ""
}
```


## enums/RegionFlag

```json
{
 "type": "flag",
 "prefix": "REGION_FLAG_",
 "tooltip": ""
}
```


## enums/RemoteDataEventType

```json
{
 "type": "enum",
 "prefix": "REMOTE_DATA_",
 "deprecated": true,
 "tooltip": ""
}
```


## enums/ReturnObjectsError

```json
{
 "type": "enum",
 "prefix": "ERR_",
 "other-values": true,
 "tooltip": ""
}
```


## enums/ReturnObjectsScope

```json
{
 "type": "flag",
 "prefix": "OBJECT_RETURN_",
 "tooltip": ""
}
```


## enums/RezFlag

```json
{
 "type": "flag",
 "prefix": "REZ_FLAG_",
 "tooltip": ""
}
```


## enums/RezParam

```json
{
 "type": "param-list",
 "prefix": "REZ_",
 "tooltip": ""
}
```


## enums/ScriptPermission

```json
{
 "type": "flag",
 "prefix": "PERMISSION_",
 "tooltip": ""
}
```


## enums/ScriptProfileMode

```json
{
 "type": "enum",
 "prefix": "PROFILE_",
 "tooltip": ""
}
```


## enums/SimulatorData

```json
{
 "type": "enum",
 "prefix": "DATA_SIM_",
 "tooltip": ""
}
```


## enums/SimulatorStat

```json
{
 "type": "enum",
 "prefix": "SIM_STAT_",
 "tooltip": ""
}
```


## enums/SitError

```json
{
 "type": "enum",
 "prefix": "SIT_",
 "tooltip": ""
}
```


## enums/SitFlag

```json
{
 "type": "flag",
 "prefix": "SIT_FLAG_",
 "tooltip": ""
}
```


## enums/StringTrimType

```json
{
 "type": "enum",
 "prefix": "STRING_TRIM_",
 "tooltip": ""
}
```


## enums/TextureAnimMode

```json
{
 "type": "flag",
 "tooltip": ""
}
```


## enums/TransferError

```json
{
 "type": "enum",
 "prefix": "TRANSFER_",
 "tooltip": ""
}
```


## enums/TransferOwnershipFlag

```json
{
 "type": "flag",
 "prefix": "TRANSFER_FLAG_",
 "tooltip": ""
}
```


## enums/TransferOwnershipParam

```json
{
 "type": "param-dict",
 "prefix": "TRANSFER_",
 "tooltip": "No options yet."
}
```


## enums/VehicleFlag

```json
{
 "type": "flag",
 "prefix": "VEHICLE_FLAG_",
 "tooltip": ""
}
```


## enums/VehicleFloatParam

```json
{
 "type": "enum",
 "prefix": "VEHICLE_",
 "tooltip": ""
}
```


## enums/VehicleRotationParam

```json
{
 "type": "enum",
 "prefix": "VEHICLE_",
 "tooltip": ""
}
```


## enums/VehicleType

```json
{
 "type": "enum",
 "prefix": "VEHICLE_TYPE_",
 "tooltip": ""
}
```


## enums/VehicleVectorParam

```json
{
 "type": "enum",
 "prefix": "VEHICLE_",
 "tooltip": ""
}
```


# Section: constants (1082 entries)


## constants/ACTIVE

```json
{
 "member-of": [
  "DetectType"
 ],
 "tooltip": "Objects running a script or physically moving (using server resources). In llDetectedType(), it identifies physical objects and agents. In llSensor() or llSensorRepeat(), it searches for moving physical objects or scripted objects.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/AGENT

```json
{
 "member-of": [
  "DetectType"
 ],
 "tooltip": "Agents (avatars). In llDetectedType, it indicates an avatar. In llSensor or llSensorRepeat, it searches for avatars by legacy name (functionally identical to AGENT_BY_LEGACY_NAME, though using AGENT_BY_LEGACY_NAME is recommended instead).",
 "type": "integer",
 "value": "0x1"
}
```


## constants/AGENT_ALWAYS_RUN

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the queried avatar has 'Always Run' enabled or is using tap-tap-hold.",
 "type": "integer",
 "value": "0x1000"
}
```


## constants/AGENT_ATTACHMENTS

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the queried avatar has attachments.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/AGENT_AUTOMATED

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to identify if the avatar is registered with Linden Lab as an automated/scripted agent (bot).",
 "type": "integer",
 "value": "0x4000"
}
```


## constants/AGENT_AUTOPILOT

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is in autopilot mode, which is enabled when the user selects 'Go Here' on the ground or uses double-click autopilot.",
 "type": "integer",
 "value": "0x2000"
}
```


## constants/AGENT_AWAY

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is in 'away' mode, which indicates they toggled away or have been inactive for too long.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/AGENT_BUSY

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is in 'busy' mode.",
 "type": "integer",
 "value": "0x800"
}
```


## constants/AGENT_BY_LEGACY_NAME

```json
{
 "member-of": [
  "DetectType"
 ],
 "tooltip": "Used to find agents by legacy name. In llDetectedType, it indicates an avatar. In llSensor or llSensorRepeat, it searches for avatars by legacy name.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/AGENT_BY_USERNAME

```json
{
 "member-of": [
  "DetectType"
 ],
 "tooltip": "Used to find agents by username (see Avatar Names).",
 "type": "integer",
 "value": "0x10"
}
```


## constants/AGENT_CROUCHING

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is crouching.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/AGENT_FLOATING_VIA_SCRIPTED_ATTACHMENT

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is floating or hovering because of a scripted attachment using either llSetHoverHeight or llGroundRepel.",
 "type": "integer",
 "value": "0x8000"
}
```


## constants/AGENT_FLYING

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the queried avatar is flying or hovering.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/AGENT_IN_AIR

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is in the air (jumping, flying, or falling).",
 "type": "integer",
 "value": "0x100"
}
```


## constants/AGENT_LIST_PARCEL

```json
{
 "member-of": [
  "AgentListScope"
 ],
 "tooltip": "Agents on the same parcel where the script is running.",
 "type": "integer",
 "value": 1
}
```


## constants/AGENT_LIST_PARCEL_OWNER

```json
{
 "member-of": [
  "AgentListScope"
 ],
 "tooltip": "Agents on any parcel in the region where the parcel owner is the same as the owner of the parcel under the scripted object.",
 "type": "integer",
 "value": 2
}
```


## constants/AGENT_LIST_REGION

```json
{
 "member-of": [
  "AgentListScope"
 ],
 "tooltip": "Returns any or all agents in the region.",
 "type": "integer",
 "value": 4
}
```


## constants/AGENT_MOUSELOOK

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is in mouselook.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/AGENT_ON_OBJECT

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is sitting on an object and linked to it.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/AGENT_SCRIPTED

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is carrying scripted objects or has scripted attachments.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/AGENT_SITTING

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is sitting.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/AGENT_TYPING

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the avatar is typing.",
 "type": "integer",
 "value": "0x200"
}
```


## constants/AGENT_WALKING

```json
{
 "member-of": [
  "AgentInfo"
 ],
 "tooltip": "Used with llGetAgentInfo to determine if the queried avatar is walking, running, or crouch walking.",
 "type": "integer",
 "value": "0x80"
}
```


## constants/ALL_SIDES

```json
{
 "member-of": [
  "Faces"
 ],
 "tooltip": "Selects all sides of an object in an applicable function.",
 "type": "integer",
 "value": -1
}
```


## constants/ANIM_ON

```json
{
 "member-of": [
  "TextureAnimMode"
 ],
 "tooltip": "Enables texture animation. This must be set to start the animation and cleared to stop it.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/ATTACH_ANY_HUD

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "A special constant representing all HUD attachment points when filtering for any HUD attachment.",
 "type": "integer",
 "value": -1
}
```


## constants/ATTACH_AVATAR_CENTER

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's geometric center or root.",
 "type": "integer",
 "value": 40
}
```


## constants/ATTACH_BACK

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's back.",
 "type": "integer",
 "value": 9
}
```


## constants/ATTACH_BELLY

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's belly, stomach, or tummy.",
 "type": "integer",
 "value": 28
}
```


## constants/ATTACH_CHEST

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's chest or sternum.",
 "type": "integer",
 "value": 1
}
```


## constants/ATTACH_CHIN

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's chin.",
 "type": "integer",
 "value": 12
}
```


## constants/ATTACH_FACE_JAW

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's jaw.",
 "type": "integer",
 "value": 47
}
```


## constants/ATTACH_FACE_LEAR

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left ear (extended).",
 "type": "integer",
 "value": 48
}
```


## constants/ATTACH_FACE_LEYE

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left eye (extended).",
 "type": "integer",
 "value": 50
}
```


## constants/ATTACH_FACE_REAR

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right ear (extended).",
 "type": "integer",
 "value": 49
}
```


## constants/ATTACH_FACE_REYE

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right eye (extended).",
 "type": "integer",
 "value": 51
}
```


## constants/ATTACH_FACE_TONGUE

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's tongue.",
 "type": "integer",
 "value": 52
}
```


## constants/ATTACH_GROIN

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's groin.",
 "type": "integer",
 "value": 53
}
```


## constants/ATTACH_HEAD

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's head.",
 "type": "integer",
 "value": 2
}
```


## constants/ATTACH_HIND_LFOOT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left hind foot.",
 "type": "integer",
 "value": 54
}
```


## constants/ATTACH_HIND_RFOOT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right hind foot.",
 "type": "integer",
 "value": 55
}
```


## constants/ATTACH_HUD_BOTTOM

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Bottom.",
 "type": "integer",
 "value": 37
}
```


## constants/ATTACH_HUD_BOTTOM_LEFT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Bottom Left.",
 "type": "integer",
 "value": 36
}
```


## constants/ATTACH_HUD_BOTTOM_RIGHT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Bottom Right.",
 "type": "integer",
 "value": 38
}
```


## constants/ATTACH_HUD_CENTER_1

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Center.",
 "type": "integer",
 "value": 35
}
```


## constants/ATTACH_HUD_CENTER_2

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Center 2.",
 "type": "integer",
 "value": 31
}
```


## constants/ATTACH_HUD_TOP_CENTER

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Top Center.",
 "type": "integer",
 "value": 33
}
```


## constants/ATTACH_HUD_TOP_LEFT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Top Left.",
 "type": "integer",
 "value": 34
}
```


## constants/ATTACH_HUD_TOP_RIGHT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for HUD Top Right.",
 "type": "integer",
 "value": 32
}
```


## constants/ATTACH_LEAR

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left ear.",
 "type": "integer",
 "value": 13
}
```


## constants/ATTACH_LEFT_PEC

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left pectoral.",
 "type": "integer",
 "value": 29
}
```


## constants/ATTACH_LEYE

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left eye.",
 "type": "integer",
 "value": 15
}
```


## constants/ATTACH_LFOOT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left foot.",
 "type": "integer",
 "value": 7
}
```


## constants/ATTACH_LHAND

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left hand.",
 "type": "integer",
 "value": 5
}
```


## constants/ATTACH_LHAND_RING1

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left ring finger.",
 "type": "integer",
 "value": 41
}
```


## constants/ATTACH_LHIP

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left hip.",
 "type": "integer",
 "value": 25
}
```


## constants/ATTACH_LLARM

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left lower arm.",
 "type": "integer",
 "value": 21
}
```


## constants/ATTACH_LLLEG

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left lower leg.",
 "type": "integer",
 "value": 27
}
```


## constants/ATTACH_LPEC

```json
{
 "deprecated": {
  "use": "ATTACH_RIGHT_PEC"
 },
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right pectoral (deprecated, use ATTACH_RIGHT_PEC).",
 "type": "integer",
 "value": 30
}
```


## constants/ATTACH_LSHOULDER

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left shoulder.",
 "type": "integer",
 "value": 3
}
```


## constants/ATTACH_LUARM

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left upper arm.",
 "type": "integer",
 "value": 20
}
```


## constants/ATTACH_LULEG

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left upper leg.",
 "type": "integer",
 "value": 26
}
```


## constants/ATTACH_LWING

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left wing.",
 "type": "integer",
 "value": 45
}
```


## constants/ATTACH_MOUTH

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's mouth.",
 "type": "integer",
 "value": 11
}
```


## constants/ATTACH_NECK

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's neck.",
 "type": "integer",
 "value": 39
}
```


## constants/ATTACH_NOSE

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's nose.",
 "type": "integer",
 "value": 17
}
```


## constants/ATTACH_PELVIS

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's pelvis.",
 "type": "integer",
 "value": 10
}
```


## constants/ATTACH_REAR

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right ear.",
 "type": "integer",
 "value": 14
}
```


## constants/ATTACH_REYE

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right eye.",
 "type": "integer",
 "value": 16
}
```


## constants/ATTACH_RFOOT

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right foot.",
 "type": "integer",
 "value": 8
}
```


## constants/ATTACH_RHAND

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right hand (the default attachment point).",
 "type": "integer",
 "value": 6
}
```


## constants/ATTACH_RHAND_RING1

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right ring finger.",
 "type": "integer",
 "value": 42
}
```


## constants/ATTACH_RHIP

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right hip.",
 "type": "integer",
 "value": 22
}
```


## constants/ATTACH_RIGHT_PEC

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right pectoral.",
 "type": "integer",
 "value": 30
}
```


## constants/ATTACH_RLARM

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right lower arm.",
 "type": "integer",
 "value": 19
}
```


## constants/ATTACH_RLLEG

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right lower leg.",
 "type": "integer",
 "value": 24
}
```


## constants/ATTACH_RPEC

```json
{
 "deprecated": {
  "use": "ATTACH_LEFT_PEC"
 },
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's left pectoral (deprecated, use ATTACH_LEFT_PEC).",
 "type": "integer",
 "value": 29
}
```


## constants/ATTACH_RSHOULDER

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right shoulder.",
 "type": "integer",
 "value": 4
}
```


## constants/ATTACH_RUARM

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right upper arm.",
 "type": "integer",
 "value": 18
}
```


## constants/ATTACH_RULEG

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right upper leg.",
 "type": "integer",
 "value": 23
}
```


## constants/ATTACH_RWING

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's right wing.",
 "type": "integer",
 "value": 46
}
```


## constants/ATTACH_TAIL_BASE

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's tail base.",
 "type": "integer",
 "value": 43
}
```


## constants/ATTACH_TAIL_TIP

```json
{
 "member-of": [
  "AttachPoint"
 ],
 "tooltip": "Attachment point for the avatar's tail tip.",
 "type": "integer",
 "value": 44
}
```


## constants/AVOID_CHARACTERS

```json
{
 "member-of": [
  "CharacterAvoidanceMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 1
}
```


## constants/AVOID_DYNAMIC_OBSTACLES

```json
{
 "member-of": [
  "CharacterAvoidanceMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 2
}
```


## constants/AVOID_NONE

```json
{
 "member-of": [
  "CharacterAvoidanceMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 0
}
```


## constants/BEACON_MAP

```json
{
 "member-of": [
  "MapBeaconParam"
 ],
 "tooltip": "Causes llMapBeacon to optionally display and focus the world map on the avatar's viewer.",
 "type": "integer",
 "value": 1,
 "values": [
  {
   "name": "open_map",
   "value-type": "boolean"
  },
  {
   "name": "focus_map",
   "value-type": "boolean"
  }
 ]
}
```


## constants/CAMERA_ACTIVE

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Option flag used with llSetCameraParams to turn scripted control of the camera on or off.",
 "type": "integer",
 "value": 12,
 "value-type": "boolean",
 "values": [
  {
   "name": "isActive",
   "value-type": "boolean",
   "default": false
  }
 ]
}
```


## constants/CAMERA_BEHINDNESS_ANGLE

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets the angle in degrees within which the camera is not constrained by changes in target rotation.",
 "type": "integer",
 "value": 8,
 "value-type": "float",
 "values": [
  {
   "name": "degrees",
   "value-type": "float",
   "range": [
    0,
    180
   ],
   "default": 10
  }
 ]
}
```


## constants/CAMERA_BEHINDNESS_LAG

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets how strongly the camera is forced to stay behind the target if outside of the behindness angle.",
 "type": "integer",
 "value": 9,
 "value-type": "float",
 "values": [
  {
   "name": "seconds",
   "value-type": "float",
   "range": [
    0,
    3
   ],
   "default": 0
  }
 ]
}
```


## constants/CAMERA_DISTANCE

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets how far away the camera wants to be from its target.",
 "type": "integer",
 "value": 7,
 "value-type": "float",
 "values": [
  {
   "name": "meters",
   "value-type": "float",
   "range": [
    0.5,
    50
   ],
   "default": 3
  }
 ]
}
```


## constants/CAMERA_FOCUS

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets camera focus (target position) in region coordinates.",
 "type": "integer",
 "value": 17,
 "value-type": "vector",
 "values": [
  {
   "name": "position",
   "value-type": "vector"
  }
 ]
}
```


## constants/CAMERA_FOCUS_LAG

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets how much the camera lags as it aims toward the target.",
 "type": "integer",
 "value": 6,
 "value-type": "float",
 "values": [
  {
   "name": "seconds",
   "value-type": "float",
   "range": [
    0,
    3
   ],
   "default": 0.1
  }
 ]
}
```


## constants/CAMERA_FOCUS_LOCKED

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Option flag used with llSetCameraParams to lock the camera focus so it does not move.",
 "type": "integer",
 "value": 22,
 "value-type": "boolean",
 "values": [
  {
   "name": "isLocked",
   "value-type": "boolean",
   "default": false
  }
 ]
}
```


## constants/CAMERA_FOCUS_OFFSET

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Adjusts the camera focus position relative to the target.",
 "type": "integer",
 "value": 1,
 "value-type": "vector",
 "values": [
  {
   "name": "meters",
   "value-type": "vector",
   "range": [
    "<-10,-10,-10>",
    "<10,10,10>"
   ],
   "default": "<0,0,0>"
  }
 ]
}
```


## constants/CAMERA_FOCUS_THRESHOLD

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets the radius of a sphere around the camera's target position within which its focus is not affected by target motion.",
 "type": "integer",
 "value": 11,
 "value-type": "float",
 "values": [
  {
   "name": "meters",
   "value-type": "float",
   "range": [
    0,
    4
   ],
   "default": 1
  }
 ]
}
```


## constants/CAMERA_PITCH

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Adjusts the angular amount that the camera aims straight ahead versus straight down, maintaining the same distance (analogous to 'incidence').",
 "type": "integer",
 "value": 0,
 "value-type": "float",
 "values": [
  {
   "name": "degrees",
   "value-type": "float",
   "range": [
    -45,
    80
   ],
   "default": 0
  }
 ]
}
```


## constants/CAMERA_POSITION

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets camera position in region coordinates.",
 "type": "integer",
 "value": 13,
 "value-type": "vector",
 "values": [
  {
   "name": "position",
   "value-type": "vector"
  }
 ]
}
```


## constants/CAMERA_POSITION_LAG

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets how much the camera lags as it moves toward its ideal position.",
 "type": "integer",
 "value": 5,
 "value-type": "float",
 "values": [
  {
   "name": "seconds",
   "value-type": "float",
   "range": [
    0,
    3
   ],
   "default": 0.1
  }
 ]
}
```


## constants/CAMERA_POSITION_LOCKED

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Option flag used with llSetCameraParams to lock the camera position so it does not move.",
 "type": "integer",
 "value": 21,
 "value-type": "boolean",
 "values": [
  {
   "name": "isLocked",
   "value-type": "boolean",
   "default": false
  }
 ]
}
```


## constants/CAMERA_POSITION_THRESHOLD

```json
{
 "member-of": [
  "CameraParam"
 ],
 "tooltip": "Sets the radius of a sphere around the camera's ideal position within which it is not affected by target motion.",
 "type": "integer",
 "value": 10,
 "value-type": "float",
 "values": [
  {
   "name": "meters",
   "value-type": "float",
   "range": [
    0,
    3
   ],
   "default": 1
  }
 ]
}
```


## constants/CHANGED_ALLOWED_DROP

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Object inventory changed because a user other than the owner (or the owner if the object is no-mod) added an item. This is only possible if enabled via llAllowInventoryDrop.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/CHANGED_COLOR

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Object's Blinn-Phong color or alpha parameters have changed.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/CHANGED_INVENTORY

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Prim inventory has changed by someone who has modification rights to it.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/CHANGED_LINK

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Number of prims making up the object or avatars seated on it has changed. Also occurs when duplicating a linked object or when a prim changes type or shape. Does not trigger on attach/detach, sit/unsit in attachments, or single prim duplication.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/CHANGED_MEDIA

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Prim Media on the prim has changed.",
 "type": "integer",
 "value": "0x800"
}
```


## constants/CHANGED_OWNER

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Object has changed owners. Triggers in the original object when a user takes it, copies it, or deeds it to a group, and in the new object when it is first rezzed.",
 "type": "integer",
 "value": "0x80"
}
```


## constants/CHANGED_REGION

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Object has changed regions by crossing a boundary or teleporting (if attached). Triggers only in the root prim of a linkset.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/CHANGED_REGION_START

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Region containing this object has just come online.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/CHANGED_RENDER_MATERIAL

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Render material (prim material ID or material overrides) has changed on one or more faces.",
 "type": "integer",
 "value": "0x1000"
}
```


## constants/CHANGED_SCALE

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Prim scale of at least one prim in the linked object has changed. Only the root prim receives this event.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/CHANGED_SHAPE

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Prim base shape (PRIM_TYPE, such as box, prism, torus, taper, twist, or cut) has changed.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/CHANGED_TELEPORT

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Avatar this object is attached to has teleported. Triggers only in the root prim of an attachment. Does not occur for child prims or 'sit teleports'. If scripts are disabled at the destination, the event queues and triggers after moving to a script-enabled parcel.",
 "type": "integer",
 "value": "0x200"
}
```


## constants/CHANGED_TEXTURE

```json
{
 "member-of": [
  "ChangeType"
 ],
 "tooltip": "Prim texture parameters (shine/bump settings, repeats, flip, rotation, offset, or texture) have changed.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/CHARACTER_ACCOUNT_FOR_SKIPPED_FRAMES

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "If set to FALSE, the pathfinding character will not attempt to catch up on lost time when performance is low, potentially providing more reliable (though potentially more stuttery) movement. Default is TRUE.",
 "type": "integer",
 "value": 14,
 "value-type": "boolean",
 "default": true
}
```


## constants/CHARACTER_AVOIDANCE_MODE

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Specifies which objects a pathfinding character avoids (other characters, dynamic obstacles like fast-moving objects and avatars, or both). Combined using bit flags; setting to AVOID_NONE disables avoidance for both categories.",
 "type": "integer",
 "value": 5,
 "value-type": "integer",
 "enum": "CharacterAvoidanceMode",
 "default": "AVOID_CHARACTERS | AVOID_DYNAMIC_OBSTACLES"
}
```


## constants/CHARACTER_CMD_JUMP

```json
{
 "member-of": [
  "CharacterCommand"
 ],
 "tooltip": "Makes the character jump. Requires a height parameter between 0.1m and 2.0m as the first element of the llExecCharacterCmd option list.",
 "type": "integer",
 "value": "0x01"
}
```


## constants/CHARACTER_CMD_SMOOTH_STOP

```json
{
 "member-of": [
  "CharacterCommand"
 ],
 "tooltip": "Stops any current pathfinding operation in a smooth fashion.",
 "type": "integer",
 "value": 2
}
```


## constants/CHARACTER_CMD_STOP

```json
{
 "member-of": [
  "CharacterCommand"
 ],
 "tooltip": "Stops any current pathfinding operation.",
 "type": "integer",
 "value": "0x00"
}
```


## constants/CHARACTER_DESIRED_SPEED

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Constant used to indicate that the following argument is the desired speed (or speed of pursuit in meters per second) for a pathfinding character.",
 "type": "integer",
 "value": 1,
 "value-type": "float",
 "range": [
  0.2,
  40
 ],
 "default": 6
}
```


## constants/CHARACTER_DESIRED_TURN_SPEED

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Specifies the character's maximum speed while turning about the Z-axis (default is 6 meters/second). Note that this is only loosely enforced, and a character may turn at higher speeds under certain conditions.",
 "type": "integer",
 "value": 12,
 "value-type": "float",
 "range": [
  0.02,
  40
 ],
 "default": 6
}
```


## constants/CHARACTER_LENGTH

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Sets the collision capsule length for a pathfinding character. If the value is less than twice the radius plus 0.1m, it automatically adjusts to twice the radius plus 0.1m.",
 "type": "integer",
 "value": 3,
 "value-type": "float",
 "range": [
  0,
  10
 ]
}
```


## constants/CHARACTER_MAX_ACCEL

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Specifies the character's maximum acceleration rate (default is 20 m/s²).",
 "type": "integer",
 "value": 8,
 "value-type": "float",
 "range": [
  0.5,
  40
 ],
 "default": 20
}
```


## constants/CHARACTER_MAX_DECEL

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Specifies the character's maximum deceleration rate (default is 30 m/s²).",
 "type": "integer",
 "value": 9,
 "value-type": "float",
 "range": [
  0.5,
  60
 ],
 "default": 30
}
```


## constants/CHARACTER_MAX_SPEED

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Specifies the character's maximum speed (must be between 0.2 and 50 meters/second; default is 20 m/s). Affects speed when avoiding dynamic obstacles and when traversing low-walkability objects in TRAVERSAL_TYPE_FAST mode.",
 "type": "integer",
 "value": 13,
 "value-type": "float",
 "range": [
  1,
  40
 ],
 "default": 20
}
```


## constants/CHARACTER_MAX_TURN_RADIUS

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Specifies the character's turn radius when traveling at CHARACTER_DESIRED_TURN_SPEED (default is 1.25 meters).",
 "type": "integer",
 "value": 10,
 "value-type": "float",
 "range": [
  0.1,
  10
 ],
 "default": 1.25
}
```


## constants/CHARACTER_ORIENTATION

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Specifies the orientation of the collision capsule for a pathfinding character to denote how to interpret its size. Valid options are VERTICAL and HORIZONTAL.",
 "type": "integer",
 "value": 4,
 "value-type": "integer",
 "enum": "CharacterOrientation",
 "default": "VERTICAL"
}
```


## constants/CHARACTER_RADIUS

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Sets the collision capsule radius used to define the size of a pathfinding character.",
 "type": "integer",
 "value": 2,
 "value-type": "float",
 "range": [
  0.125,
  5
 ]
}
```


## constants/CHARACTER_STAY_WITHIN_PARCEL

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Determines whether a character is restricted to its starting parcel (default is FALSE). If TRUE, parcel boundaries act as one-way obstacles; the character cannot voluntarily leave and pathfinding behaviors (wander, flee, evade, pursue) will only choose goal points within the parcel. If pushed out, it can re-enter but cannot voluntarily leave again.",
 "type": "integer",
 "value": 15,
 "value-type": "boolean"
}
```


## constants/CHARACTER_TYPE

```json
{
 "member-of": [
  "CharacterParam",
  "GetClosestNavPointParam",
  "GetStaticPathParam"
 ],
 "tooltip": "Specifies the preferred surface and terrain terrain-type for the character (default is CHARACTER_TYPE_NONE). Used to describe preferred surfaces rather than behavior (e.g., cows prefer type B, sheep herded along a road prefer type C).",
 "type": "integer",
 "value": 6,
 "value-type": "integer",
 "enum": "CharacterType",
 "default": "CHARACTER_TYPE_NONE"
}
```


## constants/CHARACTER_TYPE_A

```json
{
 "member-of": [
  "CharacterType"
 ],
 "tooltip": "Used for pathfinding character types that prefer movement consistent with humanoids.",
 "type": "integer",
 "value": 0
}
```


## constants/CHARACTER_TYPE_B

```json
{
 "member-of": [
  "CharacterType"
 ],
 "tooltip": "Used for pathfinding character types that prefer movement consistent with wild animals or off-road vehicles.",
 "type": "integer",
 "value": 1
}
```


## constants/CHARACTER_TYPE_C

```json
{
 "member-of": [
  "CharacterType"
 ],
 "tooltip": "Used for mechanical pathfinding character types or road-going vehicles.",
 "type": "integer",
 "value": 2
}
```


## constants/CHARACTER_TYPE_D

```json
{
 "member-of": [
  "CharacterType"
 ],
 "tooltip": "Used for pathfinding character types that are inconsistent with types A, B, or C.",
 "type": "integer",
 "value": 3
}
```


## constants/CHARACTER_TYPE_NONE

```json
{
 "member-of": [
  "CharacterType"
 ],
 "tooltip": "Used to set no specific pathfinding character type.",
 "type": "integer",
 "value": 4
}
```


## constants/CLICK_ACTION_BUY

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Opens the buy dialog when the prim is clicked or touched.",
 "type": "integer",
 "value": 2
}
```


## constants/CLICK_ACTION_DISABLED

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Disables click actions. No touches are detected or passed.",
 "type": "integer",
 "value": 8
}
```


## constants/CLICK_ACTION_IGNORE

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Disables click actions. Clicks pass through the object to whatever is behind it, and no touches are detected.",
 "type": "integer",
 "value": 9
}
```


## constants/CLICK_ACTION_NONE

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Performs the default action: triggers touch events when the prim is clicked or touched.",
 "type": "integer",
 "value": 0
}
```


## constants/CLICK_ACTION_OPEN

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Opens the object inventory dialog when the prim is clicked or touched.",
 "type": "integer",
 "value": 4
}
```


## constants/CLICK_ACTION_OPEN_MEDIA

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Opens the web media dialog or plays parcel media (without pausing) when the prim is touched.",
 "type": "integer",
 "value": 6
}
```


## constants/CLICK_ACTION_PAY

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Opens the pay dialog when the prim is clicked or touched.",
 "type": "integer",
 "value": 3
}
```


## constants/CLICK_ACTION_PLAY

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Enables HTML-on-a-prim or plays/pauses parcel media when the prim is clicked or touched.",
 "type": "integer",
 "value": 5
}
```


## constants/CLICK_ACTION_SIT

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Causes the avatar to sit on the prim when it is clicked or touched.",
 "type": "integer",
 "value": 1
}
```


## constants/CLICK_ACTION_TOUCH

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Triggers touch events when the prim is clicked or touched.",
 "type": "integer",
 "value": 0
}
```


## constants/CLICK_ACTION_ZOOM

```json
{
 "member-of": [
  "ClickAction"
 ],
 "tooltip": "Zooms the avatar camera in on the object (Viewer 2) when clicked or touched.",
 "type": "integer",
 "value": 7
}
```


## constants/COMBAT_CHANNEL

```json
{
 "member-of": [
  "Channel",
  "ChannelNonPublic"
 ],
 "tooltip": "A region-wide channel reserved for combat-related log events. Passing this to llRegionSay adds the message to the combat log, and scripts listening on this channel can monitor the combat log.",
 "type": "integer",
 "value": 2147483646
}
```


## constants/COMBAT_LOG_ID

```json
{
 "tooltip": "ID used by all combat log messages sent from the region to the COMBAT_CHANNEL. Scripts can filter llListen calls with this ID to receive only system-generated combat log messages.",
 "type": "string",
 "slua-type": "uuid",
 "value": "45e0fcfa-2268-4490-a51c-3e51bdfe80d1"
}
```


## constants/CONTENT_TYPE_ATOM

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/atom+xml'.",
 "type": "integer",
 "value": 4
}
```


## constants/CONTENT_TYPE_FORM

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/x-www-form-urlencoded'.",
 "type": "integer",
 "value": 7
}
```


## constants/CONTENT_TYPE_HTML

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'text/html'. Only valid for embedded browsers on content owned by the viewer; falls back to 'text/plain' otherwise.",
 "type": "integer",
 "value": 1
}
```


## constants/CONTENT_TYPE_JSON

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/json'.",
 "type": "integer",
 "value": 5
}
```


## constants/CONTENT_TYPE_LLSD

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/llsd+xml' (Linden Lab Structured Data).",
 "type": "integer",
 "value": 6
}
```


## constants/CONTENT_TYPE_RSS

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/rss+xml'.",
 "type": "integer",
 "value": 8
}
```


## constants/CONTENT_TYPE_TEXT

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'text/plain'.",
 "type": "integer",
 "value": 0
}
```


## constants/CONTENT_TYPE_XHTML

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/xhtml+xml'.",
 "type": "integer",
 "value": 3
}
```


## constants/CONTENT_TYPE_XML

```json
{
 "member-of": [
  "HTTPContentType"
 ],
 "tooltip": "Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/xml'.",
 "type": "integer",
 "value": 2
}
```


## constants/CONTROL_BACK

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar move back control (↓ or S).",
 "type": "integer",
 "value": "0x2"
}
```


## constants/CONTROL_DOWN

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar move down control (PgDn or C).",
 "type": "integer",
 "value": "0x20"
}
```


## constants/CONTROL_FWD

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar move forward control (↑ or W).",
 "type": "integer",
 "value": "0x1"
}
```


## constants/CONTROL_LBUTTON

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar left mouse button control.",
 "type": "integer",
 "value": "0x10000000"
}
```


## constants/CONTROL_LEFT

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar move left control (Shift + ← or Shift + A).",
 "type": "integer",
 "value": "0x4"
}
```


## constants/CONTROL_ML_LBUTTON

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar left mouse button control while in mouselook.",
 "type": "integer",
 "value": "0x40000000"
}
```


## constants/CONTROL_RIGHT

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar move right control (Shift + → or Shift + D).",
 "type": "integer",
 "value": "0x8"
}
```


## constants/CONTROL_ROT_LEFT

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar rotate left control (← or A).",
 "type": "integer",
 "value": "0x100"
}
```


## constants/CONTROL_ROT_RIGHT

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar rotate right control (→ or D).",
 "type": "integer",
 "value": "0x200"
}
```


## constants/CONTROL_UP

```json
{
 "member-of": [
  "ControlButton"
 ],
 "tooltip": "Tests for the avatar move up control (PgUp or E).",
 "type": "integer",
 "value": "0x10"
}
```


## constants/DAMAGEABLE

```json
{
 "member-of": [
  "DetectType"
 ],
 "tooltip": "Identifies objects in the world that can process damage. In llDetectedType, it indicates a damageable agent, or an object containing a script with on_damage or final_damage events. Can also filter llSensor/llSensorRepeat calls.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/DAMAGE_TYPE_ACID

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by a caustic substance, such as acid.",
 "type": "integer",
 "value": 1
}
```


## constants/DAMAGE_TYPE_BLUDGEONING

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by a blunt object, such as a club.",
 "type": "integer",
 "value": "2"
}
```


## constants/DAMAGE_TYPE_COLD

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage inflicted by exposure to extreme cold.",
 "type": "integer",
 "value": 3
}
```


## constants/DAMAGE_TYPE_ELECTRIC

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by electricity.",
 "type": "integer",
 "value": 4
}
```


## constants/DAMAGE_TYPE_EMOTIONAL

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 14
}
```


## constants/DAMAGE_TYPE_FIRE

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage inflicted by exposure to heat or flames.",
 "type": "integer",
 "value": 5
}
```


## constants/DAMAGE_TYPE_FORCE

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage inflicted by a great force or impact (Vertical Sim / SLMC).",
 "type": "integer",
 "value": 6
}
```


## constants/DAMAGE_TYPE_GENERIC

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Generic or legacy damage.",
 "type": "integer",
 "value": 0
}
```


## constants/DAMAGE_TYPE_IMPACT

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "System damage generated by impact with land, terrain, or a prim.",
 "type": "integer",
 "value": -1
}
```


## constants/DAMAGE_TYPE_NECROTIC

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by a direct assault on the life-force.",
 "type": "integer",
 "value": 7
}
```


## constants/DAMAGE_TYPE_PIERCING

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by a piercing object such as a bullet, spear, or arrow (Vertical Sim / SLMC).",
 "type": "integer",
 "value": 8
}
```


## constants/DAMAGE_TYPE_POISON

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by poison.",
 "type": "integer",
 "value": 9
}
```


## constants/DAMAGE_TYPE_PSYCHIC

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by a direct assault on the mind.",
 "type": "integer",
 "value": 10
}
```


## constants/DAMAGE_TYPE_RADIANT

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by radiation or extreme light.",
 "type": "integer",
 "value": 11
}
```


## constants/DAMAGE_TYPE_SLASHING

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by a slashing object such as a sword or axe.",
 "type": "integer",
 "value": 12
}
```


## constants/DAMAGE_TYPE_SONIC

```json
{
 "member-of": [
  "DamageType"
 ],
 "tooltip": "Damage caused by loud noises, like a Crash Worship concert.",
 "type": "integer",
 "value": 13
}
```


## constants/DATA_BORN

```json
{
 "member-of": [
  "AgentData"
 ],
 "tooltip": "Used with llRequestAgentData to return the agent's account creation ('born on') date as a string in ISO 8601 format (YYYY-MM-DD), based on Pacific Time (not UTC).",
 "type": "integer",
 "value": 3
}
```


## constants/DATA_NAME

```json
{
 "member-of": [
  "AgentData"
 ],
 "tooltip": "Used with llRequestAgentData to return the requested agent's legacy name.",
 "type": "integer",
 "value": 2
}
```


## constants/DATA_ONLINE

```json
{
 "member-of": [
  "AgentData"
 ],
 "tooltip": "Used with llRequestAgentData to return whether the requested agent is online (returns an integer boolean string: TRUE if online, FALSE if offline).",
 "type": "integer",
 "value": 1
}
```


## constants/DATA_PAYINFO

```json
{
 "member-of": [
  "AgentData"
 ],
 "tooltip": "Used with llRequestAgentData to return a string containing the integer mask flag for payment status (contains PAYMENT_INFO_ON_FILE, PAYMENT_INFO_USED, or both).",
 "type": "integer",
 "value": 8
}
```


## constants/DATA_RATING

```json
{
 "member-of": [
  "AgentData"
 ],
 "tooltip": "Deprecated. Used with llRequestAgentData to return the string '0, 0, 0, 0, 0, 0'. It formerly returned a comma-separated list of positive and negative ratings (behavior, appearance, and building) before ratings were removed from SL.",
 "type": "integer",
 "value": 4
}
```


## constants/DATA_RESERVED_0

```json
{
 "member-of": [
  "AgentData"
 ],
 "tooltip": "Reserved for Linden use.",
 "type": "integer",
 "value": 9
}
```


## constants/DATA_SIM_POS

```json
{
 "member-of": [
  "SimulatorData"
 ],
 "tooltip": "Used with llRequestSimulatorData to return the region's global position as a vector.",
 "type": "integer",
 "value": 5
}
```


## constants/DATA_SIM_RATING

```json
{
 "member-of": [
  "SimulatorData"
 ],
 "tooltip": "Used with llRequestSimulatorData to return the simulator rating string ('PG', 'MATURE', 'ADULT', or 'UNKNOWN').",
 "type": "integer",
 "value": 7
}
```


## constants/DATA_SIM_STATUS

```json
{
 "member-of": [
  "SimulatorData"
 ],
 "tooltip": "Used with llRequestSimulatorData to return the simulator status as a string.",
 "type": "integer",
 "value": 6
}
```


## constants/DEBUG_CHANNEL

```json
{
 "member-of": [
  "Channel",
  "ChannelNonPublic"
 ],
 "tooltip": "A chat channel reserved for script debugging and error messages. Passing this to llSay, llWhisper, or llShout prints text to the Script Warning/Error Window and broadcasts it to nearby avatars' script consoles.",
 "type": "integer",
 "value": 2147483647
}
```


## constants/DEG_TO_RAD

```json
{
 "tooltip": "Constant 0.017453293 (precise value is PI/180). Multiply a value in degrees by this number to convert it to radians.",
 "type": "float",
 "value": "0.017453293"
}
```


## constants/DENSITY

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "tooltip": "Used with llSetPhysicsMaterial to indicate that the density parameter is enabled (which overrides the previous value). Must be between 1.0 and 22587.0 kg/m³.",
 "type": "integer",
 "value": 1
}
```


## constants/DEREZ_DIE

```json
{
 "member-of": [
  "DerezMode"
 ],
 "tooltip": "Used with llDerezObject to immediately delete (kill) the object.",
 "type": "integer",
 "value": 0
}
```


## constants/DEREZ_MAKE_TEMP

```json
{
 "member-of": [
  "DerezMode"
 ],
 "tooltip": "Used with llDerezObject to mark the object as temporary, allowing the simulator to clean it up at a later time.",
 "type": "integer",
 "value": 1
}
```


## constants/DEREZ_TO_INVENTORY

```json
{
 "member-of": [
  "DerezMode"
 ],
 "tooltip": "Used with llDerezObject to return the targeted object to the rezzer's (derezzer's) inventory, saving its current state.",
 "type": "integer",
 "value": 2
}
```


## constants/ENVIRONMENT_DAYINFO

```json
{
 "member-of": [
  "EnvironmentParamReadOnly"
 ],
 "tooltip": "Day cycle and time information: day_length (seconds in the environment's day cycle), day_offset (seconds offset from GMT), and secs_since_midnight (seconds elapsed since the last day cycle midnight).",
 "type": "integer",
 "value": 200,
 "values": [
  {
   "name": "day_length",
   "value-type": "integer",
   "details": "Number of seconds in the environments day cycle."
  },
  {
   "name": "day_offset",
   "value-type": "integer",
   "details": "Number of seconds day cycle is offset from GMT."
  },
  {
   "name": "secs_since_midnight",
   "value-type": "float",
   "details": "Number of seconds elapsed since the last day cycle midnight."
  }
 ],
 "access": "read"
}
```


## constants/ENV_INVALID_AGENT

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Unable to find the specified agent, or could not find an agent with the specified ID.",
 "type": "integer",
 "value": -4
}
```


## constants/ENV_INVALID_RULE

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "There was an issue with one of the rules, or an attempt was made to change an unknown property.",
 "type": "integer",
 "value": -5
}
```


## constants/ENV_NOT_EXPERIENCE

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Attempted to change environments outside an experience, or the script is not running as part of an experience with a valid experience key.",
 "type": "integer",
 "value": -1
}
```


## constants/ENV_NO_ENVIRONMENT

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Environmental settings inventory object could not be found, or there is no environment on this parcel to modify.",
 "type": "integer",
 "value": -3
}
```


## constants/ENV_NO_EXPERIENCE_LAND

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Experience has not been enabled or cannot run on the land.",
 "type": "integer",
 "value": -7
}
```


## constants/ENV_NO_EXPERIENCE_PERMISSION

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Agent has not granted permission to change environments.",
 "type": "integer",
 "value": -2
}
```


## constants/ENV_NO_PERMISSIONS

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Script lacks permissions to modify the environment at this location, or an attempt was made to remove altitude track 0 or 1.",
 "type": "integer",
 "value": -9
}
```


## constants/ENV_OK

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Agent, parcel, or region will attempt to change the applied environment.",
 "type": "integer",
 "value": 1
}
```


## constants/ENV_THROTTLE

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Scripts have exceeded the throttle limit. Wait and retry the request.",
 "type": "integer",
 "value": -8
}
```


## constants/ENV_VALIDATION_FAIL

```json
{
 "member-of": [
  "EnvironmentError"
 ],
 "tooltip": "Could not validate the environmental settings or values passed.",
 "type": "integer",
 "value": -6
}
```


## constants/EOF

```json
{
 "tooltip": "Value returned by llGetNotecardLine (through the dataserver event) and llGetNotecardLineSync when the requested line is past the end of the notecard. Equal to three newline characters (\"\\n\\n\\n\").",
 "type": "string",
 "value": "\\n\\n\\n"
}
```


## constants/ERR_GENERIC

```json
{
 "member-of": [
  "ReturnObjectsError"
 ],
 "tooltip": "An inexplicable and generic error where nothing is known about the cause.",
 "type": "integer",
 "value": -1
}
```


## constants/ERR_MALFORMED_PARAMS

```json
{
 "member-of": [
  "ReturnObjectsError"
 ],
 "tooltip": "Return value for llReturnObject* functions indicating that the parameters passed are malformed.",
 "type": "integer",
 "value": -3
}
```


## constants/ERR_PARCEL_PERMISSIONS

```json
{
 "member-of": [
  "ReturnObjectsError"
 ],
 "tooltip": "Return value for llReturnObject* functions indicating a lack of permissions to perform the task on the specified parcel.",
 "type": "integer",
 "value": -2
}
```


## constants/ERR_RUNTIME_PERMISSIONS

```json
{
 "member-of": [
  "ReturnObjectsError"
 ],
 "tooltip": "Return value for llReturnObject* functions indicating the script lacks the runtime permissions required to perform the requested task.",
 "type": "integer",
 "value": -4
}
```


## constants/ERR_THROTTLED

```json
{
 "member-of": [
  "ReturnObjectsError"
 ],
 "tooltip": "Return value for llReturnObject* functions indicating that the task has been throttled and should be retried later.",
 "type": "integer",
 "value": -5
}
```


## constants/ESTATE_ACCESS_ALLOWED_AGENT_ADD

```json
{
 "member-of": [
  "EstateAccessParam"
 ],
 "tooltip": "Used as an input parameter for llManageEstateAccess to add an agent to the estate's Allowed Residents list.",
 "type": "integer",
 "value": 4
}
```


## constants/ESTATE_ACCESS_ALLOWED_AGENT_REMOVE

```json
{
 "member-of": [
  "EstateAccessParam"
 ],
 "tooltip": "Used as an input parameter for llManageEstateAccess to remove an agent from the estate's Allowed Residents list.",
 "type": "integer",
 "value": 8
}
```


## constants/ESTATE_ACCESS_ALLOWED_GROUP_ADD

```json
{
 "member-of": [
  "EstateAccessParam"
 ],
 "tooltip": "Used as an input parameter for llManageEstateAccess to add a group to the estate's Allowed Groups list.",
 "type": "integer",
 "value": 16
}
```


## constants/ESTATE_ACCESS_ALLOWED_GROUP_REMOVE

```json
{
 "member-of": [
  "EstateAccessParam"
 ],
 "tooltip": "Used as an input parameter for llManageEstateAccess to remove a group from the estate's Allowed Groups list.",
 "type": "integer",
 "value": 32
}
```


## constants/ESTATE_ACCESS_BANNED_AGENT_ADD

```json
{
 "member-of": [
  "EstateAccessParam"
 ],
 "tooltip": "Used as an input parameter for llManageEstateAccess to add an agent to the estate's Banned Residents list.",
 "type": "integer",
 "value": 64
}
```


## constants/ESTATE_ACCESS_BANNED_AGENT_REMOVE

```json
{
 "member-of": [
  "EstateAccessParam"
 ],
 "tooltip": "Used as an input parameter for llManageEstateAccess to remove an agent from the estate's Banned Residents list.",
 "type": "integer",
 "value": 128
}
```


## constants/FALSE

```json
{
 "tooltip": "Constant representing a boolean FALSE value. Used in conditional structures or variables to improve readability over the integer value (0).",
 "type": "integer",
 "slua-removed": true,
 "value": 0
}
```


## constants/FILTER_FLAGS

```json
{
 "member-of": [
  "AttachedListFilterParam"
 ],
 "tooltip": "Flags used to control which attachments are returned.",
 "type": "integer",
 "value": 2,
 "value-type": "integer",
 "enum": "AttachedListFilterFlag"
}
```


## constants/FILTER_FLAG_HUDS

```json
{
 "member-of": [
  "AttachedListFilterFlag"
 ],
 "tooltip": "Filter flag used with llGetAttachedListFiltered to include HUDs with matching experiences in the returned result.",
 "type": "integer",
 "value": "0x0001"
}
```


## constants/FILTER_INCLUDE

```json
{
 "member-of": [
  "AttachedListFilterParam"
 ],
 "tooltip": "Filter parameter used to include a specific attachment point.",
 "type": "integer",
 "value": 1,
 "value-type": "integer",
 "enum": "AttachPoint"
}
```


## constants/FORCE_DIRECT_PATH

```json
{
 "member-of": [
  "CharacterNavigateParam"
 ],
 "tooltip": "Forces the pathfinding character to navigate in a straight line toward the specified position (can be set to TRUE or FALSE).",
 "type": "integer",
 "value": 1,
 "value-type": "boolean",
 "default": false
}
```


## constants/FRICTION

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "tooltip": "Used with llSetPhysicsMaterial to enable the friction override. The value must be between 0.0 and 255.0.",
 "type": "integer",
 "value": 2
}
```


## constants/GAME_CONTROL_AXIS_ADVANCE

```json
{
 "tooltip": "Forward/backward movement. Modal axis index 1 for AVATAR, MOUSELOOK, and CAPTIVE modes.",
 "type": "integer",
 "value": 1
}
```


## constants/GAME_CONTROL_AXIS_BOOM

```json
{
 "tooltip": "Camera up/down movement. Modal axis index 4 for FLYCAM mode.",
 "type": "integer",
 "value": 4
}
```


## constants/GAME_CONTROL_AXIS_DOLLY

```json
{
 "tooltip": "Camera forward/backward movement. Modal axis index 1 for FLYCAM mode.",
 "type": "integer",
 "value": 1
}
```


## constants/GAME_CONTROL_AXIS_LEFTX

```json
{
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Left stick X axis. Canonical axis index 0.",
 "type": "integer",
 "value": 0
}
```


## constants/GAME_CONTROL_AXIS_LEFTY

```json
{
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Left stick Y axis. Canonical axis index 1.",
 "type": "integer",
 "value": 1
}
```


## constants/GAME_CONTROL_AXIS_LEFT_TRIGGER

```json
{
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Left trigger. Canonical axis index 4.",
 "type": "integer",
 "value": 4
}
```


## constants/GAME_CONTROL_AXIS_LOOK

```json
{
 "tooltip": "Looking up/down. Modal axis index 3 for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": 3
}
```


## constants/GAME_CONTROL_AXIS_PAN

```json
{
 "tooltip": "Camera pan left/right. Modal axis index 2 for FLYCAM mode.",
 "type": "integer",
 "value": 2
}
```


## constants/GAME_CONTROL_AXIS_RIGHTX

```json
{
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Right stick X axis. Canonical axis index 2.",
 "type": "integer",
 "value": 2
}
```


## constants/GAME_CONTROL_AXIS_RIGHTY

```json
{
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Right stick Y axis. Canonical axis index 3.",
 "type": "integer",
 "value": 3
}
```


## constants/GAME_CONTROL_AXIS_RIGHT_TRIGGER

```json
{
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Right trigger. Canonical axis index 5.",
 "type": "integer",
 "value": 5
}
```


## constants/GAME_CONTROL_AXIS_RISE

```json
{
 "tooltip": "Up/down movement. Modal axis index 4 for AVATAR, MOUSELOOK, and CAPTIVE modes.",
 "type": "integer",
 "value": 4
}
```


## constants/GAME_CONTROL_AXIS_ROLL

```json
{
 "tooltip": "Camera roll. Modal axis index 5 for FLYCAM mode.",
 "type": "integer",
 "value": 5
}
```


## constants/GAME_CONTROL_AXIS_STRAFE

```json
{
 "tooltip": "Left/right movement. Modal axis index 0 for AVATAR, MOUSELOOK, and CAPTIVE modes.",
 "type": "integer",
 "value": 0
}
```


## constants/GAME_CONTROL_AXIS_TILT

```json
{
 "tooltip": "Camera tilt up/down. Modal axis index 3 for FLYCAM mode.",
 "type": "integer",
 "value": 3
}
```


## constants/GAME_CONTROL_AXIS_TRIGGERLEFT

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_AXIS_LEFT_TRIGGER"
 },
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Left trigger. Canonical axis index 4 (deprecated, use GAME_CONTROL_AXIS_LEFT_TRIGGER).",
 "type": "integer",
 "value": 4
}
```


## constants/GAME_CONTROL_AXIS_TRIGGERRIGHT

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_AXIS_RIGHT_TRIGGER"
 },
 "member-of": [
  "GameControlAxis"
 ],
 "tooltip": "Right trigger. Canonical axis index 5 (deprecated, use GAME_CONTROL_AXIS_RIGHT_TRIGGER).",
 "type": "integer",
 "value": 5
}
```


## constants/GAME_CONTROL_AXIS_TRUCK

```json
{
 "tooltip": "Camera lateral (left/right) movement. Modal axis index 0 for FLYCAM mode.",
 "type": "integer",
 "value": 0
}
```


## constants/GAME_CONTROL_AXIS_TURN

```json
{
 "tooltip": "Turning left/right. Modal axis index 2 for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": 2
}
```


## constants/GAME_CONTROL_AXIS_ZOOM

```json
{
 "tooltip": "Camera zoom in/out. Modal axis index 6 for AVATAR, MOUSELOOK, CAPTIVE, and FLYCAM modes.",
 "type": "integer",
 "value": 6
}
```


## constants/GAME_CONTROL_BUTTON_A

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_BUTTON_SOUTH"
 },
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Bottom face button (deprecated, use GAME_CONTROL_BUTTON_SOUTH).",
 "type": "integer",
 "value": "0x1"
}
```


## constants/GAME_CONTROL_BUTTON_ADVANCE_BACK

```json
{
 "tooltip": "Move backward. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x1000"
}
```


## constants/GAME_CONTROL_BUTTON_ADVANCE_FORWARD

```json
{
 "tooltip": "Move forward. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x800"
}
```


## constants/GAME_CONTROL_BUTTON_B

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_BUTTON_EAST"
 },
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Right face button (deprecated, use GAME_CONTROL_BUTTON_EAST).",
 "type": "integer",
 "value": "0x2"
}
```


## constants/GAME_CONTROL_BUTTON_BACK

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_BUTTON_SELECT"
 },
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Select/back button (deprecated, use GAME_CONTROL_BUTTON_SELECT).",
 "type": "integer",
 "value": "0x10"
}
```


## constants/GAME_CONTROL_BUTTON_CROUCH

```json
{
 "tooltip": "Crouch. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/GAME_CONTROL_BUTTON_CURSOR_BUTTON_LEFT

```json
{
 "tooltip": "Left mouse button click. Modal button for MOUSELOOK and CURSOR modes.",
 "type": "integer",
 "value": "0x200"
}
```


## constants/GAME_CONTROL_BUTTON_CURSOR_BUTTON_RIGHT

```json
{
 "tooltip": "Right mouse button click. Modal button for MOUSELOOK and CURSOR modes.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/GAME_CONTROL_BUTTON_DOLLY_BACK

```json
{
 "tooltip": "Camera dolly backward. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x1000"
}
```


## constants/GAME_CONTROL_BUTTON_DOLLY_FORWARD

```json
{
 "tooltip": "Camera dolly forward. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x800"
}
```


## constants/GAME_CONTROL_BUTTON_DPAD_DOWN

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "D-pad down.",
 "type": "integer",
 "value": "0x1000"
}
```


## constants/GAME_CONTROL_BUTTON_DPAD_LEFT

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "D-pad left.",
 "type": "integer",
 "value": "0x2000"
}
```


## constants/GAME_CONTROL_BUTTON_DPAD_RIGHT

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "D-pad right.",
 "type": "integer",
 "value": "0x4000"
}
```


## constants/GAME_CONTROL_BUTTON_DPAD_UP

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "D-pad up.",
 "type": "integer",
 "value": "0x800"
}
```


## constants/GAME_CONTROL_BUTTON_EAST

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Right face button.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/GAME_CONTROL_BUTTON_GUIDE

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_BUTTON_HOME"
 },
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Home/guide button (deprecated, use GAME_CONTROL_BUTTON_HOME).",
 "type": "integer",
 "value": "0x20"
}
```


## constants/GAME_CONTROL_BUTTON_HOME

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Home/guide button.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/GAME_CONTROL_BUTTON_JUMP

```json
{
 "tooltip": "Jump. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/GAME_CONTROL_BUTTON_LEFTSHOULDER

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Left shoulder/bumper button.",
 "type": "integer",
 "value": "0x200"
}
```


## constants/GAME_CONTROL_BUTTON_LEFTSTICK

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Left analog stick click.",
 "type": "integer",
 "value": "0x80"
}
```


## constants/GAME_CONTROL_BUTTON_MISC1

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Miscellaneous button 1.",
 "type": "integer",
 "value": "0x8000"
}
```


## constants/GAME_CONTROL_BUTTON_NORTH

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Top face button.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/GAME_CONTROL_BUTTON_PADDLE1

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Paddle button 1.",
 "type": "integer",
 "value": "0x10000"
}
```


## constants/GAME_CONTROL_BUTTON_PADDLE2

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Paddle button 2.",
 "type": "integer",
 "value": "0x20000"
}
```


## constants/GAME_CONTROL_BUTTON_PADDLE3

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Paddle button 3.",
 "type": "integer",
 "value": "0x40000"
}
```


## constants/GAME_CONTROL_BUTTON_PADDLE4

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Paddle button 4.",
 "type": "integer",
 "value": "0x80000"
}
```


## constants/GAME_CONTROL_BUTTON_PAN_LEFT

```json
{
 "tooltip": "Camera pan left. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/GAME_CONTROL_BUTTON_PAN_RIGHT

```json
{
 "tooltip": "Camera pan right. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/GAME_CONTROL_BUTTON_RESET

```json
{
 "tooltip": "Reset camera to default view. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x80"
}
```


## constants/GAME_CONTROL_BUTTON_RIGHTSHOULDER

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Right shoulder/bumper button.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/GAME_CONTROL_BUTTON_RIGHTSTICK

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Right analog stick click.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/GAME_CONTROL_BUTTON_ROLL_CCW

```json
{
 "tooltip": "Roll camera counter-clockwise. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x200"
}
```


## constants/GAME_CONTROL_BUTTON_ROLL_CW

```json
{
 "tooltip": "Roll camera clockwise. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/GAME_CONTROL_BUTTON_SELECT

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Select/back button.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/GAME_CONTROL_BUTTON_SIT

```json
{
 "tooltip": "Toggle sitting. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/GAME_CONTROL_BUTTON_SOUTH

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Bottom face button.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/GAME_CONTROL_BUTTON_START

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Start/menu button.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/GAME_CONTROL_BUTTON_STRAFE_LEFT

```json
{
 "tooltip": "Strafe left. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x2000"
}
```


## constants/GAME_CONTROL_BUTTON_STRAFE_RIGHT

```json
{
 "tooltip": "Strafe right. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x4000"
}
```


## constants/GAME_CONTROL_BUTTON_TOGGLE_ALT_ZOOM

```json
{
 "tooltip": "Toggle alt-zoom. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/GAME_CONTROL_BUTTON_TOGGLE_CURSOR

```json
{
 "tooltip": "Toggle cursor mode. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/GAME_CONTROL_BUTTON_TOGGLE_FLYCAM

```json
{
 "tooltip": "Toggle flycam mode. Modal button for all modes.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/GAME_CONTROL_BUTTON_TOGGLE_FOLLOW

```json
{
 "tooltip": "Toggle camera follow mode. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/GAME_CONTROL_BUTTON_TOGGLE_MOUSELOOK

```json
{
 "tooltip": "Toggle mouselook mode. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/GAME_CONTROL_BUTTON_TOGGLE_SPEAK

```json
{
 "tooltip": "Toggle voice speak. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/GAME_CONTROL_BUTTON_TOUCHPAD

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Touchpad click.",
 "type": "integer",
 "value": "0x100000"
}
```


## constants/GAME_CONTROL_BUTTON_TRUCK_LEFT

```json
{
 "tooltip": "Camera truck left. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x2000"
}
```


## constants/GAME_CONTROL_BUTTON_TRUCK_RIGHT

```json
{
 "tooltip": "Camera truck right. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x4000"
}
```


## constants/GAME_CONTROL_BUTTON_WEST

```json
{
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Left face button.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/GAME_CONTROL_BUTTON_X

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_BUTTON_WEST"
 },
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Left face button (deprecated, use GAME_CONTROL_BUTTON_WEST).",
 "type": "integer",
 "value": "0x4"
}
```


## constants/GAME_CONTROL_BUTTON_Y

```json
{
 "deprecated": {
  "use": "GAME_CONTROL_BUTTON_NORTH"
 },
 "member-of": [
  "GameControlButton"
 ],
 "tooltip": "Top face button (deprecated, use GAME_CONTROL_BUTTON_NORTH).",
 "type": "integer",
 "value": "0x8"
}
```


## constants/GAME_CONTROL_BUTTON_ZOOM_IN

```json
{
 "tooltip": "Zoom camera in. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/GAME_CONTROL_BUTTON_ZOOM_OUT

```json
{
 "tooltip": "Zoom camera out. Modal button for FLYCAM mode.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/GAME_CONTROL_MODE_AVATAR

```json
{
 "member-of": [
  "GameControlMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 0
}
```


## constants/GAME_CONTROL_MODE_CAPTIVE

```json
{
 "member-of": [
  "GameControlMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 3
}
```


## constants/GAME_CONTROL_MODE_CURSOR

```json
{
 "member-of": [
  "GameControlMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 4
}
```


## constants/GAME_CONTROL_MODE_FLYCAM

```json
{
 "member-of": [
  "GameControlMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 2
}
```


## constants/GAME_CONTROL_MODE_MOUSELOOK

```json
{
 "member-of": [
  "GameControlMode"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 1
}
```


## constants/GCNP_GET_WALKABILITY

```json
{
 "member-of": [
  "GetClosestNavPointParam"
 ],
 "private": true,
 "tooltip": "",
 "type": "integer",
 "value": "2",
 "value-type": "boolean"
}
```


## constants/GCNP_RADIUS

```json
{
 "member-of": [
  "GetClosestNavPointParam"
 ],
 "tooltip": "Used with llGetClosestNavPoint to limit how far out to search for a navigation point.",
 "type": "integer",
 "value": 0,
 "value-type": "float",
 "default": 20
}
```


## constants/GCNP_STATIC

```json
{
 "member-of": [
  "GetClosestNavPointParam"
 ],
 "tooltip": "Used with llGetClosestNavPoint to specify that the test should use the static navmesh, ignoring all dynamic obstacles.",
 "type": "integer",
 "value": 1,
 "value-type": "boolean",
 "default": false
}
```


## constants/GRAVITY_MULTIPLIER

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "tooltip": "Used with llSetPhysicsMaterial to enable the gravity multiplier override. The value must be between -1.0 and +28.0.",
 "type": "integer",
 "value": 8
}
```


## constants/HORIZONTAL

```json
{
 "member-of": [
  "CharacterOrientation"
 ],
 "tooltip": "Constant indicating that the collision capsule orientation for a pathfinding character is horizontal.",
 "type": "integer",
 "value": 1
}
```


## constants/HTTP_ACCEPT

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "Used with llHTTPRequest to override the default Accept header with custom MIME types (such as application/json, text/html, etc.). Responses with unlisted content types will return status 415.",
 "type": "integer",
 "value": 8,
 "value-type": "string-multi",
 "default": "text/plain;charset=utf-8"
}
```


## constants/HTTP_BODY_MAXLENGTH

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "pretty-name": "max_body_length",
 "tooltip": "Sets the maximum (UTF-8 encoded) byte length of the HTTP response body. The maximum limit depends on the VM being used (Mono Max: 16384 bytes, LSO Max: 4096 bytes).",
 "type": "integer",
 "value": 2,
 "value-type": "integer",
 "default": 2048
}
```


## constants/HTTP_BODY_TRUNCATED

```json
{
 "member-of": [
  "HTTPResponseError"
 ],
 "tooltip": "Indicates the response body truncation point in bytes.",
 "type": "integer",
 "value": 0
}
```


## constants/HTTP_CUSTOM_HEADER

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "Adds custom HTTP headers to the request (up to 8 per request). At the SLua level, provide a string-keyed table mapping header names to values; the serializer emits one HTTP_CUSTOM_HEADER/key/value triple per entry. Some default or sensitive headers are blocked for security reasons.",
 "type": "integer",
 "value": 5,
 "value-type": "string-map"
}
```


## constants/HTTP_EXTENDED_ERROR

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "If set to TRUE, llHTTPRequest always returns a key. If an error occurs during the request, detailed error information (delivered in an RFC 7807 JSON block) is reported through the http_response event using that key.",
 "type": "integer",
 "value": 9,
 "value-type": "boolean",
 "default": false
}
```


## constants/HTTP_METHOD

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "Specifies the HTTP method ('GET', 'POST', 'PUT', or 'DELETE') for the request.",
 "type": "integer",
 "value": 0,
 "value-type": "string",
 "default": "GET"
}
```


## constants/HTTP_MIMETYPE

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "Specifies the request Content-Type MIME type. Text types should define a charset (e.g., 'text/plain;charset=utf-8'). Use 'application/x-www-form-urlencoded' to emulate HTML forms.",
 "type": "integer",
 "value": 1,
 "value-type": "string",
 "default": "text/plain;charset=utf-8"
}
```


## constants/HTTP_PRAGMA_NO_CACHE

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "Controls whether the 'Pragma: no-cache' header is sent with the HTTP request. When SendHeader is TRUE (default), the header is sent; when FALSE, it is omitted.",
 "type": "integer",
 "value": 6,
 "value-type": "boolean",
 "default": true
}
```


## constants/HTTP_USER_AGENT

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "Appends a custom string to the default LSL User-Agent header value. Must follow HTTP standard syntax (e.g., 'My-Script-Name/1.0'). Spaces are not allowed and will cause a script error; use hyphens instead.",
 "type": "integer",
 "value": 7,
 "value-type": "string"
}
```


## constants/HTTP_VERBOSE_THROTTLE

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "If set to TRUE, shouts error messages to DEBUG_CHANNEL if the outgoing request rate exceeds the server limit. If FALSE, these error messages are suppressed.",
 "type": "integer",
 "value": 4,
 "value-type": "boolean",
 "default": true
}
```


## constants/HTTP_VERIFY_CERT

```json
{
 "member-of": [
  "HTTPRequestParam"
 ],
 "tooltip": "If set to TRUE, the server's SSL certificate must be verifiable using a standard certificate authority when making HTTPS requests. If FALSE, any SSL certificate is accepted.",
 "type": "integer",
 "value": 3,
 "value-type": "boolean",
 "default": true
}
```


## constants/IMG_USE_BAKED_AUX1

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "9742065b-19b5-297c-858a-29711d539043"
}
```


## constants/IMG_USE_BAKED_AUX2

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "03642e83-2bd1-4eb9-34b4-4c47ed586d2d"
}
```


## constants/IMG_USE_BAKED_AUX3

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "edd51b77-fc10-ce7a-4b3d-011dfc349e4f"
}
```


## constants/IMG_USE_BAKED_EYES

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "52cc6bb6-2ee5-e632-d3ad-50197b1dcb8a"
}
```


## constants/IMG_USE_BAKED_HAIR

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "09aac1fb-6bce-0bee-7d44-caac6dbb6c63"
}
```


## constants/IMG_USE_BAKED_HEAD

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "5a9f4a74-30f2-821c-b88d-70499d3e7183"
}
```


## constants/IMG_USE_BAKED_LEFTARM

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "ff62763f-d60a-9855-890b-0c96f8f8cd98"
}
```


## constants/IMG_USE_BAKED_LEFTLEG

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "8e915e25-31d1-cc95-ae08-d58a47488251"
}
```


## constants/IMG_USE_BAKED_LOWER

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "24daea5f-0539-cfcf-047f-fbc40b2786ba"
}
```


## constants/IMG_USE_BAKED_SKIRT

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "43529ce8-7faa-ad92-165a-bc4078371687"
}
```


## constants/IMG_USE_BAKED_UPPER

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "ae2de45c-d252-50b8-5c6e-19f39ce79317"
}
```


## constants/INVENTORY_ALL

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to specify that all types of inventory items should be retrieved.",
 "type": "integer",
 "value": -1
}
```


## constants/INVENTORY_ANIMATION

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the ANIMATION type.",
 "type": "integer",
 "value": 20
}
```


## constants/INVENTORY_BODYPART

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the BODYPART type.",
 "type": "integer",
 "value": 13
}
```


## constants/INVENTORY_CLOTHING

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the CLOTHING type.",
 "type": "integer",
 "value": 5
}
```


## constants/INVENTORY_GESTURE

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the GESTURE type.",
 "type": "integer",
 "value": 21
}
```


## constants/INVENTORY_LANDMARK

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the LANDMARK type.",
 "type": "integer",
 "value": 3
}
```


## constants/INVENTORY_MATERIAL

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the MATERIAL type.",
 "type": "integer",
 "value": 57
}
```


## constants/INVENTORY_NONE

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Value returned by inventory functions indicating that the specified inventory item does not exist.",
 "type": "integer",
 "value": -1
}
```


## constants/INVENTORY_NOTECARD

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the NOTECARD type.",
 "type": "integer",
 "value": 7
}
```


## constants/INVENTORY_OBJECT

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the OBJECT type.",
 "type": "integer",
 "value": 6
}
```


## constants/INVENTORY_SCRIPT

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the SCRIPT type.",
 "type": "integer",
 "value": 10
}
```


## constants/INVENTORY_SETTING

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the SETTING type.",
 "type": "integer",
 "value": 56
}
```


## constants/INVENTORY_SOUND

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the SOUND type.",
 "type": "integer",
 "value": 1
}
```


## constants/INVENTORY_TEXTURE

```json
{
 "member-of": [
  "InventoryType"
 ],
 "tooltip": "Used with inventory functions to filter or retrieve items of the TEXTURE type.",
 "type": "integer",
 "value": 0
}
```


## constants/JSON_APPEND

```json
{
 "slua-deprecated": {
  "reason": "Use 'lljson.decode' and 'table.insert' instead."
 },
 "tooltip": "A specifier for llJsonSetValue indicating the given value should be appended to the array at the specified level. If the target value is not an array, the existing data will be overwritten and replaced by the new array.",
 "type": "integer",
 "value": -1
}
```


## constants/JSON_ARRAY

```json
{
 "slua-deprecated": {
  "use": "lljson.array_mt"
 },
 "tooltip": "Used with llList2Json to indicate that the provided list should be encoded and returned as a string-serialized JSON array.",
 "type": "string",
 "value": "\\u{FDD2}"
}
```


## constants/JSON_DELETE

```json
{
 "slua-deprecated": {
  "use": "nil"
 },
 "tooltip": "A constant used to delete a value within a JSON text string.",
 "type": "string",
 "value": "\\u{FDD8}"
}
```


## constants/JSON_FALSE

```json
{
 "slua-deprecated": {
  "use": "false"
 },
 "tooltip": "Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a boolean FALSE.",
 "type": "string",
 "value": "\\u{FDD7}"
}
```


## constants/JSON_INVALID

```json
{
 "slua-deprecated": {
  "use": "pcall"
 },
 "tooltip": "Indicates an invalid state or parameter. Returned by llList2Json when inputs are not well-formed, by llJsonValueType for an invalid JSON type, or by llJsonGetValue when attempting to access a nonexistent location.",
 "type": "string",
 "value": "\\u{FDD0}"
}
```


## constants/JSON_NULL

```json
{
 "slua-deprecated": {
  "use": "lljson.null"
 },
 "tooltip": "Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a JSON null.",
 "type": "string",
 "value": "\\u{FDD5}"
}
```


## constants/JSON_NUMBER

```json
{
 "slua-deprecated": {
  "use": "typeof"
 },
 "tooltip": "Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a number.",
 "type": "string",
 "value": "\\u{FDD3}"
}
```


## constants/JSON_OBJECT

```json
{
 "slua-deprecated": {
  "use": "lljson.object_mt"
 },
 "tooltip": "Used with llList2Json to indicate that the provided list is a strided list of key-value pairs to be encoded and returned as a JSON object.",
 "type": "string",
 "value": "\\u{FDD1}"
}
```


## constants/JSON_STRING

```json
{
 "slua-deprecated": {
  "use": "typeof"
 },
 "tooltip": "Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a string.",
 "type": "string",
 "value": "\\u{FDD4}"
}
```


## constants/JSON_TRUE

```json
{
 "slua-deprecated": {
  "use": "true"
 },
 "tooltip": "Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a boolean TRUE.",
 "type": "string",
 "value": "\\u{FDD6}"
}
```


## constants/KFM_CMD_PAUSE

```json
{
 "member-of": [
  "KeyframedMotionCommand"
 ],
 "tooltip": "Command used with KFM_COMMAND in llSetKeyframedMotion to pause the keyframed motion without resetting it to the start.",
 "type": "integer",
 "value": 2
}
```


## constants/KFM_CMD_PLAY

```json
{
 "member-of": [
  "KeyframedMotionCommand"
 ],
 "tooltip": "Command used with KFM_COMMAND in llSetKeyframedMotion to resume a motion previously stopped by KFM_CMD_STOP or paused by KFM_CMD_PAUSE.",
 "type": "integer",
 "value": 0
}
```


## constants/KFM_CMD_STOP

```json
{
 "member-of": [
  "KeyframedMotionCommand"
 ],
 "tooltip": "Command used with KFM_COMMAND in llSetKeyframedMotion to stop the keyframed motion and reset it to the start.",
 "type": "integer",
 "value": 1
}
```


## constants/KFM_COMMAND

```json
{
 "member-of": [
  "KeyframedMotionParam"
 ],
 "tooltip": "Option flag in llSetKeyframedMotion followed by KFM_CMD_STOP, KFM_CMD_PLAY, or KFM_CMD_PAUSE to play, stop, or pause the motion.",
 "type": "integer",
 "value": 0,
 "value-type": "integer",
 "enum": "KeyframedMotionCommand"
}
```


## constants/KFM_DATA

```json
{
 "member-of": [
  "KeyframedMotionParam"
 ],
 "tooltip": "Option flag in llSetKeyframedMotion followed by a bitwise combination of KFM_TRANSLATION and KFM_ROTATION to specify keyframe data. If absent, both rotation and translation data must be provided.",
 "type": "integer",
 "value": 2,
 "value-type": "integer",
 "enum": "KeyframedMotionData",
 "default": "KFM_ROTATION | KFM_TRANSLATION"
}
```


## constants/KFM_FORWARD

```json
{
 "member-of": [
  "KeyframedMotionMode"
 ],
 "tooltip": "Playback mode used with KFM_MODE in llSetKeyframedMotion (default). It plays the frames sequentially from 1 to N and then stops.",
 "type": "integer",
 "value": 0
}
```


## constants/KFM_LOOP

```json
{
 "member-of": [
  "KeyframedMotionMode"
 ],
 "tooltip": "Playback mode used with KFM_MODE in llSetKeyframedMotion. It plays the frames sequentially from 1 to N, returns to the initial position, and repeats indefinitely.",
 "type": "integer",
 "value": 1
}
```


## constants/KFM_MODE

```json
{
 "member-of": [
  "KeyframedMotionParam"
 ],
 "tooltip": "Option flag in llSetKeyframedMotion followed by KFM_LOOP, KFM_REVERSE, KFM_FORWARD, or KFM_PING_PONG to set the playback mode (defaults to KFM_FORWARD). Must be specified when the keyframe list is provided.",
 "type": "integer",
 "value": 1,
 "value-type": "integer",
 "enum": "KeyframedMotionMode",
 "default": "KFM_FORWARD"
}
```


## constants/KFM_PING_PONG

```json
{
 "member-of": [
  "KeyframedMotionMode"
 ],
 "tooltip": "Playback mode used with KFM_MODE in llSetKeyframedMotion.",
 "type": "integer",
 "value": 2
}
```


## constants/KFM_REVERSE

```json
{
 "member-of": [
  "KeyframedMotionMode"
 ],
 "tooltip": "Playback mode used with KFM_MODE in llSetKeyframedMotion. It plays the frames in reverse order (from N down to 1) and then stops.",
 "type": "integer",
 "value": 3
}
```


## constants/KFM_ROTATION

```json
{
 "member-of": [
  "KeyframedMotionData"
 ],
 "tooltip": "Specifies that rotation data is included in the moves list for llSetKeyframedMotion.",
 "type": "integer",
 "value": 1
}
```


## constants/KFM_TRANSLATION

```json
{
 "member-of": [
  "KeyframedMotionData"
 ],
 "tooltip": "Specifies that translation data is included in the moves list for llSetKeyframedMotion.",
 "type": "integer",
 "value": 2
}
```


## constants/LAND_BRUSH_LARGE

```json
{
 "member-of": [
  "ModifyLandBrush"
 ],
 "tooltip": "Use a large brush size (8m x 8m).",
 "type": "integer",
 "value": 2
}
```


## constants/LAND_BRUSH_MEDIUM

```json
{
 "member-of": [
  "ModifyLandBrush"
 ],
 "tooltip": "Use a medium brush size (4m x 4m)..",
 "type": "integer",
 "value": 1
}
```


## constants/LAND_BRUSH_SMALL

```json
{
 "member-of": [
  "ModifyLandBrush"
 ],
 "tooltip": "Use a small brush size (2m x 2m).",
 "type": "integer",
 "value": 0
}
```


## constants/LAND_LARGE_BRUSH

```json
{
 "member-of": [
  "ModifyLandBrush"
 ],
 "deprecated": {
  "use": "LAND_BRUSH_LARGE"
 },
 "tooltip": "Legacy large brush size (8m x 8m). Note: This constant value is incorrect; use LAND_BRUSH_LARGE instead.",
 "type": "integer",
 "value": 3
}
```


## constants/LAND_LEVEL

```json
{
 "member-of": [
  "ModifyLandAction"
 ],
 "tooltip": "Action used with llModifyLand to level the land at the prim's center.",
 "type": "integer",
 "value": 0
}
```


## constants/LAND_LOWER

```json
{
 "member-of": [
  "ModifyLandAction"
 ],
 "tooltip": "Action used with llModifyLand to lower the land.",
 "type": "integer",
 "value": 2
}
```


## constants/LAND_MEDIUM_BRUSH

```json
{
 "member-of": [
  "ModifyLandBrush"
 ],
 "deprecated": {
  "use": "LAND_BRUSH_MEDIUM"
 },
 "tooltip": "Legacy medium brush size (4m x 4m). Note: This constant value is incorrect; use LAND_BRUSH_MEDIUM instead.",
 "type": "integer",
 "value": 2
}
```


## constants/LAND_NOISE

```json
{
 "member-of": [
  "ModifyLandAction"
 ],
 "tooltip": "Action used with llModifyLand to randomize the terrain and make it rough.",
 "type": "integer",
 "value": 4
}
```


## constants/LAND_RAISE

```json
{
 "member-of": [
  "ModifyLandAction"
 ],
 "tooltip": "Action used with llModifyLand to raise the land.",
 "type": "integer",
 "value": 1
}
```


## constants/LAND_REVERT

```json
{
 "member-of": [
  "ModifyLandAction"
 ],
 "tooltip": "Action used with llModifyLand to restore the land to its baked value.",
 "type": "integer",
 "value": 5
}
```


## constants/LAND_SMALL_BRUSH

```json
{
 "member-of": [
  "ModifyLandBrush"
 ],
 "deprecated": {
  "use": "LAND_BRUSH_SMALL"
 },
 "tooltip": "Legacy small brush size (2m x 2m). Note: This constant value is incorrect; use LAND_BRUSH_SMALL instead.",
 "type": "integer",
 "value": 1
}
```


## constants/LAND_SMOOTH

```json
{
 "member-of": [
  "ModifyLandAction"
 ],
 "tooltip": "Action used with llModifyLand to smooth the land.",
 "type": "integer",
 "value": 3
}
```


## constants/LEGACY_MASS_FACTOR

```json
{
 "private": true,
 "tooltip": "",
 "type": "float",
 "value": "0.01"
}
```


## constants/LINKSETDATA_DELETE

```json
{
 "member-of": [
  "LinksetDataAction"
 ],
 "tooltip": "Action indicating a key was deleted from the linkset datastore via llLinksetDataDelete, llLinksetDataDeleteProtected, or by writing an empty value.",
 "type": "integer",
 "value": 2
}
```


## constants/LINKSETDATA_EMEMORY

```json
{
 "member-of": [
  "LinksetDataError"
 ],
 "tooltip": "Error code indicating the key and value were too large to write to the linkset datastore.",
 "type": "integer",
 "value": 1
}
```


## constants/LINKSETDATA_ENOKEY

```json
{
 "member-of": [
  "LinksetDataError"
 ],
 "tooltip": "Error code indicating the key name supplied to a linkset datastore operation was empty.",
 "type": "integer",
 "value": 2
}
```


## constants/LINKSETDATA_EPROTECTED

```json
{
 "member-of": [
  "LinksetDataError"
 ],
 "tooltip": "Error code indicating the key is protected from being deleted or overwritten in the linkset datastore.",
 "type": "integer",
 "value": 3
}
```


## constants/LINKSETDATA_MULTIDELETE

```json
{
 "member-of": [
  "LinksetDataAction"
 ],
 "tooltip": "Action indicating keys were deleted from the linkset datastore via llLinksetDataDeleteFound. The event's name is a comma-separated list of the deleted keys.",
 "type": "integer",
 "value": 3
}
```


## constants/LINKSETDATA_NOTFOUND

```json
{
 "member-of": [
  "LinksetDataError"
 ],
 "tooltip": "Error code indicating the specified key could not be found in the linkset datastore.",
 "type": "integer",
 "value": 4
}
```


## constants/LINKSETDATA_NOUPDATE

```json
{
 "member-of": [
  "LinksetDataError"
 ],
 "tooltip": "Status code indicating that the linkset datastore was not updated because the written value matched the existing stored value.",
 "type": "integer",
 "value": 5
}
```


## constants/LINKSETDATA_OK

```json
{
 "member-of": [
  "LinksetDataError"
 ],
 "tooltip": "Status code indicating the linkset datastore operation completed successfully.",
 "type": "integer",
 "value": 0
}
```


## constants/LINKSETDATA_RESET

```json
{
 "member-of": [
  "LinksetDataAction"
 ],
 "tooltip": "Action indicating all keys were deleted from the linkset datastore via llLinksetDataReset.",
 "type": "integer",
 "value": 0
}
```


## constants/LINKSETDATA_UPDATE

```json
{
 "member-of": [
  "LinksetDataAction"
 ],
 "tooltip": "Action indicating a key was created or updated in the linkset datastore via llLinksetDataWrite or llLinksetDataWriteProtected.",
 "type": "integer",
 "value": 1
}
```


## constants/LINK_ALL_CHILDREN

```json
{
 "member-of": [
  "Links"
 ],
 "tooltip": "Refers to all child prims in the linkset (every prim except the root).",
 "type": "integer",
 "value": -3
}
```


## constants/LINK_ALL_OTHERS

```json
{
 "member-of": [
  "Links"
 ],
 "tooltip": "Refers to every other prim in the linkset, excluding the prim containing the script.",
 "type": "integer",
 "value": -2
}
```


## constants/LINK_ROOT

```json
{
 "member-of": [
  "Link",
  "Links"
 ],
 "tooltip": "Refers to the root prim of the linkset.",
 "type": "integer",
 "value": 1
}
```


## constants/LINK_SET

```json
{
 "member-of": [
  "Links"
 ],
 "tooltip": "Refers to every prim in the linkset.",
 "type": "integer",
 "value": -1
}
```


## constants/LINK_THIS

```json
{
 "member-of": [
  "Link",
  "Links"
 ],
 "tooltip": "Refers specifically to the single prim containing the running script.",
 "type": "integer",
 "value": -4
}
```


## constants/LIST_STAT_GEOMETRIC_MEAN

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to calculate the geometric mean of a list of numbers.",
 "type": "integer",
 "value": 9
}
```


## constants/LIST_STAT_MAX

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to find the largest number in the list.",
 "type": "integer",
 "value": 2
}
```


## constants/LIST_STAT_MEAN

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to calculate the mean (average) of the numbers in the list.",
 "type": "integer",
 "value": 3
}
```


## constants/LIST_STAT_MEDIAN

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to calculate the median of the numbers in the list.",
 "type": "integer",
 "value": 4
}
```


## constants/LIST_STAT_MIN

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to find the smallest number in the list.",
 "type": "integer",
 "value": 1
}
```


## constants/LIST_STAT_NUM_COUNT

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to determine the count of float and integer elements in the list.",
 "type": "integer",
 "value": 8
}
```


## constants/LIST_STAT_RANGE

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to calculate the range (maximum value minus minimum value) of the list.",
 "type": "integer",
 "value": 0
}
```


## constants/LIST_STAT_STD_DEV

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to calculate the sample standard deviation of a list of numbers.",
 "type": "integer",
 "value": 5
}
```


## constants/LIST_STAT_SUM

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to calculate the sum of the numbers in the list.",
 "type": "integer",
 "value": 6
}
```


## constants/LIST_STAT_SUM_SQUARES

```json
{
 "member-of": [
  "ListStatisticsOperation"
 ],
 "tooltip": "Option used with llListStatistics to calculate the sum of the squares of the numbers in the list.",
 "type": "integer",
 "value": 7
}
```


## constants/LOOP

```json
{
 "member-of": [
  "TextureAnimMode"
 ],
 "tooltip": "Used with texture animation functions to cause the animation to loop continuously.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/MASK_BASE

```json
{
 "member-of": [
  "AssetPermissionCategory"
 ],
 "tooltip": "Permissions mask option representing base permissions.",
 "type": "integer",
 "value": 0
}
```


## constants/MASK_COMBINED

```json
{
 "member-of": [
  "AssetPermissionCategoryFlag"
 ],
 "tooltip": "Permissions mask option to include the object's inventory contents when calculating permissions. Can be combined with other mask flags (e.g., MASK_OWNER | MASK_COMBINED).",
 "type": "integer",
 "value": "0x10"
}
```


## constants/MASK_EVERYONE

```json
{
 "member-of": [
  "AssetPermissionCategory"
 ],
 "tooltip": "Permissions mask option representing permissions held by everyone.",
 "type": "integer",
 "value": 3
}
```


## constants/MASK_GROUP

```json
{
 "member-of": [
  "AssetPermissionCategory"
 ],
 "tooltip": "Permissions mask option representing active group permissions.",
 "type": "integer",
 "value": 2
}
```


## constants/MASK_NEXT

```json
{
 "member-of": [
  "AssetPermissionCategory"
 ],
 "tooltip": "Permissions mask option representing permissions the next owner will inherit.",
 "type": "integer",
 "value": 4
}
```


## constants/MASK_OWNER

```json
{
 "member-of": [
  "AssetPermissionCategory"
 ],
 "tooltip": "Permissions mask option representing current owner permissions.",
 "type": "integer",
 "value": 1
}
```


## constants/NAK

```json
{
 "tooltip": "Value returned by llGetNotecardLineSync and llFindNotecardTextSync (as a single-entry list) when the notecard is not in the region's cache. Equal to an ASCII NAK surrounded by newlines (codes 10, 21, 10).",
 "type": "string",
 "value": "\\n\\x15\\n"
}
```


## constants/NAVIGATE_TO_GOAL_REACHED_DIST

```json
{
 "member-of": [
  "CharacterNavigateParam"
 ],
 "private": true,
 "tooltip": "",
 "type": "integer",
 "value": 2,
 "value-type": "float",
 "range": [
  0.1,
  10
 ]
}
```


## constants/NULL_KEY

```json
{
 "tooltip": "A special string constant used as a null or empty key value.",
 "type": "string",
 "slua-type": "uuid",
 "value": "00000000-0000-0000-0000-000000000000"
}
```


## constants/OBJECT_ACCOUNT_LEVEL

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve an avatar's account level. Returns 0 for Basic, 1 for Premium, 5 for Plus, 10 for Premium Plus, or -1 if the target is not an avatar.",
 "type": "integer",
 "value": 41,
 "value-type": "integer",
 "details": "Max.length: 1"
}
```


## constants/OBJECT_ANIMATED_COUNT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails. For an object, returns a boolean indicating if the root is set as 'Animated Mesh'. For an agent, returns the total number of 'Animated Mesh' attachments worn.",
 "type": "integer",
 "value": 39,
 "value-type": "integer",
 "details": "Max.length: 1"
}
```


## constants/OBJECT_ANIMATED_SLOTS_AVAILABLE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the avatar's available 'Animated Mesh' attachment slot count (returns 0 if the ID is not an avatar).",
 "type": "integer",
 "value": 40,
 "value-type": "integer",
 "details": "Max.length: 2"
}
```


## constants/OBJECT_ATTACHED_POINT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails. Returns the integer attachment point matching an ATTACH_* constant, or 0 if the target is not an attachment (e.g., an avatar or unattached object).",
 "type": "integer",
 "value": 19,
 "value-type": "integer",
 "enum": "AttachPoint",
 "details": "Local: llGetAttached   Max.length: 11"
}
```


## constants/OBJECT_ATTACHED_SLOTS_AVAILABLE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get an avatar's available attachment slot count. Returns 0 if the ID is not an avatar or if no slots are available.",
 "type": "integer",
 "value": 35,
 "value-type": "integer",
 "details": "Max.length: 2"
}
```


## constants/OBJECT_BODY_SHAPE_TYPE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve a float representing the gender/sex setting of an avatar's shape (0.0 is standard female, 1.0 is standard male, and values greater than or equal to 0.5 are considered male). Returns -1.0 if not an avatar or if no data is available.",
 "type": "integer",
 "value": 26,
 "value-type": "float",
 "range": [
  0,
  1
 ],
 "details": "Max.length: 9"
}
```


## constants/OBJECT_CHARACTER_TIME

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the average CPU time (in seconds) spent on navigation if the target is a pathfinding character. Returns 0 for non-characters.",
 "type": "integer",
 "value": 17,
 "value-type": "float",
 "details": "Alternatives: Pathfinding characters   Max.length: 15"
}
```


## constants/OBJECT_CLICK_ACTION

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the click action of a prim. Returns an integer corresponding to a CLICK_ACTION_* constant (default is 0).",
 "type": "integer",
 "value": 28,
 "value-type": "integer",
 "enum": "ClickAction",
 "details": "Max.length: 3"
}
```


## constants/OBJECT_CREATION_TIME

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the object's creation time (established via build-menu rezzing or mesh uploads, not via inventory/script rezzes, copying, or modifying). Returns an empty string for avatars.",
 "type": "integer",
 "value": 36,
 "value-type": "string",
 "details": "Max.length: 27"
}
```


## constants/OBJECT_CREATOR

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the key of the prim's creator. Returns NULL_KEY if the ID is an avatar.",
 "type": "integer",
 "value": 8,
 "value-type": "key",
 "details": "Local: llGetCreator   Alternatives: Creator   Max.length: 36"
}
```


## constants/OBJECT_DAMAGE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the amount of damage a prim inflicts upon collision.",
 "type": "integer",
 "value": 51,
 "value-type": "float",
 "details": "Local: llGetPrimitiveParams and PRIM_DAMAGE"
}
```


## constants/OBJECT_DAMAGE_TYPE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the type of damage a prim inflicts on collision. Returns an integer matching a DAMAGE_TYPE_* constant, a custom type, or a value repurposed by a combat system.",
 "type": "integer",
 "value": 52,
 "value-type": "integer",
 "enum": "DamageType",
 "details": "Local: llGetPrimitiveParams and PRIM_DAMAGE"
}
```


## constants/OBJECT_DESC

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the prim's description. Returns an empty string if the ID is an avatar.",
 "type": "integer",
 "value": 2,
 "value-type": "string",
 "details": "Local: llGetObjectDesc   Max.length: 127"
}
```


## constants/OBJECT_GROUP

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the prim's group key. Returns NULL_KEY if the target is an avatar (which means a workaround is required to get an avatar's active group).",
 "type": "integer",
 "value": 7,
 "value-type": "key",
 "details": "Alternatives: Group   Max.length: 36"
}
```


## constants/OBJECT_GROUP_TAG

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get an avatar's active group tag/title. Returns an empty string if the target is not an avatar.",
 "type": "integer",
 "value": 33,
 "value-type": "string",
 "details": "Max.length: 20"
}
```


## constants/OBJECT_HEALTH

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the current health value of an avatar or prim.",
 "type": "integer",
 "value": 50,
 "value-type": "float",
 "details": "Local: llGetPrimitiveParams and PRIM_HEALTH / llGetHealth"
}
```


## constants/OBJECT_HOVER_HEIGHT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the dynamic hover height of an avatar (default is 0.0). Returns 0.0 if not an avatar or if no data is available; does not reflect the shape's 'Hover' slider.",
 "type": "integer",
 "value": 25,
 "value-type": "float",
 "range": [
  -2,
  2
 ],
 "details": "Max.length: 9"
}
```


## constants/OBJECT_LAST_OWNER_ID

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the key of the previous owner. For group-owned objects, returns the avatar who deeded it. Returns NULL_KEY for avatars, untransferred objects, or objects taken to inventory and re-rezzed.",
 "type": "integer",
 "value": 27,
 "value-type": "key",
 "details": "Max.length: 36"
}
```


## constants/OBJECT_LINK_NUMBER

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the index of the prim within its linkset, or 0 if unlinked.",
 "type": "integer",
 "value": 46,
 "value-type": "integer",
 "details": "Local: llGetLinkNumber"
}
```


## constants/OBJECT_LOCKED

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get a boolean, indicating if the object is locked.",
 "type": "integer",
 "value": 55,
 "value-type": "boolean"
}
```


## constants/OBJECT_MASS

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the total mass (in kilograms) of the object's linkset.",
 "type": "integer",
 "value": 43,
 "value-type": "float",
 "details": "Local: llGetMassMKS"
}
```


## constants/OBJECT_MATERIAL

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the physics material of the object, returning an integer matching a PRIM_MATERIAL_* constant.",
 "type": "integer",
 "value": 42,
 "value-type": "integer",
 "enum": "PhysicsMaterialPreset",
 "details": "Local: llGetPrimitiveParams and PRIM_MATERIAL"
}
```


## constants/OBJECT_NAME

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the prim's name, or the legacy name if the target is an avatar.",
 "type": "integer",
 "value": 1,
 "value-type": "string",
 "details": "Local: llGetObjectName   Alternatives: llKey2Name / llDetectedName   Max.length: 63"
}
```


## constants/OBJECT_OMEGA

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the rotational (angular) velocity of an object in radians per second.",
 "type": "integer",
 "value": 29,
 "value-type": "vector",
 "details": "Local: llGetOmega   Max.length: 36"
}
```


## constants/OBJECT_OWNER

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the owner's key. If the target is an avatar, their own key is returned. If group-owned, it returns NULL_KEY.",
 "type": "integer",
 "value": 6,
 "value-type": "key",
 "details": "Local: llGetOwner   Alternatives: llDetectedOwner / llGetOwnerKey   Max.length: 36"
}
```


## constants/OBJECT_PATHFINDING_TYPE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the pathfinding setting of an object in the region, returning an integer matching an OPT_* constant.",
 "type": "integer",
 "value": 20,
 "value-type": "integer",
 "enum": "ObjectPathfindingType",
 "details": "Alternatives: Pathfinding types   Max.length: 11"
}
```


## constants/OBJECT_PERMS

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the permissions of the object as five integers.",
 "type": "integer",
 "value": 53,
 "values": [
  {
   "name": "base",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "owner",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "group",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "everyone",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "next_owner",
   "value-type": "integer",
   "enum": "AssetPermission"
  }
 ],
 "details": "Local: llGetObjectPermMask"
}
```


## constants/OBJECT_PERMS_COMBINED

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the permissions of the object combined with all of its inventory items as five integers.",
 "type": "integer",
 "value": 54,
 "values": [
  {
   "name": "base",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "owner",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "group",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "everyone",
   "value-type": "integer",
   "enum": "AssetPermission"
  },
  {
   "name": "next_owner",
   "value-type": "integer",
   "enum": "AssetPermission"
  }
 ],
 "details": "Local: llGetObjectPermMask"
}
```


## constants/OBJECT_PHANTOM

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get a boolean indicating if phantom is enabled on the object. Returns 0 if the target is an avatar or attachment.",
 "type": "integer",
 "value": 22,
 "value-type": "boolean",
 "details": "Local: llGetStatus PRIM_PHANTOM   Max.length: 1"
}
```


## constants/OBJECT_PHYSICS

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get a boolean indicating if physics is enabled on the object. Returns 0 if the target is an avatar or attachment.",
 "type": "integer",
 "value": 21,
 "value-type": "boolean",
 "details": "Local: llGetStatus PRIM_PHYSICS   Max.length: 1"
}
```


## constants/OBJECT_PHYSICS_COST

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the physics cost of the object.",
 "type": "integer",
 "value": 16,
 "value-type": "float",
 "details": "Alternatives: Physics cost   Max.length: 15"
}
```


## constants/OBJECT_POS

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the prim's position in region coordinates. For an avatar outside the region, the returned position is relative to the script's region.",
 "type": "integer",
 "value": 3,
 "value-type": "vector",
 "details": "Local: llGetPos   Alternatives: llDetectedPos   Max.length: 37"
}
```


## constants/OBJECT_PRIM_COUNT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the prim count of the object. Note that the script and target object must be owned by the same owner.",
 "type": "integer",
 "value": 30,
 "value-type": "integer",
 "details": "Local: llGetNumberOfPrims   Alternatives: llGetObjectPrimCount   Max.length: 3"
}
```


## constants/OBJECT_PRIM_EQUIVALENCE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the prim equivalence of the object.",
 "type": "integer",
 "value": 13,
 "value-type": "integer",
 "details": "Alternatives: Calculating land impact   Max.length: 11"
}
```


## constants/OBJECT_RENDER_WEIGHT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the render weight (Avatar Rendering Cost) of an avatar based on viewer reports. Returns 0 for objects, -1 if unknown, and is capped at 500,000.",
 "type": "integer",
 "value": 24,
 "value-type": "integer",
 "range": [
  0,
  500000
 ],
 "details": "Alternatives: Avatar_Rendering_Cost   Max.length: 6"
}
```


## constants/OBJECT_RETURN_PARCEL

```json
{
 "member-of": [
  "ReturnObjectsScope"
 ],
 "tooltip": "Scope flag used with llReturnObjectsByOwner to return all objects on the same parcel as the script owned by the specified owner. Requires the script owner to be an estate manager or the parcel owner.",
 "type": "integer",
 "value": 1
}
```


## constants/OBJECT_RETURN_PARCEL_OWNER

```json
{
 "member-of": [
  "ReturnObjectsScope"
 ],
 "tooltip": "Scope flag used with llReturnObjectsByOwner to return all objects owned by the specified owner that are located on parcels owned by the script's owner.",
 "type": "integer",
 "value": 2
}
```


## constants/OBJECT_RETURN_REGION

```json
{
 "member-of": [
  "ReturnObjectsScope"
 ],
 "tooltip": "Scope flag used with llReturnObjectsByOwner to return all objects in the region owned by the specified owner. Only works if the script is owned by the estate owner or an estate manager.",
 "type": "integer",
 "value": 4
}
```


## constants/OBJECT_REZZER_KEY

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the key of the object or avatar that rezzed the target object.",
 "type": "integer",
 "value": 32,
 "value-type": "key",
 "details": "Max.length: 36"
}
```


## constants/OBJECT_REZ_TIME

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to retrieve the timestamp of when the object was rezzed.",
 "type": "integer",
 "value": 45,
 "value-type": "string"
}
```


## constants/OBJECT_ROOT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the ID of the root prim. For an avatar, returns the root prim of the linkset they are sitting on (or the avatar's own ID if not sitting).",
 "type": "integer",
 "value": 18,
 "value-type": "key",
 "details": "Local: llGetLinkKey   Max.length: 36"
}
```


## constants/OBJECT_ROT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the prim's rotation.",
 "type": "integer",
 "value": 4,
 "value-type": "rotation",
 "details": "Local: llGetRot   Alternatives: llDetectedRot   Max.length: 48"
}
```


## constants/OBJECT_RUNNING_SCRIPT_COUNT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the total number of running scripts attached to the target object or agent.",
 "type": "integer",
 "value": 9,
 "value-type": "integer",
 "details": "Local: llGetScriptState   Max.length: 11"
}
```


## constants/OBJECT_SCALE

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the size (scale) of the object.",
 "type": "integer",
 "value": 47,
 "value-type": "vector",
 "details": "Local: llGetScale"
}
```


## constants/OBJECT_SCRIPT_MEMORY

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the allocated script memory (or its upper limit) in bytes for the object or agent. This value is recomputed every 10-20 seconds.",
 "type": "integer",
 "value": 11,
 "value-type": "integer",
 "details": "Max.length: 11"
}
```


## constants/OBJECT_SCRIPT_TIME

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the average script CPU time (in seconds) used per frame. Reports a 30-minute average, or the average since entering the region if present for less than 30 minutes.",
 "type": "integer",
 "value": 12,
 "value-type": "float",
 "details": "Alternatives: Top Scripts   Max.length: 15"
}
```


## constants/OBJECT_SELECT_COUNT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the total number of agents/avatars actively selecting any link in the object. Returns 0 if the target is an avatar.",
 "type": "integer",
 "value": 37,
 "value-type": "integer",
 "details": "Max.length: 3"
}
```


## constants/OBJECT_SERVER_COST

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the server cost of the object.",
 "type": "integer",
 "value": 14,
 "value-type": "float",
 "details": "Alternatives: Server cost   Max.length: 15"
}
```


## constants/OBJECT_SIT_COUNT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the total number of agents sitting on any links in the object. Returns 0 if the target is an avatar.",
 "type": "integer",
 "value": 38,
 "value-type": "integer",
 "details": "Max.length: 3"
}
```


## constants/OBJECT_STREAMING_COST

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the streaming (download) cost of the object.",
 "type": "integer",
 "value": 15,
 "value-type": "float",
 "details": "Alternatives: Streaming (download) cost   Max.length: 15"
}
```


## constants/OBJECT_TEMP_ATTACHED

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get a boolean indicating whether the object is temporarily attached.",
 "type": "integer",
 "value": 34,
 "value-type": "boolean",
 "details": "Max.length: 1"
}
```


## constants/OBJECT_TEMP_ON_REZ

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get a boolean indicating if temporary-on-rez is enabled for the object.",
 "type": "integer",
 "value": 23,
 "value-type": "boolean",
 "details": "Local: PRIM_TEMP_ON_REZ   Max.length: 1"
}
```


## constants/OBJECT_TEXT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the floating (hover) text displayed above the object.",
 "type": "integer",
 "value": 44,
 "value-type": "string",
 "details": "Local: llGetPrimitiveParams and PRIM_TEXT"
}
```


## constants/OBJECT_TEXT_ALPHA

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the alpha value of the floating (hover) text displayed above the object.",
 "type": "integer",
 "value": 49,
 "value-type": "float",
 "details": "Local: llGetPrimitiveParams and PRIM_TEXT"
}
```


## constants/OBJECT_TEXT_COLOR

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the color vector of the floating (hover) text displayed above the object.",
 "type": "integer",
 "value": 48,
 "value-type": "vector",
 "details": "Local: llGetPrimitiveParams and PRIM_TEXT"
}
```


## constants/OBJECT_TOTAL_INVENTORY_COUNT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the total number of inventory items inside the object. Requires the script and target object to share the same owner.",
 "type": "integer",
 "value": 31,
 "value-type": "integer",
 "details": "Local: llGetInventoryNumber(INVENTORY_ALL)   Max.length: 10"
}
```


## constants/OBJECT_TOTAL_SCRIPT_COUNT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the total number of scripts (both running and stopped) attached to the target object or agent.",
 "type": "integer",
 "value": 10,
 "value-type": "integer",
 "details": "Local: llGetInventoryNumber   Max.length: 11"
}
```


## constants/OBJECT_UNKNOWN_DETAIL

```json
{
 "tooltip": "Flag returned by llGetObjectDetails when an invalid flag is requested.",
 "type": "integer",
 "value": -1
}
```


## constants/OBJECT_VELOCITY

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get the velocity vector of the target object.",
 "type": "integer",
 "value": 5,
 "value-type": "vector",
 "details": "Local: llGetVel   Alternatives: llDetectedVel   Max.length: 36"
}
```


## constants/OBJECT_VOLUME_DETECT

```json
{
 "member-of": [
  "ObjectDetailsParam"
 ],
 "tooltip": "Flag used with llGetObjectDetails to get a boolean, indicating if the object is VolumeDetect.",
 "type": "integer",
 "value": 56,
 "value-type": "boolean"
}
```


## constants/OPT_AVATAR

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for avatars.",
 "type": "integer",
 "value": 1
}
```


## constants/OPT_CHARACTER

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for pathfinding characters.",
 "type": "integer",
 "value": 2
}
```


## constants/OPT_EXCLUSION_VOLUME

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for exclusion volumes.",
 "type": "integer",
 "value": 6
}
```


## constants/OPT_LEGACY_LINKSET

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for movable obstacles, movable phantoms, physical, and volumedetect objects.",
 "type": "integer",
 "value": 0
}
```


## constants/OPT_MATERIAL_VOLUME

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for material volumes.",
 "type": "integer",
 "value": 5
}
```


## constants/OPT_OTHER

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for attachments, Linden trees, and grass.",
 "type": "integer",
 "value": -1
}
```


## constants/OPT_STATIC_OBSTACLE

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for static obstacles.",
 "type": "integer",
 "value": 4
}
```


## constants/OPT_WALKABLE

```json
{
 "member-of": [
  "ObjectPathfindingType"
 ],
 "tooltip": "Returned for walkable objects.",
 "type": "integer",
 "value": 3
}
```


## constants/OVERRIDE_GLTF_BASE_ALPHA

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides to set the alpha for the face(s). Only impacts rendering when the alpha mode is set to PRIM_GLTF_ALPHA_MODE_BLEND.",
 "type": "integer",
 "value": 2,
 "value-type": "float"
}
```


## constants/OVERRIDE_GLTF_BASE_ALPHA_MASK

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides to set the alpha cutoff level on the face(s) when the alpha mode is set to mask.",
 "type": "integer",
 "value": 4,
 "value-type": "float"
}
```


## constants/OVERRIDE_GLTF_BASE_ALPHA_MODE

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides to set the alpha mode on the face(s) to one of the valid blend modes.",
 "type": "integer",
 "value": 3,
 "value-type": "integer",
 "enum": "GLTFAlphaMode"
}
```


## constants/OVERRIDE_GLTF_BASE_COLOR_FACTOR

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "pretty-name": "color",
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides to set the tinting color (specified in linear RGB) used for the base color. Use llsRGB2Linear to convert colors from Blinn-Phong to PBR.",
 "type": "integer",
 "value": 1,
 "value-type": "vector"
}
```


## constants/OVERRIDE_GLTF_BASE_DOUBLE_SIDED

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides. If set to TRUE, the texture on the face(s) will be rendered as double-sided.",
 "type": "integer",
 "value": 5,
 "value-type": "boolean"
}
```


## constants/OVERRIDE_GLTF_EMISSIVE_FACTOR

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "pretty-name": "emmissive_color",
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides to set the tint (specified in linear RGB) used for the emissive texture on the face(s).",
 "type": "integer",
 "value": 8,
 "value-type": "vector"
}
```


## constants/OVERRIDE_GLTF_METALLIC_FACTOR

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "pretty-name": "metalness",
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides to adjust the metallic factor on the specified face(s) to a value between 0 and 1.",
 "type": "integer",
 "value": 6,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/OVERRIDE_GLTF_ROUGHNESS_FACTOR

```json
{
 "member-of": [
  "GLTFOverride"
 ],
 "pretty-name": "roughness",
 "tooltip": "GLTF override setting used with llSetLinkGLTFOverrides to adjust the roughness factor on the specified face(s) to a value between 0 and 1.",
 "type": "integer",
 "value": 7,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/PARCEL_COUNT_GROUP

```json
{
 "member-of": [
  "ParcelPrimCountCategory"
 ],
 "tooltip": "Used with llGetParcelPrimCount to get the total land impact of objects not owned by the parcel owner but set to or owned by the parcel's group.",
 "type": "integer",
 "value": 2
}
```


## constants/PARCEL_COUNT_OTHER

```json
{
 "member-of": [
  "ParcelPrimCountCategory"
 ],
 "tooltip": "Used with llGetParcelPrimCount to get the land impact of all objects that are neither owned by the parcel owner nor set to or owned by the parcel's group.",
 "type": "integer",
 "value": 3
}
```


## constants/PARCEL_COUNT_OWNER

```json
{
 "member-of": [
  "ParcelPrimCountCategory"
 ],
 "tooltip": "Used with llGetParcelPrimCount to get the total land impact of objects owned by the parcel owner.",
 "type": "integer",
 "value": 1
}
```


## constants/PARCEL_COUNT_SELECTED

```json
{
 "member-of": [
  "ParcelPrimCountCategory"
 ],
 "tooltip": "Used with llGetParcelPrimCount to get the total land impact of all objects currently selected or sat on.",
 "type": "integer",
 "value": 4
}
```


## constants/PARCEL_COUNT_TEMP

```json
{
 "member-of": [
  "ParcelPrimCountCategory"
 ],
 "tooltip": "Used with llGetParcelPrimCount to get the total land impact of temporary (temp-on-rez) objects.",
 "type": "integer",
 "value": 5
}
```


## constants/PARCEL_COUNT_TOTAL

```json
{
 "member-of": [
  "ParcelPrimCountCategory"
 ],
 "tooltip": "Used with llGetParcelPrimCount to get the total land impact of all objects on the parcel(s), excluding temporary (temp-on-rez) objects.",
 "type": "integer",
 "value": 0
}
```


## constants/PARCEL_DETAILS_AREA

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the parcel's area in square meters (sqm).",
 "type": "integer",
 "value": 4,
 "value-type": "integer"
}
```


## constants/PARCEL_DETAILS_DESC

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the description of the parcel (up to 127 characters).",
 "type": "integer",
 "value": 1,
 "value-type": "string"
}
```


## constants/PARCEL_DETAILS_FLAGS

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the parcel flags set on this parcel (see llGetParcelFlags for listings and meanings).",
 "type": "integer",
 "value": 12,
 "value-type": "integer",
 "enum": "ParcelFlag"
}
```


## constants/PARCEL_DETAILS_GROUP

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the parcel group's 36-character key.",
 "type": "integer",
 "value": 3,
 "value-type": "key"
}
```


## constants/PARCEL_DETAILS_ID

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the parcel's 36-character UUID/key.",
 "type": "integer",
 "value": 5,
 "value-type": "key"
}
```


## constants/PARCEL_DETAILS_LANDING_LOOKAT

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the lookat vector set for the landing point (teleport routing) on this parcel, if any.",
 "type": "integer",
 "value": 10,
 "value-type": "vector"
}
```


## constants/PARCEL_DETAILS_LANDING_POINT

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the landing point vector set for this parcel, if any.",
 "type": "integer",
 "value": 9,
 "value-type": "vector"
}
```


## constants/PARCEL_DETAILS_NAME

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the name of the parcel (up to 63 characters).",
 "type": "integer",
 "value": 0,
 "value-type": "string"
}
```


## constants/PARCEL_DETAILS_OWNER

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the parcel owner's 36-character key.",
 "type": "integer",
 "value": 2,
 "value-type": "key"
}
```


## constants/PARCEL_DETAILS_PRIM_CAPACITY

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the total prim capacity on this and all same-owner parcels, sim-wide (see llGetParcelMaxPrims for same-parcel-only and/or sim-wide reporting).",
 "type": "integer",
 "value": 7,
 "value-type": "integer"
}
```


## constants/PARCEL_DETAILS_PRIM_USED

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the total prim usage on this and all same-owner parcels, sim-wide (see llGetParcelPrimCount to get prim counts by owner, group, or temporary status).",
 "type": "integer",
 "value": 8,
 "value-type": "integer"
}
```


## constants/PARCEL_DETAILS_SCRIPT_DANGER

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to check if the script is in danger (due to restrictions that impact script execution) on the indicated parcel; see llScriptDanger.",
 "type": "integer",
 "value": 13,
 "value-type": "boolean"
}
```


## constants/PARCEL_DETAILS_SEE_AVATARS

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the 'See and chat with residents on this parcel' avatar visibility setting.",
 "type": "integer",
 "value": 6,
 "value-type": "boolean"
}
```


## constants/PARCEL_DETAILS_TP_ROUTING

```json
{
 "member-of": [
  "ParcelDetailsParam"
 ],
 "tooltip": "Flag used with llGetParcelDetails to retrieve the teleport routing setting for this parcel (0 = TP_ROUTING_BLOCKED, 1 = TP_ROUTING_LANDINGP, 2 = TP_ROUTING_FREE; rules are only enforced if a landing point is set).",
 "type": "integer",
 "value": 11,
 "value-type": "integer",
 "enum": "ParcelTeleportRouting"
}
```


## constants/PARCEL_FLAG_ALLOW_ALL_OBJECT_ENTRY

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel allows all objects to enter.",
 "type": "integer",
 "value": "0x08000000"
}
```


## constants/PARCEL_FLAG_ALLOW_CREATE_GROUP_OBJECTS

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if group members or scripts in group-deeded objects are allowed to create/rez objects on the parcel.",
 "type": "integer",
 "value": "0x4000000"
}
```


## constants/PARCEL_FLAG_ALLOW_CREATE_OBJECTS

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel allows anyone to create objects.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/PARCEL_FLAG_ALLOW_DAMAGE

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if damage is enabled on the parcel.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/PARCEL_FLAG_ALLOW_FLY

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if flying is allowed on the parcel.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/PARCEL_FLAG_ALLOW_GROUP_OBJECT_ENTRY

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel restricts object entry to only group-owned and owner-owned objects.",
 "type": "integer",
 "value": "0x10000000"
}
```


## constants/PARCEL_FLAG_ALLOW_GROUP_SCRIPTS

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel allows scripts owned by the parcel's group to run.",
 "type": "integer",
 "value": "0x2000000"
}
```


## constants/PARCEL_FLAG_ALLOW_LANDMARK

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel allows landmarks to be created.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/PARCEL_FLAG_ALLOW_SCRIPTS

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if scripts (including outside scripts) are allowed to run on the parcel.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/PARCEL_FLAG_ALLOW_TERRAFORM

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel allows anyone to terraform the land.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/PARCEL_FLAG_LINDEN_HOMES

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "private": true,
 "tooltip": "",
 "type": "integer",
 "value": "0x800000"
}
```


## constants/PARCEL_FLAG_LOCAL_SOUND_ONLY

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel restricts spatialized sounds to the parcel (preventing outside sound from being heard inside).",
 "type": "integer",
 "value": "0x8000"
}
```


## constants/PARCEL_FLAG_RESTRICT_PUSHOBJECT

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel restricts the use of llPushObject by non-owners (or non-group officers if group-owned).",
 "type": "integer",
 "value": "0x200000"
}
```


## constants/PARCEL_FLAG_USE_ACCESS_GROUP

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel limits access to group members.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/PARCEL_FLAG_USE_ACCESS_LIST

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel limits access to a specific list of residents (avatars).",
 "type": "integer",
 "value": "0x200"
}
```


## constants/PARCEL_FLAG_USE_BAN_LIST

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel uses a ban list (including restricting access based on payment information).",
 "type": "integer",
 "value": "0x400"
}
```


## constants/PARCEL_FLAG_USE_LAND_PASS_LIST

```json
{
 "member-of": [
  "ParcelFlag"
 ],
 "tooltip": "Flag used with llGetParcelFlags to check if the parcel restricts access via purchasable land passes (sold for L$).",
 "type": "integer",
 "value": "0x800"
}
```


## constants/PARCEL_MEDIA_COMMAND_AGENT

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to apply the specified media command to the designated agent only.",
 "type": "integer",
 "value": 7,
 "value-type": "key",
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_AUTO_ALIGN

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to toggle or set the parcel media option 'Auto scale content'.",
 "type": "integer",
 "value": 9,
 "value-type": "boolean",
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_DESC

```json
{
 "member-of": [
  "ParcelMediaCommand",
  "ParcelMediaQuery"
 ],
 "tooltip": "Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel media description.",
 "type": "integer",
 "value": 12,
 "value-type": "string"
}
```


## constants/PARCEL_MEDIA_COMMAND_LOOP

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to start the media stream playing from the current frame and have it loop back to the beginning when it reaches the end.",
 "type": "integer",
 "value": 3,
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_LOOP_SET

```json
{
 "member-of": [
  "ParcelMediaCommand",
  "ParcelMediaQuery"
 ],
 "tooltip": "Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel's media looping variable or loop duration (which may have functionality limitations; see VWR-19712).",
 "type": "integer",
 "value": 13,
 "value-type": "float"
}
```


## constants/PARCEL_MEDIA_COMMAND_PAUSE

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to pause the media stream on the current frame.",
 "type": "integer",
 "value": 1,
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_PLAY

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to play the media stream from its current frame, stopping when the end is reached.",
 "type": "integer",
 "value": 2,
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_SIZE

```json
{
 "member-of": [
  "ParcelMediaCommand",
  "ParcelMediaQuery"
 ],
 "tooltip": "Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel media pixel resolution.",
 "type": "integer",
 "value": 11,
 "values": [
  {
   "name": "x",
   "value-type": "integer"
  },
  {
   "name": "y",
   "value-type": "integer"
  }
 ]
}
```


## constants/PARCEL_MEDIA_COMMAND_STOP

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to stop the media stream and rewind it to the first frame.",
 "type": "integer",
 "value": 0,
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_TEXTURE

```json
{
 "member-of": [
  "ParcelMediaCommand",
  "ParcelMediaQuery"
 ],
 "tooltip": "Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel's media texture.",
 "type": "integer",
 "value": 4,
 "value-type": "asset"
}
```


## constants/PARCEL_MEDIA_COMMAND_TIME

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to jump to a specific timestamp in the media stream, specified in floating-point seconds.",
 "type": "integer",
 "value": 6,
 "value-type": "float",
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_TYPE

```json
{
 "member-of": [
  "ParcelMediaCommand",
  "ParcelMediaQuery"
 ],
 "tooltip": "Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel media MIME type (e.g., 'text/html').",
 "type": "integer",
 "value": 10,
 "value-type": "string"
}
```


## constants/PARCEL_MEDIA_COMMAND_UNLOAD

```json
{
 "member-of": [
  "ParcelMediaCommand"
 ],
 "tooltip": "Command used with llParcelMediaCommandList to completely unload the media and restore the face's original texture.",
 "type": "integer",
 "value": 8,
 "access": "write"
}
```


## constants/PARCEL_MEDIA_COMMAND_URL

```json
{
 "member-of": [
  "ParcelMediaCommand",
  "ParcelMediaQuery"
 ],
 "tooltip": "Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel's media URL.",
 "type": "integer",
 "value": 5,
 "value-type": "string"
}
```


## constants/PARCEL_SALE_AGENT

```json
{
 "member-of": [
  "ParcelSaleParam"
 ],
 "tooltip": "Option used with llSetParcelForSale to specify the agent ID authorized to buy the parcel. If none is set, any agent can purchase it.",
 "type": "integer",
 "value": 2,
 "value-type": "key"
}
```


## constants/PARCEL_SALE_ERROR_BAD_PARAMS

```json
{
 "member-of": [
  "ParcelSaleError"
 ],
 "tooltip": "Error code indicating the parameters provided to set the parcel sale information are invalid.",
 "type": "integer",
 "value": 5
}
```


## constants/PARCEL_SALE_ERROR_INVALID_PRICE

```json
{
 "member-of": [
  "ParcelSaleError"
 ],
 "tooltip": "Error code indicating the specified parcel price is invalid (e.g., less than or equal to 0).",
 "type": "integer",
 "value": 4
}
```


## constants/PARCEL_SALE_ERROR_IN_ESCROW

```json
{
 "member-of": [
  "ParcelSaleError"
 ],
 "tooltip": "Error code indicating the parcel is in escrow and cannot be put up for sale.",
 "type": "integer",
 "value": 3
}
```


## constants/PARCEL_SALE_ERROR_NO_PARCEL

```json
{
 "member-of": [
  "ParcelSaleError"
 ],
 "tooltip": "Error code indicating the parcel could not be found.",
 "type": "integer",
 "value": 1
}
```


## constants/PARCEL_SALE_ERROR_NO_PERMISSIONS

```json
{
 "member-of": [
  "ParcelSaleError"
 ],
 "tooltip": "Error code indicating the script lacks the required permissions to set the parcel sale information.",
 "type": "integer",
 "value": 2
}
```


## constants/PARCEL_SALE_OBJECTS

```json
{
 "member-of": [
  "ParcelSaleParam"
 ],
 "tooltip": "Option used with llSetParcelForSale. If set to TRUE, objects on the parcel are included in the sale.",
 "type": "integer",
 "value": 3,
 "value-type": "boolean"
}
```


## constants/PARCEL_SALE_OK

```json
{
 "member-of": [
  "ParcelSaleError"
 ],
 "tooltip": "Status code indicating the parcel sale information was successfully set.",
 "type": "integer",
 "value": 0
}
```


## constants/PARCEL_SALE_PRICE

```json
{
 "member-of": [
  "ParcelSaleParam"
 ],
 "tooltip": "Option used with llSetParcelForSale to set the parcel price. If no authorized agent is set, the price must be greater than 0.",
 "type": "integer",
 "value": 1,
 "value-type": "integer"
}
```


## constants/PASSIVE

```json
{
 "member-of": [
  "DetectType"
 ],
 "tooltip": "Identifies static or non-moving in-world objects (which do not consume active server resources). In llDetectedType(), indicates non-physical objects. In llSensor()/llSensorRepeat() filters, searches for non-physical, non-scripted, inactive, or non-moving physical objects.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/PASS_ALWAYS

```json
{
 "member-of": [
  "PassMode"
 ],
 "tooltip": "Used with event-passing functions (e.g., llPassTouches, llPassCollisions) to ensure events are always passed from the child prim to the root prim, regardless of whether they are handled by child script handlers.",
 "type": "integer",
 "value": 1
}
```


## constants/PASS_IF_NOT_HANDLED

```json
{
 "member-of": [
  "PassMode"
 ],
 "tooltip": "Used with event-passing functions (default behavior) to pass events from the child prim to the root prim only if there is no script handling the event in the child.",
 "type": "integer",
 "value": 0
}
```


## constants/PASS_NEVER

```json
{
 "member-of": [
  "PassMode"
 ],
 "tooltip": "Used with event-passing functions to ensure events are never passed from the child prim to the root prim, regardless of whether they are handled by child script handlers.",
 "type": "integer",
 "value": 2
}
```


## constants/PATROL_PAUSE_AT_WAYPOINTS

```json
{
 "member-of": [
  "CharacterPatrolPointsParam"
 ],
 "tooltip": "Option parameter for llPatrolPoints (defaults to FALSE). If TRUE, the character slows down and momentarily pauses at each waypoint. If FALSE, the character moves to the next waypoint at full speed with no pause.",
 "type": "integer",
 "value": 0,
 "value-type": "boolean",
 "default": false
}
```


## constants/PAYMENT_INFO_ON_FILE

```json
{
 "member-of": [
  "AgentDataPaymentInfo"
 ],
 "tooltip": "Agent data flag returned by llRequestAgentData indicating if the user has payment information on file.",
 "type": "integer",
 "value": 1
}
```


## constants/PAYMENT_INFO_USED

```json
{
 "member-of": [
  "AgentDataPaymentInfo"
 ],
 "tooltip": "Agent data flag returned by llRequestAgentData indicating if the user has ever used their payment information.",
 "type": "integer",
 "value": 2
}
```


## constants/PAY_DEFAULT

```json
{
 "member-of": [
  "PayButton"
 ],
 "tooltip": "Used with llSetPayPrice to use the default value for the specified quick pay button.",
 "type": "integer",
 "value": -2
}
```


## constants/PAY_HIDE

```json
{
 "member-of": [
  "PayButton"
 ],
 "tooltip": "Used with llSetPayPrice to hide the specified quick pay button completely.",
 "type": "integer",
 "value": -1
}
```


## constants/PERMISSION_ATTACH

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to successfully attach to or detach from the agent using llAttachToAvatar.",
 "type": "integer",
 "value": "0x00020"
}
```


## constants/PERMISSION_CHANGE_JOINTS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "deprecated": {
  "reason": "Not implemented."
 },
 "tooltip": "(Not yet implemented)",
 "type": "integer",
 "value": "0x00100"
}
```


## constants/PERMISSION_CHANGE_LINKS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to successfully create, break, or modify links to other objects using llCreateLink, llBreakLink, or llBreakAllLinks.",
 "type": "integer",
 "value": "0x00080"
}
```


## constants/PERMISSION_CHANGE_PERMISSIONS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "deprecated": {
  "reason": "Not implemented."
 },
 "tooltip": "(Not yet implemented)",
 "type": "integer",
 "value": "0x00200"
}
```


## constants/PERMISSION_CONTROL_CAMERA

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to control the agent's camera. The agent must be sitting on or attached to the object, and permission is automatically revoked on standing up or detaching.",
 "type": "integer",
 "value": "0x00800"
}
```


## constants/PERMISSION_DEBIT

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to successfully call llGiveMoney or llTransferLindenDollars to debit the owner's account.",
 "type": "integer",
 "value": "0x00002"
}
```


## constants/PERMISSION_GAME_CONTROL

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "",
 "type": "integer",
 "value": "0x100000"
}
```


## constants/PERMISSION_OVERRIDE_ANIMATIONS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to configure and override default animations on the agent.",
 "type": "integer",
 "value": "0x08000"
}
```


## constants/PERMISSION_PRIVILEGED_LAND_ACCESS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that grants the script privileged access to land parcel functions, which is required to use llSetParcelForSale.",
 "type": "integer",
 "value": "0x80000"
}
```


## constants/PERMISSION_RELEASE_OWNERSHIP

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "deprecated": {
  "reason": "Not implemented."
 },
 "tooltip": "(Not yet implemented)",
 "type": "integer",
 "value": "0x00040"
}
```


## constants/PERMISSION_REMAP_CONTROLS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "deprecated": {
  "reason": "Not implemented."
 },
 "tooltip": "(Not yet implemented)",
 "type": "integer",
 "value": "0x00008"
}
```


## constants/PERMISSION_RETURN_OBJECTS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission required to use the llReturnObjectsByID and llReturnObjectsByOwner functions to return objects from parcels.",
 "type": "integer",
 "value": "0x10000"
}
```


## constants/PERMISSION_SILENT_ESTATE_MANAGEMENT

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to manage estate access rules via llManageEstateAccess without notifying the object owner of the changes.",
 "type": "integer",
 "value": "0x04000"
}
```


## constants/PERMISSION_TAKE_CONTROLS

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to successfully call the llTakeControls function to intercept the agent's controls.",
 "type": "integer",
 "value": "0x00004"
}
```


## constants/PERMISSION_TELEPORT

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission required to teleport the agent using the llTeleportAgent function.",
 "type": "integer",
 "value": "0x01000"
}
```


## constants/PERMISSION_TRACK_CAMERA

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to track the agent's camera position and rotation.",
 "type": "integer",
 "value": "0x00400"
}
```


## constants/PERMISSION_TRIGGER_ANIMATION

```json
{
 "member-of": [
  "ScriptPermission"
 ],
 "tooltip": "Runtime permission that allows the script to start or stop animations on the agent (such as using llStartAnimation).",
 "type": "integer",
 "value": "0x00010"
}
```


## constants/PERM_ALL

```json
{
 "member-of": [
  "AssetPermission"
 ],
 "tooltip": "Permissions mask representing a combination of move, modify, copy, and transfer permissions.",
 "type": "integer",
 "value": "0x7FFFFFFF"
}
```


## constants/PERM_COPY

```json
{
 "member-of": [
  "AssetPermission"
 ],
 "tooltip": "Permissions mask representing copy permission.",
 "type": "integer",
 "value": "0x8000"
}
```


## constants/PERM_MODIFY

```json
{
 "member-of": [
  "AssetPermission"
 ],
 "tooltip": "Permissions mask representing modify permission.",
 "type": "integer",
 "value": "0x4000"
}
```


## constants/PERM_MOVE

```json
{
 "member-of": [
  "AssetPermission"
 ],
 "tooltip": "Permissions mask representing move permission.",
 "type": "integer",
 "value": "0x80000"
}
```


## constants/PERM_TRANSFER

```json
{
 "member-of": [
  "AssetPermission"
 ],
 "tooltip": "Permissions mask representing transfer permission.",
 "type": "integer",
 "value": "0x2000"
}
```


## constants/PI

```json
{
 "tooltip": "Mathematical constant pi, representing the number of radians in a half circle (semi-circle). When used in sensor functions, it specifies a full sphere scan.",
 "type": "float",
 "value": "3.14159265",
 "slua-deprecated": {
  "use": "math.pi",
  "reason": "Double precision."
 }
}
```


## constants/PING_PONG

```json
{
 "member-of": [
  "TextureAnimMode"
 ],
 "tooltip": "Used with texture animation functions to cause the animation to play forward first, and then in reverse.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/PI_BY_TWO

```json
{
 "tooltip": "Mathematical constant pi/2, representing the number of radians in a quarter circle. When used in sensor functions, it specifies a hemisphere scan.",
 "type": "float",
 "value": "1.57079633",
 "slua-deprecated": {
  "use": "math.pi/2",
  "reason": "Double precision."
 }
}
```


## constants/PRIM_ALLOW_UNSIT

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter for allowing or restricting manual standing for avatars seated on this prim within a valid experience. Ignored if the avatar was not seated via llSitOnLink. When restriction is active, participating seated avatars cannot manually stand or select another prim to sit on.",
 "type": "integer",
 "value": 39,
 "value-type": "boolean"
}
```


## constants/PRIM_ALPHA_MODE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to set diffuse texture alpha rendering mode attributes. Requires face, alpha_mode (PRIM_ALPHA_MODE_BLEND, _NONE, _MASK, or _EMISSIVE), and alpha_cutoff (used only for _MASK) parameters.",
 "type": "integer",
 "value": 38,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "alpha_mode",
   "value-type": "integer",
   "enum": "AlphaMode"
  },
  {
   "name": "mask_cutoff",
   "value-type": "integer",
   "range": [
    0,
    255
   ]
  }
 ]
}
```


## constants/PRIM_ALPHA_MODE_BLEND

```json
{
 "member-of": [
  "AlphaMode"
 ],
 "tooltip": "Prim parameter setting for PRIM_ALPHA_MODE. Directs the face to use alpha blending for diffuse texture rendering (if an alpha channel exists). Also used as the default value to clear material settings from a prim face.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_ALPHA_MODE_EMISSIVE

```json
{
 "member-of": [
  "AlphaMode"
 ],
 "tooltip": "Prim parameter setting for PRIM_ALPHA_MODE. Renders the diffuse texture's alpha channel as an emissivity mask. Pixels render with an emissivity corresponding to their opacity under all lighting conditions (fully opaque pixels effectively render as 'full bright').",
 "type": "integer",
 "value": 3
}
```


## constants/PRIM_ALPHA_MODE_MASK

```json
{
 "member-of": [
  "AlphaMode"
 ],
 "tooltip": "Prim parameter setting for PRIM_ALPHA_MODE. Renders the diffuse texture's alpha channel on a binary per-pixel basis; pixels more opaque than the alpha cutoff render as fully opaque, while pixels below the cutoff render as fully transparent.",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_ALPHA_MODE_NONE

```json
{
 "member-of": [
  "AlphaMode"
 ],
 "tooltip": "Prim parameter setting for PRIM_ALPHA_MODE. Directs the face to ignore the alpha channel of the diffuse texture and render as completely opaque (default setting when a material face lacks an alpha channel).",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_BUMP_BARK

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: bark.",
 "type": "integer",
 "value": 4
}
```


## constants/PRIM_BUMP_BLOBS

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: petridish (blobby amoeba-like shapes).",
 "type": "integer",
 "value": 12
}
```


## constants/PRIM_BUMP_BRICKS

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: bricks.",
 "type": "integer",
 "value": 5
}
```


## constants/PRIM_BUMP_BRIGHT

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: brightness (generated from highlights).",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_BUMP_CHECKER

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: checker.",
 "type": "integer",
 "value": 6
}
```


## constants/PRIM_BUMP_CONCRETE

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: concrete.",
 "type": "integer",
 "value": 7
}
```


## constants/PRIM_BUMP_DARK

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: darkness (generated from lowlights).",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_BUMP_DISKS

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: discs (packed circles).",
 "type": "integer",
 "value": 10
}
```


## constants/PRIM_BUMP_GRAVEL

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: gravel.",
 "type": "integer",
 "value": 11
}
```


## constants/PRIM_BUMP_LARGETILE

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: stonetile (large tile).",
 "type": "integer",
 "value": 14
}
```


## constants/PRIM_BUMP_NONE

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: none (no bump map).",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_BUMP_SHINY

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to get or set both the shininess and bump mapping settings of a face.",
 "type": "integer",
 "value": 19,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "shiny",
   "value-type": "integer",
   "enum": "PrimShiny"
  },
  {
   "name": "bump",
   "value-type": "integer",
   "enum": "PrimBump"
  }
 ]
}
```


## constants/PRIM_BUMP_SIDING

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: siding.",
 "type": "integer",
 "value": 13
}
```


## constants/PRIM_BUMP_STONE

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: cutstone (blocks).",
 "type": "integer",
 "value": 9
}
```


## constants/PRIM_BUMP_STUCCO

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: stucco.",
 "type": "integer",
 "value": 15
}
```


## constants/PRIM_BUMP_SUCTION

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: suction (rings).",
 "type": "integer",
 "value": 16
}
```


## constants/PRIM_BUMP_TILE

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: crustytile.",
 "type": "integer",
 "value": 8
}
```


## constants/PRIM_BUMP_WEAVE

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: weave.",
 "type": "integer",
 "value": 17
}
```


## constants/PRIM_BUMP_WOOD

```json
{
 "member-of": [
  "PrimBump"
 ],
 "tooltip": "Face bump mapping setting: woodgrain.",
 "type": "integer",
 "value": 3
}
```


## constants/PRIM_CAST_SHADOWS

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "deprecated": {
  "reason": "Not implemented."
 },
 "tooltip": "Deprecated prim parameter representing shadow casting settings for the primitive.",
 "type": "integer",
 "value": 24,
 "value-type": "boolean"
}
```


## constants/PRIM_CLICK_ACTION

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter followed by a CLICK_ACTION_* constant to specify the default action taken when a user clicks or touches the prim.",
 "type": "integer",
 "value": 43,
 "value-type": "integer",
 "enum": "ClickAction"
}
```


## constants/PRIM_COLLISION_SOUND

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to set the collision sound UUID and volume level for the prim.",
 "type": "integer",
 "value": 53,
 "values": [
  {
   "name": "sound",
   "value-type": "asset"
  },
  {
   "name": "volume",
   "value-type": "float"
  }
 ]
}
```


## constants/PRIM_COLOR

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the Blinn-Phong color and opacity of a face.\n\ninteger face – face number or ALL_SIDES\nvector color – color in RGB <R, G, B> (<0.0, 0.0, 0.0> = black, <1.0, 1.0, 1.0> = white)\nfloat alpha – from 0.0 (clear) to 1.0 (solid) (0.0 <= alpha <= 1.0)\n",
 "type": "integer",
 "value": 18,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "color",
   "value-type": "vector",
   "details": "Color: llGetColor."
  },
  {
   "name": "alpha",
   "value-type": "float",
   "range": [
    0,
    1
   ],
   "details": "Alpha: llGetAlpha."
  }
 ]
}
```


## constants/PRIM_DAMAGE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to get or set the damage amount and damage type delivered by the prim on collision.",
 "type": "integer",
 "value": 51,
 "values": [
  {
   "name": "damage",
   "value-type": "float"
  },
  {
   "name": "damage_type",
   "value-type": "integer",
   "enum": "DamageType"
  }
 ]
}
```


## constants/PRIM_DESC

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_DESC, string description] to get or set the prim's description (equivalent to llGetObjectDesc/llSetObjectDesc).",
 "type": "integer",
 "value": 28,
 "value-type": "string",
 "details": "Description: llGetObjectDesc."
}
```


## constants/PRIM_FLEXIBLE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the prim's flexible configuration.\n\ninteger boolean – TRUE enables, FALSE disables\ninteger softness – ranges from 0 to 3\nfloat gravity – ranges from -10.0 to 10.0\nfloat friction – ranges from 0.0 to 10.0\nfloat wind – ranges from 0.0 to 10.0\nfloat tension – ranges from 0.0 to 10.0\nvector force\n",
 "type": "integer",
 "value": 21,
 "values": [
  {
   "name": "enabled",
   "value-type": "boolean"
  },
  {
   "name": "softness",
   "value-type": "integer",
   "range": [
    0,
    3
   ]
  },
  {
   "name": "gravity",
   "value-type": "float",
   "range": [
    -10,
    10
   ]
  },
  {
   "name": "friction",
   "value-type": "float",
   "range": [
    0,
    10
   ]
  },
  {
   "name": "wind",
   "value-type": "float",
   "range": [
    0,
    10
   ]
  },
  {
   "name": "tension",
   "value-type": "float",
   "range": [
    0,
    10
   ]
  },
  {
   "name": "force",
   "value-type": "vector"
  }
 ]
}
```


## constants/PRIM_FULLBRIGHT

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_FULLBRIGHT, integer face, integer boolean] to get or set whether full-bright rendering is enabled on the specified face.",
 "type": "integer",
 "value": 20,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "enabled",
   "value-type": "boolean"
  }
 ]
}
```


## constants/PRIM_GLOW

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_GLOW, integer face, float intensity] to get or set the glow intensity on a face (the compiler integer value is 25 if the named constant is rejected).",
 "type": "integer",
 "value": 25,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "intensity",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  }
 ]
}
```


## constants/PRIM_GLTF_ALPHA_MODE_BLEND

```json
{
 "member-of": [
  "GLTFAlphaMode"
 ],
 "tooltip": "GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Renders the material with transparency (alpha blending) in linear color space. Transparency from the texture is multiplied by the material's opacity multiplier. Note: This mode can suffer from depth sorting and performance issues.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_GLTF_ALPHA_MODE_MASK

```json
{
 "member-of": [
  "GLTFAlphaMode"
 ],
 "tooltip": "GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Renders the material as fully opaque where the alpha value is greater than the alpha cutoff, and fully transparent otherwise.",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_GLTF_ALPHA_MODE_OPAQUE

```json
{
 "member-of": [
  "GLTFAlphaMode"
 ],
 "tooltip": "GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Ignores the alpha channel entirely and renders the face material as completely opaque.",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_GLTF_BASE_COLOR

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the GLTF base color override of an object's face. Requires face, texture, repeats, offsets, rotation, linear_color (in linear space; use llsRGB2Linear), alpha_mode (PRIM_GLTF_ALPHA_MODE_*), alpha_cutoff, and double_sided arguments.",
 "type": "integer",
 "value": 48,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "texture",
   "value-type": "asset"
  },
  {
   "name": "repeats",
   "value-type": "vector",
   "range": [
    "<-10000,-10000,0>",
    "<10000,10000,0>"
   ]
  },
  {
   "name": "offsets",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "rotation_in_radians",
   "value-type": "float"
  },
  {
   "name": "color",
   "value-type": "vector"
  },
  {
   "name": "alpha",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  },
  {
   "name": "gltf_alpha_mode",
   "value-type": "integer",
   "enum": "GLTFAlphaMode"
  },
  {
   "name": "alpha_mask_cutoff",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  },
  {
   "name": "double_sided",
   "value-type": "boolean"
  }
 ]
}
```


## constants/PRIM_GLTF_EMISSIVE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the GLTF emission override of a face. Requires face, texture, repeats, offsets, rotation, and emissive_tint (specified in linear space; use llsRGB2Linear).",
 "type": "integer",
 "value": 46,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "texture",
   "value-type": "asset"
  },
  {
   "name": "repeats",
   "value-type": "vector",
   "range": [
    "<-10000,-10000,0>",
    "<10000,10000,0>"
   ]
  },
  {
   "name": "offsets",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "rotation_in_radians",
   "value-type": "float"
  },
  {
   "name": "emissive_tint",
   "value-type": "vector"
  }
 ]
}
```


## constants/PRIM_GLTF_METALLIC_ROUGHNESS

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the GLTF occlusion/metallic/roughness override of a face. Requires face, texture, repeats, offsets, rotation, metallic_factor, and roughness_factor arguments.",
 "type": "integer",
 "value": 47,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "texture",
   "value-type": "asset"
  },
  {
   "name": "repeats",
   "value-type": "vector",
   "range": [
    "<-10000,-10000,0>",
    "<10000,10000,0>"
   ]
  },
  {
   "name": "offsets",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "rotation_in_radians",
   "value-type": "float"
  },
  {
   "name": "metallic_factor",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  },
  {
   "name": "roughness_factor",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  }
 ]
}
```


## constants/PRIM_GLTF_NORMAL

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the GLTF normal map override of a face. Requires face, texture, repeats, offsets, and rotation arguments.",
 "type": "integer",
 "value": 45,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "texture",
   "value-type": "asset"
  },
  {
   "name": "repeats",
   "value-type": "vector",
   "range": [
    "<-10000,-10000,0>",
    "<10000,10000,0>"
   ]
  },
  {
   "name": "offsets",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "rotation_in_radians",
   "value-type": "float"
  }
 ]
}
```


## constants/PRIM_HEALTH

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to get or set the health of the prim. Objects default to 0 health.",
 "type": "integer",
 "value": 52,
 "value-type": "float"
}
```


## constants/PRIM_HOLE_CIRCLE

```json
{
 "member-of": [
  "PrimTypeHole"
 ],
 "tooltip": "Parameter used with certain PRIM_TYPE_* flags to make a circular hole via the hole_shape parameter.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/PRIM_HOLE_DEFAULT

```json
{
 "member-of": [
  "PrimTypeHole"
 ],
 "tooltip": "Parameter used with certain PRIM_TYPE_* flags to make a hole of the same shape as the outer shape via the hole_shape parameter.",
 "type": "integer",
 "value": "0x00"
}
```


## constants/PRIM_HOLE_SQUARE

```json
{
 "member-of": [
  "PrimTypeHole"
 ],
 "tooltip": "Parameter used with certain PRIM_TYPE_* flags to make a squarish hole via the hole_shape parameter.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/PRIM_HOLE_TRIANGLE

```json
{
 "member-of": [
  "PrimTypeHole"
 ],
 "tooltip": "Parameter used with certain PRIM_TYPE_* flags to make a triangular hole via the hole_shape parameter.",
 "type": "integer",
 "value": "0x30"
}
```


## constants/PRIM_LINK_TARGET

```json
{
 "member-of": [
  "PrimParam"
 ],
 "tooltip": "Prim parameter [PRIM_LINK_TARGET, integer link_target] used to get or set properties for multiple linked prims within a single primitive parameters call.",
 "type": "integer",
 "value": 34,
 "value-type": "integer",
 "enum": "Links",
 "access": "arg"
}
```


## constants/PRIM_MATERIAL

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_MATERIAL, integer PRIM_MATERIAL_*] to get or set the prim's material. The material determines the default collision sound, sprite, friction coefficient, and restitution coefficient (elasticity) without affecting mass.",
 "type": "integer",
 "value": 2,
 "value-type": "integer",
 "enum": "PhysicsMaterialPreset"
}
```


## constants/PRIM_MATERIAL_DENSITY

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "private": true,
 "deprecated": {
  "use": "DENSITY"
 },
 "tooltip": "",
 "type": "integer",
 "value": "0x1"
}
```


## constants/PRIM_MATERIAL_FLESH

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "tooltip": "Prim material constant: flesh.",
 "type": "integer",
 "value": 4
}
```


## constants/PRIM_MATERIAL_FRICTION

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "private": true,
 "deprecated": {
  "use": "FRICTION"
 },
 "tooltip": "",
 "type": "integer",
 "value": "0x2"
}
```


## constants/PRIM_MATERIAL_GLASS

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "tooltip": "Prim material constant: glass (features very low friction).",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_MATERIAL_GRAVITY_MULTIPLIER

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "private": true,
 "deprecated": {
  "use": "GRAVITY_MULTIPLIER"
 },
 "tooltip": "",
 "type": "integer",
 "value": "0x8"
}
```


## constants/PRIM_MATERIAL_LIGHT

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "deprecated": {
  "use": "PRIM_FULLBRIGHT"
 },
 "tooltip": "Deprecated prim material constant. Light is now a face property instead of a prim property; equivalent functionality is achieved using [PRIM_FULLBRIGHT, ALL_SIDES, TRUE].",
 "type": "integer",
 "value": 7
}
```


## constants/PRIM_MATERIAL_METAL

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "tooltip": "Prim material constant: metal.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_MATERIAL_PLASTIC

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "tooltip": "Prim material constant: plastic.",
 "type": "integer",
 "value": 5
}
```


## constants/PRIM_MATERIAL_RESTITUTION

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "private": true,
 "deprecated": {
  "use": "RESTITUTION"
 },
 "tooltip": "",
 "type": "integer",
 "value": "0x4"
}
```


## constants/PRIM_MATERIAL_RUBBER

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "tooltip": "Prim material constant: rubber.",
 "type": "integer",
 "value": 6
}
```


## constants/PRIM_MATERIAL_STONE

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "tooltip": "Prim material constant: stone.",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_MATERIAL_WOOD

```json
{
 "member-of": [
  "PhysicsMaterialPreset"
 ],
 "tooltip": "Prim material constant: wood.",
 "type": "integer",
 "value": 3
}
```


## constants/PRIM_MEDIA_ALT_IMAGE_ENABLE

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Boolean. Gets or sets the default image state (the image a user sees before media is active) on a face. The default is specified by the server for that media type. Note: This flag is not currently implemented.",
 "type": "integer",
 "value": 0,
 "value-type": "boolean"
}
```


## constants/PRIM_MEDIA_AUTO_LOOP

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Boolean. Gets or sets whether auto-looping is enabled for the face media.",
 "type": "integer",
 "value": 4,
 "value-type": "boolean"
}
```


## constants/PRIM_MEDIA_AUTO_PLAY

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Boolean. Gets or sets whether media auto-plays when a resident is able to view it.",
 "type": "integer",
 "value": 5,
 "value-type": "boolean"
}
```


## constants/PRIM_MEDIA_AUTO_SCALE

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Boolean. Gets or sets whether auto-scaling is enabled, which forces the media to fill the entire texture size.",
 "type": "integer",
 "value": 6,
 "value-type": "boolean"
}
```


## constants/PRIM_MEDIA_AUTO_ZOOM

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Boolean. Gets or sets whether clicking the media triggers auto-zoom and auto-focus.",
 "type": "integer",
 "value": 7,
 "value-type": "boolean"
}
```


## constants/PRIM_MEDIA_CONTROLS

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Integer. Gets or sets the style of media controls (can be set to PRIM_MEDIA_CONTROLS_STANDARD or PRIM_MEDIA_CONTROLS_MINI).",
 "type": "integer",
 "value": 1,
 "value-type": "integer",
 "enum": "PrimMediaControl"
}
```


## constants/PRIM_MEDIA_CONTROLS_MINI

```json
{
 "member-of": [
  "PrimMediaControl"
 ],
 "tooltip": "Mini web navigation controls constant; does not include an address bar.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_MEDIA_CONTROLS_STANDARD

```json
{
 "member-of": [
  "PrimMediaControl"
 ],
 "tooltip": "Standard web navigation controls constant.",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_MEDIA_CURRENT_URL

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "String. Gets or sets the current URL displayed on the chosen face (maximum 1024 characters). Changing this URL triggers media navigation.",
 "type": "integer",
 "value": 2,
 "value-type": "string"
}
```


## constants/PRIM_MEDIA_FIRST_CLICK_INTERACT

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Boolean. Gets or sets what happens when someone click on a playing, but unfocused media face: TRUE: Does the same thing a focused media face does, and forwards the click to the web browser. FALSE: Focuses the media prim so that future clicks are forwarded to the web browser. Note: Viewer settings affect this flag. It works by default on most prims.",
 "type": "integer",
 "value": 8,
 "value-type": "boolean"
}
```


## constants/PRIM_MEDIA_HEIGHT_PIXELS

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "pretty-name": "height",
 "tooltip": "Integer. Gets or sets the height of the media in pixels.",
 "type": "integer",
 "value": 10,
 "value-type": "integer"
}
```


## constants/PRIM_MEDIA_HOME_URL

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "String. Gets or sets the home URL for the chosen face (maximum 1024 characters).",
 "type": "integer",
 "value": 3,
 "value-type": "string"
}
```


## constants/PRIM_MEDIA_MAX_HEIGHT_PIXELS

```json
{
 "tooltip": "",
 "type": "integer",
 "value": 2048
}
```


## constants/PRIM_MEDIA_MAX_URL_LENGTH

```json
{
 "tooltip": "",
 "type": "integer",
 "value": 1024
}
```


## constants/PRIM_MEDIA_MAX_WHITELIST_COUNT

```json
{
 "tooltip": "",
 "type": "integer",
 "value": 64
}
```


## constants/PRIM_MEDIA_MAX_WHITELIST_SIZE

```json
{
 "tooltip": "",
 "type": "integer",
 "value": 1024
}
```


## constants/PRIM_MEDIA_MAX_WIDTH_PIXELS

```json
{
 "tooltip": "",
 "type": "integer",
 "value": 2048
}
```


## constants/PRIM_MEDIA_PARAM_MAX

```json
{
 "tooltip": "",
 "type": "integer",
 "value": 14
}
```


## constants/PRIM_MEDIA_PERMS_CONTROL

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Integer. Gets or sets the permissions mask controlling who can see the media control bar (PRIM_MEDIA_PERM_ANYONE, _GROUP, _NONE, or _OWNER).",
 "type": "integer",
 "value": 14,
 "value-type": "integer",
 "enum": "PrimMediaPerm"
}
```


## constants/PRIM_MEDIA_PERMS_INTERACT

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Integer. Gets or sets the permissions mask controlling who can interact with the media (PRIM_MEDIA_PERM_ANYONE, _GROUP, _NONE, or _OWNER).",
 "type": "integer",
 "value": 13,
 "value-type": "integer",
 "enum": "PrimMediaPerm"
}
```


## constants/PRIM_MEDIA_PERM_ANYONE

```json
{
 "member-of": [
  "PrimMediaPerm"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 4
}
```


## constants/PRIM_MEDIA_PERM_GROUP

```json
{
 "member-of": [
  "PrimMediaPerm"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_MEDIA_PERM_NONE

```json
{
 "member-of": [
  "PrimMediaPerm"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_MEDIA_PERM_OWNER

```json
{
 "member-of": [
  "PrimMediaPerm"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_MEDIA_WHITELIST

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Gets or sets the media whitelist as an array of URL strings (up to 64 URLs or 1024 characters, whichever comes first). At the SLua level, provide a {string} array; the serializer encodes it as an escaped, comma-separated string for the underlying LSL API.",
 "type": "integer",
 "value": 12,
 "value-type": "string-csv"
}
```


## constants/PRIM_MEDIA_WHITELIST_ENABLE

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "tooltip": "Boolean. Gets or sets whether media navigation is restricted to the URLs listed in PRIM_MEDIA_WHITELIST.",
 "type": "integer",
 "value": 11,
 "value-type": "boolean"
}
```


## constants/PRIM_MEDIA_WIDTH_PIXELS

```json
{
 "member-of": [
  "PrimMediaParam"
 ],
 "pretty-name": "width",
 "tooltip": "Integer. Gets or sets the width of the media in pixels.",
 "type": "integer",
 "value": 9,
 "value-type": "integer"
}
```


## constants/PRIM_NAME

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_NAME, string name] to get or set the prim's name (equivalent to llGetObjectName/llSetObjectName).",
 "type": "integer",
 "value": 27,
 "value-type": "string",
 "details": "Name: llGetObjectName."
}
```


## constants/PRIM_NORMAL

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the Blinn-Phong normal map texture settings of a face. Requires face, texture, repeats, offsets, and rotation_in_radians arguments.",
 "type": "integer",
 "value": 37,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "texture",
   "value-type": "asset"
  },
  {
   "name": "repeats",
   "value-type": "vector",
   "range": [
    "<-100,-100,0>",
    "<100,100,0>"
   ]
  },
  {
   "name": "offsets",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "rotation_in_radians",
   "value-type": "float"
  }
 ]
}
```


## constants/PRIM_OMEGA

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get, set, or disable a client-side physical-like rotation (analogous to llTargetOmega).\n\nvector axis – arbitrary axis to rotate the object around\nfloat spinrate – rate of rotation in radians per second\nfloat gain – also modulates the final spinrate and disables the rotation behavior if zero\n",
 "type": "integer",
 "value": 32,
 "values": [
  {
   "name": "axis",
   "value-type": "vector",
   "details": "llTargetOmega"
  },
  {
   "name": "spinrate",
   "value-type": "float"
  },
  {
   "name": "gain",
   "value-type": "float"
  }
 ]
}
```


## constants/PRIM_PHANTOM

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_PHANTOM, integer boolean] to get or set whether phantom status is enabled.",
 "type": "integer",
 "value": 5,
 "value-type": "boolean",
 "details": "Phantom status: llGetStatus."
}
```


## constants/PRIM_PHYSICS

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_PHYSICS, integer boolean] to get or set whether the object responds to Second Life physics.",
 "type": "integer",
 "value": 3,
 "value-type": "boolean",
 "details": "Physics status: llGetStatus."
}
```


## constants/PRIM_PHYSICS_SHAPE_CONVEX

```json
{
 "member-of": [
  "PhysicsShapeType"
 ],
 "tooltip": "Physics shape type setting. Uses the convex hull of the prim shape to generate its physics representation (the default for mesh objects).",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_PHYSICS_SHAPE_NONE

```json
{
 "member-of": [
  "PhysicsShapeType"
 ],
 "tooltip": "Physics shape type setting. Directs the physics engine to ignore this prim entirely, preventing it from contributing to the linkset's physics shape. Note: Cannot be applied to the root prim.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_PHYSICS_SHAPE_PRIM

```json
{
 "member-of": [
  "PhysicsShapeType"
 ],
 "tooltip": "Physics shape type setting. Uses the actual visible shape of the prim to determine its physics representation (the default for all non-mesh objects).",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_PHYSICS_SHAPE_TYPE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to get or set the type of shape the physics engine uses for the prim (PRIM_PHYSICS_SHAPE_NONE, _PRIM, or _CONVEX). Mainly used for physics optimization.",
 "type": "integer",
 "value": 30,
 "value-type": "integer",
 "enum": "PhysicsShapeType"
}
```


## constants/PRIM_POINT_LIGHT

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to configure local lighting.\nAccepts color in linear space (use llsRGB2Linear to convert from sRGB).\n\ninteger boolean – TRUE enables, FALSE disables\nvector linear_color – linear color in RGB <R, G, B&> (<0.0, 0.0, 0.0> = black, <1.0, 1.0, 1.0> = white)\nfloat intensity – ranges from 0.0 to 1.0\nfloat radius – ranges from 0.1 to 20.0\nfloat falloff – ranges from 0.01 to 2.0\n",
 "type": "integer",
 "value": 23,
 "values": [
  {
   "name": "enabled",
   "value-type": "boolean"
  },
  {
   "name": "linear_color",
   "value-type": "vector"
  },
  {
   "name": "intensity",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  },
  {
   "name": "radius",
   "value-type": "float",
   "range": [
    0.1,
    20
   ]
  },
  {
   "name": "falloff",
   "value-type": "float",
   "range": [
    0,
    2
   ]
  }
 ]
}
```


## constants/PRIM_POSITION

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_POSITION, vector position] to get or set the position of the prim in region coordinates (or local coordinates depending on the script context).",
 "type": "integer",
 "value": 6,
 "value-type": "vector",
 "details": "Global position: llGetPos."
}
```


## constants/PRIM_POS_LOCAL

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_POS_LOCAL, vector position] to get or set the local position of a prim (equivalent to llGetLocalPos/llSetPos).",
 "type": "integer",
 "value": 33,
 "value-type": "vector",
 "details": "Local position: llGetLocalPos."
}
```


## constants/PRIM_PROJECTOR

```json
{
 "member-of": [
  "PrimParam"
 ],
 "tooltip": "Prim parameter [PRIM_PROJECTOR, string texture, float fov, float focus, float ambiance] to configure light projection settings. If the prim is not configured as a projector, the texture key will return NULL_KEY.",
 "type": "integer",
 "value": 42,
 "values": [
  {
   "name": "texture",
   "value-type": "string"
  },
  {
   "name": "fov",
   "value-type": "float"
  },
  {
   "name": "focus",
   "value-type": "float"
  },
  {
   "name": "ambiance",
   "value-type": "float"
  }
 ]
}
```


## constants/PRIM_REFLECTION_PROBE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to configure the object as a custom-placed reflection probe for Image-Based Lighting (IBL). Only affects objects inside its volume of influence.",
 "type": "integer",
 "value": 44,
 "values": [
  {
   "name": "enabled",
   "value-type": "boolean"
  },
  {
   "name": "ambiance",
   "value-type": "float",
   "range": [
    0,
    100
   ]
  },
  {
   "name": "clip_distance",
   "value-type": "float",
   "range": [
    0,
    1024
   ]
  },
  {
   "name": "flags",
   "value-type": "integer",
   "enum": "ReflectionProbeType"
  }
 ]
}
```


## constants/PRIM_REFLECTION_PROBE_BOX

```json
{
 "member-of": [
  "ReflectionProbeType"
 ],
 "tooltip": "Flag option used with PRIM_REFLECTION_PROBE. When set, the reflection probe volume is a box; when unset, it defaults to a sphere.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_REFLECTION_PROBE_DYNAMIC

```json
{
 "member-of": [
  "ReflectionProbeType"
 ],
 "tooltip": "Flag option used with PRIM_REFLECTION_PROBE. When set, the probe dynamically includes avatars in its image-based lighting reflections (which carries a rendering performance cost).",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_REFLECTION_PROBE_MIRROR

```json
{
 "member-of": [
  "ReflectionProbeType"
 ],
 "tooltip": "Flag option used with PRIM_REFLECTION_PROBE. When set, intersecting low-roughness PBR materials act as mirrors. Note: Mirrors do not reflect avatars unless PRIM_REFLECTION_PROBE_DYNAMIC is also enabled, and they carry a performance cost.",
 "type": "integer",
 "value": 4
}
```


## constants/PRIM_RENDER_MATERIAL

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_RENDER_MATERIAL, integer face, string material] to get or set face material settings. Note: Setting this clears most PRIM_GLTF_* properties on the face, except for repeats, offsets, and rotation_in_radians.",
 "type": "integer",
 "value": 49,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "render_material",
   "value-type": "asset",
   "details": "Material: llGetRenderMaterial."
  }
 ]
}
```


## constants/PRIM_ROTATION

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_ROTATION, rotation global_rot] to get or set the global rotation of the prim (equivalent to llGetRot/llSetRot; note that setting this on child prims may be broken).",
 "type": "integer",
 "value": 8,
 "value-type": "rotation",
 "details": "Global rotation: llGetRot."
}
```


## constants/PRIM_ROT_LOCAL

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_ROT_LOCAL, rotation local_rot] to get or set the local rotation of a prim (equivalent to llGetLocalRot/llSetLocalRot).",
 "type": "integer",
 "value": 29,
 "value-type": "rotation",
 "details": "Local rotation: llGetLocalRot."
}
```


## constants/PRIM_SCRIPTED_SIT_ONLY

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter restricting manual sitting on this prim. When active, sitting can only be initiated via llSitOnLink; manual sitting attempts fail. This restriction applies even outside experience-enabled regions.",
 "type": "integer",
 "value": 40,
 "value-type": "boolean"
}
```


## constants/PRIM_SCULPT_FLAG_ANIMESH

```json
{
 "member-of": [
  "PrimTypeSculptFlag"
 ],
 "tooltip": "Read-only flag for PRIM_TYPE_SCULPT to query whether the object is an Animated Mesh (Animesh).",
 "type": "integer",
 "value": 32
}
```


## constants/PRIM_SCULPT_FLAG_INVERT

```json
{
 "member-of": [
  "PrimTypeSculptFlag"
 ],
 "tooltip": "Flag for PRIM_TYPE_SCULPT to render the sculpted prim inside-out by inverting the normals of each polygon.",
 "type": "integer",
 "value": 64
}
```


## constants/PRIM_SCULPT_FLAG_MIRROR

```json
{
 "member-of": [
  "PrimTypeSculptFlag"
 ],
 "tooltip": "Flag for PRIM_TYPE_SCULPT to render a mirror-image of the sculpted prim, mirrored across the X-axis.",
 "type": "integer",
 "value": 128
}
```


## constants/PRIM_SCULPT_TYPE_CYLINDER

```json
{
 "member-of": [
  "PrimTypeSculptType"
 ],
 "tooltip": "Sculpt type option for PRIM_TYPE_SCULPT that stitches the left side to the right to produce a cylinder-shaped sculpted prim.",
 "type": "integer",
 "value": 4
}
```


## constants/PRIM_SCULPT_TYPE_MASK

```json
{
 "member-of": [
  "PrimTypeSculptType"
 ],
 "tooltip": "Bitmask used when parsing sculpted prim properties (PRIM_TYPE_SCULPT) from llGetPrimitiveParams to separate the base sculpt type from modifying flags (invert or mirror).",
 "type": "integer",
 "value": 7
}
```


## constants/PRIM_SCULPT_TYPE_MESH

```json
{
 "member-of": [
  "PrimTypeSculptType"
 ],
 "tooltip": "Sculpt type option for PRIM_TYPE_SCULPT indicating the object is a uploaded Mesh model.",
 "type": "integer",
 "value": 5
}
```


## constants/PRIM_SCULPT_TYPE_PLANE

```json
{
 "member-of": [
  "PrimTypeSculptType"
 ],
 "tooltip": "Sculpt type option for PRIM_TYPE_SCULPT that performs no stitching or converging, producing a flat plane-shaped sculpted prim.",
 "type": "integer",
 "value": 3
}
```


## constants/PRIM_SCULPT_TYPE_SPHERE

```json
{
 "member-of": [
  "PrimTypeSculptType"
 ],
 "tooltip": "Sculpt type option for PRIM_TYPE_SCULPT that stitches the left side to the right and separately converges the top and bottom to produce a sphere-shaped sculpted prim.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_SCULPT_TYPE_TORUS

```json
{
 "member-of": [
  "PrimTypeSculptType"
 ],
 "tooltip": "Sculpt type option for PRIM_TYPE_SCULPT that stitches top-to-bottom and left-to-right to produce a torus-shaped sculpted prim.",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_SHINY_HIGH

```json
{
 "member-of": [
  "PrimShiny"
 ],
 "tooltip": "Sets the highest intensity legacy face shininess setting.",
 "type": "integer",
 "value": 3
}
```


## constants/PRIM_SHINY_LOW

```json
{
 "member-of": [
  "PrimShiny"
 ],
 "tooltip": "Sets the lowest intensity legacy face shininess setting.",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_SHINY_MEDIUM

```json
{
 "member-of": [
  "PrimShiny"
 ],
 "tooltip": "Sets a medium intensity legacy face shininess setting.",
 "type": "integer",
 "value": 2
}
```


## constants/PRIM_SHINY_NONE

```json
{
 "member-of": [
  "PrimShiny"
 ],
 "tooltip": "Disables the legacy face shininess setting.",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_SIT_FLAGS

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to get or set sit-related flags currently active on the prim.",
 "type": "integer",
 "value": 50,
 "value-type": "integer",
 "enum": "SitFlag"
}
```


## constants/PRIM_SIT_TARGET

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_SIT_TARGET, integer boolean, vector offset, rotation rot] to get or set the prim's sit target. Setting the boolean to FALSE deactivates the target. Unlike llLinkSitTarget, offset <0.0, 0.0, 0.0> can be explicitly set.",
 "type": "integer",
 "value": 41,
 "values": [
  {
   "name": "sit_target",
   "value-type": "boolean",
   "details": "Sit target: llSitTarget."
  },
  {
   "name": "offset",
   "value-type": "vector"
  },
  {
   "name": "rot",
   "value-type": "rotation"
  }
 ]
}
```


## constants/PRIM_SIZE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_SIZE, vector size] to get or set the prim's physical dimensions (equivalent to llGetScale/llSetScale).",
 "type": "integer",
 "value": 7,
 "value-type": "vector",
 "details": "Size: llGetScale.",
 "range": [
  "<0.01,0.01,0.01>",
  "<64,64,64>"
 ]
}
```


## constants/PRIM_SLICE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_SLICE, vector slice] to get or set the prim's slice values (a shape attribute equivalent to advanced cut).",
 "type": "integer",
 "value": 35,
 "value-type": "vector",
 "range": [
  "<0,0,0>",
  "<1,1,0>"
 ]
}
```


## constants/PRIM_SPECULAR

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter to get or set the Blinn-Phong specular map texture settings of a face. Requires face, texture, repeats, offsets, rotation_in_radians, color, glossy, and environment arguments.",
 "type": "integer",
 "value": 36,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "texture",
   "value-type": "asset"
  },
  {
   "name": "repeats",
   "value-type": "vector",
   "range": [
    "<-100,-100,0>",
    "<100,100,0>"
   ]
  },
  {
   "name": "offsets",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "rotation_in_radians",
   "value-type": "float"
  },
  {
   "name": "color",
   "value-type": "vector"
  },
  {
   "name": "glossiness",
   "value-type": "integer",
   "range": [
    0,
    255
   ]
  },
  {
   "name": "environment",
   "value-type": "integer",
   "range": [
    0,
    255
   ]
  }
 ]
}
```


## constants/PRIM_TEMP_ON_REZ

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to get or set the object's temporary status. Temporary objects live until the next garbage collection cycle (about 1 minute), do not count against normal prim limits, but are subject to regional limits.",
 "type": "integer",
 "value": 4,
 "value-type": "boolean",
 "details": "Temporary attribute."
}
```


## constants/PRIM_TEXGEN

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_TEXGEN, integer face, integer mode] to get or set the texture mapping mode of the face.",
 "type": "integer",
 "value": 22,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "mode",
   "value-type": "integer",
   "enum": "PrimTexgen"
  }
 ]
}
```


## constants/PRIM_TEXGEN_DEFAULT

```json
{
 "member-of": [
  "PrimTexgen"
 ],
 "tooltip": "Texture mapping mode setting for PRIM_TEXGEN. Specifies that texture repeat units are measured in texture repeats per face.",
 "type": "integer",
 "value": 0
}
```


## constants/PRIM_TEXGEN_PLANAR

```json
{
 "member-of": [
  "PrimTexgen"
 ],
 "tooltip": "Texture mapping mode setting for PRIM_TEXGEN. Specifies that texture repeat units are measured in repeats per half-meter (unlike the in-world editor, which measures in repeats per meter).",
 "type": "integer",
 "value": 1
}
```


## constants/PRIM_TEXT

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_TEXT, string text, vector color, float alpha] to get or set the object's floating/hover text (equivalent to llSetText).",
 "type": "integer",
 "value": 26,
 "values": [
  {
   "name": "text",
   "value-type": "string"
  },
  {
   "name": "color",
   "value-type": "vector"
  },
  {
   "name": "alpha",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  }
 ]
}
```


## constants/PRIM_TEXTURE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter [PRIM_TEXTURE, integer face, string texture, vector repeats, vector offsets, float rotation_in_radians] to get or set the Blinn-Phong diffuse texture settings of a face.",
 "type": "integer",
 "value": 17,
 "values": [
  {
   "name": "face",
   "value-type": "integer",
   "enum": "Faces",
   "access": "arg"
  },
  {
   "name": "texture",
   "value-type": "asset",
   "details": "Texture: llGetTexture."
  },
  {
   "name": "repeats",
   "value-type": "vector",
   "range": [
    "<-100,-100,0>",
    "<100,100,0>"
   ],
   "details": "Repeats: llGetTextureScale."
  },
  {
   "name": "offsets",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ],
   "details": "Offset: llGetTextureOffset."
  },
  {
   "name": "rotation_in_radians",
   "value-type": "float",
   "details": "Rotation: llGetTextureRot."
  }
 ]
}
```


## constants/PRIM_TYPE

```json
{
 "member-of": [
  "PrimParam",
  "PrimParamGet"
 ],
 "tooltip": "Prim parameter used to get or set the geometric shape type (PRIM_TYPE_*) and its associated parameters.",
 "type": "integer",
 "value": 9,
 "value-type": "integer",
 "enum": "PrimType"
}
```


## constants/PRIM_TYPE_BOX

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a box and configure its shape properties.",
 "type": "integer",
 "value": 0,
 "values": [
  {
   "name": "hole_shape",
   "value-type": "integer",
   "enum": "PrimTypeHole"
  },
  {
   "name": "cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hollow",
   "value-type": "float",
   "range": [
    0,
    0.95
   ]
  },
  {
   "name": "twist",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "top_size",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<2,2,0>"
   ]
  },
  {
   "name": "top_shear",
   "value-type": "vector",
   "range": [
    "<-0.5,-0.5,0>",
    "<0.5,0.5,0>"
   ]
  }
 ]
}
```


## constants/PRIM_TYPE_CYLINDER

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a cylinder and configure its shape properties.",
 "type": "integer",
 "value": 1,
 "values": [
  {
   "name": "hole_shape",
   "value-type": "integer",
   "enum": "PrimTypeHole"
  },
  {
   "name": "cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hollow",
   "value-type": "float",
   "range": [
    0,
    0.95
   ]
  },
  {
   "name": "twist",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "top_size",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<2,2,0>"
   ]
  },
  {
   "name": "top_shear",
   "value-type": "vector",
   "range": [
    "<-0.5,-0.5,0>",
    "<0.5,0.5,0>"
   ]
  }
 ]
}
```


## constants/PRIM_TYPE_PRISM

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a prism and configure its shape properties.",
 "type": "integer",
 "value": 2,
 "values": [
  {
   "name": "hole_shape",
   "value-type": "integer",
   "enum": "PrimTypeHole"
  },
  {
   "name": "cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hollow",
   "value-type": "float",
   "range": [
    0,
    0.95
   ]
  },
  {
   "name": "twist",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "top_size",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<2,2,0>"
   ]
  },
  {
   "name": "top_shear",
   "value-type": "vector",
   "range": [
    "<-0.5,-0.5,0>",
    "<0.5,0.5,0>"
   ]
  }
 ]
}
```


## constants/PRIM_TYPE_RING

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a ring and configure its shape properties.",
 "type": "integer",
 "value": 6,
 "values": [
  {
   "name": "hole_shape",
   "value-type": "integer",
   "enum": "PrimTypeHole"
  },
  {
   "name": "cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hollow",
   "value-type": "float",
   "range": [
    0,
    0.95
   ]
  },
  {
   "name": "twist",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hole_size",
   "value-type": "vector",
   "range": [
    "<0.05,0.05,0>",
    "<1,0.5,0>"
   ]
  },
  {
   "name": "top_shear",
   "value-type": "vector",
   "range": [
    "<-0.5,-0.5,0>",
    "<0.5,0.5,0>"
   ]
  },
  {
   "name": "advanced_cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "taper",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "revolutions",
   "value-type": "float",
   "range": [
    1,
    4
   ]
  },
  {
   "name": "radius_offset",
   "value-type": "float"
  },
  {
   "name": "skew",
   "value-type": "float",
   "range": [
    -1,
    1
   ]
  }
 ]
}
```


## constants/PRIM_TYPE_SCULPT

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a sculpted prim (sculpty) or mesh of a specific type.",
 "type": "integer",
 "value": 7,
 "values": [
  {
   "name": "map",
   "value-type": "asset"
  },
  {
   "name": "type",
   "value-type": "integer",
   "enum": "PrimTypeSculpt"
  }
 ]
}
```


## constants/PRIM_TYPE_SPHERE

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a sphere and configure its shape properties.",
 "type": "integer",
 "value": 3,
 "values": [
  {
   "name": "hole_shape",
   "value-type": "integer",
   "enum": "PrimTypeHole"
  },
  {
   "name": "cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hollow",
   "value-type": "float",
   "range": [
    0,
    0.95
   ]
  },
  {
   "name": "twist",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "dimple",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  }
 ]
}
```


## constants/PRIM_TYPE_TORUS

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a torus and configure its shape properties.",
 "type": "integer",
 "value": 4,
 "values": [
  {
   "name": "hole_shape",
   "value-type": "integer",
   "enum": "PrimTypeHole"
  },
  {
   "name": "cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hollow",
   "value-type": "float",
   "range": [
    0,
    0.95
   ]
  },
  {
   "name": "twist",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hole_size",
   "value-type": "vector",
   "range": [
    "<0.05,0.05,0>",
    "<1,0.5,0>"
   ]
  },
  {
   "name": "top_shear",
   "value-type": "vector",
   "range": [
    "<-0.5,-0.5,0>",
    "<0.5,0.5,0>"
   ]
  },
  {
   "name": "advanced_cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "taper",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "revolutions",
   "value-type": "float",
   "range": [
    1,
    4
   ]
  },
  {
   "name": "radius_offset",
   "value-type": "float"
  },
  {
   "name": "skew",
   "value-type": "float",
   "range": [
    -1,
    1
   ]
  }
 ]
}
```


## constants/PRIM_TYPE_TUBE

```json
{
 "member-of": [
  "PrimType"
 ],
 "tooltip": "Shape parameter for PRIM_TYPE used to define the prim as a tube and configure its shape properties.",
 "type": "integer",
 "value": 5,
 "values": [
  {
   "name": "hole_shape",
   "value-type": "integer",
   "enum": "PrimTypeHole"
  },
  {
   "name": "cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hollow",
   "value-type": "float",
   "range": [
    0,
    0.95
   ]
  },
  {
   "name": "twist",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "hole_size",
   "value-type": "vector",
   "range": [
    "<0.05,0.05,0>",
    "<1,0.5,0>"
   ]
  },
  {
   "name": "top_shear",
   "value-type": "vector",
   "range": [
    "<-0.5,-0.5,0>",
    "<0.5,0.5,0>"
   ]
  },
  {
   "name": "advanced_cut",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "taper",
   "value-type": "vector",
   "range": [
    "<-1,-1,0>",
    "<1,1,0>"
   ]
  },
  {
   "name": "revolutions",
   "value-type": "float",
   "range": [
    1,
    4
   ]
  },
  {
   "name": "radius_offset",
   "value-type": "float"
  },
  {
   "name": "skew",
   "value-type": "float",
   "range": [
    -1,
    1
   ]
  }
 ]
}
```


## constants/PROFILE_NONE

```json
{
 "member-of": [
  "ScriptProfileMode"
 ],
 "tooltip": "Disables script profiling.",
 "type": "integer",
 "value": 0
}
```


## constants/PROFILE_SCRIPT_MEMORY

```json
{
 "member-of": [
  "ScriptProfileMode"
 ],
 "tooltip": "Enables script memory profiling, tracking the maximum amount of memory consumed while it is active.",
 "type": "integer",
 "value": 1
}
```


## constants/PSYS_PART_BF_DEST_COLOR

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "Scales the RGBA values by the RGBA values of the destination.",
 "type": "integer",
 "value": 2
}
```


## constants/PSYS_PART_BF_ONE

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "PSYS_PART_BF_ONE",
 "type": "integer",
 "value": 0
}
```


## constants/PSYS_PART_BF_ONE_MINUS_DEST_COLOR

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "Scales the RGBA values by the inverted RGBA values of the destination.",
 "type": "integer",
 "value": 4
}
```


## constants/PSYS_PART_BF_ONE_MINUS_SOURCE_ALPHA

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "Scales the RGBA values by the inverted alpha values of the particle source.",
 "type": "integer",
 "value": 9
}
```


## constants/PSYS_PART_BF_ONE_MINUS_SOURCE_COLOR

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "Scales the RGBA values by the inverted RGBA values of the particle source.",
 "type": "integer",
 "value": 5
}
```


## constants/PSYS_PART_BF_SOURCE_ALPHA

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "Scales the RGBA values by the alpha values of the particle source.",
 "type": "integer",
 "value": 7
}
```


## constants/PSYS_PART_BF_SOURCE_COLOR

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "Scales the RGBA values by the RGBA values of the particle source.",
 "type": "integer",
 "value": 3
}
```


## constants/PSYS_PART_BF_ZERO

```json
{
 "member-of": [
  "ParticleBlendFunc"
 ],
 "tooltip": "Zeros out the source or destination RGBA values.",
 "type": "integer",
 "value": 1
}
```


## constants/PSYS_PART_BLEND_FUNC_DEST

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Integer parameter defining the destination blending function.",
 "type": "integer",
 "value": 25,
 "value-type": "integer",
 "enum": "ParticleBlendFunc",
 "default": "PSYS_PART_BF_ONE_MINUS_SOURCE_ALPHA"
}
```


## constants/PSYS_PART_BLEND_FUNC_SOURCE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Integer parameter defining the source blending function.",
 "type": "integer",
 "value": 24,
 "value-type": "integer",
 "enum": "ParticleBlendFunc",
 "default": "PSYS_PART_BF_SOURCE_ALPHA"
}
```


## constants/PSYS_PART_BOUNCE_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag causing particles to bounce off a plane at the emitter object's Z height.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/PSYS_PART_EMISSIVE_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag that makes particles full-bright and unaffected by global lighting (sunlight). Otherwise, particles are lit by current global lighting or local point lights.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/PSYS_PART_END_ALPHA

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "alpha_end",
 "tooltip": "Float parameter that determines the ending alpha (transparency) of the particles.",
 "type": "integer",
 "value": 4,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/PSYS_PART_END_COLOR

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "color_end",
 "tooltip": "Vector parameter <r, g, b> that determines the ending color of the particles.",
 "type": "integer",
 "value": 3,
 "value-type": "vector"
}
```


## constants/PSYS_PART_END_GLOW

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "glow_end",
 "tooltip": "Float parameter that determines the ending glow value of the particles.",
 "type": "integer",
 "value": 27,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/PSYS_PART_END_SCALE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "scale_end",
 "tooltip": "Vector parameter <sx, sy, z> defining the ending size of the particle billboard in meters (z-axis value is ignored).",
 "type": "integer",
 "value": 6,
 "value-type": "vector",
 "range": [
  "<0.03125,0.03125,0>",
  "<4,4,0>"
 ]
}
```


## constants/PSYS_PART_FLAGS

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Integer bitfield parameter specifying the simulation flags for emitted particles. Multiple flags can be combined using bitwise OR (|).",
 "type": "integer",
 "value": 0,
 "value-type": "integer",
 "enum": "ParticleFlag"
}
```


## constants/PSYS_PART_FOLLOW_SRC_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag causing particle positions to remain relative to the position and movement of the emitter. Enabling this flag disables the PSYS_SRC_BURST_RADIUS rule.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/PSYS_PART_FOLLOW_VELOCITY_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag causing particles to rotate and orient their vertical 'top' toward their direction of movement or emission. Otherwise, they remain vertically oriented with the top of the texture facing up.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/PSYS_PART_INTERP_COLOR_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "pretty-name": "color_interp",
 "tooltip": "Particle flag causing the particle's color and alpha to smoothly interpolate from their START values to their END values over its lifetime.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/PSYS_PART_INTERP_SCALE_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "pretty-name": "scale_interp",
 "tooltip": "Particle flag causing the particle's size/scale to transition from its START setting to its END setting over its lifetime.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/PSYS_PART_MAX_AGE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the lifetime (age in seconds) of an individual particle before it dies.",
 "type": "integer",
 "value": 7,
 "value-type": "float",
 "range": [
  0,
  30
 ]
}
```


## constants/PSYS_PART_RIBBON_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag that joins emitted particles into a continuous ribbon strip. Textures stretch to join adjacent edges. Width is controlled by the 'x' start/end scale; 'y' controls maximum visibility distance. Ribbon segments are not camera-facing, mimic the emitter's Z-axis, and require horizontal movement to render.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/PSYS_PART_START_ALPHA

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "alpha_begin",
 "tooltip": "Float parameter that determines the starting alpha (transparency) of the particles.",
 "type": "integer",
 "value": 2,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/PSYS_PART_START_COLOR

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "color_begin",
 "tooltip": "Vector parameter <r, g, b> that determines the starting color of the particles.",
 "type": "integer",
 "value": 1,
 "value-type": "vector"
}
```


## constants/PSYS_PART_START_GLOW

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "glow_begin",
 "tooltip": "Float parameter that determines the starting glow value of the particles.",
 "type": "integer",
 "value": 26,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/PSYS_PART_START_SCALE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "scale_begin",
 "tooltip": "Vector parameter <sx, sy, z> defining the starting size of the particle billboard in meters (z-axis value is ignored).",
 "type": "integer",
 "value": 5,
 "value-type": "vector",
 "range": [
  "<0.03125,0.03125,0>",
  "<4,4,0>"
 ]
}
```


## constants/PSYS_PART_TARGET_LINEAR_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag causing emitted particles to move in a straight, evenly-spaced line toward the PSYS_SRC_TARGET_KEY target. Ignores non-DROP patterns, radius, burst speeds, angles, omega, acceleration, and wind. Combining with bounce while target is below emitter deflects particles upward.",
 "type": "integer",
 "value": "0x80"
}
```


## constants/PSYS_PART_TARGET_POS_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag causing emitted particles to change course and travel toward the target specified by PSYS_SRC_TARGET_KEY during their lifetime. If no valid or reachable target is set, particles target the emitting prim itself.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/PSYS_PART_WIND_MASK

```json
{
 "member-of": [
  "ParticleFlag"
 ],
 "tooltip": "Particle flag that applies wind as a secondary force on the particles, damping their velocity toward the wind velocity.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/PSYS_SRC_ACCEL

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Vector parameter <x, y, z> specifying the constant acceleration to apply to particles.",
 "type": "integer",
 "value": 8,
 "value-type": "vector",
 "range": [
  "<-100,-100,-100>",
  "<100,100,100>"
 ]
}
```


## constants/PSYS_SRC_ANGLE_BEGIN

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the angle in radians where particles will not be created (for ANGLE patterns).",
 "type": "integer",
 "value": 22,
 "value-type": "float"
}
```


## constants/PSYS_SRC_ANGLE_END

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the ending angle in radians to be filled with particles (for ANGLE patterns). If smaller than angle_begin, their roles are swapped.",
 "type": "integer",
 "value": 23,
 "value-type": "float"
}
```


## constants/PSYS_SRC_BURST_PART_COUNT

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Integer parameter specifying the number of particles to release in each burst.",
 "type": "integer",
 "value": 15,
 "value-type": "integer"
}
```


## constants/PSYS_SRC_BURST_RADIUS

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the radial distance from the emitter's center at which particles are created.",
 "type": "integer",
 "value": 16,
 "value-type": "float"
}
```


## constants/PSYS_SRC_BURST_RATE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the interval in seconds between particle bursts.",
 "type": "integer",
 "value": 13,
 "value-type": "float"
}
```


## constants/PSYS_SRC_BURST_SPEED_MAX

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the maximum initial speed of emitted particles.",
 "type": "integer",
 "value": 18,
 "value-type": "float"
}
```


## constants/PSYS_SRC_BURST_SPEED_MIN

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the minimum initial speed of emitted particles.",
 "type": "integer",
 "value": 17,
 "value-type": "float"
}
```


## constants/PSYS_SRC_INNERANGLE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "angle_inner",
 "tooltip": "Float parameter specifying the inner angle of the arc for ANGLE or ANGLE_CONE patterns. The specified inner area will not contain particles.",
 "type": "integer",
 "value": 10,
 "value-type": "float"
}
```


## constants/PSYS_SRC_MAX_AGE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Float parameter specifying the active duration of the particle system in seconds (0.0 means forever).",
 "type": "integer",
 "value": 19,
 "value-type": "float"
}
```


## constants/PSYS_SRC_OBJ_REL_MASK

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "private": true,
 "tooltip": "",
 "type": "integer",
 "value": "0x1",
 "value-type": "integer"
}
```


## constants/PSYS_SRC_OMEGA

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Vector parameter setting the angular velocity used to rotate the emission axis for ANGLE and ANGLE_CONE patterns.",
 "type": "integer",
 "value": 21,
 "value-type": "vector"
}
```


## constants/PSYS_SRC_OUTERANGLE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "pretty-name": "angle_outer",
 "tooltip": "Float parameter specifying the outer angle of the arc for ANGLE or ANGLE_CONE patterns. The area between the outer and inner angles is filled with particles.",
 "type": "integer",
 "value": 11,
 "value-type": "float"
}
```


## constants/PSYS_SRC_PATTERN

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Integer parameter specifying the generation pattern (PSYS_SRC_PATTERN_*) used to emit particles.",
 "type": "integer",
 "value": 9,
 "value-type": "integer",
 "enum": "ParticleSourcePattern"
}
```


## constants/PSYS_SRC_PATTERN_ANGLE

```json
{
 "member-of": [
  "ParticleSourcePattern"
 ],
 "tooltip": "Emission pattern that sprays particles outward in a flat circular, semi-circular, arc, or ray-shaped 2D area (around the prim's local X-axis) as defined by the start/end and inner/outer angle parameters.",
 "type": "integer",
 "value": "0x04"
}
```


## constants/PSYS_SRC_PATTERN_ANGLE_CONE

```json
{
 "member-of": [
  "ParticleSourcePattern"
 ],
 "tooltip": "Emission pattern that sprays particles outward in a 3D spherical, conical, or ring-shaped area defined by the start/end and inner/outer angle parameters. Can emulate the EXPLODE pattern if angles are set to 0.0 and PI.",
 "type": "integer",
 "value": "0x08"
}
```


## constants/PSYS_SRC_PATTERN_ANGLE_CONE_EMPTY

```json
{
 "member-of": [
  "ParticleSourcePattern"
 ],
 "tooltip": "Incomplete emission pattern that behaves identically to the DROP pattern. Intended to invert the ANGLE parameters to define an empty area where particles are not sprayed.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/PSYS_SRC_PATTERN_DROP

```json
{
 "member-of": [
  "ParticleSourcePattern"
 ],
 "tooltip": "Emission pattern that drops particles at the source position with no initial velocity. Overrides burst radius, minimum speed, and maximum speed settings to 0.0.",
 "type": "integer",
 "value": "0x01"
}
```


## constants/PSYS_SRC_PATTERN_EXPLODE

```json
{
 "member-of": [
  "ParticleSourcePattern"
 ],
 "tooltip": "Emission pattern that shoots particles outward in all directions using the burst parameters.",
 "type": "integer",
 "value": "0x02"
}
```


## constants/PSYS_SRC_TARGET_KEY

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "Key (UUID) of the target object that particles travel toward when PSYS_PART_TARGET_POS_MASK or PSYS_PART_TARGET_LINEAR_MASK is enabled.",
 "type": "integer",
 "value": 20,
 "value-type": "key"
}
```


## constants/PSYS_SRC_TEXTURE

```json
{
 "member-of": [
  "ParticleParam"
 ],
 "tooltip": "String parameter specifying the inventory name or UUID asset key of the texture used for the particles.",
 "type": "integer",
 "value": 12,
 "value-type": "asset"
}
```


## constants/PUBLIC_CHANNEL

```json
{
 "member-of": [
  "Channel"
 ],
 "tooltip": "Integer constant representing the open local chat channel. Passing this to chat functions (llSay, llWhisper, llShout) prints text to the publicly heard chat seen by nearby users and objects.",
 "type": "integer",
 "value": 0
}
```


## constants/PURSUIT_FUZZ_FACTOR

```json
{
 "member-of": [
  "CharacterPursueParam"
 ],
 "tooltip": "Option for llPursue that selects a random destination near the PURSUIT_OFFSET (range is 0 to 1, where 1 is most random). Requires a non-zero PURSUIT_OFFSET.",
 "type": "integer",
 "value": 3,
 "value-type": "float",
 "range": [
  0,
  1
 ],
 "default": 0
}
```


## constants/PURSUIT_GOAL_TOLERANCE

```json
{
 "member-of": [
  "CharacterPursueParam"
 ],
 "tooltip": "Option for llPursue defining how close (between 0.25m and 10m) the character must be to consider the goal reached.",
 "type": "integer",
 "value": 5,
 "value-type": "float",
 "range": [
  0.25,
  10
 ]
}
```


## constants/PURSUIT_INTERCEPT

```json
{
 "member-of": [
  "CharacterPursueParam"
 ],
 "tooltip": "Option for llPursue specifying whether the pathfinding character attempts to predict and intercept the target's future location.",
 "type": "integer",
 "value": 4,
 "value-type": "boolean",
 "default": false
}
```


## constants/PURSUIT_OFFSET

```json
{
 "member-of": [
  "CharacterPursueParam"
 ],
 "tooltip": "Option for llPursue specifying a constant position offset relative to the target for the character to navigate toward.",
 "type": "integer",
 "value": 1,
 "value-type": "vector",
 "default": "ZERO_VECTOR"
}
```


## constants/PU_EVADE_HIDDEN

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update status code triggered when an llEvade character determines it has successfully hidden from its pursuer.",
 "type": "integer",
 "value": "0x07"
}
```


## constants/PU_EVADE_SPOTTED

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update status code triggered when an llEvade character switches from hiding to running.",
 "type": "integer",
 "value": "0x08"
}
```


## constants/PU_FAILURE_DYNAMIC_PATHFINDING_DISABLED

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code triggered when a character enters a region where dynamic pathfinding has been disabled in the Region Debug Console.",
 "type": "integer",
 "value": 10
}
```


## constants/PU_FAILURE_INVALID_GOAL

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code triggered when the specified goal is not on the region's navigation mesh (navmesh) and is unreachable.",
 "type": "integer",
 "value": "0x03"
}
```


## constants/PU_FAILURE_INVALID_START

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code triggered when the character is at an unnavigable starting position (e.g., off the navmesh or too high above it).",
 "type": "integer",
 "value": "0x02"
}
```


## constants/PU_FAILURE_NO_NAVMESH

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update fatal error triggered when there is no navmesh generated for the region (typically indicates a server failure).",
 "type": "integer",
 "value": "0x09"
}
```


## constants/PU_FAILURE_NO_VALID_DESTINATION

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code triggered when no reachable destinations remain (e.g., all patrol waypoints are blocked).",
 "type": "integer",
 "value": "0x06"
}
```


## constants/PU_FAILURE_OTHER

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code representing an unspecified or general failure.",
 "type": "integer",
 "value": 1000000
}
```


## constants/PU_FAILURE_PARCEL_UNREACHABLE

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code triggered when a character is blocked from entering a parcel (e.g., the parcel is full or object entry was disabled after the navmesh was baked).",
 "type": "integer",
 "value": 11
}
```


## constants/PU_FAILURE_TARGET_GONE

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code triggered when an llPursue or llEvade target can no longer be tracked (e.g., they left the region or went more than ~30m outside region boundaries).",
 "type": "integer",
 "value": "0x05"
}
```


## constants/PU_FAILURE_UNREACHABLE

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update failure code triggered when a previously valid goal becomes unreachable (e.g., an obstacle blocks the path).",
 "type": "integer",
 "value": "0x04"
}
```


## constants/PU_GOAL_REACHED

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update status code triggered when the character reaches its goal and either stops or chooses a new goal (if wandering).",
 "type": "integer",
 "value": "0x01"
}
```


## constants/PU_SLOWDOWN_DISTANCE_REACHED

```json
{
 "member-of": [
  "CharacterPathUpdateType"
 ],
 "tooltip": "Path update status code triggered when the character enters the slowdown distance near its current goal.",
 "type": "integer",
 "value": "0x00"
}
```


## constants/RAD_TO_DEG

```json
{
 "tooltip": "180/PI. Multiply a value in radians by this number to convert it to degrees.",
 "type": "float",
 "value": "57.2957795"
}
```


## constants/RCERR_CAST_TIME_EXCEEDED

```json
{
 "member-of": [
  "RayCastError"
 ],
 "tooltip": "Raycast error indicating the parcel or agent exceeded the maximum allocated raycast time. Waiting a few frames and retrying will usually succeed as resources replenish.",
 "type": "integer",
 "value": -3
}
```


## constants/RCERR_SIM_PERF_LOW

```json
{
 "member-of": [
  "RayCastError"
 ],
 "tooltip": "Raycast error indicating the request failed due to low simulator performance. Wait before retrying, and if possible, reduce scene complexity.",
 "type": "integer",
 "value": -2
}
```


## constants/RCERR_UNKNOWN

```json
{
 "member-of": [
  "RayCastError"
 ],
 "tooltip": "Raycast error indicating an unspecified failure.",
 "type": "integer",
 "value": -1
}
```


## constants/RC_DATA_FLAGS

```json
{
 "member-of": [
  "RayCastParam"
 ],
 "tooltip": "Flag used with llCastRay to configure returned data.",
 "type": "integer",
 "value": 2,
 "value-type": "integer",
 "enum": "RayCastData",
 "default": 0
}
```


## constants/RC_DETECT_PHANTOM

```json
{
 "member-of": [
  "RayCastParam"
 ],
 "tooltip": "Flag used with llCastRay. If set to TRUE (or non-zero), detects both phantom and volume-detect objects (they cannot be filtered individually). This overrides the RC_REJECT_NONPHYSICAL and RC_REJECT_PHYSICAL settings in RC_REJECT_TYPES.",
 "type": "integer",
 "value": 1,
 "value-type": "boolean",
 "default": false
}
```


## constants/RC_GET_LINK_NUM

```json
{
 "member-of": [
  "RayCastData"
 ],
 "tooltip": "Flag used with llCastRay causing the results stride to include the specific link number that was hit.",
 "type": "integer",
 "value": 4
}
```


## constants/RC_GET_NORMAL

```json
{
 "member-of": [
  "RayCastData"
 ],
 "tooltip": "Flag used with llCastRay causing the results stride to include the surface normal vector of the impact point.",
 "type": "integer",
 "value": 1
}
```


## constants/RC_GET_ROOT_KEY

```json
{
 "member-of": [
  "RayCastData"
 ],
 "tooltip": "Flag used with llCastRay that returns the key of the hit object's root prim instead of the hit child prim.",
 "type": "integer",
 "value": 2
}
```


## constants/RC_MAX_HITS

```json
{
 "member-of": [
  "RayCastParam"
 ],
 "tooltip": "Flag used with llCastRay to set the maximum number of hits to return (up to 256). To avoid performance issues, keep this value small.",
 "type": "integer",
 "value": 3,
 "value-type": "integer",
 "default": 1
}
```


## constants/RC_REJECT_AGENTS

```json
{
 "member-of": [
  "RayCastRejectType"
 ],
 "tooltip": "Flag used with llCastRay to prevent the detection of avatars.",
 "type": "integer",
 "value": 1
}
```


## constants/RC_REJECT_LAND

```json
{
 "member-of": [
  "RayCastRejectType"
 ],
 "tooltip": "Flag used with llCastRay to ignore the actual terrain ground (land).",
 "type": "integer",
 "value": 8
}
```


## constants/RC_REJECT_NONPHYSICAL

```json
{
 "member-of": [
  "RayCastRejectType"
 ],
 "tooltip": "Flag used with llCastRay to ignore non-physical objects.",
 "type": "integer",
 "value": 4
}
```


## constants/RC_REJECT_PHYSICAL

```json
{
 "member-of": [
  "RayCastRejectType"
 ],
 "tooltip": "Flag used with llCastRay to ignore physical objects.",
 "type": "integer",
 "value": 2
}
```


## constants/RC_REJECT_TYPES

```json
{
 "member-of": [
  "RayCastParam"
 ],
 "tooltip": "Flag used with llCastRay to define a mask for ignoring specific types of objects and avatars.",
 "type": "integer",
 "value": 0,
 "value-type": "integer",
 "enum": "RayCastRejectType",
 "default": 0
}
```


## constants/REGION_FLAG_ALLOW_DAMAGE

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if the region is entirely damage-enabled.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/REGION_FLAG_ALLOW_DIRECT_TELEPORT

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if direct teleportation is allowed in the region.",
 "type": "integer",
 "value": "0x100000"
}
```


## constants/REGION_FLAG_BLOCK_FLY

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if flying is blocked/disabled in the region.",
 "type": "integer",
 "value": "0x80000"
}
```


## constants/REGION_FLAG_BLOCK_FLYOVER

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "",
 "type": "integer",
 "value": "0x8000000"
}
```


## constants/REGION_FLAG_BLOCK_TERRAFORM

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if terraforming is disabled in the region.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/REGION_FLAG_DISABLE_COLLISIONS

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if collisions have been disabled in the region.",
 "type": "integer",
 "value": "0x1000"
}
```


## constants/REGION_FLAG_DISABLE_PHYSICS

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if physics has been disabled in the region.",
 "type": "integer",
 "value": "0x4000"
}
```


## constants/REGION_FLAG_FIXED_SUN

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if the sun's position is fixed in the region.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/REGION_FLAG_RESTRICT_PUSHOBJECT

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if llPushObject is restricted in the region.",
 "type": "integer",
 "value": "0x400000"
}
```


## constants/REGION_FLAG_SANDBOX

```json
{
 "member-of": [
  "RegionFlag"
 ],
 "tooltip": "Flag used with llGetRegionFlags to check if the region is designated as a sandbox.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/REMOTE_DATA_CHANNEL

```json
{
 "member-of": [
  "RemoteDataEventType"
 ],
 "deprecated": true,
 "tooltip": "",
 "type": "integer",
 "value": 1
}
```


## constants/REMOTE_DATA_REPLY

```json
{
 "member-of": [
  "RemoteDataEventType"
 ],
 "deprecated": true,
 "tooltip": "",
 "type": "integer",
 "value": 3
}
```


## constants/REMOTE_DATA_REQUEST

```json
{
 "member-of": [
  "RemoteDataEventType"
 ],
 "deprecated": true,
 "tooltip": "",
 "type": "integer",
 "value": 2
}
```


## constants/REQUIRE_LINE_OF_SIGHT

```json
{
 "member-of": [
  "CharacterPursueParam"
 ],
 "tooltip": "Option flag for llPursue defining whether the character requires a physical line-of-sight to chase the target. When active, it will not target positions blocked by solid obstacles.",
 "type": "integer",
 "value": 2,
 "value-type": "boolean",
 "default": false
}
```


## constants/RESTITUTION

```json
{
 "member-of": [
  "PhysicsMaterialParam"
 ],
 "tooltip": "Used with llSetPhysicsMaterial to enable the restitution (bounciness) value (must be between 0.0 and 1.0) which overrides the previous value.",
 "type": "integer",
 "value": 4
}
```


## constants/REVERSE

```json
{
 "member-of": [
  "TextureAnimMode"
 ],
 "tooltip": "Used with texture animation functions to cause the animation to play in reverse (from end to start).",
 "type": "integer",
 "value": "0x4"
}
```


## constants/REZ_ACCEL

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying a constant acceleration force to apply to the rezzed object (as a [vector force, integer relative] pair). If relative is TRUE, the vector is in local coordinates.",
 "type": "integer",
 "value": 5,
 "values": [
  {
   "name": "force",
   "value-type": "vector"
  },
  {
   "name": "local",
   "value-type": "boolean"
  }
 ]
}
```


## constants/REZ_DAMAGE

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying the float damage amount the rezzed object inflicts on an agent upon collision.",
 "type": "integer",
 "value": 8,
 "value-type": "float"
}
```


## constants/REZ_DAMAGE_TYPE

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying the integer damage type applied on collision (supports DAMAGE_TYPE_* constants, custom types, or a repurposed damage field).",
 "type": "integer",
 "value": 12,
 "value-type": "integer",
 "enum": "DamageType"
}
```


## constants/REZ_FLAGS

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying the integer bitfield of flags to apply to the newly created object.",
 "type": "integer",
 "value": 1,
 "value-type": "integer",
 "enum": "RezFlag"
}
```


## constants/REZ_FLAG_BLOCK_GRAB_OBJECT

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag that disables grabbing on the newly rezzed object.",
 "type": "integer",
 "value": "0x0080"
}
```


## constants/REZ_FLAG_DIE_ON_COLLIDE

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag causing the object to die/delete after its first collision.",
 "type": "integer",
 "value": "0x0008"
}
```


## constants/REZ_FLAG_DIE_ON_NOENTRY

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag causing the object to die/delete if it attempts to enter an unauthorized parcel.",
 "type": "integer",
 "value": "0x0010"
}
```


## constants/REZ_FLAG_DIE_ON_NO_REZZER

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag causing the object to die if the rezzing object or agent is not present.",
 "type": "integer",
 "value": "0x0100"
}
```


## constants/REZ_FLAG_NO_COLLIDE_FAMILY

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag preventing collision events from triggering when colliding with other objects created by the same rezzer.",
 "type": "integer",
 "value": "0x0040"
}
```


## constants/REZ_FLAG_NO_COLLIDE_OWNER

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag preventing collision events from triggering when colliding with its owner.",
 "type": "integer",
 "value": "0x0020"
}
```


## constants/REZ_FLAG_PHANTOM

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag causing the object to be created as phantom.",
 "type": "integer",
 "value": "0x0004"
}
```


## constants/REZ_FLAG_PHYSICAL

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag causing the object to be created with physics enabled.",
 "type": "integer",
 "value": "0x0002"
}
```


## constants/REZ_FLAG_TEMP

```json
{
 "member-of": [
  "RezFlag"
 ],
 "tooltip": "Rez flag causing the object to be created as temporary.",
 "type": "integer",
 "value": "0x0001"
}
```


## constants/REZ_LOCK_AXES

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter [vector locks] used to prevent the physical object from rotating or spinning around specified axes. Setting a coordinate to a non-zero value locks that axis.",
 "type": "integer",
 "value": 11,
 "value-type": "vector"
}
```


## constants/REZ_OMEGA

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying the initial angular velocity (omega) applied to the object. Accepts [vector axis, integer relative, float spin, float gain]. If relative is TRUE, the axis vector is in local coordinates.",
 "type": "integer",
 "value": 7,
 "values": [
  {
   "name": "axis",
   "value-type": "vector"
  },
  {
   "name": "local",
   "value-type": "boolean"
  },
  {
   "name": "spin",
   "value-type": "float"
  },
  {
   "name": "gain",
   "value-type": "float"
  }
 ]
}
```


## constants/REZ_PARAM

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying the integer start parameter passed into the newly rezzed object's on_rez event.",
 "type": "integer",
 "value": 0,
 "value-type": "integer"
}
```


## constants/REZ_PARAM_STRING

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying an initialization string (up to 1024 bytes) passed to the root prim of the newly rezzed object, readable via llGetStartString.",
 "type": "integer",
 "value": 13,
 "value-type": "string"
}
```


## constants/REZ_POS

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter [vector position, integer relative, integer at_root] to specify where to rez the object. Can be in region coordinates or relative to the rezzing object, and centered on either the object's center or the root prim.",
 "type": "integer",
 "value": 2,
 "values": [
  {
   "name": "pos",
   "value-type": "vector"
  },
  {
   "name": "relative",
   "value-type": "boolean"
  },
  {
   "name": "at_root",
   "value-type": "boolean"
  }
 ]
}
```


## constants/REZ_ROT

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying the initial rotation to apply to the newly rezzed object. Can be relative to the rezzing object or absolute.",
 "type": "integer",
 "value": 3,
 "values": [
  {
   "name": "rot",
   "value-type": "rotation"
  },
  {
   "name": "relative",
   "value-type": "boolean"
  }
 ]
}
```


## constants/REZ_SOUND

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter [string name_or_uuid, float volume, integer loop] to attach and play a sound from inventory or a UUID asset key. If loop is TRUE, it loops continuously.",
 "type": "integer",
 "value": 9,
 "values": [
  {
   "name": "sound",
   "value-type": "asset"
  },
  {
   "name": "volume",
   "value-type": "float"
  },
  {
   "name": "loop",
   "value-type": "boolean"
  }
 ]
}
```


## constants/REZ_SOUND_COLLIDE

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter [string name_or_uuid, float volume] specifying a sound (from inventory or a UUID asset key) to play upon collision with another object, the ground, or an avatar.",
 "type": "integer",
 "value": 10,
 "values": [
  {
   "name": "sound",
   "value-type": "asset"
  },
  {
   "name": "volume",
   "value-type": "float"
  }
 ]
}
```


## constants/REZ_TORQUE

```json
{
 "member-of": [
  "RezParam"
 ],
 "private": true,
 "tooltip": "",
 "type": "integer",
 "value": 6,
 "value-type": "vector"
}
```


## constants/REZ_VEL

```json
{
 "member-of": [
  "RezParam"
 ],
 "tooltip": "Rez parameter specifying the initial velocity to apply to the object. Accepts [vector velocity, integer local, integer inherit]. If inherit is TRUE, it adds the rezzing object's velocity.",
 "type": "integer",
 "value": 4,
 "values": [
  {
   "name": "velocity",
   "value-type": "vector"
  },
  {
   "name": "local",
   "value-type": "boolean"
  },
  {
   "name": "inherit",
   "value-type": "boolean"
  }
 ]
}
```


## constants/ROTATE

```json
{
 "member-of": [
  "TextureAnimMode"
 ],
 "tooltip": "Used with texture animation functions to animate the texture's rotation. Cannot be combined with SCALE.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/SCALE

```json
{
 "member-of": [
  "TextureAnimMode"
 ],
 "tooltip": "Used with texture animation functions to animate the texture's scale. Cannot be combined with ROTATE.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/SCRIPTED

```json
{
 "member-of": [
  "DetectType"
 ],
 "tooltip": "Identifies scripted in-world objects. In llDetectedType(), indicates the target has at least one active script. In llSensor()/llSensorRepeat() filters, searches for objects containing active scripts that are currently running.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/SIM_STAT_ACTIVE_SCRIPT_COUNT

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the total number of active scripts in the region.",
 "type": "integer",
 "value": 12
}
```


## constants/SIM_STAT_AGENT_COUNT

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the total number of agents in the region.",
 "type": "integer",
 "value": 10
}
```


## constants/SIM_STAT_AGENT_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent in the 'agent' segment of the simulation frame.",
 "type": "integer",
 "value": 7
}
```


## constants/SIM_STAT_AGENT_UPDATES

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the number of agent updates per second.",
 "type": "integer",
 "value": 2
}
```


## constants/SIM_STAT_AI_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent on the AI step.",
 "type": "integer",
 "value": 26
}
```


## constants/SIM_STAT_ASSET_DOWNLOADS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the pending asset download count.",
 "type": "integer",
 "value": 15
}
```


## constants/SIM_STAT_ASSET_UPLOADS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the pending asset upload count.",
 "type": "integer",
 "value": 16
}
```


## constants/SIM_STAT_CHILD_AGENT_COUNT

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the number of child (neighboring) agents in the region.",
 "type": "integer",
 "value": 11
}
```


## constants/SIM_STAT_FRAME_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the total frame time.",
 "type": "integer",
 "value": 3
}
```


## constants/SIM_STAT_IMAGE_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent in the 'image' segment of the simulation frame.",
 "type": "integer",
 "value": 8
}
```


## constants/SIM_STAT_IO_PUMP_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the pump IO time.",
 "type": "integer",
 "value": 24
}
```


## constants/SIM_STAT_NET_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent in the 'network' segment of the simulation frame.",
 "type": "integer",
 "value": 4
}
```


## constants/SIM_STAT_OTHER_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent in the main simulation 'other' segment of the frame, which encapsulates task, script, and miscellaneous updates.",
 "type": "integer",
 "value": 5
}
```


## constants/SIM_STAT_PACKETS_IN

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the average number of incoming packets per second.",
 "type": "integer",
 "value": 13
}
```


## constants/SIM_STAT_PACKETS_OUT

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the average number of outgoing packets per second.",
 "type": "integer",
 "value": 14
}
```


## constants/SIM_STAT_PCT_CHARS_STEPPED

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the percentage of pathfinding characters updated (or skipped) each frame, averaged over the last minute. Corresponds to the 'Characters Updated' stat in the viewer's Statistics Bar.",
 "type": "integer",
 "value": 0
}
```


## constants/SIM_STAT_PHYSICS_FPS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the physics simulation frames per second (FPS).",
 "type": "integer",
 "value": 1
}
```


## constants/SIM_STAT_PHYSICS_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent in the 'physics' segment of the simulation frame.",
 "type": "integer",
 "value": 6
}
```


## constants/SIM_STAT_PHYSICS_OTHER_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the average update time for the physics 'other' segment.",
 "type": "integer",
 "value": 20
}
```


## constants/SIM_STAT_PHYSICS_SHAPE_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the average update time for the physics 'shape' segment.",
 "type": "integer",
 "value": 19
}
```


## constants/SIM_STAT_PHYSICS_STEP_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the average physics step time.",
 "type": "integer",
 "value": 18
}
```


## constants/SIM_STAT_SCRIPT_EPS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the number of script events per second.",
 "type": "integer",
 "value": 21
}
```


## constants/SIM_STAT_SCRIPT_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent in the 'script' segment of the simulation frame.",
 "type": "integer",
 "value": 9
}
```


## constants/SIM_STAT_SCRIPT_RUN_PCT

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the percentage of scripts run during the frame.",
 "type": "integer",
 "value": 25
}
```


## constants/SIM_STAT_SLEEP_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the time spent sleeping.",
 "type": "integer",
 "value": 23
}
```


## constants/SIM_STAT_SPARE_MS

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the spare time left after the frame.",
 "type": "integer",
 "value": 22
}
```


## constants/SIM_STAT_UNACKED_BYTES

```json
{
 "member-of": [
  "SimulatorStat"
 ],
 "tooltip": "Returns the total number of unacknowledged bytes.",
 "type": "integer",
 "value": 17
}
```


## constants/SIT_FLAG_ALLOW_UNSIT

```json
{
 "member-of": [
  "SitFlag"
 ],
 "tooltip": "Sit flag indicating that a seated avatar is allowed to manually stand up (unsit) from a sit target. Applies only to agents who were seated via an LSL script like llSitOnLink.",
 "type": "integer",
 "value": "0x0002"
}
```


## constants/SIT_FLAG_NO_COLLIDE

```json
{
 "member-of": [
  "SitFlag"
 ],
 "tooltip": "Sit flag that disables the avatar's collision volume/hitbox while seated on this sit target.",
 "type": "integer",
 "value": "0x0010"
}
```


## constants/SIT_FLAG_NO_DAMAGE

```json
{
 "member-of": [
  "SitFlag"
 ],
 "tooltip": "Sit flag that prevents damage from being distributed or forwarded to agents sitting on this sit target.",
 "type": "integer",
 "value": "0x0020"
}
```


## constants/SIT_FLAG_SCRIPTED_ONLY

```json
{
 "member-of": [
  "SitFlag"
 ],
 "tooltip": "Sit flag that restricts sits to script-controlled actions only, preventing avatars from manually sitting on this prim.",
 "type": "integer",
 "value": "0x0004"
}
```


## constants/SIT_FLAG_SIT_TARGET

```json
{
 "member-of": [
  "SitFlag"
 ],
 "tooltip": "Read-only sit flag indicating whether the prim has an active sit target. Set or cleared using llSitTarget, llLinkSitTarget, or PRIM_SIT_TARGET, and read via llGetLinkSitFlags or PRIM_SIT_FLAGS.",
 "type": "integer",
 "value": "0x0001"
}
```


## constants/SIT_INVALID_AGENT

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code indicating that the specified agent/avatar ID could not be found or is invalid.",
 "type": "integer",
 "value": -4
}
```


## constants/SIT_INVALID_LINK

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code indicating that the link ID does not specify a valid prim, is not found, or resolves to multiple prims.",
 "type": "integer",
 "value": -5
}
```


## constants/SIT_INVALID_OBJECT

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code returned when attempting to force an avatar to sit on an invalid target (such as an attachment) that cannot be sat upon.",
 "type": "integer",
 "value": -7
}
```


## constants/SIT_NOT_EXPERIENCE

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code returned if the script is not running within a valid experience, lacks a valid experience key, or the experience is not permitted at the current location.",
 "type": "integer",
 "value": -1
}
```


## constants/SIT_NO_ACCESS

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code indicating that the avatar lacks access to the parcel where the target prim/linkset is located.",
 "type": "integer",
 "value": -6
}
```


## constants/SIT_NO_EXPERIENCE_PERMISSION

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code indicating that the agent has not granted experience permissions to force sits.",
 "type": "integer",
 "value": -2
}
```


## constants/SIT_NO_SIT_TARGET

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code indicating that no open or available sit target could be found in the linkset.",
 "type": "integer",
 "value": -3
}
```


## constants/SIT_OK

```json
{
 "member-of": [
  "SitError"
 ],
 "tooltip": "Sit error code indicating that the agent was seated successfully.",
 "type": "integer",
 "value": 1
}
```


## constants/SKY_ABSORPTION_CONFIG

```json
{
 "private": true,
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 16
}
```


## constants/SKY_AMBIENT

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting for the ambient color used in the scene.",
 "type": "integer",
 "value": 0,
 "value-type": "vector"
}
```


## constants/SKY_BLUE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting containing the colors used to calculate blue density and blue horizon in the sky.",
 "type": "integer",
 "value": 22,
 "values": [
  {
   "name": "blue_density",
   "value-type": "vector"
  },
  {
   "name": "blue_horizon",
   "value-type": "vector"
  }
 ]
}
```


## constants/SKY_CLOUDS

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental cloud parameters including color, coverage percentage, scale, variance, scroll speed (X/Y), density, detail exponents, and default texture status.",
 "type": "integer",
 "value": 2,
 "values": [
  {
   "name": "color",
   "value-type": "vector",
   "details": "The color used for the clouds."
  },
  {
   "name": "coverage",
   "value-type": "float",
   "range": [
    0,
    1
   ],
   "details": "The coverage percentage."
  },
  {
   "name": "scale",
   "value-type": "float",
   "range": [
    0,
    3
   ],
   "details": "The scaling applied to the cloud textures."
  },
  {
   "name": "variance",
   "value-type": "float",
   "range": [
    0,
    1
   ],
   "details": "A randomizing factor applied to the main cloud layer."
  },
  {
   "name": "scroll",
   "value-type": "vector",
   "range": [
    "<-50,-50,0>",
    "<50,50,0>"
   ],
   "details": "The scroll speed of the clouds (X is east/west, Y is north/south, Z is unused)."
  },
  {
   "name": "density",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,3>"
   ],
   "details": "The X/Y and D parameter used to generate cloud density."
  },
  {
   "name": "detail",
   "value-type": "vector",
   "range": [
    "<0,0,0>",
    "<1,1,1>"
   ],
   "details": "The X/Y and D parameter used to generate cloud details."
  },
  {
   "name": "is_default",
   "value-type": "boolean",
   "access": "read"
  }
 ]
}
```


## constants/SKY_CLOUD_TEXTURE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting containing the inventory name or UUID of the texture used for the clouds.",
 "type": "integer",
 "value": 19,
 "value-type": "asset",
 "access": "write"
}
```


## constants/SKY_DENSITY_PROFILE_COUNTS

```json
{
 "private": true,
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting representing counts for each density profile type.",
 "type": "integer",
 "value": 3
}
```


## constants/SKY_DOME

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting containing sky dome parameters: offset, radius, and maximum altitude.",
 "type": "integer",
 "value": 4,
 "values": [
  {
   "name": "offset",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  },
  {
   "name": "radius",
   "value-type": "float",
   "range": [
    1000,
    2000
   ]
  },
  {
   "name": "max_altitude",
   "value-type": "float",
   "range": [
    0,
    10000
   ]
  }
 ]
}
```


## constants/SKY_GAMMA

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting for the gamma value applied to the scene (repurposed in viewer 7.0+ as the HDR Scale value in the EEP editor).",
 "type": "integer",
 "value": 5,
 "value-type": "float",
 "range": [
  0,
  20
 ]
}
```


## constants/SKY_GLOW

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting for sun and moon glow parameters: size and focus.",
 "type": "integer",
 "value": 6,
 "values": [
  {
   "name": "glow_size",
   "value-type": "float",
   "range": [
    0.2,
    40
   ]
  },
  {
   "name": "glow_focus",
   "value-type": "float",
   "range": [
    -10,
    10
   ]
  }
 ]
}
```


## constants/SKY_HAZE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting containing the values used to calculate the light scattering impact of blue density and blue horizon on the scene.",
 "type": "integer",
 "value": 23,
 "values": [
  {
   "name": "density",
   "value-type": "float"
  },
  {
   "name": "horizon",
   "value-type": "float"
  },
  {
   "name": "density_multiplier",
   "value-type": "float"
  },
  {
   "name": "distance_multiplier",
   "value-type": "float"
  }
 ]
}
```


## constants/SKY_LIGHT

```json
{
 "member-of": [
  "EnvironmentParamReadOnly"
 ],
 "tooltip": "Environmental setting containing lighting parameters: dominant light direction (unit vector), current light color (fade_color in sRGB), and total ambient color (sRGB).",
 "type": "integer",
 "value": 8,
 "values": [
  {
   "name": "light_direction",
   "value-type": "vector",
   "details": "light_direction: A unit vector indicating the direction of the dominant light source."
  },
  {
   "name": "fade_color",
   "value-type": "vector",
   "details": "fade_color: A color vector representing the current color of the light emitted from the dominant light source (in sRGB space)."
  },
  {
   "name": "total_ambient",
   "value-type": "vector",
   "details": "total_ambient: A color vector representing the current ambient color in use in the scene (in sRGB space)."
  }
 ],
 "access": "read"
}
```


## constants/SKY_MIE_CONFIG

```json
{
 "private": true,
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting for Mie scattering profile parameters.",
 "type": "integer",
 "value": 17
}
```


## constants/SKY_MOON

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental moon parameters: rotation, scale, brightness, is_default_texture, direction vector, ambient color, and diffuse color.",
 "type": "integer",
 "value": 9,
 "values": [
  {
   "name": "rot",
   "value-type": "rotation",
   "details": "The current rotation applied to the moon."
  },
  {
   "name": "scale",
   "value-type": "float",
   "range": [
    0.25,
    20
   ],
   "details": "The current scale applied to the moon's texture."
  },
  {
   "name": "brightness",
   "value-type": "float",
   "range": [
    0,
    1
   ],
   "details": "The moon's brightness."
  },
  {
   "name": "is_default_texture",
   "value-type": "boolean",
   "access": "read"
  },
  {
   "name": "direction",
   "value-type": "vector",
   "details": "A unit vector pointing at the moon.",
   "access": "read"
  },
  {
   "name": "ambient_color",
   "value-type": "vector",
   "details": "The ambient color of the moon.",
   "access": "read"
  },
  {
   "name": "diffuse_color",
   "value-type": "vector",
   "details": "The diffuse color applied to the moon.",
   "access": "read"
  }
 ]
}
```


## constants/SKY_MOON_TEXTURE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting containing the inventory name or UUID of the texture used for the moon.",
 "type": "integer",
 "value": 20,
 "value-type": "asset",
 "access": "write"
}
```


## constants/SKY_PLANET

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental planet rendering parameters: planet_radius, sky_bottom_radius, and sky_top_radius.",
 "type": "integer",
 "value": 10,
 "values": [
  {
   "name": "planet_radius",
   "value-type": "float",
   "range": [
    1000,
    32768
   ]
  },
  {
   "name": "sky_bottom_radius",
   "value-type": "float",
   "range": [
    1000,
    32768
   ]
  },
  {
   "name": "sky_top_radius",
   "value-type": "float",
   "range": [
    1000,
    32768
   ]
  }
 ]
}
```


## constants/SKY_RAYLEIGH_CONFIG

```json
{
 "private": true,
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting for Rayleigh scattering profile parameters.",
 "type": "integer",
 "value": 18
}
```


## constants/SKY_REFLECTION_PROBE_AMBIANCE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting for the minimum ambiance value of all reflection probes. Note: Supported in the GLTF Materials project, requiring compatible viewers and testing areas.",
 "type": "integer",
 "value": 24,
 "value-type": "float",
 "range": [
  0,
  10
 ]
}
```


## constants/SKY_REFRACTION

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental sky refraction parameters for rainbows and optical effects: moisture_level, droplet_radius, and ice_level.",
 "type": "integer",
 "value": 11,
 "values": [
  {
   "name": "moisture_level",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  },
  {
   "name": "droplet_radius",
   "value-type": "float",
   "range": [
    5,
    1000
   ]
  },
  {
   "name": "ice_level",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  }
 ]
}
```


## constants/SKY_STAR_BRIGHTNESS

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting for the brightness value applied to stars.",
 "type": "integer",
 "value": 13,
 "value-type": "float",
 "range": [
  0,
  500
 ]
}
```


## constants/SKY_SUN

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental sun parameters: rotation, scale, color, is_default_texture, direction vector, ambient color, and diffuse color.",
 "type": "integer",
 "value": 14,
 "values": [
  {
   "name": "rot",
   "value-type": "rotation",
   "details": "The current rotation applied to the sun."
  },
  {
   "name": "scale",
   "value-type": "float",
   "range": [
    0.25,
    20
   ],
   "details": "The current scale applied to the sun's texture."
  },
  {
   "name": "sun_color",
   "value-type": "vector"
  },
  {
   "name": "is_default_texture",
   "value-type": "boolean",
   "access": "read"
  },
  {
   "name": "direction",
   "value-type": "vector",
   "details": "A unit vector pointing at the sun.",
   "access": "read"
  },
  {
   "name": "ambient_color",
   "value-type": "vector",
   "details": "The ambient color of the sun.",
   "access": "read"
  },
  {
   "name": "diffuse_color",
   "value-type": "vector",
   "details": "The diffuse color applied to the sun.",
   "access": "read"
  }
 ]
}
```


## constants/SKY_SUN_TEXTURE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting containing the inventory name or UUID of the texture used for the sun.",
 "type": "integer",
 "value": 21,
 "value-type": "asset",
 "access": "write"
}
```


## constants/SKY_TEXTURE_DEFAULTS

```json
{
 "member-of": [
  "EnvironmentParamReadOnly"
 ],
 "tooltip": "Environmental check returning 1 if the sky textures are set to their default values, or 0 if they use custom textures.",
 "type": "integer",
 "value": 1,
 "values": [
  {
   "name": "bloom_is_default",
   "value-type": "boolean"
  },
  {
   "name": "halo_is_default",
   "value-type": "boolean"
  },
  {
   "name": "rainbow_is_default",
   "value-type": "boolean"
  }
 ],
 "access": "read"
}
```


## constants/SKY_TRACKS

```json
{
 "member-of": [
  "EnvironmentParamReadOnly"
 ],
 "tooltip": "Environmental setting containing the track altitudes used for sky transitions in the region.",
 "type": "integer",
 "value": 15,
 "values": [
  {
   "name": "sky2",
   "value-type": "float"
  },
  {
   "name": "sky3",
   "value-type": "float"
  },
  {
   "name": "sky4",
   "value-type": "float"
  }
 ],
 "access": "read"
}
```


## constants/SMOOTH

```json
{
 "member-of": [
  "TextureAnimMode"
 ],
 "tooltip": "Used with texture animation functions to cause the animation to slide smoothly in the X direction (or transition smoothly in SCALE/ROTATE modes) instead of making instant frame changes.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/SOUND_LOOP

```json
{
 "member-of": [
  "PlaySoundFlag"
 ],
 "tooltip": "Sound playback option that loops the sound continuously on the prim until stopped.",
 "type": "integer",
 "value": "0x01"
}
```


## constants/SOUND_PLAY

```json
{
 "member-of": [
  "PlaySoundFlag"
 ],
 "tooltip": "Sound playback option (default) that plays the sound once, attached to the prim.",
 "type": "integer",
 "value": "0x00"
}
```


## constants/SOUND_SYNC

```json
{
 "member-of": [
  "PlaySoundFlag"
 ],
 "tooltip": "Sound playback option that synchronizes playback to the nearest active sound master (see llLoopSoundMaster).",
 "type": "integer",
 "value": "0x04"
}
```


## constants/SOUND_TRIGGER

```json
{
 "member-of": [
  "PlaySoundFlag"
 ],
 "tooltip": "Sound playback option that triggers a non-attached sound once at the prim's current location (does not move with the prim). This flag overrides all other sound playback options.",
 "type": "integer",
 "value": "0x02"
}
```


## constants/SQRT2

```json
{
 "tooltip": "Mathematical constant representing the square root of 2.",
 "type": "float",
 "value": "1.41421356",
 "slua-deprecated": {
  "use": "math.sqrt2",
  "reason": "Double precision."
 }
}
```


## constants/STATUS_BLOCK_GRAB

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default FALSE) that blocks click-and-drag grab movements on unlinked prims or the root prim of a linkset. Useful for preventing physical objects from being trivially disturbed.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/STATUS_BLOCK_GRAB_OBJECT

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag that blocks click-and-drag grab movements on all prims across the entire linkset.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/STATUS_BOUNDS_ERROR

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating that one or more arguments passed to the function had a bounds error.",
 "type": "integer",
 "value": 1002
}
```


## constants/STATUS_CAST_SHADOWS

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "deprecated": {
  "reason": "Not implemented."
 },
 "tooltip": "Unused legacy status flag intended to configure an object's ability to cast shadows.",
 "type": "integer",
 "value": "0x200"
}
```


## constants/STATUS_DIE_AT_EDGE

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default TRUE) that causes the object to be deleted (and not returned) if it goes off-world (useful for bullets or rockets). Overridden by STATUS_RETURN_AT_EDGE.",
 "type": "integer",
 "value": "0x80"
}
```


## constants/STATUS_DIE_AT_NO_ENTRY

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default FALSE) that causes the object to be deleted if it attempts to enter an unauthorized or full parcel. No-copy objects ignore this setting and remain in-world.",
 "type": "integer",
 "value": "0x800"
}
```


## constants/STATUS_DIE_ON_NO_REZZER

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default FALSE) that causes the object to be deleted if the rezzing object or agent is not present.",
 "type": "integer",
 "value": "0x1000"
}
```


## constants/STATUS_INTERNAL_ERROR

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating an internal error occurred.",
 "type": "integer",
 "value": 1999
}
```


## constants/STATUS_MALFORMED_PARAMS

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating the function was called with malformed parameters.",
 "type": "integer",
 "value": 1000
}
```


## constants/STATUS_NOT_FOUND

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating that the specified object or item was not found.",
 "type": "integer",
 "value": 1003
}
```


## constants/STATUS_NOT_SUPPORTED

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating the requested feature is not supported.",
 "type": "integer",
 "value": 1004
}
```


## constants/STATUS_OK

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating the function call completed successfully.",
 "type": "integer",
 "value": 0
}
```


## constants/STATUS_PHANTOM

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default FALSE) that makes the entire object phantom/non-colliding when set to TRUE, allowing avatars and objects to pass through it. It is a good idea to use this for most objects that move or rotate, but are non-physical. It is also useful for simulating volumetric lighting.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/STATUS_PHYSICS

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default FALSE) that controls whether the object responds to physical interactions, gravity, and forces.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/STATUS_RETURN_AT_EDGE

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag causing the object to be returned to its owner when it goes off-world, overriding STATUS_DIE_AT_EDGE.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/STATUS_ROTATE_X

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default TRUE) that allows physical rotation on the object's local X-axis. Setting to FALSE prevents physical rotation around the local X-axis. For example, a sit-and-spin device spins around the Z axis (up) but not around the X or Y axes.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/STATUS_ROTATE_Y

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default TRUE) that allows physical rotation on the object's local Y-axis. Setting to FALSE prevents physical rotation around the local Y-axis. For example, a sit-and-spin device spins around the Z axis (up) but not around the X or Y axes.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/STATUS_ROTATE_Z

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default TRUE) that allows physical rotation on the object's local Z-axis. Setting to FALSE prevents physical rotation around the local Z-axis.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/STATUS_SANDBOX

```json
{
 "member-of": [
  "ObjectStatusParam"
 ],
 "tooltip": "Status flag (default FALSE) that restricts the object's physical movement to within its creation region and a short distance (10 to 20 meters) from its creation point to prevent it from escaping.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/STATUS_TYPE_MISMATCH

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating that one or more arguments passed to the function had a type mismatch.",
 "type": "integer",
 "value": 1001
}
```


## constants/STATUS_WHITELIST_FAILED

```json
{
 "member-of": [
  "PrimMediaError"
 ],
 "tooltip": "Status code indicating a media domain whitelist check has failed.",
 "type": "integer",
 "value": 2001
}
```


## constants/STRING_TRIM

```json
{
 "member-of": [
  "StringTrimType"
 ],
 "tooltip": "Trims whitespace off both the beginning and the end of the string.",
 "type": "integer",
 "value": "0x03"
}
```


## constants/STRING_TRIM_HEAD

```json
{
 "member-of": [
  "StringTrimType"
 ],
 "tooltip": "Trims whitespace/spaces off the beginning of the string.",
 "type": "integer",
 "value": "0x01"
}
```


## constants/STRING_TRIM_TAIL

```json
{
 "member-of": [
  "StringTrimType"
 ],
 "tooltip": "Trims whitespace/spaces off the end of the string.",
 "type": "integer",
 "value": "0x02"
}
```


## constants/TARGETED_EMAIL_OBJECT_OWNER

```json
{
 "member-of": [
  "EmailTarget"
 ],
 "tooltip": "Flag used with llTargetedEmail to send the email message to the owner of the calling object.",
 "type": "integer",
 "value": "0x02"
}
```


## constants/TARGETED_EMAIL_ROOT_CREATOR

```json
{
 "member-of": [
  "EmailTarget"
 ],
 "tooltip": "Flag used with llTargetedEmail to send the email message to the creator of the root object.",
 "type": "integer",
 "value": "0x01"
}
```


## constants/TERRAIN_DETAIL_1

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 1.",
 "type": "integer",
 "value": 0,
 "value-type": "asset"
}
```


## constants/TERRAIN_DETAIL_2

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 2.",
 "type": "integer",
 "value": 1,
 "value-type": "asset"
}
```


## constants/TERRAIN_DETAIL_3

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 3.",
 "type": "integer",
 "value": 2,
 "value-type": "asset"
}
```


## constants/TERRAIN_DETAIL_4

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 4.",
 "type": "integer",
 "value": 3,
 "value-type": "asset"
}
```


## constants/TERRAIN_HEIGHT_RANGE_NE

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the north-east height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.",
 "type": "integer",
 "value": 7,
 "values": [
  {
   "name": "low",
   "value-type": "float"
  },
  {
   "name": "high",
   "value-type": "float"
  }
 ]
}
```


## constants/TERRAIN_HEIGHT_RANGE_NW

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the north-west height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.",
 "type": "integer",
 "value": 6,
 "values": [
  {
   "name": "low",
   "value-type": "float"
  },
  {
   "name": "high",
   "value-type": "float"
  }
 ]
}
```


## constants/TERRAIN_HEIGHT_RANGE_SE

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the south-east height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.",
 "type": "integer",
 "value": 5,
 "values": [
  {
   "name": "low",
   "value-type": "float"
  },
  {
   "name": "high",
   "value-type": "float"
  }
 ]
}
```


## constants/TERRAIN_HEIGHT_RANGE_SW

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the south-west height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.",
 "type": "integer",
 "value": 4,
 "values": [
  {
   "name": "low",
   "value-type": "float"
  },
  {
   "name": "high",
   "value-type": "float"
  }
 ]
}
```


## constants/TERRAIN_PBR_OFFSET_1

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 1. Only works for PBR textures.",
 "type": "integer",
 "value": 16,
 "value-type": "vector"
}
```


## constants/TERRAIN_PBR_OFFSET_2

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 2. Only works for PBR textures.",
 "type": "integer",
 "value": 17,
 "value-type": "vector"
}
```


## constants/TERRAIN_PBR_OFFSET_3

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 3. Only works for PBR textures.",
 "type": "integer",
 "value": 18,
 "value-type": "vector"
}
```


## constants/TERRAIN_PBR_OFFSET_4

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 4. Only works for PBR textures.",
 "type": "integer",
 "value": 19,
 "value-type": "vector"
}
```


## constants/TERRAIN_PBR_ROTATION_1

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 1, in radians. Only works for PBR textures.",
 "type": "integer",
 "value": 12,
 "value-type": "float"
}
```


## constants/TERRAIN_PBR_ROTATION_2

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 2, in radians. Only works for PBR textures.",
 "type": "integer",
 "value": 13,
 "value-type": "float"
}
```


## constants/TERRAIN_PBR_ROTATION_3

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 3, in radians. Only works for PBR textures.",
 "type": "integer",
 "value": 14,
 "value-type": "float"
}
```


## constants/TERRAIN_PBR_ROTATION_4

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 4, in radians. Only works for PBR textures.",
 "type": "integer",
 "value": 15,
 "value-type": "float"
}
```


## constants/TERRAIN_PBR_SCALE_1

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 1. Only works for PBR textures.",
 "type": "integer",
 "value": 8,
 "value-type": "vector"
}
```


## constants/TERRAIN_PBR_SCALE_2

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 2. Only works for PBR textures.",
 "type": "integer",
 "value": 9,
 "value-type": "vector"
}
```


## constants/TERRAIN_PBR_SCALE_3

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 3. Only works for PBR textures.",
 "type": "integer",
 "value": 10,
 "value-type": "vector"
}
```


## constants/TERRAIN_PBR_SCALE_4

```json
{
 "member-of": [
  "GroundTextureParam"
 ],
 "tooltip": "Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 4. Only works for PBR textures.",
 "type": "integer",
 "value": 11,
 "value-type": "vector"
}
```


## constants/TEXTURE_BLANK

```json
{
 "tooltip": "Asset UUID representing the default 'Blank' texture.",
 "type": "string",
 "slua-type": "uuid",
 "value": "5748decc-f629-461c-9a36-a35a221fe21f"
}
```


## constants/TEXTURE_DEFAULT

```json
{
 "tooltip": "",
 "type": "string",
 "slua-type": "uuid",
 "value": "89556747-24cb-43ed-920b-47caed15465f"
}
```


## constants/TEXTURE_MEDIA

```json
{
 "tooltip": "Asset UUID representing the default 'Default Media' texture.",
 "type": "string",
 "slua-type": "uuid",
 "value": "8b5fec65-8d8d-9dc5-cda8-8fdf2716e361"
}
```


## constants/TEXTURE_PLYWOOD

```json
{
 "tooltip": "Asset UUID representing the default 'Plywood' texture.",
 "type": "string",
 "slua-type": "uuid",
 "value": "89556747-24cb-43ed-920b-47caed15465f"
}
```


## constants/TEXTURE_TRANSPARENT

```json
{
 "tooltip": "Asset UUID representing the '*Default Transparent Texture' in the library (included with viewers).",
 "type": "string",
 "slua-type": "uuid",
 "value": "8dcd4a48-2d37-4909-9f78-f7a9eb4ef903"
}
```


## constants/TOUCH_INVALID_FACE

```json
{
 "tooltip": "Value returned by llDetectedTouchFace when the touch position is not valid.",
 "type": "integer",
 "value": -1
}
```


## constants/TOUCH_INVALID_TEXCOORD

```json
{
 "tooltip": "Value returned by llDetectedTouchUV and llDetectedTouchST when the touch position is not valid.",
 "type": "vector",
 "value": "<-1.0, -1.0, 0.0>"
}
```


## constants/TOUCH_INVALID_VECTOR

```json
{
 "tooltip": "Value returned by llDetectedTouchPos, llDetectedTouchNormal, and llDetectedTouchBinormal when the touch position is not valid.",
 "type": "vector",
 "value": "<0.0, 0.0, 0.0>"
}
```


## constants/TP_ROUTING_BLOCKED

```json
{
 "member-of": [
  "ParcelTeleportRouting"
 ],
 "tooltip": "Teleport routing setting indicating that direct teleporting is blocked on the parcel.",
 "type": "integer",
 "value": 0
}
```


## constants/TP_ROUTING_FREE

```json
{
 "member-of": [
  "ParcelTeleportRouting"
 ],
 "tooltip": "Teleport routing setting indicating that teleports are unrestricted on the parcel.",
 "type": "integer",
 "value": 2
}
```


## constants/TP_ROUTING_LANDINGP

```json
{
 "member-of": [
  "ParcelTeleportRouting"
 ],
 "tooltip": "Teleport routing setting indicating that teleports are routed to the parcel's landing point (if one has been set).",
 "type": "integer",
 "value": 1
}
```


## constants/TRANSFER_BAD_OPTS

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Inventory transfer error code indicating that an invalid option was passed in the options list.",
 "type": "integer",
 "value": -1
}
```


## constants/TRANSFER_BAD_ROOT

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Inventory transfer error code indicating that the root path specified in TRANSFER_DEST was invalid or resolved to nothing.",
 "type": "integer",
 "value": -5
}
```


## constants/TRANSFER_DEST

```json
{
 "member-of": [
  "GiveAgentInventoryParam"
 ],
 "tooltip": "Inventory option specifying the destination root folder to transfer inventory into.",
 "type": "integer",
 "value": 0,
 "value-type": "string"
}
```


## constants/TRANSFER_FLAGS

```json
{
 "member-of": [
  "GiveAgentInventoryParam"
 ],
 "tooltip": "Inventory parameter specifying flags to control the behavior of inventory transfers.",
 "type": "integer",
 "value": 1,
 "value-type": "integer",
 "enum": "GiveAgentInventoryFlag"
}
```


## constants/TRANSFER_FLAG_COPY

```json
{
 "member-of": [
  "TransferOwnershipFlag"
 ],
 "tooltip": "Inventory transfer flag that copies the transferred object and places it in the recipient's inventory (implies TRANSFER_FLAG_TAKE).",
 "type": "integer",
 "value": "0x0004"
}
```


## constants/TRANSFER_FLAG_RESERVED

```json
{
 "member-of": [
  "TransferOwnershipFlag"
 ],
 "tooltip": "Inventory transfer flag reserved for future expansion; do not use.",
 "type": "integer",
 "value": "0x0001"
}
```


## constants/TRANSFER_FLAG_TAKE

```json
{
 "member-of": [
  "TransferOwnershipFlag"
 ],
 "tooltip": "Inventory transfer flag that automatically removes the object from the world and places it in the recipient's inventory once accepted.",
 "type": "integer",
 "value": "0x0002"
}
```


## constants/TRANSFER_NO_ATTACHMENT

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Inventory transfer error code indicating ownership of an attached object cannot be transferred.",
 "type": "integer",
 "value": -7
}
```


## constants/TRANSFER_NO_ITEMS

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Inventory transfer error code indicating that the list was empty or contained only non-transferable items.",
 "type": "integer",
 "value": -4
}
```


## constants/TRANSFER_NO_PERMS

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Inventory transfer error code indicating the object lacks transfer permissions.",
 "type": "integer",
 "value": -6
}
```


## constants/TRANSFER_NO_TARGET

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Inventory transfer error code indicating the receiving agent could not be found in the current region.",
 "type": "integer",
 "value": -2
}
```


## constants/TRANSFER_OK

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Status code indicating that the inventory transfer was successful or the transfer offer was successfully made.",
 "type": "integer",
 "value": 0
}
```


## constants/TRANSFER_THROTTLE

```json
{
 "member-of": [
  "TransferError"
 ],
 "tooltip": "Inventory transfer error code indicating that the transfer rate has exceeded the inventory transfer throttle.",
 "type": "integer",
 "value": -3
}
```


## constants/TRAVERSAL_TYPE

```json
{
 "member-of": [
  "CharacterParam"
 ],
 "tooltip": "Pathfinding parameter specifying the character's movement traversal type. Expects TRAVERSAL_TYPE_SLOW (default), _FAST, or _NONE.",
 "type": "integer",
 "value": 7,
 "value-type": "integer",
 "enum": "CharacterTraversalType",
 "default": "TRAVERSAL_TYPE_SLOW"
}
```


## constants/TRAVERSAL_TYPE_FAST

```json
{
 "member-of": [
  "CharacterTraversalType"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 1
}
```


## constants/TRAVERSAL_TYPE_NONE

```json
{
 "member-of": [
  "CharacterTraversalType"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 2
}
```


## constants/TRAVERSAL_TYPE_SLOW

```json
{
 "member-of": [
  "CharacterTraversalType"
 ],
 "tooltip": "",
 "type": "integer",
 "value": 0
}
```


## constants/TRUE

```json
{
 "tooltip": "Mnemonic constant representing a boolean TRUE value (integer 1). Used in conditional structures or variables to improve script readability.",
 "type": "integer",
 "slua-removed": true,
 "value": 1
}
```


## constants/TWO_PI

```json
{
 "tooltip": "Mathematical constant pi*2, representing the number of radians in a full circle.",
 "type": "float",
 "value": "6.28318530",
 "slua-deprecated": {
  "use": "math.tau",
  "reason": "Double precision."
 }
}
```


## constants/TYPE_FLOAT

```json
{
 "member-of": [
  "ListEntryType"
 ],
 "slua-deprecated": {
  "use": "\"number\""
 },
 "tooltip": "Variable type constant indicating the list entry or value is a float.",
 "type": "integer",
 "value": 2
}
```


## constants/TYPE_INTEGER

```json
{
 "member-of": [
  "ListEntryType"
 ],
 "slua-deprecated": {
  "use": "\"number\""
 },
 "tooltip": "Variable type constant indicating the list entry or value is an integer.",
 "type": "integer",
 "value": 1
}
```


## constants/TYPE_INVALID

```json
{
 "member-of": [
  "ListEntryType"
 ],
 "slua-deprecated": {
  "use": "nil"
 },
 "tooltip": "Variable type constant indicating the list entry or value is invalid.",
 "type": "integer",
 "value": 0
}
```


## constants/TYPE_KEY

```json
{
 "member-of": [
  "ListEntryType"
 ],
 "slua-deprecated": {
  "use": "\"uuid\""
 },
 "tooltip": "Variable type constant indicating the list entry or value is a key.",
 "type": "integer",
 "value": 4
}
```


## constants/TYPE_ROTATION

```json
{
 "member-of": [
  "ListEntryType"
 ],
 "slua-deprecated": {
  "use": "\"quaternion\""
 },
 "tooltip": "Variable type constant indicating the list entry or value is a rotation.",
 "type": "integer",
 "value": 6
}
```


## constants/TYPE_STRING

```json
{
 "member-of": [
  "ListEntryType"
 ],
 "slua-deprecated": {
  "use": "\"string\""
 },
 "tooltip": "Variable type constant indicating the list entry or value is a string.",
 "type": "integer",
 "value": 3
}
```


## constants/TYPE_VECTOR

```json
{
 "member-of": [
  "ListEntryType"
 ],
 "slua-deprecated": {
  "use": "\"vector\""
 },
 "tooltip": "Variable type constant indicating the list entry or value is a vector.",
 "type": "integer",
 "value": 5
}
```


## constants/URL_REQUEST_DENIED

```json
{
 "tooltip": "",
 "type": "string",
 "value": "URL_REQUEST_DENIED"
}
```


## constants/URL_REQUEST_GRANTED

```json
{
 "tooltip": "",
 "type": "string",
 "value": "URL_REQUEST_GRANTED"
}
```


## constants/VEHICLE_ANGULAR_DEFLECTION_EFFICIENCY

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter (range 0.0 to 1.0) acting as a scalar to modulate the strength of angular deflection, reorienting the vehicle's preferred axis toward its true velocity.",
 "type": "integer",
 "value": 32,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/VEHICLE_ANGULAR_DEFLECTION_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale for the vehicle to achieve full angular deflection, reorienting its preferred axis of motion to match its true velocity.",
 "type": "integer",
 "value": 33,
 "value-type": "float"
}
```


## constants/VEHICLE_ANGULAR_FRICTION_TIMESCALE

```json
{
 "member-of": [
  "VehicleVectorParam"
 ],
 "tooltip": "Vehicle vector parameter specifying the timescales (range [0.07, infinity) seconds per axis) for the exponential decay of angular velocity about the vehicle's preferred axes (at, left, up).",
 "type": "integer",
 "value": 17,
 "value-type": "vector",
 "range": [
  "<0.07,0.07,0.07>",
  "<inf,inf,inf>"
 ]
}
```


## constants/VEHICLE_ANGULAR_MOTOR_DECAY_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale (in seconds) for the angular motor's magnitude and effectiveness to decay toward zero.",
 "type": "integer",
 "value": 35,
 "value-type": "float",
 "range": [
  0,
  120
 ]
}
```


## constants/VEHICLE_ANGULAR_MOTOR_DIRECTION

```json
{
 "member-of": [
  "VehicleVectorParam"
 ],
 "tooltip": "Vehicle vector parameter specifying the direction and magnitude of the angular velocity (in radians per second) that the vehicle's angular motor attempts to achieve.",
 "type": "integer",
 "value": 19,
 "value-type": "vector",
 "range": [
  "<0,0,0>",
  "<12.56637,12.56637,12.56637>"
 ]
}
```


## constants/VEHICLE_ANGULAR_MOTOR_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale for the vehicle's angular motor to achieve full power and velocity.",
 "type": "integer",
 "value": 34,
 "value-type": "float"
}
```


## constants/VEHICLE_BANKING_EFFICIENCY

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter (range -1.0 to 1.0) controlling banking efficiency, where negative values lean out of turns and positive values lean into turns. This parameter makes banking affect steering; use angular motors to bank. 0.0 means no banking.",
 "type": "integer",
 "value": 38,
 "value-type": "float",
 "range": [
  -1,
  1
 ]
}
```


## constants/VEHICLE_BANKING_MIX

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter (range 0.0 (static) to 1.0) (dynamic) controlling the mix between static banking (scales only with roll angle) and dynamic banking (additionally scales with linear speed).",
 "type": "integer",
 "value": 39,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/VEHICLE_BANKING_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale for the banking behavior to take full effect. This is another way to scale the strength of the banking effect, however it affects the term that is proportional to the difference between what the banking behavior is trying to do, and what the vehicle is actually doing.",
 "type": "integer",
 "value": 40,
 "value-type": "float"
}
```


## constants/VEHICLE_BUOYANCY

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter (range -1.0 to 1.0) defining buoyancy, where -1.0 represents double gravity and 1.0 represents full anti-gravity.",
 "type": "integer",
 "value": 27,
 "value-type": "float",
 "range": [
  -1,
  1
 ]
}
```


## constants/VEHICLE_FLAG_BLOCK_INTERFERENCE

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that prevents attachments worn by passengers from pushing the vehicle via llPushObject or other scripting functions.",
 "type": "integer",
 "value": "0x400"
}
```


## constants/VEHICLE_FLAG_CAMERA_DECOUPLED

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag used with mouselook steering/banking. When set, the passenger's mouselook camera rotates independently of the vehicle's orientation.",
 "type": "integer",
 "value": "0x200"
}
```


## constants/VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that forces the hover behavior to maintain a global height rather than hovering relative to the ground or water.",
 "type": "integer",
 "value": "0x10"
}
```


## constants/VEHICLE_FLAG_HOVER_TERRAIN_ONLY

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that forces the hover behavior to ignore water height and hover exclusively relative to the terrain/land.",
 "type": "integer",
 "value": "0x8"
}
```


## constants/VEHICLE_FLAG_HOVER_UP_ONLY

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag preventing hover from pushing downward, allowing hovering vehicles to jump or fly above their designated hover height.",
 "type": "integer",
 "value": "0x20"
}
```


## constants/VEHICLE_FLAG_HOVER_WATER_ONLY

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that forces the hover behavior to ignore terrain height and hover exclusively relative to water.",
 "type": "integer",
 "value": "0x4"
}
```


## constants/VEHICLE_FLAG_LIMIT_MOTOR_UP

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that prevents ground vehicles from motoring upward into the sky. When combined with banking, banking strength decays when the vehicle is airborne (no longer colliding) to prevent steering mid-jump.",
 "type": "integer",
 "value": "0x40"
}
```


## constants/VEHICLE_FLAG_LIMIT_ROLL_ONLY

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag for vehicles with a vertical attractor that need to climb or dive, allowing airplanes to use the banking feature.",
 "type": "integer",
 "value": "0x2"
}
```


## constants/VEHICLE_FLAG_MOUSELOOK_BANK

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that enables mouselook control, remapping left-right camera motions (yaw) to rotations about the vehicle's local X-axis.",
 "type": "integer",
 "value": "0x100"
}
```


## constants/VEHICLE_FLAG_MOUSELOOK_STEER

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that enables steering via mouse, directing the angular motor to align the vehicle's local X-axis with the direction of the client-side camera.",
 "type": "integer",
 "value": "0x80"
}
```


## constants/VEHICLE_FLAG_NO_DEFLECTION_UP

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "tooltip": "Vehicle flag that prevents linear deflection parallel to the world Z-axis, preventing ground vehicles (such as bumper cars) from climbing into the sky.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/VEHICLE_FLAG_NO_FLY_UP

```json
{
 "member-of": [
  "VehicleFlag"
 ],
 "deprecated": {
  "use": "VEHICLE_FLAG_NO_DEFLECTION_UP"
 },
 "tooltip": "Obsolete legacy name for VEHICLE_FLAG_NO_DEFLECTION_UP.",
 "type": "integer",
 "value": "0x1"
}
```


## constants/VEHICLE_HOVER_EFFICIENCY

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter (range 0.0 to 1.0) controlling hover damping, where 0.0 is bouncy and 1.0 is critically damped.",
 "type": "integer",
 "value": 25,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/VEHICLE_HOVER_HEIGHT

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the height at which the vehicle attempts to hover. Set to 0.0 to disable hover.",
 "type": "integer",
 "value": 24,
 "value-type": "float"
}
```


## constants/VEHICLE_HOVER_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the timescale (period of time in seconds) for the vehicle to achieve its hover height.",
 "type": "integer",
 "value": 26,
 "value-type": "float"
}
```


## constants/VEHICLE_LINEAR_DEFLECTION_EFFICIENCY

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter (range 0.0 to 1.0) modulating the efficiency and strength of linear deflection. That is, its a simple scalar for modulating the strength of linear deflection.",
 "type": "integer",
 "value": 28,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/VEHICLE_LINEAR_DEFLECTION_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale for the vehicle to redirect its linear velocity along its preferred X-axis. It is another way to specify how much time it takes for the vehicle's linear velocity to be redirected to its preferred axis of motion.",
 "type": "integer",
 "value": 29,
 "value-type": "float"
}
```


## constants/VEHICLE_LINEAR_FRICTION_TIMESCALE

```json
{
 "member-of": [
  "VehicleVectorParam"
 ],
 "tooltip": "Vehicle vector parameter specifying the timescales (range [0.07, infinity) seconds per axis) for the exponential decay of linear velocity along the vehicle's preferred axes (at, left, up).",
 "type": "integer",
 "value": 16,
 "value-type": "vector",
 "range": [
  "<0.07,0.07,0.07>",
  "<inf,inf,inf>"
 ]
}
```


## constants/VEHICLE_LINEAR_MOTOR_DECAY_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale (in seconds) for the linear motor's magnitude and effectiveness to decay toward zero.",
 "type": "integer",
 "value": 31,
 "value-type": "float",
 "range": [
  0,
  120
 ]
}
```


## constants/VEHICLE_LINEAR_MOTOR_DIRECTION

```json
{
 "member-of": [
  "VehicleVectorParam"
 ],
 "tooltip": "Vehicle vector parameter specifying the direction and magnitude of the linear velocity (range [0, 30] m/s) that the vehicle's linear motor attempts to achieve.",
 "type": "integer",
 "value": 18,
 "value-type": "vector",
 "range": [
  "<0,0,0>",
  "<30,30,30>"
 ]
}
```


## constants/VEHICLE_LINEAR_MOTOR_OFFSET

```json
{
 "member-of": [
  "VehicleVectorParam"
 ],
 "tooltip": "Vehicle vector parameter specifying the offset from the vehicle's center of mass where the linear motor force is applied.",
 "type": "integer",
 "value": 20,
 "value-type": "vector"
}
```


## constants/VEHICLE_LINEAR_MOTOR_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale for the vehicle to reach its full linear motor velocity.",
 "type": "integer",
 "value": 30,
 "value-type": "float"
}
```


## constants/VEHICLE_REFERENCE_FRAME

```json
{
 "member-of": [
  "VehicleRotationParam"
 ],
 "tooltip": "Vehicle rotation parameter setting the orientation of the vehicle's preferred axes of motion (at, left, up) relative to its local geometric frame (x, y, z).",
 "type": "integer",
 "value": 44,
 "value-type": "rotation"
}
```


## constants/VEHICLE_TYPE_AIRPLANE

```json
{
 "member-of": [
  "VehicleType"
 ],
 "tooltip": "Vehicle type constant for aircraft that use linear deflection for lift, banking to turn, and no hover.",
 "type": "integer",
 "value": 4
}
```


## constants/VEHICLE_TYPE_BALLOON

```json
{
 "member-of": [
  "VehicleType"
 ],
 "tooltip": "Vehicle type constant for balloons that use hover and friction but no deflection.",
 "type": "integer",
 "value": 5
}
```


## constants/VEHICLE_TYPE_BOAT

```json
{
 "member-of": [
  "VehicleType"
 ],
 "tooltip": "Vehicle type constant for boats that hover over water with high friction and minor angular deflection.",
 "type": "integer",
 "value": 3
}
```


## constants/VEHICLE_TYPE_CAR

```json
{
 "member-of": [
  "VehicleType"
 ],
 "tooltip": "Vehicle type constant for land vehicles that bounce along the ground and rely on external controls or timer events to drive their motors.",
 "type": "integer",
 "value": 2
}
```


## constants/VEHICLE_TYPE_NONE

```json
{
 "member-of": [
  "VehicleType"
 ],
 "tooltip": "Constant used to disable and turn off vehicle physics support on the object.",
 "type": "integer",
 "value": 0
}
```


## constants/VEHICLE_TYPE_SLED

```json
{
 "member-of": [
  "VehicleType"
 ],
 "tooltip": "Vehicle type constant for sliding vehicles that bump along the ground and prefer to move along their local X-axis.",
 "type": "integer",
 "value": 1
}
```


## constants/VEHICLE_VERTICAL_ATTRACTION_EFFICIENCY

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter (range 0.0 to 1.0) controlling vertical attraction stability (0.0 is wobbly/bouncy, 1.0 is critically damped/firm) to keep the vehicle upright.",
 "type": "integer",
 "value": 36,
 "value-type": "float",
 "range": [
  0,
  1
 ]
}
```


## constants/VEHICLE_VERTICAL_ATTRACTION_TIMESCALE

```json
{
 "member-of": [
  "VehicleFloatParam"
 ],
 "tooltip": "Vehicle float parameter specifying the exponential timescale (in seconds) for the vehicle to rotate and align its local Z-axis (up) with the world Z-axis (vertical).",
 "type": "integer",
 "value": 37,
 "value-type": "float"
}
```


## constants/VERTICAL

```json
{
 "member-of": [
  "CharacterOrientation"
 ],
 "tooltip": "Constant indicating that the collision capsule orientation for a pathfinding character is vertical.",
 "type": "integer",
 "value": 0
}
```


## constants/WANDER_PAUSE_AT_WAYPOINTS

```json
{
 "member-of": [
  "CharacterWanderWithinParam"
 ],
 "tooltip": "Option parameter for llWanderWithin specifying whether the character should pause briefly after reaching each wander waypoint.",
 "type": "integer",
 "value": 0,
 "value-type": "boolean",
 "default": false
}
```


## constants/WATER_BLUR_MULTIPLIER

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting specifying the multiplier applied to blur the scene when underwater.",
 "type": "integer",
 "value": 100,
 "value-type": "float",
 "range": [
  -0.5,
  0.5
 ]
}
```


## constants/WATER_FOG

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental underwater fog parameters: color, density exponent, and modulation.",
 "type": "integer",
 "value": 101,
 "values": [
  {
   "name": "color",
   "value-type": "vector",
   "details": "The color of the underwater fog."
  },
  {
   "name": "density",
   "value-type": "float",
   "range": [
    -10,
    10
   ],
   "details": "Density exponent applied to the fog."
  },
  {
   "name": "modulation",
   "value-type": "float",
   "range": [
    0,
    20
   ]
  }
 ]
}
```


## constants/WATER_FRESNEL

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental water surface Fresnel scattering parameters: offset and scale.",
 "type": "integer",
 "value": 102,
 "values": [
  {
   "name": "offset",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  },
  {
   "name": "scale",
   "value-type": "float",
   "range": [
    0,
    1
   ]
  }
 ]
}
```


## constants/WATER_NORMAL_SCALE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting specifying the scaling vector applied to the water normal map.",
 "type": "integer",
 "value": 104,
 "value-type": "vector",
 "range": [
  "<0,0,0>",
  "<10,10,10>"
 ]
}
```


## constants/WATER_NORMAL_TEXTURE

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental setting containing the inventory name or UUID of the normal map texture used for water waves.",
 "type": "integer",
 "value": 107,
 "value-type": "asset",
 "access": "write"
}
```


## constants/WATER_REFRACTION

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental water surface refraction scale factors: scale_above and scale_below.",
 "type": "integer",
 "value": 105,
 "values": [
  {
   "name": "scale_above",
   "value-type": "float",
   "range": [
    0,
    3
   ]
  },
  {
   "name": "scale_below",
   "value-type": "float",
   "range": [
    0,
    3
   ]
  }
 ]
}
```


## constants/WATER_TEXTURE_DEFAULTS

```json
{
 "member-of": [
  "EnvironmentParamReadOnly"
 ],
 "tooltip": "Environmental check returning 1 if default water wave maps are used, or 0 if a custom texture is set.",
 "type": "integer",
 "value": 103,
 "values": [
  {
   "name": "normal_is_default",
   "value-type": "boolean"
  },
  {
   "name": "transparent_is_default",
   "value-type": "boolean"
  }
 ],
 "access": "read"
}
```


## constants/WATER_WAVE_DIRECTION

```json
{
 "member-of": [
  "EnvironmentParamReadOnly",
  "EnvironmentParam"
 ],
 "tooltip": "Environmental wave direction vectors (X is east/west, Y is north/south) specifying speeds and directions for both large and small waves.",
 "type": "integer",
 "value": 106,
 "values": [
  {
   "name": "large_wave",
   "value-type": "vector",
   "range": [
    "<-20,-20,0>",
    "<20,20,0>"
   ],
   "details": "Large wave speed and direction."
  },
  {
   "name": "small_wave",
   "value-type": "vector",
   "range": [
    "<-20,-20,0>",
    "<20,20,0>"
   ],
   "details": "Small wave speed and direction."
  }
 ]
}
```


## constants/XP_ERROR_EXPERIENCES_DISABLED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Region currently has experiences disabled.",
 "type": "integer",
 "value": 2
}
```


## constants/XP_ERROR_EXPERIENCE_DISABLED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Experience owner has temporarily disabled the experience.",
 "type": "integer",
 "value": 8
}
```


## constants/XP_ERROR_EXPERIENCE_SUSPENDED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Experience has been suspended by Linden Lab customer support.",
 "type": "integer",
 "value": 9
}
```


## constants/XP_ERROR_INVALID_EXPERIENCE

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Script is associated with an experience that no longer exists.",
 "type": "integer",
 "value": 7
}
```


## constants/XP_ERROR_INVALID_PARAMETERS

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "One of the string arguments was too big to fit in the key-value store.",
 "type": "integer",
 "value": 3
}
```


## constants/XP_ERROR_KEY_NOT_FOUND

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Requested key does not exist.",
 "type": "integer",
 "value": 14
}
```


## constants/XP_ERROR_MATURITY_EXCEEDED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Content rating of the experience exceeds that of the region.",
 "type": "integer",
 "value": 16
}
```


## constants/XP_ERROR_NONE

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "No error was detected.",
 "type": "integer",
 "value": 0
}
```


## constants/XP_ERROR_NOT_FOUND

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Sim was unable to verify the validity of the experience. Retrying after a short wait is advised.",
 "type": "integer",
 "value": 6
}
```


## constants/XP_ERROR_NOT_PERMITTED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "This experience is not allowed to run by the requested agent, or experience permissions were denied by the user.",
 "type": "integer",
 "value": 4
}
```


## constants/XP_ERROR_NOT_PERMITTED_LAND

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Experience is blocked or not enabled for this land, or is not allowed to run in the current region.",
 "type": "integer",
 "value": 17
}
```


## constants/XP_ERROR_NO_EXPERIENCE

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "This script is not associated with an experience.",
 "type": "integer",
 "value": 5
}
```


## constants/XP_ERROR_QUOTA_EXCEEDED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "An attempt to write data to the key-value store failed due to the data quota being met.",
 "type": "integer",
 "value": 11
}
```


## constants/XP_ERROR_REQUEST_PERM_TIMEOUT

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Request for experience permissions was ignored and the request timed out without modification.",
 "type": "integer",
 "value": 18
}
```


## constants/XP_ERROR_RETRY_UPDATE

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "A checked update failed due to an out of date request.",
 "type": "integer",
 "value": 15
}
```


## constants/XP_ERROR_STORAGE_EXCEPTION

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Unable to communicate with the key-value store, or attempted to create a key that already exists.",
 "type": "integer",
 "value": 13
}
```


## constants/XP_ERROR_STORE_DISABLED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Key-value store is currently disabled on this region.",
 "type": "integer",
 "value": 12
}
```


## constants/XP_ERROR_THROTTLED

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "Call failed due to too many recent calls.",
 "type": "integer",
 "value": 1
}
```


## constants/XP_ERROR_UNKNOWN_ERROR

```json
{
 "member-of": [
  "ExperienceError"
 ],
 "tooltip": "An unknown error occurred that is not covered by any of the other predetermined error states.",
 "type": "integer",
 "value": 10
}
```


## constants/ZERO_ROTATION

```json
{
 "tooltip": "A rotation constant representing an identity rotation (causes no change). This is the default value for rotation variables.",
 "type": "rotation",
 "value": "<0.0, 0.0, 0.0, 1.0>"
}
```


## constants/ZERO_VECTOR

```json
{
 "tooltip": "A vector constant representing <0.0, 0.0, 0.0>. This is the default value for vector variables.",
 "type": "vector",
 "value": "<0.0, 0.0, 0.0>"
}
```


# Section: events (43 entries)


## events/at_rot_target

```json
{
 "event-id": 22,
 "arguments": [
  {
   "handle": {
    "tooltip": "Integer handle returned by the llRotTarget call.",
    "type": "integer"
   }
  },
  {
   "targetrot": {
    "tooltip": "Target rotation specified in the llRotTarget call.",
    "type": "rotation"
   }
  },
  {
   "ourrot": {
    "tooltip": "Current rotation of the object (similar to llGetRot).",
    "type": "rotation"
   }
  }
 ],
 "tooltip": "Triggered when the script's rotation (ourrot) comes within a defined angle (error) of the target rotation (targetrot) set by a call to llRotTarget (which returns the associated handle).",
 "categories": [
  "movement"
 ]
}
```


## events/at_target

```json
{
 "event-id": 20,
 "arguments": [
  {
   "tnum": {
    "tooltip": "Integer target handle returned by the llTarget call.",
    "type": "integer"
   }
  },
  {
   "targetpos": {
    "tooltip": "Target position vector specified in the llTarget call.",
    "type": "vector"
   }
  },
  {
   "ourpos": {
    "tooltip": "Current position vector of the object (similar to llGetPos).",
    "type": "vector"
   }
  }
 ],
 "tooltip": "Triggered when the scripted object's position (ourpos) comes within the defined range of the target position (targetpos) set by llTarget (which returns the associated handle tnum).",
 "categories": [
  "movement"
 ]
}
```


## events/attach

```json
{
 "event-id": 26,
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar the object is attached to, or NULL_KEY if detached.",
    "type": "key"
   }
  }
 ],
 "tooltip": "Triggered whenever the object is attached to or detached from an avatar. Passes the UUID key of the avatar if attached, or NULL_KEY if detached.",
 "categories": [
  "attachments"
 ]
}
```


## events/changed

```json
{
 "event-id": 25,
 "arguments": [
  {
   "changes": {
    "tooltip": "A bitfield of CHANGED_* flags representing what changed.",
    "type": "integer",
    "enum-semantics": "ChangeType"
   }
  }
 ],
 "tooltip": "Triggered when various properties of the object change. The parameter changes is a bitfield of CHANGED_* flags.",
 "categories": [
  "asset_permissions",
  "linkset",
  "media",
  "prim_appearance",
  "prim_inventory",
  "prim_media",
  "region",
  "teleport",
  "script",
  "sit"
 ]
}
```


## events/collision

```json
{
 "event-id": 7,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Total number of detected colliders (usable with llDetected* functions).",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered continuously while an avatar or another object is colliding with the object containing the script. Passes num_detected, representing the number of detected collisions.",
 "categories": [
  "detected",
  "physics",
  "sensor"
 ]
}
```


## events/collision_end

```json
{
 "event-id": 8,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Total number of detected colliders (usable with llDetected* functions).",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered when an avatar or another object stops colliding with the object containing the script. Passes num_detected, representing the number of detected collisions.",
 "categories": [
  "detected",
  "physics",
  "sensor"
 ]
}
```


## events/collision_start

```json
{
 "event-id": 6,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Total number of detected colliders (usable with llDetected* functions).",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered when an avatar or another object first begins colliding with the object containing the script. Passes num_detected, representing the number of detected collisions.",
 "categories": [
  "detected",
  "physics",
  "sensor"
 ]
}
```


## events/control

```json
{
 "event-id": 17,
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar whose inputs are captured.",
    "type": "key"
   }
  },
  {
   "level": {
    "tooltip": "A bitfield of CONTROL_* constants representing currently held controls.",
    "type": "integer",
    "enum-semantics": "ControlButton"
   }
  },
  {
   "edge": {
    "tooltip": "A bitfield of CONTROL_* constants representing controls that just changed state.",
    "type": "integer",
    "enum-semantics": "ControlButton"
   }
  }
 ],
 "tooltip": "Triggered to pass captured avatar control inputs into the script. The parameter level indicates held controls, and edge indicates change in controls (both are bitfields of CONTROL_* constants).",
 "categories": [
  "avatar",
  "input"
 ]
}
```


## events/dataserver

```json
{
 "event-id": 27,
 "arguments": [
  {
   "queryid": {
    "tooltip": "Key identifying the asynchronous request (matches the handle returned by the requesting function).",
    "type": "key"
   }
  },
  {
   "data": {
    "tooltip": "String containing the requested data.",
    "type": "string"
   }
  }
 ],
 "tooltip": "Triggered when requested data is returned to the script (e.g., from llRequestAgentData, llRequestInventoryData, or llGetNotecardLine).",
 "categories": [
  "dataserver"
 ]
}
```


## events/email

```json
{
 "event-id": 19,
 "arguments": [
  {
   "time": {
    "tooltip": "Timestamp of when the email was received, in (string)llGetUnixTime() format.",
    "type": "string"
   }
  },
  {
   "address": {
    "tooltip": "Email address of the sender.",
    "type": "string"
   }
  },
  {
   "subject": {
    "tooltip": "Subject of the email.",
    "type": "string"
   }
  },
  {
   "msg": {
    "tooltip": "Body text of the email.",
    "type": "string"
   }
  },
  {
   "num_left": {
    "tooltip": "Number of emails still waiting in the queue.",
    "type": "integer"
   }
  }
 ],
 "tooltip": "Receive an email requested by llGetNextEmail(). NumberRemaining indicates the number of emails remaining in the queue for llGetNextEmail() to retrieve.",
 "categories": [
  "script_communication"
 ]
}
```


## events/experience_permissions

```json
{
 "event-id": 35,
 "arguments": [
  {
   "agent_id": {
    "tooltip": "UUID of the avatar approving experience permissions.",
    "type": "key"
   }
  }
 ],
 "tooltip": "Triggered when the agent specified by agent_id approves an experience permissions request (interactively or automatically if previously approved).",
 "categories": [
  "avatar",
  "experience",
  "permissions"
 ]
}
```


## events/experience_permissions_denied

```json
{
 "event-id": 38,
 "arguments": [
  {
   "agent_id": {
    "tooltip": "UUID of the avatar who denied or was blocked from granting permissions.",
    "type": "key"
   }
  },
  {
   "reason": {
    "tooltip": "XP_ERROR_* error constant describing why permissions were denied.",
    "type": "integer",
    "enum-semantics": "ExperienceError"
   }
  }
 ],
 "tooltip": "Triggered when the agent specified by agent_id denies experience permissions, or when permission is blocked for other reasons (specified by the error code reason).",
 "categories": [
  "avatar",
  "experience",
  "permissions"
 ]
}
```


## events/final_damage

```json
{
 "event-id": 43,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Number of damage events applied to the avatar or task.",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered after all on_damage events across all scripts have completed and damage is actively applied to the avatar or distributed among seated avatars. Collision detected functions (llDetected*) and llDetectedDamage are available.",
 "categories": [
  "combat",
  "detected"
 ]
}
```


## events/game_control

```json
{
 "event-id": 40,
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar supplying controller input.",
    "type": "key"
   }
  },
  {
   "button_levels": {
    "tooltip": "A 32-bit mask representing the canonical buttons currently held down on the controller.",
    "type": "integer",
    "enum-semantics": "GameControlButton"
   }
  },
  {
   "axes": {
    "tooltip": "A list of six float values in the range [-1.0, 1.0] representing canonical controller axes.",
    "type": "list",
    "slua-type": "{number}"
   }
  }
 ],
 "tooltip": "Triggered when a compatible viewer sends game controller input changes for the avatar specified by id. Only triggers for scripts in attachments or seats.",
 "categories": [
  "avatar",
  "game_control",
  "input"
 ],
 "uses-enum": "GameControlAxis"
}
```


## events/http_request

```json
{
 "event-id": 34,
 "arguments": [
  {
   "request_id": {
    "tooltip": "Unique key identifying the incoming HTTP request (used with llHTTPResponse).",
    "type": "key"
   }
  },
  {
   "method": {
    "tooltip": "HTTP method string ('GET', 'POST', 'PUT', 'DELETE') or URL request status constants.",
    "type": "string"
   }
  },
  {
   "body": {
    "tooltip": "String payload of the incoming request body.",
    "type": "string"
   }
  }
 ],
 "tooltip": "Triggered when the script's registered URL receives an incoming HTTP request identified by request_id.",
 "categories": [
  "script_communication",
  "web"
 ]
}
```


## events/http_response

```json
{
 "event-id": 33,
 "arguments": [
  {
   "request_id": {
    "tooltip": "Key matching the handle returned by the initiating llHTTPRequest call.",
    "type": "key"
   }
  },
  {
   "status": {
    "tooltip": "Integer HTTP status code returned (such as 200 or 404).",
    "type": "integer"
   }
  },
  {
   "metadata": {
    "tooltip": "A list of HTTP_* constants and response headers metadata.",
    "type": "list",
    "param-semantics": "HTTPResponseError"
   }
  },
  {
   "body": {
    "tooltip": "String payload of the received response body.",
    "type": "string"
   }
  }
 ],
 "tooltip": "Triggered when an HTTP response body is received for a pending request_id, or if the request fails or times out.",
 "categories": [
  "script_communication",
  "web"
 ]
}
```


## events/land_collision

```json
{
 "event-id": 10,
 "arguments": [
  {
   "pos": {
    "tooltip": "Vector position of collision with the ground.",
    "type": "vector"
   }
  }
 ],
 "tooltip": "Triggered in the root prim when a physical object or attached avatar is colliding with the ground at position pos.",
 "categories": [
  "physics"
 ]
}
```


## events/land_collision_end

```json
{
 "event-id": 11,
 "arguments": [
  {
   "pos": {
    "tooltip": "Vector position of the last ground collision.",
    "type": "vector"
   }
  }
 ],
 "tooltip": "Triggered in the root prim when a physical object or attached avatar stops colliding with the ground at position pos.",
 "categories": [
  "physics"
 ]
}
```


## events/land_collision_start

```json
{
 "event-id": 9,
 "arguments": [
  {
   "pos": {
    "tooltip": "Vector position of collision with the ground.",
    "type": "vector"
   }
  }
 ],
 "tooltip": "Triggered in the root prim when a physical object or attached avatar first begins colliding with the ground at position pos.",
 "categories": [
  "physics"
 ]
}
```


## events/link_message

```json
{
 "event-id": 28,
 "arguments": [
  {
   "sender_num": {
    "tooltip": "Link index of the prim containing the script that sent the message.",
    "type": "integer"
   }
  },
  {
   "num": {
    "tooltip": "An integer value passed from the sending script.",
    "type": "integer"
   }
  },
  {
   "str": {
    "tooltip": "A text string value passed from the sending script.",
    "type": "string"
   }
  },
  {
   "id": {
    "tooltip": "A key value passed from the sending script.",
    "type": "key",
    "slua-type": "string"
   }
  }
 ],
 "tooltip": "Triggered when the script receives a link message from sender_num, containing the parameters num, str, and id sent via llMessageLinked.",
 "categories": [
  "script_communication"
 ]
}
```


## events/linkset_data

```json
{
 "event-id": 39,
 "arguments": [
  {
   "action": {
    "tooltip": "Action taken (LINKSETDATA_UPDATE, LINKSETDATA_DELETE, LINKSETDATA_MULTIDELETE, or LINKSETDATA_RESET).",
    "type": "integer",
    "enum-semantics": "LinksetDataAction"
   }
  },
  {
   "name": {
    "tooltip": "Name of the modified key (a comma-separated list of keys for LINKSETDATA_MULTIDELETE, or empty for LINKSETDATA_RESET).",
    "type": "string"
   }
  },
  {
   "value": {
    "tooltip": "New value of the key (empty if the key was deleted or is protected).",
    "type": "string"
   }
  }
 ],
 "tooltip": "Fires in all scripts in the linkset whenever the linkset datastore is modified via an llLinksetData function. Passes the action taken, the affected key name, and the new value.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## events/listen

```json
{
 "event-id": 13,
 "arguments": [
  {
   "channel": {
    "tooltip": "Chat channel where the message appeared.",
    "type": "integer",
    "enum-semantics": "Channel"
   }
  },
  {
   "name": {
    "tooltip": "Name of the sending prim or the legacy name of the sending agent.",
    "type": "string"
   }
  },
  {
   "id": {
    "tooltip": "UUID of the sending agent or prim.",
    "type": "key"
   }
  },
  {
   "msg": {
    "tooltip": "Spoken text string.",
    "type": "string"
   }
  }
 ],
 "tooltip": "Triggered when a chat message matching active llListen filters is received on channel. Passes the sender's name and UUID key id, along with the spoken string msg.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## events/money

```json
{
 "event-id": 18,
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the paying resident.",
    "type": "key"
   }
  },
  {
   "amount": {
    "tooltip": "Quantity of L$ paid to the prim.",
    "type": "integer"
   }
  }
 ],
 "tooltip": "Triggered when a resident specified by id pays an amount of Linden dollars (L$) to the prim.",
 "categories": [
  "money"
 ]
}
```


## events/moving_end

```json
{
 "event-id": 30,
 "arguments": [],
 "tooltip": "Triggered whenever the physical or moving object containing the script stops moving.",
 "categories": [
  "movement",
  "pathfinding"
 ]
}
```


## events/moving_start

```json
{
 "event-id": 29,
 "arguments": [],
 "tooltip": "Triggered whenever the physical or moving object containing the script starts moving.",
 "categories": [
  "movement",
  "pathfinding"
 ]
}
```


## events/no_sensor

```json
{
 "event-id": 16,
 "arguments": [],
 "tooltip": "Triggered when active sensors (from llSensor or llSensorRepeat) complete a scan without finding any matching targets.",
 "categories": [
  "detected",
  "sensor"
 ]
}
```


## events/not_at_rot_target

```json
{
 "event-id": 23,
 "arguments": [],
 "tooltip": "Triggered continuously while the object's rotation is outside the leeway angle of targets set via llRotTarget.",
 "categories": [
  "movement"
 ]
}
```


## events/not_at_target

```json
{
 "event-id": 21,
 "arguments": [],
 "tooltip": "Triggered continuously while the object's position has not yet reached the range of targets set via llTarget.",
 "categories": [
  "movement"
 ]
}
```


## events/object_rez

```json
{
 "event-id": 31,
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the newly rezzed object.",
    "type": "key"
   }
  }
 ],
 "tooltip": "Triggered when this object successfully rezzes another object from its inventory. Passes the key (UUID) id of the newly rezzed object.",
 "categories": [
  "rez"
 ]
}
```


## events/on_damage

```json
{
 "event-id": 42,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Number of pending damage events.",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered when damage has been inflicted on an avatar or task, but before it is applied or distributed. Collision detected functions (llDetected*), llDetectedDamage, and llAdjustDamage are available. Passes num_detected, representing the number of pending damage events.",
 "categories": [
  "combat",
  "detected"
 ]
}
```


## events/on_death

```json
{
 "event-id": 41,
 "arguments": [],
 "tooltip": "Triggered on all worn attachments when the wearing avatar's health reaches 0.",
 "categories": [
  "combat"
 ]
}
```


## events/on_rez

```json
{
 "event-id": 14,
 "arguments": [
  {
   "start_param": {
    "tooltip": "Integer start parameter passed from the rezzing call.",
    "type": "integer"
   }
  }
 ],
 "tooltip": "Triggered when the object is rezzed into the world (by a script or user). Passes start_param from the rezzing call (or 0 if rezzed from inventory). Also triggers on attachments during login or when attached from inventory.",
 "categories": [
  "rez",
  "script"
 ]
}
```


## events/path_update

```json
{
 "event-id": 37,
 "arguments": [
  {
   "type": {
    "tooltip": "Path update status or failure code constant (PU_* flag).",
    "type": "integer",
    "enum-semantics": "CharacterPathUpdateType"
   }
  },
  {
   "reserved": {
    "tooltip": "Reserved parameter (currently unused).",
    "type": "list"
   }
  }
 ],
 "tooltip": "Triggered to inform the script of changes or failures in the pathfinding character's status.",
 "categories": [
  "pathfinding"
 ]
}
```


## events/remote_data

```json
{
 "event-id": 32,
 "arguments": [
  {
   "event_type": {
    "tooltip": "Integer constant representing the type of XML-RPC event.",
    "type": "integer",
    "enum-semantics": "RemoteDataEventType"
   }
  },
  {
   "channel": {
    "tooltip": "XML-RPC channel ID key.",
    "type": "key"
   }
  },
  {
   "message_id": {
    "tooltip": "XML-RPC message ID key.",
    "type": "key"
   }
  },
  {
   "sender": {
    "tooltip": "XML-RPC sender string.",
    "type": "string"
   }
  },
  {
   "idata": {
    "tooltip": "Payload integer data.",
    "type": "integer"
   }
  },
  {
   "sdata": {
    "tooltip": "Payload string data.",
    "type": "string"
   }
  }
 ],
 "deprecated": true,
 "tooltip": "Deprecated. Triggered by incoming XML-RPC calls, passing event_type, channel, message_id, sender, idata, and sdata.",
 "categories": [
  "script_communication"
 ]
}
```


## events/run_time_permissions

```json
{
 "event-id": 24,
 "arguments": [
  {
   "perm": {
    "tooltip": "Bitfield of currently granted permissions (PERMISSION_* flags).",
    "type": "integer",
    "enum-semantics": "ScriptPermission"
   }
  }
 ],
 "tooltip": "Triggered when an agent grants or denies runtime permissions requested by llRequestPermissions. Passes the active integer permissions bitfield perm (returns 0 if no permissions are currently granted).",
 "categories": [
  "permissions"
 ]
}
```


## events/sensor

```json
{
 "event-id": 15,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Total number of detected targets found (usable with llDetected* functions).",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered when objects matching constraints of llSensor or llSensorRepeat are successfully detected. Passes num_detected, representing the number of detected targets.",
 "categories": [
  "detected",
  "sensor"
 ]
}
```


## events/state_entry

```json
{
 "event-id": 1,
 "arguments": [],
 "tooltip": "Triggered immediately whenever a new state is entered (including at script start). It is always the first event handled.",
 "slua-removed": true,
 "categories": [
  "script"
 ]
}
```


## events/state_exit

```json
{
 "event-id": 2,
 "arguments": [],
 "slua-removed": true,
 "tooltip": "Triggered when the state command is used to transition out of the current state. Handled before entering the new state's state_entry.",
 "categories": [
  "script"
 ]
}
```


## events/timer

```json
{
 "event-id": 12,
 "arguments": [],
 "slua-deprecated": {
  "use": "LLTimers"
 },
 "tooltip": "Triggered at regular periodic intervals configured by llSetTimerEvent.",
 "categories": [
  "script",
  "time"
 ]
}
```


## events/touch

```json
{
 "event-id": 4,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Total number of touching agents detected (usable with llDetected* functions).",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered continuously while an avatar touches the object. Passes num_detected, representing the number of touching agents.",
 "categories": [
  "detected",
  "touch",
  "user_interface"
 ]
}
```


## events/touch_end

```json
{
 "event-id": 5,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Total number of touching agents detected (usable with llDetected* functions).",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered when an avatar stops touching the object. Passes num_detected, representing the number of touching agents.",
 "categories": [
  "detected",
  "touch",
  "user_interface"
 ]
}
```


## events/touch_start

```json
{
 "event-id": 3,
 "arguments": [
  {
   "num_detected": {
    "tooltip": "Total number of touching agents detected (usable with llDetected* functions).",
    "type": "integer"
   }
  }
 ],
 "detected-semantics": true,
 "tooltip": "Triggered when an avatar first touches the object. Passes num_detected, representing the number of touching agents.",
 "categories": [
  "detected",
  "touch",
  "user_interface"
 ]
}
```


## events/transaction_result

```json
{
 "event-id": 36,
 "arguments": [
  {
   "id": {
    "tooltip": "Key matching the handle returned by the initiating llTransfer* function.",
    "type": "key"
   }
  },
  {
   "success": {
    "tooltip": "Boolean. TRUE if the L$ transfer succeeded, FALSE otherwise.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "data": {
    "tooltip": "Contains a CSV string of transaction info on success, or an error string on failure.",
    "type": "string"
   }
  }
 ],
 "tooltip": "Triggered when an asynchronous L$ transfer (such as llTransferLindenDollars) is completed. Passes transaction info id, success status, and CSV or error data.",
 "categories": [
  "money"
 ]
}
```


# Section: functions (529 entries)


## functions/llAbs

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Integer to convert.",
    "type": "integer"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.abs",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.abs(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 6,
 "native": true,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the absolute (positive) integer value of val.",
 "categories": [
  "math"
 ]
}
```


## functions/llAcos

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "A number in the range [-1.0, 1.0].",
    "type": "float",
    "range": [
     -1,
     1
    ]
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.acos",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.acos(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 172,
 "native": true,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the arccosine of val in radians.",
 "categories": [
  "math",
  "math_trig"
 ]
}
```


## functions/llAddToLandBanList

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar to add to the ban list.",
    "type": "key"
   }
  },
  {
   "hours": {
    "tooltip": "Duration, in hours, to ban the avatar for (0 for indefinite).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 310,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Adds the avatar to the parcel ban list for the specified number of hours. A value of 0 hours adds the avatar indefinitely. Banned users teleporting to the parcel are redirected to a neighboring parcel; the minimum accepted duration is 0.01 hours (approximately 36 seconds).",
 "categories": [
  "land_moderation",
  "parcel"
 ]
}
```


## functions/llAddToLandPassList

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar to add to the pass list.",
    "type": "key"
   }
  },
  {
   "hours": {
    "tooltip": "Duration, in hours, to allow the avatar for (range [0.0, 144.0], 0 for indefinite).",
    "type": "float",
    "range": [
     0,
     144
    ]
   }
  }
 ],
 "energy": 10.0,
 "func-id": 240,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Adds the avatar to the land pass list for the specified number of hours (or indefinitely if hours is 0).",
 "categories": [
  "land_moderation",
  "parcel"
 ]
}
```


## functions/llAdjustDamage

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the damage event to modify.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "new_damage": {
    "tooltip": "New damage value to be applied or distributed after on_damage processing.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 555,
 "return": "void",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Modifies the amount of damage applied by the current on_damage event after it completes processing, specified by the damage event index number.",
 "categories": [
  "combat",
  "detected"
 ]
}
```


## functions/llAdjustSoundVolume

```json
{
 "arguments": [
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 207,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Adjusts the volume of the currently playing attached sound (has no effect on sounds started with llTriggerSound).",
 "categories": [
  "sound"
 ]
}
```


## functions/llAgentInExperience

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the avatar in the same region to query.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 392,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns TRUE if the specified agent is in the experience and the experience can run in the current region/location; returns FALSE otherwise.",
 "categories": [
  "avatar",
  "experience"
 ]
}
```


## functions/llAllowInventoryDrop

```json
{
 "arguments": [
  {
   "add": {
    "tooltip": "Boolean. If TRUE, allows anyone to drop inventory items into the prim (even without modify rights). If FALSE, restricts inventory dropping to those with modify permissions.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 176,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "If add is TRUE, allows users without object modify permissions to drop inventory items into the prim. If FALSE, restricts inventory dropping to users with modify permissions.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llAngleBetween

```json
{
 "arguments": [
  {
   "start_rot": {
    "tooltip": "Starting rotation.",
    "type": "rotation"
   }
  },
  {
   "end_rot": {
    "tooltip": "Ending rotation.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 174,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the angle, in radians, between rotations start_rot and and end_rot.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion"
 ]
}
```


## functions/llApplyImpulse

```json
{
 "arguments": [
  {
   "momentum": {
    "tooltip": "Linear impulse vector to apply.",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, momentum is treated as a local directional vector; if FALSE, it is treated as a global region vector.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 72,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Applies a linear impulse (momentum) to a physical object. If local is TRUE, the impulse is applied in local coordinates; otherwise, it is applied in global region coordinates.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llApplyRotationalImpulse

```json
{
 "arguments": [
  {
   "force": {
    "tooltip": "Rotational impulse vector to apply.",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, the force is treated as a local directional vector; if FALSE, it is treated as a global region vector.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 73,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Applies a rotational impulse (force) to a physical object. If local is TRUE, the rotational impulse is applied in local coordinates; otherwise, it is applied in global region coordinates.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llAsin

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "A number in the range [-1.0, 1.0].",
    "type": "float",
    "range": [
     -1,
     1
    ]
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.asin",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.asin(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 173,
 "native": true,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the arcsine of val in radians.",
 "categories": [
  "math",
  "math_trig"
 ]
}
```


## functions/llAtan2

```json
{
 "arguments": [
  {
   "y": {
    "tooltip": "Y coordinate.",
    "type": "float"
   }
  },
  {
   "x": {
    "tooltip": "X coordinate.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.atan2",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.atan2(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 3,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the arctangent of y/x in radians, using the signs to determine the quadrant. Note the argument order: Y is the first parameter, X is the second parameter.",
 "categories": [
  "math",
  "math_trig"
 ]
}
```


## functions/llAttachToAvatar

```json
{
 "arguments": [
  {
   "attach_point": {
    "tooltip": "ATTACH_* constant or integer value representing the target attachment point.",
    "type": "integer",
    "enum-semantics": "AttachPoint"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 113,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_ATTACH"
 ],
 "tooltip": "Attaches the object to the avatar who has granted the PERMISSION_ATTACH permission. Takes the object into the user's inventory and attaches it at attach_point.",
 "categories": [
  "attachments",
  "avatar"
 ]
}
```


## functions/llAttachToAvatarTemp

```json
{
 "arguments": [
  {
   "attach_point": {
    "tooltip": "ATTACH_* constant or integer value representing the target attachment point.",
    "type": "integer",
    "enum-semantics": "AttachPoint"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 391,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_ATTACH"
 ],
 "tooltip": "Attaches the object temporarily to an avatar who has granted the PERMISSION_ATTACH permission. No permanent inventory is created, and the object disappears on detach or disconnect. Can be used on non-owners (changing ownership to the wearer).",
 "categories": [
  "attachments",
  "avatar"
 ]
}
```


## functions/llAvatarOnLinkSitTarget

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Index of the prim in the linkset (1 for root, >1 for children), or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 376,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the UUID of the avatar seated on the specified link's sit target, or NULL_KEY if no avatar is sitting there.",
 "categories": [
  "avatar",
  "linkset",
  "sit"
 ]
}
```


## functions/llAvatarOnSitTarget

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 239,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the UUID of the avatar seated on the prim's sit target (defined via llSitTarget), or NULL_KEY if no avatar is sitting there or the prim lacks a sit target.",
 "categories": [
  "avatar",
  "prim",
  "sit"
 ]
}
```


## functions/llAxes2Rot

```json
{
 "arguments": [
  {
   "fwd": {
    "tooltip": "Forward/back directional vector of the rotation.",
    "type": "vector"
   }
  },
  {
   "left": {
    "tooltip": "Left/right directional vector of the rotation.",
    "type": "vector"
   }
  },
  {
   "up": {
    "tooltip": "Up/down directional vector of the rotation.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 17,
 "pure": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns the rotation defined by the coordinate axes fwd, left, and up.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion"
 ]
}
```


## functions/llAxisAngle2Rot

```json
{
 "arguments": [
  {
   "axis": {
    "tooltip": "Axis vector to rotate around.",
    "type": "vector"
   }
  },
  {
   "angle": {
    "tooltip": "Angle to rotate, in radians.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 169,
 "pure": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns the rotation that rotates angle radians around the axis vector.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion"
 ]
}
```


## functions/llBase64ToInteger

```json
{
 "arguments": [
  {
   "str": {
    "tooltip": "Base64-encoded string to decode.",
    "type": "string"
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use 'llbase64.decode' and 'string.unpack' or 'buffer.readi32' instead.",
  "selene-replace": [
   "string.unpack(\">i\", llbase64.decode(s))"
  ]
 },
 "energy": 10.0,
 "func-id": 281,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the Base64-decoded big-endian value of str. Returns zero if str is longer than 8 characters; the return value is unpredictable if str contains fewer than 6 characters.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llBase64ToString

```json
{
 "arguments": [
  {
   "str": {
    "tooltip": "Base64-encoded string to decode.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 261,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Decodes the Base64-encoded string str into a conventional string, interpreting the bytes as a UTF-8 character sequence. Unprintable characters are converted to question marks.",
 "categories": [
  "data_conversion"
 ],
 "slua-deprecated": {
  "use": "llbase64.decode",
  "selene-replace": [
   "llbase64.decode(%1)"
  ]
 }
}
```


## functions/llBreakAllLinks

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 143,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_CHANGE_LINKS"
 ],
 "tooltip": "Delinks all prims in the linkset. Requires the PERMISSION_CHANGE_LINKS runtime permission, which must be requested and granted by the owner.",
 "categories": [
  "linkset"
 ]
}
```


## functions/llBreakLink

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "The link number (0: unlinked, 1: root prim, >1: child prims and seated avatars) to delink.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 142,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_CHANGE_LINKS"
 ],
 "tooltip": "Delinks the prim specified by the link number link. Requires the PERMISSION_CHANGE_LINKS runtime permission.",
 "categories": [
  "linkset"
 ]
}
```


## functions/llCSV2List

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "String of comma-separated values to parse.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 196,
 "pure": true,
 "return": "list",
 "slua-return": "{string}",
 "sleep": 0.0,
 "tooltip": "Parses the comma-separated string src and returns it as a list.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llCastRay

```json
{
 "arguments": [
  {
   "start_pos": {
    "tooltip": "Starting location vector of the ray.",
    "type": "vector"
   }
  },
  {
   "end_pos": {
    "tooltip": "Ending location vector of the ray.",
    "type": "vector"
   }
  },
  {
   "options": {
    "tooltip": "A list of option flags and their parameters to configure the raycast.",
    "type": "list",
    "param-semantics": "RayCastParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 363,
 "must-use": true,
 "return": "list",
 "sleep": 0.0,
 "tooltip": "Casts a ray into the physics world from start to end and reports collision data for intersections with objects based on options. Returns a list of strided values [UUID_1, {link_number_1}, hit_position_1, {hit_normal_1}, ..., status_code]. A negative status_code indicates an error; otherwise, it represents the number of hits.",
 "categories": [
  "physics",
  "sensor"
 ],
 "uses-enum": "RayCastError"
}
```


## functions/llCeil

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Number to round up.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.ceil",
  "reason": "Fastcall.",
  "selene-replace": [
   "math.ceil(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 10,
 "native": true,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns val rounded toward positive infinity. In other words, returns the smallest integer greater than or equal to val.",
 "categories": [
  "math"
 ]
}
```


## functions/llChar

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Unicode codepoint integer (ordinal) to convert.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 526,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Constructs and returns a single-character string from the given Unicode codepoint ordinal.",
 "categories": [
  "string"
 ]
}
```


## functions/llClearCameraParams

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 314,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_CONTROL_CAMERA"
 ],
 "tooltip": "Resets all camera parameters to default values and turns off scripted camera control. Requires the PERMISSION_CONTROL_CAMERA runtime permission (automatically granted for attached or sat-on objects).",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llClearExperience

```json
{
 "arguments": [
  {
   "agentid": {
    "tooltip": "",
    "type": "key"
   }
  },
  {
   "experienceid": {
    "tooltip": "",
    "type": "key"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 411,
 "private": true,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "",
 "categories": [
  "experience"
 ]
}
```


## functions/llClearExperiencePermissions

```json
{
 "arguments": [
  {
   "agentid": {
    "tooltip": "",
    "type": "key"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 385,
 "private": true,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "",
 "categories": [
  "experience"
 ]
}
```


## functions/llClearLinkMedia

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "The link number (0: unlinked, 1: root prim, >1: child prims) or a LINK_* flag representing the target prim.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "face": {
    "tooltip": "Face number to clear.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 373,
 "return": "integer",
 "enum-semantics": "PrimMediaError",
 "sleep": 0.0,
 "tooltip": "Deletes the media and clears all parameters from the given face on the linked prim. Returns an integer STATUS_* flag detailing the success or failure of the operation.",
 "categories": [
  "linkset",
  "media",
  "prim_media"
 ]
}
```


## functions/llClearPrimMedia

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number (side) to clear.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 352,
 "return": "integer",
 "enum-semantics": "PrimMediaError",
 "sleep": 1.0,
 "tooltip": "Deletes the media and clears all parameters from the specified face. Returns an integer STATUS_* flag detailing the success or failure of the operation.",
 "categories": [
  "media",
  "prim",
  "prim_media"
 ]
}
```


## functions/llCloseRemoteDataChannel

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "XML-RPC channel ID to close.",
    "type": "key"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 257,
 "return": "void",
 "sleep": 1.0,
 "tooltip": "Deprecated. Closes the specified XML-RPC channel.",
 "categories": [
  "script_communication"
 ]
}
```


## functions/llCloud

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position, expressed in local coordinates.",
    "type": "vector"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 43,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the cloud density at the prim's position offset by the vector offset.",
 "categories": [
  "region"
 ]
}
```


## functions/llCollisionFilter

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Specific object name or avatar legacy name to filter for.",
    "type": "string"
   }
  },
  {
   "id": {
    "tooltip": "Group, avatar, or object UUID to filter by.",
    "type": "key"
   }
  },
  {
   "accept": {
    "tooltip": "Boolean. If TRUE, only collisions matching the name and id filters are processed; if FALSE, matching collisions are excluded.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 110,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the collision filter, either exclusively or inclusively. If accept is TRUE, only collisions matching name and id are processed; if FALSE, matches are excluded. Pass an empty string or NULL_KEY to name or id to skip filtering on that parameter.",
 "categories": [
  "physics",
  "sensor"
 ]
}
```


## functions/llCollisionSound

```json
{
 "arguments": [
  {
   "impact_sound": {
    "tooltip": "UUID of a sound, the name of a sound in the prim's inventory, or an empty string to suppress sounds.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "impact_volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 160,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Suppresses default collision sounds and replaces default impact sounds with impact_sound at the volume level specified by impact_volume. Supply an empty string to only suppress collision sounds.",
 "categories": [
  "physics",
  "sound"
 ]
}
```


## functions/llCollisionSprite

```json
{
 "arguments": [
  {
   "impact_sprite": {
    "tooltip": "UUID of a texture, the name of a texture in the prim's inventory, or an empty string to suppress sprites.",
    "type": "string",
    "asset-semantics": true
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 161,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Suppresses default collision sprites and replaces them with impact_sprite (which must be in the prim's inventory). Supply an empty string to only suppress collision sprites.",
 "categories": [
  "effects",
  "sound"
 ]
}
```


## functions/llComputeHash

```json
{
 "arguments": [
  {
   "message": {
    "tooltip": "Message string to be hashed.",
    "type": "string"
   }
  },
  {
   "algorithm": {
    "tooltip": "Cryptographic digest algorithm to use (e.g., md5, sha1, sha224, sha256, sha384, or sha512).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 548,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a hex-encoded hash digest string of message using the specified cryptographic algorithm.",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llCos

```json
{
 "arguments": [
  {
   "theta": {
    "tooltip": "Angle in radians.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.cos",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.cos(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 1,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the cosine of theta. Theta is in radians.",
 "categories": [
  "math",
  "math_trig"
 ]
}
```


## functions/llCreateCharacter

```json
{
 "arguments": [
  {
   "options": {
    "tooltip": "A list of key-value pairs specifying the character's configuration options.",
    "type": "list",
    "param-semantics": "CharacterParam",
    "ruleset": "character-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 399,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Converts the linkset containing the script into a pathfinding character entity (required to use pathfinding functions) using the specified options.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llCreateKeyValue

```json
{
 "arguments": [
  {
   "k": {
    "tooltip": "Unique key name for the key-value pair.",
    "type": "string"
   }
  },
  {
   "v": {
    "tooltip": "Value for the key-value pair (maximum 2047 characters, or 4095 characters if using Mono).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 387,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Starts an asynchronous transaction to create a key-value pair (k and v) associated with the script's experience. Returns a key query handle for the dataserver event. Fails with XP_ERROR_STORAGE_EXCEPTION if the key already exists.",
 "categories": [
  "data_storage",
  "dataserver",
  "experience",
  "experience_data"
 ]
}
```


## functions/llCreateLink

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the target prim/object in the same region.",
    "type": "key"
   }
  },
  {
   "parent": {
    "tooltip": "Boolean. If TRUE, the script's object becomes the root prim; if FALSE, target becomes the root.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 141,
 "return": "void",
 "sleep": 0.1,
 "requires-permission": [
  "PERMISSION_CHANGE_LINKS"
 ],
 "tooltip": "Attempts to link the object containing the script with target. Requires the PERMISSION_CHANGE_LINKS runtime permission.",
 "categories": [
  "linkset"
 ]
}
```


## functions/llDamage

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "Key of the target avatar or task to receive damage.",
    "type": "key"
   }
  },
  {
   "damage": {
    "tooltip": "Amount of damage to inflict (can exceed 100, unlike collision-based damage).",
    "type": "float"
   }
  },
  {
   "damage_type": {
    "tooltip": "Type of damage to deliver to the target (can correspond to a DAMAGE_TYPE_* constant).",
    "type": "integer",
    "enum-semantics": "DamageType"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 671,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Generates a damage event delivering the specified amount of damage and damage_type to the targeted avatar or task in the same region.",
 "categories": [
  "combat"
 ]
}
```


## functions/llDataSizeKeyValue

```json
{
 "arguments": [],
 "energy": 10.0,
 "experience": true,
 "func-id": 600,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Starts an asynchronous transaction to request the used and total data storage allocated for the experience. Returns a key query handle for the dataserver event.",
 "categories": [
  "data_storage",
  "dataserver",
  "experience",
  "experience_data"
 ]
}
```


## functions/llDeleteCharacter

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 405,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Converts the linkset back to a standard physical object, removing all pathfinding properties.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llDeleteKeyValue

```json
{
 "arguments": [
  {
   "k": {
    "tooltip": "Key of the key-value pair to delete.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 390,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Starts an asynchronous transaction to delete the key-value pair associated with key k in the experience. Returns a key query handle for the dataserver event.",
 "categories": [
  "data_storage",
  "dataserver",
  "experience",
  "experience_data"
 ]
}
```


## functions/llDeleteSubList

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "src": {
    "tooltip": "Source list to copy and modify.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "start_index": {
    "tooltip": "Starting index of the slice to remove (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Ending index of the slice to remove (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "table.remove",
  "reason": "Unnecessary table copying.",
  "selene-replace": [
   "table.remove(%1, %2)"
  ]
 },
 "energy": 10.0,
 "func-id": 193,
 "native": true,
 "pure": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a copy of the list src with the slice from start_index to end_index (inclusive) removed. Negative indices count backward from the end of the list. If start_index is greater than end_index, the deletion excludes the specified range.",
 "categories": [
  "list"
 ]
}
```


## functions/llDeleteSubString

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to modify.",
    "type": "string"
   }
  },
  {
   "start_index": {
    "tooltip": "Starting codepoint index of the substring to remove (inclusive). Supports negative indexing.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Ending codepoint index of the substring to remove (inclusive). Supports negative indexing.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 95,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a copy of the string src with the characters from start_index to end_index (inclusive) removed. Negative indices count backward from the end of the string. If start_index is greater than end_index, the deletion excludes the specified range.",
 "categories": [
  "string"
 ]
}
```


## functions/llDerezObject

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the object in the region to derez.",
    "type": "key"
   }
  },
  {
   "flags": {
    "tooltip": "Derez behavior flags matching DEREZ_* constants.",
    "type": "integer",
    "enum-semantics": "DerezMode"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 509,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Derezzes (deletes or returns) a targeted object in the region previously rezzed by a script in this linkset, returning TRUE on success or FALSE on failure.",
 "categories": [
  "prim_inventory",
  "rez"
 ]
}
```


## functions/llDetachFromAvatar

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 114,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_ATTACH"
 ],
 "tooltip": "Detaches the object containing the script from the avatar. Requires the PERMISSION_ATTACH runtime permission (automatically granted to attached objects). Note that the detached object is completely removed from the region and not dropped on the ground.",
 "categories": [
  "attachments",
  "avatar"
 ]
}
```


## functions/llDetectedDamage

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 554,
 "must-use": true,
 "return": "list",
 "enum-semantics": "DamageType",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a list containing pending damage information for the event specified by number, including the current damage, the damage type, and the original damage delivered.",
 "categories": [
  "combat",
  "detected"
 ],
 "uses-enum": "DamageType"
}
```


## functions/llDetectedGrab

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 37,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the grab offset of the user touching the object. Only works in touch events and returns <0.0, 0.0, 0.0> if number is not a valid index.",
 "categories": [
  "detected",
  "touch"
 ]
}
```


## functions/llDetectedGroup

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 39,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns TRUE if the detected object or avatar specified by number has the same active group as the prim containing the script. Returns FALSE if the group is not active or if they are not in the group.",
 "categories": [
  "detected"
 ]
}
```


## functions/llDetectedKey

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 32,
 "must-use": true,
 "return": "key",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the detected object or avatar specified by number, or NULL_KEY if number is not a valid index.",
 "categories": [
  "detected",
  "uuid"
 ]
}
```


## functions/llDetectedLinkNumber

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 40,
 "must-use": true,
 "return": "integer",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the link number (integer) of the triggered event (touches and collisions only) specified by number. Returns 0 for non-linked objects, 1 for the root prim, and 2+ for child prims. Returns 0 if not supported by the event.",
 "categories": [
  "detected"
 ]
}
```


## functions/llDetectedName

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 31,
 "must-use": true,
 "return": "string",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a string representing the name of the detected object or avatar specified by item. Returns an empty string if item is not a valid index.",
 "categories": [
  "detected"
 ]
}
```


## functions/llDetectedOwner

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 33,
 "must-use": true,
 "return": "key",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the owner of the detected object specified by number. Returns an invalid key if number is not a valid index.",
 "categories": [
  "avatar",
  "detected"
 ]
}
```


## functions/llDetectedPos

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 35,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the vector position (in region coordinates) of the detected object or avatar specified by number, or <0.0, 0.0, 0.0> if number is not a valid index.",
 "categories": [
  "detected"
 ]
}
```


## functions/llDetectedRezzer

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 553,
 "must-use": true,
 "return": "key",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the object or avatar that rezzed the detected object specified by number.",
 "categories": [
  "detected"
 ]
}
```


## functions/llDetectedRot

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 38,
 "must-use": true,
 "return": "rotation",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the rotation of the detected object or avatar specified by number, or <0.0, 0.0, 0.0, 1.0> if number is not a valid offset index.",
 "categories": [
  "detected"
 ]
}
```


## functions/llDetectedTouchBinormal

```json
{
 "arguments": [
  {
   "index": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 341,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the surface binormal vector (tangent to the surface, pointing along the positive T (V) direction of tangent space) at the touched location specified by index. Can be used with llDetectedTouchNormal to determine the tangent space.",
 "categories": [
  "detected",
  "touch"
 ]
}
```


## functions/llDetectedTouchFace

```json
{
 "arguments": [
  {
   "index": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 338,
 "must-use": true,
 "return": "integer",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the integer index of the face clicked by the avatar in the touch event specified by index.",
 "categories": [
  "detected",
  "touch"
 ]
}
```


## functions/llDetectedTouchNormal

```json
{
 "arguments": [
  {
   "index": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 340,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the surface normal vector (perpendicular to the surface) at the touched location specified by index. Can be used with llDetectedTouchBinormal to determine the tangent space.",
 "categories": [
  "detected",
  "touch"
 ]
}
```


## functions/llDetectedTouchPos

```json
{
 "arguments": [
  {
   "index": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 339,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the vector position where the object was touched (specified by index) in region coordinates, or in screen-space coordinates if the object is attached as a HUD.",
 "categories": [
  "detected",
  "touch"
 ]
}
```


## functions/llDetectedTouchST

```json
{
 "arguments": [
  {
   "index": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 342,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the surface coordinates (<s, t, 0.0>) where the prim was touched, specified by index. X and Y contain the horizontal (s) and vertical (t) face coordinates, typically in the interval [0.0, 1.0]. Returns TOUCH_INVALID_TEXCOORD if coordinates cannot be determined.",
 "categories": [
  "detected",
  "touch"
 ]
}
```


## functions/llDetectedTouchUV

```json
{
 "arguments": [
  {
   "index": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 337,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the texture coordinates (<u, v, 0.0>) where the prim was touched, specified by index. X and Y contain the horizontal (u) and vertical (v) texture coordinates, typically in the interval [0.0, 1.0] (affected by repeats and rotation). Returns TOUCH_INVALID_TEXCOORD if coordinates cannot be determined.",
 "categories": [
  "detected",
  "touch"
 ]
}
```


## functions/llDetectedType

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 34,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "DetectType",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns an integer bitfield representing the types (AGENT, ACTIVE, PASSIVE, or SCRIPTED) of the detected object or avatar specified by number. Returns 0 if number is not a valid index.",
 "categories": [
  "detected"
 ],
 "other-values": true
}
```


## functions/llDetectedVel

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Index of the detection information.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 36,
 "must-use": true,
 "return": "vector",
 "detected-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the vector velocity of the detected object or avatar specified by number, or <0.0, 0.0, 0.0> if number is not a valid offset index.",
 "categories": [
  "detected"
 ]
}
```


## functions/llDialog

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the agent in the same region.",
    "type": "key"
   }
  },
  {
   "msg": {
    "tooltip": "Text message to display in the dialog box.",
    "type": "string"
   }
  },
  {
   "buttons": {
    "tooltip": "A list of up to 12 strings representing button labels.",
    "type": "list",
    "slua-type": "{string}"
   }
  },
  {
   "channel": {
    "tooltip": "Output chat channel (any 32-bit signed integer value) where button clicks are chatted.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 247,
 "return": "void",
 "sleep": 1.0,
 "tooltip": "Shows a dialog box on the screen of the specified agent, displaying msg along with up to 12 choice buttons. Clicking a button chats its label on channel. The chat originates at the object's position, but uses the agent's name and UUID, so it can be heard as long as the agent is still in the region.",
 "categories": [
  "avatar_communication",
  "chat",
  "user_interface"
 ]
}
```


## functions/llDie

```json
{
 "arguments": [],
 "energy": 0.0,
 "func-id": 41,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Deletes the entire object containing the script (the object does not go to inventory). Use llBreakLink first to delete only a single prim.",
 "categories": [
  "rez"
 ]
}
```


## functions/llDumpList2String

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list to convert.",
    "type": "list"
   }
  },
  {
   "separator": {
    "tooltip": "Separator string to place between list entries.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 245,
 "native": true,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string that is the list src converted to a single string, with separator placed between each entry.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llEdgeOfWorld

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates.",
    "type": "vector"
   }
  },
  {
   "dir": {
    "tooltip": "Direction vector.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 205,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Checks if the border reached along the vector dir from the vector pos is the edge of the world (i.e., has no neighboring simulator). Returns TRUE if it hits the edge of the world, or FALSE if there is a neighboring simulator.",
 "categories": [
  "region"
 ]
}
```


## functions/llEjectFromLand

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 213,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Ejects the specified avatar from land/parcels owned by the object's owner (group or resident).",
 "categories": [
  "land_moderation",
  "parcel"
 ]
}
```


## functions/llEmail

```json
{
 "arguments": [
  {
   "address": {
    "tooltip": "Destination email address.",
    "type": "string"
   }
  },
  {
   "subject": {
    "tooltip": "Subject of the email.",
    "type": "string"
   }
  },
  {
   "msg": {
    "tooltip": "Message body of the email.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 119,
 "return": "void",
 "sleep": 20.0,
 "tooltip": "Sends an email with the given destination address, subject, and body msg. The email will be sent from `{ll.GetKey()}@lsl.secondlife.com`. This can be used for script communication; see llGetNextEmail()",
 "categories": [
  "avatar_communication",
  "script_communication"
 ]
}
```


## functions/llEscapeURL

```json
{
 "arguments": [
  {
   "url": {
    "tooltip": "Unescaped URL string to escape.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 307,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string representing the escaped/encoded version of url, replacing spaces with '%20' and non-alphanumeric characters with their '%xx' hexadecimal UTF-8 equivalent.",
 "categories": [
  "web"
 ]
}
```


## functions/llEuler2Rot

```json
{
 "arguments": [
  {
   "vec": {
    "tooltip": "Vector of Euler angles to convert, in radians.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 16,
 "pure": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns the quaternion representation of the Euler angles (in radians) within vec.",
 "categories": [
  "math",
  "math_3d",
  "quaternion"
 ]
}
```


## functions/llEvade

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the group, avatar, or object to evade.",
    "type": "key"
   }
  },
  {
   "options": {
    "tooltip": "No options currently available (should be empty list).",
    "type": "list",
    "param-semantics": "CharacterEvadeParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 407,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Directs a pathfinding character to evade target, attempting to hide from its pursuer if a hiding spot is available (i.e., no line of sight from the character's head to the pursuer's head, and no direct path on the navmesh).",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llExecCharacterCmd

```json
{
 "arguments": [
  {
   "command": {
    "tooltip": "Pathfinding command to execute.",
    "type": "integer",
    "enum-semantics": "CharacterCommand"
   }
  },
  {
   "options": {
    "tooltip": "A list of options for the command (e.g., jump height for CHARACTER_CMD_JUMP).",
    "type": "list"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 404,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sends a command (specified by command) to the pathing system with options. Currently only supports stopping pathfinding or making the character jump.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llFabs

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Number to convert.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.abs",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.abs(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 7,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the absolute (positive) value of val.",
 "categories": [
  "math"
 ]
}
```


## functions/llFindNotecardTextCount

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the notecard in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "pattern": {
    "tooltip": "Regular expression pattern to search for.",
    "type": "string"
   }
  },
  {
   "options": {
    "tooltip": "A list of options to control the search (currently unused, should be []).",
    "type": "list",
    "param-semantics": "FindNotecardTextParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 507,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Asynchronously requests the number of matches of pattern in the notecard name. Returns a key query handle for the dataserver event.",
 "categories": [
  "data_storage",
  "dataserver",
  "notecard"
 ]
}
```


## functions/llFindNotecardTextSync

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the notecard in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "pattern": {
    "tooltip": "Regular expression pattern to search for.",
    "type": "string"
   }
  },
  {
   "start": {
    "tooltip": "Index of the first match to return.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "count": {
    "tooltip": "Maximum number of matches to return (if 0, returns the first 64 matches).",
    "type": "integer"
   }
  },
  {
   "options": {
    "tooltip": "A list of options to control the search (currently unused, should be []).",
    "type": "list",
    "param-semantics": "FindNotecardTextParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 508,
 "must-use": true,
 "return": "list",
 "index-semantics": true,
 "sleep": 0.0,
 "tooltip": "Synchronously searches the notecard name in the region's cache for matches of pattern, without raising a dataserver event. Returns a strided list of the form [line, column, length, ...] with one stride per match, a list containing NAK if the notecard is not cached, or an empty list if there are no matches.",
 "categories": [
  "data_storage",
  "notecard"
 ]
}
```


## functions/llFleeFrom

```json
{
 "arguments": [
  {
   "position": {
    "tooltip": "Position vector in region coordinates from which to flee.",
    "type": "vector"
   }
  },
  {
   "distance": {
    "tooltip": "Distance in meters to keep from the position.",
    "type": "float"
   }
  },
  {
   "options": {
    "tooltip": "No options currently available (should be empty list).",
    "type": "list",
    "param-semantics": "CharacterFleeFromParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 402,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Directs a pathfinding character to keep the specified distance from the target position vector (within the region or adjacent regions).",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llFloor

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Number to round down.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.floor",
  "reason": "Fastcall.",
  "selene-replace": [
   "math.floor(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 9,
 "native": true,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns val rounded toward negative infinity. In other words, returns the largest integer less than or equal to val.",
 "categories": [
  "math"
 ]
}
```


## functions/llForceMouselook

```json
{
 "arguments": [
  {
   "mouselook": {
    "tooltip": "Boolean. If TRUE, forces a sitting avatar into mouselook; if FALSE, allows them to keep their current camera mode.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 294,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets whether any avatar sitting on this prim is forced into mouselook mode. Setting mouselook to TRUE forces the mode; FALSE (default) allows the avatar to keep their current camera mode.",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llFrand

```json
{
 "arguments": [
  {
   "mag": {
    "tooltip": "Float magnitude of the random range.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 8,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a pseudo-random float in the range [0.0, mag) or (mag, 0.0] depending on the sign of mag. The value is inclusive of 0.0 but exclusive of mag.",
 "categories": [
  "math"
 ]
}
```


## functions/llGenerateKey

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 383,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Generates and returns a unique versioned UUID key (utilizing SHA-1 hashing). Due to being versioned, it will not return NULL_KEY; however, the exact UUID version is an implementation detail that should not be relied upon.",
 "categories": [
  "uuid"
 ]
}
```


## functions/llGetAccel

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 78,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the acceleration of the object in the region's frame of reference.",
 "categories": [
  "physics"
 ]
}
```


## functions/llGetAgentInfo

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 206,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "AgentInfo",
 "sleep": 0.0,
 "tooltip": "Returns an integer bitfield containing status information about the agent specified by id (such as AGENT_FLYING, AGENT_ATTACHMENTS, AGENT_SITTING, etc.).",
 "categories": [
  "avatar"
 ]
}
```


## functions/llGetAgentLanguage

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 336,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string representing the language code of the preferred interface language set by the avatar.",
 "categories": [
  "avatar"
 ]
}
```


## functions/llGetAgentList

```json
{
 "arguments": [
  {
   "scope": {
    "tooltip": "Scope flag (AGENT_LIST_PARCEL, AGENT_LIST_PARCEL_OWNER, or AGENT_LIST_REGION) to filter the returned agents.",
    "type": "integer",
    "enum-semantics": "AgentListScope"
   }
  },
  {
   "options": {
    "tooltip": "A list of options to apply (currently unused).",
    "type": "list",
    "param-semantics": "AgentListParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 412,
 "must-use": true,
 "return": "list",
 "slua-return": "{uuid}",
 "sleep": 0.0,
 "tooltip": "Requests a list of avatar UUID keys for agents currently in the region, limited by scope. Returns a list of keys or a list containing an error message string.",
 "categories": [
  "avatar",
  "parcel",
  "region"
 ]
}
```


## functions/llGetAgentSize

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 218,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the estimated bounding box size of the specified avatar, or ZERO_VECTOR if they are not in the same region.",
 "categories": [
  "avatar"
 ]
}
```


## functions/llGetAlpha

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 50,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the Blinn-Phong alpha (transparency) of face. If face is ALL_SIDES, returns the mean average of all faces.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetAndResetTime

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 84,
 "return": "float",
 "slua-removed": true,
 "sleep": 0.0,
 "tooltip": "Returns the elapsed script time in seconds as a float, then resets the script timer to zero.",
 "categories": [
  "script"
 ]
}
```


## functions/llGetAnimation

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 162,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string representing the name of the currently playing locomotion animation for the specified avatar.",
 "categories": [
  "avatar",
  "avatar_animation",
  "permissions"
 ]
}
```


## functions/llGetAnimationList

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 266,
 "must-use": true,
 "return": "list",
 "slua-return": "{uuid}",
 "sleep": 0.0,
 "tooltip": "Returns a list of keys (UUIDs) representing all active animations currently playing on the specified avatar.",
 "categories": [
  "avatar",
  "avatar_animation",
  "permissions"
 ]
}
```


## functions/llGetAnimationOverride

```json
{
 "arguments": [
  {
   "anim_state": {
    "tooltip": "Animation state string to query.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 500,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_OVERRIDE_ANIMATIONS",
  "PERMISSION_TRIGGER_ANIMATION"
 ],
 "tooltip": "Returns a string representing the name of the animation currently overriding the specified anim_state. Requires the PERMISSION_OVERRIDE_ANIMATIONS or PERMISSION_TRIGGER_ANIMATION runtime permission.",
 "categories": [
  "avatar",
  "avatar_animation",
  "permissions"
 ]
}
```


## functions/llGetAttached

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 224,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "AttachPoint",
 "sleep": 0.0,
 "tooltip": "Returns the integer attachment point (an ATTACH_* constant) that the object is attached to, or 0 if it is unattached or pending detachment.",
 "categories": [
  "attachments"
 ],
 "other-values": true
}
```


## functions/llGetAttachedList

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 523,
 "must-use": true,
 "return": "list",
 "slua-return": "{uuid} | {string}",
 "sleep": 0.0,
 "tooltip": "Returns a list of object keys (UUIDs) worn by the specified avatar, in the order they were attached. HUDs are not included because they are neither public nor visible. Returns a list containing an error message string on failure.",
 "categories": [
  "attachments",
  "avatar"
 ]
}
```


## functions/llGetAttachedListFiltered

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  },
  {
   "options": {
    "tooltip": "A list of options to filter the returned attachments.",
    "type": "list",
    "param-semantics": "AttachedListFilterParam",
    "ruleset": "attached-list-filter-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 518,
 "must-use": true,
 "return": "list",
 "slua-return": "{uuid} | {string}",
 "sleep": 0.0,
 "tooltip": "Returns a list of object keys (UUIDs) worn by the specified avatar, in the order they were attached, filtered by options. Returns a list containing an error message string on failure.",
 "categories": [
  "attachments",
  "avatar"
 ]
}
```


## functions/llGetBoundingBox

```json
{
 "arguments": [
  {
   "object": {
    "tooltip": "UUID of the avatar or prim in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 277,
 "must-use": true,
 "return": "list",
 "slua-return": "{vector}",
 "sleep": 0.0,
 "tooltip": "Returns the bounding box of object (including any linked prims) relative to its root prim in local coordinates, formatted as [ (vector) min_corner, (vector) max_corner ].",
 "categories": [
  "object"
 ]
}
```


## functions/llGetCameraAspect

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 545,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TRACK_CAMERA"
 ],
 "tooltip": "Returns a float representing the camera's current aspect ratio (width/height) of the agent who granted PERMISSION_TRACK_CAMERA. Returns 0.0 if permissions are not granted.",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llGetCameraFOV

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 546,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TRACK_CAMERA"
 ],
 "tooltip": "Returns a float representing the camera's current field of view (FOV) in radians of the agent who granted PERMISSION_TRACK_CAMERA. Returns 0.0 if permissions are not granted.",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llGetCameraPos

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 303,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TRACK_CAMERA"
 ],
 "tooltip": "Returns a vector representing the camera's current position in region coordinates of the agent who granted PERMISSION_TRACK_CAMERA. Returns ZERO_VECTOR if permissions are not granted.",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llGetCameraRot

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 304,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TRACK_CAMERA"
 ],
 "tooltip": "Returns a rotation representing the camera's current orientation of the agent who granted PERMISSION_TRACK_CAMERA. Returns ZERO_ROTATION if permissions are not granted.",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llGetCenterOfMass

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 183,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the vector position (in region coordinates) of the center of mass. Returns the individual child prim's center of mass if called from a child, or the entire linkset's center of mass if called from the root.",
 "categories": [
  "object",
  "physics"
 ]
}
```


## functions/llGetClosestNavPoint

```json
{
 "arguments": [
  {
   "point": {
    "tooltip": "Position vector in region-local coordinates.",
    "type": "vector"
   }
  },
  {
   "options": {
    "tooltip": "A list of GCNP_* flags and parameters to configure the search limits.",
    "type": "list",
    "param-semantics": "GetClosestNavPointParam",
    "ruleset": "get-closest-nav-point-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 408,
 "must-use": true,
 "return": "list",
 "slua-return": "{vector}",
 "sleep": 0.0,
 "tooltip": "Returns a list containing the closest vector position on the navigation mesh (navmesh) to the specified point (expressed in region-local space), or an empty list if none is found. Configured using options.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llGetColor

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 52,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the Blinn-Phong RGB color vector of face (values between 0.0 and 1.0). If face is ALL_SIDES, returns the mean average of all faces.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetCreator

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 272,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the prim's original creator.",
 "categories": [
  "prim"
 ]
}
```


## functions/llGetDate

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 204,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string representing the current date in the UTC time zone in the format 'YYYY-MM-DD'.",
 "categories": [
  "time"
 ]
}
```


## functions/llGetDayLength

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 703,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the number of seconds in the environmental day cycle applied to the current parcel.",
 "categories": [
  "time"
 ]
}
```


## functions/llGetDayOffset

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 705,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the offset duration (in seconds) added to calculate the current environmental time on this parcel.",
 "categories": [
  "time"
 ]
}
```


## functions/llGetDisplayName

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar in the same region or otherwise known to the region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 360,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the display name string of the avatar specified by id if they are in the region or cached; returns an empty string otherwise (use llRequestDisplayName if the avatar is absent).",
 "categories": [
  "avatar"
 ]
}
```


## functions/llGetEnergy

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 149,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the remaining physics energy of the object as a percentage (0.0 to 1.0) of its maximum capacity.",
 "categories": [
  "script"
 ]
}
```


## functions/llGetEnv

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the regional data to request (unrecognized strings return an empty string).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 362,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the requested regional data specified by name.",
 "categories": [
  "region"
 ]
}
```


## functions/llGetEnvironment

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates (X/Y determine the parcel, or region if X/Y are -1; Z determines the sky track altitude).",
    "type": "vector"
   }
  },
  {
   "params": {
    "tooltip": "A list of environmental attributes to retrieve.",
    "type": "list",
    "param-get-semantics": "EnvironmentParamReadOnly",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 711,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "EnvironmentParamReadOnly",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a list containing the current environment parameters for the parcel or region at pos, retrieved in the order specified by params.",
 "categories": [
  "parcel",
  "parcel_appearance"
 ]
}
```


## functions/llGetExperienceDetails

```json
{
 "arguments": [
  {
   "experience_id": {
    "tooltip": "UUID of the experience to query (can be NULL_KEY to retrieve details for the script's own experience).",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 409,
 "must-use": true,
 "return": "list",
 "sleep": 0.0,
 "tooltip": "Returns a list of details for the specified experience_id, formatted as [string experience_name, key owner_id, key experience_id, integer state, string state_message, key group_id].",
 "categories": [
  "experience"
 ]
}
```


## functions/llGetExperienceErrorMessage

```json
{
 "arguments": [
  {
   "error": {
    "tooltip": "XP_ERROR_* error code constant to translate.",
    "type": "integer",
    "enum-semantics": "ExperienceError"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 603,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a text description of the specified experience error code, or a description of XP_ERROR_UNKNOWN_ERROR if the error is invalid.",
 "categories": [
  "experience"
 ]
}
```


## functions/llGetExperienceList

```json
{
 "arguments": [
  {
   "agentid": {
    "tooltip": "",
    "type": "key"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 410,
 "private": true,
 "must-use": true,
 "return": "list",
 "slua-return": "{uuid}",
 "sleep": 0.0,
 "tooltip": "",
 "categories": [
  "experience"
 ]
}
```


## functions/llGetForce

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 65,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the constant force currently applied to the object (if the object is physical).",
 "categories": [
  "physics"
 ]
}
```


## functions/llGetFreeMemory

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 225,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the number of free bytes of memory currently available to the script.",
 "categories": [
  "script"
 ]
}
```


## functions/llGetFreeURLs

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 344,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the number of available HTTP URLs (remaining for the owner if the object is attached, or for the region if unattached).",
 "categories": [
  "script",
  "web"
 ]
}
```


## functions/llGetGMTclock

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 282,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the time in seconds since midnight GMT (truncated to whole seconds).",
 "categories": [
  "time"
 ]
}
```


## functions/llGetGameControlMode

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar whose game-controller state to query.",
    "type": "key"
   }
  }
 ],
 "categories": [
  "avatar",
  "game_control",
  "input"
 ],
 "energy": 10.0,
 "func-id": 804,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns a GAME_CONTROL_MODE_* integer indicating the current game-control mode for the avatar specified by id."
}
```


## functions/llGetGameControlModeAxes

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar whose game-controller state to query.",
    "type": "key"
   }
  }
 ],
 "categories": [
  "avatar",
  "game_control",
  "input"
 ],
 "energy": 10.0,
 "func-id": 806,
 "must-use": true,
 "return": "list",
 "slua-return": "{number}",
 "sleep": 0.0,
 "tooltip": "Returns a list of floats representing the modal axes for the current game-control mode of the avatar specified by id. Element count and index meanings vary by mode; use the GAME_CONTROL_AXIS_* constants as indices."
}
```


## functions/llGetGameControlModeButtons

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar whose game-controller state to query.",
    "type": "key"
   }
  }
 ],
 "categories": [
  "avatar",
  "game_control",
  "input"
 ],
 "energy": 10.0,
 "func-id": 805,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns a bitmask of the modal buttons currently active for the current game-control mode of the avatar specified by id. Bit meanings vary by mode; use the GAME_CONTROL_BUTTON_* constants as masks."
}
```


## functions/llGetGeometricCenter

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 278,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the geometric center of the object relative to its root prim.",
 "categories": [
  "physics"
 ]
}
```


## functions/llGetHTTPHeader

```json
{
 "arguments": [
  {
   "request_id": {
    "tooltip": "Unique key of the HTTP request.",
    "type": "key"
   }
  },
  {
   "header": {
    "tooltip": "Lowercase name of the HTTP header to retrieve.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 349,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string representing the value of the specified header associated with the HTTP request_id.",
 "categories": [
  "web"
 ]
}
```


## functions/llGetHealth

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the agent or object to query.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 552,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the current health of the avatar or object specified by id.",
 "categories": [
  "combat"
 ]
}
```


## functions/llGetInventoryAcquireTime

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 529,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the time when the item was placed in the prim's inventory, as a UTC timestamp string of the form \"YYYY-MM-DDThh:mm:ssZ\"",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llGetInventoryCreator

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 291,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the creator of the specified inventory item.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llGetInventoryDesc

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 543,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the description string of the specified inventory item.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llGetInventoryKey

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 175,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the specified inventory item.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llGetInventoryName

```json
{
 "arguments": [
  {
   "type": {
    "tooltip": "INVENTORY_* type constant of the item.",
    "type": "integer",
    "enum-semantics": "InventoryType"
   }
  },
  {
   "index": {
    "tooltip": "Index of the item of that type.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 147,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the name of the inventory item of the specified type (INVENTORY_*) at the specified inventory index.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llGetInventoryNumber

```json
{
 "arguments": [
  {
   "type": {
    "tooltip": "INVENTORY_* type constant to count.",
    "type": "integer",
    "enum-semantics": "InventoryType"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 146,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the count of items of the specified type (INVENTORY_*) in the prim's inventory.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llGetInventoryPermMask

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  },
  {
   "group": {
    "tooltip": "MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to get.",
    "type": "integer",
    "enum-semantics": "AssetPermissionCategory"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 289,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "AssetPermission",
 "sleep": 0.0,
 "tooltip": "Returns the specified item's permission flags for the specified group.",
 "categories": [
  "asset_permissions",
  "prim_inventory"
 ]
}
```


## functions/llGetInventoryType

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 301,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "InventoryType",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the INVENTORY_* type of the named inventory item.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llGetKey

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 121,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the prim containing the script.",
 "categories": [
  "prim",
  "uuid"
 ]
}
```


## functions/llGetLandOwnerAt

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 216,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the land owner at the vector pos, or NULL_KEY if the land is public.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llGetLinkKey

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 144,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the linked prim or avatar specified by link.",
 "categories": [
  "linkset",
  "uuid"
 ]
}
```


## functions/llGetLinkMedia

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  },
  {
   "face": {
    "tooltip": "Face number (side) of the prim.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  },
  {
   "params": {
    "tooltip": "A list of PRIM_MEDIA_* property constants to retrieve values for.",
    "type": "list",
    "param-get-semantics": "PrimMediaParam",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 372,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "PrimMediaParam",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a list containing the media parameters of the specified face on the linked prim link, retrieved in the order requested by params.",
 "categories": [
  "linkset",
  "media",
  "prim_media"
 ]
}
```


## functions/llGetLinkName

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 145,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the name of the linked prim specified by link.",
 "categories": [
  "linkset"
 ]
}
```


## functions/llGetLinkNumber

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 139,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the integer link number of the prim containing the script (0 for unlinked, 1 for the root, and 2+ for children).",
 "categories": [
  "prim"
 ]
}
```


## functions/llGetLinkNumberOfSides

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 357,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the number of sides (faces) of the linked prim specified by link.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llGetLinkPrimitiveParams

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag to retrieve parameters from.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  },
  {
   "params": {
    "tooltip": "A list of PRIM_* flags specifying the attributes to retrieve.",
    "type": "list",
    "param-get-semantics": "PrimParamGet",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 354,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "PrimParamGet",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a list of primitive parameters requested in params for the linked prim specified by link (equivalent to llGetPrimitiveParams).",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llGetLinkSitFlags

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 551,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "SitFlag",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the active sit flags currently set on the linked prim specified by link.",
 "categories": [
  "linkset",
  "sit"
 ]
}
```


## functions/llGetListEntryType

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list containing the element of interest.",
    "type": "list"
   }
  },
  {
   "index": {
    "tooltip": "Zero-based index of the entry.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "typeof",
  "selene-replace": [
   "typeof(%1[%2])"
  ]
 },
 "energy": 10.0,
 "func-id": 194,
 "native": true,
 "pure": true,
 "return": "integer",
 "enum-semantics": "ListEntryType",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the variable type (TYPE_*) of the list entry at index in the list src.",
 "categories": [
  "list"
 ]
}
```


## functions/llGetListLength

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "List to measure.",
    "type": "list"
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use '#' or 'rawlen' instead. Metatable support.",
  "selene-replace": [
   "#%1",
   "rawlen(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 185,
 "native": true,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the total number of elements in the list src.",
 "categories": [
  "list"
 ]
}
```


## functions/llGetLocalPos

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 60,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a position vector relative to the root prim. If called from the root prim, it returns the global region position (or the position relative to the attachment point if attached).",
 "categories": [
  "prim"
 ]
}
```


## functions/llGetLocalRot

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 63,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns a rotation representing the local orientation of a child prim relative to the root prim, or the object's overall rotation if called from the root.",
 "categories": [
  "prim"
 ]
}
```


## functions/llGetMass

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 109,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the mass of the object (in lindograms). Returns the total linkset mass if called from the root, or the individual prim's mass if called from a child prim. Returns the wearer's mass if inside an attachment.",
 "categories": [
  "linkset",
  "physics"
 ]
}
```


## functions/llGetMassMKS

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 382,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the mass of the object in kilograms. Functionally identical to llGetMass except for using MKS (metric) units.",
 "categories": [
  "linkset",
  "physics"
 ]
}
```


## functions/llGetMaxScaleFactor

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 591,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the maximum scale factor that can be applied to the object via llScaleByFactor without violating size or linkability limits.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llGetMemoryLimit

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 370,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the maximum memory limit (in bytes) that the script is allowed to allocate.",
 "categories": [
  "script"
 ]
}
```


## functions/llGetMinScaleFactor

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 590,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the minimum scale factor that can be applied to the object via llScaleByFactor without violating size limits.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llGetMoonDirection

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 701,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a normalized vector representing the current direction of the parcel's moon, taking altitude into account. Falls back to the region's moon direction if no custom parcel environment is set.",
 "categories": [
  "parcel",
  "parcel_appearance"
 ]
}
```


## functions/llGetMoonRotation

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 709,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns a rotation representing the orientation applied to the moon on the current parcel and altitude track. Falls back to the region's moon rotation if no custom parcel environment is set.",
 "categories": [
  "parcel",
  "parcel_appearance"
 ]
}
```


## functions/llGetNextEmail

```json
{
 "arguments": [
  {
   "address": {
    "tooltip": "Sender email address filter, or \"\" for any address.",
    "type": "string"
   }
  },
  {
   "subject": {
    "tooltip": "Email subject filter, or \"\" for any subject.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 120,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Requests the next queued email via the email event. Emails must\n1. Be sent to `{ll.GetKey()}@lsl.secondlife.com`\n2. Be sent from the specified sender Address (or any address if blank)\n3. Have the specified subject Subject (or any subject if blank)",
 "categories": [
  "script_communication"
 ]
}
```


## functions/llGetNotecardLine

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the notecard in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "line": {
    "tooltip": "Index of the line to read.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 217,
 "return": "key",
 "sleep": 0.1,
 "tooltip": "Asynchronously requests the text of line in the notecard name. Returns a key query handle for the dataserver event, which receives EOF if line is past the end of the notecard.",
 "categories": [
  "data_storage",
  "dataserver",
  "notecard"
 ]
}
```


## functions/llGetNotecardLineSync

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the notecard in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "line": {
    "tooltip": "Index of the line to read.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 549,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Synchronously reads the text of line in the notecard name from the region's cache, without raising a dataserver event. Returns NAK if the notecard is not cached, or EOF if line is past the end of the notecard.",
 "categories": [
  "data_storage",
  "notecard"
 ]
}
```


## functions/llGetNumberOfNotecardLines

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the notecard in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 276,
 "return": "key",
 "sleep": 0.1,
 "tooltip": "Asynchronously requests the number of lines in the notecard name. Returns a key query handle for the dataserver event.",
 "categories": [
  "data_storage",
  "dataserver",
  "notecard"
 ]
}
```


## functions/llGetNumberOfPrims

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 275,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the total number of prims and seated avatars in the linkset containing the script.",
 "categories": [
  "linkset"
 ]
}
```


## functions/llGetNumberOfSides

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 168,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the total number of sides (faces) of the prim containing the script.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetObjectAnimationNames

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 506,
 "must-use": true,
 "return": "list",
 "slua-return": "{string}",
 "asset-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a list of strings representing the names or UUIDs of all active animations currently playing on the object.",
 "categories": [
  "object_animation"
 ]
}
```


## functions/llGetObjectDesc

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 270,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the description of the specific prim containing the script.",
 "categories": [
  "prim",
  "prim_properties"
 ]
}
```


## functions/llGetObjectDetails

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar or prim (in the same or adjacent regions) to query.",
    "type": "key"
   }
  },
  {
   "params": {
    "tooltip": "A list of OBJECT_* flags specifying the attributes to retrieve.",
    "type": "list",
    "param-get-semantics": "ObjectDetailsParam",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 332,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "ObjectDetailsParam",
 "sleep": 0.0,
 "bool-semantics": true,
 "tooltip": "Returns a list containing the requested parameters of the specified avatar or object id, retrieved in the order requested by params.",
 "categories": [
  "object",
  "prim_properties"
 ]
}
```


## functions/llGetObjectLinkKey

```json
{
 "arguments": [
  {
   "object_id": {
    "tooltip": "UUID of the target prim or linkset.",
    "type": "key"
   }
  },
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag of the prim to retrieve.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 532,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the linked child prim specified by link within the linkset identified by object_id.",
 "categories": [
  "object",
  "uuid"
 ]
}
```


## functions/llGetObjectMass

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar or object to query.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 295,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the mass of the avatar or object specified by id.",
 "categories": [
  "object",
  "physics"
 ]
}
```


## functions/llGetObjectName

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 202,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the name of the specific prim containing the script.",
 "categories": [
  "prim",
  "prim_properties"
 ]
}
```


## functions/llGetObjectPermMask

```json
{
 "arguments": [
  {
   "group": {
    "tooltip": "MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to get.",
    "type": "integer",
    "enum-semantics": "AssetPermissionCategoryOrFlag"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 287,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "AssetPermission",
 "sleep": 0.0,
 "tooltip": "Returns the script's object's permission flags for the specified group.",
 "categories": [
  "asset_permissions",
  "linkset"
 ]
}
```


## functions/llGetObjectPrimCount

```json
{
 "arguments": [
  {
   "prim": {
    "tooltip": "UUID of the prim in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 323,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the total number of prims in the object containing the specified prim.",
 "categories": [
  "object"
 ]
}
```


## functions/llGetOmega

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 79,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the physical rotation (angular velocity) of the object in radians per second.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llGetOwner

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 117,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the object's current owner.",
 "categories": [
  "linkset",
  "uuid"
 ]
}
```


## functions/llGetOwnerKey

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the prim in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 182,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the owner of the prim specified by id.",
 "categories": [
  "object",
  "uuid"
 ]
}
```


## functions/llGetParcelDetails

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates (only the X and Y components are used).",
    "type": "vector"
   }
  },
  {
   "params": {
    "tooltip": "A list of PARCEL_DETAILS_* flags specifying the attributes to retrieve.",
    "type": "list",
    "param-get-semantics": "ParcelDetailsParam",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 327,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "ParcelDetailsParam",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a list containing the requested parcel details specified by params (retrieved in the same order) for the parcel at the vector pos.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llGetParcelFlags

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates (the Z component is ignored).",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 317,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "ParcelFlag",
 "sleep": 0.0,
 "tooltip": "Returns an integer bitfield of parcel flags (PARCEL_FLAG_*) for the parcel at the position pos.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llGetParcelMaxPrims

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates (the Z component is ignored).",
    "type": "vector"
   }
  },
  {
   "sim_wide": {
    "tooltip": "Boolean. If TRUE, returns the combined land impact limit for all parcels owned by the parcel owner in the region; if FALSE, returns only the limit for the specified parcel.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 326,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the maximum combined land impact (prim limit) allowed for objects on the parcel at pos, determined either for the single parcel or sim-wide based on sim_wide.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llGetParcelMusicURL

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 396,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the parcel's streaming music (audio) URL. The object owner must also be the land owner (or share the same group deeding).",
 "categories": [
  "parcel"
 ]
}
```


## functions/llGetParcelPrimCount

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates (the Z component is ignored).",
    "type": "vector"
   }
  },
  {
   "category": {
    "tooltip": "PARCEL_COUNT_* category flag.",
    "type": "integer",
    "enum-semantics": "ParcelPrimCountCategory"
   }
  },
  {
   "sim_wide": {
    "tooltip": "Boolean. If TRUE, searches all parcels in the region owned by the targeted parcel's owner; if FALSE, searches only the specified parcel.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 325,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the total land impact of objects on the parcel at pos in the specified category. If sim_wide is TRUE, returns combined usage for all regional parcels owned by the parcel owner; if FALSE, returns usage for only the specified parcel.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llGetParcelPrimOwners

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 324,
 "must-use": true,
 "return": "list",
 "sleep": 2.0,
 "tooltip": "Returns a list of up to 100 strides (formatted as [key owner, integer land_impact]) representing owners of objects on the parcel at pos, sorted by owner key. Requires owner-like permissions for the parcel and the script owner's presence in the region.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llGetPermissions

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 138,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "ScriptPermission",
 "sleep": 0.0,
 "tooltip": "Returns an integer bitfield representing the permissions (PERMISSION_*) currently granted to the script.",
 "categories": [
  "permissions"
 ]
}
```


## functions/llGetPermissionsKey

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 137,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) of the avatar that last granted or declined permissions to the script, or NULL_KEY if the permissions request was ignored or cancelled.",
 "categories": [
  "avatar",
  "permissions"
 ]
}
```


## functions/llGetPhysicsMaterial

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 381,
 "must-use": true,
 "return": "list",
 "slua-return": "{number}",
 "sleep": 0.0,
 "tooltip": "Returns a list of the format [float gravity_multiplier, float restitution, float friction, float density] detailing the physical characteristics of the object.",
 "categories": [
  "physics",
  "prim"
 ],
 "uses-enum": "PhysicsMaterialPreset"
}
```


## functions/llGetPos

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 59,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the current position of the object in region coordinates.",
 "categories": [
  "prim"
 ]
}
```


## functions/llGetPrimMediaParams

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number (side) of the prim.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  },
  {
   "params": {
    "tooltip": "A list of PRIM_MEDIA_* property constants to retrieve values for.",
    "type": "list",
    "param-get-semantics": "PrimMediaParam",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 351,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "PrimMediaParam",
 "bool-semantics": true,
 "sleep": 1.0,
 "tooltip": "Returns a list containing the media parameters of the specified face, retrieved in the order requested by params. Returns an empty list if no media exists on the face.",
 "categories": [
  "media",
  "prim",
  "prim_media"
 ]
}
```


## functions/llGetPrimitiveParams

```json
{
 "arguments": [
  {
   "params": {
    "tooltip": "A list of PRIM_* flags specifying the attributes to retrieve.",
    "type": "list",
    "param-get-semantics": "PrimParamGet",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 279,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "PrimParamGet",
 "bool-semantics": true,
 "sleep": 0.2,
 "tooltip": "Returns a list of primitive attribute values matching the requested params list.",
 "categories": [
  "prim",
  "prim_appearance",
  "prim_properties"
 ]
}
```


## functions/llGetRegionAgentCount

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 334,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the current number of avatars in the region.",
 "categories": [
  "region"
 ]
}
```


## functions/llGetRegionCorner

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 199,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector (in meters) representing the global grid coordinates of the south-west corner of the current region (Z component is always 0.0).",
 "categories": [
  "region"
 ]
}
```


## functions/llGetRegionDayLength

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 704,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the total number of seconds in the region-wide day cycle.",
 "categories": [
  "region",
  "time"
 ]
}
```


## functions/llGetRegionDayOffset

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 706,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the offset duration (in seconds) added to calculate the current environmental time for the region.",
 "categories": [
  "region",
  "time"
 ]
}
```


## functions/llGetRegionFPS

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 228,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the average region simulator frames per second (FPS).",
 "categories": [
  "region"
 ]
}
```


## functions/llGetRegionFlags

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 318,
 "must-use": true,
 "return": "integer",
 "enum-semantics": "RegionFlag",
 "sleep": 0.0,
 "tooltip": "Returns an integer bitfield representing the region flags (REGION_FLAG_*) currently enabled for the region containing the object.",
 "categories": [
  "region"
 ]
}
```


## functions/llGetRegionMoonDirection

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 702,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a normalized vector representing the current direction of the region's moon, taking altitude into account.",
 "categories": [
  "region",
  "region_appearance"
 ]
}
```


## functions/llGetRegionMoonRotation

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 710,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns a rotation representing the orientation applied to the moon at the region level, taking altitude track into account.",
 "categories": [
  "region",
  "region_appearance"
 ]
}
```


## functions/llGetRegionName

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 226,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the name of the current region.",
 "categories": [
  "region"
 ]
}
```


## functions/llGetRegionSunDirection

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 700,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a normalized vector representing the current direction of the region's sun, taking altitude into account.",
 "categories": [
  "region",
  "region_appearance"
 ]
}
```


## functions/llGetRegionSunRotation

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 708,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns a rotation representing the orientation applied to the sun at the region level, taking altitude track into account.",
 "categories": [
  "region",
  "region_appearance"
 ]
}
```


## functions/llGetRegionTimeDilation

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 227,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the current physics time dilation of the region, ranging from 0.0 (full dilation / slow) to 1.0 (no dilation / real-world speed).",
 "categories": [
  "region"
 ]
}
```


## functions/llGetRegionTimeOfDay

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 712,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float with subsecond precision representing the elapsed seconds since region environmental midnight or region uptime (whichever is smaller). If the region's sun position is fixed, returns region uptime.",
 "categories": [
  "region",
  "time"
 ]
}
```


## functions/llGetRenderMaterial

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 760,
 "must-use": true,
 "return": "string",
 "asset-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a string representing the render material on face (returns the inventory name if it is in the prim's inventory, or its key UUID otherwise).",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetRootPosition

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 268,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the position (in region coordinates) of the root prim of the linkset containing the script.",
 "categories": [
  "linkset"
 ]
}
```


## functions/llGetRootRotation

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 269,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns a rotation representing the orientation (relative to the region) of the root prim of the linkset containing the script.",
 "categories": [
  "linkset"
 ]
}
```


## functions/llGetRot

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 62,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns a rotation representing the prim's orientation relative to the region's axes.",
 "categories": [
  "prim"
 ]
}
```


## functions/llGetSPMaxMemory

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 365,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the maximum memory (in bytes) used by the script while the memory profiler was last active (only valid after using PROFILE_SCRIPT_MEMORY).",
 "categories": [
  "script"
 ]
}
```


## functions/llGetScale

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 48,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the physical scale (dimensions in meters) of the prim containing the script.",
 "categories": [
  "prim"
 ]
}
```


## functions/llGetScriptName

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 167,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the name of the script calling this function.",
 "categories": [
  "prim_inventory",
  "script"
 ]
}
```


## functions/llGetScriptState

```json
{
 "arguments": [
  {
   "script": {
    "tooltip": "Name of the script in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 250,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a boolean integer indicating whether the specified script in the prim's inventory is running (returns TRUE if running, FALSE otherwise).",
 "categories": [
  "prim_inventory",
  "script"
 ]
}
```


## functions/llGetSimStats

```json
{
 "arguments": [
  {
   "stat_type": {
    "tooltip": "SIM_STAT_* flag of the statistic to retrieve.",
    "type": "integer",
    "enum-semantics": "SimulatorStat"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 415,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float containing the value of the requested region statistic specified by stat_type.",
 "categories": [
  "region"
 ]
}
```


## functions/llGetSimulatorHostname

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 283,
 "must-use": true,
 "return": "string",
 "sleep": 10.0,
 "tooltip": "Returns a string containing the hostname of the server machine running the script (e.g., 'sim225.agni.lindenlab.com').",
 "categories": [
  "region"
 ]
}
```


## functions/llGetStartParameter

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 134,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the start/rez parameter passed to the object on creation (returns 0 if rezzed by an agent).",
 "categories": [
  "rez",
  "script"
 ]
}
```


## functions/llGetStartString

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 556,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the initialization string passed to the object's root prim on rez with llRezObjectWithParams (via REZ_PARAM_STRING; returns an empty string if rezzed by an agent).",
 "categories": [
  "rez",
  "script"
 ]
}
```


## functions/llGetStaticPath

```json
{
 "arguments": [
  {
   "start_pos": {
    "tooltip": "Starting position vector.",
    "type": "vector"
   }
  },
  {
   "end_pos": {
    "tooltip": "Target end position vector.",
    "type": "vector"
   }
  },
  {
   "radius": {
    "tooltip": "Radius of the character path, between 0.125m and 5.0m.",
    "type": "float",
    "range": [
     0.125,
     5
    ]
   }
  },
  {
   "params": {
    "tooltip": "A list specifying the CHARACTER_TYPE parameter (defaults to CHARACTER_TYPE_NONE).",
    "type": "list",
    "param-semantics": "GetStaticPathParam",
    "ruleset": "get-static-path-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 413,
 "must-use": true,
 "return": "list",
 "sleep": 0.0,
 "tooltip": "Returns a list of position vectors representing pathfinding waypoints between start and end on the static navmesh for a character of the specified radius. Ignores movable obstacles and can be used in any region regardless of dynamic pathfinding status.",
 "categories": [
  "pathfinding"
 ],
 "uses-enum": "CharacterPathUpdateType"
}
```


## functions/llGetStatus

```json
{
 "arguments": [
  {
   "status": {
    "tooltip": "Single STATUS_* flag to check.",
    "type": "integer",
    "enum-semantics": "ObjectStatusParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 46,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a boolean integer indicating whether the specified status flag status is enabled for the object.",
 "categories": [
  "linkset",
  "physics"
 ]
}
```


## functions/llGetSubString

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to slice.",
    "type": "string"
   }
  },
  {
   "start_index": {
    "tooltip": "Starting codepoint index (inclusive). Supports negative indexing.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Ending codepoint index (inclusive). Supports negative indexing.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 94,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a copy of the substring from src within the inclusive codepoint range start_index..end_index. Negative indices count backward from the end of the string. If start_index is greater than end_index, the substring is the excluded range.",
 "categories": [
  "string"
 ]
}
```


## functions/llGetSunDirection

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 177,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a normalized vector representing the current direction of the parcel's sun, taking altitude into account. Falls back to the region's sun direction if no custom parcel environment is set.",
 "categories": [
  "parcel",
  "parcel_appearance"
 ]
}
```


## functions/llGetSunRotation

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 707,
 "must-use": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns a rotation representing the orientation applied to the sun on the current parcel and altitude track. Falls back to the region's sun rotation if no custom parcel environment is set.",
 "categories": [
  "parcel",
  "parcel_appearance"
 ]
}
```


## functions/llGetTexture

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 57,
 "must-use": true,
 "return": "string",
 "asset-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns a string representing the Blinn-Phong diffuse texture on face (returns the inventory name if it is a texture in the prim's inventory, or its key UUID otherwise).",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetTextureOffset

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 178,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector containing the texture offsets of face in the X (horizontal U) and Y (vertical V) components (Z is unused).",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetTextureRot

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 180,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the texture rotation angle (in radians) on face.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetTextureScale

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 179,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector containing the texture scales of face in the X and Y components (Z is unused).",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llGetTime

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 82,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the elapsed script time in seconds with subsecond precision (since the script started, was reset, or since the last call to llResetTime or llGetAndResetTime).",
 "categories": [
  "script"
 ]
}
```


## functions/llGetTimeOfDay

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 80,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float with subsecond precision representing the elapsed seconds since parcel environmental midnight or region uptime (whichever is smaller). If the parcel's sun position is fixed, returns region uptime.",
 "categories": [
  "time"
 ]
}
```


## functions/llGetTimestamp

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 273,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the current date and time in the UTC time zone formatted as an ISO 8601 timestamp ('YYYY-MM-DDThh:mm:ss.ff..fZ').",
 "categories": [
  "time"
 ]
}
```


## functions/llGetTorque

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 75,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the physical torque force currently acting on the object (if the object is physical).",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llGetUnixTime

```json
{
 "arguments": [],
 "slua-deprecated": {
  "use": "os.time",
  "reason": "Int32 will wrap on 2038-01-19"
 },
 "energy": 10.0,
 "func-id": 316,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the current Unix timestamp (the number of seconds elapsed since 00:00:00 Jan 1, 1970 UTC).",
 "categories": [
  "time"
 ]
}
```


## functions/llGetUsedMemory

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 366,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the total number of bytes of memory currently used by the script (non-Mono scripts always return 16,384 bytes).",
 "categories": [
  "script"
 ]
}
```


## functions/llGetUsername

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar in the same region or otherwise known to the region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 358,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string representing the unique username of the avatar specified by id if they are connected to the region or cached; returns an empty string otherwise (use llRequestUsername if the avatar is absent).",
 "categories": [
  "avatar"
 ]
}
```


## functions/llGetVel

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 77,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the velocity of the object (in meters per second) relative to the global region coordinates. For physical objects, returns the velocity of its center of mass.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llGetVisualParams

```json
{
 "arguments": [
  {
   "agentid": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  },
  {
   "params": {
    "tooltip": "A list of visual parameter IDs or names to retrieve values for.",
    "type": "list",
    "slua-type": "{number | string}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 530,
 "must-use": true,
 "return": "list",
 "slua-return": "{number | \"\"}",
 "sleep": 0.0,
 "tooltip": "Returns a list containing the values of the visual parameters requested in params for the agent specified by agentid.",
 "categories": [
  "avatar"
 ]
}
```


## functions/llGetWallclock

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 81,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the time in seconds since midnight Pacific Time (PST/PDT), which is equivalent to Second Life Time (SLT) truncated to whole seconds.",
 "categories": [
  "time"
 ]
}
```


## functions/llGiveAgentInventory

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the target agent in the same region.",
    "type": "key"
   }
  },
  {
   "folder": {
    "tooltip": "Name of the destination folder to be created",
    "type": "string"
   }
  },
  {
   "items": {
    "tooltip": "The names of the items in the prim's inventory to transfer.",
    "type": "list",
    "slua-type": "{string}"
   }
  },
  {
   "options": {
    "tooltip": "A list of options to configure the inventory transfer.",
    "type": "list",
    "param-semantics": "GiveAgentInventoryParam",
    "ruleset": "give-agent-inventory-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 517,
 "return": "integer",
 "enum-semantics": "TransferError",
 "sleep": 3.0,
 "tooltip": "Gives the specified inventory items to the agent as a new folder named folder, as permitted by the permissions system. Customizes the transfer using options.",
 "categories": [
  "avatar_inventory",
  "prim_inventory"
 ]
}
```


## functions/llGiveInventory

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the target agent or prim.",
    "type": "key"
   }
  },
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory to transfer.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 150,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Gives the specified inventory item to the target, as permitted by the permissions system. The target can be any agent or an object located in the same region.",
 "categories": [
  "avatar_inventory",
  "prim_inventory"
 ]
}
```


## functions/llGiveInventoryList

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the target agent or prim in the same region.",
    "type": "key"
   }
  },
  {
   "folder": {
    "tooltip": "Name of the destination folder to be created (ignored if the target is an object).",
    "type": "string"
   }
  },
  {
   "items": {
    "tooltip": "The names of the items in the prim's inventory to transfer.",
    "type": "list",
    "slua-type": "{string}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 231,
 "return": "void",
 "sleep": 3.0,
 "tooltip": "Gives the list of inventory items to target as a new folder named folder. If target is an object, the items are passed directly into its inventory and no folder is created. The target must be an agent or an object in the same region.",
 "categories": [
  "avatar_inventory",
  "prim_inventory"
 ]
}
```


## functions/llGiveMoney

```json
{
 "arguments": [
  {
   "destination": {
    "tooltip": "UUID of the destination avatar.",
    "type": "key"
   }
  },
  {
   "amount": {
    "tooltip": "Number of L$ to transfer (must be greater than 0).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 99,
 "return": "integer",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_DEBIT"
 ],
 "tooltip": "Transfers the specified amount of L$ from the script owner to the destination avatar. Silently fails if the PERMISSION_DEBIT permission has not been granted. Returns 0 (use llTransferLindenDollars to match transactions to transaction_result events).",
 "categories": [
  "avatar",
  "money",
  "permissions"
 ]
}
```


## functions/llGodLikeRezObject

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "Asset UUID of the object to rez.",
    "type": "key"
   }
  },
  {
   "pos": {
    "tooltip": "Position vector in region coordinates where the object will be rezzed.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 135,
 "god-mode": true,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Rezzes an object directly from a UUID specified by id at the position pos, provided the owner has the god-bit set.",
 "categories": [
  "prim_inventory",
  "rez"
 ]
}
```


## functions/llGround

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position, expressed in local coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 42,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the ground height directly below the prim's position offset by the vector offset.",
 "categories": [
  "region"
 ]
}
```


## functions/llGroundContour

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position, expressed in local coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 223,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the ground contour direction (the direction with no change in elevation) directly below the prim's position offset by the vector offset.",
 "categories": [
  "region"
 ]
}
```


## functions/llGroundNormal

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position, expressed in local coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 222,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the ground surface normal vector directly below the current position offset by the vector offset.",
 "categories": [
  "region"
 ]
}
```


## functions/llGroundRepel

```json
{
 "arguments": [
  {
   "height": {
    "tooltip": "Target distance in meters above the ground or water.",
    "type": "float"
   }
  },
  {
   "water": {
    "tooltip": "Boolean. If TRUE, damp relative to the higher of land and water; if FALSE, damp relative to land only.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "tau": {
    "tooltip": "Timescale in seconds to critically damp the movement.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 230,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Critically damps the object's vertical motion to height (using critical damping timescale tau) if it is within height * 0.5 of the terrain (or water level if water is TRUE). Only works on physics-enabled objects; do not use with vehicles.",
 "categories": [
  "region"
 ]
}
```


## functions/llGroundSlope

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position, expressed in local coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 221,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the ground slope directly below the prim's position offset by the vector offset.",
 "categories": [
  "region"
 ]
}
```


## functions/llHMAC

```json
{
 "arguments": [
  {
   "private_key": {
    "tooltip": "PEM-formatted secret key to use for the HMAC hash.",
    "type": "string"
   }
  },
  {
   "msg": {
    "tooltip": "Message string to be hashed.",
    "type": "string"
   }
  },
  {
   "algorithm": {
    "tooltip": "Cryptographic digest algorithm to use.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 538,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a Base64-encoded HMAC hash of msg using the secret key private_key and the specified digest algorithm (md5, sha1, sha224, sha256, sha384, or sha512).",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llHTTPRequest

```json
{
 "arguments": [
  {
   "url": {
    "tooltip": "Destination HTTP or HTTPS URL.",
    "type": "string"
   }
  },
  {
   "parameters": {
    "tooltip": "A list of HTTP_* configuration flags and value pairs, or an HTTPRequestParams dictionary.",
    "type": "list",
    "param-semantics": "HTTPRequestParam",
    "ruleset": "http-request-params"
   }
  },
  {
   "body": {
    "tooltip": "String contents of the request body.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 320,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Sends an HTTP request to the specified url containing body and configured via parameters. Raises an http_response event and returns a key query handle identifying the request.",
 "categories": [
  "script_communication",
  "web"
 ]
}
```


## functions/llHTTPResponse

```json
{
 "arguments": [
  {
   "request_id": {
    "tooltip": "Unique key identifying the incoming HTTP request.",
    "type": "key"
   }
  },
  {
   "status": {
    "tooltip": "Integer HTTP status code (such as 200, 400, or 404) to respond with.",
    "type": "integer"
   }
  },
  {
   "body": {
    "tooltip": "String contents of the response body.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 348,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Responds to the incoming HTTP request identified by request_id with the HTTP status code status and the payload body.",
 "categories": [
  "media",
  "prim_media",
  "script_communication",
  "web"
 ]
}
```


## functions/llHash

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "String to hash.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 528,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns an integer representing the 32-bit hash value of the string val (returns 0 if the string is empty).",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llInsertString

```json
{
 "arguments": [
  {
   "dst": {
    "tooltip": "Target destination string.",
    "type": "string"
   }
  },
  {
   "index": {
    "tooltip": "Codepoint index where insertion starts.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "src": {
    "tooltip": "Source string to insert.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 96,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a copy of dst with src inserted at the given codepoint index.",
 "categories": [
  "string"
 ]
}
```


## functions/llInstantMessage

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the destination agent.",
    "type": "key"
   }
  },
  {
   "msg": {
    "tooltip": "Text message string to send.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 118,
 "return": "void",
 "sleep": 2.0,
 "tooltip": "Sends an instant message containing msg to the agent identified by their key.",
 "categories": [
  "avatar_communication"
 ]
}
```


## functions/llIntegerToBase64

```json
{
 "arguments": [
  {
   "number": {
    "tooltip": "Integer number to encode.",
    "type": "integer"
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use 'llbase64.encode' and 'string.pack' or 'buffer.writei32' instead.",
  "selene-replace": [
   "llbase64.encode(string.pack(\">i\", i))"
  ]
 },
 "energy": 10.0,
 "func-id": 280,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns an 8-character Base64 string representing the big-endian encoded value of number.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llIsFriend

```json
{
 "arguments": [
  {
   "agent_id": {
    "tooltip": "UUID of the agent to check.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 542,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns TRUE if agent_id and the owner of the script are friends, and FALSE otherwise.",
 "categories": [
  "avatar"
 ]
}
```


## functions/llIsLinkGLTFMaterial

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (or LINK_* flag) of the prim to inspect.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  },
  {
   "face": {
    "tooltip": "Face number (or ALL_SIDES) of the prim to inspect.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 559,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Checks the specified face on the linked prim link. Returns TRUE if the face material is a PBR render material, or FALSE if it uses Blinn-Phong diffuse textures.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llJson2List

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "JSON string to parse.",
    "type": "string"
   }
  }
 ],
 "slua-deprecated": {
  "use": "lljson.decode"
 },
 "energy": 10.0,
 "func-id": 513,
 "pure": true,
 "return": "list",
 "sleep": 0.0,
 "tooltip": "Parses the JSON string src and returns a list representing its top-level elements.",
 "categories": [
  "data_conversion",
  "json"
 ]
}
```


## functions/llJsonGetValue

```json
{
 "arguments": [
  {
   "json": {
    "tooltip": "JSON string to query.",
    "type": "string"
   }
  },
  {
   "specifiers": {
    "tooltip": "A list of key names or array indices specifying the path to the desired value.",
    "type": "list"
   }
  }
 ],
 "slua-deprecated": {
  "use": "lljson.decode",
  "reason": "Also, the indices are zero-based."
 },
 "energy": 10.0,
 "func-id": 511,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Parses the JSON string json and returns the value found by traversing the specified path of specifiers as a string.",
 "categories": [
  "data_conversion",
  "json"
 ]
}
```


## functions/llJsonSetValue

```json
{
 "arguments": [
  {
   "json": {
    "tooltip": "Source JSON string to modify.",
    "type": "string"
   }
  },
  {
   "specifiers": {
    "tooltip": "A list of key names or array indices specifying the path to add, update, or delete.",
    "type": "list"
   }
  },
  {
   "value": {
    "tooltip": "New value to set, or the JSON_DELETE constant to delete the targeted element.",
    "type": "string"
   }
  }
 ],
 "slua-deprecated": {
  "use": "lljson.encode",
  "reason": "Also, the indices are zero-based."
 },
 "energy": 10.0,
 "func-id": 510,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a new JSON string representing json with the target located at specifiers set to value. Supports JSON_APPEND to append elements. Writing JSON_DELETE deletes the target. Overwriting array bounds or setting non-array levels with array indices returns JSON_INVALID.",
 "categories": [
  "data_conversion",
  "json"
 ]
}
```


## functions/llJsonValueType

```json
{
 "arguments": [
  {
   "json": {
    "tooltip": "JSON string containing the value to query.",
    "type": "string"
   }
  },
  {
   "specifiers": {
    "tooltip": "A list of key names or array indices specifying the path to the value.",
    "type": "list"
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use 'lljson.decode' and 'typeof' instead. Also, the indices are zero-based."
 },
 "energy": 10.0,
 "func-id": 512,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Parses the JSON string json and returns the JSON type constant (JSON_*) representing the value found at specifiers.",
 "categories": [
  "data_conversion",
  "json"
 ],
 "uses-enum": [
  "JSON_INVALID",
  "JSON_OBJECT",
  "JSON_ARRAY",
  "JSON_NUMBER",
  "JSON_STRING",
  "JSON_NULL",
  "JSON_TRUE",
  "JSON_FALSE",
  "JSON_DELETE"
 ]
}
```


## functions/llKey2Name

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the target avatar or prim in the same region.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 210,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string containing the name of the prim or avatar specified by id. The target must be a valid, rezzed entity in the current region, otherwise an empty string is returned. Avatars return their legacy name.",
 "categories": [
  "object"
 ]
}
```


## functions/llKeyCountKeyValue

```json
{
 "arguments": [],
 "energy": 10.0,
 "experience": true,
 "func-id": 601,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Starts an asynchronous transaction requesting the total count of keys in the experience data store. Returns a key query handle for the dataserver event.",
 "categories": [
  "data_storage",
  "dataserver",
  "experience",
  "experience_data"
 ]
}
```


## functions/llKeysKeyValue

```json
{
 "arguments": [
  {
   "first": {
    "tooltip": "Zero-based start index of the keys to retrieve.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "count": {
    "tooltip": "Number of keys to retrieve.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 602,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Starts an asynchronous transaction to retrieve count keys from the experience data store starting at the zero-based index first. Returns a key query handle for the dataserver event. Fails with XP_ERROR_KEY_NOT_FOUND if out of bounds.",
 "categories": [
  "data_storage",
  "dataserver",
  "experience",
  "experience_data"
 ]
}
```


## functions/llLinear2sRGB

```json
{
 "arguments": [
  {
   "color": {
    "tooltip": "Color vector in the linear RGB space to convert.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 715,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a sRGB colorspace vector converted from the linear RGB colorspace argument.",
 "categories": [
  "data_conversion",
  "math",
  "prim_appearance",
  "vector"
 ]
}
```


## functions/llLinkAdjustSoundVolume

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag of the prim to adjust.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 535,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Adjusts the volume of the currently playing sound attached to the linked prim link (has no effect on sounds started with llTriggerSound).",
 "categories": [
  "sound"
 ]
}
```


## functions/llLinkParticleSystem

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "rules": {
    "tooltip": "A list of particle system rules and data pairs [rule1, data1, ...], or a ParticleParams dictionary.",
    "type": "list",
    "param-semantics": "ParticleParam",
    "ruleset": "particle-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 355,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Creates or updates a particle system on the linked prim link based on the list of rules. An empty list removes the particle system.",
 "categories": [
  "effects",
  "particles"
 ]
}
```


## functions/llLinkPlaySound

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float",
    "range": [
     0,
     1
    ]
   }
  },
  {
   "flags": {
    "tooltip": "Bitwise flags (combination of SOUND_*) controlling the sound playback.",
    "type": "integer",
    "enum-semantics": "PlaySoundFlag"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 533,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays the specified sound on the linked prim link (once or looping) at volume. Only one sound can be attached to a prim at a time; new attachments or calling llStopSound stops previous playback. Controlled by flags.",
 "categories": [
  "sound"
 ]
}
```


## functions/llLinkSetSoundQueueing

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "queue": {
    "tooltip": "Boolean. If TRUE, sound queuing is enabled; if FALSE, it is disabled.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 537,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Enables or disables sound queuing on the linked prim link. When set to TRUE, sounds will queue and play in sequence.",
 "categories": [
  "sound"
 ]
}
```


## functions/llLinkSetSoundRadius

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "radius": {
    "tooltip": "Maximum distance in meters at which the sounds can be heard.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 536,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Limits the audibility radius of attached and triggered scripted sounds to distance radius (in meters) around the linked prim link.",
 "categories": [
  "sound"
 ]
}
```


## functions/llLinkSitTarget

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  },
  {
   "offset": {
    "tooltip": "Offset position vector in local prim coordinates.",
    "type": "vector",
    "range": [
     "<-300,-300,-300>",
     "<300,300,300>"
    ]
   }
  },
  {
   "rot": {
    "tooltip": "Rotation relative to the prim's rotation.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 375,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the sit target position (offset) and orientation (rot) for the linked prim link, relative to the prim's own position and rotation. Clear by setting offset to <0.0, 0.0, 0.0>.",
 "categories": [
  "linkset",
  "sit"
 ]
}
```


## functions/llLinkStopSound

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 534,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops the playback of any currently playing attached sound on the linked prim link.",
 "categories": [
  "sound"
 ]
}
```


## functions/llLinksetDataAvailable

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 654,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the number of bytes remaining in the linkset datastore.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataCountFound

```json
{
 "arguments": [
  {
   "pattern": {
    "tooltip": "Regular expression (regex) matching the keys to count.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 661,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the number of keys in the linkset datastore that match the regular expression pattern.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataCountKeys

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 653,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the number of keys in the linkset datastore.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataDelete

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the key to delete.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 652,
 "return": "integer",
 "enum-semantics": "LinksetDataError",
 "sleep": 0.0,
 "tooltip": "Deletes the unprotected key name from the linkset datastore, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataDeleteFound

```json
{
 "arguments": [
  {
   "pattern": {
    "tooltip": "Regular expression (regex) matching the keys to delete.",
    "type": "string"
   }
  },
  {
   "pass": {
    "tooltip": "Optional passphrase required to delete matching protected keys.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 662,
 "return": "list",
 "slua-return": "{number}",
 "sleep": 0.0,
 "tooltip": "Deletes all keys in the linkset datastore that match the regular expression pattern, triggering a linkset_data event if the datastore changes. Protected keys are only deleted if their passphrase matches pass. Returns a list [num_deleted, num_failed_protected].",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataDeleteProtected

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the protected key to delete.",
    "type": "string"
   }
  },
  {
   "pass": {
    "tooltip": "Passphrase required to delete the protected key.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 660,
 "return": "integer",
 "enum-semantics": "LinksetDataError",
 "sleep": 0.0,
 "tooltip": "Deletes the protected key name from the linkset datastore using the passphrase pass, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataFindKeys

```json
{
 "arguments": [
  {
   "pattern": {
    "tooltip": "Regular expression (regex) matching the keys to return.",
    "type": "string"
   }
  },
  {
   "start": {
    "tooltip": "Index of the first matching key to return.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "count": {
    "tooltip": "Maximum number of keys to return (or less than 1 to retrieve all matching keys).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 657,
 "must-use": true,
 "return": "list",
 "slua-return": "{string}",
 "sleep": 0.0,
 "tooltip": "Returns an alphabetically sorted list of up to count keys from the linkset datastore that match the regular expression pattern, starting at index start (returns all matching keys if count < 1).",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataListKeys

```json
{
 "arguments": [
  {
   "start": {
    "tooltip": "Index of the first key to return.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "count": {
    "tooltip": "Maximum number of keys to return (or less than 1 to retrieve all keys).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 656,
 "must-use": true,
 "return": "list",
 "slua-return": "{string}",
 "sleep": 0.0,
 "tooltip": "Returns an alphabetically sorted list of up to count keys from the linkset datastore, starting at index start (returns all keys if count < 1).",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataRead

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the key to read.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 651,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the value of the unprotected key name from the linkset datastore. Returns an empty string if the key is not found or is protected.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataReadProtected

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the protected key to read.",
    "type": "string"
   }
  },
  {
   "pass": {
    "tooltip": "Passphrase required to read the protected key.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 659,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the value of the protected key name from the linkset datastore using the passphrase pass. Returns an empty string if the key is not found or pass does not match.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataReset

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 655,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Deletes all keys from the linkset datastore, triggering a linkset_data event.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataWrite

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the key to write.",
    "type": "string"
   }
  },
  {
   "value": {
    "tooltip": "Value to write to the key (an empty string deletes the key).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 650,
 "return": "integer",
 "enum-semantics": "LinksetDataError",
 "sleep": 0.0,
 "tooltip": "Creates or updates the unprotected key name in the linkset datastore with value, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llLinksetDataWriteProtected

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the protected key to write.",
    "type": "string"
   }
  },
  {
   "value": {
    "tooltip": "Value to write to the key (an empty string deletes the key).",
    "type": "string"
   }
  },
  {
   "pass": {
    "tooltip": "Passphrase used to protect or update the key.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 658,
 "return": "integer",
 "enum-semantics": "LinksetDataError",
 "sleep": 0.0,
 "tooltip": "Creates or updates the protected key name in the linkset datastore with value using the passphrase pass, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.",
 "categories": [
  "data_storage",
  "linkset",
  "linkset_data"
 ]
}
```


## functions/llList2CSV

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list to convert.",
    "type": "list"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 195,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string of comma-separated values taken in order from the list src.",
 "categories": [
  "data_conversion",
  "list"
 ]
}
```


## functions/llList2Float

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list containing the element of interest.",
    "type": "list"
   }
  },
  {
   "index": {
    "tooltip": "Zero-based index of the entry.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use '[]' and 'tonumber' instead.",
  "selene-replace": [
   "tonumber(%1[%2]) or 0"
  ]
 },
 "energy": 10.0,
 "func-id": 187,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the float value at index in the list src. Returns 0.0 if the index is out of bounds or if the value cannot be type-cast.",
 "categories": [
  "data_conversion",
  "list"
 ]
}
```


## functions/llList2Integer

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list containing the element of interest.",
    "type": "list"
   }
  },
  {
   "index": {
    "tooltip": "Zero-based index of the entry.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use '[]', 'tonumber', and 'math.modf' instead.",
  "selene-replace": [
   "math.modf(tonumber(%1[%2]) or 0)"
  ]
 },
 "energy": 10.0,
 "func-id": 186,
 "native": true,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the integer value at index in the list src. Returns 0 if the index is out of bounds or if the value cannot be type-cast.",
 "categories": [
  "data_conversion",
  "list"
 ]
}
```


## functions/llList2Json

```json
{
 "arguments": [
  {
   "type": {
    "tooltip": "JSON target type (JSON_ARRAY or JSON_OBJECT).",
    "type": "string"
   }
  },
  {
   "values": {
    "tooltip": "List of values to serialize.",
    "type": "list"
   }
  }
 ],
 "slua-deprecated": {
  "use": "lljson.encode",
  "selene-replace": [
   "lljson.encode(%2)"
  ]
 },
 "energy": 10.0,
 "func-id": 514,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Converts the list values into a JSON string of the specified type (either a JSON_ARRAY or a JSON_OBJECT). Returns JSON_INVALID if an error is encountered.",
 "categories": [
  "data_conversion",
  "json",
  "list"
 ],
 "uses-enum": [
  "JSON_INVALID",
  "JSON_OBJECT",
  "JSON_ARRAY"
 ]
}
```


## functions/llList2Key

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list containing the element of interest.",
    "type": "list"
   }
  },
  {
   "index": {
    "tooltip": "Zero-based index of the entry.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use '[]' and 'touuid' instead.",
  "selene-replace": [
   "touuid(%1[%2]) or NULL_KEY"
  ]
 },
 "energy": 10.0,
 "func-id": 189,
 "native": true,
 "pure": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Returns the key (UUID) value at index in the list src. Returns a null string/key if the index is out of bounds or if the value cannot be type-cast.",
 "categories": [
  "data_conversion",
  "list"
 ]
}
```


## functions/llList2List

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "src": {
    "tooltip": "Source list to slice.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "start_index": {
    "tooltip": "Zero-based start index (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Zero-based end index (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use 'unpack' (fastcall) or 'table.move' instead. Prefer structured tables over strided lists.",
  "selene-replace": [
   "table.pack(unpack(%...))",
   "table.move(%..., 1, {})"
  ]
 },
 "energy": 10.0,
 "func-id": 192,
 "native": true,
 "pure": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a new list containing the subset of entries from src within the inclusive range specified by the start and end indices. Negative indices count backward from the end.",
 "categories": [
  "list"
 ]
}
```


## functions/llList2ListSlice

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "src": {
    "tooltip": "Source strided list.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "start_index": {
    "tooltip": "Zero-based start index (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Zero-based end index (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "stride": {
    "tooltip": "Number of entries per stride (defaults to 1 if less than 1).",
    "type": "integer"
   }
  },
  {
   "slice_index": {
    "tooltip": "Zero-based element index within each stride to extract (negatives count backward from the end of the stride).",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Prefer structured tables over strided lists."
 },
 "energy": 10.0,
 "func-id": 801,
 "must-use": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a list containing the slice_index'th element of every stride within the inclusive range from start to end in the strided list src. Stride must be a positive integer.",
 "categories": [
  "list"
 ]
}
```


## functions/llList2ListStrided

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "src": {
    "tooltip": "Source strided list.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "start_index": {
    "tooltip": "Zero-based start index (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Zero-based end index (inclusive).",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "stride": {
    "tooltip": "Number of entries per stride (defaults to 1 if less than 1).",
    "type": "integer"
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Prefer structured tables over strided lists."
 },
 "energy": 10.0,
 "func-id": 198,
 "must-use": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a new list containing the first element of every stride in the strided list src within the inclusive range from start to end.",
 "categories": [
  "list"
 ]
}
```


## functions/llList2Rot

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list containing the element of interest.",
    "type": "list"
   }
  },
  {
   "index": {
    "tooltip": "Zero-based index of the entry.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "[]",
  "selene-replace": [
   "%1[%2]"
  ]
 },
 "energy": 10.0,
 "func-id": 191,
 "native": true,
 "pure": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns the rotation value at index in the list src. Returns ZERO_ROTATION if the index is out of bounds or if the value cannot be type-cast.",
 "categories": [
  "data_conversion",
  "list"
 ]
}
```


## functions/llList2String

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list containing the element of interest.",
    "type": "list"
   }
  },
  {
   "index": {
    "tooltip": "Zero-based index of the entry.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use '[]' and 'tostring' instead.",
  "selene-replace": [
   "tostring(%1[%2])"
  ]
 },
 "energy": 10.0,
 "func-id": 188,
 "native": true,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the string value at index in the list src. Returns an empty string if the index is out of bounds.",
 "categories": [
  "data_conversion",
  "list"
 ]
}
```


## functions/llList2Vector

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source list containing the element of interest.",
    "type": "list"
   }
  },
  {
   "index": {
    "tooltip": "Zero-based index of the entry.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "[]",
  "selene-replace": [
   "%1[%2]"
  ]
 },
 "energy": 10.0,
 "func-id": 190,
 "native": true,
 "pure": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the vector value at index in the list src. Returns ZERO_VECTOR if the index is out of bounds or if the value cannot be type-cast.",
 "categories": [
  "data_conversion",
  "list"
 ]
}
```


## functions/llListFindList

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "List to search within.",
    "type": "list"
   }
  },
  {
   "test": {
    "tooltip": "List elements to search for.",
    "type": "list"
   }
  }
 ],
 "slua-deprecated": {
  "use": "table.find",
  "reason": "Prefer dictionaries or single-item searches.",
  "selene-replace": [
   "table.find(%1, %2[1])"
  ]
 },
 "energy": 10.0,
 "func-id": 201,
 "must-use": true,
 "return": "integer",
 "index-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the integer index of the first instance of list test within the list src (returns -1 if not found).",
 "categories": [
  "list"
 ]
}
```


## functions/llListFindListNext

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "List to search within.",
    "type": "list"
   }
  },
  {
   "test": {
    "tooltip": "List elements to search for.",
    "type": "list"
   }
  },
  {
   "instance": {
    "tooltip": "Zero-based occurrence index of the match to find.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "table.find",
  "reason": "Prefer dictionaries or single-item searches.",
  "selene-replace": [
   "table.find(%1, %2[1])"
  ]
 },
 "energy": 10.0,
 "func-id": 803,
 "must-use": true,
 "return": "integer",
 "index-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the integer index of the specified instance of list test within the list src (returns -1 if not found).",
 "categories": [
  "list"
 ]
}
```


## functions/llListFindStrided

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "List to search within.",
    "type": "list"
   }
  },
  {
   "test": {
    "tooltip": "List elements to search for.",
    "type": "list"
   }
  },
  {
   "start_index": {
    "tooltip": "Zero-based start index of the range to search.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Zero-based end index of the range to search.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "stride": {
    "tooltip": "Number of entries per stride in the list.",
    "type": "integer"
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Prefer dictionary lookups over strided list searches."
 },
 "energy": 10.0,
 "func-id": 800,
 "must-use": true,
 "return": "integer",
 "index-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the integer index of the first instance of list test in the strided list src within the range from start to end (stepping through by stride). Returns -1 if not found.",
 "categories": [
  "list"
 ]
}
```


## functions/llListInsertList

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "dest": {
    "tooltip": "Target destination list.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "src": {
    "tooltip": "Source list to insert.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "start": {
    "tooltip": "Zero-based index where insertion begins.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "table.insert",
  "reason": "Unnecessary table copying. Fastcall.",
  "selene-replace": [
   "table.insert(%1, %3, %2[1])",
   "table.move(%2, 1, #%2, %3, %1)"
  ]
 },
 "energy": 10.0,
 "func-id": 200,
 "native": true,
 "pure": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a new list containing all elements of dest with the elements of src inserted starting at index start. Does not modify dest itself.",
 "categories": [
  "list"
 ]
}
```


## functions/llListRandomize

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "src": {
    "tooltip": "Source list to randomize.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "stride": {
    "tooltip": "Size of each randomized block (defaults to 1 if less than 1).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 197,
 "must-use": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a randomized copy of the list src by blocks of size stride. If the list length is not perfectly divisible by stride, no randomization occurs.",
 "categories": [
  "list"
 ]
}
```


## functions/llListReplaceList

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "dest": {
    "tooltip": "Target destination list.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "src": {
    "tooltip": "Source list to insert.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "start_index": {
    "tooltip": "Zero-based start index (inclusive) of the replaced range.",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "end_index": {
    "tooltip": "Zero-based end index (inclusive) of the replaced range.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "t[n] = x",
  "reason": "Unnecessary table copying.",
  "selene-replace": [
   "%1[%3] = %2[1]"
  ]
 },
 "energy": 10.0,
 "func-id": 296,
 "native": true,
 "pure": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a copy of the list dest with the inclusive range from start to end removed, and the elements of src inserted in its place at start.",
 "categories": [
  "list"
 ]
}
```


## functions/llListSort

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "src": {
    "tooltip": "List to be sorted.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "stride": {
    "tooltip": "Number of entries per block/stride (defaults to 1 if less than 1).",
    "type": "integer"
   }
  },
  {
   "ascending": {
    "tooltip": "Boolean. If TRUE, sorts in ascending order; if FALSE, sorts in descending order.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 184,
 "must-use": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a copy of the list src, sorted into blocks of stride in ascending order (if ascending is TRUE) or descending order (if FALSE). Only works if the first entry of each block shares the same datatype.",
 "categories": [
  "list"
 ]
}
```


## functions/llListSortStrided

```json
{
 "type-arguments": [
  "T"
 ],
 "arguments": [
  {
   "src": {
    "tooltip": "List to be sorted.",
    "type": "list",
    "slua-type": "{T}"
   }
  },
  {
   "stride": {
    "tooltip": "Number of entries per block/stride (defaults to 1 if less than 1).",
    "type": "integer"
   }
  },
  {
   "stride_index": {
    "tooltip": "Zero-based index of the element within each stride to use as the sort key (negatives count backward from the end of the stride).",
    "type": "integer",
    "index-semantics": true
   }
  },
  {
   "ascending": {
    "tooltip": "Boolean. If TRUE, sorts in ascending order; if FALSE, sorts in descending order.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "slua-deprecated": {
  "use": "table.sort",
  "reason": "Prefer structured tables over strided lists."
 },
 "energy": 10.0,
 "func-id": 802,
 "must-use": true,
 "return": "list",
 "slua-return": "{T}",
 "sleep": 0.0,
 "tooltip": "Returns a copy of the list src sorted into blocks of stride by the element at stride_index in each block. Sorted in ascending order (if ascending is TRUE) or descending order (if FALSE).",
 "categories": [
  "list"
 ]
}
```


## functions/llListStatistics

```json
{
 "arguments": [
  {
   "operation": {
    "tooltip": "LIST_STAT_* constant of the statistical operation to perform.",
    "type": "integer",
    "enum-semantics": "ListStatisticsOperation"
   }
  },
  {
   "src": {
    "tooltip": "List of numbers to analyze.",
    "type": "list",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 315,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the numeric result of the statistical aggregate function operation (a LIST_STAT_* constant) on the numeric list src.",
 "categories": [
  "list",
  "math"
 ]
}
```


## functions/llListen

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "Chat channel (any 32-bit signed integer value) to listen on. Exact range is -2147483648 to 2147483647.",
    "type": "integer",
    "enum-semantics": "Channel"
   }
  },
  {
   "name": {
    "tooltip": "Specific prim name or agent legacy name to filter by (or empty string for no filter).",
    "type": "string"
   }
  },
  {
   "id": {
    "tooltip": "Specific agent or prim UUID to filter by (or NULL_KEY for no filter).",
    "type": "key"
   }
  },
  {
   "msg": {
    "tooltip": "Specific chat message string to filter by (or empty string for no filter).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 25,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Creates a listener on channel from name and id for msg. Returns an integer listener handle used to control or remove the listener. Empty strings or NULL_KEY filters do not filter on those parameters.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## functions/llListenControl

```json
{
 "arguments": [
  {
   "handle": {
    "tooltip": "Integer listener handle returned by llListen.",
    "type": "integer"
   }
  },
  {
   "active": {
    "tooltip": "Boolean. If TRUE, activates the listener; if FALSE, deactivates it.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 26,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Enables or disables the listener specified by the integer handle. If active is TRUE, the listener is activated; if FALSE, it is deactivated.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## functions/llListenRemove

```json
{
 "arguments": [
  {
   "handle": {
    "tooltip": "Integer listener handle returned by llListen to remove.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 27,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Completely removes the listener specified by the integer handle.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## functions/llLoadURL

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  },
  {
   "message": {
    "tooltip": "Text message to display in the dialog box.",
    "type": "string"
   }
  },
  {
   "url": {
    "tooltip": "Web URL to open.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 297,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Shows a dialog box displaying message to the avatar avatar offering to open the specified url. Clicking yes launches the URL in their default web browser.",
 "categories": [
  "avatar_communication",
  "user_interface",
  "web"
 ]
}
```


## functions/llLog

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Number to compute the logarithm of.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.log",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.log(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 265,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns natural (base e) logarithm of val. If negative, return 0.0.",
 "categories": [
  "math"
 ]
}
```


## functions/llLog10

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Number to compute the logarithm of.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.log10",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.log10(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 264,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns base-10 (common) logarithm of val. If negative, return 0.0.",
 "categories": [
  "math"
 ]
}
```


## functions/llLookAt

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "Target position vector in region coordinates to look at.",
    "type": "vector"
   }
  },
  {
   "strength": {
    "tooltip": "Force of rotation (0.0 cancels the tracking; values around half the object's mass are typical).",
    "type": "float"
   }
  },
  {
   "damping": {
    "tooltip": "Timescale in seconds to critically damp the orientation.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 105,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Causes the object to orient its positive Z-axis (up axis) toward the target vector, keeping its positive X-axis (forward axis) below the horizon. Tracks target until llStopLookAt is called or strength is set to 0.0.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llLoopSound

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 87,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays the attached sound looping indefinitely at the specified volume. Only one sound can be attached to a prim at a time; new loops adjust the volume of the currently playing sound without restarting it.",
 "categories": [
  "sound"
 ]
}
```


## functions/llLoopSoundMaster

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 88,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays the attached sound looping indefinitely at the specified volume and declares it a Sync Master, forcing slave sounds to synchronize with it.",
 "categories": [
  "sound"
 ]
}
```


## functions/llLoopSoundSlave

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 89,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays the attached sound looping indefinitely at the specified volume, synchronized to the most audible active Sync Master in range.",
 "categories": [
  "sound"
 ]
}
```


## functions/llMD5String

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to hash.",
    "type": "string"
   }
  },
  {
   "nonce": {
    "tooltip": "Nonce string used as a salt.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 258,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string of 32 hex characters representing the MD5 checksum of src salted with nonce (formatted as ':' + nonce).",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llMakeExplosion

```json
{
 "arguments": [
  {
   "particles": {
    "tooltip": "",
    "type": "integer"
   }
  },
  {
   "scale": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "vel": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "lifetime": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "arc": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "texture": {
    "tooltip": "Name of a texture in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).",
    "type": "vector"
   }
  }
 ],
 "deprecated": {
  "use": "ll.ParticleSystem"
 },
 "energy": 10.0,
 "func-id": 100,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Deprecated. Generates a circular explosion of particles. Use llParticleSystem instead.",
 "categories": [
  "effects"
 ]
}
```


## functions/llMakeFire

```json
{
 "arguments": [
  {
   "particles": {
    "tooltip": "",
    "type": "integer"
   }
  },
  {
   "scale": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "vel": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "lifetime": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "arc": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "texture": {
    "tooltip": "Name of a texture in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).",
    "type": "vector"
   }
  }
 ],
 "deprecated": {
  "use": "ll.ParticleSystem"
 },
 "energy": 10.0,
 "func-id": 103,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Deprecated. Generates fire-like particles. Use llParticleSystem instead.",
 "categories": [
  "effects"
 ]
}
```


## functions/llMakeFountain

```json
{
 "arguments": [
  {
   "particles": {
    "tooltip": "",
    "type": "integer"
   }
  },
  {
   "scale": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "vel": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "lifetime": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "arc": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "bounce": {
    "tooltip": "",
    "type": "integer"
   }
  },
  {
   "texture": {
    "tooltip": "Name of a texture in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).",
    "type": "vector"
   }
  },
  {
   "bounce_offset": {
    "tooltip": "",
    "type": "float"
   }
  }
 ],
 "deprecated": {
  "use": "ll.ParticleSystem"
 },
 "energy": 10.0,
 "func-id": 101,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Deprecated. Generates a fountain of particles. Use llParticleSystem instead.",
 "categories": [
  "effects"
 ]
}
```


## functions/llMakeSmoke

```json
{
 "arguments": [
  {
   "particles": {
    "tooltip": "",
    "type": "integer"
   }
  },
  {
   "scale": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "vel": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "lifetime": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "arc": {
    "tooltip": "",
    "type": "float"
   }
  },
  {
   "texture": {
    "tooltip": "Name of a texture in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).",
    "type": "vector"
   }
  }
 ],
 "deprecated": {
  "use": "ll.ParticleSystem"
 },
 "energy": 10.0,
 "func-id": 102,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Deprecated. Generates smoke-like particles. Use llParticleSystem instead.",
 "categories": [
  "effects"
 ]
}
```


## functions/llManageEstateAccess

```json
{
 "arguments": [
  {
   "action": {
    "tooltip": "An ESTATE_ACCESS_* action flag specifying the operation to perform.",
    "type": "integer",
    "enum-semantics": "EstateAccessParam"
   }
  },
  {
   "avatar": {
    "tooltip": "UUID of the avatar or group to add or remove.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 393,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Adds or removes agents from the estate's access or ban lists, or groups from the estate's group access list, specified by the action. Returns TRUE if successful, or FALSE if throttled, if the action/ID is invalid, or if the script owner lacks estate management rights.",
 "categories": [
  "land_moderation"
 ]
}
```


## functions/llMapBeacon

```json
{
 "arguments": [
  {
   "region_name": {
    "tooltip": "Name of the region where the beacon is displayed.",
    "type": "string"
   }
  },
  {
   "pos": {
    "tooltip": "Position vector in region coordinates to highlight.",
    "type": "vector"
   }
  },
  {
   "options": {
    "tooltip": "A list of options to configure the map beacon.",
    "type": "list",
    "param-semantics": "MapBeaconParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 516,
 "return": "void",
 "sleep": 1.0,
 "tooltip": "Displays an in-world beacon and optionally opens the world map for the avatar touching or wearing the object, centered on region_name with pos highlighted. Only works for attached scripts or during touch events.",
 "categories": [
  "avatar_communication",
  "user_interface"
 ]
}
```


## functions/llMapDestination

```json
{
 "arguments": [
  {
   "simname": {
    "tooltip": "Name of the target simulator region.",
    "type": "string"
   }
  },
  {
   "pos": {
    "tooltip": "Position vector in region coordinates to highlight.",
    "type": "vector"
   }
  },
  {
   "look_at": {
    "tooltip": "Position in local coordinates (currently unused/ignored).",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 309,
 "return": "void",
 "sleep": 1.0,
 "tooltip": "Opens the world map for the avatar touching or wearing the object, centered on simname with pos highlighted. Only works for attached scripts or during touch events. Note: look_at currently has no effect.",
 "categories": [
  "avatar_communication",
  "teleport",
  "user_interface"
 ]
}
```


## functions/llMessageLinked

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag controlling which prim(s) receive the message.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "num": {
    "tooltip": "An integer value passed as the second parameter of the link_message event.",
    "type": "integer"
   }
  },
  {
   "str": {
    "tooltip": "A string value passed as the third parameter of the link_message event.",
    "type": "string",
    "slua-type": "string | uuid"
   }
  },
  {
   "id": {
    "tooltip": "A key value passed as the fourth parameter of the link_message event.",
    "type": "key",
    "slua-type": "string | uuid"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 164,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Triggers a link_message event, sending num, str, and id to the scripts in the prim(s) specified by link to allow scripts within the same object to communicate.",
 "categories": [
  "script_communication"
 ]
}
```


## functions/llMinEventDelay

```json
{
 "arguments": [
  {
   "delay": {
    "tooltip": "Minimum delay duration in seconds.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 125,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the minimum delay time between events being handled (minimums and defaults vary by event type).",
 "categories": [
  "script"
 ]
}
```


## functions/llModPow

```json
{
 "arguments": [
  {
   "base": {
    "tooltip": "32-bit unsigned integer base.",
    "type": "integer"
   }
  },
  {
   "exponent": {
    "tooltip": "32-bit unsigned integer exponent.",
    "type": "integer"
   }
  },
  {
   "modulus": {
    "tooltip": "32-bit unsigned integer modulus.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 300,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns base raised to the power exponent, modulo modulus (i.e., (b^e)%m). All inputs are wrapped to unsigned 32-bit integer range [0..4294967295]. Output is wrapped to signed 32-bit integer range [-2147483648..2147483647]. Will never overflow, unlike (b^e), which can overflow to inf.",
 "categories": [
  "math"
 ]
}
```


## functions/llModifyLand

```json
{
 "arguments": [
  {
   "action": {
    "tooltip": "LAND_* action flag to perform (e.g., LAND_LEVEL, LAND_RAISE, LAND_LOWER, LAND_SMOOTH, LAND_NOISE, or LAND_REVERT).",
    "type": "integer",
    "enum-semantics": "ModifyLandAction"
   }
  },
  {
   "brush": {
    "tooltip": "Brush size (0, 1, or 2, representing 2m x 2m, 4m x 4m, or 8m x 8m).",
    "type": "integer",
    "enum-semantics": "ModifyLandBrush"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 159,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Modifies the terrain using the specified land action and brush size (0, 1, or 2, corresponding to 2m x 2m, 4m x 4m, or 8m x 8m).",
 "categories": [
  "region"
 ]
}
```


## functions/llMoveToTarget

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "Target position vector in region coordinates.",
    "type": "vector"
   }
  },
  {
   "tau": {
    "tooltip": "Timescale in seconds to critically damp the movement.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 70,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Critically damps the physical object's motion to position target in tau seconds. Setting tau to 0.0 stops the critical damping; recommended tau values are greater than 0.2.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llName2Key

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Name of the avatar (e.g., 'First Last' or 'first.last').",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 524,
 "must-use": true,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Requests the key (UUID) of the avatar name in the current region. Returns NULL_KEY if no matching agent is present. Formats are 'First Last' or 'first.last' (assumes 'Resident' if last name is omitted; case-insensitive).",
 "categories": [
  "avatar"
 ]
}
```


## functions/llNavigateTo

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Destination position vector in region coordinates.",
    "type": "vector"
   }
  },
  {
   "options": {
    "tooltip": "A list of parameters to configure pathfinding behavior (currently only FORCE_DIRECT_PATH is supported).",
    "type": "list",
    "param-semantics": "CharacterNavigateParam",
    "ruleset": "character-navigate-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 398,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Directs a pathfinding character to navigate to the position pos (located in the current or adjacent regions) using the parameters specified in options.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llOffsetTexture

```json
{
 "arguments": [
  {
   "u": {
    "tooltip": "Horizontal (U) offset, typically in the interval [-1.0, 1.0].",
    "type": "float",
    "range": [
     -1,
     1
    ]
   }
  },
  {
   "v": {
    "tooltip": "Vertical (V) offset, typically in the interval [-1.0, 1.0].",
    "type": "float",
    "range": [
     -1,
     1
    ]
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 55,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Sets the texture horizontal (u) and vertical (v) offsets for the chosen face. If face is ALL_SIDES, offsets all faces.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llOpenFloater

```json
{
 "arguments": [
  {
   "floater_name": {
    "tooltip": "Identifier string of the viewer floater to open.",
    "type": "string"
   }
  },
  {
   "url": {
    "tooltip": "URL to load within the opened floater.",
    "type": "string"
   }
  },
  {
   "params": {
    "tooltip": "Options or parameters to apply to the opened floater.",
    "type": "list"
   }
  }
 ],
 "energy": 10.0,
 "linden-experience": true,
 "func-id": 604,
 "mono-sleep": 0.2,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Opens the specified viewer floater_name loaded with url and configured via params. Returns an integer error code, or 0 if successful.",
 "categories": [
  "avatar_communication"
 ]
}
```


## functions/llOpenRemoteDataChannel

```json
{
 "arguments": [],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 254,
 "return": "void",
 "sleep": 1.0,
 "tooltip": "Deprecated. Creates a channel to listen for incoming XML-RPC calls, triggering a remote_data event with the channel ID once available.",
 "categories": [
  "script_communication"
 ]
}
```


## functions/llOrd

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Source string.",
    "type": "string"
   }
  },
  {
   "index": {
    "tooltip": "Codepoint index of the character to convert. Supports negative indexing.",
    "type": "integer",
    "index-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 527,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the ordinal (Unicode copepoint integer) of the character at index in the string val. Negative indices count backward from the end of the string.",
 "categories": [
  "string"
 ]
}
```


## functions/llOverMyLand

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the group, avatar, or object to check.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 215,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns TRUE if the avatar or object specified by key id is over land owned by the script owner, or FALSE otherwise.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llOwnerSay

```json
{
 "arguments": [
  {
   "msg": {
    "tooltip": "Text message string to send to the object owner.",
    "type": "string"
   }
  }
 ],
 "slua-deprecated": {
  "use": "print",
  "selene-replace": [
   "print(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 292,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sends the chat message msg privately to the object owner (the owner must be currently in the same region for the message to be received).",
 "categories": [
  "avatar_communication"
 ]
}
```


## functions/llParcelMediaCommandList

```json
{
 "arguments": [
  {
   "commandList": {
    "tooltip": "A list containing integer PARCEL_MEDIA_COMMAND_* flags and their corresponding parameters.",
    "type": "list",
    "param-semantics": "ParcelMediaCommand"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 298,
 "return": "void",
 "sleep": 2.0,
 "tooltip": "Controls the playback of movies and other multimedia resources on a parcel or for an agent, using the PARCEL_MEDIA_COMMAND_* settings specified in commandList.",
 "categories": [
  "media",
  "parcel",
  "parcel_media"
 ]
}
```


## functions/llParcelMediaQuery

```json
{
 "arguments": [
  {
   "query": {
    "tooltip": "A list of PARCEL_MEDIA_COMMAND_* attributes to query.",
    "type": "list",
    "param-get-semantics": "ParcelMediaQuery",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 299,
 "must-use": true,
 "return": "list",
 "param-get-semantics": "ParcelMediaQuery",
 "bool-semantics": true,
 "sleep": 2.0,
 "tooltip": "Queries the media properties of the parcel containing the script, returning a list of values in the order requested by query. Only works if the object is owned by the landowner or deeded to the land's group.",
 "categories": [
  "media",
  "parcel",
  "parcel_media"
 ]
}
```


## functions/llParseString2List

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to parse.",
    "type": "string"
   }
  },
  {
   "separators": {
    "tooltip": "A list of up to 8 strings representing separators to be discarded.",
    "type": "list",
    "slua-type": "{string}"
   }
  },
  {
   "spacers": {
    "tooltip": "A list of up to 8 strings representing spacers to be preserved in the list.",
    "type": "list",
    "slua-type": "{string}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 214,
 "pure": true,
 "return": "list",
 "slua-return": "{string}",
 "sleep": 0.0,
 "tooltip": "Breaks the string src into a list of substrings, discarding any separators, keeping spacers, and omitting any empty null values. separators and spacers accept up to 8 string entries each.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llParseStringKeepNulls

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to parse.",
    "type": "string"
   }
  },
  {
   "separators": {
    "tooltip": "A list of up to 8 strings representing separators to be discarded.",
    "type": "list",
    "slua-type": "{string}"
   }
  },
  {
   "spacers": {
    "tooltip": "A list of up to 8 strings representing spacers to be preserved in the list.",
    "type": "list",
    "slua-type": "{string}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 285,
 "pure": true,
 "return": "list",
 "slua-return": "{string}",
 "sleep": 0.0,
 "tooltip": "Breaks the string src into a list of substrings, discarding separators and keeping spacers, while preserving empty null values (unlike llParseString2List). separators and spacers accept up to 8 string entries each.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llParticleSystem

```json
{
 "arguments": [
  {
   "rules": {
    "tooltip": "A list of particle system rules and data pairs [rule1, data1, ...].",
    "type": "list",
    "param-semantics": "ParticleParam",
    "ruleset": "particle-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 229,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Creates or updates a particle system on the prim containing the script based on rules. An empty list removes the particle system.",
 "categories": [
  "effects",
  "particles"
 ]
}
```


## functions/llPassCollisions

```json
{
 "arguments": [
  {
   "pass": {
    "tooltip": "A PASS_* flag (e.g., PASS_ALWAYS, PASS_IF_NOT_HANDLED, or PASS_NEVER).",
    "type": "integer",
    "enum-semantics": "PassMode"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 166,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the pass-collisions attribute. If pass is TRUE, collision events are passed from child prims to the root; if FALSE (default), they only trigger events in the affected child prim.",
 "categories": [
  "physics",
  "sensor"
 ]
}
```


## functions/llPassTouches

```json
{
 "arguments": [
  {
   "pass": {
    "tooltip": "A PASS_* flag (e.g., PASS_ALWAYS, PASS_IF_NOT_HANDLED, or PASS_NEVER).",
    "type": "integer",
    "enum-semantics": "PassMode"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 154,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the pass-touches attribute. If pass is TRUE, touch events are passed from child prims to the root; if FALSE (default), they only trigger events in the affected child prim.",
 "categories": [
  "touch"
 ]
}
```


## functions/llPatrolPoints

```json
{
 "arguments": [
  {
   "patrolPoints": {
    "tooltip": "A list of at least two position vectors representing the patrol path.",
    "type": "list",
    "slua-type": "{vector}"
   }
  },
  {
   "options": {
    "tooltip": "A list of PATROL_* flags and parameters to configure the patrol behavior.",
    "type": "list",
    "param-semantics": "CharacterPatrolPointsParam",
    "ruleset": "character-patrol-points-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 403,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Directs a pathfinding character to patrol sequentially through the coordinates specified in patrolPoints, configured by options.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llPlaySound

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float",
    "range": [
     0,
     1
    ]
   }
  }
 ],
 "energy": 10.0,
 "func-id": 86,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays the specified sound once at volume, attached to the object. Only one sound can be attached to a prim at a time; new sounds or calling llStopSound stops previous playback. A second call with the same sound adjusts the volume without restarting it.",
 "categories": [
  "sound"
 ]
}
```


## functions/llPlaySoundSlave

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 90,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays the attached sound once at volume, synchronized to the next loop point of the most audible active Sync Master.",
 "categories": [
  "sound"
 ]
}
```


## functions/llPointAt

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector to point at.",
    "type": "vector"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 131,
 "private": true,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Directs the avatar owning the object to point at the vector pos.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llPow

```json
{
 "arguments": [
  {
   "base": {
    "tooltip": "Base number.",
    "type": "float"
   }
  },
  {
   "exponent": {
    "tooltip": "Exponent number.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "^",
  "reason": "Double precision; operator.",
  "selene-replace": [
   "%1 ^ %2",
   "math.pow(%...)",
   "math.exp(%2)"
  ]
 },
 "energy": 10.0,
 "func-id": 5,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns base raised to the power exponent. If result is imaginary, returns NaN.",
 "categories": [
  "math"
 ]
}
```


## functions/llPreloadSound

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of the sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 93,
 "return": "void",
 "sleep": 1.0,
 "tooltip": "Causes nearby viewers in range to preload the specified sound from the object's inventory to prevent playback delays.",
 "categories": [
  "sound"
 ]
}
```


## functions/llPursue

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the group, avatar, or object to pursue.",
    "type": "key"
   }
  },
  {
   "options": {
    "tooltip": "A list of options to configure pursuit behavior.",
    "type": "list",
    "param-semantics": "CharacterPursueParam",
    "ruleset": "character-pursue-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 400,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Directs a pathfinding character to pursue and chase target, configured by the parameters specified in options.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llPushObject

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the target avatar or object in the same region.",
    "type": "key"
   }
  },
  {
   "impulse": {
    "tooltip": "Linear impulse vector representing the direction and force of the push.",
    "type": "vector"
   }
  },
  {
   "ang_impulse": {
    "tooltip": "Angular impulse vector representing the rotational force.",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, forces are applied relative to the target's local axes; if FALSE, relative to region axes.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 165,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Applies physical impulse (force) and ang_impulse (rotational force) to the specified target avatar or object.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llReadKeyValue

```json
{
 "arguments": [
  {
   "k": {
    "tooltip": "Key of the key-value pair to read.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 388,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Starts an asynchronous transaction to read the value associated with key k in the experience. Returns a key query handle for the dataserver event. Fails with XP_ERROR_KEY_NOT_FOUND if the key does not exist.",
 "categories": [
  "data_storage",
  "dataserver",
  "experience",
  "experience_data"
 ]
}
```


## functions/llRefreshPrimURL

```json
{
 "arguments": [],
 "deprecated": {
  "use": "ll.SetPrimMediaParams"
 },
 "energy": 10.0,
 "func-id": 306,
 "return": "void",
 "sleep": 20.0,
 "tooltip": "Legacy function intended to reload the web page displayed on the prim's faces (currently non-functional).",
 "categories": [
  "media",
  "prim_media",
  "web"
 ]
}
```


## functions/llRegionSay

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "Chat channel (any 32-bit signed integer value except zero) to chat the message on.",
    "type": "integer",
    "enum-semantics": "ChannelNonPublic"
   }
  },
  {
   "msg": {
    "tooltip": "Text message string to broadcast.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 331,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Broadcasts the message msg to all scripts listening on channel Channel within the region. PUBLIC_CHANNEL (0) cannot be used, so, only scripts can receive the message.",
 "categories": [
  "chat",
  "script_communication"
 ]
}
```


## functions/llRegionSayTo

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the target agent or prim in the same region.",
    "type": "key"
   }
  },
  {
   "channel": {
    "tooltip": "Chat channel (any 32-bit signed integer value) to chat the message on.",
    "type": "integer"
   }
  },
  {
   "msg": {
    "tooltip": "Text message string to send.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 364,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sends the message msg on Channel privately to the targeted agent or object (if within the region). If target is an agent and channel is non-zero, the message can also be heard by any attachments worn by the avatar.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## functions/llReleaseCamera

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "deprecated": {
  "use": "ll.ClearCameraParams",
  "selene-replace": [
   "ll.ClearCameraParams()"
  ]
 },
 "energy": 10.0,
 "func-id": 116,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Deprecated. Intended to return camera control back to the avatar (use llClearCameraParams instead).",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llReleaseControls

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 112,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops taking inputs (previously acquired via llTakeControls) from the avatar, dequeuing any remaining control events and revoking the PERMISSION_TAKE_CONTROLS permission.",
 "categories": [
  "avatar",
  "input",
  "permissions"
 ]
}
```


## functions/llReleaseURL

```json
{
 "arguments": [
  {
   "url": {
    "tooltip": "URL string to release.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 347,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Releases the specified url (previously obtained via llRequestURL), rendering it no longer usable.",
 "categories": [
  "media",
  "web"
 ]
}
```


## functions/llRemoteDataReply

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "XML-RPC channel ID.",
    "type": "key"
   }
  },
  {
   "message_id": {
    "tooltip": "XML-RPC message ID.",
    "type": "key"
   }
  },
  {
   "sdata": {
    "tooltip": "String payload data to reply with.",
    "type": "string"
   }
  },
  {
   "idata": {
    "tooltip": "Integer payload data to reply with.",
    "type": "integer"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 256,
 "return": "void",
 "sleep": 3.0,
 "tooltip": "Deprecated. Sends an XML-RPC reply on channel to message_id with payload string sdata and integer idata.",
 "categories": [
  "script_communication"
 ]
}
```


## functions/llRemoteDataSetRegion

```json
{
 "arguments": [],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 263,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Deprecated. Used with XML-RPC to reregister remote data channels if the object moves to another region.",
 "categories": [
  "script_communication"
 ]
}
```


## functions/llRemoteLoadScript

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the target prim.",
    "type": "key"
   }
  },
  {
   "script": {
    "tooltip": "Name of the script in the prim's inventory.",
    "type": "string"
   }
  },
  {
   "running": {
    "tooltip": "Boolean. If TRUE, sets the copied script to run immediately; if FALSE, leaves it stopped.",
    "type": "integer"
   }
  },
  {
   "start_param": {
    "tooltip": "Integer start parameter passed to the copied script (readable via llGetStartParameter).",
    "type": "integer"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 251,
 "private": true,
 "return": "void",
 "sleep": 3.0,
 "tooltip": "Deprecated.",
 "categories": [
  "prim_inventory",
  "script"
 ]
}
```


## functions/llRemoteLoadScriptPin

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "UUID of the target prim in the same region.",
    "type": "key"
   }
  },
  {
   "script": {
    "tooltip": "Name of the script in the prim's inventory.",
    "type": "string"
   }
  },
  {
   "pin": {
    "tooltip": "Integer PIN code (must match the PIN set on the ObjectID via llSetRemoteScriptAccessPin).",
    "type": "integer"
   }
  },
  {
   "running": {
    "tooltip": "Boolean. If TRUE, sets the copied script to run immediately; if FALSE, leaves it stopped.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "start_param": {
    "tooltip": "Integer start parameter passed to the copied script (readable via llGetStartParameter).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 253,
 "return": "void",
 "sleep": 3.0,
 "tooltip": "Copies the script into target, setting it running (if running is TRUE) with the start_param, provided the script owner has modify permissions on target and target's PIN matches pin (set via llSetRemoteScriptAccessPin).",
 "categories": [
  "prim",
  "prim_inventory",
  "script"
 ]
}
```


## functions/llRemoveFromLandBanList

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar to remove.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 312,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Removes the specified avatar from the land parcel's ban list.",
 "categories": [
  "land_moderation",
  "parcel"
 ]
}
```


## functions/llRemoveFromLandPassList

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar to remove.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 311,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Removes the specified avatar from the land parcel's pass/access list.",
 "categories": [
  "land_moderation",
  "parcel"
 ]
}
```


## functions/llRemoveInventory

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory to remove.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 151,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Permanently deletes the named inventory item from the prim's inventory.",
 "categories": [
  "prim_inventory"
 ]
}
```


## functions/llRemoveVehicleFlags

```json
{
 "arguments": [
  {
   "flags": {
    "tooltip": "A bitwise mask of VEHICLE_FLAG_* constants to disable.",
    "type": "integer",
    "enum-semantics": "VehicleFlag"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 237,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Disables the specified vehicle flags (sets them to FALSE) using the bitwise mask flags.",
 "categories": [
  "physics",
  "vehicles"
 ]
}
```


## functions/llReplaceAgentEnvironment

```json
{
 "arguments": [
  {
   "agent_id": {
    "tooltip": "UUID of an agent in the region participating in the experience.",
    "type": "key"
   }
  },
  {
   "transition": {
    "tooltip": "Duration in seconds over which to transition to the new environment.",
    "type": "float"
   }
  },
  {
   "environment": {
    "tooltip": "Name of an environmental setting in inventory, or its asset UUID (or empty string/NULL_KEY to clear).",
    "type": "string",
    "asset-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 713,
 "return": "integer",
 "enum-semantics": "EnvironmentError",
 "sleep": 0.0,
 "tooltip": "Replaces the region and parcel environment seen by the specified agent_id as part of an experience, transitioning the settings over transition seconds. Passing NULL_KEY or an empty string for environment restores defaults.",
 "categories": [
  "avatar",
  "experience",
  "parcel_appearance",
  "region_appearance"
 ]
}
```


## functions/llReplaceEnvironment

```json
{
 "arguments": [
  {
   "position": {
    "tooltip": "Position vector of the target parcel (the Z component is ignored; use <-1.0, -1.0, -1.0> for the entire region).",
    "type": "vector"
   }
  },
  {
   "environment": {
    "tooltip": "Name of an environmental setting in inventory, or its asset UUID (or empty string/NULL_KEY to clear).",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "track_no": {
    "tooltip": "The elevation track to change (0: water, 1: ground, 2: 1000m, 3: 2000m, 4: 3000m, -1: all tracks).",
    "type": "integer"
   }
  },
  {
   "day_length": {
    "tooltip": "Day cycle length in seconds (-1 to leave unchanged).",
    "type": "integer"
   }
  },
  {
   "day_offset": {
    "tooltip": "Day cycle offset in seconds from UTC (-1 to leave unchanged).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 718,
 "return": "integer",
 "enum-semantics": "EnvironmentError",
 "sleep": 0.0,
 "tooltip": "Replaces the environment on the parcel containing position (or the entire region if position is <-1.0, -1.0, -1.0>) for the specified track_no. Modifies day_length and day_offset if specified. Requires edit permissions on the parcel or estate management rights.",
 "categories": [
  "parcel",
  "parcel_appearance"
 ]
}
```


## functions/llReplaceSubString

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Original source string to search.",
    "type": "string"
   }
  },
  {
   "pattern": {
    "tooltip": "Substring pattern to find and replace.",
    "type": "string"
   }
  },
  {
   "replacement_pattern": {
    "tooltip": "New substring that replaces the pattern.",
    "type": "string"
   }
  },
  {
   "count": {
    "tooltip": "Maximum number of replacements to make (0 for all, positive for left-to-right, negative for right-to-left).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 541,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a copy of src with count occurrences of pattern replaced by replacement_pattern. Setting count to 0 replaces all occurrences; positive counts process left-to-right, while negative counts process right-to-left.",
 "categories": [
  "string"
 ]
}
```


## functions/llRequestAgentData

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the agent.",
    "type": "key"
   }
  },
  {
   "data": {
    "tooltip": "DATA_* category flag of the requested information.",
    "type": "integer",
    "enum-semantics": "AgentData"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 155,
 "return": "key",
 "sleep": 0.1,
 "tooltip": "Asynchronously requests the specified data category (DATA_*) about the agent id. Triggers a dataserver event with the results and returns a key query handle.",
 "categories": [
  "avatar",
  "dataserver"
 ]
}
```


## functions/llRequestDisplayName

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar to query.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 361,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Asynchronously requests the display name of the agent specified by id, triggering a dataserver event with the results. The agent does not need to be online or in the region. Returns a key query handle.",
 "categories": [
  "avatar",
  "dataserver"
 ]
}
```


## functions/llRequestExperiencePermissions

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the agent to request permissions from.",
    "type": "key"
   }
  },
  {
   "name": {
    "tooltip": "Deprecated parameter (no longer used).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 384,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Requests permission from the specified agent to participate in the experience. These permissions are persistent and apply grid-wide across all scripts in the experience, automatically triggering experience_permissions or experience_permissions_denied.",
 "categories": [
  "avatar",
  "experience",
  "permissions"
 ]
}
```


## functions/llRequestInventoryData

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 156,
 "return": "key",
 "sleep": 1.0,
 "tooltip": "Asynchronously requests data for the named inventory item, triggering a dataserver event. Currently, only landmark items are supported (which return local region coordinates). Returns a key query handle.",
 "categories": [
  "dataserver",
  "prim_inventory"
 ]
}
```


## functions/llRequestPermissions

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the agent in the same region.",
    "type": "key"
   }
  },
  {
   "permissions": {
    "tooltip": "Bitfield containing the PERMISSION_* constants to request.",
    "type": "integer",
    "enum-semantics": "ScriptPermission"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 136,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Requests permissions (a bitfield specified by permissions) from the agent in the same region, calling run_time_permissions if granted. This call does not pause script execution.",
 "categories": [
  "permissions"
 ]
}
```


## functions/llRequestSecureURL

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 346,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Asynchronously requests one secure HTTPS (SSL, port 12043) URL for use by this object, triggering an http_request event. Returns a key query handle.",
 "categories": [
  "media",
  "script_communication",
  "web"
 ]
}
```


## functions/llRequestSimulatorData

```json
{
 "arguments": [
  {
   "region": {
    "tooltip": "Case-sensitive region name.",
    "type": "string"
   }
  },
  {
   "data": {
    "tooltip": "DATA_SIM_* flag of the requested simulator data.",
    "type": "integer",
    "enum-semantics": "SimulatorData"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 293,
 "return": "key",
 "sleep": 1.0,
 "tooltip": "Asynchronously requests data (using a DATA_SIM_* constant) about the region. Triggers a dataserver event and returns a key query handle.",
 "categories": [
  "dataserver",
  "region"
 ]
}
```


## functions/llRequestURL

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 345,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Asynchronously requests one HTTP URL for use by this script, triggering an http_request event. Returns a key query handle.",
 "categories": [
  "media",
  "script_communication",
  "web"
 ]
}
```


## functions/llRequestUserKey

```json
{
 "arguments": [
  {
   "username": {
    "tooltip": "Current or historical username of the avatar to resolve.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 525,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Asynchronously requests the Agent ID key (UUID) for the agent specified by their current or historical username, returning NULL_KEY if not found. Returns a key query handle for the dataserver event.",
 "categories": [
  "avatar",
  "dataserver",
  "uuid"
 ]
}
```


## functions/llRequestUsername

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar to query.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 359,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Asynchronously requests the unique single-word username of the agent identified by id, triggering a dataserver event. The agent does not need to be online or in the region. Returns a key query handle.",
 "categories": [
  "avatar",
  "dataserver"
 ]
}
```


## functions/llResetAnimationOverride

```json
{
 "arguments": [
  {
   "anim_state": {
    "tooltip": "Animation state string (or 'ALL') to reset.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 502,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_OVERRIDE_ANIMATIONS"
 ],
 "tooltip": "Resets the animation override for anim_state to its default value (use 'ALL' to reset all states). Requires the PERMISSION_OVERRIDE_ANIMATIONS permission.",
 "categories": [
  "avatar_animation",
  "permissions"
 ]
}
```


## functions/llResetLandBanList

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 321,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Removes all blocked residents from the land parcel's ban list.",
 "categories": [
  "land_moderation",
  "parcel"
 ]
}
```


## functions/llResetLandPassList

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 322,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Removes all residents from the land parcel's access/pass list.",
 "categories": [
  "land_moderation",
  "parcel"
 ]
}
```


## functions/llResetOtherScript

```json
{
 "arguments": [
  {
   "script": {
    "tooltip": "Name of the target script in the prim's inventory.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 249,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Resets the named script name in the prim's inventory.",
 "categories": [
  "prim_inventory",
  "script"
 ]
}
```


## functions/llResetScript

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 163,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Resets the current script.",
 "categories": [
  "script"
 ]
}
```


## functions/llResetTime

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 83,
 "return": "void",
 "slua-removed": true,
 "sleep": 0.0,
 "tooltip": "Resets the script's elapsed time timer back to zero.",
 "categories": [
  "script"
 ]
}
```


## functions/llReturnObjectsByID

```json
{
 "arguments": [
  {
   "objects": {
    "tooltip": "A list of object UUID keys to return.",
    "type": "list",
    "slua-type": "{uuid}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 520,
 "return": "integer",
 "enum-semantics": "ReturnObjectsError",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_RETURN_OBJECTS"
 ],
 "tooltip": "Returns objects specified by the list of UUIDs objects to their owners. Requires the PERMISSION_RETURN_OBJECTS permission, and the script owner must own the parcel or be an estate manager/region owner.",
 "categories": [
  "land_moderation",
  "rez"
 ]
}
```


## functions/llReturnObjectsByOwner

```json
{
 "arguments": [
  {
   "owner": {
    "tooltip": "UUID of the avatar or group whose objects will be returned.",
    "type": "key"
   }
  },
  {
   "scope": {
    "tooltip": "OBJECT_RETURN_* scope flag (such as OBJECT_RETURN_PARCEL, OBJECT_RETURN_PARCEL_OWNER, or OBJECT_RETURN_REGION).",
    "type": "integer",
    "enum-semantics": "ReturnObjectsScope"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 521,
 "return": "integer",
 "enum-semantics": "ReturnObjectsError",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_RETURN_OBJECTS"
 ],
 "tooltip": "Returns objects owned by owner within the specified scope (parcel, parcel owner, or region). Requires the PERMISSION_RETURN_OBJECTS permission, and the script owner must own the parcel or be an estate manager/region owner.",
 "categories": [
  "land_moderation",
  "rez"
 ]
}
```


## functions/llRezAtRoot

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the object in the prim's inventory to rez.",
    "type": "string"
   }
  },
  {
   "pos": {
    "tooltip": "Position vector in region coordinates where the root of the object will be placed.",
    "type": "vector"
   }
  },
  {
   "vel": {
    "tooltip": "Initial velocity vector for the rezzed object.",
    "type": "vector"
   }
  },
  {
   "rot": {
    "tooltip": "Initial rotation of the rezzed object.",
    "type": "rotation"
   }
  },
  {
   "start_param": {
    "tooltip": "Start parameter passed to the rezzed object's on_rez event (accessible via llGetStartParameter).",
    "type": "integer"
   }
  }
 ],
 "energy": 200.0,
 "func-id": 286,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Instantiates the named inventory object with the root prim at pos with velocity vel and rotation rot, passing start_param as the on_rez start parameter. The vel parameter is ignored if the rezzed object is non-physical.",
 "categories": [
  "prim_inventory",
  "rez"
 ]
}
```


## functions/llRezObject

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the object in the prim's inventory to rez.",
    "type": "string"
   }
  },
  {
   "pos": {
    "tooltip": "Position vector in region coordinates where the center of the object will be placed.",
    "type": "vector"
   }
  },
  {
   "vel": {
    "tooltip": "Initial velocity vector (maximum magnitude ~200m/s).",
    "type": "vector"
   }
  },
  {
   "rot": {
    "tooltip": "Initial rotation of the rezzed object.",
    "type": "rotation"
   }
  },
  {
   "start_param": {
    "tooltip": "Start parameter passed to the rezzed object's on_rez event (accessible via llGetStartParameter).",
    "type": "integer"
   }
  }
 ],
 "energy": 200.0,
 "func-id": 104,
 "return": "void",
 "sleep": 0.1,
 "tooltip": "Instantiates the named inventory object with the bounding box centered at pos with velocity vel and rotation rot, passing param as the on_rez start parameter. The vel parameter is ignored if the rezzed object is non-physical.",
 "categories": [
  "prim_inventory",
  "rez"
 ]
}
```


## functions/llRezObjectWithParams

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the object in the prim's inventory to rez.",
    "type": "string"
   }
  },
  {
   "options": {
    "tooltip": "A list of REZ_* options to configure the rezzed object's attributes.",
    "type": "list",
    "param-semantics": "RezParam"
   }
  }
 ],
 "energy": 200.0,
 "func-id": 544,
 "return": "key",
 "sleep": 0.1,
 "tooltip": "Instantiates the named inventory object (defaulting to the rezzing prim's position unless REZ_POS is specified) using the initial set of parameters specified in options. Returns the key of the rezzed object, or a blank key on failure.",
 "categories": [
  "combat",
  "prim_inventory",
  "rez"
 ]
}
```


## functions/llRot2Angle

```json
{
 "arguments": [
  {
   "q": {
    "tooltip": "Rotation to evaluate.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 171,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the angle, in radians, that q rotates.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion"
 ]
}
```


## functions/llRot2Axis

```json
{
 "arguments": [
  {
   "q": {
    "tooltip": "Rotation to evaluate.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 170,
 "pure": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the unit vector axis that q rotates around.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion",
  "vector"
 ]
}
```


## functions/llRot2Euler

```json
{
 "arguments": [
  {
   "q": {
    "tooltip": "Rotation to convert.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 15,
 "pure": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector of Euler angles (roll, pitch, yaw) of q. The angles will be in radians.",
 "categories": [
  "math",
  "math_3d",
  "quaternion"
 ]
}
```


## functions/llRot2Fwd

```json
{
 "arguments": [
  {
   "q": {
    "tooltip": "Rotation to convert.",
    "type": "rotation"
   }
  }
 ],
 "slua-deprecated": {
  "use": "quaternion.tofwd",
  "selene-replace": [
   "quaternion.tofwd(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 18,
 "pure": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the unit vector pointing toward positive X (forward) in the coordinate space of rotation q. Equivalent to <1, 0, 0> * q.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion",
  "vector"
 ]
}
```


## functions/llRot2Left

```json
{
 "arguments": [
  {
   "q": {
    "tooltip": "Rotation to convert.",
    "type": "rotation"
   }
  }
 ],
 "slua-deprecated": {
  "use": "quaternion.toleft",
  "selene-replace": [
   "quaternion.toleft(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 19,
 "pure": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the unit vector pointing toward positive Y (left) in the coordinate space of rotation q. Equivalent to <0, 1, 0> * q.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion",
  "vector"
 ]
}
```


## functions/llRot2Up

```json
{
 "arguments": [
  {
   "q": {
    "tooltip": "Rotation to convert.",
    "type": "rotation"
   }
  }
 ],
 "slua-deprecated": {
  "use": "quaternion.toup",
  "selene-replace": [
   "quaternion.toup(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 20,
 "pure": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the unit vector pointing toward positive Z (up) in the coordinate space of rotation q. Equivalent to <0, 0, 1> * q.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion",
  "vector"
 ]
}
```


## functions/llRotBetween

```json
{
 "arguments": [
  {
   "start_vec": {
    "tooltip": "Starting vector.",
    "type": "vector"
   }
  },
  {
   "end_vec": {
    "tooltip": "Ending vector.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 21,
 "pure": true,
 "return": "rotation",
 "sleep": 0.0,
 "tooltip": "Returns the shortest-path quaternion that rotates start_vec onto end_vec.",
 "categories": [
  "math",
  "math_3d",
  "math_trig",
  "quaternion"
 ]
}
```


## functions/llRotLookAt

```json
{
 "arguments": [
  {
   "target_direction": {
    "tooltip": "Target rotation to align the object with.",
    "type": "rotation"
   }
  },
  {
   "strength": {
    "tooltip": "Force of rotation (0.0 cancels the tracking; values around half the object's mass are typical).",
    "type": "float"
   }
  },
  {
   "damping": {
    "tooltip": "Timescale in seconds to critically damp the rotation.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 127,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Causes the object to smoothly rotate to target_direction with a force defined by strength and damping. A strength of 0.0 cancels the rotation target. Rotation is maintained until stopped with llStopLookAt.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llRotTarget

```json
{
 "arguments": [
  {
   "rot": {
    "tooltip": "Target rotation to track.",
    "type": "rotation"
   }
  },
  {
   "error": {
    "tooltip": "Tolerance angle in radians defining when the target rotation is considered reached.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 68,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Registers the rotation rot with a leeway tolerance error (in radians) as a target, triggering at_rot_target and not_at_rot_target events. Returns an integer handle to unregister the target via llRotTargetRemove.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llRotTargetRemove

```json
{
 "arguments": [
  {
   "handle": {
    "tooltip": "Integer target handle returned by llRotTarget to remove.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 69,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Removes the rotational target specified by the integer handle registered with llRotTarget.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llRotateTexture

```json
{
 "arguments": [
  {
   "angle": {
    "tooltip": "Rotation angle expressed in radians.",
    "type": "float"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 56,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Sets the texture rotation of face to the specified angle (in radians). If face is ALL_SIDES, rotates the texture on all faces.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llRound

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Number to round.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.round",
  "reason": "Fastcall.",
  "selene-replace": [
   "math.round(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 11,
 "must-use": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns val rounded to the nearest integer. Halfway values are rounded toward infinity.",
 "categories": [
  "math"
 ]
}
```


## functions/llSHA1String

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to hash.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 343,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string of 40 hex characters representing the SHA-1 security hash of src.",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llSHA256String

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to hash.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 531,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string of 64 hex characters representing the SHA-256 security hash of src.",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llSameGroup

```json
{
 "arguments": [
  {
   "uuid": {
    "tooltip": "UUID of the group, avatar, or prim to check.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 219,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns TRUE if the agent or object specified by uuid is in the same region (simulator) and shares the same active group as the prim containing the script; returns FALSE otherwise.",
 "categories": [
  "object"
 ]
}
```


## functions/llSay

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "Chat channel (any 32-bit signed integer value) to chat the message on.",
    "type": "integer",
    "enum-semantics": "Channel"
   }
  },
  {
   "msg": {
    "tooltip": "Text message string to broadcast.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 23,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv(\"chat_range\"), which is 20m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## functions/llScaleByFactor

```json
{
 "arguments": [
  {
   "scaling_factor": {
    "tooltip": "Multiplier scale factor to apply to the prim sizes and their local positions.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 592,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Attempts to uniformly resize the entire object by scaling_factor, maintaining size-position ratios of the prims. Fails if the linkset is physical, a pathfinding character, in keyframed motion, would exceed prim scale/linkability limits, or would overflow parcel capacity.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llScaleTexture

```json
{
 "arguments": [
  {
   "u": {
    "tooltip": "Horizontal (U) texture repeats scale value, in the interval [-100.0, 100.0].",
    "type": "float",
    "range": [
     -100,
     100
    ]
   }
  },
  {
   "v": {
    "tooltip": "Vertical (V) texture repeats scale value, in the interval [-100.0, 100.0].",
    "type": "float",
    "range": [
     -100,
     100
    ]
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 54,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Sets the diffuse texture horizontal u and vertical v scales (repeats) on the specified face of the prim. Setting face to ALL_SIDES updates all sides. Negative scale values flip the texture.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llScriptDanger

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector in region coordinates to check.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 246,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns TRUE if the vector position pos is over public land, sandbox land, land restricting edit/build permissions, or land that disables outside scripts.",
 "categories": [
  "parcel",
  "script"
 ]
}
```


## functions/llScriptProfiler

```json
{
 "arguments": [
  {
   "flags": {
    "tooltip": "PROFILE_* flag (such as PROFILE_NONE or PROFILE_SCRIPT_MEMORY) to set the profiling state.",
    "type": "integer",
    "enum-semantics": "ScriptProfileMode"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 367,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Enables or disables the script's profiling state using flags (supports PROFILE_SCRIPT_MEMORY on Mono, or PROFILE_NONE). Active profiling can significantly reduce script performance.",
 "categories": [
  "script"
 ]
}
```


## functions/llSendRemoteData

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "XML-RPC channel ID.",
    "type": "key"
   }
  },
  {
   "dest": {
    "tooltip": "Destination XML-RPC URL or server.",
    "type": "string"
   }
  },
  {
   "idata": {
    "tooltip": "Integer payload data.",
    "type": "integer"
   }
  },
  {
   "sdata": {
    "tooltip": "String payload data.",
    "type": "string"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 255,
 "return": "key",
 "sleep": 3.0,
 "tooltip": "Deprecated. Sends an XML-RPC request to dest on channel, containing the channel ID as a string, integer idata, and string sdata. Returns a key representing the message_id.",
 "categories": [
  "script_communication"
 ]
}
```


## functions/llSensor

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Specific object or avatar name to filter for (or empty string for no filter).",
    "type": "string"
   }
  },
  {
   "id": {
    "tooltip": "UUID of the group, avatar, or object to filter by (or NULL_KEY for no filter).",
    "type": "key"
   }
  },
  {
   "type": {
    "tooltip": "Integer bitfield type mask containing AGENT, AGENT_BY_LEGACY_NAME, AGENT_BY_USERNAME, ACTIVE, PASSIVE, or SCRIPTED (0 for no filter).",
    "type": "integer",
    "enum-semantics": "DetectType"
   }
  },
  {
   "radius": {
    "tooltip": "Maximum distance in meters to scan (range [0.0, 96.0]).",
    "type": "float",
    "range": [
     0,
     96
    ]
   }
  },
  {
   "arc": {
    "tooltip": "Maximum angle in radians relative to the local X-axis to scan (range [0.0, PI]).",
    "type": "float",
    "range": [
     0,
     3.141592
    ]
   }
  }
 ],
 "energy": 10.0,
 "func-id": 28,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Performs a single scan from the prim's forward vector for name and id of type within radius meters and arc radians. Results trigger a sensor or no_sensor event. Passing empty filters (blank name, 0 type, or NULL_KEY id) disables that filter.",
 "categories": [
  "sensor"
 ],
 "uses-enum": [
  "PI_BY_TWO",
  "PI"
 ]
}
```


## functions/llSensorRemove

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 30,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Removes the periodic sensor previously configured by llSensorRepeat.",
 "categories": [
  "sensor"
 ]
}
```


## functions/llSensorRepeat

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "Specific object or avatar name to filter for (or empty string for no filter).",
    "type": "string"
   }
  },
  {
   "id": {
    "tooltip": "UUID of the group, avatar, or object to filter by (or NULL_KEY for no filter).",
    "type": "key"
   }
  },
  {
   "type": {
    "tooltip": "Integer bitfield type mask containing AGENT, AGENT_BY_LEGACY_NAME, AGENT_BY_USERNAME, ACTIVE, PASSIVE, or SCRIPTED (0 for no filter).",
    "type": "integer",
    "enum-semantics": "DetectType"
   }
  },
  {
   "radius": {
    "tooltip": "Maximum distance in meters to scan (range [0.0, 96.0]).",
    "type": "float",
    "range": [
     0,
     96
    ]
   }
  },
  {
   "arc": {
    "tooltip": "Maximum angle in radians relative to the local X-axis to scan (range [0.0, PI]).",
    "type": "float",
    "range": [
     0,
     3.141592
    ]
   }
  },
  {
   "rate": {
    "tooltip": "Interval in seconds between repeated scans.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 29,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets up a repeating periodic scan every rate seconds for name and id of type within radius meters and arc radians of the forward vector. Results trigger sensor or no_sensor events.",
 "categories": [
  "sensor"
 ],
 "uses-enum": [
  "PI_BY_TWO",
  "PI"
 ]
}
```


## functions/llSetAgentEnvironment

```json
{
 "arguments": [
  {
   "agent_id": {
    "tooltip": "UUID of the agent participating in the experience.",
    "type": "key"
   }
  },
  {
   "transition": {
    "tooltip": "Transition duration in seconds.",
    "type": "float"
   }
  },
  {
   "params": {
    "tooltip": "A list of environmental parameters to apply.",
    "type": "list",
    "param-semantics": "EnvironmentParam"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 714,
 "return": "integer",
 "enum-semantics": "EnvironmentError",
 "sleep": 0.0,
 "tooltip": "Sets an individual agent's environmental settings using the attributes in params over a duration of transition seconds. Must be used as part of an experience; passing an empty list removes overrides.",
 "categories": [
  "avatar",
  "experience",
  "parcel_appearance",
  "region_appearance"
 ]
}
```


## functions/llSetAgentRot

```json
{
 "arguments": [
  {
   "rot": {
    "tooltip": "Target rotation to turn the avatar to face.",
    "type": "rotation"
   }
  },
  {
   "flags": {
    "tooltip": "Flags to configure the rotation behavior.",
    "type": "integer",
    "enum-semantics": "AgentRotFlags"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 515,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the rotation of the avatar to rot, controlled by flags.",
 "categories": [
  "avatar",
  "movement",
  "physics"
 ]
}
```


## functions/llSetAlpha

```json
{
 "arguments": [
  {
   "alpha": {
    "tooltip": "Transparency value to set, from 0.0 (clear) to 1.0 (solid; clamped to a minimum of 0.1).",
    "type": "float"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 51,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the diffuse texture alpha (opacity) of face. If face is ALL_SIDES, applies to all faces. Values are clamped between 0.1 and 1.0 (where 1.0 is fully opaque).",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llSetAngularVelocity

```json
{
 "arguments": [
  {
   "initial_omega": {
    "tooltip": "Angular velocity vector to apply (in radians per second).",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, initial_omega is treated as a local vector; if FALSE, as a global region vector.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 379,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the angular velocity of a physical object to initial_omega (mass-independent). If local is TRUE, applied in local coordinates; if FALSE, applied in global coordinates. Has no effect on non-physical objects.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llSetAnimationOverride

```json
{
 "arguments": [
  {
   "anim_state": {
    "tooltip": "Animation state to override.",
    "type": "string"
   }
  },
  {
   "anim": {
    "tooltip": "Name of an animation in the prim's inventory, or a built-in animation name.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 501,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_OVERRIDE_ANIMATIONS"
 ],
 "tooltip": "Overrides the default animation for anim_state with anim (which must be in the object's inventory or a built-in animation). Requires the PERMISSION_OVERRIDE_ANIMATIONS permission.",
 "categories": [
  "avatar_animation",
  "permissions"
 ]
}
```


## functions/llSetBuoyancy

```json
{
 "arguments": [
  {
   "buoyancy": {
    "tooltip": "Float buoyancy value to set.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 122,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the buoyancy of a physical object (requires physics to be enabled). A value of 0.0 offers no buoyancy, < 1.0 sinks, 1.0 counteracts gravity, and > 1.0 rises.",
 "categories": [
  "physics"
 ]
}
```


## functions/llSetCameraAtOffset

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset position vector in local coordinates relative to the prim.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 244,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the target offset vector (in local coordinates) that a seated avatar's camera will look at.",
 "categories": [
  "camera"
 ]
}
```


## functions/llSetCameraEyeOffset

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset position vector in local coordinates relative to the prim.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 243,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the eye offset vector (in local coordinates) where a seated avatar's camera is positioned.",
 "categories": [
  "camera"
 ]
}
```


## functions/llSetCameraParams

```json
{
 "arguments": [
  {
   "rules": {
    "tooltip": "A strided list of rules and data pairs configuring the camera.",
    "type": "list",
    "param-semantics": "CameraParam",
    "ruleset": "camera-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 313,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_CONTROL_CAMERA"
 ],
 "tooltip": "Sets multiple camera parameters simultaneously using the list of rules. Requires the PERMISSION_CONTROL_CAMERA runtime permission.",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llSetClickAction

```json
{
 "arguments": [
  {
   "action": {
    "tooltip": "CLICK_ACTION_* flag representing the action to apply.",
    "type": "integer",
    "enum-semantics": "ClickAction"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 333,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the action (a CLICK_ACTION_* flag) performed when an avatar left-clicks the prim.",
 "categories": [
  "input",
  "money",
  "prim_properties",
  "touch",
  "user_interface"
 ]
}
```


## functions/llSetColor

```json
{
 "arguments": [
  {
   "color": {
    "tooltip": "Color vector in RGB <R, G, B> (values from 0.0 to 1.0).",
    "type": "vector"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 49,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the Blinn-Phong diffuse RGB color of face. If face is ALL_SIDES, applies the color to all faces.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llSetContentType

```json
{
 "arguments": [
  {
   "request_id": {
    "tooltip": "Unique key identifying the incoming HTTP request.",
    "type": "key"
   }
  },
  {
   "content_type": {
    "tooltip": "CONTENT_TYPE_* constant representing the Internet media type to use.",
    "type": "integer",
    "enum-semantics": "HTTPContentType"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 374,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the 'Content-Type' header of subsequent HTTP server responses (via llHTTPResponse) for request_id using the specified content_type (a CONTENT_TYPE_* constant).",
 "categories": [
  "media",
  "prim_media",
  "web"
 ]
}
```


## functions/llSetDamage

```json
{
 "arguments": [
  {
   "damage": {
    "tooltip": "Float damage value to set (range -100.0 for full heal to 100.0 for instant kill).",
    "type": "float",
    "range": [
     -100,
     100
    ]
   }
  }
 ],
 "energy": 10.0,
 "func-id": 157,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the amount of damage delivered when this object hits an avatar. The object is immediately destroyed upon inflicting damage, and no collision event is triggered.",
 "categories": [
  "combat"
 ]
}
```


## functions/llSetEnvironment

```json
{
 "arguments": [
  {
   "position": {
    "tooltip": "Position vector in region coordinates to specify the target parcel, or <-1.0, -1.0, z> for the entire region (where z specifies the sky track, or -1 for all tracks).",
    "type": "vector"
   }
  },
  {
   "params": {
    "tooltip": "A list of environmental attributes and values to apply (or empty to clear).",
    "type": "list",
    "param-semantics": "EnvironmentParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 717,
 "return": "integer",
 "enum-semantics": "EnvironmentError",
 "sleep": 0.0,
 "tooltip": "Overrides the environmental settings at position for a parcel (or region if position is <-1.0, -1.0, z>) using the parameters in params. Passing an empty params list removes previous overrides.",
 "categories": [
  "parcel",
  "parcel_appearance"
 ]
}
```


## functions/llSetExperienceKey

```json
{
 "arguments": [
  {
   "experienceid": {
    "tooltip": "",
    "type": "key"
   }
  }
 ],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 386,
 "private": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "",
 "categories": [
  "experience"
 ]
}
```


## functions/llSetForce

```json
{
 "arguments": [
  {
   "force": {
    "tooltip": "Directional force vector to apply.",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, force is treated as a local vector; if FALSE, as a global region vector.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 64,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Applies a constant linear force to a physical object. If local is TRUE, force is applied relative to local coordinates; if FALSE, applied relative to region coordinates.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llSetForceAndTorque

```json
{
 "arguments": [
  {
   "force": {
    "tooltip": "Directional linear force vector.",
    "type": "vector"
   }
  },
  {
   "torque": {
    "tooltip": "Torque rotational force vector.",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, force and torque are treated as local vectors; if FALSE, as global region vectors.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 76,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets both the constant linear force and constant torque acting on a physical object. If local is TRUE, forces are applied in local coordinates; if FALSE, in global coordinates.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llSetGroundTexture

```json
{
 "arguments": [
  {
   "changes": {
    "tooltip": "A list of terrain detail properties and values to change.",
    "type": "list",
    "param-semantics": "GroundTextureParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 558,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Changes the painted terrain textures on the region based on changes. The script owner must have estate management rights. Returns an integer status.",
 "categories": [
  "region"
 ]
}
```


## functions/llSetHoverHeight

```json
{
 "arguments": [
  {
   "height": {
    "tooltip": "Distance to hover above the ground or water.",
    "type": "float"
   }
  },
  {
   "water": {
    "tooltip": "Boolean. If TRUE, hovers above water too; if FALSE, water is ignored.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "tau": {
    "tooltip": "Timescale in seconds to critically damp the movement.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 123,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Critically damps the physical object's vertical movement to hover at height (above ground, or above water if water is TRUE) in tau seconds. Do not use with vehicles; call llStopHover to cancel.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llSetInventoryPermMask

```json
{
 "arguments": [
  {
   "item": {
    "tooltip": "Name of the item in the prim's inventory.",
    "type": "string"
   }
  },
  {
   "group": {
    "tooltip": "MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to set.",
    "type": "integer",
    "enum-semantics": "AssetPermissionCategory"
   }
  },
  {
   "flags": {
    "tooltip": "Bitfield of permissions (PERM_* flags) to set.",
    "type": "integer",
    "enum-semantics": "AssetPermission"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 290,
 "god-mode": true,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the specified item's permission flags for the specified group.",
 "categories": [
  "asset_permissions",
  "prim_inventory"
 ]
}
```


## functions/llSetKeyframedMotion

```json
{
 "arguments": [
  {
   "keyframes": {
    "tooltip": "A strided list of the form [vector position, rotation orientation, float time] representing sequential relative keyframes (minimum time is 1/9s).",
    "type": "list"
   }
  },
  {
   "options": {
    "tooltip": "A list of options (KFM_* constants) to modify playback behavior.",
    "type": "list",
    "param-semantics": "KeyframedMotionParam",
    "ruleset": "keyframed-motion-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 394,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Smoothly moves a non-physical object between the positions, orientations, and times specified in the keyframes list, configured via options. Collisions with keyframed objects are ignored. An empty keyframes list terminates the motion.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llSetLinkAlpha

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "alpha": {
    "tooltip": "Transparency value to set, from 0.0 (clear) to 1.0 (solid).",
    "type": "float"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 274,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the Blinn-Phong alpha (transparency) of face on the linked prim link.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llSetLinkCamera

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  },
  {
   "eye": {
    "tooltip": "Eye offset position vector in local coordinates relative to the prim.",
    "type": "vector"
   }
  },
  {
   "at": {
    "tooltip": "Look-at offset position vector in local coordinates relative to the prim.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 377,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the camera eye position offset eye and looking-at position offset at for avatars who sit on the linked prim link.",
 "categories": [
  "camera",
  "sit"
 ]
}
```


## functions/llSetLinkColor

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "color": {
    "tooltip": "Color vector in RGB <R, G, B> (values from 0.0 to 1.0).",
    "type": "vector"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 140,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the Blinn-Phong diffuse RGB color of face on the linked prim link.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llSetLinkGLTFOverrides

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  },
  {
   "params": {
    "tooltip": "A list of overrides and their corresponding values to set.",
    "type": "list",
    "param-semantics": "GLTFOverride",
    "ruleset": "gltf-overrides"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 560,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets or removes individual GLTF override parameters specified by params on face of the linked prim link.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llSetLinkMedia

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  },
  {
   "face": {
    "tooltip": "Face number (side) of the prim.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  },
  {
   "params": {
    "tooltip": "A set of property-value pairs (in no particular order) specifying media parameters, or a PrimMediaParams dictionary.",
    "type": "list",
    "param-semantics": "PrimMediaParam",
    "ruleset": "prim-media-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 371,
 "return": "integer",
 "enum-semantics": "PrimMediaError",
 "sleep": 0.0,
 "tooltip": "Sets the media parameters specified by params on face of the linked prim link without a script delay. Returns an integer STATUS_* flag detailing success or failure.",
 "categories": [
  "linkset",
  "media",
  "prim_media",
  "web"
 ]
}
```


## functions/llSetLinkPrimitiveParams

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "rules": {
    "tooltip": "A list of PRIM_* rules and data to apply.",
    "type": "list",
    "param-semantics": "PrimParam"
   }
  }
 ],
 "deprecated": {
  "use": "ll.SetLinkPrimitiveParamsFast",
  "selene-replace": [
   "ll.SetLinkPrimitiveParamsFast(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 328,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Deprecated (use llSetLinkPrimitiveParamsFast instead). Sets primitive parameters for the linked prim link according to rules.",
 "categories": [
  "linkset",
  "prim_appearance",
  "prim_properties"
 ]
}
```


## functions/llSetLinkPrimitiveParamsFast

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "rules": {
    "tooltip": "A list of PRIM_* rules and data to apply.",
    "type": "list",
    "param-semantics": "PrimParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 353,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets primitive parameters for the linked prim link according to rules with no built-in script sleep delay.",
 "categories": [
  "linkset",
  "prim_appearance",
  "prim_properties"
 ]
}
```


## functions/llSetLinkRenderMaterial

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "material": {
    "tooltip": "Name of a material in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 762,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Applies material (UUID or inventory name) to face of the linked prim link. Note: This clears most PRIM_GLTF_* properties on the face except for repeats, offsets, and rotation.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llSetLinkSitFlags

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "flags": {
    "tooltip": "A bitfield of sit flags (SIT_FLAG_*) to apply.",
    "type": "integer",
    "enum-semantics": "SitFlag"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 550,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the sit target flags for the linked prim link inside the linkset.",
 "categories": [
  "linkset",
  "sit"
 ]
}
```


## functions/llSetLinkTexture

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "texture": {
    "tooltip": "Name of a texture in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 329,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Applies texture (UUID or inventory name) to face of the linked prim link.",
 "categories": [
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llSetLinkTextureAnim

```json
{
 "arguments": [
  {
   "link": {
    "tooltip": "Link number (1 for root, >1 for children) or a LINK_* flag to animate.",
    "type": "integer",
    "enum-semantics": "Links"
   }
  },
  {
   "mode": {
    "tooltip": "Bitfield of texture animation mode flags (ANIM_ON, LOOP, etc.).",
    "type": "integer",
    "enum-semantics": "TextureAnimMode"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  },
  {
   "sizex": {
    "tooltip": "Number of horizontal frames (ignored for ROTATE and SCALE).",
    "type": "integer",
    "range": [
     0,
     255
    ]
   }
  },
  {
   "sizey": {
    "tooltip": "Number of vertical frames (ignored for ROTATE and SCALE).",
    "type": "integer",
    "range": [
     0,
     255
    ]
   }
  },
  {
   "start": {
    "tooltip": "Start frame number (or radians for ROTATE).",
    "type": "float"
   }
  },
  {
   "length": {
    "tooltip": "Number of frames to display (or radians for ROTATE).",
    "type": "float"
   }
  },
  {
   "rate": {
    "tooltip": "Playback rate in frames per second (or radians/sec for ROTATE, UV coords/sec for SMOOTH). Must not be zero.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 356,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Animates the texture on face of the linked prim link by setting the scale and offset according to mode. Parameters sizex/sizey define frames, start defines the start frame/angle, length defines duration, and rate defines playback speed.",
 "categories": [
  "effects",
  "linkset",
  "prim_appearance"
 ]
}
```


## functions/llSetLocalRot

```json
{
 "arguments": [
  {
   "rot": {
    "tooltip": "Local rotation to set.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 284,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Sets the rotation of a child prim relative to its root prim using rot.",
 "categories": [
  "movement",
  "prim"
 ]
}
```


## functions/llSetMemoryLimit

```json
{
 "arguments": [
  {
   "limit": {
    "tooltip": "Integer memory limit in bytes to reserve (must be less than the 64KB maximum).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 369,
 "return": "integer",
 "bool-semantics": true,
 "slua-removed": true,
 "sleep": 0.0,
 "tooltip": "Requests that limit bytes are reserved for the script. Returns TRUE on success or FALSE on failure (has no effect in LSO).",
 "categories": [
  "script"
 ]
}
```


## functions/llSetObjectDesc

```json
{
 "arguments": [
  {
   "description": {
    "tooltip": "New description string (up to 127 characters).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 271,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the description of the prim containing the script to description (limited to 127 characters).",
 "categories": [
  "prim",
  "prim_properties"
 ]
}
```


## functions/llSetObjectName

```json
{
 "arguments": [
  {
   "name": {
    "tooltip": "New name string.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 203,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the name of the prim containing the script to name.",
 "categories": [
  "prim",
  "prim_properties"
 ]
}
```


## functions/llSetObjectPermMask

```json
{
 "arguments": [
  {
   "group": {
    "tooltip": "MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to set.",
    "type": "integer",
    "enum-semantics": "AssetPermissionCategory"
   }
  },
  {
   "flags": {
    "tooltip": "Bitfield of permissions (PERM_* flags) to set.",
    "type": "integer",
    "enum-semantics": "AssetPermission"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 288,
 "god-mode": true,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the scripts's object's permission flags for the specified group.",
 "categories": [
  "asset_permissions",
  "linkset"
 ]
}
```


## functions/llSetParcelForSale

```json
{
 "arguments": [
  {
   "ForSale": {
    "tooltip": "Boolean. If TRUE, puts the parcel up for sale; if FALSE, removes it from sale.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "Options": {
    "tooltip": "A list of options to configure the sale (e.g., price, authorized buyer, and object inclusion).",
    "type": "list",
    "param-semantics": "ParcelSaleParam",
    "ruleset": "parcel-sale"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 561,
 "return": "integer",
 "enum-semantics": "ParcelSaleError",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_PRIVILEGED_LAND_ACCESS"
 ],
 "tooltip": "Sets the parcel the object is on for sale. If ForSale is TRUE, puts the land up for sale using Options (price, buyer, objects included). Setting ForSale to FALSE removes the parcel from sale. Requires parcel ownership and the PERMISSION_PRIVILEGED_LAND_ACCESS permission. Returns an error code or 0 if successful.",
 "categories": [
  "parcel"
 ]
}
```


## functions/llSetParcelMusicURL

```json
{
 "arguments": [
  {
   "url": {
    "tooltip": "Streaming audio URL string.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 267,
 "return": "void",
 "sleep": 2.0,
 "tooltip": "Sets the streaming audio (music) URL for the parcel containing the object. The object owner must match the landowner or land group.",
 "categories": [
  "media",
  "parcel",
  "parcel_media"
 ]
}
```


## functions/llSetPayPrice

```json
{
 "arguments": [
  {
   "price": {
    "tooltip": "Default price integer shown in the text field (can accept PAY_* constants or positive values).",
    "type": "integer"
   }
  },
  {
   "quick_pay_buttons": {
    "tooltip": "A list of four integer values or PAY_* constants specifying the button payment choices.",
    "type": "list",
    "param-semantics": "PayButton",
    "slua-type": "{number}"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 302,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Suggests default amounts for the pay text input field price and the four payment dialog quick_pay_buttons when an avatar pays this object.",
 "categories": [
  "money",
  "prim_properties",
  "user_interface"
 ]
}
```


## functions/llSetPhysicsMaterial

```json
{
 "arguments": [
  {
   "mask": {
    "tooltip": "Bitwise mask combination specifying which of the floats (DENSITY, FRICTION, RESTITUTION, or GRAVITY_MULTIPLIER) to apply.",
    "type": "integer",
    "enum-semantics": "PhysicsMaterialParam"
   }
  },
  {
   "gravity_multiplier": {
    "tooltip": "Gravity multiplier float value (range [-1.0, +28.0], default is 1.0).",
    "type": "float",
    "range": [
     -1,
     28
    ]
   }
  },
  {
   "restitution": {
    "tooltip": "Elasticity restitution float value (range [0.0, 1.0]).",
    "type": "float",
    "range": [
     0,
     1
    ]
   }
  },
  {
   "friction": {
    "tooltip": "Friction coefficient float value (range [0.0, 255.0]).",
    "type": "float",
    "range": [
     0,
     255
    ]
   }
  },
  {
   "density": {
    "tooltip": "Density float value in kg/m³ (range [1.0, 22587.0]).",
    "type": "float",
    "range": [
     1,
     22587
    ]
   }
  }
 ],
 "energy": 10.0,
 "func-id": 380,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Configures the physical characteristics of an object. The mask bitfield specifies which of the other parameters (gravity_multiplier, restitution, friction, or density) should be applied to the object.",
 "categories": [
  "physics",
  "prim",
  "prim_properties"
 ],
 "uses-enum": "PhysicsMaterialPreset"
}
```


## functions/llSetPos

```json
{
 "arguments": [
  {
   "pos": {
    "tooltip": "Position vector to move to (in region coordinates, or local coordinates if in a child prim).",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 58,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Moves the non-physical object or prim toward the vector pos (up to 10m). If called in a child prim, pos is treated as root-relative; if called from the root prim, the entire object is moved.",
 "categories": [
  "movement",
  "prim"
 ]
}
```


## functions/llSetPrimMediaParams

```json
{
 "arguments": [
  {
   "face": {
    "tooltip": "Face number (side) of the prim.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  },
  {
   "params": {
    "tooltip": "A set of property-value pairs (in no particular order) specifying media parameters.",
    "type": "list",
    "param-semantics": "PrimMediaParam",
    "ruleset": "prim-media-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 350,
 "return": "integer",
 "enum-semantics": "PrimMediaError",
 "sleep": 1.0,
 "tooltip": "Sets the media parameters specified by params on the designated face of the prim. Returns an integer STATUS_* flag detailing success or failure.",
 "categories": [
  "media",
  "prim",
  "prim_media",
  "web"
 ]
}
```


## functions/llSetPrimURL

```json
{
 "arguments": [
  {
   "url": {
    "tooltip": "Web URL to display.",
    "type": "string"
   }
  }
 ],
 "deprecated": {
  "use": "ll.SetPrimMediaParams",
  "selene-replace": [
   "ll.SetPrimMediaParams(ALL_SIDES, {PRIM_MEDIA_CURRENT_URL, %1})"
  ]
 },
 "energy": 10.0,
 "func-id": 305,
 "return": "void",
 "sleep": 20.0,
 "tooltip": "Deprecated (use llSetPrimMediaParams instead). Updates the URL displayed on the prim's faces.",
 "categories": [
  "media",
  "prim",
  "prim_media",
  "web"
 ]
}
```


## functions/llSetPrimitiveParams

```json
{
 "arguments": [
  {
   "rules": {
    "tooltip": "A list of PRIM_* rules and data to apply.",
    "type": "list",
    "param-semantics": "PrimParam"
   }
  }
 ],
 "deprecated": {
  "use": "ll.SetLinkPrimitiveParamsFast",
  "selene-replace": [
   "ll.SetLinkPrimitiveParamsFast(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 259,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Deprecated (use llSetLinkPrimitiveParamsFast instead). Sets the prim's attributes according to rules.",
 "categories": [
  "prim",
  "prim_appearance",
  "prim_properties"
 ]
}
```


## functions/llSetRegionPos

```json
{
 "arguments": [
  {
   "position": {
    "tooltip": "Target position vector in region coordinates (can cross up to 10m over a region border).",
    "type": "vector",
    "range": [
     "<-10,-10,0>",
     "<266,266,4096>"
    ]
   }
  }
 ],
 "energy": 10.0,
 "func-id": 397,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Tries to move the entire object so that its root prim is within 0.1m of the vector position (underground positions are set to ground level). Returns TRUE on success or FALSE on failure.",
 "categories": [
  "movement",
  "prim"
 ]
}
```


## functions/llSetRemoteScriptAccessPin

```json
{
 "arguments": [
  {
   "pin": {
    "tooltip": "Integer PIN code (non-zero enables, zero disables).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 252,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Sets the prim's remote script access PIN to pin (a non-zero value enables loading via llRemoteLoadScriptPin, while zero disables it).",
 "categories": [
  "prim_inventory",
  "script"
 ]
}
```


## functions/llSetRenderMaterial

```json
{
 "arguments": [
  {
   "material": {
    "tooltip": "Name of a material in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 761,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Applies material (UUID or inventory name) to face of the prim. Note: This clears most PRIM_GLTF_* properties on the face except for repeats, offsets, and rotation.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llSetRot

```json
{
 "arguments": [
  {
   "rot": {
    "tooltip": "Target rotation.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 61,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Sets the rotation of the prim to rot. If in a child prim, rot is treated as root-relative; if in the root prim of a non-physical object, rotates the entire object.",
 "categories": [
  "movement",
  "prim"
 ]
}
```


## functions/llSetScale

```json
{
 "arguments": [
  {
   "size": {
    "tooltip": "Target size vector.",
    "type": "vector",
    "range": [
     "<0.01,0.01,0.01>",
     "<64,64,64>"
    ]
   }
  }
 ],
 "energy": 10.0,
 "func-id": 47,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the physical scale (dimensions) of the prim containing the script to size.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llSetScriptState

```json
{
 "arguments": [
  {
   "script": {
    "tooltip": "Name of the script in the prim's inventory.",
    "type": "string"
   }
  },
  {
   "running": {
    "tooltip": "Boolean. If TRUE, enables the script; if FALSE, disables it.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 148,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the running state of the named script in the prim's inventory. If running is TRUE, the script is enabled; if FALSE, it is disabled.",
 "categories": [
  "prim_inventory",
  "script"
 ]
}
```


## functions/llSetSitText

```json
{
 "arguments": [
  {
   "text": {
    "tooltip": "Context menu text to display.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 242,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Displays the string text instead of 'Sit' (or 'Sit Here') in the viewer's right-click context menu.",
 "categories": [
  "prim",
  "sit",
  "user_interface"
 ]
}
```


## functions/llSetSoundQueueing

```json
{
 "arguments": [
  {
   "queue": {
    "tooltip": "Boolean. If TRUE, sound queuing is enabled; if FALSE, it is disabled.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 208,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets whether attached sounds wait for the current sound to end before playing (enables queuing if queue is TRUE, disables if FALSE). The queue is one level deep.",
 "categories": [
  "sound"
 ]
}
```


## functions/llSetSoundRadius

```json
{
 "arguments": [
  {
   "radius": {
    "tooltip": "Maximum distance in meters at which the sounds can be heard.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 209,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Limits the audibility radius of attached and triggered scripted sounds to distance radius.",
 "categories": [
  "sound"
 ]
}
```


## functions/llSetStatus

```json
{
 "arguments": [
  {
   "status": {
    "tooltip": "Bitmask representing the STATUS_* flag(s) to change.",
    "type": "integer",
    "enum-semantics": "ObjectStatusParam"
   }
  },
  {
   "value": {
    "tooltip": "Boolean. If TRUE, enables the status; if FALSE, disables it.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 45,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the object status attributes specified by status to value.",
 "categories": [
  "linkset",
  "physics",
  "prim_properties"
 ]
}
```


## functions/llSetText

```json
{
 "arguments": [
  {
   "text": {
    "tooltip": "Floating text string to display.",
    "type": "string"
   }
  },
  {
   "color": {
    "tooltip": "Color vector in RGB <R, G, B> (values from 0.0 to 1.0).",
    "type": "vector"
   }
  },
  {
   "alpha": {
    "tooltip": "Transparency value to set, from 0.0 (clear) to 1.0 (solid).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 152,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Displays floating text above the prim with the specified color vector and transparency alpha.",
 "categories": [
  "avatar_communication",
  "effects",
  "prim_appearance",
  "prim_properties"
 ]
}
```


## functions/llSetTexture

```json
{
 "arguments": [
  {
   "texture": {
    "tooltip": "Name of a texture in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 53,
 "return": "void",
 "sleep": 0.2,
 "tooltip": "Applies the Blinn-Phong diffuse texture to face of the prim.",
 "categories": [
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llSetTextureAnim

```json
{
 "arguments": [
  {
   "mode": {
    "tooltip": "Bitfield of texture animation mode flags (ANIM_ON, LOOP, etc.).",
    "type": "integer",
    "enum-semantics": "TextureAnimMode"
   }
  },
  {
   "face": {
    "tooltip": "Face number or ALL_SIDES.",
    "type": "integer",
    "enum-semantics": "Faces"
   }
  },
  {
   "sizex": {
    "tooltip": "Number of horizontal frames (ignored for ROTATE and SCALE).",
    "type": "integer",
    "range": [
     0,
     255
    ]
   }
  },
  {
   "sizey": {
    "tooltip": "Number of vertical frames (ignored for ROTATE and SCALE).",
    "type": "integer",
    "range": [
     0,
     255
    ]
   }
  },
  {
   "start": {
    "tooltip": "Start frame number (or radians for ROTATE).",
    "type": "float"
   }
  },
  {
   "length": {
    "tooltip": "Number of frames to display (or radians for ROTATE).",
    "type": "float"
   }
  },
  {
   "rate": {
    "tooltip": "Playback rate in frames per second (or radians/sec for ROTATE, UV coords/sec for SMOOTH). Must not be zero.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 211,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Animates the texture on face of the prim by setting its scale and offset. mode defines options, sizex/sizey define frames, start defines the start frame/angle, length defines duration, and rate defines playback speed.",
 "categories": [
  "effects",
  "prim",
  "prim_appearance"
 ]
}
```


## functions/llSetTimerEvent

```json
{
 "arguments": [
  {
   "sec": {
    "tooltip": "Interval in seconds between timer events (0.0 to disable).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 107,
 "return": "void",
 "slua-removed": true,
 "sleep": 0.0,
 "tooltip": "Sets a timer to trigger a timer event periodically every sec seconds. Passing 0.0 stops further timer events.",
 "categories": [
  "script",
  "time"
 ]
}
```


## functions/llSetTorque

```json
{
 "arguments": [
  {
   "torque": {
    "tooltip": "Torque rotational force vector.",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, torque is treated as a local vector; if FALSE, as a global region vector.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 74,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Applies a constant torque rotational force to a physical object. If local is TRUE, torque is applied in local coordinates; if FALSE, applied in global coordinates.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llSetTouchText

```json
{
 "arguments": [
  {
   "text": {
    "tooltip": "Context menu text to display.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 241,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Displays the string text instead of 'Touch' in the right-click context menu.",
 "categories": [
  "prim_properties",
  "touch",
  "user_interface"
 ]
}
```


## functions/llSetVehicleFlags

```json
{
 "arguments": [
  {
   "flags": {
    "tooltip": "A bitwise mask of VEHICLE_FLAG_* constants to enable.",
    "type": "integer",
    "enum-semantics": "VehicleFlag"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 236,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Enables the vehicle flags specified in the Flags bitmask.",
 "categories": [
  "vehicles"
 ]
}
```


## functions/llSetVehicleFloatParam

```json
{
 "arguments": [
  {
   "param": {
    "tooltip": "VEHICLE_* float parameter constant to set.",
    "type": "integer",
    "enum-semantics": "VehicleFloatParam"
   }
  },
  {
   "value": {
    "tooltip": "Float value to set.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 233,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the specified vehicle float parameter param to value.",
 "categories": [
  "vehicles"
 ]
}
```


## functions/llSetVehicleRotationParam

```json
{
 "arguments": [
  {
   "param": {
    "tooltip": "VEHICLE_* rotation parameter constant to set.",
    "type": "integer",
    "enum-semantics": "VehicleRotationParam"
   }
  },
  {
   "rot": {
    "tooltip": "Rotation value to set.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 235,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the specified vehicle rotation parameter param to rot.",
 "categories": [
  "vehicles"
 ]
}
```


## functions/llSetVehicleType

```json
{
 "arguments": [
  {
   "type": {
    "tooltip": "VEHICLE_TYPE_* constant to set.",
    "type": "integer",
    "enum-semantics": "VehicleType"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 232,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the vehicle physics preset type to one of the default vehicle types.",
 "categories": [
  "vehicles"
 ]
}
```


## functions/llSetVehicleVectorParam

```json
{
 "arguments": [
  {
   "param": {
    "tooltip": "VEHICLE_* vector parameter constant to set.",
    "type": "integer",
    "enum-semantics": "VehicleVectorParam"
   }
  },
  {
   "vec": {
    "tooltip": "Vector value to set.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 234,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the specified vehicle vector parameter param to vec.",
 "categories": [
  "vehicles"
 ]
}
```


## functions/llSetVelocity

```json
{
 "arguments": [
  {
   "velocity": {
    "tooltip": "Linear velocity vector to apply (in meters per second).",
    "type": "vector"
   }
  },
  {
   "is_local": {
    "tooltip": "Boolean. If TRUE, velocity is treated as a local directional vector; if FALSE, as a global region vector.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 378,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the linear velocity of a physical object to velocity. If local is TRUE, velocity is treated as a local directional vector; if FALSE, as a global region directional vector. Has no effect on non-physical objects.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llShout

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "Chat channel (any 32-bit signed integer value) to shout the message on.",
    "type": "integer",
    "enum-semantics": "Channel"
   }
  },
  {
   "msg": {
    "tooltip": "Text message string to broadcast.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 24,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv(\"shout_range\"), which is 100m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## functions/llSignRSA

```json
{
 "arguments": [
  {
   "private_key": {
    "tooltip": "PEM-formatted private key.",
    "type": "string"
   }
  },
  {
   "msg": {
    "tooltip": "Message contents to sign.",
    "type": "string"
   }
  },
  {
   "algorithm": {
    "tooltip": "Digest algorithm to use (sha1, sha224, sha256, sha384, or sha512).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 539,
 "must-use": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the Base64-encoded RSA signature of msg using the PEM-formatted private_key and the specified digest algorithm (sha1, sha224, sha256, sha384, or sha512). Can be paired with llVerifyRSA to pass verifiable messages.",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llSin

```json
{
 "arguments": [
  {
   "theta": {
    "tooltip": "Angle in radians.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.sin",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.sin(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 0,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the sine of theta. Theta is in radians.",
 "categories": [
  "math",
  "math_trig"
 ]
}
```


## functions/llSitOnLink

```json
{
 "arguments": [
  {
   "agent_id": {
    "tooltip": "UUID of the avatar being forced to sit.",
    "type": "key"
   }
  },
  {
   "link": {
    "tooltip": "Link number for the prim containing the desired sit target.",
    "type": "integer",
    "enum-semantics": "Link"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 503,
 "experience": true,
 "return": "integer",
 "enum-semantics": "SitError",
 "sleep": 0.0,
 "tooltip": "Forces the avatar specified by agent_id (who must be participating in the experience) to sit on the sit target of the prim indicated by link. If occupied, searches down the linkset for an available sit target. Returns an integer.",
 "categories": [
  "experience",
  "sit"
 ]
}
```


## functions/llSitTarget

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Target position vector in local prim coordinates.",
    "type": "vector",
    "range": [
     "<-300,-300,-300>",
     "<300,300,300>"
    ]
   }
  },
  {
   "rot": {
    "tooltip": "Target rotation relative to the prim's rotation.",
    "type": "rotation"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 238,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Sets the sit target position (offset) and rotation (rot) relative to the prim's position and orientation. Clears the sit target if offset is ZERO_VECTOR.",
 "categories": [
  "prim",
  "sit"
 ]
}
```


## functions/llSleep

```json
{
 "arguments": [
  {
   "sec": {
    "tooltip": "Duration in seconds to put the script to sleep.",
    "type": "float"
   }
  }
 ],
 "energy": 0.0,
 "func-id": 108,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Puts the script to sleep for sec seconds (at least until the next server-frame, ~0.02222 seconds). The script is inactive during this time. If sec is 0.0 or less, the script does not sleep.",
 "categories": [
  "script",
  "time"
 ]
}
```


## functions/llSound

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  },
  {
   "queue": {
    "tooltip": "Boolean. If TRUE, queues the sound; if FALSE, interrupts the currently playing sound.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "loop": {
    "tooltip": "Boolean. If TRUE, loops the sound.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "deprecated": {
  "use": "ll.PlaySound",
  "selene-replace": [
   "ll.PlaySound(%1, %2)",
   "ll.LoopSound(%1, %2)"
  ]
 },
 "energy": 10.0,
 "func-id": 85,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Deprecated (use llPlaySound instead). Plays the specified sound at volume, with options to loop or queue the sound.",
 "categories": [
  "sound"
 ]
}
```


## functions/llSoundPreload

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  }
 ],
 "deprecated": {
  "use": "ll.PreloadSound",
  "selene-replace": [
   "ll.PreloadSound(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 126,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Deprecated (use llPreloadSound instead). Preloads the specified sound on viewers within range.",
 "categories": [
  "sound"
 ]
}
```


## functions/llSqrt

```json
{
 "arguments": [
  {
   "val": {
    "tooltip": "Positive float value (must be >= 0.0).",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.sqrt",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.sqrt(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 4,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the square root of val. If negative, return NaN.",
 "categories": [
  "math"
 ]
}
```


## functions/llStartAnimation

```json
{
 "arguments": [
  {
   "anim": {
    "tooltip": "Name of the animation in the prim's inventory, or the built-in animation name.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 129,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TRIGGER_ANIMATION"
 ],
 "tooltip": "Starts the animation anim (inventory or built-in) on the avatar who granted the script the PERMISSION_TRIGGER_ANIMATION permission (automatically granted for attached or sat-on objects).",
 "categories": [
  "avatar",
  "avatar_animation",
  "permissions"
 ]
}
```


## functions/llStartObjectAnimation

```json
{
 "arguments": [
  {
   "anim": {
    "tooltip": "Name of the animation in the prim's inventory, or the built-in animation name.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 504,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Starts the specified animation anim (inventory or built-in) on the rigged mesh object associated with the current script.",
 "categories": [
  "object_animation"
 ]
}
```


## functions/llStopAnimation

```json
{
 "arguments": [
  {
   "anim": {
    "tooltip": "Name of the animation in the prim's inventory, the UUID of the animation, or the built-in animation name.",
    "type": "string",
    "asset-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 130,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TRIGGER_ANIMATION"
 ],
 "tooltip": "Stops the specified animation anim (inventory, built-in, or UUID) on the avatar who granted the script the PERMISSION_TRIGGER_ANIMATION permission (automatically granted for attached or sat-on objects).",
 "categories": [
  "avatar",
  "avatar_animation",
  "permissions"
 ]
}
```


## functions/llStopHover

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 124,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops the hover behavior (such as that initiated by llSetHoverHeight).",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llStopLookAt

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 106,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops causing the object to look at or point toward a target (canceling llLookAt or llRotLookAt).",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llStopMoveToTarget

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 71,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops the critically damped movement of the object toward a target (canceling llMoveToTarget). Use llStopLookAt to stop rotational tracking.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llStopObjectAnimation

```json
{
 "arguments": [
  {
   "anim": {
    "tooltip": "Name of the animation in the prim's inventory, the UUID of the animation, or the built-in animation name.",
    "type": "string",
    "asset-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 505,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops the specified animation anim (inventory, built-in, or UUID) on the rigged mesh object associated with the current script.",
 "categories": [
  "object_animation"
 ]
}
```


## functions/llStopPointAt

```json
{
 "arguments": [],
 "deprecated": true,
 "energy": 10.0,
 "func-id": 132,
 "private": true,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops the avatar who owns the object from pointing.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llStopSound

```json
{
 "arguments": [],
 "energy": 10.0,
 "func-id": 92,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Stops playback of the currently playing attached sound.",
 "categories": [
  "sound"
 ]
}
```


## functions/llStringLength

```json
{
 "arguments": [
  {
   "str": {
    "tooltip": "String to measure.",
    "type": "string"
   }
  }
 ],
 "slua-deprecated": {
  "reason": "Use 'utf8.len' or '#' or 'string.len' instead.",
  "selene-replace": [
   "utf8.len(%1)",
   "#%1",
   "string.len(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 128,
 "pure": true,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Returns the number of unicode codepoints in the string.",
 "categories": [
  "string"
 ]
}
```


## functions/llStringToBase64

```json
{
 "arguments": [
  {
   "str": {
    "tooltip": "Source string to encode.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 260,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns the Base64 representation string of str, interpreting it as a UTF-8 byte sequence.",
 "categories": [
  "data_conversion"
 ],
 "slua-deprecated": {
  "use": "llbase64.encode",
  "selene-replace": [
   "llbase64.encode(%1)"
  ]
 }
}
```


## functions/llStringTrim

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "String to trim.",
    "type": "string"
   }
  },
  {
   "type": {
    "tooltip": "Trim type flag (STRING_TRIM_HEAD, STRING_TRIM_TAIL, or STRING_TRIM).",
    "type": "integer",
    "enum-semantics": "StringTrimType"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 330,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a copy of the string src with leading, trailing, or both types of whitespace (including spaces, tabs, and line feeds) eliminated, according to the specified trim type.",
 "categories": [
  "string"
 ]
}
```


## functions/llSubStringIndex

```json
{
 "arguments": [
  {
   "source": {
    "tooltip": "Source string to search within.",
    "type": "string"
   }
  },
  {
   "pattern": {
    "tooltip": "Substring pattern to search for.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 181,
 "pure": true,
 "return": "integer",
 "index-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns the codepoint index of the first occurrence of pattern inside the string source. Returns -1 if not found. No regex.",
 "categories": [
  "string"
 ]
}
```


## functions/llTakeCamera

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar in the same region.",
    "type": "key"
   }
  }
 ],
 "deprecated": {
  "use": "ll.SetCameraParams"
 },
 "energy": 10.0,
 "func-id": 115,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Deprecated (use llSetCameraParams instead). Formerly used to take control of the agent's camera.",
 "categories": [
  "avatar",
  "camera",
  "permissions"
 ]
}
```


## functions/llTakeControls

```json
{
 "arguments": [
  {
   "controls": {
    "tooltip": "Bitfield of CONTROL_* flags to intercept.",
    "type": "integer",
    "enum-semantics": "ControlButton"
   }
  },
  {
   "accept": {
    "tooltip": "Boolean. Determines whether control events are generated to trigger script handlers.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "pass_on": {
    "tooltip": "Boolean. If TRUE, the keys also perform their default functions; if FALSE, default actions are suppressed.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 111,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TAKE_CONTROLS"
 ],
 "tooltip": "Intercepts inputs (keyboard/mouse clicks) from the agent, specifically those specified by controls. The boolean accept determines if events are generated, and pass_on determines if inputs also perform their default functions. Requires the PERMISSION_TAKE_CONTROLS runtime permission.",
 "categories": [
  "avatar",
  "input",
  "permissions"
 ]
}
```


## functions/llTan

```json
{
 "arguments": [
  {
   "theta": {
    "tooltip": "Angle in radians.",
    "type": "float"
   }
  }
 ],
 "slua-deprecated": {
  "use": "math.tan",
  "reason": "Double precision; fastcall.",
  "selene-replace": [
   "math.tan(%...)"
  ]
 },
 "energy": 10.0,
 "func-id": 2,
 "native": true,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the tangent of theta. Theta is in radians.",
 "categories": [
  "math",
  "math_trig"
 ]
}
```


## functions/llTarget

```json
{
 "arguments": [
  {
   "position": {
    "tooltip": "Target position vector in region coordinates.",
    "type": "vector"
   }
  },
  {
   "range": {
    "tooltip": "Radius tolerance in meters surrounding the target position.",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 66,
 "return": "integer",
 "sleep": 0.0,
 "tooltip": "Registers a positional target at position with a leeway radius range. This triggers at_target and not_at_target events. Returns an integer handle to unregister the target via llTargetRemove.",
 "categories": [
  "movement"
 ]
}
```


## functions/llTargetOmega

```json
{
 "arguments": [
  {
   "axis": {
    "tooltip": "Local axis vector around which the object rotates.",
    "type": "vector"
   }
  },
  {
   "spinrate": {
    "tooltip": "Rotation rate multiplier in radians per second.",
    "type": "float"
   }
  },
  {
   "gain": {
    "tooltip": "A float modulating the rotational strength (disables the rotation if set to 0.0).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 133,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Applies a smooth client-side rotation around the local axis at a rate equal to spinrate multiplied by the magnitude of axis (in radians per second) with a force defined by gain. Set spinrate to 0.0 to cancel.",
 "categories": [
  "movement",
  "physics"
 ]
}
```


## functions/llTargetRemove

```json
{
 "arguments": [
  {
   "handle": {
    "tooltip": "Integer target handle returned by llTarget to remove.",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 67,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Removes the positional target specified by the integer handle registered with llTarget.",
 "categories": [
  "movement"
 ]
}
```


## functions/llTargetedEmail

```json
{
 "arguments": [
  {
   "target": {
    "tooltip": "Target constant (e.g., TARGETED_EMAIL_OBJECT_OWNER or TARGETED_EMAIL_ROOT_CREATOR).",
    "type": "integer",
    "enum-semantics": "EmailTarget"
   }
  },
  {
   "subject": {
    "tooltip": "Subject of the email.",
    "type": "string"
   }
  },
  {
   "msg": {
    "tooltip": "Email message body.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 750,
 "return": "void",
 "sleep": 20.0,
 "tooltip": "Sends an email to with the given subject subject and body msg to the target (which can designate the owner or creator of the object). The email will be sent from `{ll.GetKey()}@lsl.secondlife.com`.",
 "categories": [
  "avatar_communication"
 ]
}
```


## functions/llTeleportAgent

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the owning avatar to teleport.",
    "type": "key"
   }
  },
  {
   "landmark": {
    "tooltip": "Name of the landmark in the prim's inventory, or an empty string to teleport locally.",
    "type": "string"
   }
  },
  {
   "position": {
    "tooltip": "Position vector in local region coordinates to teleport to if landmark is empty.",
    "type": "vector"
   }
  },
  {
   "look_at": {
    "tooltip": "Position vector (or direction unit vector if teleporting out of region) the agent faces upon landing.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 368,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TELEPORT"
 ],
 "tooltip": "Teleports the owning agent (who must grant PERMISSION_TELEPORT) to a landmark in the object's inventory. If landmark is empty, teleports them to position within the current region. Upon arrival, the agent is turned to face look_at. Can only teleport the owner.",
 "categories": [
  "avatar",
  "permissions",
  "teleport"
 ]
}
```


## functions/llTeleportAgentGlobalCoords

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the owning avatar to teleport.",
    "type": "key"
   }
  },
  {
   "global_coordinates": {
    "tooltip": "Global coordinates vector of the target region (obtained via llRequestSimulatorData).",
    "type": "vector"
   }
  },
  {
   "region_coordinates": {
    "tooltip": "Target coordinates vector within the destination region.",
    "type": "vector"
   }
  },
  {
   "look_at": {
    "tooltip": "Position vector within the region (or unit direction vector if out of region) that the agent faces upon landing.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 414,
 "return": "void",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TELEPORT"
 ],
 "tooltip": "Teleports the owning agent (who must grant PERMISSION_TELEPORT) to region_coordinates within a target region specified by global_coordinates. Upon landing, the agent faces the direction look_at. Can only teleport the owner.",
 "categories": [
  "avatar",
  "permissions",
  "teleport"
 ]
}
```


## functions/llTeleportAgentHome

```json
{
 "arguments": [
  {
   "avatar": {
    "tooltip": "UUID of the avatar to teleport.",
    "type": "key"
   }
  }
 ],
 "energy": 100.0,
 "func-id": 158,
 "return": "void",
 "sleep": 5.0,
 "tooltip": "Teleports the avatar (who must be standing on land owned by the script owner) directly to their designated home location without warning (similar to a God Summons).",
 "categories": [
  "avatar",
  "land_moderation",
  "teleport"
 ]
}
```


## functions/llTextBox

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the agent in the same region.",
    "type": "key"
   }
  },
  {
   "msg": {
    "tooltip": "Text message to display in the text box.",
    "type": "string"
   }
  },
  {
   "channel": {
    "tooltip": "Output chat channel (any 32-bit signed integer value) where the input text is chatted.",
    "type": "integer",
    "enum-semantics": "Channel"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 335,
 "mono-sleep": 0.0,
 "return": "void",
 "sleep": 1.0,
 "tooltip": "Opens an input text box dialog displaying msg to the agent. Submitting text chats the input string on channel as if said by the agent. The chat originates at the object's position, but uses the agent's name and UUID, so it can be heard as long as the agent is still in the region.",
 "categories": [
  "avatar_communication",
  "chat",
  "user_interface"
 ]
}
```


## functions/llToLower

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to convert.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 98,
 "native": true,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a lowercase copy of the string src. Converts all unicode characters, not just ASCII.",
 "categories": [
  "string"
 ]
}
```


## functions/llToUpper

```json
{
 "arguments": [
  {
   "src": {
    "tooltip": "Source string to convert.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 97,
 "native": true,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns an uppercase copy of the string src. Converts all unicode characters, not just ASCII.",
 "categories": [
  "string"
 ]
}
```


## functions/llTransferLindenDollars

```json
{
 "arguments": [
  {
   "destination": {
    "tooltip": "UUID of the destination avatar.",
    "type": "key"
   }
  },
  {
   "amount": {
    "tooltip": "Quantity of L$ to transfer (must be greater than 0).",
    "type": "integer"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 395,
 "return": "key",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_DEBIT"
 ],
 "tooltip": "Transfers amount of L$ from the script owner to the destination avatar, requiring the PERMISSION_DEBIT permission. Returns a key query handle matching the resulting transaction_result event.",
 "categories": [
  "money",
  "permissions"
 ]
}
```


## functions/llTransferOwnership

```json
{
 "arguments": [
  {
   "agent": {
    "tooltip": "UUID of the agent to receive ownership of the object.",
    "type": "key"
   }
  },
  {
   "flags": {
    "tooltip": "Flags controlling the transfer type (such as TRANSFER_FLAG_COPY or TRANSFER_FLAG_TAKE).",
    "type": "integer",
    "enum-semantics": "TransferOwnershipFlag"
   }
  },
  {
   "options": {
    "tooltip": "Extra options applied to the transfer (currently unused).",
    "type": "list",
    "param-semantics": "TransferOwnershipParam"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 519,
 "return": "integer",
 "enum-semantics": "TransferError",
 "sleep": 0.0,
 "tooltip": "Transfers ownership of the object (or a copy of it, depending on Flags) to the specified agent. Returns an integer indicating the success or failure of the transfer.",
 "categories": [
  "asset_permissions"
 ]
}
```


## functions/llTriggerSound

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 91,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays specified sound once at volume, centered at the object's current position but not attached (does not move with the object and cannot be stopped or adjusted). Does not affect attached sounds.",
 "categories": [
  "sound"
 ]
}
```


## functions/llTriggerSoundLimited

```json
{
 "arguments": [
  {
   "sound": {
    "tooltip": "Name of a sound in the prim's inventory, or a UUID.",
    "type": "string",
    "asset-semantics": true
   }
  },
  {
   "volume": {
    "tooltip": "Volume level to set, between 0.0 (silent) and 1.0 (loud).",
    "type": "float"
   }
  },
  {
   "top_north_east": {
    "tooltip": "Top-north-east boundary position vector in region coordinates.",
    "type": "vector"
   }
  },
  {
   "bottom_south_west": {
    "tooltip": "Bottom-south-west boundary position vector in region coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 212,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Plays the specified sound once at volume, centered at the object but not attached, restricted to the axis-aligned bounding box defined by the coordinates top_north_east and bottom_south_west.",
 "categories": [
  "sound"
 ]
}
```


## functions/llUnSit

```json
{
 "arguments": [
  {
   "id": {
    "tooltip": "UUID of the avatar to unsit.",
    "type": "key"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 220,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Forces the agent specified by id to stand up if they are sitting on the object containing the script, or are currently over land owned by the object's owner.",
 "categories": [
  "avatar",
  "sit"
 ]
}
```


## functions/llUnescapeURL

```json
{
 "arguments": [
  {
   "url": {
    "tooltip": "Escaped URL string to decode.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 308,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Returns a string representing the unescaped/decoded version of url, replacing '%20' with spaces and decoding raw UTF-8 characters.",
 "categories": [
  "web"
 ]
}
```


## functions/llUpdateCharacter

```json
{
 "arguments": [
  {
   "options": {
    "tooltip": "A list of key-value pairs specifying the character's new configuration options (takes same constants as llCreateCharacter).",
    "type": "list",
    "param-semantics": "CharacterParam",
    "ruleset": "character-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 406,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Updates settings for a pathfinding character using the parameters specified in options.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llUpdateKeyValue

```json
{
 "arguments": [
  {
   "k": {
    "tooltip": "Key of the key-value pair to update.",
    "type": "string"
   }
  },
  {
   "v": {
    "tooltip": "New value for the key-value pair.",
    "type": "string"
   }
  },
  {
   "checked": {
    "tooltip": "Boolean. If TRUE, requires the existing value to match original_value to complete the update; if FALSE, creates the key if needed.",
    "type": "integer",
    "bool-semantics": true
   }
  },
  {
   "original_value": {
    "tooltip": "String value to compare against the existing value in the datastore.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "experience": true,
 "func-id": 389,
 "return": "key",
 "sleep": 0.0,
 "tooltip": "Starts an asynchronous transaction to update the key k to value v inside the experience datastore. If checked is TRUE, the update fails with XP_ERROR_RETRY_UPDATE unless the existing value matches original_value.",
 "categories": [
  "data_storage",
  "dataserver",
  "experience",
  "experience_data"
 ]
}
```


## functions/llVecDist

```json
{
 "arguments": [
  {
   "vec_a": {
    "tooltip": "First vector.",
    "type": "vector"
   }
  },
  {
   "vec_b": {
    "tooltip": "Second vector.",
    "type": "vector"
   }
  }
 ],
 "slua-deprecated": {
  "use": "vector.magnitude",
  "reason": "It's a fastcall.",
  "selene-replace": [
   "vector.magnitude(%1 - %2)"
  ]
 },
 "energy": 10.0,
 "func-id": 14,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the undirected, non-negative distance between vectors vec_a and vec_b.",
 "categories": [
  "math",
  "math_3d",
  "vector"
 ]
}
```


## functions/llVecMag

```json
{
 "arguments": [
  {
   "vec": {
    "tooltip": "Vector to evaluate.",
    "type": "vector"
   }
  }
 ],
 "slua-deprecated": {
  "use": "vector.magnitude",
  "reason": "It's a fastcall.",
  "selene-replace": [
   "vector.magnitude(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 12,
 "pure": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns the magnitude (geometric length) of vec.",
 "categories": [
  "math",
  "math_3d",
  "vector"
 ]
}
```


## functions/llVecNorm

```json
{
 "arguments": [
  {
   "vec": {
    "tooltip": "Vector to normalize.",
    "type": "vector"
   }
  }
 ],
 "slua-deprecated": {
  "use": "vector.normalize",
  "reason": "It's a fastcall.",
  "selene-replace": [
   "vector.normalize(%1)"
  ]
 },
 "energy": 10.0,
 "func-id": 13,
 "pure": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns the normalized unit vector pointing the same direction as vec. If <0, 0, 0>, return <0, 0, 0>.",
 "categories": [
  "math",
  "math_3d",
  "vector"
 ]
}
```


## functions/llVerifyRSA

```json
{
 "arguments": [
  {
   "public_key": {
    "tooltip": "PEM-formatted public key to use for signature verification.",
    "type": "string"
   }
  },
  {
   "msg": {
    "tooltip": "Message string that was signed.",
    "type": "string"
   }
  },
  {
   "signature": {
    "tooltip": "Base64-encoded signature to verify.",
    "type": "string"
   }
  },
  {
   "algorithm": {
    "tooltip": "Cryptographic digest algorithm to use.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 540,
 "must-use": true,
 "return": "integer",
 "bool-semantics": true,
 "sleep": 0.0,
 "tooltip": "Returns TRUE if the Base64-formatted signature is verified as valid for the message msg when using the digest algorithm and public_key. Returns FALSE otherwise.",
 "categories": [
  "cryptography"
 ]
}
```


## functions/llVolumeDetect

```json
{
 "arguments": [
  {
   "detect": {
    "tooltip": "Boolean. If TRUE, enables VolumeDetect; if FALSE (default), disables it.",
    "type": "integer",
    "bool-semantics": true
   }
  }
 ],
 "energy": 10.0,
 "func-id": 248,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "If detect is TRUE, enables VolumeDetect (object becomes phantom and physical objects/avatars can pass through it). Triggers collision_start on initial intersection and collision_end when intersection stops (standard collision events are suppressed while intersecting).",
 "categories": [
  "physics",
  "sensor"
 ]
}
```


## functions/llWanderWithin

```json
{
 "arguments": [
  {
   "origin": {
    "tooltip": "Center coordinate position vector to wander about.",
    "type": "vector"
   }
  },
  {
   "dist": {
    "tooltip": "A vector specifying the maximum distance limits (half-extents) along each world-aligned axis from the origin.",
    "type": "vector"
   }
  },
  {
   "options": {
    "tooltip": "A list of WANDER_* flags and parameters to configure the wander behavior.",
    "type": "list",
    "param-semantics": "CharacterWanderWithinParam",
    "ruleset": "character-wander-within-params"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 401,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Directs a pathfinding character to wander around a central coordinate origin, restricted within the bounding distance limits of dist and configured by options.",
 "categories": [
  "pathfinding"
 ]
}
```


## functions/llWater

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position, expressed in local coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 153,
 "must-use": true,
 "return": "float",
 "sleep": 0.0,
 "tooltip": "Returns a float representing the water height directly below the prim's position offset by the vector offset.",
 "categories": [
  "region"
 ]
}
```


## functions/llWhisper

```json
{
 "arguments": [
  {
   "channel": {
    "tooltip": "Chat channel (any 32-bit signed integer value) to whisper the message on.",
    "type": "integer",
    "enum-semantics": "Channel"
   }
  },
  {
   "msg": {
    "tooltip": "Text message string to broadcast.",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 22,
 "return": "void",
 "sleep": 0.0,
 "tooltip": "Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv(\"whisper_range\"), which is 10m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.",
 "categories": [
  "avatar_communication",
  "chat",
  "script_communication"
 ]
}
```


## functions/llWind

```json
{
 "arguments": [
  {
   "offset": {
    "tooltip": "Offset relative to the prim's position, expressed in local coordinates.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 44,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a vector representing the wind velocity at the prim's position offset by the vector offset.",
 "categories": [
  "region"
 ]
}
```


## functions/llWorldPosToHUD

```json
{
 "arguments": [
  {
   "world_pos": {
    "tooltip": "World-frame position vector to project into HUD space.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 547,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "requires-permission": [
  "PERMISSION_TRACK_CAMERA"
 ],
 "tooltip": "Returns the local position vector that places the center of the HUD object directly over the world coordinate world_pos as viewed by the current camera. Requires the PERMISSION_TRACK_CAMERA runtime permission.",
 "categories": [
  "avatar",
  "camera",
  "permissions",
  "user_interface"
 ]
}
```


## functions/llXorBase64

```json
{
 "arguments": [
  {
   "str1": {
    "tooltip": "First Base64 string.",
    "type": "string"
   }
  },
  {
   "str2": {
    "tooltip": "Second Base64 string (will repeat if shorter than str1).",
    "type": "string"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 522,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Correctly performs a bitwise exclusive OR (XOR) on Base64 strings str1 and str2, returning the result as a Base64 string. The string str2 repeats if it is shorter than str1.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llXorBase64Strings

```json
{
 "arguments": [
  {
   "str1": {
    "tooltip": "First Base64 string.",
    "type": "string"
   }
  },
  {
   "str2": {
    "tooltip": "Second Base64 string (will repeat if shorter than str1).",
    "type": "string"
   }
  }
 ],
 "deprecated": {
  "use": "ll.XorBase64",
  "selene-replace": [
   "ll.XorBase64(%1, %2)"
  ]
 },
 "energy": 10.0,
 "func-id": 262,
 "pure": true,
 "return": "string",
 "sleep": 0.3,
 "tooltip": "Deprecated (use llXorBase64 instead). Retained for backwards compatibility. Incorrectly performs a bitwise exclusive OR (XOR) on Base64 strings str1 and str2.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llXorBase64StringsCorrect

```json
{
 "arguments": [
  {
   "str1": {
    "tooltip": "First Base64 string.",
    "type": "string"
   }
  },
  {
   "str2": {
    "tooltip": "Second Base64 string (will repeat if shorter than str1).",
    "type": "string"
   }
  }
 ],
 "deprecated": {
  "use": "ll.XorBase64",
  "selene-replace": [
   "ll.XorBase64(%1, %2)"
  ]
 },
 "energy": 10.0,
 "func-id": 319,
 "pure": true,
 "return": "string",
 "sleep": 0.0,
 "tooltip": "Deprecated (use llXorBase64 instead). Correctly performs (unless nulls are present) a bitwise exclusive OR (XOR) on Base64 strings str1 and str2.",
 "categories": [
  "data_conversion"
 ]
}
```


## functions/llsRGB2Linear

```json
{
 "arguments": [
  {
   "color": {
    "tooltip": "Color vector in the sRGB colorspace to convert.",
    "type": "vector"
   }
  }
 ],
 "energy": 10.0,
 "func-id": 716,
 "must-use": true,
 "return": "vector",
 "sleep": 0.0,
 "tooltip": "Returns a linear RGB colorspace vector converted from the sRGB colorspace argument.",
 "categories": [
  "data_conversion",
  "math",
  "prim_appearance",
  "vector"
 ]
}
```


# Section: types (8 entries)


## types/float

```json
{
 "tooltip": "32 bit floating point value.\\nThe range is 1.175494351E-38 to 3.402823466E+38."
}
```


## types/integer

```json
{
 "tooltip": "32 bit integer value.\\n−2,147,483,648 and +2,147,483,647 (that is 0x80000000 to 0x7FFFFFFF in hex)."
}
```


## types/key

```json
{
 "tooltip": "A 128 bit unique identifier (UUID).\\nThe key is represented as hexidecimal characters (A-F and 0-9), grouped into sections (8,4,4,4,12 characters) and separated by hyphens (for a total of 36 characters). e.g. \"A822FF2B-FF02-461D-B45D-DCD10A2DE0C2\"."
}
```


## types/list

```json
{
 "tooltip": "A collection of other data types.\\nLists are signified by square brackets surrounding their elements; the elements inside are separated by commas. e.g. [0, 1, 2, 3, 4] or [\"Yes\", \"No\", \"Perhaps\"]."
}
```


## types/quaternion

```json
{
 "private": true,
 "tooltip": "Quaternion type is a left over from way back when LSL was created. It was later renamed to <rotation> to make it more user friendly, but it appears someone forgot to remove it ;-)"
}
```


## types/rotation

```json
{
 "tooltip": "Rotation type is one of several ways to represent an orientation in 3D.\\nIt is a mathematical object called a quaternion. You can think of a quaternion as four numbers (x, y, z, w), three of which represent the direction an object is facing and a fourth that represents the object's banking left or right around that direction."
}
```


## types/string

```json
{
 "tooltip": "Text data.\\nThe editor accepts UTF-8 encoded text."
}
```


## types/vector

```json
{
 "tooltip": "A vector is a data type that contains a set of three float values.\\nVectors are used to represent colors (RGB), positions, and directions/velocities."
}
```


# Section: controls (11 entries)


## controls/default

```json
{
 "tooltip": "All scripts must have a default state, which is the first state entered when the script starts.\nIf another state is defined before the default state, the compiler will report a syntax error."
}
```


## controls/do

```json
{
 "tooltip": "do / while loop\\ndo {\\n...\\n} while (<condition>);"
}
```


## controls/else

```json
{
 "tooltip": "if / else block\\nif (<condition>) {\\n...\\n[} else [if (<condition>) {\\n...]]\\n}"
}
```


## controls/event

```json
{
 "deprecated": true,
 "tooltip": "Undefined reserved word."
}
```


## controls/for

```json
{
 "tooltip": "for loop\\nfor (<initializer>; <condition>; <post-iteration-statement>)\\n{ ...\\n}"
}
```


## controls/if

```json
{
 "tooltip": "if / else block\\nif (<condition>) {\\n...\\n[} else [if (<condition>) {\\n...]]\\n}"
}
```


## controls/jump

```json
{
 "tooltip": "jump statement\\njump <label>"
}
```


## controls/print

```json
{
 "tooltip": "Say the given variable to the owner. Only works on 2025 VM."
}
```


## controls/return

```json
{
 "tooltip": "Leave current event or function.\\nreturn [<variable>];\\nOptionally pass back a variable's value, from a function."
}
```


## controls/state

```json
{
 "tooltip": "state <target>\\nIf the target state is not the same as the current one, change to the target state."
}
```


## controls/while

```json
{
 "tooltip": "while loop\\nwhile (<condition>) {\\n...\\n}"
}
```


# Section: builder-rulesets (17 entries)


## builder-rulesets/attached-list-filter-params

```json
{
 "type": "table",
 "enum": "AttachedListFilterParam",
 "lua-type": "AttachedListFilterParams",
 "flag-enum": "AttachedListFilterFlag",
 "flag-field": "flags"
}
```


## builder-rulesets/camera-params

```json
{
 "type": "table",
 "enum": "CameraParam",
 "lua-type": "CameraParams"
}
```


## builder-rulesets/character-navigate-params

```json
{
 "type": "table",
 "enum": "CharacterNavigateParam",
 "lua-type": "CharacterNavigateParams"
}
```


## builder-rulesets/character-params

```json
{
 "type": "table",
 "enum": "CharacterParam",
 "lua-type": "CharacterParams"
}
```


## builder-rulesets/character-patrol-points-params

```json
{
 "type": "table",
 "enum": "CharacterPatrolPointsParam",
 "lua-type": "CharacterPatrolPointsParams"
}
```


## builder-rulesets/character-pursue-params

```json
{
 "type": "table",
 "enum": "CharacterPursueParam",
 "lua-type": "CharacterPursueParams"
}
```


## builder-rulesets/character-wander-within-params

```json
{
 "type": "table",
 "enum": "CharacterWanderWithinParam",
 "lua-type": "CharacterWanderWithinParams"
}
```


## builder-rulesets/get-closest-nav-point-params

```json
{
 "type": "table",
 "enum": "GetClosestNavPointParam",
 "lua-type": "GetClosestNavPointParams"
}
```


## builder-rulesets/get-static-path-params

```json
{
 "type": "table",
 "enum": "GetStaticPathParam",
 "lua-type": "GetStaticPathParams"
}
```


## builder-rulesets/give-agent-inventory-params

```json
{
 "type": "table",
 "enum": "GiveAgentInventoryParam",
 "flag-enum": "GiveAgentInventoryFlag",
 "flag-field": "flags",
 "lua-type": "GiveAgentInventoryParams"
}
```


## builder-rulesets/gltf-overrides

```json
{
 "type": "table",
 "enum": "GLTFOverride",
 "filler-tokens": [
  "base"
 ],
 "lua-type": "GltfOverrides"
}
```


## builder-rulesets/http-request-params

```json
{
 "type": "table",
 "enum": "HTTPRequestParam",
 "filler-tokens": [
  "http"
 ],
 "lua-type": "HttpRequestParams"
}
```


## builder-rulesets/keyframed-motion-params

```json
{
 "type": "table",
 "enum": "KeyframedMotionParam",
 "flag-enum": "KeyframedMotionData",
 "flag-field": "data",
 "lua-type": "KeyframedMotionParams"
}
```


## builder-rulesets/parcel-sale

```json
{
 "type": "table",
 "enum": "ParcelSaleParam",
 "lua-type": "ParcelSaleParams"
}
```


## builder-rulesets/particle-params

```json
{
 "type": "table",
 "enum": "ParticleParam",
 "filler-tokens": [
  "part",
  "src"
 ],
 "flag-enum": "ParticleFlag",
 "flag-field": "flags",
 "flag-mask": "_MASK",
 "lua-type": "ParticleParams"
}
```


## builder-rulesets/prim-media-params

```json
{
 "type": "table",
 "enum": "PrimMediaParam",
 "lua-type": "PrimMediaParams"
}
```


## builder-rulesets/prim-params

```json
{
 "type": "builder",
 "enum": "PrimParam",
 "rules": {
  "LINK_TARGET": {
   "method-name": "targetLink",
   "params": [
    [
     "link",
     "link_target"
    ]
   ]
  },
  "MATERIAL": {
   "method-name": "physicsMaterial",
   "params": [
    [
     "integer",
     "flag"
    ]
   ]
  },
  "PHYSICS": {
   "method-name": "physical",
   "params": [
    [
     "boolean",
     "enabled"
    ]
   ]
  },
  "TEMP_ON_REZ": {
   "method-name": "temporary",
   "params": [
    [
     "boolean",
     "enabled"
    ]
   ]
  },
  "PHANTOM": {
   "params": [
    [
     "boolean",
     "enabled"
    ]
   ]
  },
  "POSITION": {
   "method-name": "pos",
   "params": [
    [
     "vector",
     "position"
    ]
   ]
  },
  "SIZE": {
   "params": [
    [
     "vector",
     "size"
    ]
   ]
  },
  "ROTATION": {
   "method-name": "rot",
   "params": [
    [
     "rotation",
     "rot"
    ]
   ]
  },
  "TYPE": {
   "params": [
    [
     "integer",
     "prim_type"
    ]
   ],
   "variants-on": "prim_type",
   "variant-enum": "PrimType",
   "variants": [
    {
     "applies-to": [
      "BOX",
      "CYLINDER",
      "PRISM"
     ],
     "params": [
      [
       "integer",
       "hole_type"
      ],
      [
       "vector",
       "cut"
      ],
      [
       "float",
       "hollow"
      ],
      [
       "vector",
       "twist"
      ],
      [
       "vector",
       "top_size"
      ],
      [
       "vector",
       "top_shear"
      ]
     ]
    },
    {
     "applies-to": [
      "SPHERE"
     ],
     "params": [
      [
       "integer",
       "hole_type"
      ],
      [
       "vector",
       "cut"
      ],
      [
       "float",
       "hollow"
      ],
      [
       "vector",
       "twist"
      ],
      [
       "vector",
       "dimple"
      ]
     ]
    },
    {
     "applies-to": [
      "TORUS",
      "TUBE",
      "RING"
     ],
     "params": [
      [
       "integer",
       "hole_type"
      ],
      [
       "vector",
       "cut"
      ],
      [
       "float",
       "hollow"
      ],
      [
       "vector",
       "twist"
      ],
      [
       "vector",
       "hole_size"
      ],
      [
       "vector",
       "top_shear"
      ],
      [
       "vector",
       "advanced_cut"
      ],
      [
       "vector",
       "taper"
      ],
      [
       "float",
       "revolutions"
      ],
      [
       "float",
       "radius_offset"
      ],
      [
       "float",
       "skew"
      ]
     ]
    },
    {
     "applies-to": [
      "SCULPT"
     ],
     "params": [
      [
       "asset",
       "texture"
      ],
      [
       "integer",
       "sculpt_type"
      ]
     ]
    }
   ]
  },
  "TEXTURE": {
   "face-target": true,
   "params": [
    [
     "asset",
     "texture"
    ],
    [
     "vector",
     "repeats"
    ],
    [
     "vector",
     "offsets"
    ],
    [
     "float",
     "rotation_in_radians"
    ]
   ]
  },
  "COLOR": {
   "face-target": true,
   "params": [
    [
     "vector",
     "color"
    ],
    [
     "float",
     "alpha"
    ]
   ]
  },
  "BUMP_SHINY": {
   "face-target": true,
   "method-name": "shinyBump",
   "params": [
    [
     "integer",
     "shiny"
    ],
    [
     "integer",
     "bump"
    ]
   ]
  },
  "FULLBRIGHT": {
   "face-target": true,
   "params": [
    [
     "boolean",
     "enabled"
    ]
   ]
  },
  "FLEXIBLE": {
   "params": [
    [
     "boolean",
     "enabled"
    ],
    [
     "integer",
     "softness"
    ],
    [
     "float",
     "gravity"
    ],
    [
     "float",
     "friction"
    ],
    [
     "float",
     "wind"
    ],
    [
     "float",
     "tension"
    ],
    [
     "vector",
     "force"
    ]
   ]
  },
  "TEXGEN": {
   "face-target": true,
   "params": [
    [
     "integer",
     "mode"
    ]
   ]
  },
  "POINT_LIGHT": {
   "params": [
    [
     "boolean",
     "enabled"
    ],
    [
     "vector",
     "linear_color"
    ],
    [
     "float",
     "intensity"
    ],
    [
     "float",
     "radius"
    ],
    [
     "float",
     "falloff"
    ]
   ]
  },
  "GLOW": {
   "face-target": true,
   "params": [
    [
     "float",
     "intensity"
    ]
   ]
  },
  "TEXT": {
   "params": [
    [
     "string",
     "text"
    ],
    [
     "vector",
     "color"
    ],
    [
     "float",
     "alpha"
    ]
   ]
  },
  "NAME": {
   "params": [
    [
     "string",
     "name"
    ]
   ]
  },
  "DESC": {
   "method-name": "description",
   "params": [
    [
     "string",
     "description"
    ]
   ]
  },
  "ROT_LOCAL": {
   "params": [
    [
     "rotation",
     "rot"
    ]
   ]
  },
  "PHYSICS_SHAPE_TYPE": {
   "params": [
    [
     "integer",
     "shape_type"
    ]
   ]
  },
  "OMEGA": {
   "params": [
    [
     "vector",
     "axis"
    ],
    [
     "float",
     "spinrate"
    ],
    [
     "float",
     "gain"
    ]
   ]
  },
  "POS_LOCAL": {
   "params": [
    [
     "vector",
     "position"
    ]
   ]
  },
  "SLICE": {
   "params": [
    [
     "vector",
     "slice"
    ]
   ]
  },
  "SPECULAR": {
   "face-target": true,
   "params": [
    [
     "asset",
     "texture"
    ],
    [
     "vector",
     "repeats"
    ],
    [
     "vector",
     "offsets"
    ],
    [
     "float",
     "rotation_in_radians"
    ],
    [
     "vector",
     "color"
    ],
    [
     "integer",
     "glossiness"
    ],
    [
     "integer",
     "environment"
    ]
   ]
  },
  "NORMAL": {
   "face-target": true,
   "params": [
    [
     "asset",
     "texture"
    ],
    [
     "vector",
     "repeats"
    ],
    [
     "vector",
     "offsets"
    ],
    [
     "float",
     "rotation_in_radians"
    ]
   ]
  },
  "ALPHA_MODE": {
   "face-target": true,
   "params": [
    [
     "integer",
     "alpha_mode"
    ],
    [
     "integer",
     "mask_cutoff"
    ]
   ]
  },
  "ALLOW_UNSIT": {
   "params": [
    [
     "boolean",
     "allowed"
    ]
   ]
  },
  "SCRIPTED_SIT_ONLY": {
   "params": [
    [
     "boolean",
     "enabled"
    ]
   ]
  },
  "SIT_TARGET": {
   "params": [
    [
     "boolean",
     "active"
    ],
    [
     "vector",
     "offset"
    ],
    [
     "rotation",
     "rot"
    ]
   ]
  },
  "PROJECTOR": {
   "params": [
    [
     "string",
     "texture"
    ],
    [
     "float",
     "fov"
    ],
    [
     "float",
     "focus"
    ],
    [
     "float",
     "ambiance"
    ]
   ]
  },
  "CLICK_ACTION": {
   "params": [
    [
     "integer",
     "action"
    ]
   ]
  },
  "REFLECTION_PROBE": {
   "params": [
    [
     "boolean",
     "enabled"
    ],
    [
     "float",
     "ambiance"
    ],
    [
     "float",
     "clip_distance"
    ],
    [
     "integer",
     "flags"
    ]
   ]
  },
  "GLTF_NORMAL": {
   "face-target": true,
   "nullable": true,
   "params": [
    [
     "asset",
     "texture"
    ],
    [
     "vector",
     "repeats"
    ],
    [
     "vector",
     "offsets"
    ],
    [
     "float",
     "rotation_in_radians"
    ]
   ]
  },
  "GLTF_EMISSIVE": {
   "face-target": true,
   "nullable": true,
   "params": [
    [
     "asset",
     "texture"
    ],
    [
     "vector",
     "repeats"
    ],
    [
     "vector",
     "offsets"
    ],
    [
     "float",
     "rotation_in_radians"
    ],
    [
     "vector",
     "linear_emissive_tint"
    ]
   ]
  },
  "GLTF_METALLIC_ROUGHNESS": {
   "face-target": true,
   "nullable": true,
   "params": [
    [
     "asset",
     "texture"
    ],
    [
     "vector",
     "repeats"
    ],
    [
     "vector",
     "offsets"
    ],
    [
     "float",
     "rotation_in_radians"
    ],
    [
     "float",
     "metallic_factor"
    ],
    [
     "float",
     "roughness_factor"
    ]
   ]
  },
  "GLTF_BASE_COLOR": {
   "face-target": true,
   "nullable": true,
   "params": [
    [
     "asset",
     "texture"
    ],
    [
     "vector",
     "repeats"
    ],
    [
     "vector",
     "offsets"
    ],
    [
     "float",
     "rotation_in_radians"
    ],
    [
     "vector",
     "linear_color"
    ],
    [
     "float",
     "alpha"
    ],
    [
     "integer",
     "gltf_alpha_mode"
    ],
    [
     "float",
     "alpha_mask_cutoff"
    ],
    [
     "boolean",
     "double_sided"
    ]
   ]
  },
  "RENDER_MATERIAL": {
   "face-target": true,
   "params": [
    [
     "asset",
     "render_material"
    ]
   ]
  },
  "SIT_FLAGS": {
   "params": [
    [
     "integer",
     "flags"
    ]
   ]
  },
  "DAMAGE": {
   "params": [
    [
     "float",
     "damage"
    ],
    [
     "integer",
     "damage_type"
    ]
   ]
  },
  "HEALTH": {
   "params": [
    [
     "float",
     "health"
    ]
   ]
  },
  "COLLISION_SOUND": {
   "params": [
    [
     "asset",
     "sound"
    ],
    [
     "float",
     "volume"
    ]
   ]
  }
 }
}
```
