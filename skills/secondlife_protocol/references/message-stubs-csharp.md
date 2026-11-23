# C# Message Stubs (generated from secondlife/master-message-template)

One stub per UDP message (483 messages) in C#, generated from message_template.msg field definitions. These are starting points for a codec: implement ToBytes/FromBytes following the field order exactly, honour the zerocoded flag, and verify against LibreMetaverse.Protocol and the viewer template copy before shipping.


## TestMessage (Low 1, NotTrusted, Zerocoded)

```csharp

public sealed class TestMessagePacket : Packet {

}
```


## PacketAck (Fixed 0xFFFFFFFB, NotTrusted, Unencoded)

```csharp

public sealed class PacketAckPacket : Packet {

}
```


## OpenCircuit (Fixed 0xFFFFFFFC, NotTrusted, Unencoded)

```csharp

public sealed class OpenCircuitPacket : Packet {

}
```


## CloseCircuit (Fixed 0xFFFFFFFD, NotTrusted, Unencoded)

```csharp

public sealed class CloseCircuitPacket : Packet {

}
```


## StartPingCheck (High 1, NotTrusted, Unencoded)

```csharp

public sealed class StartPingCheckPacket : Packet {

}
```


## CompletePingCheck (High 2, NotTrusted, Unencoded)

```csharp

public sealed class CompletePingCheckPacket : Packet {

}
```


## AddCircuitCode (Low 2, Trusted, Unencoded)

```csharp

public sealed class AddCircuitCodePacket : Packet {

}
```


## UseCircuitCode (Low 3, NotTrusted, Unencoded)

```csharp

public sealed class UseCircuitCodePacket : Packet {

}
```


## NeighborList (High 3, Trusted, Unencoded)

```csharp

public sealed class NeighborListPacket : Packet {

}
```


## AvatarTextureUpdate (Low 4, Trusted, Zerocoded)

```csharp

public sealed class AvatarTextureUpdatePacket : Packet {

}
```


## SimulatorMapUpdate (Low 5, Trusted, Unencoded)

```csharp

public sealed class SimulatorMapUpdatePacket : Packet {

}
```


## SimulatorSetMap (Low 6, Trusted, Unencoded)

```csharp

public sealed class SimulatorSetMapPacket : Packet {

}
```


## SubscribeLoad (Low 7, Trusted, Unencoded)

```csharp

public sealed class SubscribeLoadPacket : Packet {

}
```


## UnsubscribeLoad (Low 8, Trusted, Unencoded)

```csharp

public sealed class UnsubscribeLoadPacket : Packet {

}
```


## SimulatorReady (Low 9, Trusted, Zerocoded)

```csharp

public sealed class SimulatorReadyPacket : Packet {

}
```


## TelehubInfo (Low 10, Trusted, Unencoded)

```csharp

public sealed class TelehubInfoPacket : Packet {

}
```


## SimulatorPresentAtLocation (Low 11, Trusted, Unencoded)

```csharp

public sealed class SimulatorPresentAtLocationPacket : Packet {

}
```


## SimulatorLoad (Low 12, Trusted, Unencoded)

```csharp

public sealed class SimulatorLoadPacket : Packet {

}
```


## SimulatorShutdownRequest (Low 13, Trusted, Unencoded)

```csharp

public sealed class SimulatorShutdownRequestPacket : Packet {

}
```


## RegionPresenceRequestByRegionID (Low 14, Trusted, Unencoded)

```csharp

public sealed class RegionPresenceRequestByRegionIDPacket : Packet {

}
```


## RegionPresenceRequestByHandle (Low 15, Trusted, Unencoded)

```csharp

public sealed class RegionPresenceRequestByHandlePacket : Packet {

}
```


## RegionPresenceResponse (Low 16, Trusted, Zerocoded)

```csharp

public sealed class RegionPresenceResponsePacket : Packet {

}
```


## UpdateSimulator (Low 17, Trusted, Unencoded)

```csharp

public sealed class UpdateSimulatorPacket : Packet {

}
```


## LogDwellTime (Low 18, Trusted, Unencoded)

```csharp

public sealed class LogDwellTimePacket : Packet {

}
```


## FeatureDisabled (Low 19, Trusted, Unencoded)

```csharp

public sealed class FeatureDisabledPacket : Packet {

}
```


## LogFailedMoneyTransaction (Low 20, Trusted, Unencoded)

```csharp

public sealed class LogFailedMoneyTransactionPacket : Packet {

}
```


## UserReportInternal (Low 21, Trusted, Zerocoded)

```csharp

public sealed class UserReportInternalPacket : Packet {

}
```


## SetSimStatusInDatabase (Low 22, Trusted, Unencoded)

```csharp

public sealed class SetSimStatusInDatabasePacket : Packet {

}
```


## SetSimPresenceInDatabase (Low 23, Trusted, Unencoded)

```csharp

public sealed class SetSimPresenceInDatabasePacket : Packet {

}
```


## EconomyDataRequest (Low 24, NotTrusted, Unencoded)

```csharp

public sealed class EconomyDataRequestPacket : Packet {

}
```


## EconomyData (Low 25, Trusted, Zerocoded)

```csharp

public sealed class EconomyDataPacket : Packet {

}
```


## AvatarPickerRequest (Low 26, NotTrusted, Unencoded)

```csharp

public sealed class AvatarPickerRequestPacket : Packet {

}
```


## AvatarPickerRequestBackend (Low 27, Trusted, Unencoded)

```csharp

public sealed class AvatarPickerRequestBackendPacket : Packet {

}
```


## AvatarPickerReply (Low 28, Trusted, Unencoded)

```csharp

public sealed class AvatarPickerReplyPacket : Packet {

}
```


## PlacesQuery (Low 29, NotTrusted, Zerocoded)

```csharp

public sealed class PlacesQueryPacket : Packet {

}
```


## PlacesReply (Low 30, Trusted, Zerocoded)

```csharp

public sealed class PlacesReplyPacket : Packet {

}
```


## DirFindQuery (Low 31, NotTrusted, Zerocoded)

```csharp

public sealed class DirFindQueryPacket : Packet {

}
```


## DirFindQueryBackend (Low 32, Trusted, Zerocoded)

```csharp

public sealed class DirFindQueryBackendPacket : Packet {

}
```


## DirPlacesQuery (Low 33, NotTrusted, Zerocoded)

```csharp

public sealed class DirPlacesQueryPacket : Packet {

}
```


## DirPlacesQueryBackend (Low 34, Trusted, Zerocoded)

```csharp

public sealed class DirPlacesQueryBackendPacket : Packet {

}
```


## DirPlacesReply (Low 35, Trusted, Zerocoded)

```csharp

public sealed class DirPlacesReplyPacket : Packet {

}
```


## DirPeopleReply (Low 36, Trusted, Zerocoded)

```csharp

public sealed class DirPeopleReplyPacket : Packet {

}
```


## DirEventsReply (Low 37, Trusted, Zerocoded)

```csharp

public sealed class DirEventsReplyPacket : Packet {

}
```


## DirGroupsReply (Low 38, Trusted, Zerocoded)

```csharp

public sealed class DirGroupsReplyPacket : Packet {

}
```


## DirClassifiedQuery (Low 39, NotTrusted, Zerocoded)

```csharp

public sealed class DirClassifiedQueryPacket : Packet {

}
```


## DirClassifiedQueryBackend (Low 40, Trusted, Zerocoded)

```csharp

public sealed class DirClassifiedQueryBackendPacket : Packet {

}
```


## DirClassifiedReply (Low 41, Trusted, Zerocoded)

```csharp

public sealed class DirClassifiedReplyPacket : Packet {

}
```


## AvatarClassifiedReply (Low 42, Trusted, Unencoded)

```csharp

public sealed class AvatarClassifiedReplyPacket : Packet {

}
```


## ClassifiedInfoRequest (Low 43, NotTrusted, Zerocoded)

```csharp

public sealed class ClassifiedInfoRequestPacket : Packet {

}
```


## ClassifiedInfoReply (Low 44, Trusted, Unencoded)

```csharp

public sealed class ClassifiedInfoReplyPacket : Packet {

}
```


## ClassifiedInfoUpdate (Low 45, NotTrusted, Unencoded)

```csharp

public sealed class ClassifiedInfoUpdatePacket : Packet {

}
```


## ClassifiedDelete (Low 46, NotTrusted, Unencoded)

```csharp

public sealed class ClassifiedDeletePacket : Packet {

}
```


## ClassifiedGodDelete (Low 47, NotTrusted, Unencoded)

```csharp

public sealed class ClassifiedGodDeletePacket : Packet {

}
```


## DirLandQuery (Low 48, NotTrusted, Zerocoded)

```csharp

public sealed class DirLandQueryPacket : Packet {

}
```


## DirLandQueryBackend (Low 49, Trusted, Zerocoded)

```csharp

public sealed class DirLandQueryBackendPacket : Packet {

}
```


## DirLandReply (Low 50, Trusted, Zerocoded)

```csharp

public sealed class DirLandReplyPacket : Packet {

}
```


## DirPopularQuery (Low 51, NotTrusted, Zerocoded)

```csharp

public sealed class DirPopularQueryPacket : Packet {

}
```


## DirPopularQueryBackend (Low 52, Trusted, Zerocoded)

```csharp

public sealed class DirPopularQueryBackendPacket : Packet {

}
```


## DirPopularReply (Low 53, Trusted, Zerocoded)

```csharp

public sealed class DirPopularReplyPacket : Packet {

}
```


## ParcelInfoRequest (Low 54, NotTrusted, Unencoded)

```csharp

public sealed class ParcelInfoRequestPacket : Packet {

}
```


## ParcelInfoReply (Low 55, Trusted, Zerocoded)

```csharp

public sealed class ParcelInfoReplyPacket : Packet {

}
```


## ParcelObjectOwnersRequest (Low 56, NotTrusted, Unencoded)

```csharp

public sealed class ParcelObjectOwnersRequestPacket : Packet {

}
```


## ParcelObjectOwnersReply (Low 57, Trusted, Zerocoded)

```csharp

public sealed class ParcelObjectOwnersReplyPacket : Packet {

}
```


## GroupNoticesListRequest (Low 58, NotTrusted, Unencoded)

```csharp

public sealed class GroupNoticesListRequestPacket : Packet {

}
```


## GroupNoticesListReply (Low 59, Trusted, Unencoded)

```csharp

public sealed class GroupNoticesListReplyPacket : Packet {

}
```


## GroupNoticeRequest (Low 60, NotTrusted, Unencoded)

```csharp

public sealed class GroupNoticeRequestPacket : Packet {

}
```


## GroupNoticeAdd (Low 61, Trusted, Unencoded)

```csharp

public sealed class GroupNoticeAddPacket : Packet {

}
```


## TeleportRequest (Low 62, NotTrusted, Unencoded)

```csharp

public sealed class TeleportRequestPacket : Packet {

}
```


## TeleportLocationRequest (Low 63, NotTrusted, Unencoded)

```csharp

public sealed class TeleportLocationRequestPacket : Packet {

}
```


## TeleportLocal (Low 64, Trusted, Unencoded)

```csharp

public sealed class TeleportLocalPacket : Packet {

}
```


## TeleportLandmarkRequest (Low 65, NotTrusted, Zerocoded)

```csharp

public sealed class TeleportLandmarkRequestPacket : Packet {

}
```


## TeleportProgress (Low 66, Trusted, Unencoded)

```csharp

public sealed class TeleportProgressPacket : Packet {

}
```


## DataHomeLocationRequest (Low 67, Trusted, Zerocoded)

```csharp

public sealed class DataHomeLocationRequestPacket : Packet {

}
```


## DataHomeLocationReply (Low 68, Trusted, Unencoded)

```csharp

public sealed class DataHomeLocationReplyPacket : Packet {

}
```


## TeleportFinish (Low 69, Trusted, Unencoded)

```csharp

public sealed class TeleportFinishPacket : Packet {

}
```


## StartLure (Low 70, NotTrusted, Unencoded)

```csharp

public sealed class StartLurePacket : Packet {

}
```


## TeleportLureRequest (Low 71, NotTrusted, Unencoded)

```csharp

public sealed class TeleportLureRequestPacket : Packet {

}
```


## TeleportCancel (Low 72, NotTrusted, Unencoded)

```csharp

public sealed class TeleportCancelPacket : Packet {

}
```


## TeleportStart (Low 73, Trusted, Unencoded)

```csharp

public sealed class TeleportStartPacket : Packet {

}
```


## TeleportFailed (Low 74, Trusted, Unencoded)

```csharp

public sealed class TeleportFailedPacket : Packet {

}
```


## Undo (Low 75, NotTrusted, Unencoded)

```csharp

public sealed class UndoPacket : Packet {

}
```


## Redo (Low 76, NotTrusted, Unencoded)

```csharp

public sealed class RedoPacket : Packet {

}
```


## UndoLand (Low 77, NotTrusted, Unencoded)

```csharp

public sealed class UndoLandPacket : Packet {

}
```


## AgentPause (Low 78, NotTrusted, Unencoded)

```csharp

public sealed class AgentPausePacket : Packet {

}
```


## AgentResume (Low 79, NotTrusted, Unencoded)

```csharp

public sealed class AgentResumePacket : Packet {

}
```


## AgentUpdate (High 4, NotTrusted, Zerocoded)

```csharp

public sealed class AgentUpdatePacket : Packet {

}
```


## ChatFromViewer (Low 80, NotTrusted, Zerocoded)

```csharp

public sealed class ChatFromViewerPacket : Packet {

}
```


## AgentThrottle (Low 81, NotTrusted, Zerocoded)

```csharp

public sealed class AgentThrottlePacket : Packet {

}
```


## AgentFOV (Low 82, NotTrusted, Unencoded)

```csharp

public sealed class AgentFOVPacket : Packet {

}
```


## AgentHeightWidth (Low 83, NotTrusted, Unencoded)

```csharp

public sealed class AgentHeightWidthPacket : Packet {

}
```


## AgentSetAppearance (Low 84, NotTrusted, Zerocoded)

```csharp

public sealed class AgentSetAppearancePacket : Packet {

}
```


## AgentAnimation (High 5, NotTrusted, Unencoded)

```csharp

public sealed class AgentAnimationPacket : Packet {

}
```


## AgentRequestSit (High 6, NotTrusted, Zerocoded)

```csharp

public sealed class AgentRequestSitPacket : Packet {

}
```


## AgentSit (High 7, NotTrusted, Unencoded)

```csharp

public sealed class AgentSitPacket : Packet {

}
```


## AgentQuitCopy (Low 85, NotTrusted, Unencoded)

```csharp

public sealed class AgentQuitCopyPacket : Packet {

}
```


## RequestImage (High 8, NotTrusted, Unencoded)

```csharp

public sealed class RequestImagePacket : Packet {

}
```


## ImageNotInDatabase (Low 86, Trusted, Unencoded)

```csharp

public sealed class ImageNotInDatabasePacket : Packet {

}
```


## RebakeAvatarTextures (Low 87, Trusted, Unencoded)

```csharp

public sealed class RebakeAvatarTexturesPacket : Packet {

}
```


## SetAlwaysRun (Low 88, NotTrusted, Unencoded)

```csharp

public sealed class SetAlwaysRunPacket : Packet {

}
```


## ObjectAdd (Medium 1, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectAddPacket : Packet {

}
```


## ObjectDelete (Low 89, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectDeletePacket : Packet {

}
```


## ObjectDuplicate (Low 90, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectDuplicatePacket : Packet {

}
```


## ObjectDuplicateOnRay (Low 91, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectDuplicateOnRayPacket : Packet {

}
```


## MultipleObjectUpdate (Medium 2, NotTrusted, Zerocoded)

```csharp

public sealed class MultipleObjectUpdatePacket : Packet {

}
```


## RequestMultipleObjects (Medium 3, NotTrusted, Zerocoded)

```csharp

public sealed class RequestMultipleObjectsPacket : Packet {

}
```


## ObjectPosition (Medium 4, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectPositionPacket : Packet {

}
```


## ObjectScale (Low 92, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectScalePacket : Packet {

}
```


## ObjectRotation (Low 93, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectRotationPacket : Packet {

}
```


## ObjectFlagUpdate (Low 94, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectFlagUpdatePacket : Packet {

}
```


## ObjectClickAction (Low 95, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectClickActionPacket : Packet {

}
```


## ObjectImage (Low 96, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectImagePacket : Packet {

}
```


## ObjectBypassModUpdate (Low 431, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectBypassModUpdatePacket : Packet {

}
```


## ObjectMaterial (Low 97, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectMaterialPacket : Packet {

}
```


## ObjectShape (Low 98, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectShapePacket : Packet {

}
```


## ObjectExtraParams (Low 99, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectExtraParamsPacket : Packet {

}
```


## ObjectOwner (Low 100, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectOwnerPacket : Packet {

}
```


## ObjectGroup (Low 101, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectGroupPacket : Packet {

}
```


## ObjectBuy (Low 102, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectBuyPacket : Packet {

}
```


## BuyObjectInventory (Low 103, NotTrusted, Zerocoded)

```csharp

public sealed class BuyObjectInventoryPacket : Packet {

}
```


## DerezContainer (Low 104, Trusted, Zerocoded)

```csharp

public sealed class DerezContainerPacket : Packet {

}
```


## ObjectPermissions (Low 105, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectPermissionsPacket : Packet {

}
```


## ObjectSaleInfo (Low 106, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectSaleInfoPacket : Packet {

}
```


## ObjectName (Low 107, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectNamePacket : Packet {

}
```


## ObjectDescription (Low 108, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectDescriptionPacket : Packet {

}
```


## ObjectCategory (Low 109, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectCategoryPacket : Packet {

}
```


## ObjectSelect (Low 110, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectSelectPacket : Packet {

}
```


## ObjectDeselect (Low 111, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectDeselectPacket : Packet {

}
```


## ObjectAttach (Low 112, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectAttachPacket : Packet {

}
```


## ObjectDetach (Low 113, NotTrusted, Unencoded)

```csharp

public sealed class ObjectDetachPacket : Packet {

}
```


## ObjectDrop (Low 114, NotTrusted, Unencoded)

```csharp

public sealed class ObjectDropPacket : Packet {

}
```


## ObjectLink (Low 115, NotTrusted, Unencoded)

```csharp

public sealed class ObjectLinkPacket : Packet {

}
```


## ObjectDelink (Low 116, NotTrusted, Unencoded)

```csharp

public sealed class ObjectDelinkPacket : Packet {

}
```


## ObjectGrab (Low 117, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectGrabPacket : Packet {

}
```


## ObjectGrabUpdate (Low 118, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectGrabUpdatePacket : Packet {

}
```


## ObjectDeGrab (Low 119, NotTrusted, Unencoded)

```csharp

public sealed class ObjectDeGrabPacket : Packet {

}
```


## ObjectSpinStart (Low 120, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectSpinStartPacket : Packet {

}
```


## ObjectSpinUpdate (Low 121, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectSpinUpdatePacket : Packet {

}
```


## ObjectSpinStop (Low 122, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectSpinStopPacket : Packet {

}
```


## ObjectExportSelected (Low 123, NotTrusted, Zerocoded)

```csharp

public sealed class ObjectExportSelectedPacket : Packet {

}
```


## ModifyLand (Low 124, NotTrusted, Zerocoded)

```csharp

public sealed class ModifyLandPacket : Packet {

}
```


## VelocityInterpolateOn (Low 125, NotTrusted, Unencoded)

```csharp

public sealed class VelocityInterpolateOnPacket : Packet {

}
```


## VelocityInterpolateOff (Low 126, NotTrusted, Unencoded)

```csharp

public sealed class VelocityInterpolateOffPacket : Packet {

}
```


## StateSave (Low 127, NotTrusted, Unencoded)

```csharp

public sealed class StateSavePacket : Packet {

}
```


## ReportAutosaveCrash (Low 128, NotTrusted, Unencoded)

```csharp

public sealed class ReportAutosaveCrashPacket : Packet {

}
```


## SimWideDeletes (Low 129, NotTrusted, Unencoded)

```csharp

public sealed class SimWideDeletesPacket : Packet {

}
```


## RequestObjectPropertiesFamily (Medium 5, NotTrusted, Zerocoded)

```csharp

public sealed class RequestObjectPropertiesFamilyPacket : Packet {

}
```


## TrackAgent (Low 130, NotTrusted, Unencoded)

```csharp

public sealed class TrackAgentPacket : Packet {

}
```


## ViewerStats (Low 131, NotTrusted, Zerocoded)

```csharp

public sealed class ViewerStatsPacket : Packet {

}
```


## ScriptAnswerYes (Low 132, NotTrusted, Unencoded)

```csharp

public sealed class ScriptAnswerYesPacket : Packet {

}
```


## UserReport (Low 133, NotTrusted, Zerocoded)

```csharp

public sealed class UserReportPacket : Packet {

}
```


## AlertMessage (Low 134, Trusted, Unencoded)

```csharp

public sealed class AlertMessagePacket : Packet {

}
```


## AgentAlertMessage (Low 135, Trusted, Unencoded)

```csharp

public sealed class AgentAlertMessagePacket : Packet {

}
```


## MeanCollisionAlert (Low 136, Trusted, Zerocoded)

```csharp

public sealed class MeanCollisionAlertPacket : Packet {

}
```


## ViewerFrozenMessage (Low 137, Trusted, Unencoded)

```csharp

public sealed class ViewerFrozenMessagePacket : Packet {

}
```


## HealthMessage (Low 138, Trusted, Zerocoded)

```csharp

public sealed class HealthMessagePacket : Packet {

}
```


## ChatFromSimulator (Low 139, Trusted, Unencoded)

```csharp

public sealed class ChatFromSimulatorPacket : Packet {

}
```


## SimStats (Low 140, Trusted, Unencoded)

```csharp

public sealed class SimStatsPacket : Packet {

}
```


## RequestRegionInfo (Low 141, NotTrusted, Unencoded)

```csharp

public sealed class RequestRegionInfoPacket : Packet {

}
```


## RegionInfo (Low 142, NotTrusted, Zerocoded)

```csharp

public sealed class RegionInfoPacket : Packet {

}
```


## GodUpdateRegionInfo (Low 143, NotTrusted, Zerocoded)

```csharp

public sealed class GodUpdateRegionInfoPacket : Packet {

}
```


## NearestLandingRegionRequest (Low 144, Trusted, Unencoded)

```csharp

public sealed class NearestLandingRegionRequestPacket : Packet {

}
```


## NearestLandingRegionReply (Low 145, Trusted, Unencoded)

```csharp

public sealed class NearestLandingRegionReplyPacket : Packet {

}
```


## NearestLandingRegionUpdated (Low 146, Trusted, Unencoded)

```csharp

public sealed class NearestLandingRegionUpdatedPacket : Packet {

}
```


## TeleportLandingStatusChanged (Low 147, Trusted, Unencoded)

```csharp

public sealed class TeleportLandingStatusChangedPacket : Packet {

}
```


## RegionHandshake (Low 148, Trusted, Zerocoded)

```csharp

public sealed class RegionHandshakePacket : Packet {

}
```


## RegionHandshakeReply (Low 149, NotTrusted, Zerocoded)

```csharp

public sealed class RegionHandshakeReplyPacket : Packet {

}
```


## CoarseLocationUpdate (Medium 6, Trusted, Unencoded)

```csharp

public sealed class CoarseLocationUpdatePacket : Packet {

}
```


## ImageData (High 9, Trusted, Unencoded)

```csharp

public sealed class ImageDataPacket : Packet {

}
```


## ImagePacket (High 10, Trusted, Unencoded)

```csharp

public sealed class ImagePacketPacket : Packet {

}
```


## LayerData (High 11, Trusted, Unencoded)

```csharp

public sealed class LayerDataPacket : Packet {

}
```


## ObjectUpdate (High 12, Trusted, Zerocoded)

```csharp

public sealed class ObjectUpdatePacket : Packet {

}
```


## ObjectUpdateCompressed (High 13, Trusted, Unencoded)

```csharp

public sealed class ObjectUpdateCompressedPacket : Packet {

}
```


## ObjectUpdateCached (High 14, Trusted, Unencoded)

```csharp

public sealed class ObjectUpdateCachedPacket : Packet {

}
```


## ImprovedTerseObjectUpdate (High 15, Trusted, Unencoded)

```csharp

public sealed class ImprovedTerseObjectUpdatePacket : Packet {

}
```


## KillObject (High 16, Trusted, Unencoded)

```csharp

public sealed class KillObjectPacket : Packet {

}
```


## CrossedRegion (Medium 7, Trusted, Unencoded)

```csharp

public sealed class CrossedRegionPacket : Packet {

}
```


## SimulatorViewerTimeMessage (Low 150, Trusted, Unencoded)

```csharp

public sealed class SimulatorViewerTimeMessagePacket : Packet {

}
```


## EnableSimulator (Low 151, Trusted, Unencoded)

```csharp

public sealed class EnableSimulatorPacket : Packet {

}
```


## DisableSimulator (Low 152, Trusted, Unencoded)

```csharp

public sealed class DisableSimulatorPacket : Packet {

}
```


## ConfirmEnableSimulator (Medium 8, Trusted, Unencoded)

```csharp

public sealed class ConfirmEnableSimulatorPacket : Packet {

}
```


## TransferRequest (Low 153, NotTrusted, Zerocoded)

```csharp

public sealed class TransferRequestPacket : Packet {

}
```


## TransferInfo (Low 154, NotTrusted, Zerocoded)

```csharp

public sealed class TransferInfoPacket : Packet {

}
```


## TransferPacket (High 17, NotTrusted, Unencoded)

```csharp

public sealed class TransferPacketPacket : Packet {

}
```


## TransferAbort (Low 155, NotTrusted, Zerocoded)

```csharp

public sealed class TransferAbortPacket : Packet {

}
```


## RequestXfer (Low 156, NotTrusted, Zerocoded)

```csharp

public sealed class RequestXferPacket : Packet {

}
```


## SendXferPacket (High 18, NotTrusted, Unencoded)

```csharp

public sealed class SendXferPacketPacket : Packet {

}
```


## ConfirmXferPacket (High 19, NotTrusted, Unencoded)

```csharp

public sealed class ConfirmXferPacketPacket : Packet {

}
```


## AbortXfer (Low 157, NotTrusted, Unencoded)

```csharp

public sealed class AbortXferPacket : Packet {

}
```


## AvatarAnimation (High 20, Trusted, Unencoded)

```csharp

public sealed class AvatarAnimationPacket : Packet {

}
```


## AvatarAppearance (Low 158, Trusted, Zerocoded)

```csharp

public sealed class AvatarAppearancePacket : Packet {

}
```


## AvatarSitResponse (High 21, Trusted, Zerocoded)

```csharp

public sealed class AvatarSitResponsePacket : Packet {

}
```


## SetFollowCamProperties (Low 159, Trusted, Unencoded)

```csharp

public sealed class SetFollowCamPropertiesPacket : Packet {

}
```


## ClearFollowCamProperties (Low 160, Trusted, Unencoded)

```csharp

public sealed class ClearFollowCamPropertiesPacket : Packet {

}
```


## CameraConstraint (High 22, Trusted, Zerocoded)

```csharp

public sealed class CameraConstraintPacket : Packet {

}
```


## ObjectProperties (Medium 9, Trusted, Zerocoded)

```csharp

public sealed class ObjectPropertiesPacket : Packet {

}
```


## ObjectPropertiesFamily (Medium 10, Trusted, Zerocoded)

```csharp

public sealed class ObjectPropertiesFamilyPacket : Packet {

}
```


## RequestPayPrice (Low 161, NotTrusted, Unencoded)

```csharp

public sealed class RequestPayPricePacket : Packet {

}
```


## PayPriceReply (Low 162, Trusted, Unencoded)

```csharp

public sealed class PayPriceReplyPacket : Packet {

}
```


## KickUser (Low 163, Trusted, Unencoded)

```csharp

public sealed class KickUserPacket : Packet {

}
```


## KickUserAck (Low 164, Trusted, Unencoded)

```csharp

public sealed class KickUserAckPacket : Packet {

}
```


## GodKickUser (Low 165, NotTrusted, Unencoded)

```csharp

public sealed class GodKickUserPacket : Packet {

}
```


## SystemKickUser (Low 166, Trusted, Unencoded)

```csharp

public sealed class SystemKickUserPacket : Packet {

}
```


## EjectUser (Low 167, NotTrusted, Unencoded)

```csharp

public sealed class EjectUserPacket : Packet {

}
```


## FreezeUser (Low 168, NotTrusted, Unencoded)

```csharp

public sealed class FreezeUserPacket : Packet {

}
```


## AvatarPropertiesRequest (Low 169, NotTrusted, Unencoded)

```csharp

public sealed class AvatarPropertiesRequestPacket : Packet {

}
```


## AvatarPropertiesRequestBackend (Low 170, Trusted, Unencoded)

```csharp

public sealed class AvatarPropertiesRequestBackendPacket : Packet {

}
```


## AvatarPropertiesReply (Low 171, Trusted, Zerocoded)

```csharp

public sealed class AvatarPropertiesReplyPacket : Packet {

}
```


## AvatarInterestsReply (Low 172, Trusted, Zerocoded)

```csharp

public sealed class AvatarInterestsReplyPacket : Packet {

}
```


## AvatarGroupsReply (Low 173, Trusted, Zerocoded)

```csharp

public sealed class AvatarGroupsReplyPacket : Packet {

}
```


## AvatarPropertiesUpdate (Low 174, NotTrusted, Zerocoded)

```csharp

public sealed class AvatarPropertiesUpdatePacket : Packet {

}
```


## AvatarInterestsUpdate (Low 175, NotTrusted, Zerocoded)

```csharp

public sealed class AvatarInterestsUpdatePacket : Packet {

}
```


## AvatarNotesReply (Low 176, Trusted, Unencoded)

```csharp

public sealed class AvatarNotesReplyPacket : Packet {

}
```


## AvatarNotesUpdate (Low 177, NotTrusted, Unencoded)

```csharp

public sealed class AvatarNotesUpdatePacket : Packet {

}
```


## AvatarPicksReply (Low 178, Trusted, Unencoded)

```csharp

public sealed class AvatarPicksReplyPacket : Packet {

}
```


## EventInfoRequest (Low 179, NotTrusted, Unencoded)

```csharp

public sealed class EventInfoRequestPacket : Packet {

}
```


## EventInfoReply (Low 180, Trusted, Unencoded)

```csharp

public sealed class EventInfoReplyPacket : Packet {

}
```


## EventNotificationAddRequest (Low 181, NotTrusted, Unencoded)

```csharp

public sealed class EventNotificationAddRequestPacket : Packet {

}
```


## EventNotificationRemoveRequest (Low 182, NotTrusted, Unencoded)

```csharp

public sealed class EventNotificationRemoveRequestPacket : Packet {

}
```


## EventGodDelete (Low 183, NotTrusted, Unencoded)

```csharp

public sealed class EventGodDeletePacket : Packet {

}
```


## PickInfoReply (Low 184, Trusted, Unencoded)

```csharp

public sealed class PickInfoReplyPacket : Packet {

}
```


## PickInfoUpdate (Low 185, NotTrusted, Unencoded)

```csharp

public sealed class PickInfoUpdatePacket : Packet {

}
```


## PickDelete (Low 186, NotTrusted, Unencoded)

```csharp

public sealed class PickDeletePacket : Packet {

}
```


## PickGodDelete (Low 187, NotTrusted, Unencoded)

```csharp

public sealed class PickGodDeletePacket : Packet {

}
```


## ScriptQuestion (Low 188, Trusted, Unencoded)

```csharp

public sealed class ScriptQuestionPacket : Packet {

}
```


## ScriptControlChange (Low 189, Trusted, Unencoded)

```csharp

public sealed class ScriptControlChangePacket : Packet {

}
```


## ScriptDialog (Low 190, Trusted, Zerocoded)

```csharp

public sealed class ScriptDialogPacket : Packet {

}
```


## ScriptDialogReply (Low 191, NotTrusted, Zerocoded)

```csharp

public sealed class ScriptDialogReplyPacket : Packet {

}
```


## ForceScriptControlRelease (Low 192, NotTrusted, Unencoded)

```csharp

public sealed class ForceScriptControlReleasePacket : Packet {

}
```


## RevokePermissions (Low 193, NotTrusted, Unencoded)

```csharp

public sealed class RevokePermissionsPacket : Packet {

}
```


## LoadURL (Low 194, Trusted, Unencoded)

```csharp

public sealed class LoadURLPacket : Packet {

}
```


## ScriptTeleportRequest (Low 195, Trusted, Unencoded)

```csharp

public sealed class ScriptTeleportRequestPacket : Packet {

}
```


## ParcelOverlay (Low 196, Trusted, Zerocoded)

```csharp

public sealed class ParcelOverlayPacket : Packet {

}
```


## ParcelPropertiesRequest (Medium 11, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelPropertiesRequestPacket : Packet {

}
```


## ParcelPropertiesRequestByID (Low 197, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelPropertiesRequestByIDPacket : Packet {

}
```


## ParcelProperties (High 23, Trusted, Zerocoded)

```csharp

public sealed class ParcelPropertiesPacket : Packet {

}
```


## ParcelPropertiesUpdate (Low 198, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelPropertiesUpdatePacket : Packet {

}
```


## ParcelReturnObjects (Low 199, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelReturnObjectsPacket : Packet {

}
```


## ParcelSetOtherCleanTime (Low 200, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelSetOtherCleanTimePacket : Packet {

}
```


## ParcelDisableObjects (Low 201, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelDisableObjectsPacket : Packet {

}
```


## ParcelSelectObjects (Low 202, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelSelectObjectsPacket : Packet {

}
```


## EstateCovenantRequest (Low 203, NotTrusted, Unencoded)

```csharp

public sealed class EstateCovenantRequestPacket : Packet {

}
```


## EstateCovenantReply (Low 204, Trusted, Unencoded)

```csharp

public sealed class EstateCovenantReplyPacket : Packet {

}
```


## ForceObjectSelect (Low 205, Trusted, Unencoded)

```csharp

public sealed class ForceObjectSelectPacket : Packet {

}
```


## ParcelBuyPass (Low 206, NotTrusted, Unencoded)

```csharp

public sealed class ParcelBuyPassPacket : Packet {

}
```


## ParcelDeedToGroup (Low 207, NotTrusted, Unencoded)

```csharp

public sealed class ParcelDeedToGroupPacket : Packet {

}
```


## ParcelReclaim (Low 208, NotTrusted, Unencoded)

```csharp

public sealed class ParcelReclaimPacket : Packet {

}
```


## ParcelClaim (Low 209, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelClaimPacket : Packet {

}
```


## ParcelJoin (Low 210, NotTrusted, Unencoded)

```csharp

public sealed class ParcelJoinPacket : Packet {

}
```


## ParcelDivide (Low 211, NotTrusted, Unencoded)

```csharp

public sealed class ParcelDividePacket : Packet {

}
```


## ParcelRelease (Low 212, NotTrusted, Unencoded)

```csharp

public sealed class ParcelReleasePacket : Packet {

}
```


## ParcelBuy (Low 213, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelBuyPacket : Packet {

}
```


## ParcelGodForceOwner (Low 214, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelGodForceOwnerPacket : Packet {

}
```


## ParcelAccessListRequest (Low 215, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelAccessListRequestPacket : Packet {

}
```


## ParcelAccessListReply (Low 216, Trusted, Zerocoded)

```csharp

public sealed class ParcelAccessListReplyPacket : Packet {

}
```


## ParcelAccessListUpdate (Low 217, NotTrusted, Zerocoded)

```csharp

public sealed class ParcelAccessListUpdatePacket : Packet {

}
```


## ParcelDwellRequest (Low 218, NotTrusted, Unencoded)

```csharp

public sealed class ParcelDwellRequestPacket : Packet {

}
```


## ParcelDwellReply (Low 219, Trusted, Unencoded)

```csharp

public sealed class ParcelDwellReplyPacket : Packet {

}
```


## RequestParcelTransfer (Low 220, Trusted, Zerocoded)

```csharp

public sealed class RequestParcelTransferPacket : Packet {

}
```


## UpdateParcel (Low 221, Trusted, Zerocoded)

```csharp

public sealed class UpdateParcelPacket : Packet {

}
```


## RemoveParcel (Low 222, Trusted, Unencoded)

```csharp

public sealed class RemoveParcelPacket : Packet {

}
```


## MergeParcel (Low 223, Trusted, Unencoded)

```csharp

public sealed class MergeParcelPacket : Packet {

}
```


## LogParcelChanges (Low 224, Trusted, Zerocoded)

```csharp

public sealed class LogParcelChangesPacket : Packet {

}
```


## CheckParcelSales (Low 225, Trusted, Unencoded)

```csharp

public sealed class CheckParcelSalesPacket : Packet {

}
```


## ParcelSales (Low 226, Trusted, Unencoded)

```csharp

public sealed class ParcelSalesPacket : Packet {

}
```


## ParcelGodMarkAsContent (Low 227, NotTrusted, Unencoded)

```csharp

public sealed class ParcelGodMarkAsContentPacket : Packet {

}
```


## ViewerStartAuction (Low 228, NotTrusted, Unencoded)

```csharp

public sealed class ViewerStartAuctionPacket : Packet {

}
```


## StartAuction (Low 229, Trusted, Unencoded)

```csharp

public sealed class StartAuctionPacket : Packet {

}
```


## ConfirmAuctionStart (Low 230, Trusted, Unencoded)

```csharp

public sealed class ConfirmAuctionStartPacket : Packet {

}
```


## CompleteAuction (Low 231, Trusted, Unencoded)

```csharp

public sealed class CompleteAuctionPacket : Packet {

}
```


## CancelAuction (Low 232, Trusted, Unencoded)

```csharp

public sealed class CancelAuctionPacket : Packet {

}
```


## CheckParcelAuctions (Low 233, Trusted, Unencoded)

```csharp

public sealed class CheckParcelAuctionsPacket : Packet {

}
```


## ParcelAuctions (Low 234, Trusted, Unencoded)

```csharp

public sealed class ParcelAuctionsPacket : Packet {

}
```


## UUIDNameRequest (Low 235, NotTrusted, Unencoded)

```csharp

public sealed class UUIDNameRequestPacket : Packet {

}
```


## UUIDNameReply (Low 236, Trusted, Unencoded)

```csharp

public sealed class UUIDNameReplyPacket : Packet {

}
```


## UUIDGroupNameRequest (Low 237, NotTrusted, Unencoded)

```csharp

public sealed class UUIDGroupNameRequestPacket : Packet {

}
```


## UUIDGroupNameReply (Low 238, Trusted, Unencoded)

```csharp

public sealed class UUIDGroupNameReplyPacket : Packet {

}
```


## ChatPass (Low 239, Trusted, Zerocoded)

```csharp

public sealed class ChatPassPacket : Packet {

}
```


## EdgeDataPacket (High 24, Trusted, Zerocoded)

```csharp

public sealed class EdgeDataPacketPacket : Packet {

}
```


## SimStatus (Medium 12, Trusted, Unencoded)

```csharp

public sealed class SimStatusPacket : Packet {

}
```


## ChildAgentUpdate (High 25, Trusted, Zerocoded)

```csharp

public sealed class ChildAgentUpdatePacket : Packet {

}
```


## ChildAgentAlive (High 26, Trusted, Unencoded)

```csharp

public sealed class ChildAgentAlivePacket : Packet {

}
```


## ChildAgentPositionUpdate (High 27, Trusted, Unencoded)

```csharp

public sealed class ChildAgentPositionUpdatePacket : Packet {

}
```


## ChildAgentDying (Low 240, Trusted, Zerocoded)

```csharp

public sealed class ChildAgentDyingPacket : Packet {

}
```


## ChildAgentUnknown (Low 241, Trusted, Unencoded)

```csharp

public sealed class ChildAgentUnknownPacket : Packet {

}
```


## AtomicPassObject (High 28, Trusted, Unencoded)

```csharp

public sealed class AtomicPassObjectPacket : Packet {

}
```


## KillChildAgents (Low 242, Trusted, Unencoded)

```csharp

public sealed class KillChildAgentsPacket : Packet {

}
```


## GetScriptRunning (Low 243, NotTrusted, Unencoded)

```csharp

public sealed class GetScriptRunningPacket : Packet {

}
```


## ScriptRunningReply (Low 244, NotTrusted, Unencoded)

```csharp

public sealed class ScriptRunningReplyPacket : Packet {

}
```


## SetScriptRunning (Low 245, NotTrusted, Unencoded)

```csharp

public sealed class SetScriptRunningPacket : Packet {

}
```


## ScriptReset (Low 246, NotTrusted, Unencoded)

```csharp

public sealed class ScriptResetPacket : Packet {

}
```


## ScriptSensorRequest (Low 247, Trusted, Zerocoded)

```csharp

public sealed class ScriptSensorRequestPacket : Packet {

}
```


## ScriptSensorReply (Low 248, Trusted, Zerocoded)

```csharp

public sealed class ScriptSensorReplyPacket : Packet {

}
```


## CompleteAgentMovement (Low 249, NotTrusted, Unencoded)

```csharp

public sealed class CompleteAgentMovementPacket : Packet {

}
```


## AgentMovementComplete (Low 250, NotTrusted, Unencoded)

```csharp

public sealed class AgentMovementCompletePacket : Packet {

}
```


## DataServerLogout (Low 251, Trusted, Unencoded)

```csharp

public sealed class DataServerLogoutPacket : Packet {

}
```


## LogoutRequest (Low 252, NotTrusted, Unencoded)

```csharp

public sealed class LogoutRequestPacket : Packet {

}
```


## LogoutReply (Low 253, Trusted, Zerocoded)

```csharp

public sealed class LogoutReplyPacket : Packet {

}
```


## ImprovedInstantMessage (Low 254, NotTrusted, Zerocoded)

```csharp

public sealed class ImprovedInstantMessagePacket : Packet {

}
```


## RetrieveInstantMessages (Low 255, NotTrusted, Unencoded)

```csharp

public sealed class RetrieveInstantMessagesPacket : Packet {

}
```


## FindAgent (Low 256, NotTrusted, Unencoded)

```csharp

public sealed class FindAgentPacket : Packet {

}
```


## RequestGodlikePowers (Low 257, NotTrusted, Unencoded)

```csharp

public sealed class RequestGodlikePowersPacket : Packet {

}
```


## GrantGodlikePowers (Low 258, Trusted, Unencoded)

```csharp

public sealed class GrantGodlikePowersPacket : Packet {

}
```


## GodlikeMessage (Low 259, NotTrusted, Zerocoded)

```csharp

public sealed class GodlikeMessagePacket : Packet {

}
```


## EstateOwnerMessage (Low 260, NotTrusted, Zerocoded)

```csharp

public sealed class EstateOwnerMessagePacket : Packet {

}
```


## GenericMessage (Low 261, NotTrusted, Zerocoded)

```csharp

public sealed class GenericMessagePacket : Packet {

}
```


## GenericStreamingMessage (High 31, Trusted, Unencoded)

```csharp

public sealed class GenericStreamingMessagePacket : Packet {

}
```


## LargeGenericMessage (Low 430, NotTrusted, Unencoded)

```csharp

public sealed class LargeGenericMessagePacket : Packet {

}
```


## MuteListRequest (Low 262, NotTrusted, Unencoded)

```csharp

public sealed class MuteListRequestPacket : Packet {

}
```


## UpdateMuteListEntry (Low 263, NotTrusted, Unencoded)

```csharp

public sealed class UpdateMuteListEntryPacket : Packet {

}
```


## RemoveMuteListEntry (Low 264, NotTrusted, Unencoded)

```csharp

public sealed class RemoveMuteListEntryPacket : Packet {

}
```


## CopyInventoryFromNotecard (Low 265, NotTrusted, Zerocoded)

```csharp

public sealed class CopyInventoryFromNotecardPacket : Packet {

}
```


## UpdateInventoryItem (Low 266, NotTrusted, Zerocoded)

```csharp

public sealed class UpdateInventoryItemPacket : Packet {

}
```


## UpdateCreateInventoryItem (Low 267, Trusted, Zerocoded)

```csharp

public sealed class UpdateCreateInventoryItemPacket : Packet {

}
```


## MoveInventoryItem (Low 268, NotTrusted, Zerocoded)

```csharp

public sealed class MoveInventoryItemPacket : Packet {

}
```


## CopyInventoryItem (Low 269, NotTrusted, Zerocoded)

```csharp

public sealed class CopyInventoryItemPacket : Packet {

}
```


## RemoveInventoryItem (Low 270, NotTrusted, Unencoded)

```csharp

public sealed class RemoveInventoryItemPacket : Packet {

}
```


## ChangeInventoryItemFlags (Low 271, NotTrusted, Unencoded)

```csharp

public sealed class ChangeInventoryItemFlagsPacket : Packet {

}
```


## SaveAssetIntoInventory (Low 272, Trusted, Unencoded)

```csharp

public sealed class SaveAssetIntoInventoryPacket : Packet {

}
```


## CreateInventoryFolder (Low 273, NotTrusted, Unencoded)

```csharp

public sealed class CreateInventoryFolderPacket : Packet {

}
```


## UpdateInventoryFolder (Low 274, NotTrusted, Unencoded)

```csharp

public sealed class UpdateInventoryFolderPacket : Packet {

}
```


## MoveInventoryFolder (Low 275, NotTrusted, Zerocoded)

```csharp

public sealed class MoveInventoryFolderPacket : Packet {

}
```


## RemoveInventoryFolder (Low 276, NotTrusted, Unencoded)

```csharp

public sealed class RemoveInventoryFolderPacket : Packet {

}
```


## FetchInventoryDescendents (Low 277, NotTrusted, Zerocoded)

```csharp

public sealed class FetchInventoryDescendentsPacket : Packet {

}
```


## InventoryDescendents (Low 278, Trusted, Zerocoded)

```csharp

public sealed class InventoryDescendentsPacket : Packet {

}
```


## FetchInventory (Low 279, NotTrusted, Zerocoded)

```csharp

public sealed class FetchInventoryPacket : Packet {

}
```


## FetchInventoryReply (Low 280, Trusted, Zerocoded)

```csharp

public sealed class FetchInventoryReplyPacket : Packet {

}
```


## BulkUpdateInventory (Low 281, Trusted, Zerocoded)

```csharp

public sealed class BulkUpdateInventoryPacket : Packet {

}
```


## RequestInventoryAsset (Low 282, Trusted, Unencoded)

```csharp

public sealed class RequestInventoryAssetPacket : Packet {

}
```


## InventoryAssetResponse (Low 283, Trusted, Unencoded)

```csharp

public sealed class InventoryAssetResponsePacket : Packet {

}
```


## RemoveInventoryObjects (Low 284, NotTrusted, Unencoded)

```csharp

public sealed class RemoveInventoryObjectsPacket : Packet {

}
```


## PurgeInventoryDescendents (Low 285, NotTrusted, Zerocoded)

```csharp

public sealed class PurgeInventoryDescendentsPacket : Packet {

}
```


## UpdateTaskInventory (Low 286, NotTrusted, Zerocoded)

```csharp

public sealed class UpdateTaskInventoryPacket : Packet {

}
```


## RemoveTaskInventory (Low 287, NotTrusted, Zerocoded)

```csharp

public sealed class RemoveTaskInventoryPacket : Packet {

}
```


## MoveTaskInventory (Low 288, NotTrusted, Unencoded)

```csharp

public sealed class MoveTaskInventoryPacket : Packet {

}
```


## RequestTaskInventory (Low 289, NotTrusted, Unencoded)

```csharp

public sealed class RequestTaskInventoryPacket : Packet {

}
```


## ReplyTaskInventory (Low 290, Trusted, Zerocoded)

```csharp

public sealed class ReplyTaskInventoryPacket : Packet {

}
```


## DeRezObject (Low 291, NotTrusted, Zerocoded)

```csharp

public sealed class DeRezObjectPacket : Packet {

}
```


## DeRezAck (Low 292, Trusted, Unencoded)

```csharp

public sealed class DeRezAckPacket : Packet {

}
```


## RezObject (Low 293, NotTrusted, Zerocoded)

```csharp

public sealed class RezObjectPacket : Packet {

}
```


## RezObjectFromNotecard (Low 294, NotTrusted, Zerocoded)

```csharp

public sealed class RezObjectFromNotecardPacket : Packet {

}
```


## TransferInventory (Low 295, Trusted, Zerocoded)

```csharp

public sealed class TransferInventoryPacket : Packet {

}
```


## TransferInventoryAck (Low 296, Trusted, Zerocoded)

```csharp

public sealed class TransferInventoryAckPacket : Packet {

}
```


## AcceptFriendship (Low 297, NotTrusted, Unencoded)

```csharp

public sealed class AcceptFriendshipPacket : Packet {

}
```


## DeclineFriendship (Low 298, NotTrusted, Unencoded)

```csharp

public sealed class DeclineFriendshipPacket : Packet {

}
```


## FormFriendship (Low 299, Trusted, Unencoded)

```csharp

public sealed class FormFriendshipPacket : Packet {

}
```


## TerminateFriendship (Low 300, NotTrusted, Unencoded)

```csharp

public sealed class TerminateFriendshipPacket : Packet {

}
```


## OfferCallingCard (Low 301, NotTrusted, Unencoded)

```csharp

public sealed class OfferCallingCardPacket : Packet {

}
```


## AcceptCallingCard (Low 302, NotTrusted, Unencoded)

```csharp

public sealed class AcceptCallingCardPacket : Packet {

}
```


## DeclineCallingCard (Low 303, NotTrusted, Unencoded)

```csharp

public sealed class DeclineCallingCardPacket : Packet {

}
```


## RezScript (Low 304, NotTrusted, Zerocoded)

```csharp

public sealed class RezScriptPacket : Packet {

}
```


## CreateInventoryItem (Low 305, NotTrusted, Zerocoded)

```csharp

public sealed class CreateInventoryItemPacket : Packet {

}
```


## CreateLandmarkForEvent (Low 306, NotTrusted, Zerocoded)

```csharp

public sealed class CreateLandmarkForEventPacket : Packet {

}
```


## EventLocationRequest (Low 307, Trusted, Zerocoded)

```csharp

public sealed class EventLocationRequestPacket : Packet {

}
```


## EventLocationReply (Low 308, Trusted, Zerocoded)

```csharp

public sealed class EventLocationReplyPacket : Packet {

}
```


## RegionHandleRequest (Low 309, NotTrusted, Unencoded)

```csharp

public sealed class RegionHandleRequestPacket : Packet {

}
```


## RegionIDAndHandleReply (Low 310, Trusted, Unencoded)

```csharp

public sealed class RegionIDAndHandleReplyPacket : Packet {

}
```


## MoneyTransferRequest (Low 311, NotTrusted, Zerocoded)

```csharp

public sealed class MoneyTransferRequestPacket : Packet {

}
```


## MoneyTransferBackend (Low 312, Trusted, Zerocoded)

```csharp

public sealed class MoneyTransferBackendPacket : Packet {

}
```


## MoneyBalanceRequest (Low 313, NotTrusted, Zerocoded)

```csharp

public sealed class MoneyBalanceRequestPacket : Packet {

}
```


## MoneyBalanceReply (Low 314, Trusted, Zerocoded)

```csharp

public sealed class MoneyBalanceReplyPacket : Packet {

}
```


## RoutedMoneyBalanceReply (Low 315, Trusted, Zerocoded)

```csharp

public sealed class RoutedMoneyBalanceReplyPacket : Packet {

}
```


## ActivateGestures (Low 316, NotTrusted, Unencoded)

```csharp

public sealed class ActivateGesturesPacket : Packet {

}
```


## DeactivateGestures (Low 317, NotTrusted, Unencoded)

```csharp

public sealed class DeactivateGesturesPacket : Packet {

}
```


## MuteListUpdate (Low 318, Trusted, Unencoded)

```csharp

public sealed class MuteListUpdatePacket : Packet {

}
```


## UseCachedMuteList (Low 319, NotTrusted, Unencoded)

```csharp

public sealed class UseCachedMuteListPacket : Packet {

}
```


## GrantUserRights (Low 320, NotTrusted, Unencoded)

```csharp

public sealed class GrantUserRightsPacket : Packet {

}
```


## ChangeUserRights (Low 321, Trusted, Unencoded)

```csharp

public sealed class ChangeUserRightsPacket : Packet {

}
```


## OnlineNotification (Low 322, Trusted, Unencoded)

```csharp

public sealed class OnlineNotificationPacket : Packet {

}
```


## OfflineNotification (Low 323, Trusted, Unencoded)

```csharp

public sealed class OfflineNotificationPacket : Packet {

}
```


## SetStartLocationRequest (Low 324, NotTrusted, Zerocoded)

```csharp

public sealed class SetStartLocationRequestPacket : Packet {

}
```


## SetStartLocation (Low 325, Trusted, Zerocoded)

```csharp

public sealed class SetStartLocationPacket : Packet {

}
```


## NetTest (Low 326, NotTrusted, Unencoded)

```csharp

public sealed class NetTestPacket : Packet {

}
```


## SetCPURatio (Low 327, NotTrusted, Unencoded)

```csharp

public sealed class SetCPURatioPacket : Packet {

}
```


## SimCrashed (Low 328, NotTrusted, Unencoded)

```csharp

public sealed class SimCrashedPacket : Packet {

}
```


## NameValuePair (Low 329, Trusted, Unencoded)

```csharp

public sealed class NameValuePairPacket : Packet {

}
```


## RemoveNameValuePair (Low 330, Trusted, Unencoded)

```csharp

public sealed class RemoveNameValuePairPacket : Packet {

}
```


## UpdateAttachment (Low 331, Trusted, Zerocoded)

```csharp

public sealed class UpdateAttachmentPacket : Packet {

}
```


## RemoveAttachment (Low 332, NotTrusted, Unencoded)

```csharp

public sealed class RemoveAttachmentPacket : Packet {

}
```


## SoundTrigger (High 29, NotTrusted, Unencoded)

```csharp

public sealed class SoundTriggerPacket : Packet {

}
```


## AttachedSound (Medium 13, Trusted, Unencoded)

```csharp

public sealed class AttachedSoundPacket : Packet {

}
```


## AttachedSoundGainChange (Medium 14, Trusted, Unencoded)

```csharp

public sealed class AttachedSoundGainChangePacket : Packet {

}
```


## PreloadSound (Medium 15, Trusted, Unencoded)

```csharp

public sealed class PreloadSoundPacket : Packet {

}
```


## ObjectAnimation (High 30, Trusted, Unencoded)

```csharp

public sealed class ObjectAnimationPacket : Packet {

}
```


## AssetUploadRequest (Low 333, NotTrusted, Unencoded)

```csharp

public sealed class AssetUploadRequestPacket : Packet {

}
```


## AssetUploadComplete (Low 334, NotTrusted, Unencoded)

```csharp

public sealed class AssetUploadCompletePacket : Packet {

}
```


## EmailMessageRequest (Low 335, Trusted, Unencoded)

```csharp

public sealed class EmailMessageRequestPacket : Packet {

}
```


## EmailMessageReply (Low 336, Trusted, Unencoded)

```csharp

public sealed class EmailMessageReplyPacket : Packet {

}
```


## InternalScriptMail (Medium 16, Trusted, Unencoded)

```csharp

public sealed class InternalScriptMailPacket : Packet {

}
```


## ScriptDataRequest (Low 337, Trusted, Unencoded)

```csharp

public sealed class ScriptDataRequestPacket : Packet {

}
```


## ScriptDataReply (Low 338, Trusted, Unencoded)

```csharp

public sealed class ScriptDataReplyPacket : Packet {

}
```


## CreateGroupRequest (Low 339, NotTrusted, Zerocoded)

```csharp

public sealed class CreateGroupRequestPacket : Packet {

}
```


## CreateGroupReply (Low 340, Trusted, Unencoded)

```csharp

public sealed class CreateGroupReplyPacket : Packet {

}
```


## UpdateGroupInfo (Low 341, NotTrusted, Zerocoded)

```csharp

public sealed class UpdateGroupInfoPacket : Packet {

}
```


## GroupRoleChanges (Low 342, NotTrusted, Unencoded)

```csharp

public sealed class GroupRoleChangesPacket : Packet {

}
```


## JoinGroupRequest (Low 343, NotTrusted, Zerocoded)

```csharp

public sealed class JoinGroupRequestPacket : Packet {

}
```


## JoinGroupReply (Low 344, Trusted, Unencoded)

```csharp

public sealed class JoinGroupReplyPacket : Packet {

}
```


## EjectGroupMemberRequest (Low 345, NotTrusted, Unencoded)

```csharp

public sealed class EjectGroupMemberRequestPacket : Packet {

}
```


## EjectGroupMemberReply (Low 346, Trusted, Unencoded)

```csharp

public sealed class EjectGroupMemberReplyPacket : Packet {

}
```


## LeaveGroupRequest (Low 347, NotTrusted, Unencoded)

```csharp

public sealed class LeaveGroupRequestPacket : Packet {

}
```


## LeaveGroupReply (Low 348, Trusted, Unencoded)

```csharp

public sealed class LeaveGroupReplyPacket : Packet {

}
```


## InviteGroupRequest (Low 349, NotTrusted, Unencoded)

```csharp

public sealed class InviteGroupRequestPacket : Packet {

}
```


## InviteGroupResponse (Low 350, Trusted, Unencoded)

```csharp

public sealed class InviteGroupResponsePacket : Packet {

}
```


## GroupProfileRequest (Low 351, NotTrusted, Unencoded)

```csharp

public sealed class GroupProfileRequestPacket : Packet {

}
```


## GroupProfileReply (Low 352, Trusted, Zerocoded)

```csharp

public sealed class GroupProfileReplyPacket : Packet {

}
```


## GroupAccountSummaryRequest (Low 353, NotTrusted, Zerocoded)

```csharp

public sealed class GroupAccountSummaryRequestPacket : Packet {

}
```


## GroupAccountSummaryReply (Low 354, Trusted, Zerocoded)

```csharp

public sealed class GroupAccountSummaryReplyPacket : Packet {

}
```


## GroupAccountDetailsRequest (Low 355, NotTrusted, Zerocoded)

```csharp

public sealed class GroupAccountDetailsRequestPacket : Packet {

}
```


## GroupAccountDetailsReply (Low 356, Trusted, Zerocoded)

```csharp

public sealed class GroupAccountDetailsReplyPacket : Packet {

}
```


## GroupAccountTransactionsRequest (Low 357, NotTrusted, Zerocoded)

```csharp

public sealed class GroupAccountTransactionsRequestPacket : Packet {

}
```


## GroupAccountTransactionsReply (Low 358, Trusted, Zerocoded)

```csharp

public sealed class GroupAccountTransactionsReplyPacket : Packet {

}
```


## GroupActiveProposalsRequest (Low 359, NotTrusted, Unencoded)

```csharp

public sealed class GroupActiveProposalsRequestPacket : Packet {

}
```


## GroupActiveProposalItemReply (Low 360, Trusted, Zerocoded)

```csharp

public sealed class GroupActiveProposalItemReplyPacket : Packet {

}
```


## GroupVoteHistoryRequest (Low 361, NotTrusted, Unencoded)

```csharp

public sealed class GroupVoteHistoryRequestPacket : Packet {

}
```


## GroupVoteHistoryItemReply (Low 362, Trusted, Zerocoded)

```csharp

public sealed class GroupVoteHistoryItemReplyPacket : Packet {

}
```


## StartGroupProposal (Low 363, NotTrusted, Zerocoded)

```csharp

public sealed class StartGroupProposalPacket : Packet {

}
```


## GroupProposalBallot (Low 364, NotTrusted, Unencoded)

```csharp

public sealed class GroupProposalBallotPacket : Packet {

}
```


## TallyVotes (Low 365, Trusted, Unencoded)

```csharp

public sealed class TallyVotesPacket : Packet {

}
```


## GroupMembersRequest (Low 366, NotTrusted, Unencoded)

```csharp

public sealed class GroupMembersRequestPacket : Packet {

}
```


## GroupMembersReply (Low 367, Trusted, Zerocoded)

```csharp

public sealed class GroupMembersReplyPacket : Packet {

}
```


## ActivateGroup (Low 368, NotTrusted, Zerocoded)

```csharp

public sealed class ActivateGroupPacket : Packet {

}
```


## SetGroupContribution (Low 369, NotTrusted, Unencoded)

```csharp

public sealed class SetGroupContributionPacket : Packet {

}
```


## SetGroupAcceptNotices (Low 370, NotTrusted, Unencoded)

```csharp

public sealed class SetGroupAcceptNoticesPacket : Packet {

}
```


## GroupRoleDataRequest (Low 371, NotTrusted, Unencoded)

```csharp

public sealed class GroupRoleDataRequestPacket : Packet {

}
```


## GroupRoleDataReply (Low 372, Trusted, Unencoded)

```csharp

public sealed class GroupRoleDataReplyPacket : Packet {

}
```


## GroupRoleMembersRequest (Low 373, NotTrusted, Unencoded)

```csharp

public sealed class GroupRoleMembersRequestPacket : Packet {

}
```


## GroupRoleMembersReply (Low 374, Trusted, Unencoded)

```csharp

public sealed class GroupRoleMembersReplyPacket : Packet {

}
```


## GroupTitlesRequest (Low 375, NotTrusted, Unencoded)

```csharp

public sealed class GroupTitlesRequestPacket : Packet {

}
```


## GroupTitlesReply (Low 376, Trusted, Zerocoded)

```csharp

public sealed class GroupTitlesReplyPacket : Packet {

}
```


## GroupTitleUpdate (Low 377, NotTrusted, Unencoded)

```csharp

public sealed class GroupTitleUpdatePacket : Packet {

}
```


## GroupRoleUpdate (Low 378, NotTrusted, Unencoded)

```csharp

public sealed class GroupRoleUpdatePacket : Packet {

}
```


## LiveHelpGroupRequest (Low 379, Trusted, Unencoded)

```csharp

public sealed class LiveHelpGroupRequestPacket : Packet {

}
```


## LiveHelpGroupReply (Low 380, Trusted, Unencoded)

```csharp

public sealed class LiveHelpGroupReplyPacket : Packet {

}
```


## AgentWearablesRequest (Low 381, NotTrusted, Unencoded)

```csharp

public sealed class AgentWearablesRequestPacket : Packet {

}
```


## AgentWearablesUpdate (Low 382, Trusted, Zerocoded)

```csharp

public sealed class AgentWearablesUpdatePacket : Packet {

}
```


## AgentIsNowWearing (Low 383, NotTrusted, Zerocoded)

```csharp

public sealed class AgentIsNowWearingPacket : Packet {

}
```


## AgentCachedTexture (Low 384, NotTrusted, Unencoded)

```csharp

public sealed class AgentCachedTexturePacket : Packet {

}
```


## AgentCachedTextureResponse (Low 385, Trusted, Unencoded)

```csharp

public sealed class AgentCachedTextureResponsePacket : Packet {

}
```


## AgentDataUpdateRequest (Low 386, NotTrusted, Unencoded)

```csharp

public sealed class AgentDataUpdateRequestPacket : Packet {

}
```


## AgentDataUpdate (Low 387, Trusted, Zerocoded)

```csharp

public sealed class AgentDataUpdatePacket : Packet {

}
```


## GroupDataUpdate (Low 388, Trusted, Zerocoded)

```csharp

public sealed class GroupDataUpdatePacket : Packet {

}
```


## AgentGroupDataUpdate (Low 389, Trusted, Zerocoded)

```csharp

public sealed class AgentGroupDataUpdatePacket : Packet {

}
```


## AgentDropGroup (Low 390, Trusted, Zerocoded)

```csharp

public sealed class AgentDropGroupPacket : Packet {

}
```


## LogTextMessage (Low 391, Trusted, Zerocoded)

```csharp

public sealed class LogTextMessagePacket : Packet {

}
```


## ViewerEffect (Medium 17, NotTrusted, Zerocoded)

```csharp

public sealed class ViewerEffectPacket : Packet {

}
```


## CreateTrustedCircuit (Low 392, NotTrusted, Unencoded)

```csharp

public sealed class CreateTrustedCircuitPacket : Packet {

}
```


## DenyTrustedCircuit (Low 393, NotTrusted, Unencoded)

```csharp

public sealed class DenyTrustedCircuitPacket : Packet {

}
```


## RequestTrustedCircuit (Low 394, Trusted, Unencoded)

```csharp

public sealed class RequestTrustedCircuitPacket : Packet {

}
```


## RezSingleAttachmentFromInv (Low 395, NotTrusted, Zerocoded)

```csharp

public sealed class RezSingleAttachmentFromInvPacket : Packet {

}
```


## RezMultipleAttachmentsFromInv (Low 396, NotTrusted, Zerocoded)

```csharp

public sealed class RezMultipleAttachmentsFromInvPacket : Packet {

}
```


## DetachAttachmentIntoInv (Low 397, NotTrusted, Unencoded)

```csharp

public sealed class DetachAttachmentIntoInvPacket : Packet {

}
```


## CreateNewOutfitAttachments (Low 398, NotTrusted, Unencoded)

```csharp

public sealed class CreateNewOutfitAttachmentsPacket : Packet {

}
```


## UserInfoRequest (Low 399, NotTrusted, Unencoded)

```csharp

public sealed class UserInfoRequestPacket : Packet {

}
```


## UserInfoReply (Low 400, NotTrusted, Unencoded)

```csharp

public sealed class UserInfoReplyPacket : Packet {

}
```


## UpdateUserInfo (Low 401, NotTrusted, Unencoded)

```csharp

public sealed class UpdateUserInfoPacket : Packet {

}
```


## ParcelRename (Low 402, Trusted, Unencoded)

```csharp

public sealed class ParcelRenamePacket : Packet {

}
```


## InitiateDownload (Low 403, NotTrusted, Unencoded)

```csharp

public sealed class InitiateDownloadPacket : Packet {

}
```


## SystemMessage (Low 404, Trusted, Zerocoded)

```csharp

public sealed class SystemMessagePacket : Packet {

}
```


## MapLayerRequest (Low 405, NotTrusted, Unencoded)

```csharp

public sealed class MapLayerRequestPacket : Packet {

}
```


## MapLayerReply (Low 406, Trusted, Unencoded)

```csharp

public sealed class MapLayerReplyPacket : Packet {

}
```


## MapBlockRequest (Low 407, NotTrusted, Unencoded)

```csharp

public sealed class MapBlockRequestPacket : Packet {

}
```


## MapNameRequest (Low 408, NotTrusted, Unencoded)

```csharp

public sealed class MapNameRequestPacket : Packet {

}
```


## MapBlockReply (Low 409, Trusted, Unencoded)

```csharp

public sealed class MapBlockReplyPacket : Packet {

}
```


## MapItemRequest (Low 410, NotTrusted, Unencoded)

```csharp

public sealed class MapItemRequestPacket : Packet {

}
```


## MapItemReply (Low 411, Trusted, Unencoded)

```csharp

public sealed class MapItemReplyPacket : Packet {

}
```


## SendPostcard (Low 412, NotTrusted, Unencoded)

```csharp

public sealed class SendPostcardPacket : Packet {

}
```


## RpcChannelRequest (Low 413, Trusted, Unencoded)

```csharp

public sealed class RpcChannelRequestPacket : Packet {

}
```


## RpcChannelReply (Low 414, Trusted, Unencoded)

```csharp

public sealed class RpcChannelReplyPacket : Packet {

}
```


## RpcScriptRequestInbound (Low 415, NotTrusted, Unencoded)

```csharp

public sealed class RpcScriptRequestInboundPacket : Packet {

}
```


## RpcScriptRequestInboundForward (Low 416, Trusted, Unencoded)

```csharp

public sealed class RpcScriptRequestInboundForwardPacket : Packet {

}
```


## RpcScriptReplyInbound (Low 417, NotTrusted, Unencoded)

```csharp

public sealed class RpcScriptReplyInboundPacket : Packet {

}
```


## ScriptMailRegistration (Low 418, Trusted, Unencoded)

```csharp

public sealed class ScriptMailRegistrationPacket : Packet {

}
```


## ParcelMediaCommandMessage (Low 419, Trusted, Unencoded)

```csharp

public sealed class ParcelMediaCommandMessagePacket : Packet {

}
```


## ParcelMediaUpdate (Low 420, Trusted, Unencoded)

```csharp

public sealed class ParcelMediaUpdatePacket : Packet {

}
```


## LandStatRequest (Low 421, NotTrusted, Unencoded)

```csharp

public sealed class LandStatRequestPacket : Packet {

}
```


## LandStatReply (Low 422, Trusted, Unencoded)

```csharp

public sealed class LandStatReplyPacket : Packet {

}
```


## Error (Low 423, NotTrusted, Zerocoded)

```csharp

public sealed class ErrorPacket : Packet {

}
```


## ObjectIncludeInSearch (Low 424, NotTrusted, Unencoded)

```csharp

public sealed class ObjectIncludeInSearchPacket : Packet {

}
```


## RezRestoreToWorld (Low 425, NotTrusted, Unencoded)

```csharp

public sealed class RezRestoreToWorldPacket : Packet {

}
```


## LinkInventoryItem (Low 426, NotTrusted, Zerocoded)

```csharp

public sealed class LinkInventoryItemPacket : Packet {

}
```


## RetrieveIMsExtended (Low 427, Trusted, Unencoded)

```csharp

public sealed class RetrieveIMsExtendedPacket : Packet {

}
```


## JoinGroupRequestExtended (Low 428, Trusted, Unencoded)

```csharp

public sealed class JoinGroupRequestExtendedPacket : Packet {

}
```


## CreateGroupRequestExtended (Low 429, Trusted, Unencoded)

```csharp

public sealed class CreateGroupRequestExtendedPacket : Packet {

}
```


## GameControlInput (High 32, NotTrusted, Zerocoded)

```csharp

public sealed class GameControlInputPacket : Packet {

}
```
