# OSSL Function Reference (generated from opensim/opensim source)

Extracted 267 os* function signatures from the OpenSimulator source tree (OSSL API implementation files). OSSL functions exist only in OpenSim, never on Agni, and each is gated by a threat level and osslEnable.ini allow lists. Verify the threat level for a function in the OpenSim wiki OSSL pages and in osslEnable.ini before relying on it for a non-owner user.


## osAESDecrypt

```csharp
LSL_String osAESDecrypt(string secret, string encryptedText)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAESDecryptFrom

```csharp
LSL_String osAESDecryptFrom(string secret, string encryptedText, string ivString)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAESEncrypt

```csharp
LSL_String osAESEncrypt(string secret, string plainText)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAESEncryptTo

```csharp
LSL_String osAESEncryptTo(string secret, string plainText, string ivString)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAdjustSoundVolume

```csharp
void osAdjustSoundVolume(LSL_Integer linknum, LSL_Float volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAgentSaveAppearance

```csharp
LSL_Key osAgentSaveAppearance(LSL_Key agentId, LSL_String notecard, LSL_Integer includeHuds)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAngleBetween

```csharp
LSL_Float osAngleBetween(vector a, vector b)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osApproxEquals

```csharp
LSL_Integer osApproxEquals(rotation ra, rotation rb, LSL_Float margin)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAvatarName2Key

```csharp
string osAvatarName2Key(string firstname, string lastname)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAvatarPlayAnimation

```csharp
void osAvatarPlayAnimation(LSL_Key avatar, string animation)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAvatarStopAnimation

```csharp
void osAvatarStopAnimation(LSL_Key avatar, string animation)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osAvatarType

```csharp
LSL_Integer osAvatarType(LSL_String sFirstName, LSL_String sLastName)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osCauseDamage

```csharp
void osCauseDamage(key avatar, LSL_Float damage)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osCauseHealing

```csharp
void osCauseHealing(key avatar, LSL_Float healing)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osCheckODE

```csharp
LSL_Integer osCheckODE()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osClearInertia

```csharp
void osClearInertia()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osClearObjectAnimations

```csharp
LSL_Integer osClearObjectAnimations()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osCollisionSound

```csharp
void osCollisionSound(string impact_sound, double impact_volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osConsoleCommand

```csharp
bool osConsoleCommand(string Command)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDetectedCountry

```csharp
LSL_String osDetectedCountry(LSL_Integer number)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDie

```csharp
void osDie(LSL_Key objectUUID)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawEllipse

```csharp
string osDrawEllipse(string drawList, int width, int height)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawFilledEllipse

```csharp
string osDrawFilledEllipse(string drawList, int width, int height)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawFilledPolygon

```csharp
string osDrawFilledPolygon(string drawList, LSL_List x, LSL_List y)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawFilledRectangle

```csharp
string osDrawFilledRectangle(string drawList, int width, int height)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawImage

```csharp
string osDrawImage(string drawList, int width, int height, string imageUrl)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawLine

```csharp
string osDrawLine(string drawList, int endX, int endY)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawPolygon

```csharp
string osDrawPolygon(string drawList, LSL_List x, LSL_List y)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawRectangle

```csharp
string osDrawRectangle(string drawList, int width, int height)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawResetTransform

```csharp
string osDrawResetTransform(string drawList)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawRotationTransform

```csharp
string osDrawRotationTransform(string drawList, LSL_Float x)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawScaleTransform

```csharp
string osDrawScaleTransform(string drawList, LSL_Float x, LSL_Float y)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawText

```csharp
string osDrawText(string drawList, string text)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDrawTranslationTransform

```csharp
string osDrawTranslationTransform(string drawList, LSL_Float x, LSL_Float y)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDropAttachment

```csharp
void osDropAttachment()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osDropAttachmentAt

```csharp
void osDropAttachmentAt(vector pos, rotation rot)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osEjectFromGroup

```csharp
LSL_Integer osEjectFromGroup(LSL_Key agentId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceAttachToAvatar

```csharp
void osForceAttachToAvatar(int attachmentPoint)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceAttachToAvatarFromInventory

```csharp
void osForceAttachToAvatarFromInventory(string itemName, int attachmentPoint)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceAttachToOtherAvatarFromInventory

```csharp
void osForceAttachToOtherAvatarFromInventory(string rawAvatarId, string itemName, int attachmentPoint)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceBreakAllLinks

```csharp
void osForceBreakAllLinks()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceBreakLink

```csharp
void osForceBreakLink(int linknum)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceCreateLink

```csharp
void osForceCreateLink(string target, int parent)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceDetachFromAvatar

```csharp
void osForceDetachFromAvatar()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceDropAttachment

```csharp
void osForceDropAttachment()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceDropAttachmentAt

```csharp
void osForceDropAttachmentAt(vector pos, rotation rot)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osForceOtherSit

```csharp
void osForceOtherSit(string avatar, string target)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osFormatString

```csharp
LSL_String osFormatString(string str, LSL_List strings)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetAgentCountry

```csharp
LSL_String osGetAgentCountry(LSL_Key agentId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetAgentIP

```csharp
string osGetAgentIP(string agent)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetAgents

```csharp
LSL_List osGetAgents()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetApparentRegionTime

```csharp
LSL_Float osGetApparentRegionTime()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetApparentRegionTimeString

```csharp
LSL_String osGetApparentRegionTimeString(LSL_Integer format24)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetApparentTime

```csharp
LSL_Float osGetApparentTime()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetApparentTimeString

```csharp
LSL_String osGetApparentTimeString(LSL_Integer format24)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetAvatarHomeURI

```csharp
string osGetAvatarHomeURI(string uuid)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetAvatarList

```csharp
LSL_List osGetAvatarList()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetCurrentSunHour

```csharp
LSL_Float osGetCurrentSunHour()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetDrawStringSize

```csharp
vector osGetDrawStringSize(string contentType, string text, string fontName, int fontSize)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetGender

```csharp
string osGetGender(LSL_Key rawAvatarId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetGridCustom

```csharp
string osGetGridCustom(string key)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetGridGatekeeperURI

```csharp
string osGetGridGatekeeperURI()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetGridHomeURI

```csharp
string osGetGridHomeURI()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetGridLoginURI

```csharp
string osGetGridLoginURI()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetGridName

```csharp
string osGetGridName()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetGridNick

```csharp
string osGetGridNick()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetHealRate

```csharp
LSL_Float osGetHealRate(key avatar)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetHealth

```csharp
LSL_Float osGetHealth(key avatar)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetInertiaData

```csharp
LSL_List osGetInertiaData()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetInventoryDesc

```csharp
LSL_String osGetInventoryDesc(LSL_String itemNameOrId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetInventoryItemKey

```csharp
LSL_Key osGetInventoryItemKey(LSL_String name)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetInventoryItemKeys

```csharp
LSL_List osGetInventoryItemKeys(LSL_Integer type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetInventoryLastOwner

```csharp
LSL_Key osGetInventoryLastOwner(LSL_String itemNameOrId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetInventoryName

```csharp
LSL_String osGetInventoryName(LSL_Key itemId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetInventoryNames

```csharp
LSL_List osGetInventoryNames(LSL_Integer type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLastChangedEventKey

```csharp
LSL_Key osGetLastChangedEventKey()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkColor

```csharp
vector osGetLinkColor(LSL_Integer link, LSL_Integer face)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkInventoryDesc

```csharp
LSL_String osGetLinkInventoryDesc(LSL_Integer linkNumber, LSL_String itemNameOrId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkInventoryItemKey

```csharp
LSL_Key osGetLinkInventoryItemKey(LSL_Integer linkNumber, LSL_String name)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkInventoryItemKeys

```csharp
LSL_List osGetLinkInventoryItemKeys(LSL_Integer linkNumber, LSL_Integer type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkInventoryKey

```csharp
LSL_Key osGetLinkInventoryKey(LSL_Integer linkNumber, LSL_String name, LSL_Integer type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkInventoryKeys

```csharp
LSL_List osGetLinkInventoryKeys(LSL_Integer linkNumber, LSL_Integer type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkInventoryName

```csharp
LSL_String osGetLinkInventoryName(LSL_Integer linkNumber, LSL_Key itemId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkInventoryNames

```csharp
LSL_List osGetLinkInventoryNames(LSL_Integer linkNumber, LSL_Integer type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkNumber

```csharp
LSL_Integer osGetLinkNumber(LSL_String name)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkPrimitiveParams

```csharp
LSL_List osGetLinkPrimitiveParams(int linknumber, LSL_List rules)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkSitActiveRange

```csharp
LSL_Float osGetLinkSitActiveRange(LSL_Integer linkNumber)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetLinkStandTarget

```csharp
vector osGetLinkStandTarget(LSL_Integer linkNumber)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetMapTexture

```csharp
key osGetMapTexture()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetNPCList

```csharp
LSL_List osGetNPCList()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetNotecard

```csharp
string osGetNotecard(string name)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetNotecardLine

```csharp
string osGetNotecardLine(string name, int line)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetNumberOfAttachments

```csharp
LSL_List osGetNumberOfAttachments(LSL_Key avatar, LSL_List attachmentPoints)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetNumberOfNotecardLines

```csharp
int osGetNumberOfNotecardLines(string name)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetPSTWallclock

```csharp
LSL_Float osGetPSTWallclock()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetParcelDetails

```csharp
LSL_List osGetParcelDetails(LSL_Key id, LSL_List param)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetParcelDwell

```csharp
LSL_Integer osGetParcelDwell(vector pos)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetParcelID

```csharp
LSL_Key osGetParcelID()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetParcelIDs

```csharp
LSL_List osGetParcelIDs()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetPhysicsEngineName

```csharp
string osGetPhysicsEngineName()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetPhysicsEngineType

```csharp
string osGetPhysicsEngineType()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetPrimCount

```csharp
LSL_Integer osGetPrimCount(LSL_Key object_id)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetPrimitiveParams

```csharp
LSL_List osGetPrimitiveParams(LSL_Key prim, LSL_List rules)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetRegionMapTexture

```csharp
key osGetRegionMapTexture(string regionNameOrID)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetRegionSize

```csharp
vector osGetRegionSize()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetRegionStats

```csharp
LSL_List osGetRegionStats()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetRezzingObject

```csharp
LSL_Key osGetRezzingObject()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetScriptEngineName

```csharp
string osGetScriptEngineName()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSimulatorMemory

```csharp
LSL_Integer osGetSimulatorMemory()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSimulatorMemoryKB

```csharp
LSL_Integer osGetSimulatorMemoryKB()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSimulatorVersion

```csharp
string osGetSimulatorVersion()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSitActiveRange

```csharp
LSL_Float osGetSitActiveRange()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSitTargetPos

```csharp
vector osGetSitTargetPos()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSitTargetRot

```csharp
rotation osGetSitTargetRot()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSittingAvatarsCount

```csharp
LSL_Integer osGetSittingAvatarsCount(LSL_Key object_id)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetStandTarget

```csharp
vector osGetStandTarget()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetSunParam

```csharp
LSL_Float osGetSunParam(LSL_String param)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetTerrainHeight

```csharp
LSL_Float osGetTerrainHeight(int x, int y)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGetWindParam

```csharp
LSL_Float osGetWindParam(string plugin, string param)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGiveLinkInventory

```csharp
void osGiveLinkInventory(LSL_Integer linkNumber, LSL_Key destination, LSL_String inventory)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osGiveLinkInventoryList

```csharp
void osGiveLinkInventoryList(LSL_Integer linkNumber, LSL_Key destination, LSL_String category, LSL_List inventory)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osInviteToGroup

```csharp
LSL_Integer osInviteToGroup(LSL_Key agentId)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osIsNotValidNumber

```csharp
LSL_Integer osIsNotValidNumber(LSL_Float v)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osIsNpc

```csharp
LSL_Integer osIsNpc(LSL_Key npc)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osIsUUID

```csharp
LSL_Integer osIsUUID(string thing)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osKey2Name

```csharp
string osKey2Name(string id)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osKickAvatar

```csharp
void osKickAvatar(LSL_Key agentId, string alert)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLinkParticleSystem

```csharp
void osLinkParticleSystem(LSL_Integer linknumber, LSL_List rules)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListAsFloat

```csharp
LSL_Float osListAsFloat(LSL_List src, int index)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListAsInteger

```csharp
LSL_Integer osListAsInteger(LSL_List src, int index)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListAsRotation

```csharp
rotation osListAsRotation(LSL_List src, int index)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListAsString

```csharp
LSL_String osListAsString(LSL_List src, int index)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListAsVector

```csharp
vector osListAsVector(LSL_List src, int index)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListFindListNext

```csharp
LSL_Integer osListFindListNext(LSL_List src, LSL_List test, LSL_Integer start, LSL_Integer end, LSL_Integer instance)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListSortInPlace

```csharp
void osListSortInPlace(LSL_List src, LSL_Integer stride, LSL_Integer ascending)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListSortInPlaceStrided

```csharp
void osListSortInPlaceStrided(LSL_List src, LSL_Integer stride, LSL_Integer stride_index, LSL_Integer ascending)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osListenRegex

```csharp
LSL_Integer osListenRegex(int channelID, string name, string ID, string msg, int regexBitfield)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLoadedCreationDate

```csharp
string osLoadedCreationDate()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLoadedCreationID

```csharp
string osLoadedCreationID()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLoadedCreationTime

```csharp
string osLoadedCreationTime()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLocalTeleportAgent

```csharp
void osLocalTeleportAgent(LSL_Key agent, vector position, vector velocity, vector lookat, LSL_Integer flags)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLoopSound

```csharp
void osLoopSound(LSL_Integer linknum, LSL_String sound, LSL_Float volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLoopSoundMaster

```csharp
void osLoopSoundMaster(LSL_Integer linknum, LSL_String sound, LSL_Float volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osLoopSoundSlave

```csharp
void osLoopSoundSlave(LSL_Integer linknum, LSL_String sound, LSL_Float volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osMakeNotecard

```csharp
void osMakeNotecard(string notecardName, LSL_List contents)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osMatchString

```csharp
LSL_List osMatchString(string src, string pattern, int start)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osMax

```csharp
LSL_Float osMax(double a, double b)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osMessageAttachments

```csharp
void osMessageAttachments(LSL_Key avatar, string message, LSL_List attachmentPoints, int flags)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osMessageObject

```csharp
void osMessageObject(key objectUUID,string message)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osMin

```csharp
LSL_Float osMin(double a, double b)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osMovePen

```csharp
string osMovePen(string drawList, int x, int y)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcCreate

```csharp
key osNpcCreate(string user, string name, vector position, key cloneFrom, int options)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcGetOwner

```csharp
LSL_Key osNpcGetOwner(LSL_Key npc)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcGetPos

```csharp
vector osNpcGetPos(LSL_Key npc)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcGetRot

```csharp
rotation osNpcGetRot(key npc)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcLoadAppearance

```csharp
void osNpcLoadAppearance(key npc, string notecard)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcLookAt

```csharp
LSL_Integer osNpcLookAt(LSL_Key npckey, LSL_Integer type, LSL_Key objkey, vector offset)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcMoveTo

```csharp
void osNpcMoveTo(key npc, vector position)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcMoveToTarget

```csharp
void osNpcMoveToTarget(key npc, vector target, int options)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcPlayAnimation

```csharp
void osNpcPlayAnimation(LSL_Key npc, string animation)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcRemove

```csharp
void osNpcRemove(key npc)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcSaveAppearance

```csharp
key osNpcSaveAppearance(key npc, LSL_String notecard, LSL_Integer includeHuds)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcSay

```csharp
void osNpcSay(key npc, int channel, string message)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcSayTo

```csharp
void osNpcSayTo(LSL_Key npc, LSL_Key target, int channel, string msg)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcSetProfileAbout

```csharp
void osNpcSetProfileAbout(LSL_Key npc, string about)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcSetProfileImage

```csharp
void osNpcSetProfileImage(LSL_Key npc, string image)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcSetRot

```csharp
void osNpcSetRot(key npc, rotation rot)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcShout

```csharp
void osNpcShout(key npc, int channel, string message)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcSit

```csharp
void osNpcSit(LSL_Key npc, LSL_Key target, int options)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcStand

```csharp
void osNpcStand(LSL_Key npc)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcStopAnimation

```csharp
void osNpcStopAnimation(LSL_Key npc, string animation)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcStopMoveToTarget

```csharp
void osNpcStopMoveToTarget(LSL_Key npc)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcTouch

```csharp
void osNpcTouch(LSL_Key npcLSL_Key, LSL_Key object_key, LSL_Integer link_num)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osNpcWhisper

```csharp
void osNpcWhisper(key npc, int channel, string message)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osOldList2ListStrided

```csharp
LSL_List osOldList2ListStrided(LSL_List src, int start, int end, int stride)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osOwnerSaveAppearance

```csharp
LSL_Key osOwnerSaveAppearance(LSL_String notecard, LSL_Integer includeHuds)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osParcelJoin

```csharp
void osParcelJoin(vector pos1, vector pos2)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osParcelSetDetails

```csharp
void osParcelSetDetails(vector pos, LSL_List rules)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osParcelSubdivide

```csharp
void osParcelSubdivide(vector pos1, vector pos2)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osParticleSystem

```csharp
void osParticleSystem(LSL_List rules)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osPlaySound

```csharp
void osPlaySound(LSL_Integer linknum, LSL_String sound, LSL_Float volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osPlaySoundSlave

```csharp
void osPlaySoundSlave(LSL_Integer linknum, LSL_String sound, LSL_Float volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osPreloadSound

```csharp
void osPreloadSound(LSL_Integer linknum, LSL_String sound)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osRegexIsMatch

```csharp
LSL_Integer osRegexIsMatch(string input, string pattern)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osRegionNotice

```csharp
void osRegionNotice(LSL_Key agentID, string msg)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osRegionRestart

```csharp
int osRegionRestart(double seconds, string msg)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osRemoveLinkInventory

```csharp
void osRemoveLinkInventory(LSL_Integer linkNumber, LSL_String name)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osReplaceAgentEnvironment

```csharp
LSL_Integer osReplaceAgentEnvironment(LSL_Key agentkey, LSL_Integer transition, LSL_String daycycle)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osReplaceParcelEnvironment

```csharp
LSL_Integer osReplaceParcelEnvironment(LSL_Integer transition, LSL_String daycycle)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osReplaceRegionEnvironment

```csharp
LSL_Integer osReplaceRegionEnvironment(LSL_Integer transition, LSL_String daycycle, LSL_Float daylen, LSL_Float dayoffset, LSL_Float altitude1, LSL_Float altitude2, LSL_Float altitude3)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osReplaceString

```csharp
LSL_String osReplaceString(string src, string pattern, string replace, int count, int start)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osRequestSecureURL

```csharp
LSL_Key osRequestSecureURL(LSL_List options)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osRequestURL

```csharp
LSL_Key osRequestURL(LSL_List options)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osResetAllScripts

```csharp
void osResetAllScripts(LSL_Integer allLinkSet)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osResetEnvironment

```csharp
LSL_Integer osResetEnvironment(LSL_Integer parcelOrRegion, LSL_Integer transition)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osRound

```csharp
LSL_Float osRound(LSL_Float value, LSL_Integer digits)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSHA256

```csharp
string osSHA256(string input)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetContentType

```csharp
void osSetContentType(LSL_Key id, string type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetDynamicTextureData

```csharp
string osSetDynamicTextureData(string dynamicID, string contentType, string data, string extraParams, int timer)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetDynamicTextureDataBlend

```csharp
string osSetDynamicTextureDataBlend(string dynamicID, string contentType, string data, string extraParams, int timer, int alpha)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetDynamicTextureDataBlendFace

```csharp
string osSetDynamicTextureDataBlendFace(string dynamicID, string contentType, string data, string extraParams, bool blend, int disp, int timer, int alpha, int face)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetDynamicTextureDataFace

```csharp
string osSetDynamicTextureDataFace(string dynamicID, string contentType, string data, string extraParams, int timer, int face)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetDynamicTextureURL

```csharp
string osSetDynamicTextureURL(string dynamicID, string contentType, string url, string extraParams, int timer)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetDynamicTextureURLBlend

```csharp
string osSetDynamicTextureURLBlend(string dynamicID, string contentType, string url, string extraParams, int timer, int alpha)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetDynamicTextureURLBlendFace

```csharp
string osSetDynamicTextureURLBlendFace(string dynamicID, string contentType, string url, string extraParams, bool blend, int disp, int timer, int alpha, int face)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetEstateSunSettings

```csharp
void osSetEstateSunSettings(bool sunFixed, double sunHour)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetFontName

```csharp
string osSetFontName(string drawList, string fontName)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetFontSize

```csharp
string osSetFontSize(string drawList, int fontSize)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetHealRate

```csharp
void osSetHealRate(key avatar, LSL_Float health)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetHealth

```csharp
void osSetHealth(key avatar, LSL_Float health)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetInertia

```csharp
void osSetInertia(LSL_Float mass, vector centerOfMass, vector principalInertiaScaled, rotation rot)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetInertiaAsBox

```csharp
void osSetInertiaAsBox(LSL_Float mass, vector boxSize, vector centerOfMass, rotation rot)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetInertiaAsCylinder

```csharp
void osSetInertiaAsCylinder(LSL_Float mass, LSL_Float radius, LSL_Float length, vector centerOfMass,rotation lslrot)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetInertiaAsSphere

```csharp
void osSetInertiaAsSphere(LSL_Float mass, LSL_Float radius, vector centerOfMass)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetLinkSitActiveRange

```csharp
void osSetLinkSitActiveRange(LSL_Integer linkNumber, LSL_Float v)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetLinkStandTarget

```csharp
void osSetLinkStandTarget(LSL_Integer linkNumber, vector v)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetOwnerSpeed

```csharp
void osSetOwnerSpeed(LSL_Float SpeedModifier)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetParcelDetails

```csharp
void osSetParcelDetails(vector pos, LSL_List rules)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetParcelMediaURL

```csharp
void osSetParcelMediaURL(LSL_String url)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetParcelMusicURL

```csharp
void osSetParcelMusicURL(LSL_String url)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetParcelSIPAddress

```csharp
void osSetParcelSIPAddress(string SIPAddress)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetPenCap

```csharp
string osSetPenCap(string drawList, string direction, string type)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetPenColor

```csharp
string osSetPenColor(string drawList, vector color, float alpha)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetPenColour

```csharp
string osSetPenColour(string drawList, string colour)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetPenSize

```csharp
string osSetPenSize(string drawList, int penSize)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetPrimFloatOnWater

```csharp
void osSetPrimFloatOnWater(int floatYN)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetPrimitiveParams

```csharp
void osSetPrimitiveParams(LSL_Key prim, LSL_List rules)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetProjectionParams

```csharp
void osSetProjectionParams(LSL_Integer linknumber, LSL_Integer projection, LSL_Key texture, LSL_Float fov, LSL_Float focus, LSL_Float amb)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetRegionSunSettings

```csharp
void osSetRegionSunSettings(bool useEstateSun, bool sunFixed, double sunHour)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetRegionWaterHeight

```csharp
void osSetRegionWaterHeight(double height)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetRot

```csharp
void osSetRot(UUID target, Quaternion rotation)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Implementation/OSSL_Api.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetSitActiveRange

```csharp
void osSetSitActiveRange(LSL_Float v)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetSoundRadius

```csharp
void osSetSoundRadius(LSL_Integer linknum, LSL_Float radius)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetSpeed

```csharp
void osSetSpeed(string UUID, LSL_Float SpeedModifier)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetStandTarget

```csharp
void osSetStandTarget(vector v)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetSunParam

```csharp
void osSetSunParam(string param, double value)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetTerrainHeight

```csharp
LSL_Integer osSetTerrainHeight(int x, int y, double val)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetTerrainTexture

```csharp
void osSetTerrainTexture(int level, LSL_Key texture)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetTerrainTextureHeight

```csharp
void osSetTerrainTextureHeight(int corner, double low, double high)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetTerrainTextures

```csharp
void osSetTerrainTextures(LSL_List textures, LSL_Integer types)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSetWindParam

```csharp
void osSetWindParam(string plugin, string param, LSL_Float value)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSlerp

```csharp
vector osSlerp(vector a, vector b, LSL_Float amount)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStopSound

```csharp
void osStopSound(LSL_Integer linknum)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStringEndsWith

```csharp
LSL_Integer osStringEndsWith(LSL_String src, LSL_String value, LSL_Integer ignorecase)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStringIndexOf

```csharp
LSL_Integer osStringIndexOf(LSL_String src, LSL_String value, LSL_Integer offset, LSL_Integer count, LSL_Integer ignorecase)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStringLastIndexOf

```csharp
LSL_Integer osStringLastIndexOf(LSL_String src, LSL_String value, LSL_Integer offset, LSL_Integer count, LSL_Integer ignorecase)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStringRemove

```csharp
LSL_String osStringRemove(LSL_String src, LSL_Integer offset, LSL_Integer count)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStringReplace

```csharp
LSL_String osStringReplace(LSL_String src, LSL_String oldvalue, LSL_String newvalue)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStringStartsWith

```csharp
LSL_Integer osStringStartsWith(LSL_String src, LSL_String value, LSL_Integer ignorecase)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osStringSubString

```csharp
LSL_String osStringSubString(LSL_String src, LSL_Integer offset, LSL_Integer length)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSunGetParam

```csharp
double osSunGetParam(string param)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osSunSetParam

```csharp
void osSunSetParam(string param, double value)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTeleportAgent

```csharp
void osTeleportAgent(string agent, vector position, vector lookat)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTeleportObject

```csharp
LSL_Integer osTeleportObject(LSL_Key objectUUID, vector targetPos, rotation targetrotation, LSL_Integer flags)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTeleportOwner

```csharp
void osTeleportOwner(vector position, vector lookat)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTemperature2sRBG

```csharp
vector osTemperature2sRBG(LSL_Float dtemp)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTemperature2sRGB

```csharp
LSL_Vector osTemperature2sRGB(LSL_Float dtemp)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Implementation/OSSL_Api.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTerrainFlush

```csharp
void osTerrainFlush()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTerrainGetHeight

```csharp
LSL_Float osTerrainGetHeight(int x, int y)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTerrainSetHeight

```csharp
LSL_Integer osTerrainSetHeight(int x, int y, double val)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTriggerSound

```csharp
void osTriggerSound(LSL_Integer linknum, LSL_String sound, LSL_Float volume)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osTriggerSoundLimited

```csharp
void osTriggerSoundLimited(LSL_Integer linknum, LSL_String sound, LSL_Float volume, vector top_north_east, vector bottom_south_west)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osUnixTimeToTimestamp

```csharp
LSL_String osUnixTimeToTimestamp(LSL_Integer time)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osVecDistSquare

```csharp
LSL_Float osVecDistSquare(vector a, vector b)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osVecMagSquare

```csharp
LSL_Float osVecMagSquare(vector a)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osVolumeDetect

```csharp
void osVolumeDetect(int detect)
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.


## osWindActiveModelPluginName

```csharp
string osWindActiveModelPluginName()
```

- Implemented in: `OpenSim/Region/ScriptEngine/Shared/Api/Runtime/OSSL_Stub.cs`

- Grid check required: wrap calls in a grid detection pattern or keep OpenSim-only scripts separate from SL builds. On Agni this call is a compile error, not a runtime failure.
