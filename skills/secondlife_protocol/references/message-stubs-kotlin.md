# Kotlin Message Stubs (generated from secondlife/master-message-template)

One stub per UDP message (483 messages) in Kotlin, generated from message_template.msg field definitions. These are starting points for a codec: implement ToBytes/FromBytes following the field order exactly, honour the zerocoded flag, and verify against LibreMetaverse.Protocol and the viewer template copy before shipping.


## TestMessage (Low 1, NotTrusted, Zerocoded)

```kotlin

data class TestMessageMessage(

}
```


## PacketAck (Fixed 0xFFFFFFFB, NotTrusted, Unencoded)

```kotlin

data class PacketAckMessage(

}
```


## OpenCircuit (Fixed 0xFFFFFFFC, NotTrusted, Unencoded)

```kotlin

data class OpenCircuitMessage(

}
```


## CloseCircuit (Fixed 0xFFFFFFFD, NotTrusted, Unencoded)

```kotlin

data class CloseCircuitMessage(

}
```


## StartPingCheck (High 1, NotTrusted, Unencoded)

```kotlin

data class StartPingCheckMessage(

}
```


## CompletePingCheck (High 2, NotTrusted, Unencoded)

```kotlin

data class CompletePingCheckMessage(

}
```


## AddCircuitCode (Low 2, Trusted, Unencoded)

```kotlin

data class AddCircuitCodeMessage(

}
```


## UseCircuitCode (Low 3, NotTrusted, Unencoded)

```kotlin

data class UseCircuitCodeMessage(

}
```


## NeighborList (High 3, Trusted, Unencoded)

```kotlin

data class NeighborListMessage(

}
```


## AvatarTextureUpdate (Low 4, Trusted, Zerocoded)

```kotlin

data class AvatarTextureUpdateMessage(

}
```


## SimulatorMapUpdate (Low 5, Trusted, Unencoded)

```kotlin

data class SimulatorMapUpdateMessage(

}
```


## SimulatorSetMap (Low 6, Trusted, Unencoded)

```kotlin

data class SimulatorSetMapMessage(

}
```


## SubscribeLoad (Low 7, Trusted, Unencoded)

```kotlin

data class SubscribeLoadMessage(

}
```


## UnsubscribeLoad (Low 8, Trusted, Unencoded)

```kotlin

data class UnsubscribeLoadMessage(

}
```


## SimulatorReady (Low 9, Trusted, Zerocoded)

```kotlin

data class SimulatorReadyMessage(

}
```


## TelehubInfo (Low 10, Trusted, Unencoded)

```kotlin

data class TelehubInfoMessage(

}
```


## SimulatorPresentAtLocation (Low 11, Trusted, Unencoded)

```kotlin

data class SimulatorPresentAtLocationMessage(

}
```


## SimulatorLoad (Low 12, Trusted, Unencoded)

```kotlin

data class SimulatorLoadMessage(

}
```


## SimulatorShutdownRequest (Low 13, Trusted, Unencoded)

```kotlin

data class SimulatorShutdownRequestMessage(

}
```


## RegionPresenceRequestByRegionID (Low 14, Trusted, Unencoded)

```kotlin

data class RegionPresenceRequestByRegionIDMessage(

}
```


## RegionPresenceRequestByHandle (Low 15, Trusted, Unencoded)

```kotlin

data class RegionPresenceRequestByHandleMessage(

}
```


## RegionPresenceResponse (Low 16, Trusted, Zerocoded)

```kotlin

data class RegionPresenceResponseMessage(

}
```


## UpdateSimulator (Low 17, Trusted, Unencoded)

```kotlin

data class UpdateSimulatorMessage(

}
```


## LogDwellTime (Low 18, Trusted, Unencoded)

```kotlin

data class LogDwellTimeMessage(

}
```


## FeatureDisabled (Low 19, Trusted, Unencoded)

```kotlin

data class FeatureDisabledMessage(

}
```


## LogFailedMoneyTransaction (Low 20, Trusted, Unencoded)

```kotlin

data class LogFailedMoneyTransactionMessage(

}
```


## UserReportInternal (Low 21, Trusted, Zerocoded)

```kotlin

data class UserReportInternalMessage(

}
```


## SetSimStatusInDatabase (Low 22, Trusted, Unencoded)

```kotlin

data class SetSimStatusInDatabaseMessage(

}
```


## SetSimPresenceInDatabase (Low 23, Trusted, Unencoded)

```kotlin

data class SetSimPresenceInDatabaseMessage(

}
```


## EconomyDataRequest (Low 24, NotTrusted, Unencoded)

```kotlin

data class EconomyDataRequestMessage(

}
```


## EconomyData (Low 25, Trusted, Zerocoded)

```kotlin

data class EconomyDataMessage(

}
```


## AvatarPickerRequest (Low 26, NotTrusted, Unencoded)

```kotlin

data class AvatarPickerRequestMessage(

}
```


## AvatarPickerRequestBackend (Low 27, Trusted, Unencoded)

```kotlin

data class AvatarPickerRequestBackendMessage(

}
```


## AvatarPickerReply (Low 28, Trusted, Unencoded)

```kotlin

data class AvatarPickerReplyMessage(

}
```


## PlacesQuery (Low 29, NotTrusted, Zerocoded)

```kotlin

data class PlacesQueryMessage(

}
```


## PlacesReply (Low 30, Trusted, Zerocoded)

```kotlin

data class PlacesReplyMessage(

}
```


## DirFindQuery (Low 31, NotTrusted, Zerocoded)

```kotlin

data class DirFindQueryMessage(

}
```


## DirFindQueryBackend (Low 32, Trusted, Zerocoded)

```kotlin

data class DirFindQueryBackendMessage(

}
```


## DirPlacesQuery (Low 33, NotTrusted, Zerocoded)

```kotlin

data class DirPlacesQueryMessage(

}
```


## DirPlacesQueryBackend (Low 34, Trusted, Zerocoded)

```kotlin

data class DirPlacesQueryBackendMessage(

}
```


## DirPlacesReply (Low 35, Trusted, Zerocoded)

```kotlin

data class DirPlacesReplyMessage(

}
```


## DirPeopleReply (Low 36, Trusted, Zerocoded)

```kotlin

data class DirPeopleReplyMessage(

}
```


## DirEventsReply (Low 37, Trusted, Zerocoded)

```kotlin

data class DirEventsReplyMessage(

}
```


## DirGroupsReply (Low 38, Trusted, Zerocoded)

```kotlin

data class DirGroupsReplyMessage(

}
```


## DirClassifiedQuery (Low 39, NotTrusted, Zerocoded)

```kotlin

data class DirClassifiedQueryMessage(

}
```


## DirClassifiedQueryBackend (Low 40, Trusted, Zerocoded)

```kotlin

data class DirClassifiedQueryBackendMessage(

}
```


## DirClassifiedReply (Low 41, Trusted, Zerocoded)

```kotlin

data class DirClassifiedReplyMessage(

}
```


## AvatarClassifiedReply (Low 42, Trusted, Unencoded)

```kotlin

data class AvatarClassifiedReplyMessage(

}
```


## ClassifiedInfoRequest (Low 43, NotTrusted, Zerocoded)

```kotlin

data class ClassifiedInfoRequestMessage(

}
```


## ClassifiedInfoReply (Low 44, Trusted, Unencoded)

```kotlin

data class ClassifiedInfoReplyMessage(

}
```


## ClassifiedInfoUpdate (Low 45, NotTrusted, Unencoded)

```kotlin

data class ClassifiedInfoUpdateMessage(

}
```


## ClassifiedDelete (Low 46, NotTrusted, Unencoded)

```kotlin

data class ClassifiedDeleteMessage(

}
```


## ClassifiedGodDelete (Low 47, NotTrusted, Unencoded)

```kotlin

data class ClassifiedGodDeleteMessage(

}
```


## DirLandQuery (Low 48, NotTrusted, Zerocoded)

```kotlin

data class DirLandQueryMessage(

}
```


## DirLandQueryBackend (Low 49, Trusted, Zerocoded)

```kotlin

data class DirLandQueryBackendMessage(

}
```


## DirLandReply (Low 50, Trusted, Zerocoded)

```kotlin

data class DirLandReplyMessage(

}
```


## DirPopularQuery (Low 51, NotTrusted, Zerocoded)

```kotlin

data class DirPopularQueryMessage(

}
```


## DirPopularQueryBackend (Low 52, Trusted, Zerocoded)

```kotlin

data class DirPopularQueryBackendMessage(

}
```


## DirPopularReply (Low 53, Trusted, Zerocoded)

```kotlin

data class DirPopularReplyMessage(

}
```


## ParcelInfoRequest (Low 54, NotTrusted, Unencoded)

```kotlin

data class ParcelInfoRequestMessage(

}
```


## ParcelInfoReply (Low 55, Trusted, Zerocoded)

```kotlin

data class ParcelInfoReplyMessage(

}
```


## ParcelObjectOwnersRequest (Low 56, NotTrusted, Unencoded)

```kotlin

data class ParcelObjectOwnersRequestMessage(

}
```


## ParcelObjectOwnersReply (Low 57, Trusted, Zerocoded)

```kotlin

data class ParcelObjectOwnersReplyMessage(

}
```


## GroupNoticesListRequest (Low 58, NotTrusted, Unencoded)

```kotlin

data class GroupNoticesListRequestMessage(

}
```


## GroupNoticesListReply (Low 59, Trusted, Unencoded)

```kotlin

data class GroupNoticesListReplyMessage(

}
```


## GroupNoticeRequest (Low 60, NotTrusted, Unencoded)

```kotlin

data class GroupNoticeRequestMessage(

}
```


## GroupNoticeAdd (Low 61, Trusted, Unencoded)

```kotlin

data class GroupNoticeAddMessage(

}
```


## TeleportRequest (Low 62, NotTrusted, Unencoded)

```kotlin

data class TeleportRequestMessage(

}
```


## TeleportLocationRequest (Low 63, NotTrusted, Unencoded)

```kotlin

data class TeleportLocationRequestMessage(

}
```


## TeleportLocal (Low 64, Trusted, Unencoded)

```kotlin

data class TeleportLocalMessage(

}
```


## TeleportLandmarkRequest (Low 65, NotTrusted, Zerocoded)

```kotlin

data class TeleportLandmarkRequestMessage(

}
```


## TeleportProgress (Low 66, Trusted, Unencoded)

```kotlin

data class TeleportProgressMessage(

}
```


## DataHomeLocationRequest (Low 67, Trusted, Zerocoded)

```kotlin

data class DataHomeLocationRequestMessage(

}
```


## DataHomeLocationReply (Low 68, Trusted, Unencoded)

```kotlin

data class DataHomeLocationReplyMessage(

}
```


## TeleportFinish (Low 69, Trusted, Unencoded)

```kotlin

data class TeleportFinishMessage(

}
```


## StartLure (Low 70, NotTrusted, Unencoded)

```kotlin

data class StartLureMessage(

}
```


## TeleportLureRequest (Low 71, NotTrusted, Unencoded)

```kotlin

data class TeleportLureRequestMessage(

}
```


## TeleportCancel (Low 72, NotTrusted, Unencoded)

```kotlin

data class TeleportCancelMessage(

}
```


## TeleportStart (Low 73, Trusted, Unencoded)

```kotlin

data class TeleportStartMessage(

}
```


## TeleportFailed (Low 74, Trusted, Unencoded)

```kotlin

data class TeleportFailedMessage(

}
```


## Undo (Low 75, NotTrusted, Unencoded)

```kotlin

data class UndoMessage(

}
```


## Redo (Low 76, NotTrusted, Unencoded)

```kotlin

data class RedoMessage(

}
```


## UndoLand (Low 77, NotTrusted, Unencoded)

```kotlin

data class UndoLandMessage(

}
```


## AgentPause (Low 78, NotTrusted, Unencoded)

```kotlin

data class AgentPauseMessage(

}
```


## AgentResume (Low 79, NotTrusted, Unencoded)

```kotlin

data class AgentResumeMessage(

}
```


## AgentUpdate (High 4, NotTrusted, Zerocoded)

```kotlin

data class AgentUpdateMessage(

}
```


## ChatFromViewer (Low 80, NotTrusted, Zerocoded)

```kotlin

data class ChatFromViewerMessage(

}
```


## AgentThrottle (Low 81, NotTrusted, Zerocoded)

```kotlin

data class AgentThrottleMessage(

}
```


## AgentFOV (Low 82, NotTrusted, Unencoded)

```kotlin

data class AgentFOVMessage(

}
```


## AgentHeightWidth (Low 83, NotTrusted, Unencoded)

```kotlin

data class AgentHeightWidthMessage(

}
```


## AgentSetAppearance (Low 84, NotTrusted, Zerocoded)

```kotlin

data class AgentSetAppearanceMessage(

}
```


## AgentAnimation (High 5, NotTrusted, Unencoded)

```kotlin

data class AgentAnimationMessage(

}
```


## AgentRequestSit (High 6, NotTrusted, Zerocoded)

```kotlin

data class AgentRequestSitMessage(

}
```


## AgentSit (High 7, NotTrusted, Unencoded)

```kotlin

data class AgentSitMessage(

}
```


## AgentQuitCopy (Low 85, NotTrusted, Unencoded)

```kotlin

data class AgentQuitCopyMessage(

}
```


## RequestImage (High 8, NotTrusted, Unencoded)

```kotlin

data class RequestImageMessage(

}
```


## ImageNotInDatabase (Low 86, Trusted, Unencoded)

```kotlin

data class ImageNotInDatabaseMessage(

}
```


## RebakeAvatarTextures (Low 87, Trusted, Unencoded)

```kotlin

data class RebakeAvatarTexturesMessage(

}
```


## SetAlwaysRun (Low 88, NotTrusted, Unencoded)

```kotlin

data class SetAlwaysRunMessage(

}
```


## ObjectAdd (Medium 1, NotTrusted, Zerocoded)

```kotlin

data class ObjectAddMessage(

}
```


## ObjectDelete (Low 89, NotTrusted, Zerocoded)

```kotlin

data class ObjectDeleteMessage(

}
```


## ObjectDuplicate (Low 90, NotTrusted, Zerocoded)

```kotlin

data class ObjectDuplicateMessage(

}
```


## ObjectDuplicateOnRay (Low 91, NotTrusted, Zerocoded)

```kotlin

data class ObjectDuplicateOnRayMessage(

}
```


## MultipleObjectUpdate (Medium 2, NotTrusted, Zerocoded)

```kotlin

data class MultipleObjectUpdateMessage(

}
```


## RequestMultipleObjects (Medium 3, NotTrusted, Zerocoded)

```kotlin

data class RequestMultipleObjectsMessage(

}
```


## ObjectPosition (Medium 4, NotTrusted, Zerocoded)

```kotlin

data class ObjectPositionMessage(

}
```


## ObjectScale (Low 92, NotTrusted, Zerocoded)

```kotlin

data class ObjectScaleMessage(

}
```


## ObjectRotation (Low 93, NotTrusted, Zerocoded)

```kotlin

data class ObjectRotationMessage(

}
```


## ObjectFlagUpdate (Low 94, NotTrusted, Zerocoded)

```kotlin

data class ObjectFlagUpdateMessage(

}
```


## ObjectClickAction (Low 95, NotTrusted, Zerocoded)

```kotlin

data class ObjectClickActionMessage(

}
```


## ObjectImage (Low 96, NotTrusted, Zerocoded)

```kotlin

data class ObjectImageMessage(

}
```


## ObjectBypassModUpdate (Low 431, NotTrusted, Zerocoded)

```kotlin

data class ObjectBypassModUpdateMessage(

}
```


## ObjectMaterial (Low 97, NotTrusted, Zerocoded)

```kotlin

data class ObjectMaterialMessage(

}
```


## ObjectShape (Low 98, NotTrusted, Zerocoded)

```kotlin

data class ObjectShapeMessage(

}
```


## ObjectExtraParams (Low 99, NotTrusted, Zerocoded)

```kotlin

data class ObjectExtraParamsMessage(

}
```


## ObjectOwner (Low 100, NotTrusted, Zerocoded)

```kotlin

data class ObjectOwnerMessage(

}
```


## ObjectGroup (Low 101, NotTrusted, Zerocoded)

```kotlin

data class ObjectGroupMessage(

}
```


## ObjectBuy (Low 102, NotTrusted, Zerocoded)

```kotlin

data class ObjectBuyMessage(

}
```


## BuyObjectInventory (Low 103, NotTrusted, Zerocoded)

```kotlin

data class BuyObjectInventoryMessage(

}
```


## DerezContainer (Low 104, Trusted, Zerocoded)

```kotlin

data class DerezContainerMessage(

}
```


## ObjectPermissions (Low 105, NotTrusted, Zerocoded)

```kotlin

data class ObjectPermissionsMessage(

}
```


## ObjectSaleInfo (Low 106, NotTrusted, Zerocoded)

```kotlin

data class ObjectSaleInfoMessage(

}
```


## ObjectName (Low 107, NotTrusted, Zerocoded)

```kotlin

data class ObjectNameMessage(

}
```


## ObjectDescription (Low 108, NotTrusted, Zerocoded)

```kotlin

data class ObjectDescriptionMessage(

}
```


## ObjectCategory (Low 109, NotTrusted, Zerocoded)

```kotlin

data class ObjectCategoryMessage(

}
```


## ObjectSelect (Low 110, NotTrusted, Zerocoded)

```kotlin

data class ObjectSelectMessage(

}
```


## ObjectDeselect (Low 111, NotTrusted, Zerocoded)

```kotlin

data class ObjectDeselectMessage(

}
```


## ObjectAttach (Low 112, NotTrusted, Zerocoded)

```kotlin

data class ObjectAttachMessage(

}
```


## ObjectDetach (Low 113, NotTrusted, Unencoded)

```kotlin

data class ObjectDetachMessage(

}
```


## ObjectDrop (Low 114, NotTrusted, Unencoded)

```kotlin

data class ObjectDropMessage(

}
```


## ObjectLink (Low 115, NotTrusted, Unencoded)

```kotlin

data class ObjectLinkMessage(

}
```


## ObjectDelink (Low 116, NotTrusted, Unencoded)

```kotlin

data class ObjectDelinkMessage(

}
```


## ObjectGrab (Low 117, NotTrusted, Zerocoded)

```kotlin

data class ObjectGrabMessage(

}
```


## ObjectGrabUpdate (Low 118, NotTrusted, Zerocoded)

```kotlin

data class ObjectGrabUpdateMessage(

}
```


## ObjectDeGrab (Low 119, NotTrusted, Unencoded)

```kotlin

data class ObjectDeGrabMessage(

}
```


## ObjectSpinStart (Low 120, NotTrusted, Zerocoded)

```kotlin

data class ObjectSpinStartMessage(

}
```


## ObjectSpinUpdate (Low 121, NotTrusted, Zerocoded)

```kotlin

data class ObjectSpinUpdateMessage(

}
```


## ObjectSpinStop (Low 122, NotTrusted, Zerocoded)

```kotlin

data class ObjectSpinStopMessage(

}
```


## ObjectExportSelected (Low 123, NotTrusted, Zerocoded)

```kotlin

data class ObjectExportSelectedMessage(

}
```


## ModifyLand (Low 124, NotTrusted, Zerocoded)

```kotlin

data class ModifyLandMessage(

}
```


## VelocityInterpolateOn (Low 125, NotTrusted, Unencoded)

```kotlin

data class VelocityInterpolateOnMessage(

}
```


## VelocityInterpolateOff (Low 126, NotTrusted, Unencoded)

```kotlin

data class VelocityInterpolateOffMessage(

}
```


## StateSave (Low 127, NotTrusted, Unencoded)

```kotlin

data class StateSaveMessage(

}
```


## ReportAutosaveCrash (Low 128, NotTrusted, Unencoded)

```kotlin

data class ReportAutosaveCrashMessage(

}
```


## SimWideDeletes (Low 129, NotTrusted, Unencoded)

```kotlin

data class SimWideDeletesMessage(

}
```


## RequestObjectPropertiesFamily (Medium 5, NotTrusted, Zerocoded)

```kotlin

data class RequestObjectPropertiesFamilyMessage(

}
```


## TrackAgent (Low 130, NotTrusted, Unencoded)

```kotlin

data class TrackAgentMessage(

}
```


## ViewerStats (Low 131, NotTrusted, Zerocoded)

```kotlin

data class ViewerStatsMessage(

}
```


## ScriptAnswerYes (Low 132, NotTrusted, Unencoded)

```kotlin

data class ScriptAnswerYesMessage(

}
```


## UserReport (Low 133, NotTrusted, Zerocoded)

```kotlin

data class UserReportMessage(

}
```


## AlertMessage (Low 134, Trusted, Unencoded)

```kotlin

data class AlertMessageMessage(

}
```


## AgentAlertMessage (Low 135, Trusted, Unencoded)

```kotlin

data class AgentAlertMessageMessage(

}
```


## MeanCollisionAlert (Low 136, Trusted, Zerocoded)

```kotlin

data class MeanCollisionAlertMessage(

}
```


## ViewerFrozenMessage (Low 137, Trusted, Unencoded)

```kotlin

data class ViewerFrozenMessageMessage(

}
```


## HealthMessage (Low 138, Trusted, Zerocoded)

```kotlin

data class HealthMessageMessage(

}
```


## ChatFromSimulator (Low 139, Trusted, Unencoded)

```kotlin

data class ChatFromSimulatorMessage(

}
```


## SimStats (Low 140, Trusted, Unencoded)

```kotlin

data class SimStatsMessage(

}
```


## RequestRegionInfo (Low 141, NotTrusted, Unencoded)

```kotlin

data class RequestRegionInfoMessage(

}
```


## RegionInfo (Low 142, NotTrusted, Zerocoded)

```kotlin

data class RegionInfoMessage(

}
```


## GodUpdateRegionInfo (Low 143, NotTrusted, Zerocoded)

```kotlin

data class GodUpdateRegionInfoMessage(

}
```


## NearestLandingRegionRequest (Low 144, Trusted, Unencoded)

```kotlin

data class NearestLandingRegionRequestMessage(

}
```


## NearestLandingRegionReply (Low 145, Trusted, Unencoded)

```kotlin

data class NearestLandingRegionReplyMessage(

}
```


## NearestLandingRegionUpdated (Low 146, Trusted, Unencoded)

```kotlin

data class NearestLandingRegionUpdatedMessage(

}
```


## TeleportLandingStatusChanged (Low 147, Trusted, Unencoded)

```kotlin

data class TeleportLandingStatusChangedMessage(

}
```


## RegionHandshake (Low 148, Trusted, Zerocoded)

```kotlin

data class RegionHandshakeMessage(

}
```


## RegionHandshakeReply (Low 149, NotTrusted, Zerocoded)

```kotlin

data class RegionHandshakeReplyMessage(

}
```


## CoarseLocationUpdate (Medium 6, Trusted, Unencoded)

```kotlin

data class CoarseLocationUpdateMessage(

}
```


## ImageData (High 9, Trusted, Unencoded)

```kotlin

data class ImageDataMessage(

}
```


## ImagePacket (High 10, Trusted, Unencoded)

```kotlin

data class ImagePacketMessage(

}
```


## LayerData (High 11, Trusted, Unencoded)

```kotlin

data class LayerDataMessage(

}
```


## ObjectUpdate (High 12, Trusted, Zerocoded)

```kotlin

data class ObjectUpdateMessage(

}
```


## ObjectUpdateCompressed (High 13, Trusted, Unencoded)

```kotlin

data class ObjectUpdateCompressedMessage(

}
```


## ObjectUpdateCached (High 14, Trusted, Unencoded)

```kotlin

data class ObjectUpdateCachedMessage(

}
```


## ImprovedTerseObjectUpdate (High 15, Trusted, Unencoded)

```kotlin

data class ImprovedTerseObjectUpdateMessage(

}
```


## KillObject (High 16, Trusted, Unencoded)

```kotlin

data class KillObjectMessage(

}
```


## CrossedRegion (Medium 7, Trusted, Unencoded)

```kotlin

data class CrossedRegionMessage(

}
```


## SimulatorViewerTimeMessage (Low 150, Trusted, Unencoded)

```kotlin

data class SimulatorViewerTimeMessageMessage(

}
```


## EnableSimulator (Low 151, Trusted, Unencoded)

```kotlin

data class EnableSimulatorMessage(

}
```


## DisableSimulator (Low 152, Trusted, Unencoded)

```kotlin

data class DisableSimulatorMessage(

}
```


## ConfirmEnableSimulator (Medium 8, Trusted, Unencoded)

```kotlin

data class ConfirmEnableSimulatorMessage(

}
```


## TransferRequest (Low 153, NotTrusted, Zerocoded)

```kotlin

data class TransferRequestMessage(

}
```


## TransferInfo (Low 154, NotTrusted, Zerocoded)

```kotlin

data class TransferInfoMessage(

}
```


## TransferPacket (High 17, NotTrusted, Unencoded)

```kotlin

data class TransferPacketMessage(

}
```


## TransferAbort (Low 155, NotTrusted, Zerocoded)

```kotlin

data class TransferAbortMessage(

}
```


## RequestXfer (Low 156, NotTrusted, Zerocoded)

```kotlin

data class RequestXferMessage(

}
```


## SendXferPacket (High 18, NotTrusted, Unencoded)

```kotlin

data class SendXferPacketMessage(

}
```


## ConfirmXferPacket (High 19, NotTrusted, Unencoded)

```kotlin

data class ConfirmXferPacketMessage(

}
```


## AbortXfer (Low 157, NotTrusted, Unencoded)

```kotlin

data class AbortXferMessage(

}
```


## AvatarAnimation (High 20, Trusted, Unencoded)

```kotlin

data class AvatarAnimationMessage(

}
```


## AvatarAppearance (Low 158, Trusted, Zerocoded)

```kotlin

data class AvatarAppearanceMessage(

}
```


## AvatarSitResponse (High 21, Trusted, Zerocoded)

```kotlin

data class AvatarSitResponseMessage(

}
```


## SetFollowCamProperties (Low 159, Trusted, Unencoded)

```kotlin

data class SetFollowCamPropertiesMessage(

}
```


## ClearFollowCamProperties (Low 160, Trusted, Unencoded)

```kotlin

data class ClearFollowCamPropertiesMessage(

}
```


## CameraConstraint (High 22, Trusted, Zerocoded)

```kotlin

data class CameraConstraintMessage(

}
```


## ObjectProperties (Medium 9, Trusted, Zerocoded)

```kotlin

data class ObjectPropertiesMessage(

}
```


## ObjectPropertiesFamily (Medium 10, Trusted, Zerocoded)

```kotlin

data class ObjectPropertiesFamilyMessage(

}
```


## RequestPayPrice (Low 161, NotTrusted, Unencoded)

```kotlin

data class RequestPayPriceMessage(

}
```


## PayPriceReply (Low 162, Trusted, Unencoded)

```kotlin

data class PayPriceReplyMessage(

}
```


## KickUser (Low 163, Trusted, Unencoded)

```kotlin

data class KickUserMessage(

}
```


## KickUserAck (Low 164, Trusted, Unencoded)

```kotlin

data class KickUserAckMessage(

}
```


## GodKickUser (Low 165, NotTrusted, Unencoded)

```kotlin

data class GodKickUserMessage(

}
```


## SystemKickUser (Low 166, Trusted, Unencoded)

```kotlin

data class SystemKickUserMessage(

}
```


## EjectUser (Low 167, NotTrusted, Unencoded)

```kotlin

data class EjectUserMessage(

}
```


## FreezeUser (Low 168, NotTrusted, Unencoded)

```kotlin

data class FreezeUserMessage(

}
```


## AvatarPropertiesRequest (Low 169, NotTrusted, Unencoded)

```kotlin

data class AvatarPropertiesRequestMessage(

}
```


## AvatarPropertiesRequestBackend (Low 170, Trusted, Unencoded)

```kotlin

data class AvatarPropertiesRequestBackendMessage(

}
```


## AvatarPropertiesReply (Low 171, Trusted, Zerocoded)

```kotlin

data class AvatarPropertiesReplyMessage(

}
```


## AvatarInterestsReply (Low 172, Trusted, Zerocoded)

```kotlin

data class AvatarInterestsReplyMessage(

}
```


## AvatarGroupsReply (Low 173, Trusted, Zerocoded)

```kotlin

data class AvatarGroupsReplyMessage(

}
```


## AvatarPropertiesUpdate (Low 174, NotTrusted, Zerocoded)

```kotlin

data class AvatarPropertiesUpdateMessage(

}
```


## AvatarInterestsUpdate (Low 175, NotTrusted, Zerocoded)

```kotlin

data class AvatarInterestsUpdateMessage(

}
```


## AvatarNotesReply (Low 176, Trusted, Unencoded)

```kotlin

data class AvatarNotesReplyMessage(

}
```


## AvatarNotesUpdate (Low 177, NotTrusted, Unencoded)

```kotlin

data class AvatarNotesUpdateMessage(

}
```


## AvatarPicksReply (Low 178, Trusted, Unencoded)

```kotlin

data class AvatarPicksReplyMessage(

}
```


## EventInfoRequest (Low 179, NotTrusted, Unencoded)

```kotlin

data class EventInfoRequestMessage(

}
```


## EventInfoReply (Low 180, Trusted, Unencoded)

```kotlin

data class EventInfoReplyMessage(

}
```


## EventNotificationAddRequest (Low 181, NotTrusted, Unencoded)

```kotlin

data class EventNotificationAddRequestMessage(

}
```


## EventNotificationRemoveRequest (Low 182, NotTrusted, Unencoded)

```kotlin

data class EventNotificationRemoveRequestMessage(

}
```


## EventGodDelete (Low 183, NotTrusted, Unencoded)

```kotlin

data class EventGodDeleteMessage(

}
```


## PickInfoReply (Low 184, Trusted, Unencoded)

```kotlin

data class PickInfoReplyMessage(

}
```


## PickInfoUpdate (Low 185, NotTrusted, Unencoded)

```kotlin

data class PickInfoUpdateMessage(

}
```


## PickDelete (Low 186, NotTrusted, Unencoded)

```kotlin

data class PickDeleteMessage(

}
```


## PickGodDelete (Low 187, NotTrusted, Unencoded)

```kotlin

data class PickGodDeleteMessage(

}
```


## ScriptQuestion (Low 188, Trusted, Unencoded)

```kotlin

data class ScriptQuestionMessage(

}
```


## ScriptControlChange (Low 189, Trusted, Unencoded)

```kotlin

data class ScriptControlChangeMessage(

}
```


## ScriptDialog (Low 190, Trusted, Zerocoded)

```kotlin

data class ScriptDialogMessage(

}
```


## ScriptDialogReply (Low 191, NotTrusted, Zerocoded)

```kotlin

data class ScriptDialogReplyMessage(

}
```


## ForceScriptControlRelease (Low 192, NotTrusted, Unencoded)

```kotlin

data class ForceScriptControlReleaseMessage(

}
```


## RevokePermissions (Low 193, NotTrusted, Unencoded)

```kotlin

data class RevokePermissionsMessage(

}
```


## LoadURL (Low 194, Trusted, Unencoded)

```kotlin

data class LoadURLMessage(

}
```


## ScriptTeleportRequest (Low 195, Trusted, Unencoded)

```kotlin

data class ScriptTeleportRequestMessage(

}
```


## ParcelOverlay (Low 196, Trusted, Zerocoded)

```kotlin

data class ParcelOverlayMessage(

}
```


## ParcelPropertiesRequest (Medium 11, NotTrusted, Zerocoded)

```kotlin

data class ParcelPropertiesRequestMessage(

}
```


## ParcelPropertiesRequestByID (Low 197, NotTrusted, Zerocoded)

```kotlin

data class ParcelPropertiesRequestByIDMessage(

}
```


## ParcelProperties (High 23, Trusted, Zerocoded)

```kotlin

data class ParcelPropertiesMessage(

}
```


## ParcelPropertiesUpdate (Low 198, NotTrusted, Zerocoded)

```kotlin

data class ParcelPropertiesUpdateMessage(

}
```


## ParcelReturnObjects (Low 199, NotTrusted, Zerocoded)

```kotlin

data class ParcelReturnObjectsMessage(

}
```


## ParcelSetOtherCleanTime (Low 200, NotTrusted, Zerocoded)

```kotlin

data class ParcelSetOtherCleanTimeMessage(

}
```


## ParcelDisableObjects (Low 201, NotTrusted, Zerocoded)

```kotlin

data class ParcelDisableObjectsMessage(

}
```


## ParcelSelectObjects (Low 202, NotTrusted, Zerocoded)

```kotlin

data class ParcelSelectObjectsMessage(

}
```


## EstateCovenantRequest (Low 203, NotTrusted, Unencoded)

```kotlin

data class EstateCovenantRequestMessage(

}
```


## EstateCovenantReply (Low 204, Trusted, Unencoded)

```kotlin

data class EstateCovenantReplyMessage(

}
```


## ForceObjectSelect (Low 205, Trusted, Unencoded)

```kotlin

data class ForceObjectSelectMessage(

}
```


## ParcelBuyPass (Low 206, NotTrusted, Unencoded)

```kotlin

data class ParcelBuyPassMessage(

}
```


## ParcelDeedToGroup (Low 207, NotTrusted, Unencoded)

```kotlin

data class ParcelDeedToGroupMessage(

}
```


## ParcelReclaim (Low 208, NotTrusted, Unencoded)

```kotlin

data class ParcelReclaimMessage(

}
```


## ParcelClaim (Low 209, NotTrusted, Zerocoded)

```kotlin

data class ParcelClaimMessage(

}
```


## ParcelJoin (Low 210, NotTrusted, Unencoded)

```kotlin

data class ParcelJoinMessage(

}
```


## ParcelDivide (Low 211, NotTrusted, Unencoded)

```kotlin

data class ParcelDivideMessage(

}
```


## ParcelRelease (Low 212, NotTrusted, Unencoded)

```kotlin

data class ParcelReleaseMessage(

}
```


## ParcelBuy (Low 213, NotTrusted, Zerocoded)

```kotlin

data class ParcelBuyMessage(

}
```


## ParcelGodForceOwner (Low 214, NotTrusted, Zerocoded)

```kotlin

data class ParcelGodForceOwnerMessage(

}
```


## ParcelAccessListRequest (Low 215, NotTrusted, Zerocoded)

```kotlin

data class ParcelAccessListRequestMessage(

}
```


## ParcelAccessListReply (Low 216, Trusted, Zerocoded)

```kotlin

data class ParcelAccessListReplyMessage(

}
```


## ParcelAccessListUpdate (Low 217, NotTrusted, Zerocoded)

```kotlin

data class ParcelAccessListUpdateMessage(

}
```


## ParcelDwellRequest (Low 218, NotTrusted, Unencoded)

```kotlin

data class ParcelDwellRequestMessage(

}
```


## ParcelDwellReply (Low 219, Trusted, Unencoded)

```kotlin

data class ParcelDwellReplyMessage(

}
```


## RequestParcelTransfer (Low 220, Trusted, Zerocoded)

```kotlin

data class RequestParcelTransferMessage(

}
```


## UpdateParcel (Low 221, Trusted, Zerocoded)

```kotlin

data class UpdateParcelMessage(

}
```


## RemoveParcel (Low 222, Trusted, Unencoded)

```kotlin

data class RemoveParcelMessage(

}
```


## MergeParcel (Low 223, Trusted, Unencoded)

```kotlin

data class MergeParcelMessage(

}
```


## LogParcelChanges (Low 224, Trusted, Zerocoded)

```kotlin

data class LogParcelChangesMessage(

}
```


## CheckParcelSales (Low 225, Trusted, Unencoded)

```kotlin

data class CheckParcelSalesMessage(

}
```


## ParcelSales (Low 226, Trusted, Unencoded)

```kotlin

data class ParcelSalesMessage(

}
```


## ParcelGodMarkAsContent (Low 227, NotTrusted, Unencoded)

```kotlin

data class ParcelGodMarkAsContentMessage(

}
```


## ViewerStartAuction (Low 228, NotTrusted, Unencoded)

```kotlin

data class ViewerStartAuctionMessage(

}
```


## StartAuction (Low 229, Trusted, Unencoded)

```kotlin

data class StartAuctionMessage(

}
```


## ConfirmAuctionStart (Low 230, Trusted, Unencoded)

```kotlin

data class ConfirmAuctionStartMessage(

}
```


## CompleteAuction (Low 231, Trusted, Unencoded)

```kotlin

data class CompleteAuctionMessage(

}
```


## CancelAuction (Low 232, Trusted, Unencoded)

```kotlin

data class CancelAuctionMessage(

}
```


## CheckParcelAuctions (Low 233, Trusted, Unencoded)

```kotlin

data class CheckParcelAuctionsMessage(

}
```


## ParcelAuctions (Low 234, Trusted, Unencoded)

```kotlin

data class ParcelAuctionsMessage(

}
```


## UUIDNameRequest (Low 235, NotTrusted, Unencoded)

```kotlin

data class UUIDNameRequestMessage(

}
```


## UUIDNameReply (Low 236, Trusted, Unencoded)

```kotlin

data class UUIDNameReplyMessage(

}
```


## UUIDGroupNameRequest (Low 237, NotTrusted, Unencoded)

```kotlin

data class UUIDGroupNameRequestMessage(

}
```


## UUIDGroupNameReply (Low 238, Trusted, Unencoded)

```kotlin

data class UUIDGroupNameReplyMessage(

}
```


## ChatPass (Low 239, Trusted, Zerocoded)

```kotlin

data class ChatPassMessage(

}
```


## EdgeDataPacket (High 24, Trusted, Zerocoded)

```kotlin

data class EdgeDataPacketMessage(

}
```


## SimStatus (Medium 12, Trusted, Unencoded)

```kotlin

data class SimStatusMessage(

}
```


## ChildAgentUpdate (High 25, Trusted, Zerocoded)

```kotlin

data class ChildAgentUpdateMessage(

}
```


## ChildAgentAlive (High 26, Trusted, Unencoded)

```kotlin

data class ChildAgentAliveMessage(

}
```


## ChildAgentPositionUpdate (High 27, Trusted, Unencoded)

```kotlin

data class ChildAgentPositionUpdateMessage(

}
```


## ChildAgentDying (Low 240, Trusted, Zerocoded)

```kotlin

data class ChildAgentDyingMessage(

}
```


## ChildAgentUnknown (Low 241, Trusted, Unencoded)

```kotlin

data class ChildAgentUnknownMessage(

}
```


## AtomicPassObject (High 28, Trusted, Unencoded)

```kotlin

data class AtomicPassObjectMessage(

}
```


## KillChildAgents (Low 242, Trusted, Unencoded)

```kotlin

data class KillChildAgentsMessage(

}
```


## GetScriptRunning (Low 243, NotTrusted, Unencoded)

```kotlin

data class GetScriptRunningMessage(

}
```


## ScriptRunningReply (Low 244, NotTrusted, Unencoded)

```kotlin

data class ScriptRunningReplyMessage(

}
```


## SetScriptRunning (Low 245, NotTrusted, Unencoded)

```kotlin

data class SetScriptRunningMessage(

}
```


## ScriptReset (Low 246, NotTrusted, Unencoded)

```kotlin

data class ScriptResetMessage(

}
```


## ScriptSensorRequest (Low 247, Trusted, Zerocoded)

```kotlin

data class ScriptSensorRequestMessage(

}
```


## ScriptSensorReply (Low 248, Trusted, Zerocoded)

```kotlin

data class ScriptSensorReplyMessage(

}
```


## CompleteAgentMovement (Low 249, NotTrusted, Unencoded)

```kotlin

data class CompleteAgentMovementMessage(

}
```


## AgentMovementComplete (Low 250, NotTrusted, Unencoded)

```kotlin

data class AgentMovementCompleteMessage(

}
```


## DataServerLogout (Low 251, Trusted, Unencoded)

```kotlin

data class DataServerLogoutMessage(

}
```


## LogoutRequest (Low 252, NotTrusted, Unencoded)

```kotlin

data class LogoutRequestMessage(

}
```


## LogoutReply (Low 253, Trusted, Zerocoded)

```kotlin

data class LogoutReplyMessage(

}
```


## ImprovedInstantMessage (Low 254, NotTrusted, Zerocoded)

```kotlin

data class ImprovedInstantMessageMessage(

}
```


## RetrieveInstantMessages (Low 255, NotTrusted, Unencoded)

```kotlin

data class RetrieveInstantMessagesMessage(

}
```


## FindAgent (Low 256, NotTrusted, Unencoded)

```kotlin

data class FindAgentMessage(

}
```


## RequestGodlikePowers (Low 257, NotTrusted, Unencoded)

```kotlin

data class RequestGodlikePowersMessage(

}
```


## GrantGodlikePowers (Low 258, Trusted, Unencoded)

```kotlin

data class GrantGodlikePowersMessage(

}
```


## GodlikeMessage (Low 259, NotTrusted, Zerocoded)

```kotlin

data class GodlikeMessageMessage(

}
```


## EstateOwnerMessage (Low 260, NotTrusted, Zerocoded)

```kotlin

data class EstateOwnerMessageMessage(

}
```


## GenericMessage (Low 261, NotTrusted, Zerocoded)

```kotlin

data class GenericMessageMessage(

}
```


## GenericStreamingMessage (High 31, Trusted, Unencoded)

```kotlin

data class GenericStreamingMessageMessage(

}
```


## LargeGenericMessage (Low 430, NotTrusted, Unencoded)

```kotlin

data class LargeGenericMessageMessage(

}
```


## MuteListRequest (Low 262, NotTrusted, Unencoded)

```kotlin

data class MuteListRequestMessage(

}
```


## UpdateMuteListEntry (Low 263, NotTrusted, Unencoded)

```kotlin

data class UpdateMuteListEntryMessage(

}
```


## RemoveMuteListEntry (Low 264, NotTrusted, Unencoded)

```kotlin

data class RemoveMuteListEntryMessage(

}
```


## CopyInventoryFromNotecard (Low 265, NotTrusted, Zerocoded)

```kotlin

data class CopyInventoryFromNotecardMessage(

}
```


## UpdateInventoryItem (Low 266, NotTrusted, Zerocoded)

```kotlin

data class UpdateInventoryItemMessage(

}
```


## UpdateCreateInventoryItem (Low 267, Trusted, Zerocoded)

```kotlin

data class UpdateCreateInventoryItemMessage(

}
```


## MoveInventoryItem (Low 268, NotTrusted, Zerocoded)

```kotlin

data class MoveInventoryItemMessage(

}
```


## CopyInventoryItem (Low 269, NotTrusted, Zerocoded)

```kotlin

data class CopyInventoryItemMessage(

}
```


## RemoveInventoryItem (Low 270, NotTrusted, Unencoded)

```kotlin

data class RemoveInventoryItemMessage(

}
```


## ChangeInventoryItemFlags (Low 271, NotTrusted, Unencoded)

```kotlin

data class ChangeInventoryItemFlagsMessage(

}
```


## SaveAssetIntoInventory (Low 272, Trusted, Unencoded)

```kotlin

data class SaveAssetIntoInventoryMessage(

}
```


## CreateInventoryFolder (Low 273, NotTrusted, Unencoded)

```kotlin

data class CreateInventoryFolderMessage(

}
```


## UpdateInventoryFolder (Low 274, NotTrusted, Unencoded)

```kotlin

data class UpdateInventoryFolderMessage(

}
```


## MoveInventoryFolder (Low 275, NotTrusted, Zerocoded)

```kotlin

data class MoveInventoryFolderMessage(

}
```


## RemoveInventoryFolder (Low 276, NotTrusted, Unencoded)

```kotlin

data class RemoveInventoryFolderMessage(

}
```


## FetchInventoryDescendents (Low 277, NotTrusted, Zerocoded)

```kotlin

data class FetchInventoryDescendentsMessage(

}
```


## InventoryDescendents (Low 278, Trusted, Zerocoded)

```kotlin

data class InventoryDescendentsMessage(

}
```


## FetchInventory (Low 279, NotTrusted, Zerocoded)

```kotlin

data class FetchInventoryMessage(

}
```


## FetchInventoryReply (Low 280, Trusted, Zerocoded)

```kotlin

data class FetchInventoryReplyMessage(

}
```


## BulkUpdateInventory (Low 281, Trusted, Zerocoded)

```kotlin

data class BulkUpdateInventoryMessage(

}
```


## RequestInventoryAsset (Low 282, Trusted, Unencoded)

```kotlin

data class RequestInventoryAssetMessage(

}
```


## InventoryAssetResponse (Low 283, Trusted, Unencoded)

```kotlin

data class InventoryAssetResponseMessage(

}
```


## RemoveInventoryObjects (Low 284, NotTrusted, Unencoded)

```kotlin

data class RemoveInventoryObjectsMessage(

}
```


## PurgeInventoryDescendents (Low 285, NotTrusted, Zerocoded)

```kotlin

data class PurgeInventoryDescendentsMessage(

}
```


## UpdateTaskInventory (Low 286, NotTrusted, Zerocoded)

```kotlin

data class UpdateTaskInventoryMessage(

}
```


## RemoveTaskInventory (Low 287, NotTrusted, Zerocoded)

```kotlin

data class RemoveTaskInventoryMessage(

}
```


## MoveTaskInventory (Low 288, NotTrusted, Unencoded)

```kotlin

data class MoveTaskInventoryMessage(

}
```


## RequestTaskInventory (Low 289, NotTrusted, Unencoded)

```kotlin

data class RequestTaskInventoryMessage(

}
```


## ReplyTaskInventory (Low 290, Trusted, Zerocoded)

```kotlin

data class ReplyTaskInventoryMessage(

}
```


## DeRezObject (Low 291, NotTrusted, Zerocoded)

```kotlin

data class DeRezObjectMessage(

}
```


## DeRezAck (Low 292, Trusted, Unencoded)

```kotlin

data class DeRezAckMessage(

}
```


## RezObject (Low 293, NotTrusted, Zerocoded)

```kotlin

data class RezObjectMessage(

}
```


## RezObjectFromNotecard (Low 294, NotTrusted, Zerocoded)

```kotlin

data class RezObjectFromNotecardMessage(

}
```


## TransferInventory (Low 295, Trusted, Zerocoded)

```kotlin

data class TransferInventoryMessage(

}
```


## TransferInventoryAck (Low 296, Trusted, Zerocoded)

```kotlin

data class TransferInventoryAckMessage(

}
```


## AcceptFriendship (Low 297, NotTrusted, Unencoded)

```kotlin

data class AcceptFriendshipMessage(

}
```


## DeclineFriendship (Low 298, NotTrusted, Unencoded)

```kotlin

data class DeclineFriendshipMessage(

}
```


## FormFriendship (Low 299, Trusted, Unencoded)

```kotlin

data class FormFriendshipMessage(

}
```


## TerminateFriendship (Low 300, NotTrusted, Unencoded)

```kotlin

data class TerminateFriendshipMessage(

}
```


## OfferCallingCard (Low 301, NotTrusted, Unencoded)

```kotlin

data class OfferCallingCardMessage(

}
```


## AcceptCallingCard (Low 302, NotTrusted, Unencoded)

```kotlin

data class AcceptCallingCardMessage(

}
```


## DeclineCallingCard (Low 303, NotTrusted, Unencoded)

```kotlin

data class DeclineCallingCardMessage(

}
```


## RezScript (Low 304, NotTrusted, Zerocoded)

```kotlin

data class RezScriptMessage(

}
```


## CreateInventoryItem (Low 305, NotTrusted, Zerocoded)

```kotlin

data class CreateInventoryItemMessage(

}
```


## CreateLandmarkForEvent (Low 306, NotTrusted, Zerocoded)

```kotlin

data class CreateLandmarkForEventMessage(

}
```


## EventLocationRequest (Low 307, Trusted, Zerocoded)

```kotlin

data class EventLocationRequestMessage(

}
```


## EventLocationReply (Low 308, Trusted, Zerocoded)

```kotlin

data class EventLocationReplyMessage(

}
```


## RegionHandleRequest (Low 309, NotTrusted, Unencoded)

```kotlin

data class RegionHandleRequestMessage(

}
```


## RegionIDAndHandleReply (Low 310, Trusted, Unencoded)

```kotlin

data class RegionIDAndHandleReplyMessage(

}
```


## MoneyTransferRequest (Low 311, NotTrusted, Zerocoded)

```kotlin

data class MoneyTransferRequestMessage(

}
```


## MoneyTransferBackend (Low 312, Trusted, Zerocoded)

```kotlin

data class MoneyTransferBackendMessage(

}
```


## MoneyBalanceRequest (Low 313, NotTrusted, Zerocoded)

```kotlin

data class MoneyBalanceRequestMessage(

}
```


## MoneyBalanceReply (Low 314, Trusted, Zerocoded)

```kotlin

data class MoneyBalanceReplyMessage(

}
```


## RoutedMoneyBalanceReply (Low 315, Trusted, Zerocoded)

```kotlin

data class RoutedMoneyBalanceReplyMessage(

}
```


## ActivateGestures (Low 316, NotTrusted, Unencoded)

```kotlin

data class ActivateGesturesMessage(

}
```


## DeactivateGestures (Low 317, NotTrusted, Unencoded)

```kotlin

data class DeactivateGesturesMessage(

}
```


## MuteListUpdate (Low 318, Trusted, Unencoded)

```kotlin

data class MuteListUpdateMessage(

}
```


## UseCachedMuteList (Low 319, NotTrusted, Unencoded)

```kotlin

data class UseCachedMuteListMessage(

}
```


## GrantUserRights (Low 320, NotTrusted, Unencoded)

```kotlin

data class GrantUserRightsMessage(

}
```


## ChangeUserRights (Low 321, Trusted, Unencoded)

```kotlin

data class ChangeUserRightsMessage(

}
```


## OnlineNotification (Low 322, Trusted, Unencoded)

```kotlin

data class OnlineNotificationMessage(

}
```


## OfflineNotification (Low 323, Trusted, Unencoded)

```kotlin

data class OfflineNotificationMessage(

}
```


## SetStartLocationRequest (Low 324, NotTrusted, Zerocoded)

```kotlin

data class SetStartLocationRequestMessage(

}
```


## SetStartLocation (Low 325, Trusted, Zerocoded)

```kotlin

data class SetStartLocationMessage(

}
```


## NetTest (Low 326, NotTrusted, Unencoded)

```kotlin

data class NetTestMessage(

}
```


## SetCPURatio (Low 327, NotTrusted, Unencoded)

```kotlin

data class SetCPURatioMessage(

}
```


## SimCrashed (Low 328, NotTrusted, Unencoded)

```kotlin

data class SimCrashedMessage(

}
```


## NameValuePair (Low 329, Trusted, Unencoded)

```kotlin

data class NameValuePairMessage(

}
```


## RemoveNameValuePair (Low 330, Trusted, Unencoded)

```kotlin

data class RemoveNameValuePairMessage(

}
```


## UpdateAttachment (Low 331, Trusted, Zerocoded)

```kotlin

data class UpdateAttachmentMessage(

}
```


## RemoveAttachment (Low 332, NotTrusted, Unencoded)

```kotlin

data class RemoveAttachmentMessage(

}
```


## SoundTrigger (High 29, NotTrusted, Unencoded)

```kotlin

data class SoundTriggerMessage(

}
```


## AttachedSound (Medium 13, Trusted, Unencoded)

```kotlin

data class AttachedSoundMessage(

}
```


## AttachedSoundGainChange (Medium 14, Trusted, Unencoded)

```kotlin

data class AttachedSoundGainChangeMessage(

}
```


## PreloadSound (Medium 15, Trusted, Unencoded)

```kotlin

data class PreloadSoundMessage(

}
```


## ObjectAnimation (High 30, Trusted, Unencoded)

```kotlin

data class ObjectAnimationMessage(

}
```


## AssetUploadRequest (Low 333, NotTrusted, Unencoded)

```kotlin

data class AssetUploadRequestMessage(

}
```


## AssetUploadComplete (Low 334, NotTrusted, Unencoded)

```kotlin

data class AssetUploadCompleteMessage(

}
```


## EmailMessageRequest (Low 335, Trusted, Unencoded)

```kotlin

data class EmailMessageRequestMessage(

}
```


## EmailMessageReply (Low 336, Trusted, Unencoded)

```kotlin

data class EmailMessageReplyMessage(

}
```


## InternalScriptMail (Medium 16, Trusted, Unencoded)

```kotlin

data class InternalScriptMailMessage(

}
```


## ScriptDataRequest (Low 337, Trusted, Unencoded)

```kotlin

data class ScriptDataRequestMessage(

}
```


## ScriptDataReply (Low 338, Trusted, Unencoded)

```kotlin

data class ScriptDataReplyMessage(

}
```


## CreateGroupRequest (Low 339, NotTrusted, Zerocoded)

```kotlin

data class CreateGroupRequestMessage(

}
```


## CreateGroupReply (Low 340, Trusted, Unencoded)

```kotlin

data class CreateGroupReplyMessage(

}
```


## UpdateGroupInfo (Low 341, NotTrusted, Zerocoded)

```kotlin

data class UpdateGroupInfoMessage(

}
```


## GroupRoleChanges (Low 342, NotTrusted, Unencoded)

```kotlin

data class GroupRoleChangesMessage(

}
```


## JoinGroupRequest (Low 343, NotTrusted, Zerocoded)

```kotlin

data class JoinGroupRequestMessage(

}
```


## JoinGroupReply (Low 344, Trusted, Unencoded)

```kotlin

data class JoinGroupReplyMessage(

}
```


## EjectGroupMemberRequest (Low 345, NotTrusted, Unencoded)

```kotlin

data class EjectGroupMemberRequestMessage(

}
```


## EjectGroupMemberReply (Low 346, Trusted, Unencoded)

```kotlin

data class EjectGroupMemberReplyMessage(

}
```


## LeaveGroupRequest (Low 347, NotTrusted, Unencoded)

```kotlin

data class LeaveGroupRequestMessage(

}
```


## LeaveGroupReply (Low 348, Trusted, Unencoded)

```kotlin

data class LeaveGroupReplyMessage(

}
```


## InviteGroupRequest (Low 349, NotTrusted, Unencoded)

```kotlin

data class InviteGroupRequestMessage(

}
```


## InviteGroupResponse (Low 350, Trusted, Unencoded)

```kotlin

data class InviteGroupResponseMessage(

}
```


## GroupProfileRequest (Low 351, NotTrusted, Unencoded)

```kotlin

data class GroupProfileRequestMessage(

}
```


## GroupProfileReply (Low 352, Trusted, Zerocoded)

```kotlin

data class GroupProfileReplyMessage(

}
```


## GroupAccountSummaryRequest (Low 353, NotTrusted, Zerocoded)

```kotlin

data class GroupAccountSummaryRequestMessage(

}
```


## GroupAccountSummaryReply (Low 354, Trusted, Zerocoded)

```kotlin

data class GroupAccountSummaryReplyMessage(

}
```


## GroupAccountDetailsRequest (Low 355, NotTrusted, Zerocoded)

```kotlin

data class GroupAccountDetailsRequestMessage(

}
```


## GroupAccountDetailsReply (Low 356, Trusted, Zerocoded)

```kotlin

data class GroupAccountDetailsReplyMessage(

}
```


## GroupAccountTransactionsRequest (Low 357, NotTrusted, Zerocoded)

```kotlin

data class GroupAccountTransactionsRequestMessage(

}
```


## GroupAccountTransactionsReply (Low 358, Trusted, Zerocoded)

```kotlin

data class GroupAccountTransactionsReplyMessage(

}
```


## GroupActiveProposalsRequest (Low 359, NotTrusted, Unencoded)

```kotlin

data class GroupActiveProposalsRequestMessage(

}
```


## GroupActiveProposalItemReply (Low 360, Trusted, Zerocoded)

```kotlin

data class GroupActiveProposalItemReplyMessage(

}
```


## GroupVoteHistoryRequest (Low 361, NotTrusted, Unencoded)

```kotlin

data class GroupVoteHistoryRequestMessage(

}
```


## GroupVoteHistoryItemReply (Low 362, Trusted, Zerocoded)

```kotlin

data class GroupVoteHistoryItemReplyMessage(

}
```


## StartGroupProposal (Low 363, NotTrusted, Zerocoded)

```kotlin

data class StartGroupProposalMessage(

}
```


## GroupProposalBallot (Low 364, NotTrusted, Unencoded)

```kotlin

data class GroupProposalBallotMessage(

}
```


## TallyVotes (Low 365, Trusted, Unencoded)

```kotlin

data class TallyVotesMessage(

}
```


## GroupMembersRequest (Low 366, NotTrusted, Unencoded)

```kotlin

data class GroupMembersRequestMessage(

}
```


## GroupMembersReply (Low 367, Trusted, Zerocoded)

```kotlin

data class GroupMembersReplyMessage(

}
```


## ActivateGroup (Low 368, NotTrusted, Zerocoded)

```kotlin

data class ActivateGroupMessage(

}
```


## SetGroupContribution (Low 369, NotTrusted, Unencoded)

```kotlin

data class SetGroupContributionMessage(

}
```


## SetGroupAcceptNotices (Low 370, NotTrusted, Unencoded)

```kotlin

data class SetGroupAcceptNoticesMessage(

}
```


## GroupRoleDataRequest (Low 371, NotTrusted, Unencoded)

```kotlin

data class GroupRoleDataRequestMessage(

}
```


## GroupRoleDataReply (Low 372, Trusted, Unencoded)

```kotlin

data class GroupRoleDataReplyMessage(

}
```


## GroupRoleMembersRequest (Low 373, NotTrusted, Unencoded)

```kotlin

data class GroupRoleMembersRequestMessage(

}
```


## GroupRoleMembersReply (Low 374, Trusted, Unencoded)

```kotlin

data class GroupRoleMembersReplyMessage(

}
```


## GroupTitlesRequest (Low 375, NotTrusted, Unencoded)

```kotlin

data class GroupTitlesRequestMessage(

}
```


## GroupTitlesReply (Low 376, Trusted, Zerocoded)

```kotlin

data class GroupTitlesReplyMessage(

}
```


## GroupTitleUpdate (Low 377, NotTrusted, Unencoded)

```kotlin

data class GroupTitleUpdateMessage(

}
```


## GroupRoleUpdate (Low 378, NotTrusted, Unencoded)

```kotlin

data class GroupRoleUpdateMessage(

}
```


## LiveHelpGroupRequest (Low 379, Trusted, Unencoded)

```kotlin

data class LiveHelpGroupRequestMessage(

}
```


## LiveHelpGroupReply (Low 380, Trusted, Unencoded)

```kotlin

data class LiveHelpGroupReplyMessage(

}
```


## AgentWearablesRequest (Low 381, NotTrusted, Unencoded)

```kotlin

data class AgentWearablesRequestMessage(

}
```


## AgentWearablesUpdate (Low 382, Trusted, Zerocoded)

```kotlin

data class AgentWearablesUpdateMessage(

}
```


## AgentIsNowWearing (Low 383, NotTrusted, Zerocoded)

```kotlin

data class AgentIsNowWearingMessage(

}
```


## AgentCachedTexture (Low 384, NotTrusted, Unencoded)

```kotlin

data class AgentCachedTextureMessage(

}
```


## AgentCachedTextureResponse (Low 385, Trusted, Unencoded)

```kotlin

data class AgentCachedTextureResponseMessage(

}
```


## AgentDataUpdateRequest (Low 386, NotTrusted, Unencoded)

```kotlin

data class AgentDataUpdateRequestMessage(

}
```


## AgentDataUpdate (Low 387, Trusted, Zerocoded)

```kotlin

data class AgentDataUpdateMessage(

}
```


## GroupDataUpdate (Low 388, Trusted, Zerocoded)

```kotlin

data class GroupDataUpdateMessage(

}
```


## AgentGroupDataUpdate (Low 389, Trusted, Zerocoded)

```kotlin

data class AgentGroupDataUpdateMessage(

}
```


## AgentDropGroup (Low 390, Trusted, Zerocoded)

```kotlin

data class AgentDropGroupMessage(

}
```


## LogTextMessage (Low 391, Trusted, Zerocoded)

```kotlin

data class LogTextMessageMessage(

}
```


## ViewerEffect (Medium 17, NotTrusted, Zerocoded)

```kotlin

data class ViewerEffectMessage(

}
```


## CreateTrustedCircuit (Low 392, NotTrusted, Unencoded)

```kotlin

data class CreateTrustedCircuitMessage(

}
```


## DenyTrustedCircuit (Low 393, NotTrusted, Unencoded)

```kotlin

data class DenyTrustedCircuitMessage(

}
```


## RequestTrustedCircuit (Low 394, Trusted, Unencoded)

```kotlin

data class RequestTrustedCircuitMessage(

}
```


## RezSingleAttachmentFromInv (Low 395, NotTrusted, Zerocoded)

```kotlin

data class RezSingleAttachmentFromInvMessage(

}
```


## RezMultipleAttachmentsFromInv (Low 396, NotTrusted, Zerocoded)

```kotlin

data class RezMultipleAttachmentsFromInvMessage(

}
```


## DetachAttachmentIntoInv (Low 397, NotTrusted, Unencoded)

```kotlin

data class DetachAttachmentIntoInvMessage(

}
```


## CreateNewOutfitAttachments (Low 398, NotTrusted, Unencoded)

```kotlin

data class CreateNewOutfitAttachmentsMessage(

}
```


## UserInfoRequest (Low 399, NotTrusted, Unencoded)

```kotlin

data class UserInfoRequestMessage(

}
```


## UserInfoReply (Low 400, NotTrusted, Unencoded)

```kotlin

data class UserInfoReplyMessage(

}
```


## UpdateUserInfo (Low 401, NotTrusted, Unencoded)

```kotlin

data class UpdateUserInfoMessage(

}
```


## ParcelRename (Low 402, Trusted, Unencoded)

```kotlin

data class ParcelRenameMessage(

}
```


## InitiateDownload (Low 403, NotTrusted, Unencoded)

```kotlin

data class InitiateDownloadMessage(

}
```


## SystemMessage (Low 404, Trusted, Zerocoded)

```kotlin

data class SystemMessageMessage(

}
```


## MapLayerRequest (Low 405, NotTrusted, Unencoded)

```kotlin

data class MapLayerRequestMessage(

}
```


## MapLayerReply (Low 406, Trusted, Unencoded)

```kotlin

data class MapLayerReplyMessage(

}
```


## MapBlockRequest (Low 407, NotTrusted, Unencoded)

```kotlin

data class MapBlockRequestMessage(

}
```


## MapNameRequest (Low 408, NotTrusted, Unencoded)

```kotlin

data class MapNameRequestMessage(

}
```


## MapBlockReply (Low 409, Trusted, Unencoded)

```kotlin

data class MapBlockReplyMessage(

}
```


## MapItemRequest (Low 410, NotTrusted, Unencoded)

```kotlin

data class MapItemRequestMessage(

}
```


## MapItemReply (Low 411, Trusted, Unencoded)

```kotlin

data class MapItemReplyMessage(

}
```


## SendPostcard (Low 412, NotTrusted, Unencoded)

```kotlin

data class SendPostcardMessage(

}
```


## RpcChannelRequest (Low 413, Trusted, Unencoded)

```kotlin

data class RpcChannelRequestMessage(

}
```


## RpcChannelReply (Low 414, Trusted, Unencoded)

```kotlin

data class RpcChannelReplyMessage(

}
```


## RpcScriptRequestInbound (Low 415, NotTrusted, Unencoded)

```kotlin

data class RpcScriptRequestInboundMessage(

}
```


## RpcScriptRequestInboundForward (Low 416, Trusted, Unencoded)

```kotlin

data class RpcScriptRequestInboundForwardMessage(

}
```


## RpcScriptReplyInbound (Low 417, NotTrusted, Unencoded)

```kotlin

data class RpcScriptReplyInboundMessage(

}
```


## ScriptMailRegistration (Low 418, Trusted, Unencoded)

```kotlin

data class ScriptMailRegistrationMessage(

}
```


## ParcelMediaCommandMessage (Low 419, Trusted, Unencoded)

```kotlin

data class ParcelMediaCommandMessageMessage(

}
```


## ParcelMediaUpdate (Low 420, Trusted, Unencoded)

```kotlin

data class ParcelMediaUpdateMessage(

}
```


## LandStatRequest (Low 421, NotTrusted, Unencoded)

```kotlin

data class LandStatRequestMessage(

}
```


## LandStatReply (Low 422, Trusted, Unencoded)

```kotlin

data class LandStatReplyMessage(

}
```


## Error (Low 423, NotTrusted, Zerocoded)

```kotlin

data class ErrorMessage(

}
```


## ObjectIncludeInSearch (Low 424, NotTrusted, Unencoded)

```kotlin

data class ObjectIncludeInSearchMessage(

}
```


## RezRestoreToWorld (Low 425, NotTrusted, Unencoded)

```kotlin

data class RezRestoreToWorldMessage(

}
```


## LinkInventoryItem (Low 426, NotTrusted, Zerocoded)

```kotlin

data class LinkInventoryItemMessage(

}
```


## RetrieveIMsExtended (Low 427, Trusted, Unencoded)

```kotlin

data class RetrieveIMsExtendedMessage(

}
```


## JoinGroupRequestExtended (Low 428, Trusted, Unencoded)

```kotlin

data class JoinGroupRequestExtendedMessage(

}
```


## CreateGroupRequestExtended (Low 429, Trusted, Unencoded)

```kotlin

data class CreateGroupRequestExtendedMessage(

}
```


## GameControlInput (High 32, NotTrusted, Zerocoded)

```kotlin

data class GameControlInputMessage(

}
```
