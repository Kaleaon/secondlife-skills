# TypeScript Message Stubs (generated from secondlife/master-message-template)

One stub per UDP message (483 messages) in TypeScript, generated from message_template.msg field definitions. These are starting points for a codec: implement ToBytes/FromBytes following the field order exactly, honour the zerocoded flag, and verify against LibreMetaverse.Protocol and the viewer template copy before shipping.


## TestMessage (Low 1, NotTrusted, Zerocoded)

```ts

export interface TestMessageMessage {

}
```


## PacketAck (Fixed 0xFFFFFFFB, NotTrusted, Unencoded)

```ts

export interface PacketAckMessage {

}
```


## OpenCircuit (Fixed 0xFFFFFFFC, NotTrusted, Unencoded)

```ts

export interface OpenCircuitMessage {

}
```


## CloseCircuit (Fixed 0xFFFFFFFD, NotTrusted, Unencoded)

```ts

export interface CloseCircuitMessage {

}
```


## StartPingCheck (High 1, NotTrusted, Unencoded)

```ts

export interface StartPingCheckMessage {

}
```


## CompletePingCheck (High 2, NotTrusted, Unencoded)

```ts

export interface CompletePingCheckMessage {

}
```


## AddCircuitCode (Low 2, Trusted, Unencoded)

```ts

export interface AddCircuitCodeMessage {

}
```


## UseCircuitCode (Low 3, NotTrusted, Unencoded)

```ts

export interface UseCircuitCodeMessage {

}
```


## NeighborList (High 3, Trusted, Unencoded)

```ts

export interface NeighborListMessage {

}
```


## AvatarTextureUpdate (Low 4, Trusted, Zerocoded)

```ts

export interface AvatarTextureUpdateMessage {

}
```


## SimulatorMapUpdate (Low 5, Trusted, Unencoded)

```ts

export interface SimulatorMapUpdateMessage {

}
```


## SimulatorSetMap (Low 6, Trusted, Unencoded)

```ts

export interface SimulatorSetMapMessage {

}
```


## SubscribeLoad (Low 7, Trusted, Unencoded)

```ts

export interface SubscribeLoadMessage {

}
```


## UnsubscribeLoad (Low 8, Trusted, Unencoded)

```ts

export interface UnsubscribeLoadMessage {

}
```


## SimulatorReady (Low 9, Trusted, Zerocoded)

```ts

export interface SimulatorReadyMessage {

}
```


## TelehubInfo (Low 10, Trusted, Unencoded)

```ts

export interface TelehubInfoMessage {

}
```


## SimulatorPresentAtLocation (Low 11, Trusted, Unencoded)

```ts

export interface SimulatorPresentAtLocationMessage {

}
```


## SimulatorLoad (Low 12, Trusted, Unencoded)

```ts

export interface SimulatorLoadMessage {

}
```


## SimulatorShutdownRequest (Low 13, Trusted, Unencoded)

```ts

export interface SimulatorShutdownRequestMessage {

}
```


## RegionPresenceRequestByRegionID (Low 14, Trusted, Unencoded)

```ts

export interface RegionPresenceRequestByRegionIDMessage {

}
```


## RegionPresenceRequestByHandle (Low 15, Trusted, Unencoded)

```ts

export interface RegionPresenceRequestByHandleMessage {

}
```


## RegionPresenceResponse (Low 16, Trusted, Zerocoded)

```ts

export interface RegionPresenceResponseMessage {

}
```


## UpdateSimulator (Low 17, Trusted, Unencoded)

```ts

export interface UpdateSimulatorMessage {

}
```


## LogDwellTime (Low 18, Trusted, Unencoded)

```ts

export interface LogDwellTimeMessage {

}
```


## FeatureDisabled (Low 19, Trusted, Unencoded)

```ts

export interface FeatureDisabledMessage {

}
```


## LogFailedMoneyTransaction (Low 20, Trusted, Unencoded)

```ts

export interface LogFailedMoneyTransactionMessage {

}
```


## UserReportInternal (Low 21, Trusted, Zerocoded)

```ts

export interface UserReportInternalMessage {

}
```


## SetSimStatusInDatabase (Low 22, Trusted, Unencoded)

```ts

export interface SetSimStatusInDatabaseMessage {

}
```


## SetSimPresenceInDatabase (Low 23, Trusted, Unencoded)

```ts

export interface SetSimPresenceInDatabaseMessage {

}
```


## EconomyDataRequest (Low 24, NotTrusted, Unencoded)

```ts

export interface EconomyDataRequestMessage {

}
```


## EconomyData (Low 25, Trusted, Zerocoded)

```ts

export interface EconomyDataMessage {

}
```


## AvatarPickerRequest (Low 26, NotTrusted, Unencoded)

```ts

export interface AvatarPickerRequestMessage {

}
```


## AvatarPickerRequestBackend (Low 27, Trusted, Unencoded)

```ts

export interface AvatarPickerRequestBackendMessage {

}
```


## AvatarPickerReply (Low 28, Trusted, Unencoded)

```ts

export interface AvatarPickerReplyMessage {

}
```


## PlacesQuery (Low 29, NotTrusted, Zerocoded)

```ts

export interface PlacesQueryMessage {

}
```


## PlacesReply (Low 30, Trusted, Zerocoded)

```ts

export interface PlacesReplyMessage {

}
```


## DirFindQuery (Low 31, NotTrusted, Zerocoded)

```ts

export interface DirFindQueryMessage {

}
```


## DirFindQueryBackend (Low 32, Trusted, Zerocoded)

```ts

export interface DirFindQueryBackendMessage {

}
```


## DirPlacesQuery (Low 33, NotTrusted, Zerocoded)

```ts

export interface DirPlacesQueryMessage {

}
```


## DirPlacesQueryBackend (Low 34, Trusted, Zerocoded)

```ts

export interface DirPlacesQueryBackendMessage {

}
```


## DirPlacesReply (Low 35, Trusted, Zerocoded)

```ts

export interface DirPlacesReplyMessage {

}
```


## DirPeopleReply (Low 36, Trusted, Zerocoded)

```ts

export interface DirPeopleReplyMessage {

}
```


## DirEventsReply (Low 37, Trusted, Zerocoded)

```ts

export interface DirEventsReplyMessage {

}
```


## DirGroupsReply (Low 38, Trusted, Zerocoded)

```ts

export interface DirGroupsReplyMessage {

}
```


## DirClassifiedQuery (Low 39, NotTrusted, Zerocoded)

```ts

export interface DirClassifiedQueryMessage {

}
```


## DirClassifiedQueryBackend (Low 40, Trusted, Zerocoded)

```ts

export interface DirClassifiedQueryBackendMessage {

}
```


## DirClassifiedReply (Low 41, Trusted, Zerocoded)

```ts

export interface DirClassifiedReplyMessage {

}
```


## AvatarClassifiedReply (Low 42, Trusted, Unencoded)

```ts

export interface AvatarClassifiedReplyMessage {

}
```


## ClassifiedInfoRequest (Low 43, NotTrusted, Zerocoded)

```ts

export interface ClassifiedInfoRequestMessage {

}
```


## ClassifiedInfoReply (Low 44, Trusted, Unencoded)

```ts

export interface ClassifiedInfoReplyMessage {

}
```


## ClassifiedInfoUpdate (Low 45, NotTrusted, Unencoded)

```ts

export interface ClassifiedInfoUpdateMessage {

}
```


## ClassifiedDelete (Low 46, NotTrusted, Unencoded)

```ts

export interface ClassifiedDeleteMessage {

}
```


## ClassifiedGodDelete (Low 47, NotTrusted, Unencoded)

```ts

export interface ClassifiedGodDeleteMessage {

}
```


## DirLandQuery (Low 48, NotTrusted, Zerocoded)

```ts

export interface DirLandQueryMessage {

}
```


## DirLandQueryBackend (Low 49, Trusted, Zerocoded)

```ts

export interface DirLandQueryBackendMessage {

}
```


## DirLandReply (Low 50, Trusted, Zerocoded)

```ts

export interface DirLandReplyMessage {

}
```


## DirPopularQuery (Low 51, NotTrusted, Zerocoded)

```ts

export interface DirPopularQueryMessage {

}
```


## DirPopularQueryBackend (Low 52, Trusted, Zerocoded)

```ts

export interface DirPopularQueryBackendMessage {

}
```


## DirPopularReply (Low 53, Trusted, Zerocoded)

```ts

export interface DirPopularReplyMessage {

}
```


## ParcelInfoRequest (Low 54, NotTrusted, Unencoded)

```ts

export interface ParcelInfoRequestMessage {

}
```


## ParcelInfoReply (Low 55, Trusted, Zerocoded)

```ts

export interface ParcelInfoReplyMessage {

}
```


## ParcelObjectOwnersRequest (Low 56, NotTrusted, Unencoded)

```ts

export interface ParcelObjectOwnersRequestMessage {

}
```


## ParcelObjectOwnersReply (Low 57, Trusted, Zerocoded)

```ts

export interface ParcelObjectOwnersReplyMessage {

}
```


## GroupNoticesListRequest (Low 58, NotTrusted, Unencoded)

```ts

export interface GroupNoticesListRequestMessage {

}
```


## GroupNoticesListReply (Low 59, Trusted, Unencoded)

```ts

export interface GroupNoticesListReplyMessage {

}
```


## GroupNoticeRequest (Low 60, NotTrusted, Unencoded)

```ts

export interface GroupNoticeRequestMessage {

}
```


## GroupNoticeAdd (Low 61, Trusted, Unencoded)

```ts

export interface GroupNoticeAddMessage {

}
```


## TeleportRequest (Low 62, NotTrusted, Unencoded)

```ts

export interface TeleportRequestMessage {

}
```


## TeleportLocationRequest (Low 63, NotTrusted, Unencoded)

```ts

export interface TeleportLocationRequestMessage {

}
```


## TeleportLocal (Low 64, Trusted, Unencoded)

```ts

export interface TeleportLocalMessage {

}
```


## TeleportLandmarkRequest (Low 65, NotTrusted, Zerocoded)

```ts

export interface TeleportLandmarkRequestMessage {

}
```


## TeleportProgress (Low 66, Trusted, Unencoded)

```ts

export interface TeleportProgressMessage {

}
```


## DataHomeLocationRequest (Low 67, Trusted, Zerocoded)

```ts

export interface DataHomeLocationRequestMessage {

}
```


## DataHomeLocationReply (Low 68, Trusted, Unencoded)

```ts

export interface DataHomeLocationReplyMessage {

}
```


## TeleportFinish (Low 69, Trusted, Unencoded)

```ts

export interface TeleportFinishMessage {

}
```


## StartLure (Low 70, NotTrusted, Unencoded)

```ts

export interface StartLureMessage {

}
```


## TeleportLureRequest (Low 71, NotTrusted, Unencoded)

```ts

export interface TeleportLureRequestMessage {

}
```


## TeleportCancel (Low 72, NotTrusted, Unencoded)

```ts

export interface TeleportCancelMessage {

}
```


## TeleportStart (Low 73, Trusted, Unencoded)

```ts

export interface TeleportStartMessage {

}
```


## TeleportFailed (Low 74, Trusted, Unencoded)

```ts

export interface TeleportFailedMessage {

}
```


## Undo (Low 75, NotTrusted, Unencoded)

```ts

export interface UndoMessage {

}
```


## Redo (Low 76, NotTrusted, Unencoded)

```ts

export interface RedoMessage {

}
```


## UndoLand (Low 77, NotTrusted, Unencoded)

```ts

export interface UndoLandMessage {

}
```


## AgentPause (Low 78, NotTrusted, Unencoded)

```ts

export interface AgentPauseMessage {

}
```


## AgentResume (Low 79, NotTrusted, Unencoded)

```ts

export interface AgentResumeMessage {

}
```


## AgentUpdate (High 4, NotTrusted, Zerocoded)

```ts

export interface AgentUpdateMessage {

}
```


## ChatFromViewer (Low 80, NotTrusted, Zerocoded)

```ts

export interface ChatFromViewerMessage {

}
```


## AgentThrottle (Low 81, NotTrusted, Zerocoded)

```ts

export interface AgentThrottleMessage {

}
```


## AgentFOV (Low 82, NotTrusted, Unencoded)

```ts

export interface AgentFOVMessage {

}
```


## AgentHeightWidth (Low 83, NotTrusted, Unencoded)

```ts

export interface AgentHeightWidthMessage {

}
```


## AgentSetAppearance (Low 84, NotTrusted, Zerocoded)

```ts

export interface AgentSetAppearanceMessage {

}
```


## AgentAnimation (High 5, NotTrusted, Unencoded)

```ts

export interface AgentAnimationMessage {

}
```


## AgentRequestSit (High 6, NotTrusted, Zerocoded)

```ts

export interface AgentRequestSitMessage {

}
```


## AgentSit (High 7, NotTrusted, Unencoded)

```ts

export interface AgentSitMessage {

}
```


## AgentQuitCopy (Low 85, NotTrusted, Unencoded)

```ts

export interface AgentQuitCopyMessage {

}
```


## RequestImage (High 8, NotTrusted, Unencoded)

```ts

export interface RequestImageMessage {

}
```


## ImageNotInDatabase (Low 86, Trusted, Unencoded)

```ts

export interface ImageNotInDatabaseMessage {

}
```


## RebakeAvatarTextures (Low 87, Trusted, Unencoded)

```ts

export interface RebakeAvatarTexturesMessage {

}
```


## SetAlwaysRun (Low 88, NotTrusted, Unencoded)

```ts

export interface SetAlwaysRunMessage {

}
```


## ObjectAdd (Medium 1, NotTrusted, Zerocoded)

```ts

export interface ObjectAddMessage {

}
```


## ObjectDelete (Low 89, NotTrusted, Zerocoded)

```ts

export interface ObjectDeleteMessage {

}
```


## ObjectDuplicate (Low 90, NotTrusted, Zerocoded)

```ts

export interface ObjectDuplicateMessage {

}
```


## ObjectDuplicateOnRay (Low 91, NotTrusted, Zerocoded)

```ts

export interface ObjectDuplicateOnRayMessage {

}
```


## MultipleObjectUpdate (Medium 2, NotTrusted, Zerocoded)

```ts

export interface MultipleObjectUpdateMessage {

}
```


## RequestMultipleObjects (Medium 3, NotTrusted, Zerocoded)

```ts

export interface RequestMultipleObjectsMessage {

}
```


## ObjectPosition (Medium 4, NotTrusted, Zerocoded)

```ts

export interface ObjectPositionMessage {

}
```


## ObjectScale (Low 92, NotTrusted, Zerocoded)

```ts

export interface ObjectScaleMessage {

}
```


## ObjectRotation (Low 93, NotTrusted, Zerocoded)

```ts

export interface ObjectRotationMessage {

}
```


## ObjectFlagUpdate (Low 94, NotTrusted, Zerocoded)

```ts

export interface ObjectFlagUpdateMessage {

}
```


## ObjectClickAction (Low 95, NotTrusted, Zerocoded)

```ts

export interface ObjectClickActionMessage {

}
```


## ObjectImage (Low 96, NotTrusted, Zerocoded)

```ts

export interface ObjectImageMessage {

}
```


## ObjectBypassModUpdate (Low 431, NotTrusted, Zerocoded)

```ts

export interface ObjectBypassModUpdateMessage {

}
```


## ObjectMaterial (Low 97, NotTrusted, Zerocoded)

```ts

export interface ObjectMaterialMessage {

}
```


## ObjectShape (Low 98, NotTrusted, Zerocoded)

```ts

export interface ObjectShapeMessage {

}
```


## ObjectExtraParams (Low 99, NotTrusted, Zerocoded)

```ts

export interface ObjectExtraParamsMessage {

}
```


## ObjectOwner (Low 100, NotTrusted, Zerocoded)

```ts

export interface ObjectOwnerMessage {

}
```


## ObjectGroup (Low 101, NotTrusted, Zerocoded)

```ts

export interface ObjectGroupMessage {

}
```


## ObjectBuy (Low 102, NotTrusted, Zerocoded)

```ts

export interface ObjectBuyMessage {

}
```


## BuyObjectInventory (Low 103, NotTrusted, Zerocoded)

```ts

export interface BuyObjectInventoryMessage {

}
```


## DerezContainer (Low 104, Trusted, Zerocoded)

```ts

export interface DerezContainerMessage {

}
```


## ObjectPermissions (Low 105, NotTrusted, Zerocoded)

```ts

export interface ObjectPermissionsMessage {

}
```


## ObjectSaleInfo (Low 106, NotTrusted, Zerocoded)

```ts

export interface ObjectSaleInfoMessage {

}
```


## ObjectName (Low 107, NotTrusted, Zerocoded)

```ts

export interface ObjectNameMessage {

}
```


## ObjectDescription (Low 108, NotTrusted, Zerocoded)

```ts

export interface ObjectDescriptionMessage {

}
```


## ObjectCategory (Low 109, NotTrusted, Zerocoded)

```ts

export interface ObjectCategoryMessage {

}
```


## ObjectSelect (Low 110, NotTrusted, Zerocoded)

```ts

export interface ObjectSelectMessage {

}
```


## ObjectDeselect (Low 111, NotTrusted, Zerocoded)

```ts

export interface ObjectDeselectMessage {

}
```


## ObjectAttach (Low 112, NotTrusted, Zerocoded)

```ts

export interface ObjectAttachMessage {

}
```


## ObjectDetach (Low 113, NotTrusted, Unencoded)

```ts

export interface ObjectDetachMessage {

}
```


## ObjectDrop (Low 114, NotTrusted, Unencoded)

```ts

export interface ObjectDropMessage {

}
```


## ObjectLink (Low 115, NotTrusted, Unencoded)

```ts

export interface ObjectLinkMessage {

}
```


## ObjectDelink (Low 116, NotTrusted, Unencoded)

```ts

export interface ObjectDelinkMessage {

}
```


## ObjectGrab (Low 117, NotTrusted, Zerocoded)

```ts

export interface ObjectGrabMessage {

}
```


## ObjectGrabUpdate (Low 118, NotTrusted, Zerocoded)

```ts

export interface ObjectGrabUpdateMessage {

}
```


## ObjectDeGrab (Low 119, NotTrusted, Unencoded)

```ts

export interface ObjectDeGrabMessage {

}
```


## ObjectSpinStart (Low 120, NotTrusted, Zerocoded)

```ts

export interface ObjectSpinStartMessage {

}
```


## ObjectSpinUpdate (Low 121, NotTrusted, Zerocoded)

```ts

export interface ObjectSpinUpdateMessage {

}
```


## ObjectSpinStop (Low 122, NotTrusted, Zerocoded)

```ts

export interface ObjectSpinStopMessage {

}
```


## ObjectExportSelected (Low 123, NotTrusted, Zerocoded)

```ts

export interface ObjectExportSelectedMessage {

}
```


## ModifyLand (Low 124, NotTrusted, Zerocoded)

```ts

export interface ModifyLandMessage {

}
```


## VelocityInterpolateOn (Low 125, NotTrusted, Unencoded)

```ts

export interface VelocityInterpolateOnMessage {

}
```


## VelocityInterpolateOff (Low 126, NotTrusted, Unencoded)

```ts

export interface VelocityInterpolateOffMessage {

}
```


## StateSave (Low 127, NotTrusted, Unencoded)

```ts

export interface StateSaveMessage {

}
```


## ReportAutosaveCrash (Low 128, NotTrusted, Unencoded)

```ts

export interface ReportAutosaveCrashMessage {

}
```


## SimWideDeletes (Low 129, NotTrusted, Unencoded)

```ts

export interface SimWideDeletesMessage {

}
```


## RequestObjectPropertiesFamily (Medium 5, NotTrusted, Zerocoded)

```ts

export interface RequestObjectPropertiesFamilyMessage {

}
```


## TrackAgent (Low 130, NotTrusted, Unencoded)

```ts

export interface TrackAgentMessage {

}
```


## ViewerStats (Low 131, NotTrusted, Zerocoded)

```ts

export interface ViewerStatsMessage {

}
```


## ScriptAnswerYes (Low 132, NotTrusted, Unencoded)

```ts

export interface ScriptAnswerYesMessage {

}
```


## UserReport (Low 133, NotTrusted, Zerocoded)

```ts

export interface UserReportMessage {

}
```


## AlertMessage (Low 134, Trusted, Unencoded)

```ts

export interface AlertMessageMessage {

}
```


## AgentAlertMessage (Low 135, Trusted, Unencoded)

```ts

export interface AgentAlertMessageMessage {

}
```


## MeanCollisionAlert (Low 136, Trusted, Zerocoded)

```ts

export interface MeanCollisionAlertMessage {

}
```


## ViewerFrozenMessage (Low 137, Trusted, Unencoded)

```ts

export interface ViewerFrozenMessageMessage {

}
```


## HealthMessage (Low 138, Trusted, Zerocoded)

```ts

export interface HealthMessageMessage {

}
```


## ChatFromSimulator (Low 139, Trusted, Unencoded)

```ts

export interface ChatFromSimulatorMessage {

}
```


## SimStats (Low 140, Trusted, Unencoded)

```ts

export interface SimStatsMessage {

}
```


## RequestRegionInfo (Low 141, NotTrusted, Unencoded)

```ts

export interface RequestRegionInfoMessage {

}
```


## RegionInfo (Low 142, NotTrusted, Zerocoded)

```ts

export interface RegionInfoMessage {

}
```


## GodUpdateRegionInfo (Low 143, NotTrusted, Zerocoded)

```ts

export interface GodUpdateRegionInfoMessage {

}
```


## NearestLandingRegionRequest (Low 144, Trusted, Unencoded)

```ts

export interface NearestLandingRegionRequestMessage {

}
```


## NearestLandingRegionReply (Low 145, Trusted, Unencoded)

```ts

export interface NearestLandingRegionReplyMessage {

}
```


## NearestLandingRegionUpdated (Low 146, Trusted, Unencoded)

```ts

export interface NearestLandingRegionUpdatedMessage {

}
```


## TeleportLandingStatusChanged (Low 147, Trusted, Unencoded)

```ts

export interface TeleportLandingStatusChangedMessage {

}
```


## RegionHandshake (Low 148, Trusted, Zerocoded)

```ts

export interface RegionHandshakeMessage {

}
```


## RegionHandshakeReply (Low 149, NotTrusted, Zerocoded)

```ts

export interface RegionHandshakeReplyMessage {

}
```


## CoarseLocationUpdate (Medium 6, Trusted, Unencoded)

```ts

export interface CoarseLocationUpdateMessage {

}
```


## ImageData (High 9, Trusted, Unencoded)

```ts

export interface ImageDataMessage {

}
```


## ImagePacket (High 10, Trusted, Unencoded)

```ts

export interface ImagePacketMessage {

}
```


## LayerData (High 11, Trusted, Unencoded)

```ts

export interface LayerDataMessage {

}
```


## ObjectUpdate (High 12, Trusted, Zerocoded)

```ts

export interface ObjectUpdateMessage {

}
```


## ObjectUpdateCompressed (High 13, Trusted, Unencoded)

```ts

export interface ObjectUpdateCompressedMessage {

}
```


## ObjectUpdateCached (High 14, Trusted, Unencoded)

```ts

export interface ObjectUpdateCachedMessage {

}
```


## ImprovedTerseObjectUpdate (High 15, Trusted, Unencoded)

```ts

export interface ImprovedTerseObjectUpdateMessage {

}
```


## KillObject (High 16, Trusted, Unencoded)

```ts

export interface KillObjectMessage {

}
```


## CrossedRegion (Medium 7, Trusted, Unencoded)

```ts

export interface CrossedRegionMessage {

}
```


## SimulatorViewerTimeMessage (Low 150, Trusted, Unencoded)

```ts

export interface SimulatorViewerTimeMessageMessage {

}
```


## EnableSimulator (Low 151, Trusted, Unencoded)

```ts

export interface EnableSimulatorMessage {

}
```


## DisableSimulator (Low 152, Trusted, Unencoded)

```ts

export interface DisableSimulatorMessage {

}
```


## ConfirmEnableSimulator (Medium 8, Trusted, Unencoded)

```ts

export interface ConfirmEnableSimulatorMessage {

}
```


## TransferRequest (Low 153, NotTrusted, Zerocoded)

```ts

export interface TransferRequestMessage {

}
```


## TransferInfo (Low 154, NotTrusted, Zerocoded)

```ts

export interface TransferInfoMessage {

}
```


## TransferPacket (High 17, NotTrusted, Unencoded)

```ts

export interface TransferPacketMessage {

}
```


## TransferAbort (Low 155, NotTrusted, Zerocoded)

```ts

export interface TransferAbortMessage {

}
```


## RequestXfer (Low 156, NotTrusted, Zerocoded)

```ts

export interface RequestXferMessage {

}
```


## SendXferPacket (High 18, NotTrusted, Unencoded)

```ts

export interface SendXferPacketMessage {

}
```


## ConfirmXferPacket (High 19, NotTrusted, Unencoded)

```ts

export interface ConfirmXferPacketMessage {

}
```


## AbortXfer (Low 157, NotTrusted, Unencoded)

```ts

export interface AbortXferMessage {

}
```


## AvatarAnimation (High 20, Trusted, Unencoded)

```ts

export interface AvatarAnimationMessage {

}
```


## AvatarAppearance (Low 158, Trusted, Zerocoded)

```ts

export interface AvatarAppearanceMessage {

}
```


## AvatarSitResponse (High 21, Trusted, Zerocoded)

```ts

export interface AvatarSitResponseMessage {

}
```


## SetFollowCamProperties (Low 159, Trusted, Unencoded)

```ts

export interface SetFollowCamPropertiesMessage {

}
```


## ClearFollowCamProperties (Low 160, Trusted, Unencoded)

```ts

export interface ClearFollowCamPropertiesMessage {

}
```


## CameraConstraint (High 22, Trusted, Zerocoded)

```ts

export interface CameraConstraintMessage {

}
```


## ObjectProperties (Medium 9, Trusted, Zerocoded)

```ts

export interface ObjectPropertiesMessage {

}
```


## ObjectPropertiesFamily (Medium 10, Trusted, Zerocoded)

```ts

export interface ObjectPropertiesFamilyMessage {

}
```


## RequestPayPrice (Low 161, NotTrusted, Unencoded)

```ts

export interface RequestPayPriceMessage {

}
```


## PayPriceReply (Low 162, Trusted, Unencoded)

```ts

export interface PayPriceReplyMessage {

}
```


## KickUser (Low 163, Trusted, Unencoded)

```ts

export interface KickUserMessage {

}
```


## KickUserAck (Low 164, Trusted, Unencoded)

```ts

export interface KickUserAckMessage {

}
```


## GodKickUser (Low 165, NotTrusted, Unencoded)

```ts

export interface GodKickUserMessage {

}
```


## SystemKickUser (Low 166, Trusted, Unencoded)

```ts

export interface SystemKickUserMessage {

}
```


## EjectUser (Low 167, NotTrusted, Unencoded)

```ts

export interface EjectUserMessage {

}
```


## FreezeUser (Low 168, NotTrusted, Unencoded)

```ts

export interface FreezeUserMessage {

}
```


## AvatarPropertiesRequest (Low 169, NotTrusted, Unencoded)

```ts

export interface AvatarPropertiesRequestMessage {

}
```


## AvatarPropertiesRequestBackend (Low 170, Trusted, Unencoded)

```ts

export interface AvatarPropertiesRequestBackendMessage {

}
```


## AvatarPropertiesReply (Low 171, Trusted, Zerocoded)

```ts

export interface AvatarPropertiesReplyMessage {

}
```


## AvatarInterestsReply (Low 172, Trusted, Zerocoded)

```ts

export interface AvatarInterestsReplyMessage {

}
```


## AvatarGroupsReply (Low 173, Trusted, Zerocoded)

```ts

export interface AvatarGroupsReplyMessage {

}
```


## AvatarPropertiesUpdate (Low 174, NotTrusted, Zerocoded)

```ts

export interface AvatarPropertiesUpdateMessage {

}
```


## AvatarInterestsUpdate (Low 175, NotTrusted, Zerocoded)

```ts

export interface AvatarInterestsUpdateMessage {

}
```


## AvatarNotesReply (Low 176, Trusted, Unencoded)

```ts

export interface AvatarNotesReplyMessage {

}
```


## AvatarNotesUpdate (Low 177, NotTrusted, Unencoded)

```ts

export interface AvatarNotesUpdateMessage {

}
```


## AvatarPicksReply (Low 178, Trusted, Unencoded)

```ts

export interface AvatarPicksReplyMessage {

}
```


## EventInfoRequest (Low 179, NotTrusted, Unencoded)

```ts

export interface EventInfoRequestMessage {

}
```


## EventInfoReply (Low 180, Trusted, Unencoded)

```ts

export interface EventInfoReplyMessage {

}
```


## EventNotificationAddRequest (Low 181, NotTrusted, Unencoded)

```ts

export interface EventNotificationAddRequestMessage {

}
```


## EventNotificationRemoveRequest (Low 182, NotTrusted, Unencoded)

```ts

export interface EventNotificationRemoveRequestMessage {

}
```


## EventGodDelete (Low 183, NotTrusted, Unencoded)

```ts

export interface EventGodDeleteMessage {

}
```


## PickInfoReply (Low 184, Trusted, Unencoded)

```ts

export interface PickInfoReplyMessage {

}
```


## PickInfoUpdate (Low 185, NotTrusted, Unencoded)

```ts

export interface PickInfoUpdateMessage {

}
```


## PickDelete (Low 186, NotTrusted, Unencoded)

```ts

export interface PickDeleteMessage {

}
```


## PickGodDelete (Low 187, NotTrusted, Unencoded)

```ts

export interface PickGodDeleteMessage {

}
```


## ScriptQuestion (Low 188, Trusted, Unencoded)

```ts

export interface ScriptQuestionMessage {

}
```


## ScriptControlChange (Low 189, Trusted, Unencoded)

```ts

export interface ScriptControlChangeMessage {

}
```


## ScriptDialog (Low 190, Trusted, Zerocoded)

```ts

export interface ScriptDialogMessage {

}
```


## ScriptDialogReply (Low 191, NotTrusted, Zerocoded)

```ts

export interface ScriptDialogReplyMessage {

}
```


## ForceScriptControlRelease (Low 192, NotTrusted, Unencoded)

```ts

export interface ForceScriptControlReleaseMessage {

}
```


## RevokePermissions (Low 193, NotTrusted, Unencoded)

```ts

export interface RevokePermissionsMessage {

}
```


## LoadURL (Low 194, Trusted, Unencoded)

```ts

export interface LoadURLMessage {

}
```


## ScriptTeleportRequest (Low 195, Trusted, Unencoded)

```ts

export interface ScriptTeleportRequestMessage {

}
```


## ParcelOverlay (Low 196, Trusted, Zerocoded)

```ts

export interface ParcelOverlayMessage {

}
```


## ParcelPropertiesRequest (Medium 11, NotTrusted, Zerocoded)

```ts

export interface ParcelPropertiesRequestMessage {

}
```


## ParcelPropertiesRequestByID (Low 197, NotTrusted, Zerocoded)

```ts

export interface ParcelPropertiesRequestByIDMessage {

}
```


## ParcelProperties (High 23, Trusted, Zerocoded)

```ts

export interface ParcelPropertiesMessage {

}
```


## ParcelPropertiesUpdate (Low 198, NotTrusted, Zerocoded)

```ts

export interface ParcelPropertiesUpdateMessage {

}
```


## ParcelReturnObjects (Low 199, NotTrusted, Zerocoded)

```ts

export interface ParcelReturnObjectsMessage {

}
```


## ParcelSetOtherCleanTime (Low 200, NotTrusted, Zerocoded)

```ts

export interface ParcelSetOtherCleanTimeMessage {

}
```


## ParcelDisableObjects (Low 201, NotTrusted, Zerocoded)

```ts

export interface ParcelDisableObjectsMessage {

}
```


## ParcelSelectObjects (Low 202, NotTrusted, Zerocoded)

```ts

export interface ParcelSelectObjectsMessage {

}
```


## EstateCovenantRequest (Low 203, NotTrusted, Unencoded)

```ts

export interface EstateCovenantRequestMessage {

}
```


## EstateCovenantReply (Low 204, Trusted, Unencoded)

```ts

export interface EstateCovenantReplyMessage {

}
```


## ForceObjectSelect (Low 205, Trusted, Unencoded)

```ts

export interface ForceObjectSelectMessage {

}
```


## ParcelBuyPass (Low 206, NotTrusted, Unencoded)

```ts

export interface ParcelBuyPassMessage {

}
```


## ParcelDeedToGroup (Low 207, NotTrusted, Unencoded)

```ts

export interface ParcelDeedToGroupMessage {

}
```


## ParcelReclaim (Low 208, NotTrusted, Unencoded)

```ts

export interface ParcelReclaimMessage {

}
```


## ParcelClaim (Low 209, NotTrusted, Zerocoded)

```ts

export interface ParcelClaimMessage {

}
```


## ParcelJoin (Low 210, NotTrusted, Unencoded)

```ts

export interface ParcelJoinMessage {

}
```


## ParcelDivide (Low 211, NotTrusted, Unencoded)

```ts

export interface ParcelDivideMessage {

}
```


## ParcelRelease (Low 212, NotTrusted, Unencoded)

```ts

export interface ParcelReleaseMessage {

}
```


## ParcelBuy (Low 213, NotTrusted, Zerocoded)

```ts

export interface ParcelBuyMessage {

}
```


## ParcelGodForceOwner (Low 214, NotTrusted, Zerocoded)

```ts

export interface ParcelGodForceOwnerMessage {

}
```


## ParcelAccessListRequest (Low 215, NotTrusted, Zerocoded)

```ts

export interface ParcelAccessListRequestMessage {

}
```


## ParcelAccessListReply (Low 216, Trusted, Zerocoded)

```ts

export interface ParcelAccessListReplyMessage {

}
```


## ParcelAccessListUpdate (Low 217, NotTrusted, Zerocoded)

```ts

export interface ParcelAccessListUpdateMessage {

}
```


## ParcelDwellRequest (Low 218, NotTrusted, Unencoded)

```ts

export interface ParcelDwellRequestMessage {

}
```


## ParcelDwellReply (Low 219, Trusted, Unencoded)

```ts

export interface ParcelDwellReplyMessage {

}
```


## RequestParcelTransfer (Low 220, Trusted, Zerocoded)

```ts

export interface RequestParcelTransferMessage {

}
```


## UpdateParcel (Low 221, Trusted, Zerocoded)

```ts

export interface UpdateParcelMessage {

}
```


## RemoveParcel (Low 222, Trusted, Unencoded)

```ts

export interface RemoveParcelMessage {

}
```


## MergeParcel (Low 223, Trusted, Unencoded)

```ts

export interface MergeParcelMessage {

}
```


## LogParcelChanges (Low 224, Trusted, Zerocoded)

```ts

export interface LogParcelChangesMessage {

}
```


## CheckParcelSales (Low 225, Trusted, Unencoded)

```ts

export interface CheckParcelSalesMessage {

}
```


## ParcelSales (Low 226, Trusted, Unencoded)

```ts

export interface ParcelSalesMessage {

}
```


## ParcelGodMarkAsContent (Low 227, NotTrusted, Unencoded)

```ts

export interface ParcelGodMarkAsContentMessage {

}
```


## ViewerStartAuction (Low 228, NotTrusted, Unencoded)

```ts

export interface ViewerStartAuctionMessage {

}
```


## StartAuction (Low 229, Trusted, Unencoded)

```ts

export interface StartAuctionMessage {

}
```


## ConfirmAuctionStart (Low 230, Trusted, Unencoded)

```ts

export interface ConfirmAuctionStartMessage {

}
```


## CompleteAuction (Low 231, Trusted, Unencoded)

```ts

export interface CompleteAuctionMessage {

}
```


## CancelAuction (Low 232, Trusted, Unencoded)

```ts

export interface CancelAuctionMessage {

}
```


## CheckParcelAuctions (Low 233, Trusted, Unencoded)

```ts

export interface CheckParcelAuctionsMessage {

}
```


## ParcelAuctions (Low 234, Trusted, Unencoded)

```ts

export interface ParcelAuctionsMessage {

}
```


## UUIDNameRequest (Low 235, NotTrusted, Unencoded)

```ts

export interface UUIDNameRequestMessage {

}
```


## UUIDNameReply (Low 236, Trusted, Unencoded)

```ts

export interface UUIDNameReplyMessage {

}
```


## UUIDGroupNameRequest (Low 237, NotTrusted, Unencoded)

```ts

export interface UUIDGroupNameRequestMessage {

}
```


## UUIDGroupNameReply (Low 238, Trusted, Unencoded)

```ts

export interface UUIDGroupNameReplyMessage {

}
```


## ChatPass (Low 239, Trusted, Zerocoded)

```ts

export interface ChatPassMessage {

}
```


## EdgeDataPacket (High 24, Trusted, Zerocoded)

```ts

export interface EdgeDataPacketMessage {

}
```


## SimStatus (Medium 12, Trusted, Unencoded)

```ts

export interface SimStatusMessage {

}
```


## ChildAgentUpdate (High 25, Trusted, Zerocoded)

```ts

export interface ChildAgentUpdateMessage {

}
```


## ChildAgentAlive (High 26, Trusted, Unencoded)

```ts

export interface ChildAgentAliveMessage {

}
```


## ChildAgentPositionUpdate (High 27, Trusted, Unencoded)

```ts

export interface ChildAgentPositionUpdateMessage {

}
```


## ChildAgentDying (Low 240, Trusted, Zerocoded)

```ts

export interface ChildAgentDyingMessage {

}
```


## ChildAgentUnknown (Low 241, Trusted, Unencoded)

```ts

export interface ChildAgentUnknownMessage {

}
```


## AtomicPassObject (High 28, Trusted, Unencoded)

```ts

export interface AtomicPassObjectMessage {

}
```


## KillChildAgents (Low 242, Trusted, Unencoded)

```ts

export interface KillChildAgentsMessage {

}
```


## GetScriptRunning (Low 243, NotTrusted, Unencoded)

```ts

export interface GetScriptRunningMessage {

}
```


## ScriptRunningReply (Low 244, NotTrusted, Unencoded)

```ts

export interface ScriptRunningReplyMessage {

}
```


## SetScriptRunning (Low 245, NotTrusted, Unencoded)

```ts

export interface SetScriptRunningMessage {

}
```


## ScriptReset (Low 246, NotTrusted, Unencoded)

```ts

export interface ScriptResetMessage {

}
```


## ScriptSensorRequest (Low 247, Trusted, Zerocoded)

```ts

export interface ScriptSensorRequestMessage {

}
```


## ScriptSensorReply (Low 248, Trusted, Zerocoded)

```ts

export interface ScriptSensorReplyMessage {

}
```


## CompleteAgentMovement (Low 249, NotTrusted, Unencoded)

```ts

export interface CompleteAgentMovementMessage {

}
```


## AgentMovementComplete (Low 250, NotTrusted, Unencoded)

```ts

export interface AgentMovementCompleteMessage {

}
```


## DataServerLogout (Low 251, Trusted, Unencoded)

```ts

export interface DataServerLogoutMessage {

}
```


## LogoutRequest (Low 252, NotTrusted, Unencoded)

```ts

export interface LogoutRequestMessage {

}
```


## LogoutReply (Low 253, Trusted, Zerocoded)

```ts

export interface LogoutReplyMessage {

}
```


## ImprovedInstantMessage (Low 254, NotTrusted, Zerocoded)

```ts

export interface ImprovedInstantMessageMessage {

}
```


## RetrieveInstantMessages (Low 255, NotTrusted, Unencoded)

```ts

export interface RetrieveInstantMessagesMessage {

}
```


## FindAgent (Low 256, NotTrusted, Unencoded)

```ts

export interface FindAgentMessage {

}
```


## RequestGodlikePowers (Low 257, NotTrusted, Unencoded)

```ts

export interface RequestGodlikePowersMessage {

}
```


## GrantGodlikePowers (Low 258, Trusted, Unencoded)

```ts

export interface GrantGodlikePowersMessage {

}
```


## GodlikeMessage (Low 259, NotTrusted, Zerocoded)

```ts

export interface GodlikeMessageMessage {

}
```


## EstateOwnerMessage (Low 260, NotTrusted, Zerocoded)

```ts

export interface EstateOwnerMessageMessage {

}
```


## GenericMessage (Low 261, NotTrusted, Zerocoded)

```ts

export interface GenericMessageMessage {

}
```


## GenericStreamingMessage (High 31, Trusted, Unencoded)

```ts

export interface GenericStreamingMessageMessage {

}
```


## LargeGenericMessage (Low 430, NotTrusted, Unencoded)

```ts

export interface LargeGenericMessageMessage {

}
```


## MuteListRequest (Low 262, NotTrusted, Unencoded)

```ts

export interface MuteListRequestMessage {

}
```


## UpdateMuteListEntry (Low 263, NotTrusted, Unencoded)

```ts

export interface UpdateMuteListEntryMessage {

}
```


## RemoveMuteListEntry (Low 264, NotTrusted, Unencoded)

```ts

export interface RemoveMuteListEntryMessage {

}
```


## CopyInventoryFromNotecard (Low 265, NotTrusted, Zerocoded)

```ts

export interface CopyInventoryFromNotecardMessage {

}
```


## UpdateInventoryItem (Low 266, NotTrusted, Zerocoded)

```ts

export interface UpdateInventoryItemMessage {

}
```


## UpdateCreateInventoryItem (Low 267, Trusted, Zerocoded)

```ts

export interface UpdateCreateInventoryItemMessage {

}
```


## MoveInventoryItem (Low 268, NotTrusted, Zerocoded)

```ts

export interface MoveInventoryItemMessage {

}
```


## CopyInventoryItem (Low 269, NotTrusted, Zerocoded)

```ts

export interface CopyInventoryItemMessage {

}
```


## RemoveInventoryItem (Low 270, NotTrusted, Unencoded)

```ts

export interface RemoveInventoryItemMessage {

}
```


## ChangeInventoryItemFlags (Low 271, NotTrusted, Unencoded)

```ts

export interface ChangeInventoryItemFlagsMessage {

}
```


## SaveAssetIntoInventory (Low 272, Trusted, Unencoded)

```ts

export interface SaveAssetIntoInventoryMessage {

}
```


## CreateInventoryFolder (Low 273, NotTrusted, Unencoded)

```ts

export interface CreateInventoryFolderMessage {

}
```


## UpdateInventoryFolder (Low 274, NotTrusted, Unencoded)

```ts

export interface UpdateInventoryFolderMessage {

}
```


## MoveInventoryFolder (Low 275, NotTrusted, Zerocoded)

```ts

export interface MoveInventoryFolderMessage {

}
```


## RemoveInventoryFolder (Low 276, NotTrusted, Unencoded)

```ts

export interface RemoveInventoryFolderMessage {

}
```


## FetchInventoryDescendents (Low 277, NotTrusted, Zerocoded)

```ts

export interface FetchInventoryDescendentsMessage {

}
```


## InventoryDescendents (Low 278, Trusted, Zerocoded)

```ts

export interface InventoryDescendentsMessage {

}
```


## FetchInventory (Low 279, NotTrusted, Zerocoded)

```ts

export interface FetchInventoryMessage {

}
```


## FetchInventoryReply (Low 280, Trusted, Zerocoded)

```ts

export interface FetchInventoryReplyMessage {

}
```


## BulkUpdateInventory (Low 281, Trusted, Zerocoded)

```ts

export interface BulkUpdateInventoryMessage {

}
```


## RequestInventoryAsset (Low 282, Trusted, Unencoded)

```ts

export interface RequestInventoryAssetMessage {

}
```


## InventoryAssetResponse (Low 283, Trusted, Unencoded)

```ts

export interface InventoryAssetResponseMessage {

}
```


## RemoveInventoryObjects (Low 284, NotTrusted, Unencoded)

```ts

export interface RemoveInventoryObjectsMessage {

}
```


## PurgeInventoryDescendents (Low 285, NotTrusted, Zerocoded)

```ts

export interface PurgeInventoryDescendentsMessage {

}
```


## UpdateTaskInventory (Low 286, NotTrusted, Zerocoded)

```ts

export interface UpdateTaskInventoryMessage {

}
```


## RemoveTaskInventory (Low 287, NotTrusted, Zerocoded)

```ts

export interface RemoveTaskInventoryMessage {

}
```


## MoveTaskInventory (Low 288, NotTrusted, Unencoded)

```ts

export interface MoveTaskInventoryMessage {

}
```


## RequestTaskInventory (Low 289, NotTrusted, Unencoded)

```ts

export interface RequestTaskInventoryMessage {

}
```


## ReplyTaskInventory (Low 290, Trusted, Zerocoded)

```ts

export interface ReplyTaskInventoryMessage {

}
```


## DeRezObject (Low 291, NotTrusted, Zerocoded)

```ts

export interface DeRezObjectMessage {

}
```


## DeRezAck (Low 292, Trusted, Unencoded)

```ts

export interface DeRezAckMessage {

}
```


## RezObject (Low 293, NotTrusted, Zerocoded)

```ts

export interface RezObjectMessage {

}
```


## RezObjectFromNotecard (Low 294, NotTrusted, Zerocoded)

```ts

export interface RezObjectFromNotecardMessage {

}
```


## TransferInventory (Low 295, Trusted, Zerocoded)

```ts

export interface TransferInventoryMessage {

}
```


## TransferInventoryAck (Low 296, Trusted, Zerocoded)

```ts

export interface TransferInventoryAckMessage {

}
```


## AcceptFriendship (Low 297, NotTrusted, Unencoded)

```ts

export interface AcceptFriendshipMessage {

}
```


## DeclineFriendship (Low 298, NotTrusted, Unencoded)

```ts

export interface DeclineFriendshipMessage {

}
```


## FormFriendship (Low 299, Trusted, Unencoded)

```ts

export interface FormFriendshipMessage {

}
```


## TerminateFriendship (Low 300, NotTrusted, Unencoded)

```ts

export interface TerminateFriendshipMessage {

}
```


## OfferCallingCard (Low 301, NotTrusted, Unencoded)

```ts

export interface OfferCallingCardMessage {

}
```


## AcceptCallingCard (Low 302, NotTrusted, Unencoded)

```ts

export interface AcceptCallingCardMessage {

}
```


## DeclineCallingCard (Low 303, NotTrusted, Unencoded)

```ts

export interface DeclineCallingCardMessage {

}
```


## RezScript (Low 304, NotTrusted, Zerocoded)

```ts

export interface RezScriptMessage {

}
```


## CreateInventoryItem (Low 305, NotTrusted, Zerocoded)

```ts

export interface CreateInventoryItemMessage {

}
```


## CreateLandmarkForEvent (Low 306, NotTrusted, Zerocoded)

```ts

export interface CreateLandmarkForEventMessage {

}
```


## EventLocationRequest (Low 307, Trusted, Zerocoded)

```ts

export interface EventLocationRequestMessage {

}
```


## EventLocationReply (Low 308, Trusted, Zerocoded)

```ts

export interface EventLocationReplyMessage {

}
```


## RegionHandleRequest (Low 309, NotTrusted, Unencoded)

```ts

export interface RegionHandleRequestMessage {

}
```


## RegionIDAndHandleReply (Low 310, Trusted, Unencoded)

```ts

export interface RegionIDAndHandleReplyMessage {

}
```


## MoneyTransferRequest (Low 311, NotTrusted, Zerocoded)

```ts

export interface MoneyTransferRequestMessage {

}
```


## MoneyTransferBackend (Low 312, Trusted, Zerocoded)

```ts

export interface MoneyTransferBackendMessage {

}
```


## MoneyBalanceRequest (Low 313, NotTrusted, Zerocoded)

```ts

export interface MoneyBalanceRequestMessage {

}
```


## MoneyBalanceReply (Low 314, Trusted, Zerocoded)

```ts

export interface MoneyBalanceReplyMessage {

}
```


## RoutedMoneyBalanceReply (Low 315, Trusted, Zerocoded)

```ts

export interface RoutedMoneyBalanceReplyMessage {

}
```


## ActivateGestures (Low 316, NotTrusted, Unencoded)

```ts

export interface ActivateGesturesMessage {

}
```


## DeactivateGestures (Low 317, NotTrusted, Unencoded)

```ts

export interface DeactivateGesturesMessage {

}
```


## MuteListUpdate (Low 318, Trusted, Unencoded)

```ts

export interface MuteListUpdateMessage {

}
```


## UseCachedMuteList (Low 319, NotTrusted, Unencoded)

```ts

export interface UseCachedMuteListMessage {

}
```


## GrantUserRights (Low 320, NotTrusted, Unencoded)

```ts

export interface GrantUserRightsMessage {

}
```


## ChangeUserRights (Low 321, Trusted, Unencoded)

```ts

export interface ChangeUserRightsMessage {

}
```


## OnlineNotification (Low 322, Trusted, Unencoded)

```ts

export interface OnlineNotificationMessage {

}
```


## OfflineNotification (Low 323, Trusted, Unencoded)

```ts

export interface OfflineNotificationMessage {

}
```


## SetStartLocationRequest (Low 324, NotTrusted, Zerocoded)

```ts

export interface SetStartLocationRequestMessage {

}
```


## SetStartLocation (Low 325, Trusted, Zerocoded)

```ts

export interface SetStartLocationMessage {

}
```


## NetTest (Low 326, NotTrusted, Unencoded)

```ts

export interface NetTestMessage {

}
```


## SetCPURatio (Low 327, NotTrusted, Unencoded)

```ts

export interface SetCPURatioMessage {

}
```


## SimCrashed (Low 328, NotTrusted, Unencoded)

```ts

export interface SimCrashedMessage {

}
```


## NameValuePair (Low 329, Trusted, Unencoded)

```ts

export interface NameValuePairMessage {

}
```


## RemoveNameValuePair (Low 330, Trusted, Unencoded)

```ts

export interface RemoveNameValuePairMessage {

}
```


## UpdateAttachment (Low 331, Trusted, Zerocoded)

```ts

export interface UpdateAttachmentMessage {

}
```


## RemoveAttachment (Low 332, NotTrusted, Unencoded)

```ts

export interface RemoveAttachmentMessage {

}
```


## SoundTrigger (High 29, NotTrusted, Unencoded)

```ts

export interface SoundTriggerMessage {

}
```


## AttachedSound (Medium 13, Trusted, Unencoded)

```ts

export interface AttachedSoundMessage {

}
```


## AttachedSoundGainChange (Medium 14, Trusted, Unencoded)

```ts

export interface AttachedSoundGainChangeMessage {

}
```


## PreloadSound (Medium 15, Trusted, Unencoded)

```ts

export interface PreloadSoundMessage {

}
```


## ObjectAnimation (High 30, Trusted, Unencoded)

```ts

export interface ObjectAnimationMessage {

}
```


## AssetUploadRequest (Low 333, NotTrusted, Unencoded)

```ts

export interface AssetUploadRequestMessage {

}
```


## AssetUploadComplete (Low 334, NotTrusted, Unencoded)

```ts

export interface AssetUploadCompleteMessage {

}
```


## EmailMessageRequest (Low 335, Trusted, Unencoded)

```ts

export interface EmailMessageRequestMessage {

}
```


## EmailMessageReply (Low 336, Trusted, Unencoded)

```ts

export interface EmailMessageReplyMessage {

}
```


## InternalScriptMail (Medium 16, Trusted, Unencoded)

```ts

export interface InternalScriptMailMessage {

}
```


## ScriptDataRequest (Low 337, Trusted, Unencoded)

```ts

export interface ScriptDataRequestMessage {

}
```


## ScriptDataReply (Low 338, Trusted, Unencoded)

```ts

export interface ScriptDataReplyMessage {

}
```


## CreateGroupRequest (Low 339, NotTrusted, Zerocoded)

```ts

export interface CreateGroupRequestMessage {

}
```


## CreateGroupReply (Low 340, Trusted, Unencoded)

```ts

export interface CreateGroupReplyMessage {

}
```


## UpdateGroupInfo (Low 341, NotTrusted, Zerocoded)

```ts

export interface UpdateGroupInfoMessage {

}
```


## GroupRoleChanges (Low 342, NotTrusted, Unencoded)

```ts

export interface GroupRoleChangesMessage {

}
```


## JoinGroupRequest (Low 343, NotTrusted, Zerocoded)

```ts

export interface JoinGroupRequestMessage {

}
```


## JoinGroupReply (Low 344, Trusted, Unencoded)

```ts

export interface JoinGroupReplyMessage {

}
```


## EjectGroupMemberRequest (Low 345, NotTrusted, Unencoded)

```ts

export interface EjectGroupMemberRequestMessage {

}
```


## EjectGroupMemberReply (Low 346, Trusted, Unencoded)

```ts

export interface EjectGroupMemberReplyMessage {

}
```


## LeaveGroupRequest (Low 347, NotTrusted, Unencoded)

```ts

export interface LeaveGroupRequestMessage {

}
```


## LeaveGroupReply (Low 348, Trusted, Unencoded)

```ts

export interface LeaveGroupReplyMessage {

}
```


## InviteGroupRequest (Low 349, NotTrusted, Unencoded)

```ts

export interface InviteGroupRequestMessage {

}
```


## InviteGroupResponse (Low 350, Trusted, Unencoded)

```ts

export interface InviteGroupResponseMessage {

}
```


## GroupProfileRequest (Low 351, NotTrusted, Unencoded)

```ts

export interface GroupProfileRequestMessage {

}
```


## GroupProfileReply (Low 352, Trusted, Zerocoded)

```ts

export interface GroupProfileReplyMessage {

}
```


## GroupAccountSummaryRequest (Low 353, NotTrusted, Zerocoded)

```ts

export interface GroupAccountSummaryRequestMessage {

}
```


## GroupAccountSummaryReply (Low 354, Trusted, Zerocoded)

```ts

export interface GroupAccountSummaryReplyMessage {

}
```


## GroupAccountDetailsRequest (Low 355, NotTrusted, Zerocoded)

```ts

export interface GroupAccountDetailsRequestMessage {

}
```


## GroupAccountDetailsReply (Low 356, Trusted, Zerocoded)

```ts

export interface GroupAccountDetailsReplyMessage {

}
```


## GroupAccountTransactionsRequest (Low 357, NotTrusted, Zerocoded)

```ts

export interface GroupAccountTransactionsRequestMessage {

}
```


## GroupAccountTransactionsReply (Low 358, Trusted, Zerocoded)

```ts

export interface GroupAccountTransactionsReplyMessage {

}
```


## GroupActiveProposalsRequest (Low 359, NotTrusted, Unencoded)

```ts

export interface GroupActiveProposalsRequestMessage {

}
```


## GroupActiveProposalItemReply (Low 360, Trusted, Zerocoded)

```ts

export interface GroupActiveProposalItemReplyMessage {

}
```


## GroupVoteHistoryRequest (Low 361, NotTrusted, Unencoded)

```ts

export interface GroupVoteHistoryRequestMessage {

}
```


## GroupVoteHistoryItemReply (Low 362, Trusted, Zerocoded)

```ts

export interface GroupVoteHistoryItemReplyMessage {

}
```


## StartGroupProposal (Low 363, NotTrusted, Zerocoded)

```ts

export interface StartGroupProposalMessage {

}
```


## GroupProposalBallot (Low 364, NotTrusted, Unencoded)

```ts

export interface GroupProposalBallotMessage {

}
```


## TallyVotes (Low 365, Trusted, Unencoded)

```ts

export interface TallyVotesMessage {

}
```


## GroupMembersRequest (Low 366, NotTrusted, Unencoded)

```ts

export interface GroupMembersRequestMessage {

}
```


## GroupMembersReply (Low 367, Trusted, Zerocoded)

```ts

export interface GroupMembersReplyMessage {

}
```


## ActivateGroup (Low 368, NotTrusted, Zerocoded)

```ts

export interface ActivateGroupMessage {

}
```


## SetGroupContribution (Low 369, NotTrusted, Unencoded)

```ts

export interface SetGroupContributionMessage {

}
```


## SetGroupAcceptNotices (Low 370, NotTrusted, Unencoded)

```ts

export interface SetGroupAcceptNoticesMessage {

}
```


## GroupRoleDataRequest (Low 371, NotTrusted, Unencoded)

```ts

export interface GroupRoleDataRequestMessage {

}
```


## GroupRoleDataReply (Low 372, Trusted, Unencoded)

```ts

export interface GroupRoleDataReplyMessage {

}
```


## GroupRoleMembersRequest (Low 373, NotTrusted, Unencoded)

```ts

export interface GroupRoleMembersRequestMessage {

}
```


## GroupRoleMembersReply (Low 374, Trusted, Unencoded)

```ts

export interface GroupRoleMembersReplyMessage {

}
```


## GroupTitlesRequest (Low 375, NotTrusted, Unencoded)

```ts

export interface GroupTitlesRequestMessage {

}
```


## GroupTitlesReply (Low 376, Trusted, Zerocoded)

```ts

export interface GroupTitlesReplyMessage {

}
```


## GroupTitleUpdate (Low 377, NotTrusted, Unencoded)

```ts

export interface GroupTitleUpdateMessage {

}
```


## GroupRoleUpdate (Low 378, NotTrusted, Unencoded)

```ts

export interface GroupRoleUpdateMessage {

}
```


## LiveHelpGroupRequest (Low 379, Trusted, Unencoded)

```ts

export interface LiveHelpGroupRequestMessage {

}
```


## LiveHelpGroupReply (Low 380, Trusted, Unencoded)

```ts

export interface LiveHelpGroupReplyMessage {

}
```


## AgentWearablesRequest (Low 381, NotTrusted, Unencoded)

```ts

export interface AgentWearablesRequestMessage {

}
```


## AgentWearablesUpdate (Low 382, Trusted, Zerocoded)

```ts

export interface AgentWearablesUpdateMessage {

}
```


## AgentIsNowWearing (Low 383, NotTrusted, Zerocoded)

```ts

export interface AgentIsNowWearingMessage {

}
```


## AgentCachedTexture (Low 384, NotTrusted, Unencoded)

```ts

export interface AgentCachedTextureMessage {

}
```


## AgentCachedTextureResponse (Low 385, Trusted, Unencoded)

```ts

export interface AgentCachedTextureResponseMessage {

}
```


## AgentDataUpdateRequest (Low 386, NotTrusted, Unencoded)

```ts

export interface AgentDataUpdateRequestMessage {

}
```


## AgentDataUpdate (Low 387, Trusted, Zerocoded)

```ts

export interface AgentDataUpdateMessage {

}
```


## GroupDataUpdate (Low 388, Trusted, Zerocoded)

```ts

export interface GroupDataUpdateMessage {

}
```


## AgentGroupDataUpdate (Low 389, Trusted, Zerocoded)

```ts

export interface AgentGroupDataUpdateMessage {

}
```


## AgentDropGroup (Low 390, Trusted, Zerocoded)

```ts

export interface AgentDropGroupMessage {

}
```


## LogTextMessage (Low 391, Trusted, Zerocoded)

```ts

export interface LogTextMessageMessage {

}
```


## ViewerEffect (Medium 17, NotTrusted, Zerocoded)

```ts

export interface ViewerEffectMessage {

}
```


## CreateTrustedCircuit (Low 392, NotTrusted, Unencoded)

```ts

export interface CreateTrustedCircuitMessage {

}
```


## DenyTrustedCircuit (Low 393, NotTrusted, Unencoded)

```ts

export interface DenyTrustedCircuitMessage {

}
```


## RequestTrustedCircuit (Low 394, Trusted, Unencoded)

```ts

export interface RequestTrustedCircuitMessage {

}
```


## RezSingleAttachmentFromInv (Low 395, NotTrusted, Zerocoded)

```ts

export interface RezSingleAttachmentFromInvMessage {

}
```


## RezMultipleAttachmentsFromInv (Low 396, NotTrusted, Zerocoded)

```ts

export interface RezMultipleAttachmentsFromInvMessage {

}
```


## DetachAttachmentIntoInv (Low 397, NotTrusted, Unencoded)

```ts

export interface DetachAttachmentIntoInvMessage {

}
```


## CreateNewOutfitAttachments (Low 398, NotTrusted, Unencoded)

```ts

export interface CreateNewOutfitAttachmentsMessage {

}
```


## UserInfoRequest (Low 399, NotTrusted, Unencoded)

```ts

export interface UserInfoRequestMessage {

}
```


## UserInfoReply (Low 400, NotTrusted, Unencoded)

```ts

export interface UserInfoReplyMessage {

}
```


## UpdateUserInfo (Low 401, NotTrusted, Unencoded)

```ts

export interface UpdateUserInfoMessage {

}
```


## ParcelRename (Low 402, Trusted, Unencoded)

```ts

export interface ParcelRenameMessage {

}
```


## InitiateDownload (Low 403, NotTrusted, Unencoded)

```ts

export interface InitiateDownloadMessage {

}
```


## SystemMessage (Low 404, Trusted, Zerocoded)

```ts

export interface SystemMessageMessage {

}
```


## MapLayerRequest (Low 405, NotTrusted, Unencoded)

```ts

export interface MapLayerRequestMessage {

}
```


## MapLayerReply (Low 406, Trusted, Unencoded)

```ts

export interface MapLayerReplyMessage {

}
```


## MapBlockRequest (Low 407, NotTrusted, Unencoded)

```ts

export interface MapBlockRequestMessage {

}
```


## MapNameRequest (Low 408, NotTrusted, Unencoded)

```ts

export interface MapNameRequestMessage {

}
```


## MapBlockReply (Low 409, Trusted, Unencoded)

```ts

export interface MapBlockReplyMessage {

}
```


## MapItemRequest (Low 410, NotTrusted, Unencoded)

```ts

export interface MapItemRequestMessage {

}
```


## MapItemReply (Low 411, Trusted, Unencoded)

```ts

export interface MapItemReplyMessage {

}
```


## SendPostcard (Low 412, NotTrusted, Unencoded)

```ts

export interface SendPostcardMessage {

}
```


## RpcChannelRequest (Low 413, Trusted, Unencoded)

```ts

export interface RpcChannelRequestMessage {

}
```


## RpcChannelReply (Low 414, Trusted, Unencoded)

```ts

export interface RpcChannelReplyMessage {

}
```


## RpcScriptRequestInbound (Low 415, NotTrusted, Unencoded)

```ts

export interface RpcScriptRequestInboundMessage {

}
```


## RpcScriptRequestInboundForward (Low 416, Trusted, Unencoded)

```ts

export interface RpcScriptRequestInboundForwardMessage {

}
```


## RpcScriptReplyInbound (Low 417, NotTrusted, Unencoded)

```ts

export interface RpcScriptReplyInboundMessage {

}
```


## ScriptMailRegistration (Low 418, Trusted, Unencoded)

```ts

export interface ScriptMailRegistrationMessage {

}
```


## ParcelMediaCommandMessage (Low 419, Trusted, Unencoded)

```ts

export interface ParcelMediaCommandMessageMessage {

}
```


## ParcelMediaUpdate (Low 420, Trusted, Unencoded)

```ts

export interface ParcelMediaUpdateMessage {

}
```


## LandStatRequest (Low 421, NotTrusted, Unencoded)

```ts

export interface LandStatRequestMessage {

}
```


## LandStatReply (Low 422, Trusted, Unencoded)

```ts

export interface LandStatReplyMessage {

}
```


## Error (Low 423, NotTrusted, Zerocoded)

```ts

export interface ErrorMessage {

}
```


## ObjectIncludeInSearch (Low 424, NotTrusted, Unencoded)

```ts

export interface ObjectIncludeInSearchMessage {

}
```


## RezRestoreToWorld (Low 425, NotTrusted, Unencoded)

```ts

export interface RezRestoreToWorldMessage {

}
```


## LinkInventoryItem (Low 426, NotTrusted, Zerocoded)

```ts

export interface LinkInventoryItemMessage {

}
```


## RetrieveIMsExtended (Low 427, Trusted, Unencoded)

```ts

export interface RetrieveIMsExtendedMessage {

}
```


## JoinGroupRequestExtended (Low 428, Trusted, Unencoded)

```ts

export interface JoinGroupRequestExtendedMessage {

}
```


## CreateGroupRequestExtended (Low 429, Trusted, Unencoded)

```ts

export interface CreateGroupRequestExtendedMessage {

}
```


## GameControlInput (High 32, NotTrusted, Zerocoded)

```ts

export interface GameControlInputMessage {

}
```
