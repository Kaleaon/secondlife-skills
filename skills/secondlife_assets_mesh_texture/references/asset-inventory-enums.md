# Asset and Inventory Type Enums (generated from LibreMetaverse.Types)


## AvatarTextureIndex (from LibreMetaverse.Assets/Appearance/AvatarTextureIndex.cs)

- `Unknown = -1`

- `HeadBodypaint = 0`

- `UpperShirt`

- `LowerPants`

- `EyesIris`

- `Hair`

- `UpperBodypaint`

- `LowerBodypaint`

- `LowerShoes`

- `HeadBaked,  // pre-composited`

- `UpperBaked, // pre-composited`

- `LowerBaked, // pre-composited`

- `EyesBaked,  // pre-composited`

- `LowerSocks`

- `UpperJacket`

- `LowerJacket`

- `UpperGloves`

- `UpperUndershirt`

- `LowerUnderpants`

- `Skirt`

- `SkirtBaked, // pre-composited`

- `HairBaked,  // pre-composited`

- `LowerAlpha`

- `UpperAlpha`

- `HeadAlpha`

- `EyesAlpha`

- `HairAlpha`

- `HeadTattoo`

- `UpperTattoo`

- `LowerTattoo`

- `HeadUniversalTattoo`

- `UpperUniversalTattoo`

- `LowerUniversalTattoo`

- `SkirtTattoo`

- `HairTattoo`

- `EyesTattoo`

- `LeftArmTattoo`

- `LeftLegTattoo`

- `Aux1Tattoo`

- `Aux2Tattoo`

- `Aux3Tattoo`

- `LeftArmBaked,   // pre-composited`

- `LegLegBaked,    // pre-composited`

- `Aux1Baked,  // pre-composited`

- `Aux2Baked,  // pre-composited`

- `Aux3Baked,  // pre-composited`

- `NumberOfEntries`


## GltfPrimitiveMode (from LibreMetaverse.Assets/Assets/Gltf/GltfEnums.cs)

- `Points = 0`

- `Lines = 1`

- `LineLoop = 2`

- `LineStrip = 3`

- `Triangles = 4`

- `TriangleStrip = 5`

- `TriangleFan = 6`


## InventorySortOrder (from LibreMetaverse.Assets/Inventory/InventoryEnums.cs)

- `ByName = 0`

- `ByDate = 1`

- `FoldersByName = 2`

- `SystemFoldersToTop = 4`


## InventoryItemFlags (from LibreMetaverse.Assets/Inventory/InventoryEnums.cs)

- `None = 0`

- `ObjectSlamPerm = 0x100`

- `ObjectSlamSale = 0x1000`

- `ObjectOverwriteBase = 0x010000`

- `ObjectOverwriteOwner = 0x020000`

- `ObjectOverwriteGroup = 0x040000`

- `ObjectOverwriteEveryone = 0x080000`

- `ObjectOverwriteNextOwner = 0x100000`

- `ObjectHasMultipleItems = 0x200000`

- `SharedSingleReference = 0x40000000`


## TextureAttributes (from LibreMetaverse.Assets/Primitives/TextureEntry.cs)

- `None = 0`

- `TextureID = 1 << 0`

- `RGBA = 1 << 1`

- `RepeatU = 1 << 2`

- `RepeatV = 1 << 3`

- `OffsetU = 1 << 4`

- `OffsetV = 1 << 5`

- `Rotation = 1 << 6`

- `Material = 1 << 7`

- `Media = 1 << 8`

- `Glow = 1 << 9`

- `MaterialID = 1 << 10`

- `RenderMaterialID = 1 << 11`

- `All = 0xFFFFFFFF`


## TextureAnimMode (from LibreMetaverse.Assets/Primitives/TextureEntry.cs)

- `ANIM_OFF = 0x00`

- `ANIM_ON = 0x01`

- `LOOP = 0x02`

- `REVERSE = 0x04`

- `PING_PONG = 0x08`

- `SMOOTH = 0x10`

- `ROTATE = 0x20`

- `SCALE = 0x40`


## FaceType (from LibreMetaverse.Assets/Rendering/Rendering.cs)

- `PathBegin = 0x1 << 0`

- `PathEnd = 0x1 << 1`

- `InnerSide = 0x1 << 2`

- `ProfileBegin = 0x1 << 3`

- `ProfileEnd = 0x1 << 4`

- `OuterSide0 = 0x1 << 5`

- `OuterSide1 = 0x1 << 6`

- `OuterSide2 = 0x1 << 7`

- `OuterSide3 = 0x1 << 8`


## EstateAssetType (from LibreMetaverse.Protocol/AssetTransferEnums.cs)

- `None = -1`

- `Covenant = 0`


## RlvAttachmentPoint (from LibreMetaverse.RLV/RlvAttachmentPoint.cs)

- `Default`

- `Chest`

- `Skull`

- `LeftShoulder`

- `RightShoulder`

- `LeftHand`

- `RightHand`

- `LeftFoot`

- `RightFoot`

- `Spine`

- `Pelvis`

- `Mouth`

- `Chin`

- `LeftEar`

- `RightEar`

- `LeftEyeball`

- `RightEyeball`

- `Nose`

- `RightUpperArm`

- `RightForearm`

- `LeftUpperArm`

- `LeftForearm`

- `RightHip`

- `RightUpperLeg`

- `RightLowerLeg`

- `LeftHip`

- `LeftUpperLeg`

- `LeftLowerLeg`

- `Stomach`

- `LeftPec`

- `RightPec`

- `HUDCenter2`

- `HUDTopRight`

- `HUDTop`

- `HUDTopLeft`

- `HUDCenter`

- `HUDBottomLeft`

- `HUDBottom`

- `HUDBottomRight`

- `Neck`

- `AvatarCenter`

- `LeftHandRing`

- `RightHandRing`

- `TailBase`

- `TailTip`

- `LeftWing`

- `RightWing`

- `Jaw`

- `AltLeftEar`

- `AltRightEar`

- `AltLeftEye`

- `AltRightEye`

- `Tongue`

- `Groin`

- `LeftHindFoot`

- `RightHindFoot`


## RlvWearableType (from LibreMetaverse.RLV/RlvWearableType.cs)

- `Shape = 0`

- `Skin = 1`

- `Hair = 2`

- `Eyes = 3`

- `Shirt = 4`

- `Pants = 5`

- `Shoes = 6`

- `Socks = 7`

- `Jacket = 8`

- `Gloves = 9`

- `Undershirt = 10`

- `Underpants = 11`

- `Skirt = 12`

- `Alpha = 13`

- `Tattoo = 14`

- `Physics = 15`

- `Universal = 16`

- `Invalid = 255`


## AssetType (from LibreMetaverse.Types/Enums.cs)

- `[EnumInfo(Text = "invalid")]`

- `Unknown = -1`

- `[EnumInfo (Text = "texture")]`

- `Texture = 0`

- `[EnumInfo(Text = "sound")]`

- `Sound = 1`

- `[EnumInfo(Text = "callcard")]`

- `CallingCard = 2`

- `[EnumInfo(Text = "landmark")]`

- `Landmark = 3`

- `[Obsolete("No longer used")]`

- `[EnumInfo(Text = "script")]`

- `Script = 4`

- `[EnumInfo(Text = "clothing")]`

- `Clothing = 5`

- `[EnumInfo(Text = "object")]`

- `Object = 6`

- `[EnumInfo(Text = "notecard")]`

- `Notecard = 7`

- `[EnumInfo(Text = "category")]`

- `Folder = 8`

- `[EnumInfo(Text = "lsltext")]`

- `LSLText = 10`

- `[EnumInfo(Text = "lslbyte")]`

- `LSLBytecode = 11`

- `[EnumInfo(Text = "txtr_tga")]`

- `TextureTGA = 12`

- `[EnumInfo(Text = "bodypart")]`

- `Bodypart = 13`

- `[EnumInfo(Text = "snd_wav")]`

- `SoundWAV = 17`

- `[EnumInfo(Text = "img_tga")]`

- `ImageTGA = 18`

- `[EnumInfo(Text = "jpeg")]`

- `ImageJPEG = 19`

- `[EnumInfo(Text = "animatn")]`

- `Animation = 20`

- `[EnumInfo(Text = "gesture")]`

- `Gesture = 21`

- `[EnumInfo(Text = "simstate")]`

- `Simstate = 22`

- `[EnumInfo(Text = "link")]`

- `Link = 24`

- `[EnumInfo(Text = "link_f")]`

- `LinkFolder = 25`

- `[EnumInfo(Text = "mesh")]`

- `Mesh = 49`

- `[EnumInfo(Text = "widget")]`

- `Widget = 40`

- `[EnumInfo(Text = "person")]`

- `Person = 45`

- `[EnumInfo(Text = "settings")]`

- `Settings = 56`

- `[EnumInfo(Text = "material")]`

- `Material = 57`


## InventoryType (from LibreMetaverse.Types/Enums.cs)

- `Unknown = -1`

- `Texture = 0`

- `Sound = 1`

- `CallingCard = 2`

- `Landmark = 3`

- `/*`

- `[Obsolete("See LSL")] Script = 4`

- `[Obsolete("See Wearable")] Clothing = 5`

- `*/`

- `Object = 6`

- `Notecard = 7`

- `Category = 8`

- `Folder = 8`

- `RootCategory = 9`

- `LSL = 10`

- `/*`

- `*/`

- `Snapshot = 15`

- `/*`

- `*/`

- `Attachment = 17`

- `Wearable = 18`

- `Animation = 19`

- `Gesture = 20`

- `Mesh = 22`

- `Widget = 23`

- `Person = 24`

- `Settings = 25`

- `Material = 26`

- `GLTF = 27`

- `GLTFBin = 28`


## SaleType (from LibreMetaverse.Types/Enums.cs)

- `Not = 0`

- `Original = 1`

- `Copy = 2`

- `Contents = 3`


## WearableType (from LibreMetaverse.Types/Enums.cs)

- `[EnumInfo(Text = "Shape")]`

- `Shape = 0`

- `[EnumInfo(Text = "Skin")]`

- `Skin`

- `[EnumInfo(Text = "Hair")]`

- `Hair`

- `[EnumInfo(Text = "Eyes")]`

- `Eyes`

- `[EnumInfo(Text = "Shirt")]`

- `Shirt`

- `[EnumInfo(Text = "Pants")]`

- `Pants`

- `[EnumInfo(Text = "Shoes")]`

- `Shoes`

- `[EnumInfo(Text = "Socks")]`

- `Socks`

- `[EnumInfo(Text = "Jacket")]`

- `Jacket`

- `[EnumInfo(Text = "Gloves")]`

- `Gloves`

- `[EnumInfo(Text = "Undershirt")]`

- `Undershirt`

- `[EnumInfo(Text = "Underpants")]`

- `Underpants`

- `[EnumInfo(Text = "Skirt")]`

- `Skirt`

- `[EnumInfo(Text = "Alpha")]`

- `Alpha`

- `[EnumInfo(Text = "Tattoo")]`

- `Tattoo`

- `[EnumInfo(Text = "Physics")]`

- `Physics`

- `[EnumInfo(Text = "Universal")]`

- `Universal`

- `[EnumInfo(Text = "Invalid")]`

- `Invalid = 255`


## PCode (from LibreMetaverse.Types/EnumsPrimitive.cs)

- `None = 0`

- `Prim = 9`

- `Avatar = 47`

- `Grass = 95`

- `NewTree = 111`

- `ParticleSystem = 143`

- `Tree = 255`


## PrimFlags (from LibreMetaverse.Types/EnumsPrimitive.cs)

- `None = 0`

- `Physics = 0x00000001`

- `CreateSelected = 0x00000002`

- `ObjectModify = 0x00000004`

- `ObjectCopy = 0x00000008`

- `ObjectAnyOwner = 0x00000010`

- `ObjectYouOwner = 0x00000020`

- `Scripted = 0x00000040`

- `Touch = 0x00000080`

- `ObjectMove = 0x00000100`

- `Money = 0x00000200`

- `Phantom = 0x00000400`

- `InventoryEmpty = 0x00000800`

- `JointHinge = 0x00001000`

- `JointP2P = 0x00002000`

- `JointLP2P = 0x00004000`

- `JointWheel = 0x00008000`

- `AllowInventoryDrop = 0x00010000`

- `ObjectTransfer = 0x00020000`

- `ObjectGroupOwned = 0x00040000`

- `ObjectYouOfficer = 0x00080000`

- `CameraDecoupled = 0x00100000`

- `AnimSource = 0x00200000`

- `CameraSource = 0x00400000`

- `CastShadows = 0x00800000`

- `DieAtEdge = 0x01000000`

- `ReturnAtEdge = 0x02000000`

- `Sandbox = 0x04000000`

- `Flying = 0x08000000`

- `ObjectOwnerModify = 0x10000000`

- `TemporaryOnRez = 0x20000000`

- `Temporary = 0x40000000`

- `ZlibCompressed = 0x80000000`


## PrimType (from LibreMetaverse.Types/EnumsPrimitive.cs)

- `Unknown`

- `Box`

- `Cylinder`

- `Prism`

- `Sphere`

- `Torus`

- `Tube`

- `Ring`

- `Sculpt`

- `Mesh`


## FaceType (from LibreMetaverse.Types/EnumsPrimitive.cs)

- `PathBegin = 0x1 << 0`

- `PathEnd = 0x1 << 1`

- `InnerSide = 0x1 << 2`

- `ProfileBegin = 0x1 << 3`

- `ProfileEnd = 0x1 << 4`

- `OuterSide0 = 0x1 << 5`

- `OuterSide1 = 0x1 << 6`

- `OuterSide2 = 0x1 << 7`

- `OuterSide3 = 0x1 << 8`


## ObjectCategory (from LibreMetaverse.Types/EnumsPrimitive.cs)

- `Invalid = -1`

- `None = 0`

- `Owner`

- `Group`

- `Other`

- `Selected`

- `Temporary`


## AttachmentPoint (from LibreMetaverse.Types/EnumsPrimitive.cs)

- `[EnumInfo(Text = "Default")]`

- `Default = 0`

- `[EnumInfo(Text = "Chest")]`

- `Chest = 1`

- `[EnumInfo(Text = "Head")]`

- `Skull`

- `[EnumInfo(Text = "Left Shoulder")]`

- `LeftShoulder`

- `[EnumInfo(Text = "Right Shoulder")]`

- `RightShoulder`

- `[EnumInfo(Text = "Left Hand")]`

- `LeftHand`

- `[EnumInfo(Text = "Right Hand")]`

- `RightHand`

- `[EnumInfo(Text = "Left Foot")]`

- `LeftFoot`

- `[EnumInfo(Text = "Right Foot")]`

- `RightFoot`

- `[EnumInfo(Text = "Back")]`

- `Spine`

- `[EnumInfo(Text = "Pelvis")]`

- `Pelvis`

- `[EnumInfo(Text = "Mouth")]`

- `Mouth`

- `[EnumInfo(Text = "Chin")]`

- `Chin`

- `[EnumInfo(Text = "Left Ear")]`

- `LeftEar`

- `[EnumInfo(Text = "Right Ear")]`

- `RightEar`

- `[EnumInfo(Text = "Left Eye")]`

- `LeftEyeball`

- `[EnumInfo(Text = "Right Eye")]`

- `RightEyeball`

- `[EnumInfo(Text = "Nose")]`

- `Nose`

- `[EnumInfo(Text = "Right Upper Arm")]`

- `RightUpperArm`

- `[EnumInfo(Text = "Right Lower Arm")]`

- `RightForearm`

- `[EnumInfo(Text = "Left Upper Arm")]`

- `LeftUpperArm`

- `[EnumInfo(Text = "Left Lower Arm")]`

- `LeftForearm`

- `[EnumInfo(Text = "Right Hip")]`

- `RightHip`

- `[EnumInfo(Text = "Right Upper Leg")]`

- `RightUpperLeg`

- `[EnumInfo(Text = "Right Lower Leg")]`

- `RightLowerLeg`

- `[EnumInfo(Text = "Left Hip")]`

- `LeftHip`

- `[EnumInfo(Text = "Left Upper Leg")]`

- `LeftUpperLeg`

- `[EnumInfo(Text = "Left Lower Leg")]`

- `LeftLowerLeg`

- `[EnumInfo(Text = "Belly")]`

- `Stomach`

- `[EnumInfo(Text = "Left Pec")]`

- `LeftPec`

- `[EnumInfo(Text = "Right Pec")]`

- `RightPec`

- `[EnumInfo(Text = "HUD Center 2")]`

- `HUDCenter2`

- `[EnumInfo(Text = "HUD Top Right")]`

- `HUDTopRight`

- `[EnumInfo(Text = "HUD Top Center")]`

- `HUDTop`

- `[EnumInfo(Text = "HUD Top Left")]`

- `HUDTopLeft`

- `[EnumInfo(Text = "HUD Center 1")]`

- `HUDCenter`

- `[EnumInfo(Text = "HUD Bottom Left")]`

- `HUDBottomLeft`

- `[EnumInfo(Text = "HUD Bottom")]`

- `HUDBottom`

- `[EnumInfo(Text = "HUD Bottom Right")]`

- `HUDBottomRight`

- `[EnumInfo(Text = "Neck")]`

- `Neck`

- `[EnumInfo(Text = "Avatar Center")]`

- `Root`

- `[EnumInfo(Text = "Left Ring Finger")]`

- `LeftHandRing`

- `[EnumInfo(Text = "Right Ring Finger")]`

- `RightHandRing`

- `[EnumInfo(Text = "Tail Base")]`

- `TailBase`

- `[EnumInfo(Text = "Tail Tip")]`

- `TailTip`

- `[EnumInfo(Text = "Left Wing")]`

- `LeftWing`

- `[EnumInfo(Text = "Right Wing")]`

- `RightWing`

- `[EnumInfo(Text = "Jaw")]`

- `Jaw`

- `[EnumInfo(Text = "Alt Left Ear")]`

- `AltLeftEar`

- `[EnumInfo(Text = "Alt Right Ear")]`

- `AltRightEar`

- `[EnumInfo(Text = "Alt Left Eye")]`

- `AltLeftEye`

- `[EnumInfo(Text = "Alt Right Eye")]`

- `AltRightEye`

- `[EnumInfo(Text = "Tongue")]`

- `Tongue`

- `[EnumInfo(Text = "Groin")]`

- `Groin`

- `[EnumInfo(Text = "Left Hind Foot")]`

- `LeftHindFoot`

- `[EnumInfo(Text = "Right Hind Foot")]`

- `RightHindFoot`


## TextureRequestState (from LibreMetaverse/TexturePipeline.cs)

- `Pending`

- `Started`

- `Progress`

- `Finished`

- `Timeout`

- `Aborted`

- `NotFound`


## BakeType (from LibreMetaverse/Appearance/AppearanceManager.cs)

- `Unknown = -1`

- `Head = 0`

- `UpperBody = 1`

- `LowerBody = 2`

- `Eyes = 3`

- `Skirt = 4`

- `Hair = 5`

- `BakedLeftArm`

- `BakedLeftLeg`

- `BakedAux1`

- `BakedAux2`

- `BakedAux3`
