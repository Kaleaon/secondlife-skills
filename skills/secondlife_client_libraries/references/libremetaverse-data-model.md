# LibreMetaverse Data Model Reference (generated from cinderblocks/libremetaverse)

Every public class, struct, record, and enum in LibreMetaverse.Protocol, LibreMetaverse.Types, and LibreMetaverse.Assets, with its public fields. This is the data model a port must reproduce: packet records, login data, asset types, prim and inventory structures.

Types catalogued: 514.


## AgentDisplayName (class) — LibreMetaverse.Protocol/AgentDisplayName.cs

- `UUID ID`

- `string? UserName`

- `string? DisplayName`

- `string? LegacyFirstName`

- `string? LegacyLastName`

- `string LegacyFullName`

- `bool IsDefaultDisplayName`

- `DateTime NextUpdate`

- `DateTime Updated`


## TeleportFlags (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## InstantMessageOnline (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## InstantMessageDialog (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## PointAtType (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## EffectType (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## ChatType (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## ChatAudibleLevel (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## AgentState (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## AgentFlags (enum) — LibreMetaverse.Protocol/AgentEnums.cs


## ScriptPermission (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## ChatSourceType (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## MoneyTransactionType (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## TransactionFlags (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## MeanCollisionType (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## ScriptControlChange (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## TeleportStatus (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## TeleportLureFlags (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## ScriptSensorTypeFlags (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## MuteType (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## MuteFlags (enum) — LibreMetaverse.Protocol/AgentRecords.cs


## InstantMessage (struct) — LibreMetaverse.Protocol/AgentRecords.cs

- `UUID FromAgentID`

- `string FromAgentName`

- `UUID ToAgentID`

- `uint ParentEstateID`

- `UUID RegionID`

- `Vector3 Position`

- `InstantMessageDialog Dialog`

- `bool GroupIM`

- `UUID IMSessionID`

- `DateTime Timestamp`

- `string Message`

- `InstantMessageOnline Offline`

- `byte[] BinaryBucket`


## MuteEntry (class) — LibreMetaverse.Protocol/AgentRecords.cs

- `MuteType Type`

- `UUID ID`

- `string Name`

- `MuteFlags Flags`


## TransactionInfo (class) — LibreMetaverse.Protocol/AgentRecords.cs

- `int TransactionType`

- `UUID SourceID`

- `bool IsSourceGroup`

- `UUID DestID`

- `bool IsDestGroup`

- `int Amount`

- `string ItemDescription`


## Animations (class) — LibreMetaverse.Protocol/Animations.cs

- `UUID AFRAID`

- `UUID AIM_BAZOOKA_R`

- `UUID AIM_BOW_L`

- `UUID AIM_HANDGUN_R`

- `UUID AIM_RIFLE_R`

- `UUID ANGRY`

- `UUID AWAY`

- `UUID BACKFLIP`

- `UUID BELLY_LAUGH`

- `UUID BLOW_KISS`

- `UUID BORED`

- `UUID BOW`

- `UUID BRUSH`

- `UUID BUSY`

- `UUID CLAP`

- `UUID COURTBOW`

- `UUID CROUCH`

- `UUID CROUCHWALK`

- `UUID CRY`

- `UUID CUSTOMIZE`

- `UUID CUSTOMIZE_DONE`

- `UUID DANCE1`

- `UUID DANCE2`

- `UUID DANCE3`

- `UUID DANCE4`

- `UUID DANCE5`

- `UUID DANCE6`

- `UUID DANCE7`

- `UUID DANCE8`

- `UUID DEAD`

- `UUID DRINK`

- `UUID EMBARRASSED`

- `UUID EXPRESS_AFRAID`

- `UUID EXPRESS_ANGER`

- `UUID EXPRESS_BORED`

- `UUID EXPRESS_CRY`

- `UUID EXPRESS_DISDAIN`

- `UUID EXPRESS_EMBARRASSED`


## TargetType (enum) — LibreMetaverse.Protocol/AssetEnums.cs


## SourceType (enum) — LibreMetaverse.Protocol/AssetEnums.cs


## ImageType (enum) — LibreMetaverse.Protocol/AssetEnums.cs


## ImageCodec (enum) — LibreMetaverse.Protocol/AssetEnums.cs


## ChannelType (enum) — LibreMetaverse.Protocol/AssetEnums.cs


## EstateAssetType (enum) — LibreMetaverse.Protocol/AssetTransferEnums.cs


## StatusCode (enum) — LibreMetaverse.Protocol/AssetTransferEnums.cs


## TransferError (enum) — LibreMetaverse.Protocol/AssetTransferEnums.cs


## ProfileFlags (enum) — LibreMetaverse.Protocol/AvatarEnums.cs


## AvatarGroup (struct) — LibreMetaverse.Protocol/AvatarRecords.cs

- `bool AcceptNotices`

- `UUID GroupID`

- `UUID GroupInsigniaID`

- `string GroupName`

- `GroupPowers GroupPowers`

- `string GroupTitle`

- `bool ListInProfile`


## ProfilePick (struct) — LibreMetaverse.Protocol/AvatarRecords.cs

- `UUID PickID`

- `UUID CreatorID`

- `bool TopPick`

- `UUID ParcelID`

- `string Name`

- `string Desc`

- `UUID SnapshotID`

- `string User`

- `string OriginalName`

- `string SimName`

- `Vector3d PosGlobal`

- `int SortOrder`

- `bool Enabled`


## ClassifiedAd (struct) — LibreMetaverse.Protocol/AvatarRecords.cs

- `UUID ClassifiedID`

- `UUID CreatorID`

- `uint CreationDate`

- `uint ExpirationDate`

- `uint Category`

- `UUID ParcelID`

- `uint ParentEstate`

- `UUID SnapShotID`

- `Vector3d Position`

- `string SimName`

- `string ParcelName`

- `byte ClassifiedFlags`

- `int Price`

- `string Name`

- `string Desc`


## Packet (class) — LibreMetaverse.Protocol/CapsToPacket.cs


## EnvironmentTrack (enum) — LibreMetaverse.Protocol/EnvironmentEnums.cs


## EstateTask (class) — LibreMetaverse.Protocol/EstateRecords.cs

- `Vector3 Position`

- `float Score`

- `float MonoScore`

- `UUID TaskID`

- `uint TaskLocalID`

- `string TaskName`

- `string OwnerName`


## RegionRestartDays (enum) — LibreMetaverse.Protocol/EstateRecords.cs


## RegionRestartSchedule (class) — LibreMetaverse.Protocol/EstateRecords.cs

- `bool IsDaily`

- `RegionRestartDays Days`

- `TimeSpan Time`


## FriendRights (enum) — LibreMetaverse.Protocol/FriendRecords.cs


## FriendInfo (class) — LibreMetaverse.Protocol/FriendRecords.cs

- `UUID UUID`

- `string Name`

- `bool IsOnline`

- `bool CanSeeMeOnline`

- `bool CanSeeMeOnMap`

- `bool CanModifyMyObjects`

- `bool CanSeeThemOnline`

- `bool CanSeeThemOnMap`

- `bool CanModifyTheirObjects`

- `FriendRights TheirFriendRights`

- `FriendRights MyFriendRights`


## GridLayerType (enum) — LibreMetaverse.Protocol/GridEnums.cs


## GridItemType (enum) — LibreMetaverse.Protocol/GridEnums.cs


## GridRegion (struct) — LibreMetaverse.Protocol/GridRecords.cs

- `int X`

- `int Y`

- `string Name`

- `SimAccess Access`

- `RegionFlags RegionFlags`

- `byte WaterHeight`

- `byte Agents`

- `UUID MapImageID`

- `ulong RegionHandle`

- `struct GridLayer`

- `int Bottom`

- `int Left`

- `int Top`

- `int Right`

- `UUID ImageID`


## GridLayer (struct) — LibreMetaverse.Protocol/GridRecords.cs

- `int Bottom`

- `int Left`

- `int Top`

- `int Right`

- `UUID ImageID`


## GroupPowers (enum) — LibreMetaverse.Protocol/GroupEnums.cs


## GroupMember (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `UUID ID`

- `int Contribution`

- `string OnlineStatus`

- `GroupPowers Powers`

- `string Title`

- `bool IsOwner`


## GroupRole (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `UUID GroupID`

- `UUID ID`

- `string Name`

- `string Title`

- `string Description`

- `GroupPowers Powers`

- `uint Members`


## GroupTitle (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `UUID GroupID`

- `UUID RoleID`

- `string Title`

- `bool Selected`


## Group (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `UUID ID`

- `UUID InsigniaID`

- `UUID FounderID`

- `UUID OwnerRole`

- `string Name`

- `string Charter`

- `string MemberTitle`

- `bool OpenEnrollment`

- `bool ShowInList`

- `GroupPowers Powers`

- `bool AcceptNotices`

- `bool AllowPublish`

- `bool MaturePublish`

- `int MembershipFee`

- `int Money`

- `int Contribution`

- `int GroupMembershipCount`

- `int GroupRolesCount`

- `bool ListInProfile`


## Vote (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `UUID Candidate`

- `string VoteString`

- `int NumVotes`


## GroupProposal (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `string VoteText`

- `int Quorum`

- `float Majority`

- `int Duration`


## GroupVoteMajority (class) — LibreMetaverse.Protocol/GroupRecords.cs

- `float SimpleMajority`

- `float TwoThirdsMajority`

- `float Unanimous`


## GroupRoleChangeType (enum) — LibreMetaverse.Protocol/GroupRecords.cs


## GroupAccountSummary (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `int IntervalDays`

- `int CurrentInterval`

- `string StartDate`

- `int Balance`

- `int TotalCredits`

- `int TotalDebits`

- `int ObjectTaxCurrent`

- `int LightTaxCurrent`

- `int LandTaxCurrent`

- `int GroupTaxCurrent`

- `int ParcelDirFeeCurrent`

- `int ObjectTaxEstimate`

- `int LightTaxEstimate`

- `int LandTaxEstimate`

- `int GroupTaxEstimate`

- `int ParcelDirFeeEstimate`

- `int NonExemptMembers`

- `string LastTaxDate`

- `string TaxDate`


## GroupNotice (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `string Subject`

- `string Message`

- `UUID AttachmentID`

- `UUID OwnerID`


## GroupNoticesListEntry (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `UUID NoticeID`

- `uint Timestamp`

- `string FromName`

- `string Subject`

- `bool HasAttachment`

- `AssetType AssetType`


## ChatSessionMember (struct) — LibreMetaverse.Protocol/GroupRecords.cs

- `UUID AvatarKey`

- `bool CanVoiceChat`

- `bool IsModerator`

- `bool MuteText`

- `bool MuteVoice`


## GroupRoleUpdate (enum) — LibreMetaverse.Protocol/GroupRecords.cs


## GroupBanAction (enum) — LibreMetaverse.Protocol/GroupRecords.cs


## CompressedFlags (enum) — LibreMetaverse.Protocol/ObjectEnums.cs


## ReportType (enum) — LibreMetaverse.Protocol/ObjectRecordEnums.cs


## UpdateType (enum) — LibreMetaverse.Protocol/ObjectRecordEnums.cs


## PayPriceType (enum) — LibreMetaverse.Protocol/ObjectRecordEnums.cs


## PacketFrequency (enum) — LibreMetaverse.Protocol/Packet.cs


## MalformedDataException (class) — LibreMetaverse.Protocol/Packet.cs


## Header (struct) — LibreMetaverse.Protocol/Packet.cs

- `bool Reliable`

- `bool Resent`

- `bool Zerocoded`

- `bool AppendedAcks`

- `uint Sequence`

- `ushort ID`

- `PacketFrequency Frequency`

- `uint[]? AckList`


## PacketBlock (class) — LibreMetaverse.Protocol/Packet.cs


## PacketDecoder (class) — LibreMetaverse.Protocol/PacketDecoder.cs


## Parcel (class) — LibreMetaverse.Protocol/Parcel.cs

- `int SelfCount`

- `int OtherCount`

- `int PublicCount`

- `int LocalID`

- `UUID OwnerID`

- `bool IsGroupOwned`

- `uint AuctionID`

- `DateTime ClaimDate`

- `int ClaimPrice`

- `int RentPrice`

- `Vector3 AABBMin`

- `Vector3 AABBMax`

- `byte[] Bitmap`

- `int Area`

- `ParcelStatus Status`

- `int SimWideMaxPrims`

- `int SimWideTotalPrims`

- `int MaxPrims`

- `int TotalPrims`

- `int OwnerPrims`

- `int GroupPrims`

- `int OtherPrims`

- `float ParcelPrimBonus`

- `int OtherCleanTime`

- `ParcelFlags Flags`

- `int SalePrice`

- `string Name`

- `string Desc`

- `string MusicURL`

- `UUID GroupID`

- `int PassPrice`

- `float PassHours`

- `ParcelCategory Category`

- `UUID AuthBuyerID`

- `UUID SnapshotID`

- `Vector3 UserLocation`

- `Vector3 UserLookAt`

- `LandingType Landing`

- `float Dwell`

- `bool RegionDenyAnonymous`

- `bool RegionPushOverride`

- `List<ParcelAccessEntry> AccessWhiteList`

- `List<ParcelAccessEntry> AccessBlackList`

- `bool RegionDenyAgeUnverified`

- `bool ObscureMedia`

- `bool ObscureMusic`

- `ParcelMedia Media`

- `bool SeeAVs`

- `bool AnyAVSounds`


## ParcelStatus (enum) — LibreMetaverse.Protocol/ParcelEnums.cs


## ParcelResult (enum) — LibreMetaverse.Protocol/ParcelEnums.cs


## ParcelFlags (enum) — LibreMetaverse.Protocol/ParcelEnums.cs


## ParcelCategory (enum) — LibreMetaverse.Protocol/ParcelEnums.cs


## LandingType (enum) — LibreMetaverse.Protocol/ParcelEnums.cs


## AccessList (enum) — LibreMetaverse.Protocol/ParcelEnums.cs


## ObjectReturnType (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## ParcelAccessFlags (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## ParcelPropertiesStatus (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## TerraformAction (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## TerraformBrushSize (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## AccessDeniedReason (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## ParcelOverlayType (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## ParcelMediaCommand (enum) — LibreMetaverse.Protocol/ParcelRecords.cs


## ParcelInfo (struct) — LibreMetaverse.Protocol/ParcelRecords.cs

- `UUID ID`

- `UUID OwnerID`

- `string Name`

- `string Description`

- `int ActualArea`

- `int BillableArea`

- `bool Mature`

- `float GlobalX`

- `float GlobalY`

- `float GlobalZ`

- `string SimName`

- `UUID SnapshotID`

- `float Dwell`

- `int SalePrice`

- `int AuctionID`


## ParcelMedia (struct) — LibreMetaverse.Protocol/ParcelRecords.cs

- `bool MediaAutoScale`

- `bool MediaLoop`

- `UUID MediaID`

- `string MediaURL`

- `string MediaDesc`

- `int MediaHeight`

- `int MediaWidth`

- `string MediaType`


## ParcelAccessEntry (struct) — LibreMetaverse.Protocol/ParcelRecords.cs

- `UUID AgentID`

- `DateTime Time`

- `AccessList Flags`


## ParcelPrimOwners (struct) — LibreMetaverse.Protocol/ParcelRecords.cs

- `UUID OwnerID`

- `bool IsGroupOwned`

- `int Count`

- `bool OnlineStatus`

- `DateTime NewestPrim`


## RegionFlags (enum) — LibreMetaverse.Protocol/RegionEnums.cs


## SimAccess (enum) — LibreMetaverse.Protocol/RegionEnums.cs


## RegionProtocols (enum) — LibreMetaverse.Protocol/RegionProtocols.cs


## TerrainPatch (class) — LibreMetaverse.Protocol/TerrainCompressor.cs

- `struct GroupHeader`

- `int Stride`

- `int PatchSize`

- `LayerType Type`

- `struct Header`

- `float DCOffset`

- `int Range`

- `int QuantWBits`

- `int PatchIDs`

- `uint WordBits`

- `bool LargeRegion`

- `int X`

- `int Y`

- `float[] Data`


## LayerType (enum) — LibreMetaverse.Protocol/TerrainCompressor.cs

- `struct GroupHeader`

- `int Stride`

- `int PatchSize`

- `LayerType Type`

- `struct Header`

- `float DCOffset`

- `int Range`

- `int QuantWBits`

- `int PatchIDs`

- `uint WordBits`

- `bool LargeRegion`

- `int X`

- `int Y`

- `float[] Data`


## GroupHeader (struct) — LibreMetaverse.Protocol/TerrainCompressor.cs

- `int Stride`

- `int PatchSize`

- `LayerType Type`

- `struct Header`

- `float DCOffset`

- `int Range`

- `int QuantWBits`

- `int PatchIDs`

- `uint WordBits`

- `bool LargeRegion`

- `int X`

- `int Y`

- `float[] Data`


## Header (struct) — LibreMetaverse.Protocol/TerrainCompressor.cs

- `float DCOffset`

- `int Range`

- `int QuantWBits`

- `int PatchIDs`

- `uint WordBits`

- `bool LargeRegion`

- `int X`

- `int Y`

- `float[] Data`


## TerrainCompressor (class) — LibreMetaverse.Protocol/TerrainCompressor.cs

- `int PATCHES_PER_EDGE`

- `int END_OF_PATCHES`


## AccountLevelBenefits (class) — LibreMetaverse.Protocol/Login/AccountLevelBenefits.cs

- `int MeshUploadCost`

- `int OneTimeEventAllowed`

- `int RepeatingEventsCost`

- `string EstateAccessToken`

- `int LastnameChangeRate`

- `int MarketplaceConciergeSupport`

- `int PhoneSupport`

- `double LindenBuyFee`

- `int PartnerFee`

- `int CreateRepeatingEvents`

- `int TextureUploadCost`

- `int PriorityEntry`

- `int ObjectAccountLevel`

- `int UseAnimesh`

- `double LastnameChangeCost`

- `int BetaGridLand`

- `int CreateGroupCost`

- `int LiveChat`

- `int LandAuctionsAllowed`

- `int MainlandTier`

- `int LocalExperiences`

- `int OneTimeEventCost`

- `int MarketplacePleLimit`

- `int UnpartnerFee`

- `int GroupMembershipLimit`

- `int AnimationUploadCost`

- `int ScriptLimit`

- `int TransactionHistoryLimit`

- `List<int> LargeTextureUploadCost`

- `int AnimatedObjectLimit`

- `int GridwideExperienceLimit`

- `int LastnameChangeAllowed`

- `int SoundUploadCost`

- `int PremiumAlts`

- `int PicksLimit`

- `int PlacePages`

- `int PremiumAccess`

- `int MarketplaceListingLimit`

- `int PremiumGifts`

- `int VoiceMorphing`

- `int StoredImLimit`

- `int Stipend`

- `int SignupBonus`

- `int AttachmentLimit`


## LoginRequest (class) — LibreMetaverse.Protocol/Login/LoginRequest.cs

- `string FirstName`

- `string LastName`

- `string Password`

- `string Start`

- `string Channel`

- `string Version`

- `string Platform`

- `string PlatformVersion`

- `string Mac`

- `string ViewerDigest`

- `string Id0`

- `bool AgreeToTos`

- `bool ReadCritical`

- `LastExecStatus LastExecEvent`

- `bool HasMfa`

- `string Token`

- `string MfaHash`

- `List<string> Options`

- `int MaxPasswordLength`


## LoginState (enum) — LibreMetaverse.Protocol/Login/LoginResponseData.cs


## LoginResponseData (class) — LibreMetaverse.Protocol/Login/LoginResponseData.cs

- `enum ParseMessageLevel`

- `class ParseMessage`

- `ParseMessageLevel Level`

- `string Message`

- `Exception? Exception`

- `class ParseResult`

- `bool Success`

- `IReadOnlyList<ParseMessage> Messages`

- `LoginResponseData? ParsedData`

- `LoginState Login`

- `string Reason`

- `bool FirstLogin`

- `UUID AgentID`

- `UUID SessionID`

- `UUID SecureSessionID`

- `string MfaHash`

- `string FirstName`

- `string LastName`

- `string StartLocation`

- `string AccountType`

- `string AgentAccess`

- `string AgentAccessMax`

- `string AgentRegionAccess`

- `string InitialOutfit`

- `Vector3 LookAt`

- `HomeInfo Home`

- `int CircuitCode`

- `uint RegionX`

- `uint RegionY`

- `uint RegionSizeX`

- `uint RegionSizeY`

- `ushort SimPort`

- `IPAddress? SimIP`

- `string SeedCapability`

- `BuddyListEntry[] BuddyList`

- `int SecondsSinceEpoch`

- `string UDPBlacklist`

- `int MaxAgentGroups`

- `string OpenIDUrl`

- `string AgentAppearanceServiceURL`

- `string MapServerUrl`

- `string SnapshotConfigUrl`

- `uint COFVersion`

- `AccountLevelBenefits? AccountLevelBenefits`

- `List<object> ClassifiedCategories`

- `List<object> EventCategories`

- `List<object> GlobalTextures`

- `List<object> UiConfig`


## ParseMessageLevel (enum) — LibreMetaverse.Protocol/Login/LoginResponseData.cs

- `class ParseMessage`

- `ParseMessageLevel Level`

- `string Message`

- `Exception? Exception`

- `class ParseResult`

- `bool Success`

- `IReadOnlyList<ParseMessage> Messages`

- `LoginResponseData? ParsedData`

- `LoginState Login`

- `string Reason`

- `bool FirstLogin`

- `UUID AgentID`

- `UUID SessionID`

- `UUID SecureSessionID`

- `string MfaHash`

- `string FirstName`

- `string LastName`

- `string StartLocation`

- `string AccountType`

- `string AgentAccess`

- `string AgentAccessMax`

- `string AgentRegionAccess`

- `string InitialOutfit`

- `Vector3 LookAt`

- `HomeInfo Home`

- `int CircuitCode`

- `uint RegionX`

- `uint RegionY`

- `uint RegionSizeX`

- `uint RegionSizeY`

- `ushort SimPort`

- `IPAddress? SimIP`

- `string SeedCapability`

- `BuddyListEntry[] BuddyList`

- `int SecondsSinceEpoch`

- `string UDPBlacklist`

- `int MaxAgentGroups`

- `string OpenIDUrl`

- `string AgentAppearanceServiceURL`

- `string MapServerUrl`

- `string SnapshotConfigUrl`

- `uint COFVersion`

- `AccountLevelBenefits? AccountLevelBenefits`

- `List<object> ClassifiedCategories`

- `List<object> EventCategories`

- `List<object> GlobalTextures`

- `List<object> UiConfig`

- `UUID InventoryRoot`


## ParseMessage (class) — LibreMetaverse.Protocol/Login/LoginResponseData.cs

- `ParseMessageLevel Level`

- `string Message`

- `Exception? Exception`

- `class ParseResult`

- `bool Success`

- `IReadOnlyList<ParseMessage> Messages`

- `LoginResponseData? ParsedData`

- `LoginState Login`

- `string Reason`

- `bool FirstLogin`

- `UUID AgentID`

- `UUID SessionID`

- `UUID SecureSessionID`

- `string MfaHash`

- `string FirstName`

- `string LastName`

- `string StartLocation`

- `string AccountType`

- `string AgentAccess`

- `string AgentAccessMax`

- `string AgentRegionAccess`

- `string InitialOutfit`

- `Vector3 LookAt`

- `HomeInfo Home`

- `int CircuitCode`

- `uint RegionX`

- `uint RegionY`

- `uint RegionSizeX`

- `uint RegionSizeY`

- `ushort SimPort`

- `IPAddress? SimIP`

- `string SeedCapability`

- `BuddyListEntry[] BuddyList`

- `int SecondsSinceEpoch`

- `string UDPBlacklist`

- `int MaxAgentGroups`

- `string OpenIDUrl`

- `string AgentAppearanceServiceURL`

- `string MapServerUrl`

- `string SnapshotConfigUrl`

- `uint COFVersion`

- `AccountLevelBenefits? AccountLevelBenefits`

- `List<object> ClassifiedCategories`

- `List<object> EventCategories`

- `List<object> GlobalTextures`

- `List<object> UiConfig`

- `UUID InventoryRoot`

- `UUID LibraryRoot`

- `InventoryFolder[] InventorySkeleton`

- `InventoryFolder[] LibrarySkeleton`


## ParseResult (class) — LibreMetaverse.Protocol/Login/LoginResponseData.cs

- `bool Success`

- `IReadOnlyList<ParseMessage> Messages`

- `LoginResponseData? ParsedData`

- `LoginState Login`

- `string Reason`

- `string Message`

- `bool FirstLogin`

- `UUID AgentID`

- `UUID SessionID`

- `UUID SecureSessionID`

- `string MfaHash`

- `string FirstName`

- `string LastName`

- `string StartLocation`

- `string AccountType`

- `string AgentAccess`

- `string AgentAccessMax`

- `string AgentRegionAccess`

- `string InitialOutfit`

- `Vector3 LookAt`

- `HomeInfo Home`

- `int CircuitCode`

- `uint RegionX`

- `uint RegionY`

- `uint RegionSizeX`

- `uint RegionSizeY`

- `ushort SimPort`

- `IPAddress? SimIP`

- `string SeedCapability`

- `BuddyListEntry[] BuddyList`

- `int SecondsSinceEpoch`

- `string UDPBlacklist`

- `int MaxAgentGroups`

- `string OpenIDUrl`

- `string AgentAppearanceServiceURL`

- `string MapServerUrl`

- `string SnapshotConfigUrl`

- `uint COFVersion`

- `AccountLevelBenefits? AccountLevelBenefits`

- `List<object> ClassifiedCategories`

- `List<object> EventCategories`

- `List<object> GlobalTextures`

- `List<object> UiConfig`

- `UUID InventoryRoot`

- `UUID LibraryRoot`

- `InventoryFolder[] InventorySkeleton`

- `InventoryFolder[] LibrarySkeleton`

- `UUID LibraryOwner`

- `string NextMethod`

- `string NextUrl`

- `string[] NextOptions`

- `int NextDuration`

- `string AgentId`

- `string SessionId`

- `string SecureSessionId`


## HomeInfo (class) — LibreMetaverse.Protocol/Login/LoginResponseData.cs

- `string Key`

- `string Home`

- `string Position`

- `string RegionHandle`

- `string LookAt`


## LastExecStatus (enum) — LibreMetaverse.Protocol/Login/LoginTypes.cs


## BuddyListEntry (struct) — LibreMetaverse.Protocol/Login/LoginTypes.cs

- `int BuddyRightsGiven`

- `string BuddyId`

- `int BuddyRightsHas`


## HomeInfo (class) — LibreMetaverse.Protocol/Login/LoginTypes.cs

- `ulong RegionHandle`

- `Vector3 Position`

- `Vector3 LookAt`


## LoginException (class) — LibreMetaverse.Protocol/Login/LoginTypes.cs


## TeleportFinishMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AgentID`

- `int LocationID`

- `ulong RegionHandle`

- `Uri SeedCapability`

- `SimAccess SimAccess`

- `IPAddress IP`

- `int Port`

- `TeleportFlags Flags`

- `uint RegionSizeX`

- `uint RegionSizeY`


## NavMeshStatusUpdateMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `OSDMap RawData`

- `UUID RegionID`

- `string Status`

- `uint Version`


## EstablishAgentCommunicationMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AgentID`

- `IPAddress Address`

- `int Port`

- `Uri SeedCapability`


## CrossedRegionMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `Vector3 LookAt`

- `Vector3 Position`

- `UUID AgentID`

- `UUID SessionID`

- `ulong RegionHandle`

- `Uri SeedCapability`

- `IPAddress IP`

- `int Port`

- `uint RegionSizeX`

- `uint RegionSizeY`


## EnableSimulatorMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class SimulatorInfoBlock`

- `ulong RegionHandle`

- `IPAddress IP`

- `int Port`

- `uint RegionSizeX`

- `uint RegionSizeY`

- `SimulatorInfoBlock[] Simulators`


## SimulatorInfoBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `ulong RegionHandle`

- `IPAddress IP`

- `int Port`

- `uint RegionSizeX`

- `uint RegionSizeY`

- `SimulatorInfoBlock[] Simulators`


## TeleportFailedMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string ExtraParams`

- `string MessageKey`

- `UUID AgentID`

- `string Reason`


## LandStatReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `uint ReportType`

- `uint RequestFlags`

- `uint TotalObjectCount`

- `class ReportDataBlock`

- `Vector3 Location`

- `string OwnerName`

- `float Score`

- `UUID TaskID`

- `uint TaskLocalID`

- `string TaskName`

- `float MonoScore`

- `DateTime TimeStamp`

- `ReportDataBlock[] ReportDataBlocks`


## ReportDataBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `Vector3 Location`

- `string OwnerName`

- `float Score`

- `UUID TaskID`

- `uint TaskLocalID`

- `string TaskName`

- `float MonoScore`

- `DateTime TimeStamp`

- `ReportDataBlock[] ReportDataBlocks`


## ParcelObjectOwnersReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class PrimOwner`

- `UUID OwnerID`

- `int Count`

- `bool IsGroupOwned`

- `bool OnlineStatus`

- `DateTime TimeStamp`

- `PrimOwner[] PrimOwnersBlock`


## PrimOwner (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID OwnerID`

- `int Count`

- `bool IsGroupOwned`

- `bool OnlineStatus`

- `DateTime TimeStamp`

- `PrimOwner[] PrimOwnersBlock`


## ParcelPropertiesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int LocalID`

- `Vector3 AABBMax`

- `Vector3 AABBMin`

- `int Area`

- `uint AuctionID`

- `UUID AuthBuyerID`

- `byte[] Bitmap`

- `ParcelCategory Category`

- `DateTime ClaimDate`

- `int ClaimPrice`

- `string Desc`

- `ParcelFlags ParcelFlags`

- `UUID GroupID`

- `int GroupPrims`

- `bool IsGroupOwned`

- `LandingType LandingType`

- `int MaxPrims`

- `UUID MediaID`

- `string MediaURL`

- `bool MediaAutoScale`

- `string MusicURL`

- `string Name`

- `int OtherCleanTime`

- `int OtherCount`

- `int OtherPrims`

- `UUID OwnerID`

- `int OwnerPrims`

- `float ParcelPrimBonus`

- `float PassHours`

- `int PassPrice`

- `int PublicCount`

- `bool Privacy`

- `bool RegionDenyAnonymous`

- `bool RegionDenyIdentified`

- `bool RegionDenyTransacted`

- `bool RegionDenyAgeUnverified`

- `bool RegionPushOverride`

- `int RentPrice`

- `ParcelResult RequestResult`

- `int SalePrice`

- `int SelectedPrims`

- `int SelfCount`

- `int SequenceID`

- `int SimWideMaxPrims`

- `int SimWideTotalPrims`

- `bool SnapSelection`

- `UUID SnapshotID`

- `ParcelStatus Status`

- `int TotalPrims`

- `Vector3 UserLocation`

- `Vector3 UserLookAt`

- `string MediaDesc`

- `int MediaHeight`

- `int MediaWidth`

- `bool MediaLoop`


## ParcelPropertiesUpdateMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AuthBuyerID`

- `bool MediaAutoScale`

- `ParcelCategory Category`

- `string Desc`

- `UUID GroupID`

- `LandingType Landing`

- `int LocalID`

- `string MediaDesc`

- `int MediaHeight`

- `bool MediaLoop`

- `UUID MediaID`

- `string MediaType`

- `string MediaURL`

- `int MediaWidth`

- `string MusicURL`

- `string Name`

- `bool ObscureMedia`

- `bool ObscureMusic`

- `ParcelFlags ParcelFlags`

- `float PassHours`

- `uint PassPrice`

- `bool Privacy`

- `uint SalePrice`

- `UUID SnapshotID`

- `Vector3 UserLocation`

- `Vector3 UserLookAt`

- `bool SeeAVs`

- `bool AnyAVSounds`

- `bool GroupAVSounds`


## RemoteParcelRequestBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## RemoteParcelRequestRequest (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `Vector3 Location`

- `ulong RegionHandle`

- `UUID RegionID`


## RemoteParcelRequestReply (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ParcelID`


## RemoteParcelRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `RemoteParcelRequestBlock Request`


## NewFileAgentInventoryMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID FolderID`

- `AssetType AssetType`

- `InventoryType InventoryType`

- `string Name`

- `string Description`

- `PermissionMask EveryoneMask`

- `PermissionMask GroupMask`

- `PermissionMask NextOwnerMask`


## NewFileAgentInventoryReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string State`

- `Uri Uploader`


## NewFileAgentInventoryVariablePriceMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID FolderID`

- `AssetType AssetType`

- `InventoryType InventoryType`

- `string Name`

- `string Description`

- `PermissionMask EveryoneMask`

- `PermissionMask GroupMask`

- `PermissionMask NextOwnerMask`


## NewFileAgentInventoryVariablePriceReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int ResourceCost`

- `string State`

- `int UploadPrice`

- `Uri Rsvp`


## NewFileAgentInventoryUploadReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID NewInventoryItem`

- `UUID NewAsset`

- `string State`

- `PermissionMask NewBaseMask`

- `PermissionMask NewEveryoneMask`

- `PermissionMask NewOwnerMask`

- `PermissionMask NewNextOwnerMask`


## BulkUpdateInventoryMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class FolderDataInfo`

- `UUID FolderID`

- `UUID ParentID`

- `string Name`

- `FolderType Type`

- `class ItemDataInfo`

- `UUID ItemID`

- `uint CallbackID`

- `UUID CreatorID`

- `UUID OwnerID`

- `UUID GroupID`

- `PermissionMask BaseMask`

- `PermissionMask OwnerMask`

- `PermissionMask GroupMask`

- `PermissionMask EveryoneMask`

- `PermissionMask NextOwnerMask`

- `bool GroupOwned`

- `UUID AssetID`

- `InventoryType InvType`

- `uint Flags`

- `SaleType SaleType`

- `int SalePrice`

- `string Description`

- `DateTime CreationDate`

- `uint CRC`

- `UUID AgentID`

- `UUID TransactionID`

- `FolderDataInfo[] FolderData`

- `ItemDataInfo[] ItemData`


## FolderDataInfo (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID FolderID`

- `UUID ParentID`

- `string Name`

- `FolderType Type`

- `class ItemDataInfo`

- `UUID ItemID`

- `uint CallbackID`

- `UUID CreatorID`

- `UUID OwnerID`

- `UUID GroupID`

- `PermissionMask BaseMask`

- `PermissionMask OwnerMask`

- `PermissionMask GroupMask`

- `PermissionMask EveryoneMask`

- `PermissionMask NextOwnerMask`

- `bool GroupOwned`

- `UUID AssetID`

- `InventoryType InvType`

- `uint Flags`

- `SaleType SaleType`

- `int SalePrice`

- `string Description`

- `DateTime CreationDate`

- `uint CRC`

- `UUID AgentID`

- `UUID TransactionID`

- `FolderDataInfo[] FolderData`

- `ItemDataInfo[] ItemData`


## ItemDataInfo (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ItemID`

- `uint CallbackID`

- `UUID FolderID`

- `UUID CreatorID`

- `UUID OwnerID`

- `UUID GroupID`

- `PermissionMask BaseMask`

- `PermissionMask OwnerMask`

- `PermissionMask GroupMask`

- `PermissionMask EveryoneMask`

- `PermissionMask NextOwnerMask`

- `bool GroupOwned`

- `UUID AssetID`

- `AssetType Type`

- `InventoryType InvType`

- `uint Flags`

- `SaleType SaleType`

- `int SalePrice`

- `string Name`

- `string Description`

- `DateTime CreationDate`

- `uint CRC`

- `UUID AgentID`

- `UUID TransactionID`

- `FolderDataInfo[] FolderData`

- `ItemDataInfo[] ItemData`


## AgentGroupDataUpdateMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AgentID`

- `UUID AvatarID`

- `class GroupData`

- `bool AcceptNotices`

- `int Contribution`

- `UUID GroupID`

- `UUID GroupInsigniaID`

- `string GroupTitle`

- `string GroupName`

- `GroupPowers GroupPowers`

- `class NewGroupData`

- `bool ListInProfile`

- `GroupData[] GroupDataBlock`

- `NewGroupData[] NewGroupDataBlock`


## GroupData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `bool AcceptNotices`

- `int Contribution`

- `UUID GroupID`

- `UUID GroupInsigniaID`

- `string GroupTitle`

- `string GroupName`

- `GroupPowers GroupPowers`

- `class NewGroupData`

- `bool ListInProfile`

- `GroupData[] GroupDataBlock`

- `NewGroupData[] NewGroupDataBlock`


## NewGroupData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `bool ListInProfile`

- `GroupData[] GroupDataBlock`

- `NewGroupData[] NewGroupDataBlock`


## UpdateAgentLanguageMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Language`

- `bool LanguagePublic`


## AgentDropGroupMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class AgentData`

- `UUID AgentID`

- `UUID GroupID`

- `AgentData[] AgentDataBlock`


## AgentData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AgentID`

- `UUID GroupID`

- `AgentData[] AgentDataBlock`


## AgentStateUpdateMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `OSDMap RawData`

- `bool CanModifyNavmesh`

- `bool HasModifiedNavmesh`

- `string MaxAccess`

- `bool AlterNavmeshObjects`

- `bool AlterPermanentObjects`

- `int GodLevel`

- `string Language`

- `bool LanguageIsPublic`


## AssetUploaderBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string State`


## UploaderRequestUpload (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `Uri Url`


## UploaderRequestComplete (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AssetID`


## UploadBakedTextureMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AssetUploaderBlock Request`


## RequiredVoiceVersionMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int MajorVersion`

- `int MinorVersion`

- `string RegionName`


## ParcelVoiceInfoRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int ParcelID`

- `string RegionName`

- `Uri SipChannelUri`


## ProvisionVoiceAccountRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Password`

- `string Username`


## UploadScriptTaskMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AssetUploaderBlock Request`


## ScriptRunningReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ItemID`

- `bool Mono`

- `bool Luau`

- `bool LuauLanguage`

- `UUID ObjectID`

- `bool Running`

- `string CompileTarget`


## UpdateGestureAgentInventoryMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AssetUploaderBlock Request`


## UpdateNotecardTaskInventoryMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID TaskID`

- `UUID ItemID`


## UpdateAgentInventoryRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ItemID`


## UpdateNotecardAgentInventoryMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AssetUploaderBlock Request`


## CopyInventoryFromNotecardMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int CallbackID`

- `UUID FolderID`

- `UUID ItemID`

- `UUID NotecardID`

- `UUID ObjectID`


## UploaderScriptRequestError (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `bool Compiled`

- `string Error`

- `UUID AssetID`


## UpdateScriptTaskUpdateMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `bool ScriptRunning`

- `UUID ItemID`

- `string Target`

- `UUID TaskID`


## UpdateScriptTaskMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AssetUploaderBlock Request`


## UploaderRequestScriptComplete (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AssetID`

- `bool Compiled`


## UpdateScriptAgentRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ItemID`

- `string Target`


## UpdateScriptAgentMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AssetUploaderBlock Request`


## SendPostcardMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Message`

- `string FromName`

- `Vector3 GlobalPosition`

- `string Subject`

- `string ToEmail`


## MapLayerMessageBase (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int Flags`


## MapLayerRequestVariant (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## MapLayerReplyVariant (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class LayerData`

- `UUID ImageID`

- `int Bottom`

- `int Left`

- `int Right`

- `int Top`

- `LayerData[] LayerDataBlocks`


## LayerData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ImageID`

- `int Bottom`

- `int Left`

- `int Right`

- `int Top`

- `LayerData[] LayerDataBlocks`


## MapLayerMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `MapLayerMessageBase Request`


## ProductInfoRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class ProductInfo`

- `string Sku`

- `string Name`

- `string Description`

- `List<ProductInfo> Products`


## ProductInfo (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Sku`

- `string Name`

- `string Description`

- `List<ProductInfo> Products`


## SearchStatRequestBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## SearchStatRequestRequest (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ClassifiedID`


## SearchStatRequestReply (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int MapClicks`

- `int ProfileClicks`

- `int SearchMapClicks`

- `int SearchProfileClicks`

- `int SearchTeleportClicks`

- `int TeleportClicks`


## SearchStatRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `SearchStatRequestBlock Request`


## ChatSessionRequestBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Method`


## ChatSessionRequestStartConference (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID[] AgentsBlock`

- `UUID SessionID`


## ChatSessionRequestMuteUpdate (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID SessionID`

- `UUID AgentID`

- `string RequestKey`

- `bool RequestValue`


## ChatSessionAcceptInvitation (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID SessionID`


## ChatSessionRequestMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `ChatSessionRequestBlock Request`


## ChatterboxSessionEventReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID SessionID`

- `bool Success`


## ChatterBoxSessionStartReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID SessionID`

- `UUID TempSessionID`

- `bool Success`

- `string SessionName`

- `int Type`

- `bool VoiceEnabled`

- `bool ModeratedVoice`


## ChatterBoxInvitationMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID FromAgentID`

- `string FromAgentName`

- `UUID ToAgentID`

- `uint ParentEstateID`

- `UUID RegionID`

- `Vector3 Position`

- `InstantMessageDialog Dialog`

- `bool GroupIM`

- `UUID IMSessionID`

- `DateTime Timestamp`

- `string Message`

- `InstantMessageOnline Offline`

- `byte[] BinaryBucket`

- `bool Voice`

- `string VoiceChannelUri`

- `string VoiceChannelCredentials`


## RegionInfoMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int ParcelLocalID`

- `string RegionName`

- `string ChannelUri`


## ChatterBoxSessionAgentListUpdatesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID SessionID`

- `class AgentUpdatesBlock`

- `UUID AgentID`

- `bool CanVoiceChat`

- `bool IsModerator`

- `string Transition`

- `bool MuteText`

- `bool MuteVoice`

- `AgentUpdatesBlock[] Updates`


## AgentUpdatesBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AgentID`

- `bool CanVoiceChat`

- `bool IsModerator`

- `string Transition`

- `bool MuteText`

- `bool MuteVoice`

- `AgentUpdatesBlock[] Updates`


## ForceCloseChatterBoxSessionMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Reason`

- `UUID SessionID`


## EventMessageBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## EventQueueAck (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int AckID`

- `bool Done`


## EventQueueEvent (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class QueueEvent`

- `IMessage? EventMessage`

- `string MessageKey`

- `int Sequence`

- `QueueEvent[] MessageEvents`


## QueueEvent (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `IMessage? EventMessage`

- `string MessageKey`

- `int Sequence`

- `QueueEvent[] MessageEvents`


## EventQueueGetMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `EventMessageBlock Messages`


## ViewerStatsMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int AgentsInView`

- `float AgentFPS`

- `string AgentLanguage`

- `float AgentMemoryUsed`

- `float MetersTraveled`

- `float AgentPing`

- `int RegionsVisited`

- `float AgentRuntime`

- `float SimulatorFPS`

- `DateTime AgentStartTime`

- `string AgentVersion`

- `float object_kbytes`

- `float texture_kbytes`

- `float world_kbytes`

- `float MiscVersion`

- `bool VertexBuffersEnabled`

- `UUID SessionID`

- `int StatsDropped`

- `int StatsFailedResends`

- `int FailuresInvalid`

- `int FailuresOffCircuit`

- `int FailuresResent`

- `int FailuresSendPacket`

- `int MiscInt1`

- `int MiscInt2`

- `string MiscString1`

- `int InCompressedPackets`

- `float InKbytes`

- `float InPackets`

- `float InSavings`

- `int OutCompressedPackets`

- `float OutKbytes`

- `float OutPackets`

- `float OutSavings`

- `string SystemCPU`

- `string SystemGPU`

- `int SystemGPUClass`

- `string SystemGPUVendor`

- `string SystemGPUVersion`

- `string SystemOS`

- `int SystemInstalledRam`


## PlacesReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AgentID`

- `UUID QueryID`

- `UUID TransactionID`

- `class QueryData`

- `int ActualArea`

- `int BillableArea`

- `string Description`

- `float Dwell`

- `int Flags`

- `float GlobalX`

- `float GlobalY`

- `float GlobalZ`

- `string Name`

- `UUID OwnerID`

- `string SimName`

- `UUID SnapShotID`

- `string ProductSku`

- `int Price`

- `QueryData[] QueryDataBlocks`


## QueryData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int ActualArea`

- `int BillableArea`

- `string Description`

- `float Dwell`

- `int Flags`

- `float GlobalX`

- `float GlobalY`

- `float GlobalZ`

- `string Name`

- `UUID OwnerID`

- `string SimName`

- `UUID SnapShotID`

- `string ProductSku`

- `int Price`

- `QueryData[] QueryDataBlocks`


## UpdateAgentInformationMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string MaxAccess`


## DirLandReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID AgentID`

- `UUID QueryID`

- `class QueryReply`

- `int ActualArea`

- `bool Auction`

- `bool ForSale`

- `string Name`

- `UUID ParcelID`

- `string ProductSku`

- `int SalePrice`

- `QueryReply[] QueryReplies`


## QueryReply (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int ActualArea`

- `bool Auction`

- `bool ForSale`

- `string Name`

- `UUID ParcelID`

- `string ProductSku`

- `int SalePrice`

- `QueryReply[] QueryReplies`


## UploadObjectAssetMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class Object`

- `class Face`

- `Bumpiness Bump`

- `Color4 Color`

- `bool Fullbright`

- `float Glow`

- `UUID ImageID`

- `float ImageRot`

- `int MediaFlags`

- `float OffsetS`

- `float OffsetT`

- `float ScaleS`

- `float ScaleT`

- `class ExtraParam`

- `ExtraParamType Type`

- `byte[] ExtraParamData`

- `Face[] Faces`

- `ExtraParam[] ExtraParams`

- `UUID GroupID`

- `Material Material`

- `string Name`

- `Vector3 Position`

- `Quaternion Rotation`

- `Vector3 Scale`

- `float PathBegin`

- `int PathCurve`

- `float PathEnd`

- `float RadiusOffset`

- `float Revolutions`

- `float ScaleX`

- `float ScaleY`

- `float ShearX`

- `float ShearY`

- `float Skew`

- `float TaperX`

- `float TaperY`

- `float Twist`

- `float TwistBegin`

- `float ProfileBegin`

- `int ProfileCurve`

- `float ProfileEnd`

- `float ProfileHollow`

- `UUID SculptID`

- `SculptType SculptType`


## Object (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class Face`

- `Bumpiness Bump`

- `Color4 Color`

- `bool Fullbright`

- `float Glow`

- `UUID ImageID`

- `float ImageRot`

- `int MediaFlags`

- `float OffsetS`

- `float OffsetT`

- `float ScaleS`

- `float ScaleT`

- `class ExtraParam`

- `ExtraParamType Type`

- `byte[] ExtraParamData`

- `Face[] Faces`

- `ExtraParam[] ExtraParams`

- `UUID GroupID`

- `Material Material`

- `string Name`

- `Vector3 Position`

- `Quaternion Rotation`

- `Vector3 Scale`

- `float PathBegin`

- `int PathCurve`

- `float PathEnd`

- `float RadiusOffset`

- `float Revolutions`

- `float ScaleX`

- `float ScaleY`

- `float ShearX`

- `float ShearY`

- `float Skew`

- `float TaperX`

- `float TaperY`

- `float Twist`

- `float TwistBegin`

- `float ProfileBegin`

- `int ProfileCurve`

- `float ProfileEnd`

- `float ProfileHollow`

- `UUID SculptID`

- `SculptType SculptType`


## Face (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `Bumpiness Bump`

- `Color4 Color`

- `bool Fullbright`

- `float Glow`

- `UUID ImageID`

- `float ImageRot`

- `int MediaFlags`

- `float OffsetS`

- `float OffsetT`

- `float ScaleS`

- `float ScaleT`

- `class ExtraParam`

- `ExtraParamType Type`

- `byte[] ExtraParamData`

- `Face[] Faces`

- `ExtraParam[] ExtraParams`

- `UUID GroupID`

- `Material Material`

- `string Name`

- `Vector3 Position`

- `Quaternion Rotation`

- `Vector3 Scale`

- `float PathBegin`

- `int PathCurve`

- `float PathEnd`

- `float RadiusOffset`

- `float Revolutions`

- `float ScaleX`

- `float ScaleY`

- `float ShearX`

- `float ShearY`

- `float Skew`

- `float TaperX`

- `float TaperY`

- `float Twist`

- `float TwistBegin`

- `float ProfileBegin`

- `int ProfileCurve`

- `float ProfileEnd`

- `float ProfileHollow`

- `UUID SculptID`

- `SculptType SculptType`


## ExtraParam (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `ExtraParamType Type`

- `byte[] ExtraParamData`

- `Face[] Faces`

- `ExtraParam[] ExtraParams`

- `UUID GroupID`

- `Material Material`

- `string Name`

- `Vector3 Position`

- `Quaternion Rotation`

- `Vector3 Scale`

- `float PathBegin`

- `int PathCurve`

- `float PathEnd`

- `float RadiusOffset`

- `float Revolutions`

- `float ScaleX`

- `float ScaleY`

- `float ShearX`

- `float ShearY`

- `float Skew`

- `float TaperX`

- `float TaperY`

- `float Twist`

- `float TwistBegin`

- `float ProfileBegin`

- `int ProfileCurve`

- `float ProfileEnd`

- `float ProfileHollow`

- `UUID SculptID`

- `SculptType SculptType`


## ObjectPhysicsPropertiesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `Primitive.PhysicsProperties[] ObjectPhysicsProperties`


## RenderMaterialsMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `OSD MaterialData`


## GetObjectCostRequest (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID[] ObjectIDs`


## GetObjectCostMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID object_id`

- `double link_cost`

- `double object_cost`

- `double physics_cost`

- `double link_physics_cost`


## ObjectMediaNavigateMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string URL`

- `UUID PrimID`

- `int Face`


## ObjectMediaBlock (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## ObjectMediaRequest (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID PrimID`

- `string Verb`


## ObjectMediaResponse (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID PrimID`

- `MediaEntry[] FaceMedia`

- `string Version`


## ObjectMediaUpdate (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID PrimID`

- `MediaEntry[] FaceMedia`

- `string Verb`


## ObjectMediaMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `ObjectMediaBlock Request`


## ObjectResourcesDetail (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ID`

- `string Name`

- `bool GroupOwned`

- `Vector3d Location`

- `UUID OwnerID`


## ParcelResourcesDetail (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ID`

- `int LocalID`

- `string Name`

- `bool GroupOwned`

- `UUID OwnerID`

- `ObjectResourcesDetail[] Objects`


## BaseResourcesInfo (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## AttachmentResourcesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## LandResourcesRequest (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ParcelID`


## LandResourcesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `Uri ScriptResourceDetails`

- `Uri ScriptResourceSummary`


## LandResourcesInfo (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `ParcelResourcesDetail[] Parcels`


## GetDisplayNamesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AgentDisplayName[] Agents`

- `UUID[] BadIDs`


## SetDisplayNameMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string OldDisplayName`

- `string NewDisplayName`


## SetDisplayNameReplyMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `AgentDisplayName DisplayName`

- `string Reason`

- `int Status`


## DisplayNameUpdateMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string OldDisplayName`

- `AgentDisplayName DisplayName`


## AgentProfileMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class GroupData`

- `string Description`

- `bool Enabled`

- `UUID FounderID`

- `UUID ID`

- `UUID ImageID`

- `bool IsMaturePublish`

- `string Name`

- `bool IsOpenEnrollment`

- `bool IsShownInSearch`

- `class PickData`

- `double GridX`

- `double GridY`

- `UUID ParcelID`

- `string ParcelName`

- `string RegionName`

- `double RegionX`

- `double RegionY`

- `double RegionZ`

- `Uri Slurl`

- `UUID SnapshotID`

- `UUID AvatarID`

- `UUID SecondLifeImageID`

- `UUID FirstLifeImageID`

- `UUID PartnerID`

- `string SecondLifeAboutText`

- `string FirstLifeAboutText`

- `DateTime MemberSince`

- `bool? HideAge`

- `string CustomerType`

- `string Notes`

- `SimAccess AllowedMaturity`

- `SimAccess PreferredMaturity`

- `string DisplayName`

- `DateTime DisplayNameNextUpdate`

- `bool IsDisplayNameDefault`

- `string Username`

- `string LegacyFirstName`

- `string LegacyLastName`

- `bool IsMatureProfile`

- `string Title`

- `string HomePage`

- `int? CaptionIndex`

- `string? CaptionText`

- `List<GroupData> Groups`

- `List<PickData> Picks`

- `ProfileFlags Flags`


## GroupData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Description`

- `bool Enabled`

- `UUID FounderID`

- `UUID ID`

- `UUID ImageID`

- `bool IsMaturePublish`

- `string Name`

- `bool IsOpenEnrollment`

- `bool IsShownInSearch`

- `class PickData`

- `double GridX`

- `double GridY`

- `UUID ParcelID`

- `string ParcelName`

- `string RegionName`

- `double RegionX`

- `double RegionY`

- `double RegionZ`

- `Uri Slurl`

- `UUID SnapshotID`

- `UUID AvatarID`

- `UUID SecondLifeImageID`

- `UUID FirstLifeImageID`

- `UUID PartnerID`

- `string SecondLifeAboutText`

- `string FirstLifeAboutText`

- `DateTime MemberSince`

- `bool? HideAge`

- `string CustomerType`

- `string Notes`

- `SimAccess AllowedMaturity`

- `SimAccess PreferredMaturity`

- `string DisplayName`

- `DateTime DisplayNameNextUpdate`

- `bool IsDisplayNameDefault`

- `string Username`

- `string LegacyFirstName`

- `string LegacyLastName`

- `bool IsMatureProfile`

- `string Title`

- `string HomePage`

- `int? CaptionIndex`

- `string? CaptionText`

- `List<GroupData> Groups`

- `List<PickData> Picks`

- `ProfileFlags Flags`


## PickData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ID`

- `string Description`

- `bool Enabled`

- `double GridX`

- `double GridY`

- `string Name`

- `UUID ParcelID`

- `string ParcelName`

- `string RegionName`

- `double RegionX`

- `double RegionY`

- `double RegionZ`

- `Uri Slurl`

- `UUID SnapshotID`

- `UUID AvatarID`

- `UUID SecondLifeImageID`

- `UUID FirstLifeImageID`

- `UUID PartnerID`

- `string SecondLifeAboutText`

- `string FirstLifeAboutText`

- `DateTime MemberSince`

- `bool? HideAge`

- `string CustomerType`

- `string Notes`

- `SimAccess AllowedMaturity`

- `SimAccess PreferredMaturity`

- `string DisplayName`

- `DateTime DisplayNameNextUpdate`

- `bool IsDisplayNameDefault`

- `string Username`

- `string LegacyFirstName`

- `string LegacyLastName`

- `bool IsMatureProfile`

- `string Title`

- `string HomePage`

- `int? CaptionIndex`

- `string? CaptionText`

- `List<GroupData> Groups`

- `List<PickData> Picks`

- `ProfileFlags Flags`


## AvatarRenderInfoMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class AvatarInfo`

- `int Weight`

- `bool TooComplex`

- `int OverLimit`

- `int ReportingLimit`


## AvatarInfo (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int Weight`

- `bool TooComplex`

- `int OverLimit`

- `int ReportingLimit`


## ViewerBenefitsMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `class BenefitPackage`

- `int AnimatedObjectLimit`

- `int AnimationUploadCost`

- `int AttachmentLimit`

- `int CreateGroupCost`

- `int GroupMembershipLimit`

- `int PicksLimit`

- `int SoundUploadCost`

- `int TextureUploadCost`

- `int[] LargeTextureUploadCost`

- `string AccountType`

- `BenefitPackage AccountLevelBenefits`


## BenefitPackage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int AnimatedObjectLimit`

- `int AnimationUploadCost`

- `int AttachmentLimit`

- `int CreateGroupCost`

- `int GroupMembershipLimit`

- `int PicksLimit`

- `int SoundUploadCost`

- `int TextureUploadCost`

- `int[] LargeTextureUploadCost`

- `string AccountType`

- `BenefitPackage AccountLevelBenefits`


## AgentPreferencesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `OSDMap RawData`

- `float HoverHeight`


## ExperienceFlags (enum) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## ExperienceInfo (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `UUID ExperienceID`

- `UUID PublicID`

- `string Name`

- `string Description`

- `ExperienceFlags Flags`

- `UUID GroupID`

- `UUID AgentID`

- `int Quota`

- `int Maturity`

- `UUID ImageID`

- `string Marketplace`

- `string ExtendedMetadata`

- `string SLURL`


## ExperienceInfoMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `List<ExperienceInfo> Experiences`


## ExperienceListMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `List<UUID> ExperienceIDs`


## ExperiencePreferencesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `List<UUID> Allowed`

- `List<UUID> Blocked`


## RegionExperiencesMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `List<UUID> Blocked`

- `List<UUID> Trusted`

- `List<UUID> Allowed`

- `UUID Default`


## EnvironmentFlags (enum) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## EnvironmentData (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `int DayLength`

- `int DayOffset`

- `EnvironmentFlags Flags`

- `bool IsDefault`

- `OSD? DayCycle`


## ExtEnvironmentMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `bool Success`

- `EnvironmentData? Environment`

- `int ParcelId`

- `int Version`

- `string Message`


## LegacyEnvironmentMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `OSD? Settings`


## InterestListMode (enum) — LibreMetaverse.Protocol/Messages/LindenMessages.cs


## InterestListMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Mode`

- `InterestListMode InterestListMode`


## SimConsoleAsyncMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Command`


## SimConsoleResponseMessage (class) — LibreMetaverse.Protocol/Messages/LindenMessages.cs

- `string Body`


## MessageUtils (class) — LibreMetaverse.Protocol/Messages/MessageEventDecoder.cs


## MessageUtils (class) — LibreMetaverse.Protocol/Messages/Messages.cs


## CRC32 (class) — LibreMetaverse.Types/CRC32.cs

- `uint CRC`


## CacheDictionary (class) — LibreMetaverse.Types/CacheDictionary.cs

- `ICollection<TKey> Keys`

- `ICollection<TValue> Values`

- `int Count`

- `bool IsReadOnly`


## CacheDictionaryEnumerator (class) — LibreMetaverse.Types/CacheDictionary.cs


## EmptyRemovalStrategy (class) — LibreMetaverse.Types/CacheDictionary.cs


## MruRemovalStrategy (class) — LibreMetaverse.Types/CacheDictionary.cs


## LruRemovalStrategy (class) — LibreMetaverse.Types/CacheDictionary.cs


## CoordinateFrame (class) — LibreMetaverse.Types/CoordinateFrame.cs

- `Vector3 X_AXIS`

- `Vector3 Y_AXIS`

- `Vector3 Z_AXIS`

- `Vector3 Origin`

- `Vector3 XAxis`

- `Vector3 YAxis`

- `Vector3 ZAxis`


## DoubleDictionary (class) — LibreMetaverse.Types/DoubleDictionary.cs

- `int Count`


## EnumInfoAttribute (class) — LibreMetaverse.Types/Enums.cs

- `string Text`


## AssetType (enum) — LibreMetaverse.Types/Enums.cs


## FolderType (enum) — LibreMetaverse.Types/Enums.cs


## InventoryType (enum) — LibreMetaverse.Types/Enums.cs


## SaleType (enum) — LibreMetaverse.Types/Enums.cs


## WearableType (enum) — LibreMetaverse.Types/Enums.cs


## EnumInfoExtensions (class) — LibreMetaverse.Types/Enums.cs


## PCode (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## PrimFlags (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## SoundFlags (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## ProfileCurve (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## HoleType (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## PathCurve (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## Material (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## PrimType (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## ExtraParamType (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## JointType (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## SculptType (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## FaceType (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## ObjectCategory (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## AttachmentPoint (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## ClickAction (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## PhysicsShapeType (enum) — LibreMetaverse.Types/EnumsPrimitive.cs


## ExpiringCache (class) — LibreMetaverse.Types/ExpiringCache.cs

- `int Count`


## MultiValueDictionary (class) — LibreMetaverse.Types/MultiValueDictionary.cs


## Ray (struct) — LibreMetaverse.Types/Ray.cs

- `Vector3 Origin`

- `Vector3 Direction`


## ViewerUriType (enum) — LibreMetaverse.Types/SlurlParser.cs


## SlappCommand (enum) — LibreMetaverse.Types/SlurlParser.cs


## SlurlParser (class) — LibreMetaverse.Types/SlurlParser.cs

- `string Sim`

- `int X`

- `int Y`

- `int Z`

- `ViewerUriType UriType`

- `SlappCommand Command`

- `string CommandPath`


## TokenBucket (class) — LibreMetaverse.Types/TokenBucket.cs

- `TokenBucket Parent`

- `int MaxBurst`

- `int DripRate`

- `int Content`


## Utils (class) — LibreMetaverse.Types/Utils.cs

- `enum Platform`

- `float E`

- `float LOG10E`

- `float LOG2E`

- `float PI`

- `float TWO_PI`

- `float PI_OVER_TWO`

- `float PI_OVER_FOUR`

- `float DEG_TO_RAD`

- `float RAD_TO_DEG`

- `System.Globalization.CultureInfo EnUsCulture`

- `DateTime Epoch`

- `byte[] EmptyBytes`


## Platform (enum) — LibreMetaverse.Types/Utils.cs

- `float E`

- `float LOG10E`

- `float LOG2E`

- `float PI`

- `float TWO_PI`

- `float PI_OVER_TWO`

- `float PI_OVER_FOUR`

- `float DEG_TO_RAD`

- `float RAD_TO_DEG`

- `System.Globalization.CultureInfo EnUsCulture`

- `DateTime Epoch`

- `byte[] EmptyBytes`


## Utils (class) — LibreMetaverse.Types/UtilsConversions.cs


## Vector2 (struct) — LibreMetaverse.Types/Vector2.cs

- `float X`

- `float Y`


## Vector3d (struct) — LibreMetaverse.Types/Vector3d.cs

- `double X`

- `double Y`

- `double Z`


## Vector4 (struct) — LibreMetaverse.Types/Vector4.cs

- `float X`

- `float Y`

- `float Z`

- `float W`


## ManagedAutoResetEvent (class) — LibreMetaverse.Types/Threading/ManagedAutoResetEvent.cs

- `bool WasDisposed`

- `bool IsSet`


## ManagedManualResetEvent (class) — LibreMetaverse.Types/Threading/ManagedManualResetEvent.cs

- `bool WasDisposed`

- `bool IsSet`


## ManagedSemaphore (class) — LibreMetaverse.Types/Threading/ManagedSemaphore.cs

- `bool WasDisposed`


## OptimisticReaderWriterLock (class) — LibreMetaverse.Types/Threading/OptimisticReaderWriterLock.cs


## SpinLockSlim (struct) — LibreMetaverse.Types/Threading/SpinLockSlim.cs


## SpinReaderWriterLock (class) — LibreMetaverse.Types/Threading/SpinReaderWriterLock.cs


## SpinReaderWriterLockSlim (struct) — LibreMetaverse.Types/Threading/SpinReaderWriterLockSlim.cs


## WaitHandleAsyncFactory (class) — LibreMetaverse.Types/Threading/WaitHandleAsyncFactory.cs


## OptimisticReadLock (struct) — LibreMetaverse.Types/Threading/Disposers/OptimisticReadLock.cs


## OptimisticUpgradeableLock (struct) — LibreMetaverse.Types/Threading/Disposers/OptimisticUpgradeableLock.cs


## OptimisticWriteLock (struct) — LibreMetaverse.Types/Threading/Disposers/OptimisticWriteLock.cs


## SpinReadLock (struct) — LibreMetaverse.Types/Threading/Disposers/SpinReadLock.cs


## SpinUpgradeableLock (struct) — LibreMetaverse.Types/Threading/Disposers/SpinUpgradeableLock.cs


## SpinWriteLock (struct) — LibreMetaverse.Types/Threading/Disposers/SpinWriteLock.cs


## DisposalHelper (class) — LibreMetaverse.Types/Util/DisposalHelper.cs


## DisposalGuard (class) — LibreMetaverse.Types/Util/DisposalHelper.cs


## EventSubscriptionHelper (class) — LibreMetaverse.Types/Util/EventSubscriptionHelper.cs


## EventSubscription (class) — LibreMetaverse.Types/Util/EventSubscriptionHelper.cs


## FileHelper (class) — LibreMetaverse.Types/Util/FileHelper.cs


## DictionaryEventAction (enum) — LibreMetaverse.Types/Util/ObservableDictionary.cs


## ObservableDictionary (class) — LibreMetaverse.Types/Util/ObservableDictionary.cs

- `int Count`


## Repeat (class) — LibreMetaverse.Types/Util/Repeat.cs


## Animation (struct) — LibreMetaverse.Assets/Animation.cs

- `UUID AnimationID`

- `int AnimationSequence`

- `UUID AnimationSourceObjectID`


## BitPack (class) — LibreMetaverse.Assets/BitPack.cs

- `byte[] Data`

- `int BytePos`

- `int BitPos`


## Logger (class) — LibreMetaverse.Assets/Logger.cs


## PermissionMask (enum) — LibreMetaverse.Assets/Permissions.cs


## PermissionWho (enum) — LibreMetaverse.Assets/Permissions.cs


## Permissions (struct) — LibreMetaverse.Assets/Permissions.cs

- `PermissionMask BaseMask`

- `PermissionMask EveryoneMask`

- `PermissionMask GroupMask`

- `PermissionMask NextOwnerMask`

- `PermissionMask OwnerMask`

- `bool operator`

- `Permissions NoPermissions`

- `Permissions FullPermissions`


## Sounds (class) — LibreMetaverse.Assets/Sounds.cs

- `UUID BELL_TING`

- `UUID CLICK`

- `UUID HEALTH_REDUCTION_FEMALE`

- `UUID HEALTH_REDUCTION_MALE`

- `UUID IM_START`

- `UUID INSTANT_MESSAGE_NOTIFICATION`

- `UUID INVALID_OPERATION`

- `UUID KEYBOARD_LOOP`

- `UUID MONEY_REDUCTION_COINS`

- `UUID MONEY_INCREASE_CASH_REGISTER_BELL`

- `UUID NULL_KEYSTROKE`

- `UUID OBJECT_COLLISION`

- `UUID OBJECT_COLLISION_RUBBER`

- `UUID OBJECT_COLLISION_PLASTIC`

- `UUID OBJECT_COLLISION_FLESH`

- `UUID OBJECT_COLLISION_WOOD_SPLINTERING`

- `UUID OBJECT_COLLISION_GLASS_BREAK`

- `UUID OBJECT_COLLISION_METAL_CLUNK`

- `UUID OBJECT_CREATE_WHOOSH`

- `UUID OBJECT_DELETE_SHAKE`

- `UUID OBJECT_REZ`

- `UUID PIE_MENU_APPEAR_DING`

- `UUID PIE_MENU_SLICE_HIGHLIGHT`

- `UUID PIE_MENU_SLICE_HIGHLIGHT1`

- `UUID PIE_MENU_SLICE_HIGHLIGHT2`

- `UUID PIE_MENU_SLICE_HIGHLIGHT3`

- `UUID PIE_MENU_SLICE_HIGHLIGHT4`

- `UUID PIE_MENU_SLICE_HIGHLIGHT5`

- `UUID PIE_MENU_SLICE_HIGHLIGHT6`

- `UUID PIE_MENU_SLICE_HIGHLIGHT7`

- `UUID SNAPSHOT`

- `UUID TELEPORT_TEXTURE_APPLY`

- `UUID THUNDER`

- `UUID WINDOW_CLOSE`

- `UUID WINDOW_OPEN`

- `UUID ZIPPER`


## AnimationTrack (class) — LibreMetaverse.Assets/Animation/AnimationTrack.cs

- `UUID AnimationID`

- `BinBVHAnimationReader? Data`

- `float CurrentTime`

- `bool IsFinished`

- `float EaseWeight`


## AnimeshPlayer (class) — LibreMetaverse.Assets/Animation/AnimeshPlayer.cs

- `UUID ObjectID`

- `int TrackCount`


## BinBVHAnimationReader (class) — LibreMetaverse.Assets/Animation/BVHDecoder.cs

- `ushort unknown0`

- `ushort unknown1`

- `int Priority`

- `float Length`

- `string ExpressionName`

- `float InPoint`

- `float OutPoint`

- `bool Loop`

- `float EaseInTime`

- `float EaseOutTime`

- `uint HandPose`

- `uint JointCount`

- `int MaxJoints`

- `binBVHJoint[] joints`


## binBVHJoint (struct) — LibreMetaverse.Assets/Animation/BVHDecoder.cs

- `bool operator`

- `string Name`

- `int Priority`

- `binBVHJointKey[] rotationkeys`

- `binBVHJointKey[] positionkeys`

- `object Tag`


## binBVHJointKey (struct) — LibreMetaverse.Assets/Animation/BVHDecoder.cs

- `float time`

- `Vector3 key_element`


## HandPose (enum) — LibreMetaverse.Assets/Animation/BVHDecoder.cs


## JointPose (struct) — LibreMetaverse.Assets/Animesh/JointPose.cs

- `Quaternion Rotation`

- `bool HasRotation`

- `Vector3 Position`

- `bool HasPosition`

- `int Priority`

- `float EaseWeight`


## AvatarTextureIndex (enum) — LibreMetaverse.Assets/Appearance/AvatarTextureIndex.cs


## Asset (class) — LibreMetaverse.Assets/Assets/Asset.cs

- `byte[] AssetData`

- `bool Temporary`

- `UUID AssetID`


## AssetAnimation (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetAnimation.cs


## AssetBodypart (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetBodypart.cs


## AssetCallingCard (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetCallingCard.cs

- `UUID AvatarID`


## AssetClothing (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetClothing.cs


## GestureStepType (enum) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs


## GestureStep (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs


## GestureStepAnimation (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs

- `bool AnimationStart`

- `UUID ID`

- `string Name`


## GestureStepSound (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs

- `UUID ID`

- `string Name`


## GestureStepChat (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs

- `string Text`


## GestureStepWait (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs

- `bool WaitForAnimation`

- `bool WaitForTime`

- `float WaitTime`


## GestureStepEOF (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs


## AssetGesture (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetGesture.cs

- `byte TriggerKey`

- `uint TriggerKeyMask`

- `string Trigger`

- `string ReplaceWith`

- `List<GestureStep> Sequence`


## AssetLandmark (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetLandmark.cs

- `UUID RegionID`

- `Vector3 Position`


## GltfAlphaMode (enum) — LibreMetaverse.Assets/Assets/AssetTypes/AssetMaterial.cs


## GltfTextureTransform (struct) — LibreMetaverse.Assets/Assets/AssetTypes/AssetMaterial.cs

- `GltfTextureTransform Default`

- `Vector2 Offset`

- `Vector2 Scale`

- `float Rotation`

- `bool IsDefault`


## AssetMaterial (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetMaterial.cs

- `int TEXTURE_BASE_COLOR`

- `int TEXTURE_NORMAL`

- `int TEXTURE_METALLIC_ROUGHNESS`

- `int TEXTURE_EMISSIVE`

- `int TEXTURE_COUNT`

- `UUID GLTF_OVERRIDE_NULL_UUID`

- `string Name`

- `UUID[] TextureIds`

- `GltfTextureTransform[] TextureTransforms`

- `Color4 BaseColorFactor`

- `Vector3 EmissiveFactor`

- `float MetallicFactor`

- `float RoughnessFactor`

- `float AlphaCutoff`

- `GltfAlphaMode AlphaMode`

- `bool DoubleSided`

- `bool OverrideAlphaMode`

- `bool OverrideDoubleSided`


## AssetMesh (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetMesh.cs

- `OSDMap MeshData`

- `int MaxParts`

- `int MaxInflatedPartBytes`

- `long MaxInflatedAssetBytes`

- `int MaxDecodedElements`


## AssetMutable (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetMutable.cs

- `AssetType currentType`


## AssetNotecard (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetNotecard.cs

- `string BodyText`

- `List<InventoryItem> EmbeddedItems`


## AssetPrim (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `PrimObject? Parent`

- `List<PrimObject> Children`


## PrimObject (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `class FlexibleBlock`

- `int Softness`

- `float Gravity`

- `float Drag`

- `float Wind`

- `float Tension`

- `Vector3 Force`

- `class LightBlock`

- `Color4 Color`

- `float Intensity`

- `float Radius`

- `float Falloff`

- `float Cutoff`

- `class SculptBlock`

- `UUID Texture`

- `int Type`

- `class ParticlesBlock`

- `int Flags`

- `int Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `int BurstParticleCount`

- `Vector3 AngularVelocity`

- `Vector3 Acceleration`

- `UUID TextureID`

- `UUID TargetID`

- `int DataFlags`

- `float ParticleMaxAge`

- `Color4 ParticleStartColor`

- `Color4 ParticleEndColor`

- `Vector2 ParticleStartScale`

- `Vector2 ParticleEndScale`

- `uint Crc`

- `float ParticleStartGlow`

- `float ParticleEndGlow`

- `int BlendFuncSource`

- `int BlendFuncDest`


## FlexibleBlock (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `int Softness`

- `float Gravity`

- `float Drag`

- `float Wind`

- `float Tension`

- `Vector3 Force`

- `class LightBlock`

- `Color4 Color`

- `float Intensity`

- `float Radius`

- `float Falloff`

- `float Cutoff`

- `class SculptBlock`

- `UUID Texture`

- `int Type`

- `class ParticlesBlock`

- `int Flags`

- `int Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `int BurstParticleCount`

- `Vector3 AngularVelocity`

- `Vector3 Acceleration`

- `UUID TextureID`

- `UUID TargetID`

- `int DataFlags`

- `float ParticleMaxAge`

- `Color4 ParticleStartColor`

- `Color4 ParticleEndColor`

- `Vector2 ParticleStartScale`

- `Vector2 ParticleEndScale`

- `uint Crc`

- `float ParticleStartGlow`

- `float ParticleEndGlow`

- `int BlendFuncSource`

- `int BlendFuncDest`


## LightBlock (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `Color4 Color`

- `float Intensity`

- `float Radius`

- `float Falloff`

- `float Cutoff`

- `class SculptBlock`

- `UUID Texture`

- `int Type`

- `class ParticlesBlock`

- `int Flags`

- `int Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `int BurstParticleCount`

- `Vector3 AngularVelocity`

- `Vector3 Acceleration`

- `UUID TextureID`

- `UUID TargetID`

- `int DataFlags`

- `float ParticleMaxAge`

- `Color4 ParticleStartColor`

- `Color4 ParticleEndColor`

- `Vector2 ParticleStartScale`

- `Vector2 ParticleEndScale`

- `uint Crc`

- `float ParticleStartGlow`

- `float ParticleEndGlow`

- `int BlendFuncSource`

- `int BlendFuncDest`


## SculptBlock (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `UUID Texture`

- `int Type`

- `class ParticlesBlock`

- `int Flags`

- `int Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `int BurstParticleCount`

- `Vector3 AngularVelocity`

- `Vector3 Acceleration`

- `UUID TextureID`

- `UUID TargetID`

- `int DataFlags`

- `float ParticleMaxAge`

- `Color4 ParticleStartColor`

- `Color4 ParticleEndColor`

- `Vector2 ParticleStartScale`

- `Vector2 ParticleEndScale`

- `uint Crc`

- `float ParticleStartGlow`

- `float ParticleEndGlow`

- `int BlendFuncSource`

- `int BlendFuncDest`

- `bool IsSet`


## ParticlesBlock (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `int Flags`

- `int Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `int BurstParticleCount`

- `Vector3 AngularVelocity`

- `Vector3 Acceleration`

- `UUID TextureID`

- `UUID TargetID`

- `int DataFlags`

- `float ParticleMaxAge`

- `Color4 ParticleStartColor`

- `Color4 ParticleEndColor`

- `Vector2 ParticleStartScale`

- `Vector2 ParticleEndScale`

- `uint Crc`

- `float ParticleStartGlow`

- `float ParticleEndGlow`

- `int BlendFuncSource`

- `int BlendFuncDest`

- `bool IsSet`


## ShapeBlock (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `int PathCurve`

- `float PathBegin`

- `float PathEnd`

- `float PathScaleX`

- `float PathScaleY`

- `float PathShearX`

- `float PathShearY`

- `float PathTwist`

- `float PathTwistBegin`

- `float PathRadiusOffset`

- `float PathTaperX`

- `float PathTaperY`

- `float PathRevolutions`

- `float PathSkew`

- `int ProfileCurve`

- `float ProfileBegin`

- `float ProfileEnd`

- `float ProfileHollow`

- `class InventoryBlock`

- `class ItemBlock`

- `UUID ID`

- `string Name`

- `UUID OwnerID`

- `UUID CreatorID`

- `UUID GroupID`

- `UUID LastOwnerID`

- `UUID PermsGranterID`

- `UUID AssetID`

- `AssetType Type`

- `InventoryType InvType`

- `string Description`

- `uint PermsBase`

- `uint PermsOwner`

- `uint PermsGroup`

- `uint PermsEveryone`

- `uint PermsNextOwner`

- `int Flags`

- `DateTime CreationDate`


## InventoryBlock (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `class ItemBlock`

- `UUID ID`

- `string Name`

- `UUID OwnerID`

- `UUID CreatorID`

- `UUID GroupID`

- `UUID LastOwnerID`

- `UUID PermsGranterID`

- `UUID AssetID`

- `AssetType Type`

- `InventoryType InvType`

- `string Description`

- `uint PermsBase`

- `uint PermsOwner`

- `uint PermsGroup`

- `uint PermsEveryone`

- `uint PermsNextOwner`

- `int Flags`

- `DateTime CreationDate`

- `int Serial`

- `ItemBlock[] Items`


## ItemBlock (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetPrim.cs

- `UUID ID`

- `string Name`

- `UUID OwnerID`

- `UUID CreatorID`

- `UUID GroupID`

- `UUID LastOwnerID`

- `UUID PermsGranterID`

- `UUID AssetID`

- `AssetType Type`

- `InventoryType InvType`

- `string Description`

- `uint PermsBase`

- `uint PermsOwner`

- `uint PermsGroup`

- `uint PermsEveryone`

- `uint PermsNextOwner`

- `int Flags`

- `DateTime CreationDate`

- `int Serial`

- `ItemBlock[] Items`


## AssetScriptBinary (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetScriptBinary.cs


## AssetScriptText (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetScriptText.cs

- `string? Source`


## AssetSettings (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetSettings.cs

- `OSD? Settings`


## AssetSound (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetSound.cs


## AssetTexture (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetTexture.cs

- `ManagedImage? Image`

- `int Components`

- `int MaxDimension`

- `int MaxComponents`

- `int MaxBitDepth`

- `int MaxTiles`

- `int MaxDecompositionLevels`


## AssetWearable (class) — LibreMetaverse.Assets/Assets/AssetTypes/AssetWearable.cs

- `string Name`

- `string Description`

- `WearableType WearableType`

- `SaleType ForSale`

- `int SalePrice`

- `UUID Creator`

- `UUID Owner`

- `UUID LastOwner`

- `UUID Group`

- `bool GroupOwned`

- `Permissions Permissions`


## SceneObjectGroupXmlWriter (class) — LibreMetaverse.Assets/Assets/AssetTypes/SceneObjectGroupXmlWriter.cs


## GltfAnimationSampler (class) — LibreMetaverse.Assets/Assets/Gltf/GltfAnimation.cs

- `int Input`

- `int Output`

- `GltfAnimationInterpolation Interpolation`


## GltfAnimationChannelTarget (class) — LibreMetaverse.Assets/Assets/Gltf/GltfAnimation.cs

- `int Node`

- `GltfAnimationTargetPath Path`


## GltfAnimationChannel (class) — LibreMetaverse.Assets/Assets/Gltf/GltfAnimation.cs

- `int Sampler`

- `GltfAnimationChannelTarget Target`


## GltfAnimation (class) — LibreMetaverse.Assets/Assets/Gltf/GltfAnimation.cs

- `string? Name`

- `List<GltfAnimationSampler> Samplers`

- `List<GltfAnimationChannel> Channels`


## GltfBuffer (class) — LibreMetaverse.Assets/Assets/Gltf/GltfBuffer.cs

- `byte[]? Data`

- `string? Uri`

- `int ByteLength`

- `string? Name`


## GltfBufferView (class) — LibreMetaverse.Assets/Assets/Gltf/GltfBuffer.cs

- `int Buffer`

- `int ByteOffset`

- `int ByteLength`

- `int ByteStride`

- `int Target`

- `string? Name`


## GltfAccessor (class) — LibreMetaverse.Assets/Assets/Gltf/GltfBuffer.cs

- `int BufferView`

- `int ByteOffset`

- `GltfComponentType ComponentType`

- `bool Normalized`

- `int Count`

- `GltfAccessorType Type`

- `double[]? Max`

- `double[]? Min`

- `string? Name`

- `int ComponentCount`

- `int ComponentByteSize`

- `int DefaultStride`


## GltfDocument (class) — LibreMetaverse.Assets/Assets/Gltf/GltfDocument.cs

- `string Version`

- `string? Generator`

- `string? Copyright`

- `string? MinVersion`

- `int DefaultScene`

- `List<GltfScene> Scenes`

- `List<GltfNode> Nodes`

- `List<GltfMesh> Meshes`

- `List<GltfSkin> Skins`

- `List<GltfAnimation> Animations`

- `List<GltfDocumentMaterial> Materials`

- `List<GltfTexture> Textures`

- `List<GltfSampler> Samplers`

- `List<GltfImage> Images`

- `List<GltfAccessor> Accessors`

- `List<GltfBufferView> BufferViews`

- `List<GltfBuffer> Buffers`

- `List<string> ExtensionsUsed`

- `List<string> ExtensionsRequired`


## GltfPrimitiveMode (enum) — LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs


## GltfComponentType (enum) — LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs


## GltfAccessorType (enum) — LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs


## GltfSamplerFilter (enum) — LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs


## GltfSamplerWrap (enum) — LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs


## GltfAnimationInterpolation (enum) — LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs


## GltfAnimationTargetPath (enum) — LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs


## GltfPrimitive (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSceneGraph.cs

- `string ATTR_POSITION`

- `string ATTR_NORMAL`

- `string ATTR_TANGENT`

- `string ATTR_TEXCOORD_0`

- `string ATTR_TEXCOORD_1`

- `string ATTR_COLOR_0`

- `string ATTR_JOINTS_0`

- `string ATTR_WEIGHTS_0`

- `int Indices`

- `int Material`

- `GltfPrimitiveMode Mode`


## GltfMesh (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSceneGraph.cs

- `string? Name`

- `List<GltfPrimitive> Primitives`

- `double[]? Weights`


## GltfNode (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSceneGraph.cs

- `string? Name`

- `int Mesh`

- `int Skin`

- `List<int> Children`

- `Vector3 Translation`

- `Quaternion Rotation`

- `Vector3 Scale`

- `Matrix4? Matrix`

- `double[]? Weights`


## GltfScene (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSceneGraph.cs

- `string? Name`

- `List<int> Nodes`


## GltfSkin (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSceneGraph.cs

- `string? Name`

- `int InverseBindMatrices`

- `int Skeleton`

- `List<int> Joints`


## GltfImage (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSurface.cs

- `string? Name`

- `string? Uri`

- `string? MimeType`

- `int BufferView`


## GltfSampler (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSurface.cs

- `GltfSamplerFilter MagFilter`

- `GltfSamplerFilter MinFilter`

- `GltfSamplerWrap WrapS`

- `GltfSamplerWrap WrapT`

- `string? Name`


## GltfTexture (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSurface.cs

- `int Sampler`

- `int Source`

- `string? Name`


## GltfTextureRef (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSurface.cs

- `int Index`

- `int TexCoord`

- `GltfTextureTransform Transform`


## GltfNormalTextureRef (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSurface.cs

- `float Scale`


## GltfOcclusionTextureRef (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSurface.cs

- `float Strength`


## GltfDocumentMaterial (class) — LibreMetaverse.Assets/Assets/Gltf/GltfSurface.cs

- `string? Name`

- `Color4 BaseColorFactor`

- `GltfTextureRef? BaseColorTexture`

- `float MetallicFactor`

- `float RoughnessFactor`

- `GltfTextureRef? MetallicRoughnessTexture`

- `GltfNormalTextureRef? NormalTexture`

- `GltfOcclusionTextureRef? OcclusionTexture`

- `GltfTextureRef? EmissiveTexture`

- `Vector3 EmissiveFactor`

- `GltfAlphaMode AlphaMode`

- `float AlphaCutoff`

- `bool DoubleSided`


## ManagedImageInterleavedExtensions (class) — LibreMetaverse.Assets/Imaging/ManagedImageInterleavedExtensions.cs


## ManagedImageCreator (class) — LibreMetaverse.Assets/Imaging/ManagedImageJ2kCreator.cs


## Targa (class) — LibreMetaverse.Assets/Imaging/Targa.cs


## ModelMaterial (class) — LibreMetaverse.Assets/ImportExport/Model.cs

- `string ID`

- `Color4 DiffuseColor`

- `string Texture`

- `byte[] TextureData`

- `int Width`

- `int Height`

- `ModelPbrMaterial? Pbr`


## ModelTexture (class) — LibreMetaverse.Assets/ImportExport/Model.cs

- `string Name`

- `byte[] Data`

- `int Width`

- `int Height`

- `int TexCoord`

- `GltfTextureTransform Transform`


## ModelPbrMaterial (class) — LibreMetaverse.Assets/ImportExport/Model.cs

- `string Name`

- `Color4 BaseColorFactor`

- `float MetallicFactor`

- `float RoughnessFactor`

- `Vector3 EmissiveFactor`

- `GltfAlphaMode AlphaMode`

- `float AlphaCutoff`

- `bool DoubleSided`

- `float NormalScale`

- `float OcclusionStrength`

- `ModelTexture? BaseColorTexture`

- `ModelTexture? NormalTexture`

- `ModelTexture? MetallicRoughnessTexture`

- `ModelTexture? EmissiveTexture`


## ModelSkin (class) — LibreMetaverse.Assets/ImportExport/Model.cs

- `int MaxJoints`

- `List<string> JointNames`

- `float[] InverseBindMatrices`

- `float[] BindShapeMatrix`


## ModelFace (class) — LibreMetaverse.Assets/ImportExport/Model.cs

- `List<Vertex> Vertices`

- `List<uint> Indices`

- `string MaterialID`

- `ModelMaterial Material`

- `List<VertexWeight>? Weights`

- `Vertex Vertex`

- `VertexWeight Weight`


## ModelPrim (class) — LibreMetaverse.Assets/ImportExport/Model.cs

- `int MaxFaces`

- `int MaxVerticesPerFace`

- `List<Vector3> Positions`

- `Vector3 BoundMin`

- `Vector3 BoundMax`

- `Vector3 Position`

- `Vector3 Scale`

- `Quaternion Rotation`

- `List<ModelFace> Faces`

- `string ID`

- `byte[] Asset`

- `ModelSkin? Skin`


## ModelAssetOptions (class) — LibreMetaverse.Assets/ImportExport/ModelAssetOptions.cs

- `bool GenerateLods`

- `float LodReduction`

- `bool GeneratePhysics`

- `ModelAssetOptions None`


## ModelDiagnosticSeverity (enum) — LibreMetaverse.Assets/ImportExport/ModelDiagnostics.cs


## ModelDiagnosticCode (enum) — LibreMetaverse.Assets/ImportExport/ModelDiagnostics.cs


## ModelDiagnostic (class) — LibreMetaverse.Assets/ImportExport/ModelDiagnostics.cs

- `ModelDiagnosticSeverity Severity`

- `ModelDiagnosticCode Code`

- `string Message`

- `string? Subject`

- `int Count`


## ModelDiagnosticCollector (class) — LibreMetaverse.Assets/ImportExport/ModelDiagnostics.cs

- `IReadOnlyList<ModelDiagnostic> Diagnostics`

- `bool HasErrors`


## ModelLoadResult (class) — LibreMetaverse.Assets/ImportExport/ModelDiagnostics.cs

- `IReadOnlyList<ModelPrim> Prims`

- `IReadOnlyList<ModelDiagnostic> Diagnostics`

- `bool HasErrors`


## ModelUploadChecks (class) — LibreMetaverse.Assets/ImportExport/ModelUploadChecks.cs


## RendererNameAttribute (class) — LibreMetaverse.Assets/Interfaces/IRendering.cs


## InventoryBase (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `UUID UUID`

- `UUID ParentUUID`

- `string Name`

- `UUID OwnerID`

- `UUID ThumbnailUUID`


## InventoryItem (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `UUID AssetUUID`

- `Permissions Permissions`

- `AssetType AssetType`

- `InventoryType InventoryType`

- `UUID CreatorID`

- `string Description`

- `UUID GroupID`

- `bool GroupOwned`

- `int SalePrice`

- `SaleType SaleType`

- `uint Flags`

- `DateTime CreationDate`

- `UUID TransactionID`

- `UUID LastOwnerID`

- `UUID ResolvedItemID`

- `UUID ResolvedAssetID`


## InventoryTexture (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventorySound (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryCallingCard (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryLandmark (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `bool LandmarkVisited`


## InventoryObject (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `InventoryItemFlags ItemFlags`

- `AttachmentPoint AttachPoint`


## InventoryNotecard (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryCategory (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryLSL (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `ScriptSubtype Subtype`

- `bool IsLua`

- `string Runtime`

- `string CompileTarget`


## InventorySnapshot (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryAttachment (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `AttachmentPoint AttachmentPoint`


## InventoryWearable (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `WearableType WearableType`


## InventoryAnimation (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryGesture (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventorySettings (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryMaterial (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs


## InventoryFolder (class) — LibreMetaverse.Assets/Inventory/InventoryBase.cs

- `int VERSION_UNKNOWN`

- `FolderType PreferredType`

- `int Version`

- `int DescendentCount`


## InventorySortOrder (enum) — LibreMetaverse.Assets/Inventory/InventoryEnums.cs


## DeRezDestination (enum) — LibreMetaverse.Assets/Inventory/InventoryEnums.cs


## ScriptSubtype (enum) — LibreMetaverse.Assets/Inventory/InventoryEnums.cs


## InventoryItemFlags (enum) — LibreMetaverse.Assets/Inventory/InventoryEnums.cs


## InventoryHelpers (class) — LibreMetaverse.Assets/Inventory/InventoryHelpers.cs

- `UUID MagicId`


## ScriptCompileTarget (class) — LibreMetaverse.Assets/Inventory/ScriptCompileTarget.cs

- `string Lsl2`

- `string Mono`

- `string LslLuau`

- `string Luau`


## LegacyMaterial (class) — LibreMetaverse.Assets/Materials/LegacyMaterial.cs

- `UUID ID`

- `UUID NormalMap`

- `double NormalMapOffsetX`

- `double NormalMapOffsetY`

- `double NormalMapRepeatX`

- `double NormalMapRepeatY`

- `double NormalMapRotation`

- `UUID SpecularMap`

- `double SpecularMapOffsetX`

- `double SpecularMapOffsetY`

- `double SpecularMapRepeatX`

- `double SpecularMapRepeatY`

- `double SpecularMapRotation`

- `Color4 SpecularColor`

- `byte SpecularExponent`

- `byte EnvironmentIntensity`

- `byte AlphaMaskCutoff`

- `LegacyMaterialAlphaMode DiffuseAlphaMode`


## LegacyMaterialAlphaMode (enum) — LibreMetaverse.Assets/Materials/LegacyMaterialAlphaMode.cs


## MediaPermission (enum) — LibreMetaverse.Assets/Primitives/ObjectMedia.cs


## MediaControls (enum) — LibreMetaverse.Assets/Primitives/ObjectMedia.cs


## MediaEntry (class) — LibreMetaverse.Assets/Primitives/ObjectMedia.cs

- `bool EnableAlternativeImage`

- `bool AutoLoop`

- `bool AutoPlay`

- `bool AutoScale`

- `bool AutoZoom`

- `bool InteractOnFirstClick`

- `MediaControls Controls`

- `string HomeURL`

- `string CurrentURL`

- `int Height`

- `int Width`

- `MediaPermission ControlPermissions`

- `MediaPermission InteractPermissions`

- `bool EnableWhiteList`

- `string[] WhiteList`


## Primitive (class) — LibreMetaverse.Assets/Primitives/ObjectMedia.cs

- `string MediaVersion`

- `MediaEntry[] FaceMedia`


## LiveParticle (struct) — LibreMetaverse.Assets/Primitives/ParticleSimulator.cs

- `Vector3 Position`

- `Vector3 Velocity`

- `float Age`

- `float NormalizedAge`

- `Color4 Color`

- `float ScaleX`

- `float ScaleY`

- `float Glow`


## ParticleSimulator (class) — LibreMetaverse.Assets/Primitives/ParticleSimulator.cs

- `Vector3 SourcePosition`

- `Vector3 TargetPosition`

- `Quaternion SourceRotation`

- `Vector3 Wind`

- `float SystemAge`

- `bool IsActive`


## Primitive (class) — LibreMetaverse.Assets/Primitives/ParticleSystem.cs

- `uint CRC`

- `uint PartFlags`

- `SourcePattern Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`


## ParticleSystem (struct) — LibreMetaverse.Assets/Primitives/ParticleSystem.cs

- `uint CRC`

- `uint PartFlags`

- `SourcePattern Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `byte BurstPartCount`


## SourcePattern (enum) — LibreMetaverse.Assets/Primitives/ParticleSystem.cs

- `uint CRC`

- `uint PartFlags`

- `SourcePattern Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `byte BurstPartCount`

- `Vector3 AngularVelocity`


## ParticleDataFlags (enum) — LibreMetaverse.Assets/Primitives/ParticleSystem.cs

- `uint CRC`

- `uint PartFlags`

- `SourcePattern Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `byte BurstPartCount`

- `Vector3 AngularVelocity`

- `Vector3 PartAcceleration`

- `UUID Texture`

- `UUID Target`

- `ParticleDataFlags PartDataFlags`

- `float PartMaxAge`

- `Color4 PartStartColor`


## ParticleFlags (enum) — LibreMetaverse.Assets/Primitives/ParticleSystem.cs

- `uint CRC`

- `uint PartFlags`

- `SourcePattern Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `byte BurstPartCount`

- `Vector3 AngularVelocity`

- `Vector3 PartAcceleration`

- `UUID Texture`

- `UUID Target`

- `ParticleDataFlags PartDataFlags`

- `float PartMaxAge`

- `Color4 PartStartColor`

- `Color4 PartEndColor`

- `float PartStartScaleX`

- `float PartStartScaleY`

- `float PartEndScaleX`

- `float PartEndScaleY`

- `float PartStartGlow`

- `float PartEndGlow`

- `byte BlendFuncSource`

- `byte BlendFuncDest`


## BlendFunc (enum) — LibreMetaverse.Assets/Primitives/ParticleSystem.cs

- `uint CRC`

- `uint PartFlags`

- `SourcePattern Pattern`

- `float MaxAge`

- `float StartAge`

- `float InnerAngle`

- `float OuterAngle`

- `float BurstRate`

- `float BurstRadius`

- `float BurstSpeedMin`

- `float BurstSpeedMax`

- `byte BurstPartCount`

- `Vector3 AngularVelocity`

- `Vector3 PartAcceleration`

- `UUID Texture`

- `UUID Target`

- `ParticleDataFlags PartDataFlags`

- `float PartMaxAge`

- `Color4 PartStartColor`

- `Color4 PartEndColor`

- `float PartStartScaleX`

- `float PartStartScaleY`

- `float PartEndScaleX`

- `float PartEndScaleY`

- `float PartStartGlow`

- `float PartEndGlow`

- `byte BlendFuncSource`

- `byte BlendFuncDest`

- `byte MaxDataBlockSize`

- `byte LegacyDataBlockSize`

- `byte SysDataSize`

- `byte PartDataSize`


## Primitive (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `class ConstructionData`

- `byte profileCurve`

- `PathCurve PathCurve`

- `float PathEnd`

- `float PathRadiusOffset`

- `float PathSkew`

- `float PathScaleX`

- `float PathScaleY`

- `float PathShearX`

- `float PathShearY`

- `float PathTaperX`

- `float PathTaperY`

- `float PathBegin`

- `float PathTwist`

- `float PathTwistBegin`

- `float PathRevolutions`

- `float ProfileBegin`

- `float ProfileEnd`

- `float ProfileHollow`

- `Material Material`

- `byte State`

- `PCode PCode`

- `AttachmentPoint AttachmentPoint`

- `ProfileCurve ProfileCurve`

- `HoleType ProfileHole`

- `Vector2 PathBeginScale`

- `Vector2 PathEndScale`


## ConstructionData (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `byte profileCurve`

- `PathCurve PathCurve`

- `float PathEnd`

- `float PathRadiusOffset`

- `float PathSkew`

- `float PathScaleX`

- `float PathScaleY`

- `float PathShearX`

- `float PathShearY`

- `float PathTaperX`

- `float PathTaperY`

- `float PathBegin`

- `float PathTwist`

- `float PathTwistBegin`

- `float PathRevolutions`

- `float ProfileBegin`

- `float ProfileEnd`

- `float ProfileHollow`

- `Material Material`

- `byte State`

- `PCode PCode`

- `AttachmentPoint AttachmentPoint`

- `ProfileCurve ProfileCurve`

- `HoleType ProfileHole`

- `Vector2 PathBeginScale`

- `Vector2 PathEndScale`


## FlexibleData (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `int Softness`

- `float Gravity`

- `float Drag`

- `float Wind`

- `float Tension`

- `Vector3 Force`

- `class LightData`

- `Color4 Color`

- `float Intensity`

- `float Radius`

- `float Cutoff`

- `float Falloff`


## LightData (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `Color4 Color`

- `float Intensity`

- `float Radius`

- `float Cutoff`

- `float Falloff`

- `class LightImage`

- `UUID LightTexture`

- `Vector3 Params`


## LightImage (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `UUID LightTexture`

- `Vector3 Params`

- `class SculptData`

- `UUID SculptTexture`

- `SculptType Type`

- `bool Invert`

- `bool Mirror`

- `class ObjectProperties`

- `UUID ObjectID`

- `UUID CreatorID`

- `UUID OwnerID`

- `UUID GroupID`

- `DateTime CreationDate`

- `Permissions Permissions`

- `int OwnershipCost`

- `SaleType SaleType`

- `int SalePrice`

- `byte AggregatePerms`


## SculptData (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `UUID SculptTexture`

- `SculptType Type`

- `bool Invert`

- `bool Mirror`

- `class ObjectProperties`

- `UUID ObjectID`

- `UUID CreatorID`

- `UUID OwnerID`

- `UUID GroupID`

- `DateTime CreationDate`

- `Permissions Permissions`

- `int OwnershipCost`

- `SaleType SaleType`

- `int SalePrice`

- `byte AggregatePerms`

- `byte AggregatePermTextures`

- `byte AggregatePermTexturesOwner`

- `ObjectCategory Category`

- `short InventorySerial`

- `UUID ItemID`

- `UUID FolderID`

- `UUID FromTaskID`

- `UUID LastOwnerID`

- `string Name`

- `string Description`

- `string TouchName`

- `string SitName`

- `UUID[] TextureIDs`


## ObjectProperties (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `UUID ObjectID`

- `UUID CreatorID`

- `UUID OwnerID`

- `UUID GroupID`

- `DateTime CreationDate`

- `Permissions Permissions`

- `int OwnershipCost`

- `SaleType SaleType`

- `int SalePrice`

- `byte AggregatePerms`

- `byte AggregatePermTextures`

- `byte AggregatePermTexturesOwner`

- `ObjectCategory Category`

- `short InventorySerial`

- `UUID ItemID`

- `UUID FolderID`

- `UUID FromTaskID`

- `UUID LastOwnerID`

- `string Name`

- `string Description`

- `string TouchName`

- `string SitName`

- `UUID[] TextureIDs`

- `class PhysicsProperties`

- `uint LocalID`

- `float Density`

- `float Friction`

- `float GravityMultiplier`

- `PhysicsShapeType PhysicsShapeType`

- `float Restitution`

- `UUID ID`

- `uint ParentID`


## PhysicsProperties (class) — LibreMetaverse.Assets/Primitives/Primitive.cs

- `uint LocalID`

- `float Density`

- `float Friction`

- `float GravityMultiplier`

- `PhysicsShapeType PhysicsShapeType`

- `float Restitution`

- `UUID ID`

- `UUID GroupID`

- `uint ParentID`

- `ulong RegionHandle`

- `PrimFlags Flags`

- `Tree TreeSpecies`

- `Grass GrassSpecies`

- `byte[] ScratchPad`

- `Vector3 Position`

- `Vector3 Scale`

- `Quaternion Rotation`

- `Vector3 Velocity`

- `Vector3 AngularVelocity`

- `Vector3 Acceleration`

- `Vector4 CollisionPlane`

- `FlexibleData Flexible`

- `LightData Light`

- `LightImage LightMap`

- `SculptData? Sculpt`

- `UInt32 ExtendedMeshFlags`

- `List<Animation>? SignaledAnimations`

- `ClickAction ClickAction`

- `UUID Sound`

- `UUID OwnerID`

- `SoundFlags SoundFlags`


## Bumpiness (enum) — LibreMetaverse.Assets/Primitives/TextureEntry.cs


## Shininess (enum) — LibreMetaverse.Assets/Primitives/TextureEntry.cs


## MappingType (enum) — LibreMetaverse.Assets/Primitives/TextureEntry.cs


## TextureAttributes (enum) — LibreMetaverse.Assets/Primitives/TextureEntry.cs


## Primitive (class) — LibreMetaverse.Assets/Primitives/TextureEntry.cs

- `bool Valid`

- `Color4 RGBA`

- `float RepeatU`

- `float RepeatV`

- `float OffsetU`

- `float OffsetV`

- `float Rotation`

- `float Glow`

- `Bumpiness Bump`


## TextureAnimMode (enum) — LibreMetaverse.Assets/Primitives/TextureEntry.cs

- `bool Valid`

- `Color4 RGBA`

- `float RepeatU`

- `float RepeatV`

- `float OffsetU`

- `float OffsetV`

- `float Rotation`

- `float Glow`

- `Bumpiness Bump`


## TextureEntryFace (class) — LibreMetaverse.Assets/Primitives/TextureEntry.cs

- `bool Valid`

- `Color4 RGBA`

- `float RepeatU`

- `float RepeatV`

- `float OffsetU`

- `float OffsetV`

- `float Rotation`

- `float Glow`

- `Bumpiness Bump`

- `Shininess Shiny`

- `bool Fullbright`


## TextureEntry (class) — LibreMetaverse.Assets/Primitives/TextureEntry.cs

- `int MAX_FACES`

- `UUID WHITE_TEXTURE`

- `TextureEntryFace? DefaultTexture`

- `TextureEntryFace[] FaceTextures`


## TextureAnimation (struct) — LibreMetaverse.Assets/Primitives/TextureEntry.cs

- `TextureAnimMode Flags`

- `uint Face`

- `uint SizeX`

- `uint SizeY`

- `float Start`

- `float Length`

- `float Rate`

- `TextureEntry? Textures`

- `TextureAnimation TextureAnim`


## AnimeshSkinning (class) — LibreMetaverse.Assets/Rendering/AnimeshSkinning.cs


## AttachmentRiggedSkin (class) — LibreMetaverse.Assets/Rendering/AttachmentRiggedSkin.cs

- `string[] JointNames`

- `System.Numerics.Matrix4x4[] InvBindMatrices`

- `int[] Joints`

- `float[] Weights`

- `UUID MeshId`

- `bool LockScaleIfJointPosition`


## RiggedSkinMath (class) — LibreMetaverse.Assets/Rendering/AttachmentRiggedSkin.cs


## AvatarBoneMath (class) — LibreMetaverse.Assets/Rendering/AvatarBoneMath.cs


## AvatarPhysicsSimulator (class) — LibreMetaverse.Assets/Rendering/AvatarPhysicsSimulator.cs


## PhysicsVolumeMorphs (class) — LibreMetaverse.Assets/Rendering/AvatarPhysicsSimulator.cs


## EndianAwareBinaryReader (class) — LibreMetaverse.Assets/Rendering/EndianAwareBinaryReader.cs

- `enum SourceFormat`


## SourceFormat (enum) — LibreMetaverse.Assets/Rendering/EndianAwareBinaryReader.cs


## AvatarAttachmentPoint (class) — LibreMetaverse.Assets/Rendering/LindenAvatarDefinition.cs

- `int Id`

- `int Group`

- `string Name`

- `string Joint`

- `string Location`

- `Vector3 Position`

- `Vector3 Rotation`

- `bool VisibleInFirstPerson`


## AvatarMeshDefinition (class) — LibreMetaverse.Assets/Rendering/LindenAvatarDefinition.cs

- `string Type`

- `int LodLevel`

- `string FileName`

- `int MinPixelWidth`


## BoneTransform (struct) — LibreMetaverse.Assets/Rendering/LindenAvatarDefinition.cs

- `Vector3 Position`

- `Vector3 Scale`


## LindenAvatarDefinition (class) — LibreMetaverse.Assets/Rendering/LindenAvatarDefinition.cs

- `LindenSkeleton Skeleton`

- `IReadOnlyList<AvatarAttachmentPoint> AttachmentPoints`

- `IReadOnlyList<AvatarMeshDefinition> MeshDefinitions`


## LindenMesh (class) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `LindenSkeleton? Skeleton`

- `struct Face`

- `short[] Indices`

- `struct Vertex`

- `Vector3 Coord`

- `Vector3 Normal`

- `Vector3 BiNormal`

- `Vector2 TexCoord`

- `Vector2 DetailTexCoord`

- `float Weight`

- `struct MorphVertex`

- `uint VertexIndex`

- `struct Morph`

- `string Name`

- `int NumVertices`

- `MorphVertex[] Vertices`

- `struct VertexRemap`

- `int RemapSource`

- `int RemapDestination`

- `class ReferenceMesh`

- `float MinPixelWidth`

- `string Header`

- `bool HasWeights`

- `bool HasDetailTexCoords`


## Face (struct) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `short[] Indices`

- `struct Vertex`

- `Vector3 Coord`

- `Vector3 Normal`

- `Vector3 BiNormal`

- `Vector2 TexCoord`

- `Vector2 DetailTexCoord`

- `float Weight`

- `struct MorphVertex`

- `uint VertexIndex`

- `struct Morph`

- `string Name`

- `int NumVertices`

- `MorphVertex[] Vertices`

- `struct VertexRemap`

- `int RemapSource`

- `int RemapDestination`

- `class ReferenceMesh`

- `float MinPixelWidth`

- `string Header`

- `bool HasWeights`

- `bool HasDetailTexCoords`

- `Vector3 Position`

- `Vector3 RotationAngles`

- `byte RotationOrder`

- `Vector3 Scale`


## Vertex (struct) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `Vector3 Coord`

- `Vector3 Normal`

- `Vector3 BiNormal`

- `Vector2 TexCoord`

- `Vector2 DetailTexCoord`

- `float Weight`

- `struct MorphVertex`

- `uint VertexIndex`

- `struct Morph`

- `string Name`

- `int NumVertices`

- `MorphVertex[] Vertices`

- `struct VertexRemap`

- `int RemapSource`

- `int RemapDestination`

- `class ReferenceMesh`

- `float MinPixelWidth`

- `string Header`

- `bool HasWeights`

- `bool HasDetailTexCoords`

- `Vector3 Position`

- `Vector3 RotationAngles`

- `byte RotationOrder`

- `Vector3 Scale`

- `ushort NumFaces`

- `Face[] Faces`


## MorphVertex (struct) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `uint VertexIndex`

- `Vector3 Coord`

- `Vector3 Normal`

- `Vector3 BiNormal`

- `Vector2 TexCoord`

- `struct Morph`

- `string Name`

- `int NumVertices`

- `MorphVertex[] Vertices`

- `struct VertexRemap`

- `int RemapSource`

- `int RemapDestination`

- `class ReferenceMesh`

- `float MinPixelWidth`

- `string Header`

- `bool HasWeights`

- `bool HasDetailTexCoords`

- `Vector3 Position`

- `Vector3 RotationAngles`

- `byte RotationOrder`

- `Vector3 Scale`

- `ushort NumFaces`

- `Face[] Faces`


## Morph (struct) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `string Name`

- `int NumVertices`

- `MorphVertex[] Vertices`

- `struct VertexRemap`

- `int RemapSource`

- `int RemapDestination`

- `class ReferenceMesh`

- `float MinPixelWidth`

- `string Header`

- `bool HasWeights`

- `bool HasDetailTexCoords`

- `Vector3 Position`

- `Vector3 RotationAngles`

- `byte RotationOrder`

- `Vector3 Scale`

- `ushort NumFaces`

- `Face[] Faces`


## VertexRemap (struct) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `int RemapSource`

- `int RemapDestination`

- `class ReferenceMesh`

- `float MinPixelWidth`

- `string Header`

- `bool HasWeights`

- `bool HasDetailTexCoords`

- `Vector3 Position`

- `Vector3 RotationAngles`

- `byte RotationOrder`

- `Vector3 Scale`

- `ushort NumFaces`

- `Face[] Faces`

- `string Name`

- `ushort NumVertices`

- `Vertex[] Vertices`

- `ushort NumSkinJoints`

- `string[] SkinJoints`

- `int NumRemaps`

- `VertexRemap[] VertexRemaps`


## ReferenceMesh (class) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `float MinPixelWidth`

- `string Header`

- `bool HasWeights`

- `bool HasDetailTexCoords`

- `Vector3 Position`

- `Vector3 RotationAngles`

- `byte RotationOrder`

- `Vector3 Scale`

- `ushort NumFaces`

- `Face[] Faces`

- `string Name`

- `ushort NumVertices`

- `Vertex[] Vertices`

- `ushort NumSkinJoints`

- `string[] SkinJoints`

- `int NumRemaps`

- `VertexRemap[] VertexRemaps`

- `Morph[] Morphs`


## SkinWeightElement (struct) — LibreMetaverse.Assets/Rendering/LindenMesh.cs

- `string Bone1`

- `string Bone2`

- `float Weight1`

- `float Weight2`

- `List<SkinWeightElement> SkinWeights`


## JointSupportCategory (enum) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Ext.cs


## JointBase (class) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Ext.cs

- `JointSupportCategory SupportCategory`


## Joint (class) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Ext.cs


## LindenSkeleton (class) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Ext.cs


## LindenSkeleton (class) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Xsd.cs

- `Joint bone`

- `float version`

- `bool versionSpecified`

- `string num_bones`

- `string num_collision_volumes`


## Joint (class) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Xsd.cs

- `CollisionVolume[] collision_volume`

- `Joint[] bone`

- `float[] pivot`

- `string aliases`

- `bool connected`


## CollisionVolume (class) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Xsd.cs


## JointBase (class) — LibreMetaverse.Assets/Rendering/LindenSkeleton.Xsd.cs

- `string name`

- `float[] pos`

- `float[] rot`

- `float[] scale`

- `string group`

- `string support`

- `float[] end`

- `bool reposition`


## FaceType (enum) — LibreMetaverse.Assets/Rendering/Rendering.cs


## FaceMask (enum) — LibreMetaverse.Assets/Rendering/Rendering.cs


## DetailLevel (enum) — LibreMetaverse.Assets/Rendering/Rendering.cs


## Vertex (struct) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `Vector3 Position`

- `Vector3 Normal`

- `Vector2 TexCoord`

- `bool operator`


## ProfileFace (struct) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `int Index`

- `int Count`

- `float ScaleU`

- `bool Cap`

- `bool Flat`

- `FaceType Type`


## Profile (struct) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `float MinX`

- `float MaxX`

- `bool Open`

- `bool Concave`

- `int TotalOutsidePoints`

- `List<Vector3> Positions`

- `List<ProfileFace> Faces`


## PathPoint (struct) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `Vector3 Position`

- `Vector2 Scale`

- `Quaternion Rotation`

- `float TexT`


## Path (struct) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `List<PathPoint> Points`

- `bool Open`


## Face (struct) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `int BeginS`

- `int BeginT`

- `int NumS`

- `int NumT`

- `int ID`

- `Vector3 Center`

- `Vector3 MinExtent`

- `Vector3 MaxExtent`

- `List<Vertex> Vertices`

- `List<ushort> Indices`

- `List<int> Edge`

- `FaceMask Mask`

- `Primitive.TextureEntryFace TextureFace`

- `object UserData`

- `List<VertexWeight> Weights`

- `List<Vector2>? TexCoords1`

- `Vector3 NormalizedScale`


## VertexWeight (struct) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `int Joint0`

- `int Joint1`

- `int Joint2`

- `int Joint3`

- `float Weight0`

- `float Weight1`

- `float Weight2`

- `float Weight3`


## MeshSkinData (class) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `string[] JointNames`

- `float[] InverseBindMatrices`

- `float[] BindShapeMatrix`

- `float PelvisOffset`

- `float[] AltInverseBindMatrices`

- `bool LockScaleIfJointPosition`


## RenderingException (class) — LibreMetaverse.Assets/Rendering/Rendering.cs


## Mesh (class) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `Primitive Prim`

- `Path Path`

- `Profile Profile`


## FacetedMesh (class) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `List<Face> Faces`

- `MeshSkinData? SkinData`

- `int MaxFaces`

- `int MaxVerticesPerFace`

- `int MaxTrianglesPerFace`

- `int MaxSkinJoints`


## SimpleMesh (class) — LibreMetaverse.Assets/Rendering/Rendering.cs

- `List<Vertex> Vertices`

- `List<ushort> Indices`


## RenderingLoader (class) — LibreMetaverse.Assets/Rendering/Rendering.cs


## Helpers (class) — LibreMetaverse.Assets/Util/Helpers.cs

- `byte MSG_APPENDED_ACKS`

- `byte MSG_RESENT`

- `byte MSG_RELIABLE`

- `byte MSG_ZEROCODED`


## NameValue (struct) — LibreMetaverse.Assets/Util/NameValue.cs

- `enum ValueType`

- `enum ClassType`

- `enum SendtoType`

- `string Name`

- `ValueType Type`

- `ClassType Class`

- `SendtoType Sendto`

- `object? Value`


## ValueType (enum) — LibreMetaverse.Assets/Util/NameValue.cs

- `enum ClassType`

- `enum SendtoType`

- `string Name`

- `ValueType Type`

- `ClassType Class`

- `SendtoType Sendto`

- `object? Value`


## ClassType (enum) — LibreMetaverse.Assets/Util/NameValue.cs

- `enum SendtoType`

- `string Name`

- `ValueType Type`

- `ClassType Class`

- `SendtoType Sendto`

- `object? Value`


## SendtoType (enum) — LibreMetaverse.Assets/Util/NameValue.cs

- `string Name`

- `ValueType Type`

- `ClassType Class`

- `SendtoType Sendto`

- `object? Value`


## ProcessSettings (class) — LibreMetaverse.Assets/Util/ProcessSettings.cs

- `LogLevel LogLevel`

- `string ResourceDir`


## RegionDefaults (class) — LibreMetaverse.Assets/Util/RegionDefaults.cs

- `uint SizeX`

- `uint SizeY`
