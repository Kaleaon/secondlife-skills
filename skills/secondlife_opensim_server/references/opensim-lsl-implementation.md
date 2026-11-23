# LSL Functions as Implemented by OpenSim (generated from opensim/opensim source)

Extracted 474 ll* signatures from OpenSim's LSL_Api implementation. Where a function is missing here but exists in the canonical lsl-definitions reference, OpenSim may implement it in another partial class file or not at all. Behaviour differences between this implementation and Linden Lab's are the porting risk when moving scripts between grids.


## llAbs

```csharp
LSL_Integer llAbs(LSL_Integer i)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAcos

```csharp
LSL_Float llAcos(LSL_Float val)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAddToLandBanList

```csharp
void llAddToLandBanList(LSL_Key avatar, LSL_Float hours)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAddToLandPassList

```csharp
void llAddToLandPassList(LSL_Key avatar, LSL_Float hours)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAdjustSoundVolume

```csharp
void llAdjustSoundVolume(LSL_Float volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAllowInventoryDrop

```csharp
void llAllowInventoryDrop(LSL_Integer add)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAngleBetween

```csharp
LSL_Float llAngleBetween(LSL_Rotation a, LSL_Rotation b)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llApplyImpulse

```csharp
void llApplyImpulse(LSL_Vector force, LSL_Integer local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llApplyRotationalImpulse

```csharp
void llApplyRotationalImpulse(LSL_Vector force, int local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAsin

```csharp
LSL_Float llAsin(LSL_Float val)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAtan2

```csharp
LSL_Float llAtan2(LSL_Float y, LSL_Float x)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAttachToAvatar

```csharp
void llAttachToAvatar(LSL_Integer attachment)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAttachToAvatarTemp

```csharp
void llAttachToAvatarTemp(LSL_Integer attachment)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAvatarOnLinkSitTarget

```csharp
LSL_Key llAvatarOnLinkSitTarget(LSL_Integer linknum)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAvatarOnSitTarget

```csharp
LSL_Key llAvatarOnSitTarget()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAxes2Rot

```csharp
LSL_Rotation llAxes2Rot(LSL_Vector fwd, LSL_Vector left, LSL_Vector up)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llAxisAngle2Rot

```csharp
LSL_Rotation llAxisAngle2Rot(LSL_Vector axis, double angle)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llBase64ToInteger

```csharp
LSL_Integer llBase64ToInteger(string str)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llBase64ToString

```csharp
LSL_String llBase64ToString(string str)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llBreakAllLinks

```csharp
void llBreakAllLinks()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llBreakLink

```csharp
void llBreakLink(int linknum)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCSV2List

```csharp
LSL_List llCSV2List(string src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCastRay

```csharp
LSL_List llCastRay(LSL_Vector start, LSL_Vector end, LSL_List options)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCastRayV3

```csharp
LSL_List llCastRayV3(LSL_Vector start, LSL_Vector end, LSL_List options)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Implementation/LSL_Api.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCeil

```csharp
LSL_Integer llCeil(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llChar

```csharp
LSL_String llChar(LSL_Integer unicode)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llClearCameraParams

```csharp
void llClearCameraParams()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llClearLinkMedia

```csharp
LSL_Integer llClearLinkMedia(LSL_Integer link, LSL_Integer face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llClearPrimMedia

```csharp
LSL_Integer llClearPrimMedia(LSL_Integer face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCloseRemoteDataChannel

```csharp
void llCloseRemoteDataChannel(string channel)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCloud

```csharp
LSL_Float llCloud(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCollisionFilter

```csharp
void llCollisionFilter(LSL_String name, LSL_Key id, LSL_Integer accept)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCollisionSound

```csharp
void llCollisionSound(LSL_String impact_sound, LSL_Float impact_volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCollisionSprite

```csharp
void llCollisionSprite(LSL_String impact_sprite)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llComputeHash

```csharp
LSL_String llComputeHash(LSL_String message, LSL_String algo)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCos

```csharp
LSL_Float llCos(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llCreateLink

```csharp
void llCreateLink(LSL_Key target, LSL_Integer parent)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDeleteSubList

```csharp
LSL_List llDeleteSubList(LSL_List src, int start, int end)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDeleteSubString

```csharp
LSL_String llDeleteSubString(string src, int start, int end)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDerezObject

```csharp
LSL_Integer llDerezObject(LSL_Key objectUUID, LSL_Integer flag)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetachFromAvatar

```csharp
void llDetachFromAvatar()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedGrab

```csharp
LSL_Vector llDetectedGrab(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedGroup

```csharp
LSL_Integer llDetectedGroup(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedKey

```csharp
LSL_Key llDetectedKey(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedLinkNumber

```csharp
LSL_Integer llDetectedLinkNumber(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedName

```csharp
LSL_String llDetectedName(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedOwner

```csharp
LSL_Key llDetectedOwner(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedPos

```csharp
LSL_Vector llDetectedPos(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedRot

```csharp
LSL_Rotation llDetectedRot(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedTouchBinormal

```csharp
LSL_Vector llDetectedTouchBinormal(int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedTouchFace

```csharp
LSL_Integer llDetectedTouchFace(int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedTouchNormal

```csharp
LSL_Vector llDetectedTouchNormal(int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedTouchPos

```csharp
LSL_Vector llDetectedTouchPos(int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedTouchST

```csharp
LSL_Vector llDetectedTouchST(int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedTouchUV

```csharp
LSL_Vector llDetectedTouchUV(int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedType

```csharp
LSL_Integer llDetectedType(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDetectedVel

```csharp
LSL_Vector llDetectedVel(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDialog

```csharp
void llDialog(LSL_Key avatar, LSL_String message, LSL_List buttons, int chat_channel)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDie

```csharp
void llDie()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llDumpList2String

```csharp
LSL_String llDumpList2String(LSL_List src, string seperator)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llEdgeOfWorld

```csharp
LSL_Integer llEdgeOfWorld(LSL_Vector pos, LSL_Vector dir)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llEjectFromLand

```csharp
void llEjectFromLand(LSL_Key pest)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llEmail

```csharp
void llEmail(string address, string subject, string message)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llEscapeURL

```csharp
LSL_String llEscapeURL(string url)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llEuler2Rot

```csharp
LSL_Rotation llEuler2Rot(LSL_Vector v)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llFabs

```csharp
LSL_Float llFabs(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llFloor

```csharp
LSL_Integer llFloor(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llForceMouselook

```csharp
void llForceMouselook(int mouselook)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llFrand

```csharp
LSL_Float llFrand(double mag)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGenerateKey

```csharp
LSL_Key llGenerateKey()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAccel

```csharp
LSL_Vector llGetAccel()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAgentInfo

```csharp
LSL_Integer llGetAgentInfo(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAgentLanguage

```csharp
LSL_String llGetAgentLanguage(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAgentList

```csharp
LSL_List llGetAgentList(LSL_Integer scope, LSL_List options)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAgentSize

```csharp
LSL_Vector llGetAgentSize(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAlpha

```csharp
LSL_Float llGetAlpha(int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAndResetTime

```csharp
LSL_Float llGetAndResetTime()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAnimation

```csharp
LSL_String llGetAnimation(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAnimationList

```csharp
LSL_List llGetAnimationList(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAnimationOverride

```csharp
LSL_String llGetAnimationOverride(LSL_String anim_state)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAttached

```csharp
LSL_Integer llGetAttached()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetAttachedList

```csharp
LSL_List llGetAttachedList(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetBoundingBox

```csharp
LSL_List llGetBoundingBox(string obj)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetCameraAspect

```csharp
LSL_Float llGetCameraAspect()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetCameraFOV

```csharp
LSL_Float llGetCameraFOV()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetCameraPos

```csharp
LSL_Vector llGetCameraPos()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetCameraRot

```csharp
LSL_Rotation llGetCameraRot()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetCenterOfMass

```csharp
LSL_Vector llGetCenterOfMass()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetColor

```csharp
LSL_Vector llGetColor(int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetCreator

```csharp
LSL_Key llGetCreator()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetDate

```csharp
LSL_String llGetDate()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetDayLength

```csharp
LSL_Integer llGetDayLength()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetDayOffset

```csharp
LSL_Integer llGetDayOffset()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetDisplayName

```csharp
LSL_String llGetDisplayName(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetEnergy

```csharp
LSL_Float llGetEnergy()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetEnv

```csharp
LSL_String llGetEnv(LSL_String name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetForce

```csharp
LSL_Vector llGetForce()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetFreeMemory

```csharp
LSL_Integer llGetFreeMemory()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetFreeURLs

```csharp
LSL_Integer llGetFreeURLs()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetGMTclock

```csharp
LSL_Float llGetGMTclock()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetGeometricCenter

```csharp
LSL_Vector llGetGeometricCenter()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetHTTPHeader

```csharp
LSL_String llGetHTTPHeader(LSL_Key request_id, string header)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetHealth

```csharp
LSL_Float llGetHealth(LSL_String key)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryAcquireTime

```csharp
LSL_String llGetInventoryAcquireTime(string item)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryCreator

```csharp
LSL_Key llGetInventoryCreator(string item)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryDesc

```csharp
LSL_String llGetInventoryDesc(string name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryKey

```csharp
LSL_Key llGetInventoryKey(string name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryName

```csharp
LSL_String llGetInventoryName(int type, int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryNumber

```csharp
LSL_Integer llGetInventoryNumber(int type)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryPermMask

```csharp
LSL_Integer llGetInventoryPermMask(string item, int mask)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetInventoryType

```csharp
LSL_Integer llGetInventoryType(string name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetKey

```csharp
LSL_Key llGetKey()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLandOwnerAt

```csharp
LSL_Key llGetLandOwnerAt(LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLinkKey

```csharp
LSL_Key llGetLinkKey(int linknum)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLinkMedia

```csharp
LSL_List llGetLinkMedia(LSL_Integer link, LSL_Integer face, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLinkName

```csharp
LSL_String llGetLinkName(int linknum)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLinkNumber

```csharp
LSL_Integer llGetLinkNumber()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLinkNumberOfSides

```csharp
LSL_Integer llGetLinkNumberOfSides(LSL_Integer link)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLinkPrimitiveParams

```csharp
LSL_List llGetLinkPrimitiveParams(int linknum, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLinkSitFlags

```csharp
LSL_Integer llGetLinkSitFlags(LSL_Integer linknum)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetListEntryType

```csharp
LSL_Integer llGetListEntryType(LSL_List src, int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetListLength

```csharp
LSL_Integer llGetListLength(LSL_List src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLocalPos

```csharp
LSL_Vector llGetLocalPos()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetLocalRot

```csharp
LSL_Rotation llGetLocalRot()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetMass

```csharp
LSL_Float llGetMass()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetMassMKS

```csharp
LSL_Float llGetMassMKS()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetMaxScaleFactor

```csharp
LSL_Float llGetMaxScaleFactor()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetMemoryLimit

```csharp
LSL_Integer llGetMemoryLimit()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetMinScaleFactor

```csharp
LSL_Float llGetMinScaleFactor()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetMoonDirection

```csharp
LSL_Vector llGetMoonDirection()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetMoonRotation

```csharp
LSL_Rotation llGetMoonRotation()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetNextEmail

```csharp
void llGetNextEmail(string address, string subject)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetNotecardLine

```csharp
LSL_Key llGetNotecardLine(string name, int line)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetNotecardLineSync

```csharp
LSL_String llGetNotecardLineSync(string name, int line)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetNumberOfNotecardLines

```csharp
LSL_Key llGetNumberOfNotecardLines(string name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetNumberOfPrims

```csharp
LSL_Integer llGetNumberOfPrims()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetNumberOfSides

```csharp
LSL_Integer llGetNumberOfSides()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectAnimationNames

```csharp
LSL_List llGetObjectAnimationNames()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectDesc

```csharp
LSL_String llGetObjectDesc()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectDetails

```csharp
LSL_List llGetObjectDetails(LSL_Key id, LSL_List args)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectLinkKey

```csharp
LSL_Key llGetObjectLinkKey(LSL_Key objectid, int linknum)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectMass

```csharp
LSL_Float llGetObjectMass(string id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectName

```csharp
LSL_String llGetObjectName()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectPermMask

```csharp
LSL_Integer llGetObjectPermMask(int mask)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetObjectPrimCount

```csharp
LSL_Integer llGetObjectPrimCount(LSL_Key object_id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetOmega

```csharp
LSL_Vector llGetOmega()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetOwner

```csharp
LSL_Key llGetOwner()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetOwnerKey

```csharp
LSL_Key llGetOwnerKey(string id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetParcelDetails

```csharp
LSL_List llGetParcelDetails(LSL_Vector pos, LSL_List param)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetParcelFlags

```csharp
LSL_Integer llGetParcelFlags(LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetParcelMaxPrims

```csharp
LSL_Integer llGetParcelMaxPrims(LSL_Vector pos, int sim_wide)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetParcelMusicURL

```csharp
LSL_String llGetParcelMusicURL()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetParcelPrimCount

```csharp
LSL_Integer llGetParcelPrimCount(LSL_Vector pos, int category, int sim_wide)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetParcelPrimOwners

```csharp
LSL_List llGetParcelPrimOwners(LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetPermissions

```csharp
LSL_Integer llGetPermissions()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetPermissionsKey

```csharp
LSL_Key llGetPermissionsKey()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetPhysicsMaterial

```csharp
LSL_List llGetPhysicsMaterial()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetPos

```csharp
LSL_Vector llGetPos()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetPrimMediaParams

```csharp
LSL_List llGetPrimMediaParams(int face, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetPrimitiveParams

```csharp
LSL_List llGetPrimitiveParams(LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionAgentCount

```csharp
LSL_Integer llGetRegionAgentCount()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionCorner

```csharp
LSL_Vector llGetRegionCorner()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionDayLength

```csharp
LSL_Integer llGetRegionDayLength()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionDayOffset

```csharp
LSL_Integer llGetRegionDayOffset()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionFPS

```csharp
LSL_Float llGetRegionFPS()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionFlags

```csharp
LSL_Integer llGetRegionFlags()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionMoonDirection

```csharp
LSL_Vector llGetRegionMoonDirection()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionMoonRotation

```csharp
LSL_Rotation llGetRegionMoonRotation()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionName

```csharp
LSL_String llGetRegionName()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionSunDirection

```csharp
LSL_Vector llGetRegionSunDirection()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionSunRotation

```csharp
LSL_Rotation llGetRegionSunRotation()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRegionTimeDilation

```csharp
LSL_Float llGetRegionTimeDilation()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRenderMaterial

```csharp
LSL_String llGetRenderMaterial(LSL_Integer face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRootPosition

```csharp
LSL_Vector llGetRootPosition()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRootRotation

```csharp
LSL_Rotation llGetRootRotation()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetRot

```csharp
LSL_Rotation llGetRot()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetSPMaxMemory

```csharp
LSL_Integer llGetSPMaxMemory()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetScale

```csharp
LSL_Vector llGetScale()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetScriptName

```csharp
LSL_String llGetScriptName()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetScriptState

```csharp
LSL_Integer llGetScriptState(string name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetSimStats

```csharp
LSL_Float llGetSimStats(LSL_Integer stat_type)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetSimulatorHostname

```csharp
LSL_String llGetSimulatorHostname()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetStartParameter

```csharp
LSL_Integer llGetStartParameter()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetStartString

```csharp
LSL_String llGetStartString()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Implementation/LSL_Api.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetStatus

```csharp
LSL_Integer llGetStatus(int status)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetSubString

```csharp
LSL_String llGetSubString(string src, int start, int end)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetSunDirection

```csharp
LSL_Vector llGetSunDirection()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetSunRotation

```csharp
LSL_Rotation llGetSunRotation()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTexture

```csharp
LSL_String llGetTexture(int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTextureOffset

```csharp
LSL_Vector llGetTextureOffset(int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTextureRot

```csharp
LSL_Float llGetTextureRot(int side)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTextureScale

```csharp
LSL_Vector llGetTextureScale(int side)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTime

```csharp
LSL_Float llGetTime()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTimeOfDay

```csharp
LSL_Float llGetTimeOfDay()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTimestamp

```csharp
LSL_String llGetTimestamp()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetTorque

```csharp
LSL_Vector llGetTorque()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetUnixTime

```csharp
LSL_Integer llGetUnixTime()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetUsedMemory

```csharp
LSL_Integer llGetUsedMemory()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetUsername

```csharp
LSL_String llGetUsername(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetVel

```csharp
LSL_Vector llGetVel()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetVisualParams

```csharp
LSL_List llGetVisualParams(string id, LSL_List visualparams)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGetWallclock

```csharp
LSL_Float llGetWallclock()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGiveInventory

```csharp
void llGiveInventory(LSL_Key destination, LSL_String inventory)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGiveInventoryList

```csharp
void llGiveInventoryList(LSL_Key destination, LSL_String category, LSL_List inventory)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGiveMoney

```csharp
LSL_Integer llGiveMoney(LSL_Key destination, LSL_Integer amount)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGodLikeRezObject

```csharp
void llGodLikeRezObject(LSL_String inventory, LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGround

```csharp
LSL_Float llGround(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGroundContour

```csharp
LSL_Vector llGroundContour(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGroundNormal

```csharp
LSL_Vector llGroundNormal(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGroundRepel

```csharp
void llGroundRepel(double height, int water, double tau)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llGroundSlope

```csharp
LSL_Vector llGroundSlope(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llHMAC

```csharp
LSL_String llHMAC(LSL_String private_key, LSL_String message, LSL_String algo)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llHTTPRequest

```csharp
LSL_Key llHTTPRequest(LSL_String url, LSL_List parameters, LSL_String body)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llHTTPResponse

```csharp
void llHTTPResponse(LSL_Key id, int status, LSL_String body)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llHash

```csharp
LSL_Integer llHash(LSL_String s)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llInsertString

```csharp
LSL_String llInsertString(LSL_String dst, int position, LSL_String src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llInstantMessage

```csharp
void llInstantMessage(LSL_String user, LSL_String message)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llIntegerToBase64

```csharp
LSL_String llIntegerToBase64(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llIsFriend

```csharp
LSL_Integer llIsFriend(LSL_Key agent_id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llIsLinkGLTFMaterial

```csharp
LSL_Integer llIsLinkGLTFMaterial(LSL_Integer linknum, LSL_Integer face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llJson2List

```csharp
LSL_List llJson2List(LSL_String json)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llJsonGetValue

```csharp
LSL_String llJsonGetValue(LSL_String json, LSL_List specifiers)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llJsonSetValue

```csharp
LSL_String llJsonSetValue(LSL_String json, LSL_List specifiers, LSL_String value)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llJsonValueType

```csharp
LSL_String llJsonValueType(LSL_String json, LSL_List specifiers)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llKey2Name

```csharp
LSL_String llKey2Name(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinear2sRGB

```csharp
LSL_Vector llLinear2sRGB(LSL_Vector src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinkAdjustSoundVolume

```csharp
void llLinkAdjustSoundVolume(LSL_Integer linknumber, LSL_Float volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinkParticleSystem

```csharp
void llLinkParticleSystem(int linknum, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinkPlaySound

```csharp
void llLinkPlaySound(LSL_Integer linknumber, string sound, double volume, LSL_Integer flags)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinkSetSoundQueueing

```csharp
void llLinkSetSoundQueueing(int linknumber, int queue)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinkSetSoundRadius

```csharp
void llLinkSetSoundRadius(int linknumber, double radius)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinkSitTarget

```csharp
void llLinkSitTarget(LSL_Integer link, LSL_Vector offset, LSL_Rotation rot)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinkStopSound

```csharp
void llLinkStopSound(LSL_Integer linknumber)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataAvailable

```csharp
LSL_Integer llLinksetDataAvailable()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataCountFound

```csharp
LSL_Integer llLinksetDataCountFound(LSL_String pattern)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataCountKeys

```csharp
LSL_Integer llLinksetDataCountKeys()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataDelete

```csharp
LSL_Integer llLinksetDataDelete(LSL_String name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataDeleteFound

```csharp
LSL_List llLinksetDataDeleteFound(LSL_String pattern, LSL_String pass)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataDeleteProtected

```csharp
LSL_Integer llLinksetDataDeleteProtected(LSL_String name, LSL_String pass)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataFindKeys

```csharp
LSL_List llLinksetDataFindKeys(LSL_String pattern, LSL_Integer start, LSL_Integer count)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataListKeys

```csharp
LSL_List llLinksetDataListKeys(LSL_Integer start, LSL_Integer count)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataRead

```csharp
LSL_String llLinksetDataRead(LSL_String name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataReadProtected

```csharp
LSL_String llLinksetDataReadProtected(LSL_String name, LSL_String pass)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataReset

```csharp
void llLinksetDataReset()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataWrite

```csharp
LSL_Integer llLinksetDataWrite(LSL_String name, LSL_String value)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLinksetDataWriteProtected

```csharp
LSL_Integer llLinksetDataWriteProtected(LSL_String name, LSL_String value, LSL_String pass)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2CSV

```csharp
LSL_String llList2CSV(LSL_List src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2Float

```csharp
LSL_Float llList2Float(LSL_List src, int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2Integer

```csharp
LSL_Integer llList2Integer(LSL_List src, int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2Json

```csharp
LSL_String llList2Json(LSL_String type, LSL_List values)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2Key

```csharp
LSL_Key llList2Key(LSL_List src, int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2List

```csharp
LSL_List llList2List(LSL_List src, int start, int end)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2ListSlice

```csharp
LSL_List llList2ListSlice(LSL_List src, int start, int end, int stride, int stride_index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2ListStrided

```csharp
LSL_List llList2ListStrided(LSL_List src, int start, int end, int stride)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2Rot

```csharp
LSL_Rotation llList2Rot(LSL_List src, int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2String

```csharp
LSL_String llList2String(LSL_List src, int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llList2Vector

```csharp
LSL_Vector llList2Vector(LSL_List src, int index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListFindList

```csharp
LSL_Integer llListFindList(LSL_List src, LSL_List test)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListFindListNext

```csharp
LSL_Integer llListFindListNext(LSL_List src, LSL_List test, LSL_Integer instance)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListFindStrided

```csharp
LSL_Integer llListFindStrided(LSL_List src, LSL_List test, LSL_Integer lstart, LSL_Integer lend, LSL_Integer lstride)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListInsertList

```csharp
LSL_List llListInsertList(LSL_List dest, LSL_List src, int start)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListRandomize

```csharp
LSL_List llListRandomize(LSL_List src, int stride)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListReplaceList

```csharp
LSL_List llListReplaceList(LSL_List dest, LSL_List src, int start, int end)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListSort

```csharp
LSL_List llListSort(LSL_List src, int stride, int ascending)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListSortStrided

```csharp
LSL_List llListSortStrided(LSL_List src, int stride, int stride_index, int ascending)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListStatistics

```csharp
LSL_Float llListStatistics(int operation, LSL_List src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListen

```csharp
LSL_Integer llListen(int channelID, string name, string ID, string msg)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListenControl

```csharp
void llListenControl(int number, int active)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llListenRemove

```csharp
void llListenRemove(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLoadURL

```csharp
void llLoadURL(string avatar_id, string message, string url)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLog

```csharp
LSL_Float llLog(double val)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLog10

```csharp
LSL_Float llLog10(double val)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLookAt

```csharp
void llLookAt(LSL_Vector target, double strength, double damping)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLoopSound

```csharp
void llLoopSound(string sound, double volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLoopSoundMaster

```csharp
void llLoopSoundMaster(string sound, double volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llLoopSoundSlave

```csharp
void llLoopSoundSlave(string sound, double volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMD5String

```csharp
LSL_String llMD5String(string src, int nonce)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMakeExplosion

```csharp
void llMakeExplosion(int particles, double scale, double vel, double lifetime, double arc, string texture, LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMakeFire

```csharp
void llMakeFire(int particles, double scale, double vel, double lifetime, double arc, string texture, LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMakeFountain

```csharp
void llMakeFountain(int particles, double scale, double vel, double lifetime, double arc, int bounce, string texture, LSL_Vector offset, double bounce_offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMakeSmoke

```csharp
void llMakeSmoke(int particles, double scale, double vel, double lifetime, double arc, string texture, LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llManageEstateAccess

```csharp
LSL_Integer llManageEstateAccess(int action, string avatar)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMapBeacon

```csharp
void llMapBeacon(string simname, LSL_Vector pos, LSL_List loptions)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMapDestination

```csharp
void llMapDestination(string simname, LSL_Vector pos, LSL_Vector look_at)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMessageLinked

```csharp
void llMessageLinked(int linknum, int num, string str, string id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMinEventDelay

```csharp
void llMinEventDelay(double delay)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llModPow

```csharp
LSL_Integer llModPow(int a, int b, int c)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llModifyLand

```csharp
void llModifyLand(int action, int brush)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llMoveToTarget

```csharp
void llMoveToTarget(LSL_Vector target, double tau)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llName2Key

```csharp
LSL_Key llName2Key(LSL_String name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llOffsetTexture

```csharp
void llOffsetTexture(double u, double v, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llOpenRemoteDataChannel

```csharp
void llOpenRemoteDataChannel()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llOrd

```csharp
LSL_Integer llOrd(LSL_String s, LSL_Integer index)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llOverMyLand

```csharp
LSL_Integer llOverMyLand(string id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llOwnerSay

```csharp
void llOwnerSay(string msg)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llParcelMediaCommandList

```csharp
void llParcelMediaCommandList(LSL_List commandList)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llParcelMediaQuery

```csharp
LSL_List llParcelMediaQuery(LSL_List aList)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llParseString2List

```csharp
LSL_List llParseString2List(string str, LSL_List separators, LSL_List spacers)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llParseStringKeepNulls

```csharp
LSL_List llParseStringKeepNulls(string src, LSL_List seperators, LSL_List spacers)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llParticleSystem

```csharp
void llParticleSystem(LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPassCollisions

```csharp
void llPassCollisions(int pass)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPassTouches

```csharp
void llPassTouches(int pass)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPlaySound

```csharp
void llPlaySound(string sound, double volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPlaySoundSlave

```csharp
void llPlaySoundSlave(string sound, double volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPointAt

```csharp
void llPointAt(LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPow

```csharp
LSL_Float llPow(double fbase, double fexponent)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPreloadSound

```csharp
void llPreloadSound(string sound)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llPushObject

```csharp
void llPushObject(string target, LSL_Vector impulse, LSL_Vector ang_impulse, int local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRefreshPrimURL

```csharp
void llRefreshPrimURL()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRegionSay

```csharp
void llRegionSay(int channelID, string text)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRegionSayTo

```csharp
void llRegionSayTo(string key, int channelID, string text)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llReleaseCamera

```csharp
void llReleaseCamera(string avatar)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llReleaseControls

```csharp
void llReleaseControls()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llReleaseURL

```csharp
void llReleaseURL(string url)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoteDataReply

```csharp
void llRemoteDataReply(string channel, string message_id, string sdata, int idata)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoteDataSetRegion

```csharp
void llRemoteDataSetRegion()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoteLoadScript

```csharp
void llRemoteLoadScript(string target, string name, int running, int start_param)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoteLoadScriptPin

```csharp
void llRemoteLoadScriptPin(string target, string name, int pin, int running, int start_param)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoveFromLandBanList

```csharp
void llRemoveFromLandBanList(string avatar)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoveFromLandPassList

```csharp
void llRemoveFromLandPassList(string avatar)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoveInventory

```csharp
void llRemoveInventory(string item)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRemoveVehicleFlags

```csharp
void llRemoveVehicleFlags(int flags)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llReplaceSubString

```csharp
LSL_String llReplaceSubString(LSL_String src, LSL_String pattern, LSL_String replacement, int count)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestAgentData

```csharp
LSL_Key llRequestAgentData(string id, int data)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestDisplayName

```csharp
LSL_Key llRequestDisplayName(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestInventoryData

```csharp
LSL_Key llRequestInventoryData(LSL_String name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestPermissions

```csharp
void llRequestPermissions(string agent, int perm)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestSecureURL

```csharp
LSL_Key llRequestSecureURL()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestSimulatorData

```csharp
LSL_Key llRequestSimulatorData(string simulator, int data)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestURL

```csharp
LSL_Key llRequestURL()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestUserKey

```csharp
LSL_Key llRequestUserKey(LSL_String username)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRequestUsername

```csharp
LSL_Key llRequestUsername(LSL_Key id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llResetAnimationOverride

```csharp
void llResetAnimationOverride(LSL_String anim_state)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llResetLandBanList

```csharp
void llResetLandBanList()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llResetLandPassList

```csharp
void llResetLandPassList()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llResetOtherScript

```csharp
void llResetOtherScript(string name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llResetScript

```csharp
void llResetScript()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llResetTime

```csharp
void llResetTime()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRezAtRoot

```csharp
void llRezAtRoot(string inventory, LSL_Vector position, LSL_Vector velocity, LSL_Rotation rot, int param)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRezObject

```csharp
void llRezObject(string inventory, LSL_Vector pos, LSL_Vector vel, LSL_Rotation rot, int param)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRezObjectWithParams

```csharp
LSL_Key llRezObjectWithParams(string inventory, LSL_List lparam)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRot2Angle

```csharp
LSL_Float llRot2Angle(LSL_Rotation rot)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRot2Axis

```csharp
LSL_Vector llRot2Axis(LSL_Rotation rot)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRot2Euler

```csharp
LSL_Vector llRot2Euler(LSL_Rotation r)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRot2Fwd

```csharp
LSL_Vector llRot2Fwd(LSL_Rotation r)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRot2Left

```csharp
LSL_Vector llRot2Left(LSL_Rotation r)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRot2Up

```csharp
LSL_Vector llRot2Up(LSL_Rotation r)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRotBetween

```csharp
LSL_Rotation llRotBetween(LSL_Vector start, LSL_Vector end)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRotLookAt

```csharp
void llRotLookAt(LSL_Rotation target, double strength, double damping)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRotTarget

```csharp
LSL_Integer llRotTarget(LSL_Rotation rot, double error)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRotTargetRemove

```csharp
void llRotTargetRemove(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRotateTexture

```csharp
void llRotateTexture(double rotation, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llRound

```csharp
LSL_Integer llRound(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSHA1String

```csharp
LSL_String llSHA1String(string src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSHA256String

```csharp
LSL_String llSHA256String(LSL_String src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSameGroup

```csharp
LSL_Integer llSameGroup(string agent)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSay

```csharp
void llSay(int channelID, string text)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llScaleByFactor

```csharp
LSL_Integer llScaleByFactor(double scaling_factor)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llScaleTexture

```csharp
void llScaleTexture(double u, double v, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llScriptDanger

```csharp
LSL_Integer llScriptDanger(LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llScriptProfiler

```csharp
void llScriptProfiler(LSL_Integer flags)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSendRemoteData

```csharp
LSL_Key llSendRemoteData(string channel, string dest, int idata, string sdata)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSensor

```csharp
void llSensor(string name, string id, int type, double range, double arc)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSensorRemove

```csharp
void llSensorRemove()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSensorRepeat

```csharp
void llSensorRepeat(string name, string id, int type, double range, double arc, double rate)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetAlpha

```csharp
void llSetAlpha(double alpha, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetAngularVelocity

```csharp
void llSetAngularVelocity(LSL_Vector force, int local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetAnimationOverride

```csharp
void llSetAnimationOverride(LSL_String animState, LSL_String anim)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetBuoyancy

```csharp
void llSetBuoyancy(double buoyancy)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetCameraAtOffset

```csharp
void llSetCameraAtOffset(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetCameraEyeOffset

```csharp
void llSetCameraEyeOffset(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetCameraParams

```csharp
void llSetCameraParams(LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetClickAction

```csharp
void llSetClickAction(int action)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetColor

```csharp
void llSetColor(LSL_Vector color, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetContentType

```csharp
void llSetContentType(LSL_Key id, LSL_Integer type)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetDamage

```csharp
void llSetDamage(double damage)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetForce

```csharp
void llSetForce(LSL_Vector force, int local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetForceAndTorque

```csharp
void llSetForceAndTorque(LSL_Vector force, LSL_Vector torque, int local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetHoverHeight

```csharp
void llSetHoverHeight(double height, int water, double tau)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetInventoryPermMask

```csharp
void llSetInventoryPermMask(string item, int mask, int value)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetKeyframedMotion

```csharp
void llSetKeyframedMotion(LSL_List frames, LSL_List options)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkAlpha

```csharp
void llSetLinkAlpha(int linknumber, double alpha, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkCamera

```csharp
void llSetLinkCamera(LSL_Integer link, LSL_Vector eye, LSL_Vector at)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkColor

```csharp
void llSetLinkColor(int linknumber, LSL_Vector color, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkMedia

```csharp
LSL_Integer llSetLinkMedia(LSL_Integer link, LSL_Integer face, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkPrimitiveParams

```csharp
void llSetLinkPrimitiveParams(int linknumber, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkPrimitiveParamsFast

```csharp
void llSetLinkPrimitiveParamsFast(int linknum, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkSitFlags

```csharp
void llSetLinkSitFlags(LSL_Integer linknum, LSL_Integer flags)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkTexture

```csharp
void llSetLinkTexture(int linknumber, string texture, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLinkTextureAnim

```csharp
void llSetLinkTextureAnim(int linknum, int mode, int face, int sizex, int sizey, double start, double length, double rate)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetLocalRot

```csharp
void llSetLocalRot(LSL_Rotation rot)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetMemoryLimit

```csharp
LSL_Integer llSetMemoryLimit(LSL_Integer limit)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetObjectDesc

```csharp
void llSetObjectDesc(string desc)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetObjectName

```csharp
void llSetObjectName(string name)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetObjectPermMask

```csharp
void llSetObjectPermMask(int mask, int value)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetParcelMusicURL

```csharp
void llSetParcelMusicURL(string url)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetPayPrice

```csharp
void llSetPayPrice(int price, LSL_List quick_pay_buttons)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetPhysicsMaterial

```csharp
void llSetPhysicsMaterial(int material_bits, LSL_Float material_gravity_modifier, LSL_Float material_restitution, LSL_Float material_friction, LSL_Float material_density)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetPos

```csharp
void llSetPos(LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetPrimMediaParams

```csharp
LSL_Integer llSetPrimMediaParams(int face, LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetPrimURL

```csharp
void llSetPrimURL(string url)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetPrimitiveParams

```csharp
void llSetPrimitiveParams(LSL_List rules)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetRegionPos

```csharp
LSL_Integer llSetRegionPos(LSL_Vector pos)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetRemoteScriptAccessPin

```csharp
void llSetRemoteScriptAccessPin(int pin)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetRenderMaterial

```csharp
void llSetRenderMaterial(LSL_String material, LSL_Integer face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetRot

```csharp
void llSetRot(LSL_Rotation rot)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetScale

```csharp
void llSetScale(LSL_Vector scale)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetScriptState

```csharp
void llSetScriptState(string name, int run)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetSitText

```csharp
void llSetSitText(string text)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetSoundQueueing

```csharp
void llSetSoundQueueing(int queue)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetSoundRadius

```csharp
void llSetSoundRadius(double radius)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetStatus

```csharp
void llSetStatus(int status, int value)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetText

```csharp
void llSetText(string text, LSL_Vector color, double alpha)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetTexture

```csharp
void llSetTexture(string texture, int face)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetTextureAnim

```csharp
void llSetTextureAnim(int mode, int face, int sizex, int sizey, double start, double length, double rate)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetTimerEvent

```csharp
void llSetTimerEvent(double sec)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetTorque

```csharp
void llSetTorque(LSL_Vector torque, int local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetTouchText

```csharp
void llSetTouchText(string text)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetVehicleFlags

```csharp
void llSetVehicleFlags(int flags)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetVehicleFloatParam

```csharp
void llSetVehicleFloatParam(int param, LSL_Float value)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetVehicleRotationParam

```csharp
void llSetVehicleRotationParam(int param, LSL_Rotation rot)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetVehicleType

```csharp
void llSetVehicleType(int type)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetVehicleVectorParam

```csharp
void llSetVehicleVectorParam(int param, LSL_Vector vec)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSetVelocity

```csharp
void llSetVelocity(LSL_Vector force, int local)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llShout

```csharp
void llShout(int channelID, string text)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSin

```csharp
LSL_Float llSin(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSitTarget

```csharp
void llSitTarget(LSL_Vector offset, LSL_Rotation rot)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSleep

```csharp
void llSleep(double sec)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSound

```csharp
void llSound(string sound, double volume, int queue, int loop)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSoundPreload

```csharp
void llSoundPreload(string sound)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSqrt

```csharp
LSL_Float llSqrt(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStartAnimation

```csharp
void llStartAnimation(string anim)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStartObjectAnimation

```csharp
void llStartObjectAnimation(string anim)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStopAnimation

```csharp
void llStopAnimation(string anim)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStopHover

```csharp
void llStopHover()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStopLookAt

```csharp
void llStopLookAt()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStopMoveToTarget

```csharp
void llStopMoveToTarget()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStopObjectAnimation

```csharp
void llStopObjectAnimation(string anim)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStopPointAt

```csharp
void llStopPointAt()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStopSound

```csharp
void llStopSound()
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStringLength

```csharp
LSL_Integer llStringLength(string str)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStringToBase64

```csharp
LSL_String llStringToBase64(string str)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llStringTrim

```csharp
LSL_String llStringTrim(LSL_String src, LSL_Integer type)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llSubStringIndex

```csharp
LSL_Integer llSubStringIndex(string source, string pattern)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTakeCamera

```csharp
void llTakeCamera(string avatar)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTakeControls

```csharp
void llTakeControls(int controls, int accept, int pass_on)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTan

```csharp
LSL_Float llTan(double f)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTarget

```csharp
LSL_Integer llTarget(LSL_Vector position, double range)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTargetOmega

```csharp
void llTargetOmega(LSL_Vector axis, double spinrate, double gain)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTargetRemove

```csharp
void llTargetRemove(int number)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTargetedEmail

```csharp
void llTargetedEmail(LSL_Integer target, LSL_String subject, LSL_String message)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTeleportAgent

```csharp
void llTeleportAgent(string agent, string simname, LSL_Vector pos, LSL_Vector lookAt)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTeleportAgentGlobalCoords

```csharp
void llTeleportAgentGlobalCoords(string agent, LSL_Vector global, LSL_Vector pos, LSL_Vector lookAt)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTeleportAgentHome

```csharp
void llTeleportAgentHome(string agent)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTextBox

```csharp
void llTextBox(string avatar, string message, int chat_channel)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llToLower

```csharp
LSL_String llToLower(string source)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llToUpper

```csharp
LSL_String llToUpper(string source)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTransferLindenDollars

```csharp
LSL_Key llTransferLindenDollars(LSL_Key destination, LSL_Integer amount)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTriggerSound

```csharp
void llTriggerSound(string sound, double volume)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llTriggerSoundLimited

```csharp
void llTriggerSoundLimited(string sound, double volume, LSL_Vector top_north_east, LSL_Vector bottom_south_west)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llUnSit

```csharp
void llUnSit(string id)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llUnescapeURL

```csharp
LSL_String llUnescapeURL(string url)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llVecDist

```csharp
LSL_Float llVecDist(LSL_Vector a, LSL_Vector b)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llVecMag

```csharp
LSL_Float llVecMag(LSL_Vector v)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llVecNorm

```csharp
LSL_Vector llVecNorm(LSL_Vector v)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llVolumeDetect

```csharp
void llVolumeDetect(int detect)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llWater

```csharp
LSL_Float llWater(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llWhisper

```csharp
void llWhisper(int channelID, string text)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llWind

```csharp
LSL_Vector llWind(LSL_Vector offset)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llWorldPosToHUD

```csharp
LSL_Vector llWorldPosToHUD(LSL_Vector WorldPosition)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llXorBase64

```csharp
LSL_String llXorBase64(string str1, string str2)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llXorBase64Strings

```csharp
LSL_String llXorBase64Strings(string str1, string str2)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llXorBase64StringsCorrect

```csharp
LSL_String llXorBase64StringsCorrect(string str1, string str2)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.


## llsRGB2Linear

```csharp
LSL_Vector llsRGB2Linear(LSL_Vector src)
```

- OpenSim implementation: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/LSL_Stub.cs` | Canonical definition: see lsl-functions.md in secondlife_lsl_scripting.
