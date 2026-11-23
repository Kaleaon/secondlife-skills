# UDP Message Reference (generated from secondlife/master-message-template)

Generated from `message_template.msg`. Always diff against the template shipped in the viewer you target: the master template has been stale before. Frequency encoding: High = 1 byte ID, Medium = 2 bytes, Low = 4 bytes, Fixed = 4 bytes.


## TestMessage

- Frequency: Low | Number: 1 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PacketAck

- Frequency: Fixed | Number: 0xFFFFFFFB | Trust: NotTrusted | Encoding: Unencoded 

- Fixed: protocol-level messages with 0xFFFFFFxx IDs, handled by the circuit layer itself.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## OpenCircuit

- Frequency: Fixed | Number: 0xFFFFFFFC | Trust: NotTrusted | Encoding: Unencoded UDPBlackListed

- Fixed: protocol-level messages with 0xFFFFFFxx IDs, handled by the circuit layer itself.

- Flags: UDPBlackListed. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CloseCircuit

- Frequency: Fixed | Number: 0xFFFFFFFD | Trust: NotTrusted | Encoding: Unencoded 

- Fixed: protocol-level messages with 0xFFFFFFxx IDs, handled by the circuit layer itself.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## StartPingCheck

- Frequency: High | Number: 1 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CompletePingCheck

- Frequency: High | Number: 2 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AddCircuitCode

- Frequency: Low | Number: 2 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UseCircuitCode

- Frequency: Low | Number: 3 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## NeighborList

- Frequency: High | Number: 3 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarTextureUpdate

- Frequency: Low | Number: 4 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimulatorMapUpdate

- Frequency: Low | Number: 5 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimulatorSetMap

- Frequency: Low | Number: 6 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SubscribeLoad

- Frequency: Low | Number: 7 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UnsubscribeLoad

- Frequency: Low | Number: 8 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimulatorReady

- Frequency: Low | Number: 9 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TelehubInfo

- Frequency: Low | Number: 10 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimulatorPresentAtLocation

- Frequency: Low | Number: 11 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimulatorLoad

- Frequency: Low | Number: 12 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimulatorShutdownRequest

- Frequency: Low | Number: 13 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionPresenceRequestByRegionID

- Frequency: Low | Number: 14 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionPresenceRequestByHandle

- Frequency: Low | Number: 15 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionPresenceResponse

- Frequency: Low | Number: 16 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateSimulator

- Frequency: Low | Number: 17 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LogDwellTime

- Frequency: Low | Number: 18 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## FeatureDisabled

- Frequency: Low | Number: 19 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LogFailedMoneyTransaction

- Frequency: Low | Number: 20 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UserReportInternal

- Frequency: Low | Number: 21 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetSimStatusInDatabase

- Frequency: Low | Number: 22 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetSimPresenceInDatabase

- Frequency: Low | Number: 23 | Trust: Trusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EconomyDataRequest

- Frequency: Low | Number: 24 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EconomyData

- Frequency: Low | Number: 25 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPickerRequest

- Frequency: Low | Number: 26 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPickerRequestBackend

- Frequency: Low | Number: 27 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPickerReply

- Frequency: Low | Number: 28 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PlacesQuery

- Frequency: Low | Number: 29 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PlacesReply

- Frequency: Low | Number: 30 | Trust: Trusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirFindQuery

- Frequency: Low | Number: 31 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirFindQueryBackend

- Frequency: Low | Number: 32 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirPlacesQuery

- Frequency: Low | Number: 33 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirPlacesQueryBackend

- Frequency: Low | Number: 34 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirPlacesReply

- Frequency: Low | Number: 35 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirPeopleReply

- Frequency: Low | Number: 36 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirEventsReply

- Frequency: Low | Number: 37 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirGroupsReply

- Frequency: Low | Number: 38 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirClassifiedQuery

- Frequency: Low | Number: 39 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirClassifiedQueryBackend

- Frequency: Low | Number: 40 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirClassifiedReply

- Frequency: Low | Number: 41 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarClassifiedReply

- Frequency: Low | Number: 42 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ClassifiedInfoRequest

- Frequency: Low | Number: 43 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ClassifiedInfoReply

- Frequency: Low | Number: 44 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ClassifiedInfoUpdate

- Frequency: Low | Number: 45 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ClassifiedDelete

- Frequency: Low | Number: 46 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ClassifiedGodDelete

- Frequency: Low | Number: 47 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirLandQuery

- Frequency: Low | Number: 48 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirLandQueryBackend

- Frequency: Low | Number: 49 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirLandReply

- Frequency: Low | Number: 50 | Trust: Trusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirPopularQuery

- Frequency: Low | Number: 51 | Trust: NotTrusted | Encoding: Zerocoded Deprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: Deprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirPopularQueryBackend

- Frequency: Low | Number: 52 | Trust: Trusted | Encoding: Zerocoded Deprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: Deprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DirPopularReply

- Frequency: Low | Number: 53 | Trust: Trusted | Encoding: Zerocoded Deprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: Deprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelInfoRequest

- Frequency: Low | Number: 54 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelInfoReply

- Frequency: Low | Number: 55 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelObjectOwnersRequest

- Frequency: Low | Number: 56 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelObjectOwnersReply

- Frequency: Low | Number: 57 | Trust: Trusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupNoticesListRequest

- Frequency: Low | Number: 58 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupNoticesListReply

- Frequency: Low | Number: 59 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupNoticeRequest

- Frequency: Low | Number: 60 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupNoticeAdd

- Frequency: Low | Number: 61 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportRequest

- Frequency: Low | Number: 62 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportLocationRequest

- Frequency: Low | Number: 63 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportLocal

- Frequency: Low | Number: 64 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportLandmarkRequest

- Frequency: Low | Number: 65 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportProgress

- Frequency: Low | Number: 66 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DataHomeLocationRequest

- Frequency: Low | Number: 67 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DataHomeLocationReply

- Frequency: Low | Number: 68 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportFinish

- Frequency: Low | Number: 69 | Trust: Trusted | Encoding: Unencoded UDPBlackListed

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPBlackListed. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## StartLure

- Frequency: Low | Number: 70 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportLureRequest

- Frequency: Low | Number: 71 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportCancel

- Frequency: Low | Number: 72 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportStart

- Frequency: Low | Number: 73 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportFailed

- Frequency: Low | Number: 74 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## Undo

- Frequency: Low | Number: 75 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## Redo

- Frequency: Low | Number: 76 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UndoLand

- Frequency: Low | Number: 77 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentPause

- Frequency: Low | Number: 78 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentResume

- Frequency: Low | Number: 79 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentUpdate

- Frequency: High | Number: 4 | Trust: NotTrusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChatFromViewer

- Frequency: Low | Number: 80 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentThrottle

- Frequency: Low | Number: 81 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentFOV

- Frequency: Low | Number: 82 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentHeightWidth

- Frequency: Low | Number: 83 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentSetAppearance

- Frequency: Low | Number: 84 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentAnimation

- Frequency: High | Number: 5 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentRequestSit

- Frequency: High | Number: 6 | Trust: NotTrusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentSit

- Frequency: High | Number: 7 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentQuitCopy

- Frequency: Low | Number: 85 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestImage

- Frequency: High | Number: 8 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ImageNotInDatabase

- Frequency: Low | Number: 86 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RebakeAvatarTextures

- Frequency: Low | Number: 87 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetAlwaysRun

- Frequency: Low | Number: 88 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectAdd

- Frequency: Medium | Number: 1 | Trust: NotTrusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDelete

- Frequency: Low | Number: 89 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDuplicate

- Frequency: Low | Number: 90 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDuplicateOnRay

- Frequency: Low | Number: 91 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MultipleObjectUpdate

- Frequency: Medium | Number: 2 | Trust: NotTrusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestMultipleObjects

- Frequency: Medium | Number: 3 | Trust: NotTrusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectPosition

- Frequency: Medium | Number: 4 | Trust: NotTrusted | Encoding: Zerocoded Deprecated

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: Deprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectScale

- Frequency: Low | Number: 92 | Trust: NotTrusted | Encoding: Zerocoded Deprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: Deprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectRotation

- Frequency: Low | Number: 93 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectFlagUpdate

- Frequency: Low | Number: 94 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectClickAction

- Frequency: Low | Number: 95 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectImage

- Frequency: Low | Number: 96 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectBypassModUpdate

- Frequency: Low | Number: 431 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectMaterial

- Frequency: Low | Number: 97 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectShape

- Frequency: Low | Number: 98 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectExtraParams

- Frequency: Low | Number: 99 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectOwner

- Frequency: Low | Number: 100 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectGroup

- Frequency: Low | Number: 101 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectBuy

- Frequency: Low | Number: 102 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## BuyObjectInventory

- Frequency: Low | Number: 103 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DerezContainer

- Frequency: Low | Number: 104 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectPermissions

- Frequency: Low | Number: 105 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectSaleInfo

- Frequency: Low | Number: 106 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectName

- Frequency: Low | Number: 107 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDescription

- Frequency: Low | Number: 108 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectCategory

- Frequency: Low | Number: 109 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectSelect

- Frequency: Low | Number: 110 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDeselect

- Frequency: Low | Number: 111 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectAttach

- Frequency: Low | Number: 112 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDetach

- Frequency: Low | Number: 113 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDrop

- Frequency: Low | Number: 114 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectLink

- Frequency: Low | Number: 115 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDelink

- Frequency: Low | Number: 116 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectGrab

- Frequency: Low | Number: 117 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectGrabUpdate

- Frequency: Low | Number: 118 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectDeGrab

- Frequency: Low | Number: 119 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectSpinStart

- Frequency: Low | Number: 120 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectSpinUpdate

- Frequency: Low | Number: 121 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectSpinStop

- Frequency: Low | Number: 122 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectExportSelected

- Frequency: Low | Number: 123 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ModifyLand

- Frequency: Low | Number: 124 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## VelocityInterpolateOn

- Frequency: Low | Number: 125 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## VelocityInterpolateOff

- Frequency: Low | Number: 126 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## StateSave

- Frequency: Low | Number: 127 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ReportAutosaveCrash

- Frequency: Low | Number: 128 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimWideDeletes

- Frequency: Low | Number: 129 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestObjectPropertiesFamily

- Frequency: Medium | Number: 5 | Trust: NotTrusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TrackAgent

- Frequency: Low | Number: 130 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ViewerStats

- Frequency: Low | Number: 131 | Trust: NotTrusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptAnswerYes

- Frequency: Low | Number: 132 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UserReport

- Frequency: Low | Number: 133 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AlertMessage

- Frequency: Low | Number: 134 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentAlertMessage

- Frequency: Low | Number: 135 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MeanCollisionAlert

- Frequency: Low | Number: 136 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ViewerFrozenMessage

- Frequency: Low | Number: 137 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## HealthMessage

- Frequency: Low | Number: 138 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChatFromSimulator

- Frequency: Low | Number: 139 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimStats

- Frequency: Low | Number: 140 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestRegionInfo

- Frequency: Low | Number: 141 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionInfo

- Frequency: Low | Number: 142 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GodUpdateRegionInfo

- Frequency: Low | Number: 143 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## NearestLandingRegionRequest

- Frequency: Low | Number: 144 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## NearestLandingRegionReply

- Frequency: Low | Number: 145 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## NearestLandingRegionUpdated

- Frequency: Low | Number: 146 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TeleportLandingStatusChanged

- Frequency: Low | Number: 147 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionHandshake

- Frequency: Low | Number: 148 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionHandshakeReply

- Frequency: Low | Number: 149 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CoarseLocationUpdate

- Frequency: Medium | Number: 6 | Trust: Trusted | Encoding: Unencoded 

- Medium frequency: regular session traffic.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ImageData

- Frequency: High | Number: 9 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ImagePacket

- Frequency: High | Number: 10 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LayerData

- Frequency: High | Number: 11 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectUpdate

- Frequency: High | Number: 12 | Trust: Trusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectUpdateCompressed

- Frequency: High | Number: 13 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectUpdateCached

- Frequency: High | Number: 14 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ImprovedTerseObjectUpdate

- Frequency: High | Number: 15 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## KillObject

- Frequency: High | Number: 16 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CrossedRegion

- Frequency: Medium | Number: 7 | Trust: Trusted | Encoding: Unencoded UDPBlackListed

- Medium frequency: regular session traffic.

- Flags: UDPBlackListed. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimulatorViewerTimeMessage

- Frequency: Low | Number: 150 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EnableSimulator

- Frequency: Low | Number: 151 | Trust: Trusted | Encoding: Unencoded UDPBlackListed

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPBlackListed. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DisableSimulator

- Frequency: Low | Number: 152 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ConfirmEnableSimulator

- Frequency: Medium | Number: 8 | Trust: Trusted | Encoding: Unencoded 

- Medium frequency: regular session traffic.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TransferRequest

- Frequency: Low | Number: 153 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TransferInfo

- Frequency: Low | Number: 154 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TransferPacket

- Frequency: High | Number: 17 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TransferAbort

- Frequency: Low | Number: 155 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestXfer

- Frequency: Low | Number: 156 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SendXferPacket

- Frequency: High | Number: 18 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ConfirmXferPacket

- Frequency: High | Number: 19 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AbortXfer

- Frequency: Low | Number: 157 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarAnimation

- Frequency: High | Number: 20 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarAppearance

- Frequency: Low | Number: 158 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarSitResponse

- Frequency: High | Number: 21 | Trust: Trusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetFollowCamProperties

- Frequency: Low | Number: 159 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ClearFollowCamProperties

- Frequency: Low | Number: 160 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CameraConstraint

- Frequency: High | Number: 22 | Trust: Trusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectProperties

- Frequency: Medium | Number: 9 | Trust: Trusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectPropertiesFamily

- Frequency: Medium | Number: 10 | Trust: Trusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestPayPrice

- Frequency: Low | Number: 161 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PayPriceReply

- Frequency: Low | Number: 162 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## KickUser

- Frequency: Low | Number: 163 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## KickUserAck

- Frequency: Low | Number: 164 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GodKickUser

- Frequency: Low | Number: 165 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SystemKickUser

- Frequency: Low | Number: 166 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EjectUser

- Frequency: Low | Number: 167 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## FreezeUser

- Frequency: Low | Number: 168 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPropertiesRequest

- Frequency: Low | Number: 169 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPropertiesRequestBackend

- Frequency: Low | Number: 170 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPropertiesReply

- Frequency: Low | Number: 171 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarInterestsReply

- Frequency: Low | Number: 172 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarGroupsReply

- Frequency: Low | Number: 173 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPropertiesUpdate

- Frequency: Low | Number: 174 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarInterestsUpdate

- Frequency: Low | Number: 175 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarNotesReply

- Frequency: Low | Number: 176 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarNotesUpdate

- Frequency: Low | Number: 177 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AvatarPicksReply

- Frequency: Low | Number: 178 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EventInfoRequest

- Frequency: Low | Number: 179 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EventInfoReply

- Frequency: Low | Number: 180 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EventNotificationAddRequest

- Frequency: Low | Number: 181 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EventNotificationRemoveRequest

- Frequency: Low | Number: 182 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EventGodDelete

- Frequency: Low | Number: 183 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PickInfoReply

- Frequency: Low | Number: 184 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PickInfoUpdate

- Frequency: Low | Number: 185 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PickDelete

- Frequency: Low | Number: 186 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PickGodDelete

- Frequency: Low | Number: 187 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptQuestion

- Frequency: Low | Number: 188 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptControlChange

- Frequency: Low | Number: 189 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptDialog

- Frequency: Low | Number: 190 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptDialogReply

- Frequency: Low | Number: 191 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ForceScriptControlRelease

- Frequency: Low | Number: 192 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RevokePermissions

- Frequency: Low | Number: 193 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LoadURL

- Frequency: Low | Number: 194 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptTeleportRequest

- Frequency: Low | Number: 195 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelOverlay

- Frequency: Low | Number: 196 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelPropertiesRequest

- Frequency: Medium | Number: 11 | Trust: NotTrusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelPropertiesRequestByID

- Frequency: Low | Number: 197 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelProperties

- Frequency: High | Number: 23 | Trust: Trusted | Encoding: Zerocoded UDPDeprecated

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelPropertiesUpdate

- Frequency: Low | Number: 198 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelReturnObjects

- Frequency: Low | Number: 199 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelSetOtherCleanTime

- Frequency: Low | Number: 200 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelDisableObjects

- Frequency: Low | Number: 201 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelSelectObjects

- Frequency: Low | Number: 202 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EstateCovenantRequest

- Frequency: Low | Number: 203 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EstateCovenantReply

- Frequency: Low | Number: 204 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ForceObjectSelect

- Frequency: Low | Number: 205 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelBuyPass

- Frequency: Low | Number: 206 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelDeedToGroup

- Frequency: Low | Number: 207 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelReclaim

- Frequency: Low | Number: 208 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelClaim

- Frequency: Low | Number: 209 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelJoin

- Frequency: Low | Number: 210 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelDivide

- Frequency: Low | Number: 211 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelRelease

- Frequency: Low | Number: 212 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelBuy

- Frequency: Low | Number: 213 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelGodForceOwner

- Frequency: Low | Number: 214 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelAccessListRequest

- Frequency: Low | Number: 215 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelAccessListReply

- Frequency: Low | Number: 216 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelAccessListUpdate

- Frequency: Low | Number: 217 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelDwellRequest

- Frequency: Low | Number: 218 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelDwellReply

- Frequency: Low | Number: 219 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestParcelTransfer

- Frequency: Low | Number: 220 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateParcel

- Frequency: Low | Number: 221 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveParcel

- Frequency: Low | Number: 222 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MergeParcel

- Frequency: Low | Number: 223 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LogParcelChanges

- Frequency: Low | Number: 224 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CheckParcelSales

- Frequency: Low | Number: 225 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelSales

- Frequency: Low | Number: 226 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelGodMarkAsContent

- Frequency: Low | Number: 227 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ViewerStartAuction

- Frequency: Low | Number: 228 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## StartAuction

- Frequency: Low | Number: 229 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ConfirmAuctionStart

- Frequency: Low | Number: 230 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CompleteAuction

- Frequency: Low | Number: 231 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CancelAuction

- Frequency: Low | Number: 232 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CheckParcelAuctions

- Frequency: Low | Number: 233 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelAuctions

- Frequency: Low | Number: 234 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UUIDNameRequest

- Frequency: Low | Number: 235 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UUIDNameReply

- Frequency: Low | Number: 236 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UUIDGroupNameRequest

- Frequency: Low | Number: 237 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UUIDGroupNameReply

- Frequency: Low | Number: 238 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChatPass

- Frequency: Low | Number: 239 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EdgeDataPacket

- Frequency: High | Number: 24 | Trust: Trusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimStatus

- Frequency: Medium | Number: 12 | Trust: Trusted | Encoding: Unencoded 

- Medium frequency: regular session traffic.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChildAgentUpdate

- Frequency: High | Number: 25 | Trust: Trusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChildAgentAlive

- Frequency: High | Number: 26 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChildAgentPositionUpdate

- Frequency: High | Number: 27 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChildAgentDying

- Frequency: Low | Number: 240 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChildAgentUnknown

- Frequency: Low | Number: 241 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AtomicPassObject

- Frequency: High | Number: 28 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## KillChildAgents

- Frequency: Low | Number: 242 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GetScriptRunning

- Frequency: Low | Number: 243 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptRunningReply

- Frequency: Low | Number: 244 | Trust: NotTrusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetScriptRunning

- Frequency: Low | Number: 245 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptReset

- Frequency: Low | Number: 246 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptSensorRequest

- Frequency: Low | Number: 247 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptSensorReply

- Frequency: Low | Number: 248 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CompleteAgentMovement

- Frequency: Low | Number: 249 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentMovementComplete

- Frequency: Low | Number: 250 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DataServerLogout

- Frequency: Low | Number: 251 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LogoutRequest

- Frequency: Low | Number: 252 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LogoutReply

- Frequency: Low | Number: 253 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ImprovedInstantMessage

- Frequency: Low | Number: 254 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RetrieveInstantMessages

- Frequency: Low | Number: 255 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## FindAgent

- Frequency: Low | Number: 256 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestGodlikePowers

- Frequency: Low | Number: 257 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GrantGodlikePowers

- Frequency: Low | Number: 258 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GodlikeMessage

- Frequency: Low | Number: 259 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EstateOwnerMessage

- Frequency: Low | Number: 260 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GenericMessage

- Frequency: Low | Number: 261 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GenericStreamingMessage

- Frequency: High | Number: 31 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LargeGenericMessage

- Frequency: Low | Number: 430 | Trust: NotTrusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MuteListRequest

- Frequency: Low | Number: 262 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateMuteListEntry

- Frequency: Low | Number: 263 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveMuteListEntry

- Frequency: Low | Number: 264 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CopyInventoryFromNotecard

- Frequency: Low | Number: 265 | Trust: NotTrusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateInventoryItem

- Frequency: Low | Number: 266 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateCreateInventoryItem

- Frequency: Low | Number: 267 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MoveInventoryItem

- Frequency: Low | Number: 268 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CopyInventoryItem

- Frequency: Low | Number: 269 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveInventoryItem

- Frequency: Low | Number: 270 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChangeInventoryItemFlags

- Frequency: Low | Number: 271 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SaveAssetIntoInventory

- Frequency: Low | Number: 272 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateInventoryFolder

- Frequency: Low | Number: 273 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateInventoryFolder

- Frequency: Low | Number: 274 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MoveInventoryFolder

- Frequency: Low | Number: 275 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveInventoryFolder

- Frequency: Low | Number: 276 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## FetchInventoryDescendents

- Frequency: Low | Number: 277 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## InventoryDescendents

- Frequency: Low | Number: 278 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## FetchInventory

- Frequency: Low | Number: 279 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## FetchInventoryReply

- Frequency: Low | Number: 280 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## BulkUpdateInventory

- Frequency: Low | Number: 281 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestInventoryAsset

- Frequency: Low | Number: 282 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## InventoryAssetResponse

- Frequency: Low | Number: 283 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveInventoryObjects

- Frequency: Low | Number: 284 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PurgeInventoryDescendents

- Frequency: Low | Number: 285 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateTaskInventory

- Frequency: Low | Number: 286 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveTaskInventory

- Frequency: Low | Number: 287 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MoveTaskInventory

- Frequency: Low | Number: 288 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestTaskInventory

- Frequency: Low | Number: 289 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ReplyTaskInventory

- Frequency: Low | Number: 290 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DeRezObject

- Frequency: Low | Number: 291 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DeRezAck

- Frequency: Low | Number: 292 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RezObject

- Frequency: Low | Number: 293 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RezObjectFromNotecard

- Frequency: Low | Number: 294 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TransferInventory

- Frequency: Low | Number: 295 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TransferInventoryAck

- Frequency: Low | Number: 296 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AcceptFriendship

- Frequency: Low | Number: 297 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DeclineFriendship

- Frequency: Low | Number: 298 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## FormFriendship

- Frequency: Low | Number: 299 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TerminateFriendship

- Frequency: Low | Number: 300 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## OfferCallingCard

- Frequency: Low | Number: 301 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AcceptCallingCard

- Frequency: Low | Number: 302 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DeclineCallingCard

- Frequency: Low | Number: 303 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RezScript

- Frequency: Low | Number: 304 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateInventoryItem

- Frequency: Low | Number: 305 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateLandmarkForEvent

- Frequency: Low | Number: 306 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EventLocationRequest

- Frequency: Low | Number: 307 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EventLocationReply

- Frequency: Low | Number: 308 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionHandleRequest

- Frequency: Low | Number: 309 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RegionIDAndHandleReply

- Frequency: Low | Number: 310 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MoneyTransferRequest

- Frequency: Low | Number: 311 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MoneyTransferBackend

- Frequency: Low | Number: 312 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MoneyBalanceRequest

- Frequency: Low | Number: 313 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MoneyBalanceReply

- Frequency: Low | Number: 314 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RoutedMoneyBalanceReply

- Frequency: Low | Number: 315 | Trust: Trusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ActivateGestures

- Frequency: Low | Number: 316 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DeactivateGestures

- Frequency: Low | Number: 317 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MuteListUpdate

- Frequency: Low | Number: 318 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UseCachedMuteList

- Frequency: Low | Number: 319 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GrantUserRights

- Frequency: Low | Number: 320 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ChangeUserRights

- Frequency: Low | Number: 321 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## OnlineNotification

- Frequency: Low | Number: 322 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## OfflineNotification

- Frequency: Low | Number: 323 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetStartLocationRequest

- Frequency: Low | Number: 324 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetStartLocation

- Frequency: Low | Number: 325 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## NetTest

- Frequency: Low | Number: 326 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetCPURatio

- Frequency: Low | Number: 327 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SimCrashed

- Frequency: Low | Number: 328 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## NameValuePair

- Frequency: Low | Number: 329 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveNameValuePair

- Frequency: Low | Number: 330 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateAttachment

- Frequency: Low | Number: 331 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RemoveAttachment

- Frequency: Low | Number: 332 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SoundTrigger

- Frequency: High | Number: 29 | Trust: NotTrusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AttachedSound

- Frequency: Medium | Number: 13 | Trust: Trusted | Encoding: Unencoded 

- Medium frequency: regular session traffic.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AttachedSoundGainChange

- Frequency: Medium | Number: 14 | Trust: Trusted | Encoding: Unencoded 

- Medium frequency: regular session traffic.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## PreloadSound

- Frequency: Medium | Number: 15 | Trust: Trusted | Encoding: Unencoded 

- Medium frequency: regular session traffic.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectAnimation

- Frequency: High | Number: 30 | Trust: Trusted | Encoding: Unencoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AssetUploadRequest

- Frequency: Low | Number: 333 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AssetUploadComplete

- Frequency: Low | Number: 334 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EmailMessageRequest

- Frequency: Low | Number: 335 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EmailMessageReply

- Frequency: Low | Number: 336 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## InternalScriptMail

- Frequency: Medium | Number: 16 | Trust: Trusted | Encoding: Unencoded 

- Medium frequency: regular session traffic.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptDataRequest

- Frequency: Low | Number: 337 | Trust: Trusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptDataReply

- Frequency: Low | Number: 338 | Trust: Trusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateGroupRequest

- Frequency: Low | Number: 339 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateGroupReply

- Frequency: Low | Number: 340 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateGroupInfo

- Frequency: Low | Number: 341 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupRoleChanges

- Frequency: Low | Number: 342 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## JoinGroupRequest

- Frequency: Low | Number: 343 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## JoinGroupReply

- Frequency: Low | Number: 344 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EjectGroupMemberRequest

- Frequency: Low | Number: 345 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## EjectGroupMemberReply

- Frequency: Low | Number: 346 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LeaveGroupRequest

- Frequency: Low | Number: 347 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LeaveGroupReply

- Frequency: Low | Number: 348 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## InviteGroupRequest

- Frequency: Low | Number: 349 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## InviteGroupResponse

- Frequency: Low | Number: 350 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupProfileRequest

- Frequency: Low | Number: 351 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupProfileReply

- Frequency: Low | Number: 352 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupAccountSummaryRequest

- Frequency: Low | Number: 353 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupAccountSummaryReply

- Frequency: Low | Number: 354 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupAccountDetailsRequest

- Frequency: Low | Number: 355 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupAccountDetailsReply

- Frequency: Low | Number: 356 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupAccountTransactionsRequest

- Frequency: Low | Number: 357 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupAccountTransactionsReply

- Frequency: Low | Number: 358 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupActiveProposalsRequest

- Frequency: Low | Number: 359 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupActiveProposalItemReply

- Frequency: Low | Number: 360 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupVoteHistoryRequest

- Frequency: Low | Number: 361 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupVoteHistoryItemReply

- Frequency: Low | Number: 362 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## StartGroupProposal

- Frequency: Low | Number: 363 | Trust: NotTrusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupProposalBallot

- Frequency: Low | Number: 364 | Trust: NotTrusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## TallyVotes

- Frequency: Low | Number: 365 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupMembersRequest

- Frequency: Low | Number: 366 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupMembersReply

- Frequency: Low | Number: 367 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ActivateGroup

- Frequency: Low | Number: 368 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetGroupContribution

- Frequency: Low | Number: 369 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SetGroupAcceptNotices

- Frequency: Low | Number: 370 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupRoleDataRequest

- Frequency: Low | Number: 371 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupRoleDataReply

- Frequency: Low | Number: 372 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupRoleMembersRequest

- Frequency: Low | Number: 373 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupRoleMembersReply

- Frequency: Low | Number: 374 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupTitlesRequest

- Frequency: Low | Number: 375 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupTitlesReply

- Frequency: Low | Number: 376 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupTitleUpdate

- Frequency: Low | Number: 377 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupRoleUpdate

- Frequency: Low | Number: 378 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LiveHelpGroupRequest

- Frequency: Low | Number: 379 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LiveHelpGroupReply

- Frequency: Low | Number: 380 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentWearablesRequest

- Frequency: Low | Number: 381 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentWearablesUpdate

- Frequency: Low | Number: 382 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentIsNowWearing

- Frequency: Low | Number: 383 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentCachedTexture

- Frequency: Low | Number: 384 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentCachedTextureResponse

- Frequency: Low | Number: 385 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentDataUpdateRequest

- Frequency: Low | Number: 386 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentDataUpdate

- Frequency: Low | Number: 387 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GroupDataUpdate

- Frequency: Low | Number: 388 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentGroupDataUpdate

- Frequency: Low | Number: 389 | Trust: Trusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## AgentDropGroup

- Frequency: Low | Number: 390 | Trust: Trusted | Encoding: Zerocoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LogTextMessage

- Frequency: Low | Number: 391 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ViewerEffect

- Frequency: Medium | Number: 17 | Trust: NotTrusted | Encoding: Zerocoded 

- Medium frequency: regular session traffic.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateTrustedCircuit

- Frequency: Low | Number: 392 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DenyTrustedCircuit

- Frequency: Low | Number: 393 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RequestTrustedCircuit

- Frequency: Low | Number: 394 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RezSingleAttachmentFromInv

- Frequency: Low | Number: 395 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RezMultipleAttachmentsFromInv

- Frequency: Low | Number: 396 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## DetachAttachmentIntoInv

- Frequency: Low | Number: 397 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateNewOutfitAttachments

- Frequency: Low | Number: 398 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UserInfoRequest

- Frequency: Low | Number: 399 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UserInfoReply

- Frequency: Low | Number: 400 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## UpdateUserInfo

- Frequency: Low | Number: 401 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelRename

- Frequency: Low | Number: 402 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## InitiateDownload

- Frequency: Low | Number: 403 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SystemMessage

- Frequency: Low | Number: 404 | Trust: Trusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MapLayerRequest

- Frequency: Low | Number: 405 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MapLayerReply

- Frequency: Low | Number: 406 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MapBlockRequest

- Frequency: Low | Number: 407 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MapNameRequest

- Frequency: Low | Number: 408 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MapBlockReply

- Frequency: Low | Number: 409 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MapItemRequest

- Frequency: Low | Number: 410 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## MapItemReply

- Frequency: Low | Number: 411 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## SendPostcard

- Frequency: Low | Number: 412 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RpcChannelRequest

- Frequency: Low | Number: 413 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RpcChannelReply

- Frequency: Low | Number: 414 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RpcScriptRequestInbound

- Frequency: Low | Number: 415 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RpcScriptRequestInboundForward

- Frequency: Low | Number: 416 | Trust: Trusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RpcScriptReplyInbound

- Frequency: Low | Number: 417 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ScriptMailRegistration

- Frequency: Low | Number: 418 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelMediaCommandMessage

- Frequency: Low | Number: 419 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ParcelMediaUpdate

- Frequency: Low | Number: 420 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LandStatRequest

- Frequency: Low | Number: 421 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LandStatReply

- Frequency: Low | Number: 422 | Trust: Trusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## Error

- Frequency: Low | Number: 423 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## ObjectIncludeInSearch

- Frequency: Low | Number: 424 | Trust: NotTrusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RezRestoreToWorld

- Frequency: Low | Number: 425 | Trust: NotTrusted | Encoding: Unencoded UDPDeprecated

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Flags: UDPDeprecated. Treat deprecated or blacklisted messages as do-not-send for new code.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## LinkInventoryItem

- Frequency: Low | Number: 426 | Trust: NotTrusted | Encoding: Zerocoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## RetrieveIMsExtended

- Frequency: Low | Number: 427 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## JoinGroupRequestExtended

- Frequency: Low | Number: 428 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## CreateGroupRequestExtended

- Frequency: Low | Number: 429 | Trust: Trusted | Encoding: Unencoded 

- Low frequency: the bulk of the protocol. Most feature messages live here.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.


## GameControlInput

- Frequency: High | Number: 32 | Trust: NotTrusted | Encoding: Zerocoded 

- High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.

- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.

- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.
