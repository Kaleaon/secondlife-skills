# Rust Message Stubs (generated from secondlife/master-message-template)

One stub per UDP message (483 messages) in Rust, generated from message_template.msg field definitions. These are starting points for a codec: implement ToBytes/FromBytes following the field order exactly, honour the zerocoded flag, and verify against LibreMetaverse.Protocol and the viewer template copy before shipping.


## TestMessage (Low 1, NotTrusted, Zerocoded)

```rust

pub struct TestMessageMessage {

}
```


## PacketAck (Fixed 0xFFFFFFFB, NotTrusted, Unencoded)

```rust

pub struct PacketAckMessage {

}
```


## OpenCircuit (Fixed 0xFFFFFFFC, NotTrusted, Unencoded)

```rust

pub struct OpenCircuitMessage {

}
```


## CloseCircuit (Fixed 0xFFFFFFFD, NotTrusted, Unencoded)

```rust

pub struct CloseCircuitMessage {

}
```


## StartPingCheck (High 1, NotTrusted, Unencoded)

```rust

pub struct StartPingCheckMessage {

}
```


## CompletePingCheck (High 2, NotTrusted, Unencoded)

```rust

pub struct CompletePingCheckMessage {

}
```


## AddCircuitCode (Low 2, Trusted, Unencoded)

```rust

pub struct AddCircuitCodeMessage {

}
```


## UseCircuitCode (Low 3, NotTrusted, Unencoded)

```rust

pub struct UseCircuitCodeMessage {

}
```


## NeighborList (High 3, Trusted, Unencoded)

```rust

pub struct NeighborListMessage {

}
```


## AvatarTextureUpdate (Low 4, Trusted, Zerocoded)

```rust

pub struct AvatarTextureUpdateMessage {

}
```


## SimulatorMapUpdate (Low 5, Trusted, Unencoded)

```rust

pub struct SimulatorMapUpdateMessage {

}
```


## SimulatorSetMap (Low 6, Trusted, Unencoded)

```rust

pub struct SimulatorSetMapMessage {

}
```


## SubscribeLoad (Low 7, Trusted, Unencoded)

```rust

pub struct SubscribeLoadMessage {

}
```


## UnsubscribeLoad (Low 8, Trusted, Unencoded)

```rust

pub struct UnsubscribeLoadMessage {

}
```


## SimulatorReady (Low 9, Trusted, Zerocoded)

```rust

pub struct SimulatorReadyMessage {

}
```


## TelehubInfo (Low 10, Trusted, Unencoded)

```rust

pub struct TelehubInfoMessage {

}
```


## SimulatorPresentAtLocation (Low 11, Trusted, Unencoded)

```rust

pub struct SimulatorPresentAtLocationMessage {

}
```


## SimulatorLoad (Low 12, Trusted, Unencoded)

```rust

pub struct SimulatorLoadMessage {

}
```


## SimulatorShutdownRequest (Low 13, Trusted, Unencoded)

```rust

pub struct SimulatorShutdownRequestMessage {

}
```


## RegionPresenceRequestByRegionID (Low 14, Trusted, Unencoded)

```rust

pub struct RegionPresenceRequestByRegionIDMessage {

}
```


## RegionPresenceRequestByHandle (Low 15, Trusted, Unencoded)

```rust

pub struct RegionPresenceRequestByHandleMessage {

}
```


## RegionPresenceResponse (Low 16, Trusted, Zerocoded)

```rust

pub struct RegionPresenceResponseMessage {

}
```


## UpdateSimulator (Low 17, Trusted, Unencoded)

```rust

pub struct UpdateSimulatorMessage {

}
```


## LogDwellTime (Low 18, Trusted, Unencoded)

```rust

pub struct LogDwellTimeMessage {

}
```


## FeatureDisabled (Low 19, Trusted, Unencoded)

```rust

pub struct FeatureDisabledMessage {

}
```


## LogFailedMoneyTransaction (Low 20, Trusted, Unencoded)

```rust

pub struct LogFailedMoneyTransactionMessage {

}
```


## UserReportInternal (Low 21, Trusted, Zerocoded)

```rust

pub struct UserReportInternalMessage {

}
```


## SetSimStatusInDatabase (Low 22, Trusted, Unencoded)

```rust

pub struct SetSimStatusInDatabaseMessage {

}
```


## SetSimPresenceInDatabase (Low 23, Trusted, Unencoded)

```rust

pub struct SetSimPresenceInDatabaseMessage {

}
```


## EconomyDataRequest (Low 24, NotTrusted, Unencoded)

```rust

pub struct EconomyDataRequestMessage {

}
```


## EconomyData (Low 25, Trusted, Zerocoded)

```rust

pub struct EconomyDataMessage {

}
```


## AvatarPickerRequest (Low 26, NotTrusted, Unencoded)

```rust

pub struct AvatarPickerRequestMessage {

}
```


## AvatarPickerRequestBackend (Low 27, Trusted, Unencoded)

```rust

pub struct AvatarPickerRequestBackendMessage {

}
```


## AvatarPickerReply (Low 28, Trusted, Unencoded)

```rust

pub struct AvatarPickerReplyMessage {

}
```


## PlacesQuery (Low 29, NotTrusted, Zerocoded)

```rust

pub struct PlacesQueryMessage {

}
```


## PlacesReply (Low 30, Trusted, Zerocoded)

```rust

pub struct PlacesReplyMessage {

}
```


## DirFindQuery (Low 31, NotTrusted, Zerocoded)

```rust

pub struct DirFindQueryMessage {

}
```


## DirFindQueryBackend (Low 32, Trusted, Zerocoded)

```rust

pub struct DirFindQueryBackendMessage {

}
```


## DirPlacesQuery (Low 33, NotTrusted, Zerocoded)

```rust

pub struct DirPlacesQueryMessage {

}
```


## DirPlacesQueryBackend (Low 34, Trusted, Zerocoded)

```rust

pub struct DirPlacesQueryBackendMessage {

}
```


## DirPlacesReply (Low 35, Trusted, Zerocoded)

```rust

pub struct DirPlacesReplyMessage {

}
```


## DirPeopleReply (Low 36, Trusted, Zerocoded)

```rust

pub struct DirPeopleReplyMessage {

}
```


## DirEventsReply (Low 37, Trusted, Zerocoded)

```rust

pub struct DirEventsReplyMessage {

}
```


## DirGroupsReply (Low 38, Trusted, Zerocoded)

```rust

pub struct DirGroupsReplyMessage {

}
```


## DirClassifiedQuery (Low 39, NotTrusted, Zerocoded)

```rust

pub struct DirClassifiedQueryMessage {

}
```


## DirClassifiedQueryBackend (Low 40, Trusted, Zerocoded)

```rust

pub struct DirClassifiedQueryBackendMessage {

}
```


## DirClassifiedReply (Low 41, Trusted, Zerocoded)

```rust

pub struct DirClassifiedReplyMessage {

}
```


## AvatarClassifiedReply (Low 42, Trusted, Unencoded)

```rust

pub struct AvatarClassifiedReplyMessage {

}
```


## ClassifiedInfoRequest (Low 43, NotTrusted, Zerocoded)

```rust

pub struct ClassifiedInfoRequestMessage {

}
```


## ClassifiedInfoReply (Low 44, Trusted, Unencoded)

```rust

pub struct ClassifiedInfoReplyMessage {

}
```


## ClassifiedInfoUpdate (Low 45, NotTrusted, Unencoded)

```rust

pub struct ClassifiedInfoUpdateMessage {

}
```


## ClassifiedDelete (Low 46, NotTrusted, Unencoded)

```rust

pub struct ClassifiedDeleteMessage {

}
```


## ClassifiedGodDelete (Low 47, NotTrusted, Unencoded)

```rust

pub struct ClassifiedGodDeleteMessage {

}
```


## DirLandQuery (Low 48, NotTrusted, Zerocoded)

```rust

pub struct DirLandQueryMessage {

}
```


## DirLandQueryBackend (Low 49, Trusted, Zerocoded)

```rust

pub struct DirLandQueryBackendMessage {

}
```


## DirLandReply (Low 50, Trusted, Zerocoded)

```rust

pub struct DirLandReplyMessage {

}
```


## DirPopularQuery (Low 51, NotTrusted, Zerocoded)

```rust

pub struct DirPopularQueryMessage {

}
```


## DirPopularQueryBackend (Low 52, Trusted, Zerocoded)

```rust

pub struct DirPopularQueryBackendMessage {

}
```


## DirPopularReply (Low 53, Trusted, Zerocoded)

```rust

pub struct DirPopularReplyMessage {

}
```


## ParcelInfoRequest (Low 54, NotTrusted, Unencoded)

```rust

pub struct ParcelInfoRequestMessage {

}
```


## ParcelInfoReply (Low 55, Trusted, Zerocoded)

```rust

pub struct ParcelInfoReplyMessage {

}
```


## ParcelObjectOwnersRequest (Low 56, NotTrusted, Unencoded)

```rust

pub struct ParcelObjectOwnersRequestMessage {

}
```


## ParcelObjectOwnersReply (Low 57, Trusted, Zerocoded)

```rust

pub struct ParcelObjectOwnersReplyMessage {

}
```


## GroupNoticesListRequest (Low 58, NotTrusted, Unencoded)

```rust

pub struct GroupNoticesListRequestMessage {

}
```


## GroupNoticesListReply (Low 59, Trusted, Unencoded)

```rust

pub struct GroupNoticesListReplyMessage {

}
```


## GroupNoticeRequest (Low 60, NotTrusted, Unencoded)

```rust

pub struct GroupNoticeRequestMessage {

}
```


## GroupNoticeAdd (Low 61, Trusted, Unencoded)

```rust

pub struct GroupNoticeAddMessage {

}
```


## TeleportRequest (Low 62, NotTrusted, Unencoded)

```rust

pub struct TeleportRequestMessage {

}
```


## TeleportLocationRequest (Low 63, NotTrusted, Unencoded)

```rust

pub struct TeleportLocationRequestMessage {

}
```


## TeleportLocal (Low 64, Trusted, Unencoded)

```rust

pub struct TeleportLocalMessage {

}
```


## TeleportLandmarkRequest (Low 65, NotTrusted, Zerocoded)

```rust

pub struct TeleportLandmarkRequestMessage {

}
```


## TeleportProgress (Low 66, Trusted, Unencoded)

```rust

pub struct TeleportProgressMessage {

}
```


## DataHomeLocationRequest (Low 67, Trusted, Zerocoded)

```rust

pub struct DataHomeLocationRequestMessage {

}
```


## DataHomeLocationReply (Low 68, Trusted, Unencoded)

```rust

pub struct DataHomeLocationReplyMessage {

}
```


## TeleportFinish (Low 69, Trusted, Unencoded)

```rust

pub struct TeleportFinishMessage {

}
```


## StartLure (Low 70, NotTrusted, Unencoded)

```rust

pub struct StartLureMessage {

}
```


## TeleportLureRequest (Low 71, NotTrusted, Unencoded)

```rust

pub struct TeleportLureRequestMessage {

}
```


## TeleportCancel (Low 72, NotTrusted, Unencoded)

```rust

pub struct TeleportCancelMessage {

}
```


## TeleportStart (Low 73, Trusted, Unencoded)

```rust

pub struct TeleportStartMessage {

}
```


## TeleportFailed (Low 74, Trusted, Unencoded)

```rust

pub struct TeleportFailedMessage {

}
```


## Undo (Low 75, NotTrusted, Unencoded)

```rust

pub struct UndoMessage {

}
```


## Redo (Low 76, NotTrusted, Unencoded)

```rust

pub struct RedoMessage {

}
```


## UndoLand (Low 77, NotTrusted, Unencoded)

```rust

pub struct UndoLandMessage {

}
```


## AgentPause (Low 78, NotTrusted, Unencoded)

```rust

pub struct AgentPauseMessage {

}
```


## AgentResume (Low 79, NotTrusted, Unencoded)

```rust

pub struct AgentResumeMessage {

}
```


## AgentUpdate (High 4, NotTrusted, Zerocoded)

```rust

pub struct AgentUpdateMessage {

}
```


## ChatFromViewer (Low 80, NotTrusted, Zerocoded)

```rust

pub struct ChatFromViewerMessage {

}
```


## AgentThrottle (Low 81, NotTrusted, Zerocoded)

```rust

pub struct AgentThrottleMessage {

}
```


## AgentFOV (Low 82, NotTrusted, Unencoded)

```rust

pub struct AgentFOVMessage {

}
```


## AgentHeightWidth (Low 83, NotTrusted, Unencoded)

```rust

pub struct AgentHeightWidthMessage {

}
```


## AgentSetAppearance (Low 84, NotTrusted, Zerocoded)

```rust

pub struct AgentSetAppearanceMessage {

}
```


## AgentAnimation (High 5, NotTrusted, Unencoded)

```rust

pub struct AgentAnimationMessage {

}
```


## AgentRequestSit (High 6, NotTrusted, Zerocoded)

```rust

pub struct AgentRequestSitMessage {

}
```


## AgentSit (High 7, NotTrusted, Unencoded)

```rust

pub struct AgentSitMessage {

}
```


## AgentQuitCopy (Low 85, NotTrusted, Unencoded)

```rust

pub struct AgentQuitCopyMessage {

}
```


## RequestImage (High 8, NotTrusted, Unencoded)

```rust

pub struct RequestImageMessage {

}
```


## ImageNotInDatabase (Low 86, Trusted, Unencoded)

```rust

pub struct ImageNotInDatabaseMessage {

}
```


## RebakeAvatarTextures (Low 87, Trusted, Unencoded)

```rust

pub struct RebakeAvatarTexturesMessage {

}
```


## SetAlwaysRun (Low 88, NotTrusted, Unencoded)

```rust

pub struct SetAlwaysRunMessage {

}
```


## ObjectAdd (Medium 1, NotTrusted, Zerocoded)

```rust

pub struct ObjectAddMessage {

}
```


## ObjectDelete (Low 89, NotTrusted, Zerocoded)

```rust

pub struct ObjectDeleteMessage {

}
```


## ObjectDuplicate (Low 90, NotTrusted, Zerocoded)

```rust

pub struct ObjectDuplicateMessage {

}
```


## ObjectDuplicateOnRay (Low 91, NotTrusted, Zerocoded)

```rust

pub struct ObjectDuplicateOnRayMessage {

}
```


## MultipleObjectUpdate (Medium 2, NotTrusted, Zerocoded)

```rust

pub struct MultipleObjectUpdateMessage {

}
```


## RequestMultipleObjects (Medium 3, NotTrusted, Zerocoded)

```rust

pub struct RequestMultipleObjectsMessage {

}
```


## ObjectPosition (Medium 4, NotTrusted, Zerocoded)

```rust

pub struct ObjectPositionMessage {

}
```


## ObjectScale (Low 92, NotTrusted, Zerocoded)

```rust

pub struct ObjectScaleMessage {

}
```


## ObjectRotation (Low 93, NotTrusted, Zerocoded)

```rust

pub struct ObjectRotationMessage {

}
```


## ObjectFlagUpdate (Low 94, NotTrusted, Zerocoded)

```rust

pub struct ObjectFlagUpdateMessage {

}
```


## ObjectClickAction (Low 95, NotTrusted, Zerocoded)

```rust

pub struct ObjectClickActionMessage {

}
```


## ObjectImage (Low 96, NotTrusted, Zerocoded)

```rust

pub struct ObjectImageMessage {

}
```


## ObjectBypassModUpdate (Low 431, NotTrusted, Zerocoded)

```rust

pub struct ObjectBypassModUpdateMessage {

}
```


## ObjectMaterial (Low 97, NotTrusted, Zerocoded)

```rust

pub struct ObjectMaterialMessage {

}
```


## ObjectShape (Low 98, NotTrusted, Zerocoded)

```rust

pub struct ObjectShapeMessage {

}
```


## ObjectExtraParams (Low 99, NotTrusted, Zerocoded)

```rust

pub struct ObjectExtraParamsMessage {

}
```


## ObjectOwner (Low 100, NotTrusted, Zerocoded)

```rust

pub struct ObjectOwnerMessage {

}
```


## ObjectGroup (Low 101, NotTrusted, Zerocoded)

```rust

pub struct ObjectGroupMessage {

}
```


## ObjectBuy (Low 102, NotTrusted, Zerocoded)

```rust

pub struct ObjectBuyMessage {

}
```


## BuyObjectInventory (Low 103, NotTrusted, Zerocoded)

```rust

pub struct BuyObjectInventoryMessage {

}
```


## DerezContainer (Low 104, Trusted, Zerocoded)

```rust

pub struct DerezContainerMessage {

}
```


## ObjectPermissions (Low 105, NotTrusted, Zerocoded)

```rust

pub struct ObjectPermissionsMessage {

}
```


## ObjectSaleInfo (Low 106, NotTrusted, Zerocoded)

```rust

pub struct ObjectSaleInfoMessage {

}
```


## ObjectName (Low 107, NotTrusted, Zerocoded)

```rust

pub struct ObjectNameMessage {

}
```


## ObjectDescription (Low 108, NotTrusted, Zerocoded)

```rust

pub struct ObjectDescriptionMessage {

}
```


## ObjectCategory (Low 109, NotTrusted, Zerocoded)

```rust

pub struct ObjectCategoryMessage {

}
```


## ObjectSelect (Low 110, NotTrusted, Zerocoded)

```rust

pub struct ObjectSelectMessage {

}
```


## ObjectDeselect (Low 111, NotTrusted, Zerocoded)

```rust

pub struct ObjectDeselectMessage {

}
```


## ObjectAttach (Low 112, NotTrusted, Zerocoded)

```rust

pub struct ObjectAttachMessage {

}
```


## ObjectDetach (Low 113, NotTrusted, Unencoded)

```rust

pub struct ObjectDetachMessage {

}
```


## ObjectDrop (Low 114, NotTrusted, Unencoded)

```rust

pub struct ObjectDropMessage {

}
```


## ObjectLink (Low 115, NotTrusted, Unencoded)

```rust

pub struct ObjectLinkMessage {

}
```


## ObjectDelink (Low 116, NotTrusted, Unencoded)

```rust

pub struct ObjectDelinkMessage {

}
```


## ObjectGrab (Low 117, NotTrusted, Zerocoded)

```rust

pub struct ObjectGrabMessage {

}
```


## ObjectGrabUpdate (Low 118, NotTrusted, Zerocoded)

```rust

pub struct ObjectGrabUpdateMessage {

}
```


## ObjectDeGrab (Low 119, NotTrusted, Unencoded)

```rust

pub struct ObjectDeGrabMessage {

}
```


## ObjectSpinStart (Low 120, NotTrusted, Zerocoded)

```rust

pub struct ObjectSpinStartMessage {

}
```


## ObjectSpinUpdate (Low 121, NotTrusted, Zerocoded)

```rust

pub struct ObjectSpinUpdateMessage {

}
```


## ObjectSpinStop (Low 122, NotTrusted, Zerocoded)

```rust

pub struct ObjectSpinStopMessage {

}
```


## ObjectExportSelected (Low 123, NotTrusted, Zerocoded)

```rust

pub struct ObjectExportSelectedMessage {

}
```


## ModifyLand (Low 124, NotTrusted, Zerocoded)

```rust

pub struct ModifyLandMessage {

}
```


## VelocityInterpolateOn (Low 125, NotTrusted, Unencoded)

```rust

pub struct VelocityInterpolateOnMessage {

}
```


## VelocityInterpolateOff (Low 126, NotTrusted, Unencoded)

```rust

pub struct VelocityInterpolateOffMessage {

}
```


## StateSave (Low 127, NotTrusted, Unencoded)

```rust

pub struct StateSaveMessage {

}
```


## ReportAutosaveCrash (Low 128, NotTrusted, Unencoded)

```rust

pub struct ReportAutosaveCrashMessage {

}
```


## SimWideDeletes (Low 129, NotTrusted, Unencoded)

```rust

pub struct SimWideDeletesMessage {

}
```


## RequestObjectPropertiesFamily (Medium 5, NotTrusted, Zerocoded)

```rust

pub struct RequestObjectPropertiesFamilyMessage {

}
```


## TrackAgent (Low 130, NotTrusted, Unencoded)

```rust

pub struct TrackAgentMessage {

}
```


## ViewerStats (Low 131, NotTrusted, Zerocoded)

```rust

pub struct ViewerStatsMessage {

}
```


## ScriptAnswerYes (Low 132, NotTrusted, Unencoded)

```rust

pub struct ScriptAnswerYesMessage {

}
```


## UserReport (Low 133, NotTrusted, Zerocoded)

```rust

pub struct UserReportMessage {

}
```


## AlertMessage (Low 134, Trusted, Unencoded)

```rust

pub struct AlertMessageMessage {

}
```


## AgentAlertMessage (Low 135, Trusted, Unencoded)

```rust

pub struct AgentAlertMessageMessage {

}
```


## MeanCollisionAlert (Low 136, Trusted, Zerocoded)

```rust

pub struct MeanCollisionAlertMessage {

}
```


## ViewerFrozenMessage (Low 137, Trusted, Unencoded)

```rust

pub struct ViewerFrozenMessageMessage {

}
```


## HealthMessage (Low 138, Trusted, Zerocoded)

```rust

pub struct HealthMessageMessage {

}
```


## ChatFromSimulator (Low 139, Trusted, Unencoded)

```rust

pub struct ChatFromSimulatorMessage {

}
```


## SimStats (Low 140, Trusted, Unencoded)

```rust

pub struct SimStatsMessage {

}
```


## RequestRegionInfo (Low 141, NotTrusted, Unencoded)

```rust

pub struct RequestRegionInfoMessage {

}
```


## RegionInfo (Low 142, NotTrusted, Zerocoded)

```rust

pub struct RegionInfoMessage {

}
```


## GodUpdateRegionInfo (Low 143, NotTrusted, Zerocoded)

```rust

pub struct GodUpdateRegionInfoMessage {

}
```


## NearestLandingRegionRequest (Low 144, Trusted, Unencoded)

```rust

pub struct NearestLandingRegionRequestMessage {

}
```


## NearestLandingRegionReply (Low 145, Trusted, Unencoded)

```rust

pub struct NearestLandingRegionReplyMessage {

}
```


## NearestLandingRegionUpdated (Low 146, Trusted, Unencoded)

```rust

pub struct NearestLandingRegionUpdatedMessage {

}
```


## TeleportLandingStatusChanged (Low 147, Trusted, Unencoded)

```rust

pub struct TeleportLandingStatusChangedMessage {

}
```


## RegionHandshake (Low 148, Trusted, Zerocoded)

```rust

pub struct RegionHandshakeMessage {

}
```


## RegionHandshakeReply (Low 149, NotTrusted, Zerocoded)

```rust

pub struct RegionHandshakeReplyMessage {

}
```


## CoarseLocationUpdate (Medium 6, Trusted, Unencoded)

```rust

pub struct CoarseLocationUpdateMessage {

}
```


## ImageData (High 9, Trusted, Unencoded)

```rust

pub struct ImageDataMessage {

}
```


## ImagePacket (High 10, Trusted, Unencoded)

```rust

pub struct ImagePacketMessage {

}
```


## LayerData (High 11, Trusted, Unencoded)

```rust

pub struct LayerDataMessage {

}
```


## ObjectUpdate (High 12, Trusted, Zerocoded)

```rust

pub struct ObjectUpdateMessage {

}
```


## ObjectUpdateCompressed (High 13, Trusted, Unencoded)

```rust

pub struct ObjectUpdateCompressedMessage {

}
```


## ObjectUpdateCached (High 14, Trusted, Unencoded)

```rust

pub struct ObjectUpdateCachedMessage {

}
```


## ImprovedTerseObjectUpdate (High 15, Trusted, Unencoded)

```rust

pub struct ImprovedTerseObjectUpdateMessage {

}
```


## KillObject (High 16, Trusted, Unencoded)

```rust

pub struct KillObjectMessage {

}
```


## CrossedRegion (Medium 7, Trusted, Unencoded)

```rust

pub struct CrossedRegionMessage {

}
```


## SimulatorViewerTimeMessage (Low 150, Trusted, Unencoded)

```rust

pub struct SimulatorViewerTimeMessageMessage {

}
```


## EnableSimulator (Low 151, Trusted, Unencoded)

```rust

pub struct EnableSimulatorMessage {

}
```


## DisableSimulator (Low 152, Trusted, Unencoded)

```rust

pub struct DisableSimulatorMessage {

}
```


## ConfirmEnableSimulator (Medium 8, Trusted, Unencoded)

```rust

pub struct ConfirmEnableSimulatorMessage {

}
```


## TransferRequest (Low 153, NotTrusted, Zerocoded)

```rust

pub struct TransferRequestMessage {

}
```


## TransferInfo (Low 154, NotTrusted, Zerocoded)

```rust

pub struct TransferInfoMessage {

}
```


## TransferPacket (High 17, NotTrusted, Unencoded)

```rust

pub struct TransferPacketMessage {

}
```


## TransferAbort (Low 155, NotTrusted, Zerocoded)

```rust

pub struct TransferAbortMessage {

}
```


## RequestXfer (Low 156, NotTrusted, Zerocoded)

```rust

pub struct RequestXferMessage {

}
```


## SendXferPacket (High 18, NotTrusted, Unencoded)

```rust

pub struct SendXferPacketMessage {

}
```


## ConfirmXferPacket (High 19, NotTrusted, Unencoded)

```rust

pub struct ConfirmXferPacketMessage {

}
```


## AbortXfer (Low 157, NotTrusted, Unencoded)

```rust

pub struct AbortXferMessage {

}
```


## AvatarAnimation (High 20, Trusted, Unencoded)

```rust

pub struct AvatarAnimationMessage {

}
```


## AvatarAppearance (Low 158, Trusted, Zerocoded)

```rust

pub struct AvatarAppearanceMessage {

}
```


## AvatarSitResponse (High 21, Trusted, Zerocoded)

```rust

pub struct AvatarSitResponseMessage {

}
```


## SetFollowCamProperties (Low 159, Trusted, Unencoded)

```rust

pub struct SetFollowCamPropertiesMessage {

}
```


## ClearFollowCamProperties (Low 160, Trusted, Unencoded)

```rust

pub struct ClearFollowCamPropertiesMessage {

}
```


## CameraConstraint (High 22, Trusted, Zerocoded)

```rust

pub struct CameraConstraintMessage {

}
```


## ObjectProperties (Medium 9, Trusted, Zerocoded)

```rust

pub struct ObjectPropertiesMessage {

}
```


## ObjectPropertiesFamily (Medium 10, Trusted, Zerocoded)

```rust

pub struct ObjectPropertiesFamilyMessage {

}
```


## RequestPayPrice (Low 161, NotTrusted, Unencoded)

```rust

pub struct RequestPayPriceMessage {

}
```


## PayPriceReply (Low 162, Trusted, Unencoded)

```rust

pub struct PayPriceReplyMessage {

}
```


## KickUser (Low 163, Trusted, Unencoded)

```rust

pub struct KickUserMessage {

}
```


## KickUserAck (Low 164, Trusted, Unencoded)

```rust

pub struct KickUserAckMessage {

}
```


## GodKickUser (Low 165, NotTrusted, Unencoded)

```rust

pub struct GodKickUserMessage {

}
```


## SystemKickUser (Low 166, Trusted, Unencoded)

```rust

pub struct SystemKickUserMessage {

}
```


## EjectUser (Low 167, NotTrusted, Unencoded)

```rust

pub struct EjectUserMessage {

}
```


## FreezeUser (Low 168, NotTrusted, Unencoded)

```rust

pub struct FreezeUserMessage {

}
```


## AvatarPropertiesRequest (Low 169, NotTrusted, Unencoded)

```rust

pub struct AvatarPropertiesRequestMessage {

}
```


## AvatarPropertiesRequestBackend (Low 170, Trusted, Unencoded)

```rust

pub struct AvatarPropertiesRequestBackendMessage {

}
```


## AvatarPropertiesReply (Low 171, Trusted, Zerocoded)

```rust

pub struct AvatarPropertiesReplyMessage {

}
```


## AvatarInterestsReply (Low 172, Trusted, Zerocoded)

```rust

pub struct AvatarInterestsReplyMessage {

}
```


## AvatarGroupsReply (Low 173, Trusted, Zerocoded)

```rust

pub struct AvatarGroupsReplyMessage {

}
```


## AvatarPropertiesUpdate (Low 174, NotTrusted, Zerocoded)

```rust

pub struct AvatarPropertiesUpdateMessage {

}
```


## AvatarInterestsUpdate (Low 175, NotTrusted, Zerocoded)

```rust

pub struct AvatarInterestsUpdateMessage {

}
```


## AvatarNotesReply (Low 176, Trusted, Unencoded)

```rust

pub struct AvatarNotesReplyMessage {

}
```


## AvatarNotesUpdate (Low 177, NotTrusted, Unencoded)

```rust

pub struct AvatarNotesUpdateMessage {

}
```


## AvatarPicksReply (Low 178, Trusted, Unencoded)

```rust

pub struct AvatarPicksReplyMessage {

}
```


## EventInfoRequest (Low 179, NotTrusted, Unencoded)

```rust

pub struct EventInfoRequestMessage {

}
```


## EventInfoReply (Low 180, Trusted, Unencoded)

```rust

pub struct EventInfoReplyMessage {

}
```


## EventNotificationAddRequest (Low 181, NotTrusted, Unencoded)

```rust

pub struct EventNotificationAddRequestMessage {

}
```


## EventNotificationRemoveRequest (Low 182, NotTrusted, Unencoded)

```rust

pub struct EventNotificationRemoveRequestMessage {

}
```


## EventGodDelete (Low 183, NotTrusted, Unencoded)

```rust

pub struct EventGodDeleteMessage {

}
```


## PickInfoReply (Low 184, Trusted, Unencoded)

```rust

pub struct PickInfoReplyMessage {

}
```


## PickInfoUpdate (Low 185, NotTrusted, Unencoded)

```rust

pub struct PickInfoUpdateMessage {

}
```


## PickDelete (Low 186, NotTrusted, Unencoded)

```rust

pub struct PickDeleteMessage {

}
```


## PickGodDelete (Low 187, NotTrusted, Unencoded)

```rust

pub struct PickGodDeleteMessage {

}
```


## ScriptQuestion (Low 188, Trusted, Unencoded)

```rust

pub struct ScriptQuestionMessage {

}
```


## ScriptControlChange (Low 189, Trusted, Unencoded)

```rust

pub struct ScriptControlChangeMessage {

}
```


## ScriptDialog (Low 190, Trusted, Zerocoded)

```rust

pub struct ScriptDialogMessage {

}
```


## ScriptDialogReply (Low 191, NotTrusted, Zerocoded)

```rust

pub struct ScriptDialogReplyMessage {

}
```


## ForceScriptControlRelease (Low 192, NotTrusted, Unencoded)

```rust

pub struct ForceScriptControlReleaseMessage {

}
```


## RevokePermissions (Low 193, NotTrusted, Unencoded)

```rust

pub struct RevokePermissionsMessage {

}
```


## LoadURL (Low 194, Trusted, Unencoded)

```rust

pub struct LoadURLMessage {

}
```


## ScriptTeleportRequest (Low 195, Trusted, Unencoded)

```rust

pub struct ScriptTeleportRequestMessage {

}
```


## ParcelOverlay (Low 196, Trusted, Zerocoded)

```rust

pub struct ParcelOverlayMessage {

}
```


## ParcelPropertiesRequest (Medium 11, NotTrusted, Zerocoded)

```rust

pub struct ParcelPropertiesRequestMessage {

}
```


## ParcelPropertiesRequestByID (Low 197, NotTrusted, Zerocoded)

```rust

pub struct ParcelPropertiesRequestByIDMessage {

}
```


## ParcelProperties (High 23, Trusted, Zerocoded)

```rust

pub struct ParcelPropertiesMessage {

}
```


## ParcelPropertiesUpdate (Low 198, NotTrusted, Zerocoded)

```rust

pub struct ParcelPropertiesUpdateMessage {

}
```


## ParcelReturnObjects (Low 199, NotTrusted, Zerocoded)

```rust

pub struct ParcelReturnObjectsMessage {

}
```


## ParcelSetOtherCleanTime (Low 200, NotTrusted, Zerocoded)

```rust

pub struct ParcelSetOtherCleanTimeMessage {

}
```


## ParcelDisableObjects (Low 201, NotTrusted, Zerocoded)

```rust

pub struct ParcelDisableObjectsMessage {

}
```


## ParcelSelectObjects (Low 202, NotTrusted, Zerocoded)

```rust

pub struct ParcelSelectObjectsMessage {

}
```


## EstateCovenantRequest (Low 203, NotTrusted, Unencoded)

```rust

pub struct EstateCovenantRequestMessage {

}
```


## EstateCovenantReply (Low 204, Trusted, Unencoded)

```rust

pub struct EstateCovenantReplyMessage {

}
```


## ForceObjectSelect (Low 205, Trusted, Unencoded)

```rust

pub struct ForceObjectSelectMessage {

}
```


## ParcelBuyPass (Low 206, NotTrusted, Unencoded)

```rust

pub struct ParcelBuyPassMessage {

}
```


## ParcelDeedToGroup (Low 207, NotTrusted, Unencoded)

```rust

pub struct ParcelDeedToGroupMessage {

}
```


## ParcelReclaim (Low 208, NotTrusted, Unencoded)

```rust

pub struct ParcelReclaimMessage {

}
```


## ParcelClaim (Low 209, NotTrusted, Zerocoded)

```rust

pub struct ParcelClaimMessage {

}
```


## ParcelJoin (Low 210, NotTrusted, Unencoded)

```rust

pub struct ParcelJoinMessage {

}
```


## ParcelDivide (Low 211, NotTrusted, Unencoded)

```rust

pub struct ParcelDivideMessage {

}
```


## ParcelRelease (Low 212, NotTrusted, Unencoded)

```rust

pub struct ParcelReleaseMessage {

}
```


## ParcelBuy (Low 213, NotTrusted, Zerocoded)

```rust

pub struct ParcelBuyMessage {

}
```


## ParcelGodForceOwner (Low 214, NotTrusted, Zerocoded)

```rust

pub struct ParcelGodForceOwnerMessage {

}
```


## ParcelAccessListRequest (Low 215, NotTrusted, Zerocoded)

```rust

pub struct ParcelAccessListRequestMessage {

}
```


## ParcelAccessListReply (Low 216, Trusted, Zerocoded)

```rust

pub struct ParcelAccessListReplyMessage {

}
```


## ParcelAccessListUpdate (Low 217, NotTrusted, Zerocoded)

```rust

pub struct ParcelAccessListUpdateMessage {

}
```


## ParcelDwellRequest (Low 218, NotTrusted, Unencoded)

```rust

pub struct ParcelDwellRequestMessage {

}
```


## ParcelDwellReply (Low 219, Trusted, Unencoded)

```rust

pub struct ParcelDwellReplyMessage {

}
```


## RequestParcelTransfer (Low 220, Trusted, Zerocoded)

```rust

pub struct RequestParcelTransferMessage {

}
```


## UpdateParcel (Low 221, Trusted, Zerocoded)

```rust

pub struct UpdateParcelMessage {

}
```


## RemoveParcel (Low 222, Trusted, Unencoded)

```rust

pub struct RemoveParcelMessage {

}
```


## MergeParcel (Low 223, Trusted, Unencoded)

```rust

pub struct MergeParcelMessage {

}
```


## LogParcelChanges (Low 224, Trusted, Zerocoded)

```rust

pub struct LogParcelChangesMessage {

}
```


## CheckParcelSales (Low 225, Trusted, Unencoded)

```rust

pub struct CheckParcelSalesMessage {

}
```


## ParcelSales (Low 226, Trusted, Unencoded)

```rust

pub struct ParcelSalesMessage {

}
```


## ParcelGodMarkAsContent (Low 227, NotTrusted, Unencoded)

```rust

pub struct ParcelGodMarkAsContentMessage {

}
```


## ViewerStartAuction (Low 228, NotTrusted, Unencoded)

```rust

pub struct ViewerStartAuctionMessage {

}
```


## StartAuction (Low 229, Trusted, Unencoded)

```rust

pub struct StartAuctionMessage {

}
```


## ConfirmAuctionStart (Low 230, Trusted, Unencoded)

```rust

pub struct ConfirmAuctionStartMessage {

}
```


## CompleteAuction (Low 231, Trusted, Unencoded)

```rust

pub struct CompleteAuctionMessage {

}
```


## CancelAuction (Low 232, Trusted, Unencoded)

```rust

pub struct CancelAuctionMessage {

}
```


## CheckParcelAuctions (Low 233, Trusted, Unencoded)

```rust

pub struct CheckParcelAuctionsMessage {

}
```


## ParcelAuctions (Low 234, Trusted, Unencoded)

```rust

pub struct ParcelAuctionsMessage {

}
```


## UUIDNameRequest (Low 235, NotTrusted, Unencoded)

```rust

pub struct UUIDNameRequestMessage {

}
```


## UUIDNameReply (Low 236, Trusted, Unencoded)

```rust

pub struct UUIDNameReplyMessage {

}
```


## UUIDGroupNameRequest (Low 237, NotTrusted, Unencoded)

```rust

pub struct UUIDGroupNameRequestMessage {

}
```


## UUIDGroupNameReply (Low 238, Trusted, Unencoded)

```rust

pub struct UUIDGroupNameReplyMessage {

}
```


## ChatPass (Low 239, Trusted, Zerocoded)

```rust

pub struct ChatPassMessage {

}
```


## EdgeDataPacket (High 24, Trusted, Zerocoded)

```rust

pub struct EdgeDataPacketMessage {

}
```


## SimStatus (Medium 12, Trusted, Unencoded)

```rust

pub struct SimStatusMessage {

}
```


## ChildAgentUpdate (High 25, Trusted, Zerocoded)

```rust

pub struct ChildAgentUpdateMessage {

}
```


## ChildAgentAlive (High 26, Trusted, Unencoded)

```rust

pub struct ChildAgentAliveMessage {

}
```


## ChildAgentPositionUpdate (High 27, Trusted, Unencoded)

```rust

pub struct ChildAgentPositionUpdateMessage {

}
```


## ChildAgentDying (Low 240, Trusted, Zerocoded)

```rust

pub struct ChildAgentDyingMessage {

}
```


## ChildAgentUnknown (Low 241, Trusted, Unencoded)

```rust

pub struct ChildAgentUnknownMessage {

}
```


## AtomicPassObject (High 28, Trusted, Unencoded)

```rust

pub struct AtomicPassObjectMessage {

}
```


## KillChildAgents (Low 242, Trusted, Unencoded)

```rust

pub struct KillChildAgentsMessage {

}
```


## GetScriptRunning (Low 243, NotTrusted, Unencoded)

```rust

pub struct GetScriptRunningMessage {

}
```


## ScriptRunningReply (Low 244, NotTrusted, Unencoded)

```rust

pub struct ScriptRunningReplyMessage {

}
```


## SetScriptRunning (Low 245, NotTrusted, Unencoded)

```rust

pub struct SetScriptRunningMessage {

}
```


## ScriptReset (Low 246, NotTrusted, Unencoded)

```rust

pub struct ScriptResetMessage {

}
```


## ScriptSensorRequest (Low 247, Trusted, Zerocoded)

```rust

pub struct ScriptSensorRequestMessage {

}
```


## ScriptSensorReply (Low 248, Trusted, Zerocoded)

```rust

pub struct ScriptSensorReplyMessage {

}
```


## CompleteAgentMovement (Low 249, NotTrusted, Unencoded)

```rust

pub struct CompleteAgentMovementMessage {

}
```


## AgentMovementComplete (Low 250, NotTrusted, Unencoded)

```rust

pub struct AgentMovementCompleteMessage {

}
```


## DataServerLogout (Low 251, Trusted, Unencoded)

```rust

pub struct DataServerLogoutMessage {

}
```


## LogoutRequest (Low 252, NotTrusted, Unencoded)

```rust

pub struct LogoutRequestMessage {

}
```


## LogoutReply (Low 253, Trusted, Zerocoded)

```rust

pub struct LogoutReplyMessage {

}
```


## ImprovedInstantMessage (Low 254, NotTrusted, Zerocoded)

```rust

pub struct ImprovedInstantMessageMessage {

}
```


## RetrieveInstantMessages (Low 255, NotTrusted, Unencoded)

```rust

pub struct RetrieveInstantMessagesMessage {

}
```


## FindAgent (Low 256, NotTrusted, Unencoded)

```rust

pub struct FindAgentMessage {

}
```


## RequestGodlikePowers (Low 257, NotTrusted, Unencoded)

```rust

pub struct RequestGodlikePowersMessage {

}
```


## GrantGodlikePowers (Low 258, Trusted, Unencoded)

```rust

pub struct GrantGodlikePowersMessage {

}
```


## GodlikeMessage (Low 259, NotTrusted, Zerocoded)

```rust

pub struct GodlikeMessageMessage {

}
```


## EstateOwnerMessage (Low 260, NotTrusted, Zerocoded)

```rust

pub struct EstateOwnerMessageMessage {

}
```


## GenericMessage (Low 261, NotTrusted, Zerocoded)

```rust

pub struct GenericMessageMessage {

}
```


## GenericStreamingMessage (High 31, Trusted, Unencoded)

```rust

pub struct GenericStreamingMessageMessage {

}
```


## LargeGenericMessage (Low 430, NotTrusted, Unencoded)

```rust

pub struct LargeGenericMessageMessage {

}
```


## MuteListRequest (Low 262, NotTrusted, Unencoded)

```rust

pub struct MuteListRequestMessage {

}
```


## UpdateMuteListEntry (Low 263, NotTrusted, Unencoded)

```rust

pub struct UpdateMuteListEntryMessage {

}
```


## RemoveMuteListEntry (Low 264, NotTrusted, Unencoded)

```rust

pub struct RemoveMuteListEntryMessage {

}
```


## CopyInventoryFromNotecard (Low 265, NotTrusted, Zerocoded)

```rust

pub struct CopyInventoryFromNotecardMessage {

}
```


## UpdateInventoryItem (Low 266, NotTrusted, Zerocoded)

```rust

pub struct UpdateInventoryItemMessage {

}
```


## UpdateCreateInventoryItem (Low 267, Trusted, Zerocoded)

```rust

pub struct UpdateCreateInventoryItemMessage {

}
```


## MoveInventoryItem (Low 268, NotTrusted, Zerocoded)

```rust

pub struct MoveInventoryItemMessage {

}
```


## CopyInventoryItem (Low 269, NotTrusted, Zerocoded)

```rust

pub struct CopyInventoryItemMessage {

}
```


## RemoveInventoryItem (Low 270, NotTrusted, Unencoded)

```rust

pub struct RemoveInventoryItemMessage {

}
```


## ChangeInventoryItemFlags (Low 271, NotTrusted, Unencoded)

```rust

pub struct ChangeInventoryItemFlagsMessage {

}
```


## SaveAssetIntoInventory (Low 272, Trusted, Unencoded)

```rust

pub struct SaveAssetIntoInventoryMessage {

}
```


## CreateInventoryFolder (Low 273, NotTrusted, Unencoded)

```rust

pub struct CreateInventoryFolderMessage {

}
```


## UpdateInventoryFolder (Low 274, NotTrusted, Unencoded)

```rust

pub struct UpdateInventoryFolderMessage {

}
```


## MoveInventoryFolder (Low 275, NotTrusted, Zerocoded)

```rust

pub struct MoveInventoryFolderMessage {

}
```


## RemoveInventoryFolder (Low 276, NotTrusted, Unencoded)

```rust

pub struct RemoveInventoryFolderMessage {

}
```


## FetchInventoryDescendents (Low 277, NotTrusted, Zerocoded)

```rust

pub struct FetchInventoryDescendentsMessage {

}
```


## InventoryDescendents (Low 278, Trusted, Zerocoded)

```rust

pub struct InventoryDescendentsMessage {

}
```


## FetchInventory (Low 279, NotTrusted, Zerocoded)

```rust

pub struct FetchInventoryMessage {

}
```


## FetchInventoryReply (Low 280, Trusted, Zerocoded)

```rust

pub struct FetchInventoryReplyMessage {

}
```


## BulkUpdateInventory (Low 281, Trusted, Zerocoded)

```rust

pub struct BulkUpdateInventoryMessage {

}
```


## RequestInventoryAsset (Low 282, Trusted, Unencoded)

```rust

pub struct RequestInventoryAssetMessage {

}
```


## InventoryAssetResponse (Low 283, Trusted, Unencoded)

```rust

pub struct InventoryAssetResponseMessage {

}
```


## RemoveInventoryObjects (Low 284, NotTrusted, Unencoded)

```rust

pub struct RemoveInventoryObjectsMessage {

}
```


## PurgeInventoryDescendents (Low 285, NotTrusted, Zerocoded)

```rust

pub struct PurgeInventoryDescendentsMessage {

}
```


## UpdateTaskInventory (Low 286, NotTrusted, Zerocoded)

```rust

pub struct UpdateTaskInventoryMessage {

}
```


## RemoveTaskInventory (Low 287, NotTrusted, Zerocoded)

```rust

pub struct RemoveTaskInventoryMessage {

}
```


## MoveTaskInventory (Low 288, NotTrusted, Unencoded)

```rust

pub struct MoveTaskInventoryMessage {

}
```


## RequestTaskInventory (Low 289, NotTrusted, Unencoded)

```rust

pub struct RequestTaskInventoryMessage {

}
```


## ReplyTaskInventory (Low 290, Trusted, Zerocoded)

```rust

pub struct ReplyTaskInventoryMessage {

}
```


## DeRezObject (Low 291, NotTrusted, Zerocoded)

```rust

pub struct DeRezObjectMessage {

}
```


## DeRezAck (Low 292, Trusted, Unencoded)

```rust

pub struct DeRezAckMessage {

}
```


## RezObject (Low 293, NotTrusted, Zerocoded)

```rust

pub struct RezObjectMessage {

}
```


## RezObjectFromNotecard (Low 294, NotTrusted, Zerocoded)

```rust

pub struct RezObjectFromNotecardMessage {

}
```


## TransferInventory (Low 295, Trusted, Zerocoded)

```rust

pub struct TransferInventoryMessage {

}
```


## TransferInventoryAck (Low 296, Trusted, Zerocoded)

```rust

pub struct TransferInventoryAckMessage {

}
```


## AcceptFriendship (Low 297, NotTrusted, Unencoded)

```rust

pub struct AcceptFriendshipMessage {

}
```


## DeclineFriendship (Low 298, NotTrusted, Unencoded)

```rust

pub struct DeclineFriendshipMessage {

}
```


## FormFriendship (Low 299, Trusted, Unencoded)

```rust

pub struct FormFriendshipMessage {

}
```


## TerminateFriendship (Low 300, NotTrusted, Unencoded)

```rust

pub struct TerminateFriendshipMessage {

}
```


## OfferCallingCard (Low 301, NotTrusted, Unencoded)

```rust

pub struct OfferCallingCardMessage {

}
```


## AcceptCallingCard (Low 302, NotTrusted, Unencoded)

```rust

pub struct AcceptCallingCardMessage {

}
```


## DeclineCallingCard (Low 303, NotTrusted, Unencoded)

```rust

pub struct DeclineCallingCardMessage {

}
```


## RezScript (Low 304, NotTrusted, Zerocoded)

```rust

pub struct RezScriptMessage {

}
```


## CreateInventoryItem (Low 305, NotTrusted, Zerocoded)

```rust

pub struct CreateInventoryItemMessage {

}
```


## CreateLandmarkForEvent (Low 306, NotTrusted, Zerocoded)

```rust

pub struct CreateLandmarkForEventMessage {

}
```


## EventLocationRequest (Low 307, Trusted, Zerocoded)

```rust

pub struct EventLocationRequestMessage {

}
```


## EventLocationReply (Low 308, Trusted, Zerocoded)

```rust

pub struct EventLocationReplyMessage {

}
```


## RegionHandleRequest (Low 309, NotTrusted, Unencoded)

```rust

pub struct RegionHandleRequestMessage {

}
```


## RegionIDAndHandleReply (Low 310, Trusted, Unencoded)

```rust

pub struct RegionIDAndHandleReplyMessage {

}
```


## MoneyTransferRequest (Low 311, NotTrusted, Zerocoded)

```rust

pub struct MoneyTransferRequestMessage {

}
```


## MoneyTransferBackend (Low 312, Trusted, Zerocoded)

```rust

pub struct MoneyTransferBackendMessage {

}
```


## MoneyBalanceRequest (Low 313, NotTrusted, Zerocoded)

```rust

pub struct MoneyBalanceRequestMessage {

}
```


## MoneyBalanceReply (Low 314, Trusted, Zerocoded)

```rust

pub struct MoneyBalanceReplyMessage {

}
```


## RoutedMoneyBalanceReply (Low 315, Trusted, Zerocoded)

```rust

pub struct RoutedMoneyBalanceReplyMessage {

}
```


## ActivateGestures (Low 316, NotTrusted, Unencoded)

```rust

pub struct ActivateGesturesMessage {

}
```


## DeactivateGestures (Low 317, NotTrusted, Unencoded)

```rust

pub struct DeactivateGesturesMessage {

}
```


## MuteListUpdate (Low 318, Trusted, Unencoded)

```rust

pub struct MuteListUpdateMessage {

}
```


## UseCachedMuteList (Low 319, NotTrusted, Unencoded)

```rust

pub struct UseCachedMuteListMessage {

}
```


## GrantUserRights (Low 320, NotTrusted, Unencoded)

```rust

pub struct GrantUserRightsMessage {

}
```


## ChangeUserRights (Low 321, Trusted, Unencoded)

```rust

pub struct ChangeUserRightsMessage {

}
```


## OnlineNotification (Low 322, Trusted, Unencoded)

```rust

pub struct OnlineNotificationMessage {

}
```


## OfflineNotification (Low 323, Trusted, Unencoded)

```rust

pub struct OfflineNotificationMessage {

}
```


## SetStartLocationRequest (Low 324, NotTrusted, Zerocoded)

```rust

pub struct SetStartLocationRequestMessage {

}
```


## SetStartLocation (Low 325, Trusted, Zerocoded)

```rust

pub struct SetStartLocationMessage {

}
```


## NetTest (Low 326, NotTrusted, Unencoded)

```rust

pub struct NetTestMessage {

}
```


## SetCPURatio (Low 327, NotTrusted, Unencoded)

```rust

pub struct SetCPURatioMessage {

}
```


## SimCrashed (Low 328, NotTrusted, Unencoded)

```rust

pub struct SimCrashedMessage {

}
```


## NameValuePair (Low 329, Trusted, Unencoded)

```rust

pub struct NameValuePairMessage {

}
```


## RemoveNameValuePair (Low 330, Trusted, Unencoded)

```rust

pub struct RemoveNameValuePairMessage {

}
```


## UpdateAttachment (Low 331, Trusted, Zerocoded)

```rust

pub struct UpdateAttachmentMessage {

}
```


## RemoveAttachment (Low 332, NotTrusted, Unencoded)

```rust

pub struct RemoveAttachmentMessage {

}
```


## SoundTrigger (High 29, NotTrusted, Unencoded)

```rust

pub struct SoundTriggerMessage {

}
```


## AttachedSound (Medium 13, Trusted, Unencoded)

```rust

pub struct AttachedSoundMessage {

}
```


## AttachedSoundGainChange (Medium 14, Trusted, Unencoded)

```rust

pub struct AttachedSoundGainChangeMessage {

}
```


## PreloadSound (Medium 15, Trusted, Unencoded)

```rust

pub struct PreloadSoundMessage {

}
```


## ObjectAnimation (High 30, Trusted, Unencoded)

```rust

pub struct ObjectAnimationMessage {

}
```


## AssetUploadRequest (Low 333, NotTrusted, Unencoded)

```rust

pub struct AssetUploadRequestMessage {

}
```


## AssetUploadComplete (Low 334, NotTrusted, Unencoded)

```rust

pub struct AssetUploadCompleteMessage {

}
```


## EmailMessageRequest (Low 335, Trusted, Unencoded)

```rust

pub struct EmailMessageRequestMessage {

}
```


## EmailMessageReply (Low 336, Trusted, Unencoded)

```rust

pub struct EmailMessageReplyMessage {

}
```


## InternalScriptMail (Medium 16, Trusted, Unencoded)

```rust

pub struct InternalScriptMailMessage {

}
```


## ScriptDataRequest (Low 337, Trusted, Unencoded)

```rust

pub struct ScriptDataRequestMessage {

}
```


## ScriptDataReply (Low 338, Trusted, Unencoded)

```rust

pub struct ScriptDataReplyMessage {

}
```


## CreateGroupRequest (Low 339, NotTrusted, Zerocoded)

```rust

pub struct CreateGroupRequestMessage {

}
```


## CreateGroupReply (Low 340, Trusted, Unencoded)

```rust

pub struct CreateGroupReplyMessage {

}
```


## UpdateGroupInfo (Low 341, NotTrusted, Zerocoded)

```rust

pub struct UpdateGroupInfoMessage {

}
```


## GroupRoleChanges (Low 342, NotTrusted, Unencoded)

```rust

pub struct GroupRoleChangesMessage {

}
```


## JoinGroupRequest (Low 343, NotTrusted, Zerocoded)

```rust

pub struct JoinGroupRequestMessage {

}
```


## JoinGroupReply (Low 344, Trusted, Unencoded)

```rust

pub struct JoinGroupReplyMessage {

}
```


## EjectGroupMemberRequest (Low 345, NotTrusted, Unencoded)

```rust

pub struct EjectGroupMemberRequestMessage {

}
```


## EjectGroupMemberReply (Low 346, Trusted, Unencoded)

```rust

pub struct EjectGroupMemberReplyMessage {

}
```


## LeaveGroupRequest (Low 347, NotTrusted, Unencoded)

```rust

pub struct LeaveGroupRequestMessage {

}
```


## LeaveGroupReply (Low 348, Trusted, Unencoded)

```rust

pub struct LeaveGroupReplyMessage {

}
```


## InviteGroupRequest (Low 349, NotTrusted, Unencoded)

```rust

pub struct InviteGroupRequestMessage {

}
```


## InviteGroupResponse (Low 350, Trusted, Unencoded)

```rust

pub struct InviteGroupResponseMessage {

}
```


## GroupProfileRequest (Low 351, NotTrusted, Unencoded)

```rust

pub struct GroupProfileRequestMessage {

}
```


## GroupProfileReply (Low 352, Trusted, Zerocoded)

```rust

pub struct GroupProfileReplyMessage {

}
```


## GroupAccountSummaryRequest (Low 353, NotTrusted, Zerocoded)

```rust

pub struct GroupAccountSummaryRequestMessage {

}
```


## GroupAccountSummaryReply (Low 354, Trusted, Zerocoded)

```rust

pub struct GroupAccountSummaryReplyMessage {

}
```


## GroupAccountDetailsRequest (Low 355, NotTrusted, Zerocoded)

```rust

pub struct GroupAccountDetailsRequestMessage {

}
```


## GroupAccountDetailsReply (Low 356, Trusted, Zerocoded)

```rust

pub struct GroupAccountDetailsReplyMessage {

}
```


## GroupAccountTransactionsRequest (Low 357, NotTrusted, Zerocoded)

```rust

pub struct GroupAccountTransactionsRequestMessage {

}
```


## GroupAccountTransactionsReply (Low 358, Trusted, Zerocoded)

```rust

pub struct GroupAccountTransactionsReplyMessage {

}
```


## GroupActiveProposalsRequest (Low 359, NotTrusted, Unencoded)

```rust

pub struct GroupActiveProposalsRequestMessage {

}
```


## GroupActiveProposalItemReply (Low 360, Trusted, Zerocoded)

```rust

pub struct GroupActiveProposalItemReplyMessage {

}
```


## GroupVoteHistoryRequest (Low 361, NotTrusted, Unencoded)

```rust

pub struct GroupVoteHistoryRequestMessage {

}
```


## GroupVoteHistoryItemReply (Low 362, Trusted, Zerocoded)

```rust

pub struct GroupVoteHistoryItemReplyMessage {

}
```


## StartGroupProposal (Low 363, NotTrusted, Zerocoded)

```rust

pub struct StartGroupProposalMessage {

}
```


## GroupProposalBallot (Low 364, NotTrusted, Unencoded)

```rust

pub struct GroupProposalBallotMessage {

}
```


## TallyVotes (Low 365, Trusted, Unencoded)

```rust

pub struct TallyVotesMessage {

}
```


## GroupMembersRequest (Low 366, NotTrusted, Unencoded)

```rust

pub struct GroupMembersRequestMessage {

}
```


## GroupMembersReply (Low 367, Trusted, Zerocoded)

```rust

pub struct GroupMembersReplyMessage {

}
```


## ActivateGroup (Low 368, NotTrusted, Zerocoded)

```rust

pub struct ActivateGroupMessage {

}
```


## SetGroupContribution (Low 369, NotTrusted, Unencoded)

```rust

pub struct SetGroupContributionMessage {

}
```


## SetGroupAcceptNotices (Low 370, NotTrusted, Unencoded)

```rust

pub struct SetGroupAcceptNoticesMessage {

}
```


## GroupRoleDataRequest (Low 371, NotTrusted, Unencoded)

```rust

pub struct GroupRoleDataRequestMessage {

}
```


## GroupRoleDataReply (Low 372, Trusted, Unencoded)

```rust

pub struct GroupRoleDataReplyMessage {

}
```


## GroupRoleMembersRequest (Low 373, NotTrusted, Unencoded)

```rust

pub struct GroupRoleMembersRequestMessage {

}
```


## GroupRoleMembersReply (Low 374, Trusted, Unencoded)

```rust

pub struct GroupRoleMembersReplyMessage {

}
```


## GroupTitlesRequest (Low 375, NotTrusted, Unencoded)

```rust

pub struct GroupTitlesRequestMessage {

}
```


## GroupTitlesReply (Low 376, Trusted, Zerocoded)

```rust

pub struct GroupTitlesReplyMessage {

}
```


## GroupTitleUpdate (Low 377, NotTrusted, Unencoded)

```rust

pub struct GroupTitleUpdateMessage {

}
```


## GroupRoleUpdate (Low 378, NotTrusted, Unencoded)

```rust

pub struct GroupRoleUpdateMessage {

}
```


## LiveHelpGroupRequest (Low 379, Trusted, Unencoded)

```rust

pub struct LiveHelpGroupRequestMessage {

}
```


## LiveHelpGroupReply (Low 380, Trusted, Unencoded)

```rust

pub struct LiveHelpGroupReplyMessage {

}
```


## AgentWearablesRequest (Low 381, NotTrusted, Unencoded)

```rust

pub struct AgentWearablesRequestMessage {

}
```


## AgentWearablesUpdate (Low 382, Trusted, Zerocoded)

```rust

pub struct AgentWearablesUpdateMessage {

}
```


## AgentIsNowWearing (Low 383, NotTrusted, Zerocoded)

```rust

pub struct AgentIsNowWearingMessage {

}
```


## AgentCachedTexture (Low 384, NotTrusted, Unencoded)

```rust

pub struct AgentCachedTextureMessage {

}
```


## AgentCachedTextureResponse (Low 385, Trusted, Unencoded)

```rust

pub struct AgentCachedTextureResponseMessage {

}
```


## AgentDataUpdateRequest (Low 386, NotTrusted, Unencoded)

```rust

pub struct AgentDataUpdateRequestMessage {

}
```


## AgentDataUpdate (Low 387, Trusted, Zerocoded)

```rust

pub struct AgentDataUpdateMessage {

}
```


## GroupDataUpdate (Low 388, Trusted, Zerocoded)

```rust

pub struct GroupDataUpdateMessage {

}
```


## AgentGroupDataUpdate (Low 389, Trusted, Zerocoded)

```rust

pub struct AgentGroupDataUpdateMessage {

}
```


## AgentDropGroup (Low 390, Trusted, Zerocoded)

```rust

pub struct AgentDropGroupMessage {

}
```


## LogTextMessage (Low 391, Trusted, Zerocoded)

```rust

pub struct LogTextMessageMessage {

}
```


## ViewerEffect (Medium 17, NotTrusted, Zerocoded)

```rust

pub struct ViewerEffectMessage {

}
```


## CreateTrustedCircuit (Low 392, NotTrusted, Unencoded)

```rust

pub struct CreateTrustedCircuitMessage {

}
```


## DenyTrustedCircuit (Low 393, NotTrusted, Unencoded)

```rust

pub struct DenyTrustedCircuitMessage {

}
```


## RequestTrustedCircuit (Low 394, Trusted, Unencoded)

```rust

pub struct RequestTrustedCircuitMessage {

}
```


## RezSingleAttachmentFromInv (Low 395, NotTrusted, Zerocoded)

```rust

pub struct RezSingleAttachmentFromInvMessage {

}
```


## RezMultipleAttachmentsFromInv (Low 396, NotTrusted, Zerocoded)

```rust

pub struct RezMultipleAttachmentsFromInvMessage {

}
```


## DetachAttachmentIntoInv (Low 397, NotTrusted, Unencoded)

```rust

pub struct DetachAttachmentIntoInvMessage {

}
```


## CreateNewOutfitAttachments (Low 398, NotTrusted, Unencoded)

```rust

pub struct CreateNewOutfitAttachmentsMessage {

}
```


## UserInfoRequest (Low 399, NotTrusted, Unencoded)

```rust

pub struct UserInfoRequestMessage {

}
```


## UserInfoReply (Low 400, NotTrusted, Unencoded)

```rust

pub struct UserInfoReplyMessage {

}
```


## UpdateUserInfo (Low 401, NotTrusted, Unencoded)

```rust

pub struct UpdateUserInfoMessage {

}
```


## ParcelRename (Low 402, Trusted, Unencoded)

```rust

pub struct ParcelRenameMessage {

}
```


## InitiateDownload (Low 403, NotTrusted, Unencoded)

```rust

pub struct InitiateDownloadMessage {

}
```


## SystemMessage (Low 404, Trusted, Zerocoded)

```rust

pub struct SystemMessageMessage {

}
```


## MapLayerRequest (Low 405, NotTrusted, Unencoded)

```rust

pub struct MapLayerRequestMessage {

}
```


## MapLayerReply (Low 406, Trusted, Unencoded)

```rust

pub struct MapLayerReplyMessage {

}
```


## MapBlockRequest (Low 407, NotTrusted, Unencoded)

```rust

pub struct MapBlockRequestMessage {

}
```


## MapNameRequest (Low 408, NotTrusted, Unencoded)

```rust

pub struct MapNameRequestMessage {

}
```


## MapBlockReply (Low 409, Trusted, Unencoded)

```rust

pub struct MapBlockReplyMessage {

}
```


## MapItemRequest (Low 410, NotTrusted, Unencoded)

```rust

pub struct MapItemRequestMessage {

}
```


## MapItemReply (Low 411, Trusted, Unencoded)

```rust

pub struct MapItemReplyMessage {

}
```


## SendPostcard (Low 412, NotTrusted, Unencoded)

```rust

pub struct SendPostcardMessage {

}
```


## RpcChannelRequest (Low 413, Trusted, Unencoded)

```rust

pub struct RpcChannelRequestMessage {

}
```


## RpcChannelReply (Low 414, Trusted, Unencoded)

```rust

pub struct RpcChannelReplyMessage {

}
```


## RpcScriptRequestInbound (Low 415, NotTrusted, Unencoded)

```rust

pub struct RpcScriptRequestInboundMessage {

}
```


## RpcScriptRequestInboundForward (Low 416, Trusted, Unencoded)

```rust

pub struct RpcScriptRequestInboundForwardMessage {

}
```


## RpcScriptReplyInbound (Low 417, NotTrusted, Unencoded)

```rust

pub struct RpcScriptReplyInboundMessage {

}
```


## ScriptMailRegistration (Low 418, Trusted, Unencoded)

```rust

pub struct ScriptMailRegistrationMessage {

}
```


## ParcelMediaCommandMessage (Low 419, Trusted, Unencoded)

```rust

pub struct ParcelMediaCommandMessageMessage {

}
```


## ParcelMediaUpdate (Low 420, Trusted, Unencoded)

```rust

pub struct ParcelMediaUpdateMessage {

}
```


## LandStatRequest (Low 421, NotTrusted, Unencoded)

```rust

pub struct LandStatRequestMessage {

}
```


## LandStatReply (Low 422, Trusted, Unencoded)

```rust

pub struct LandStatReplyMessage {

}
```


## Error (Low 423, NotTrusted, Zerocoded)

```rust

pub struct ErrorMessage {

}
```


## ObjectIncludeInSearch (Low 424, NotTrusted, Unencoded)

```rust

pub struct ObjectIncludeInSearchMessage {

}
```


## RezRestoreToWorld (Low 425, NotTrusted, Unencoded)

```rust

pub struct RezRestoreToWorldMessage {

}
```


## LinkInventoryItem (Low 426, NotTrusted, Zerocoded)

```rust

pub struct LinkInventoryItemMessage {

}
```


## RetrieveIMsExtended (Low 427, Trusted, Unencoded)

```rust

pub struct RetrieveIMsExtendedMessage {

}
```


## JoinGroupRequestExtended (Low 428, Trusted, Unencoded)

```rust

pub struct JoinGroupRequestExtendedMessage {

}
```


## CreateGroupRequestExtended (Low 429, Trusted, Unencoded)

```rust

pub struct CreateGroupRequestExtendedMessage {

}
```


## GameControlInput (High 32, NotTrusted, Zerocoded)

```rust

pub struct GameControlInputMessage {

}
```
