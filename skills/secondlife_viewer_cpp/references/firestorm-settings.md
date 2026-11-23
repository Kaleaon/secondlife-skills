# Firestorm Settings Reference (generated from FirestormViewer/phoenix-firestorm)

Generated from Firestorm's `indra/newview/app_settings/settings.xml` (2438 settings). Firestorm adds many settings the official viewer does not have and changes some defaults. When code or advice depends on a setting, check whether the name exists in the official viewer reference too, and state which viewer you mean.


## 360CaptureCameraFOV

- Type: U32 | Default value: `75` | Persisted: 1

- Comment: Field of view of the WebGL camera that converts the cubemap to an equirectangular image


## 360CaptureDebugSaveImage

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flag if set, saves off each cube map as an image, as well as the JavaScript data URL, for debugging purposes


## 360CaptureHideAvatars

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flag if set, removes all the avatars from the 360 snapshot


## 360CaptureJPEGEncodeQuality

- Type: U32 | Default value: `95` | Persisted: 1

- Comment: Quality value to use in the JPEG encoder (0..100)


## 360CaptureNumRenderPasses

- Type: U32 | Default value: `3` | Persisted: 1

- Comment: Number of times to render the scene while taking a snapshot


## 360CaptureOutputImageWidth

- Type: U32 | Default value: `4096` | Persisted: 1

- Comment: Width of the output 360 equirectangular image


## 360QualitySelection

- Type: U32 | Default value: `128` | Persisted: 1

- Comment: Quality level for the 360 snapshot


## AFKTimeout

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: 
        Time before automatically setting AFK (away from keyboard) mode (seconds, 0=never).
        Valid values are: 0, 120, 300, 600, 1800, 3600, 5400, 7200
      


## AbuseReportScreenshotDelay

- Type: F32 | Default value: `0.3` | Persisted: 1

- Comment: Time delay before taking screenshot to avoid UI artifacts.


## AckCollectTime

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Ack messages collection and grouping time


## ActiveFloaterTransparency

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Transparency of active floaters (floaters that have focus)


## AdminMenu

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enable the debug admin menu from the main menu.  Note: This will just allow the menu to be shown; this does not grant admin privileges.


## AdvanceSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display advanced parameter settings in snapshot interface


## AgentPause

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Ask the simulator to stop updating the agent while enabled


## AlertedUnsupportedHardware

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Set if there's unsupported hardware and we've already done a notification.


## AllowMUpose

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow MU* pose style in chat and IM (with ':' as a synonymous to '/me ')


## AllowMultipleViewers

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow multiple viewers.


## AllowNoCopyRezRestoreToWorld

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow Restore to Last Position for no-copy objects on Second Life grids. This can lead to content loss, and is only meant to be used for testing a potential server side fix.


## AllowSelectAvatar

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Allows user to select and move avatars, move is viewer sided, does not propagate to server, also supresses avatar position updates while avatars are selected


## AllowSelfImpostor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow own render time to impostor your avatar.


## AllowTapTapHoldRun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Tapping a direction key twice and holding it down makes avatar run


## AnalyzePerformance

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Request performance analysis for a particular viewer run


## AnimateTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable texture animation (debug)


## AnimatedObjectsAllowLeftClick

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow left-click interaction with animated objects. Uncertain how much performance impact this will have.


## AnimatedObjectsMaxLegalOffset

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Max visual offset between object position and rendered position


## AnimatedObjectsMaxLegalSize

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Max bounding box size for animated object's rendered position


## AppearanceCameraMovement

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When entering appearance editing mode, camera zooms in on currently selected portion of avatar


## ApplyColorImmediately

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Preview selections in color picker immediately


## ArrowKeysAlwaysMove

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: While cursor is in chat entry box, arrow keys still control your avatar


## AssetFetchConcurrency

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Maximum number of HTTP connections used for asset fetches


## AuctionShowFence

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When auctioning land, include parcel boundary marker in snapshot


## AudioLevelAmbient

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of environment sounds


## AudioLevelMaster

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Master audio level, or overall volume


## AudioLevelMedia

- Type: F32 | Default value: `0.3` | Persisted: 1

- Comment: Audio level of parcel Media


## AudioLevelMic

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Audio level of microphone input


## AudioLevelMusic

- Type: F32 | Default value: `0.3` | Persisted: 1

- Comment: Audio level of streaming music


## AudioLevelSFX

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of in-world sound effects


## AudioLevelUI

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of UI sound effects


## AudioLevelVoice

- Type: F32 | Default value: `0.7` | Persisted: 1

- Comment: Audio level of voice chat


## AudioLevelWind

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of wind noise when standing still


## AudioStreamingMedia

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable streaming


## AudioStreamingMusic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable streaming audio


## AutoAcceptNewInventory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Automatically accept new notecards/textures/landmarks


## AutoCloseOOC

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Auto-close OOC chat (i.e. add "))" if not found and "((" was used)


## AutoDisengageMic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically turn off the microphone when ending IM calls.


## AutoLeveling

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep Flycam level.


## AutoLogin

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Login automatically using last username/password combination


## AutoMimeDiscovery

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable viewer mime type discovery of media URLs


## AutoPilotLocksCamera

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Keep camera position locked when avatar walks to selected position


## AutoQueryGridStatus

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Query status.secondlifegrid.net for latest news at login.


## AutoQueryGridStatusURL

- Type: String | Default value: `https://phoenixviewer.com/app/loginV3/secondlifegrid.xml` | Persisted: 1

- Comment: URL for AutoQueryGridStatus. WordPress RSS 2.0 format.


## AutoReplace

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Replaces keywords with a configured word or phrase


## AutoSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Update snapshot when camera stops moving, or any parameter changes


## AutoTuneFPS

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow the viewer to adjust your settings to achieve target FPS


## AutoTuneImpostorByDistEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable/disable using MaxNonImpostor to limit avatar rendering by distance.


## AutoTuneImpostorFarAwayDistance

- Type: F32 | Default value: `64.0` | Persisted: 0

- Comment: Avatars beyond this range will automatically be optimized


## AutoTuneLock

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When enabled the viewer will dynamically change settings until auto tune is explicitly turned off.


## AutoTuneRenderFarClipMin

- Type: F32 | Default value: `32.0` | Persisted: 0

- Comment: The lowest draw distance that auto tune is allowed to use


## AutoTuneRenderFarClipTarget

- Type: F32 | Default value: `256.0` | Persisted: 0

- Comment: The draw distance that auto tune will try to achieve


## AutohideChatBar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hide the chat bar from the bottom button bar and only show it as an overlay when needed.


## AutomaticFly

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Fly by holding jump key or using "Fly" command (FALSE = fly by using "Fly" command only)


## AvatarAlignMini

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use the compact mini compass floater instead of the full compass.


## AvatarAxisDeadZone0

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 0 dead zone.


## AvatarAxisDeadZone1

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 1 dead zone.


## AvatarAxisDeadZone2

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 2 dead zone.


## AvatarAxisDeadZone3

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 3 dead zone.


## AvatarAxisDeadZone4

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 4 dead zone.


## AvatarAxisDeadZone5

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 5 dead zone.


## AvatarAxisScale0

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 0 scaler.


## AvatarAxisScale1

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 1 scaler.


## AvatarAxisScale2

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 2 scaler.


## AvatarAxisScale3

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 3 scaler.


## AvatarAxisScale4

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 4 scaler.


## AvatarAxisScale5

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 5 scaler.


## AvatarBakedTextureUploadTimeout

- Type: U32 | Default value: `70` | Persisted: 1

- Comment: Specifies the maximum time in seconds to wait before sending your baked textures for avatar appearance.  Set to 0 to disable and wait until all baked textures are at highest resolution.


## AvatarExtentRefreshMaxPerBatch

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: how many avatars do we want to handle in total per batch (default is 5)


## AvatarExtentRefreshPeriodBatch

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: how many frames do we spread over by default when refreshing extents (default is 4)


## AvatarFeathering

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Avatar feathering (less is softer)


## AvatarInspectorTooltipDelay

- Type: F32 | Default value: `0.35` | Persisted: 1

- Comment: Seconds before displaying avatar inspector tooltip


## AvatarNameTagMode

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Select Avatar Name Tag Mode


## AvatarPhysics

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable avatar physics.


## AvatarRotateThresholdFast

- Type: F32 | Default value: `2` | Persisted: 1

- Comment: Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving fast (degrees)


## AvatarRotateThresholdSlow

- Type: F32 | Default value: `60` | Persisted: 1

- Comment: Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving slowly (degrees)


## AvatarSex

- Type: U32 | Default value: `0` | Persisted: 0


## AvatarSitOnAway

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sit down when marked AFK


## AvatarSitRotation

- Type: Quaternion | Default value: `0 0 0 1` | Persisted: 1

- Comment: Avatar real sitting rotation used in preset


## AvatarWelcomePack

- Type: String | Default value: `https://lecs-viewer-web-components.s3.amazonaws.com/v3.0/[GRID_LOWERCASE]/vawp/index.html` | Persisted: 1

- Comment: Avatar Welcome Pack contents


## AzureTranslateAPIKey

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Azure Translation service data to use with the MS Azure Translator API


## BackgroundYieldTime

- Type: S32 | Default value: `40` | Persisted: 1

- Comment: Amount of time to yield every frame to other applications when SL is not the foreground window (milliseconds)


## BasicUITooltips

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show tooltips for various 2D UI elements like buttons or checkboxes, won't supress tooltips like drag'n'drop, inworld, links or media


## BatchSizeAIS3

- Type: S32 | Default value: `20` | Persisted: 1

- Comment: Amount of folder ais packs into category subset request


## BlockAvatarAppearanceMessages

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignores appearance messages (for simulating Ruth)


## BlockPeopleSortOrder

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Specifies sort order for recent people (0 = by name, 1 = by type)


## BrowserEnableJSObject

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: (WARNING: Advanced feature. Use if you are aware of the implications). Enable or disable the viewer to Javascript bridge object.


## BrowserFileAccessFromFileUrls

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow access to local files via file urls in the embedded browser


## BrowserIgnoreSSLCertErrors

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: FOR TESTING ONLY: Tell the built-in web browser to ignore SSL cert errors.


## BrowserJavascriptEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable JavaScript in the built-in Web browser?


## BrowserPluginsEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable Web plugins in the built-in Web browser?


## BrowserProxyAddress

- Type: String | Default value: `` | Persisted: 1

- Comment: Address for the Web Proxy]


## BrowserProxyEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Web Proxy


## BrowserProxyPort

- Type: S32 | Default value: `3128` | Persisted: 1

- Comment: Port for Web Proxy


## BrowserWebSecurityDisabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable web security features in the built-in Web browser?


## BuildAxisDeadZone0

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 0 dead zone.


## BuildAxisDeadZone1

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 1 dead zone.


## BuildAxisDeadZone2

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 2 dead zone.


## BuildAxisDeadZone3

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 3 dead zone.


## BuildAxisDeadZone4

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 4 dead zone.


## BuildAxisDeadZone5

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 5 dead zone.


## BuildAxisScale0

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 0 scaler.


## BuildAxisScale1

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 1 scaler.


## BuildAxisScale2

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 2 scaler.


## BuildAxisScale3

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 3 scaler.


## BuildAxisScale4

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 4 scaler.


## BuildAxisScale5

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 5 scaler.


## BuildFeathering

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Build feathering (less is softer)


## BulkChangeEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects can be copied by everyone


## BulkChangeIncludeAnimations

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect animations


## BulkChangeIncludeBodyParts

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect body parts


## BulkChangeIncludeClothing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect clothing


## BulkChangeIncludeGestures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect gestures


## BulkChangeIncludeMaterials

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect materials


## BulkChangeIncludeNotecards

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect notecards


## BulkChangeIncludeObjects

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect objects


## BulkChangeIncludeScripts

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect scripts


## BulkChangeIncludeSettings

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect environment settings


## BulkChangeIncludeSounds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect sounds


## BulkChangeIncludeTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect textures


## BulkChangeNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects can be copied by next owner


## BulkChangeNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects can be modified by next owner


## BulkChangeNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk changed objects can be resold or given away by next owner


## BulkChangeShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects are shared with the currently active group


## BulkUpload2KTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk upload scales textures to 2K if true, to 1K if false


## BuyCurrencyAddPaymentURL

- Type: String | Default value: `https://accounts.secondlife.com/packs/floater/add-payment-enabled` | Persisted: 1

- Comment: URL the viewer probes at login; a 200 means the L$ packs floater handles residents without a payment method


## BuyCurrencyHTML

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use HTML based L$ packs floater instead of legacy XUI version


## BuyCurrencyPacksURL

- Type: String | Default value: `https://accounts.secondlife.com/packs/floater?lang=[LANGUAGE]&shortfall=[SHORTFALL]` | Persisted: 1

- Comment: URL for the L$ packs purchase floater


## CEFRemoteDebuggingPort

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: Enable CEF remote debugging on the specified base port (1024 to 65535, 0 to disable). Each new SLPlugin gets base+N.


## CacheLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Controls the location of the local disk cache


## CacheLocationTopFolder

- Type: String | Default value: `` | Persisted: 1

- Comment: Controls the top folder location of the local disk cache


## CacheSize

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: Controls amount of hard drive space reserved for local texture caching in MB


## CacheValidateCounter

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Used to distribute cache validation


## CallLogSortOrder

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Specifies sort order for Call Log (0 = by name, 1 = by date)


## CameraAngle

- Type: F32 | Default value: `1.047197551` | Persisted: 1

- Comment: Camera field of view angle (Radians)


## CameraDoFResScale

- Type: F32 | Default value: `0.7` | Persisted: 1

- Comment: Amount to scale down depth of field resolution.  Valid range is 0.25 (quarter res) to 1.0 (full res)


## CameraFNumber

- Type: F32 | Default value: `9.0` | Persisted: 1

- Comment: Camera f-number value for DoF effect


## CameraFieldOfView

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Vertical camera field of view for DoF effect (in degrees)


## CameraFocalLength

- Type: F32 | Default value: `50` | Persisted: 1

- Comment: Camera focal length for DoF effect (in millimeters)


## CameraFocusTransitionTime

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: How many seconds it takes the camera to transition between focal distances


## CameraMaxCoF

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Maximum camera circle of confusion for DoF effect


## CameraMouseWheelZoom

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Camera zooms in and out with mouse wheel


## CameraOffset

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Render with camera offset from view frustum (rendering debug)


## CameraOffsetBuild

- Type: Vector3 | Default value: `-6.0 0.0 6.0` | Persisted: 1

- Comment: Default camera position relative to focus point when entering build mode


## CameraOffsetRearView

- Type: Vector3 | Default value: `-3.0 0.0 0.75` | Persisted: 1

- Comment: Initial camera offset from avatar in Rear View


## CameraOffsetScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scales the default offset


## CameraOpacity

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Opacity of the Camera Controls floater


## CameraPosOnLogout

- Type: Vector3D | Default value: `0.0 0.0 0.0` | Persisted: 1

- Comment: Camera position when last logged out (global coordinates)


## CameraPositionSmoothing

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Smooths camera position over time


## CameraPreset

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Preset camera position - view (0 - rear, 1 - front, 2 - group)


## CameraPresetType

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Preset camera position - view (0 - rear, 1 - front, 2 - group, 3 - custom)


## CameraZoomDistance

- Type: F32 | Default value: `2.5` | Persisted: 1

- Comment: Camera distance to the zoomed in avatar


## CameraZoomEyeZOffset

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Camera height offset of the camera itself on the zoomed in avatar from avatar center


## CameraZoomFocusZOffset

- Type: F32 | Default value: `0.6` | Persisted: 1

- Comment: Camera height offset of zoomed point on the zoomed in avatar from avatar center


## CameraZoomFraction

- Type: F32 | Default value: `0.9` | Persisted: 1

- Comment: Mousewheel driven fraction of zoom


## CefVerboseLog

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable/disable CEF verbose logging


## CertStore

- Type: String | Default value: `default` | Persisted: 1

- Comment: Specifies the Certificate Store for certificate trust verification


## ChannelBottomPanelMargin

- Type: S32 | Default value: `35` | Persisted: 1

- Comment: Space from a lower toast to the Bottom Tray


## ChatAutocompleteGestures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Auto-complete gestures in nearby chat


## ChatBubbleOpacity

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Opacity of chat bubble background (0.0 = completely transparent, 1.0 = completely opaque)


## ChatConsoleFontSize

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Size of chat text in chat console (0 to 3, small to huge)


## ChatFontSize

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Size of chat text in chat floater (0 to 3, small to huge)


## ChatFullWidth

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Chat console takes up full width of SL window


## ChatHistoryTornOff

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show chat transcript window separately from Communicate window.


## ChatLoadGroupMaxMembers

- Type: S32 | Default value: `100` | Persisted: 1

- Comment: Max number of active members we'll show up for an unresponsive group


## ChatOnlineNotification

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Provide notifications for when friend log on and off of SL


## ChatPersistTime

- Type: F32 | Default value: `20.0` | Persisted: 1

- Comment: Time for which chat stays visible in console (seconds)


## ChatServiceEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable accumulated direct-message history from Chat Service for this login.


## ChatTabDirection

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Toggles the direction of chat tabs between horizontal and vertical


## CheesyBeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable cheesy beacon effects


## ClickOnAvatarKeepsCamera

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Normally, clicking on your avatar resets the camera position. This option removes this behavior.


## ClickToWalk

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete)Click in world to walk to location


## ClientSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Client settings file name (per install).


## CloseChatOnEmptyReturn

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Close the chat transcript floater after hitting return on an empty line


## CloseChatOnReturn

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Close chat after hitting return


## CloseIMOnEmptyReturn

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Close the IM floater after hitting return on an empty line


## CmdLineChannel

- Type: String | Default value: `` | Persisted: 0

- Comment: Command line specified channel name


## CmdLineDisableVoice

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disable Voice.


## CmdLineGridChoice

- Type: String | Default value: `` | Persisted: 0

- Comment: The user's grid choice or ip address.


## CmdLineHelperURI

- Type: String | Default value: `` | Persisted: 0

- Comment: Command line specified helper web CGI prefix to use.


## CmdLineLoginLocation

- Type: String | Default value: `` | Persisted: 0

- Comment: Startup destination requested on command line


## CmdLineLoginURI

- Type: LLSD | Default value: `` | Persisted: 0

- Comment: Command line specified login server and CGI prefix to use.


## CmdLineSkipUpdater

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Command line skip updater check.


## CmdLineUpdateService

- Type: String | Default value: `` | Persisted: 0

- Comment: Override the url base for the update query.


## CollectFontVertexBuffers

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: When enabled some UI elements with cache buffers generated by fonts and reuse them. When disabled general cahce will be used with a significant overhead for hash, but it regenerates vertices each frame so it's always up to date.


## CollectUIImageVertexBuffers

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: When enabled, images will cache vertex buffers and reuse them. When disabled, the general cache will be used with significant hash-lookup overhead, but vertices are regenerated each frame so they are always up to date.


## ColorSettingsHideDefault

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show non-default settings only in Color Settings list


## ComplexityChangesPopUpDelay

- Type: U32 | Default value: `300` | Persisted: 1

- Comment: Delay before viewer will show avatar complexity notice again


## ConnectAsGod

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log in as god if you have god access.


## ConnectionPort

- Type: U32 | Default value: `13000` | Persisted: 1

- Comment: Custom connection port number


## ConnectionPortEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use the custom connection port?


## ConsoleBackgroundOpacity

- Type: F32 | Default value: `0.500` | Persisted: 1

- Comment: Opacity of chat console (0.0 = completely transparent, 1.0 = completely opaque)


## ConsoleBufferSize

- Type: S32 | Default value: `40` | Persisted: 1

- Comment: Size of chat console transcript (lines of chat)


## ConsoleMaxLines

- Type: S32 | Default value: `40` | Persisted: 1

- Comment: Max number of lines of chat text visible in console.


## ContactsTornOff

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show contacts window separately from Communicate window.


## ConversationSortOrder

- Type: U32 | Default value: `131073` | Persisted: 1

- Comment: Specifies sort key for conversations


## CookiesEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Accept cookies from Web sites?


## CoroutineStackSize

- Type: S32 | Default value: `524288` | Persisted: 1

- Comment: Size (in bytes) for each coroutine stack


## CrashHostUrl

- Type: String | Default value: `` | Persisted: 1

- Comment: A URL pointing to a crash report handler; overrides cluster negotiation to locate crash handler.


## CrashOnStartup

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: User-requested crash on viewer startup


## CrashSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Crash settings file name (per install).


## CreateToolCopyCenters

- Type: Boolean | Default value: `1` | Persisted: 0


## CreateToolCopyRotates

- Type: Boolean | Default value: `0` | Persisted: 0


## CreateToolCopySelection

- Type: Boolean | Default value: `0` | Persisted: 0


## CreateToolKeepSelected

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: After using create tool, keep the create tool active


## CurlRequestTimeOut

- Type: F32 | Default value: `120.0` | Persisted: 1

- Comment: Max idle time of a curl request before killed (requires restart)


## CurrentGrid

- Type: String | Default value: `` | Persisted: 1

- Comment: Currently Selected Grid


## CurrentMapServerURL

- Type: String | Default value: `` | Persisted: 0

- Comment: Current Session World map URL


## CurrentlyUsingBakesOnMesh

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Are we currently on a grid that uses bakes on mesh? Persisted to force rebakes on login to named grids.


## Cursor3D

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Treat Joystick values as absolute positions (not deltas).


## DAEExportConsolidateMaterials

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Combine faces with same texture


## DAEExportSingleUVMap

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: set all objects to have the same UV map name


## DAEExportSkipTransparent

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Skip exporting faces with default transparent texture or full transparent


## DAEExportTextureParams

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Apply texture params suchs as repeats to the exported UV map


## DAEExportTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Export textures when exporting Collada


## DAEExportTexturesFormat

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Image file format to use when exporting Collada


## DayCycleName

- Type: String | Default value: `Default` | Persisted: 1

- Comment: Day cycle to use. May be superseded by region settings.


## DebugAnimatedObjects

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show info related to animated objects


## DebugAvatarAppearanceMessage

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Dump a bunch of XML files when handling appearance messages


## DebugAvatarAppearanceServiceURLOverride

- Type: String | Default value: `` | Persisted: 1

- Comment: URL to use for baked texture requests; overrides value returned by login server.


## DebugAvatarCompositeBaked

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Colorize avatar meshes based on baked/composite state.


## DebugAvatarExperimentalServerAppearanceUpdate

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Experiment with sending full cof_contents instead of cof_version


## DebugAvatarJoints

- Type: String | Default value: `` | Persisted: 1

- Comment: List of joints to emit additional debugging info about.


## DebugAvatarLocalTexLoadedTime

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display time for loading avatar local textures.


## DebugAvatarRezTime

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display times for avatars to resolve.


## DebugBeaconLineWidth

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Size of lines for Debug Beacons


## DebugForceAppearanceRequestFailure

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Request wrong cof version to test the failure path for server appearance update requests.


## DebugHideEmptySystemFolders

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hide empty system folders when on


## DebugLookAtShowNames

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Show names with DebugLookAt. 0) None, 1) "Display Name (user.name)", 2) "Display Name", 3) Legacy "First Last", 4) "user.name"


## DebugObjectLODs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show info related to lod calculations for attached or animated objects


## DebugPermissions

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log permissions for selected inventory items


## DebugPluginDisableTimeout

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable the code which watches for plugins that are crashed or hung


## DebugQualityPerformance

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Allows to change performance quality directly from debug settings.


## DebugRenderHitboxes

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Renders the avatars' hitboxes (collision areas) which are unaffected by viewer side animations.


## DebugSearch

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE use search url as given in SearchURLDebug


## DebugSelectionLODs

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: Force selection to show specific LOD, -1 for off, 0 - lowest, 4 - high.


## DebugSession

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Request debugging for a particular viewer session


## DebugSettingsHideDefault

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show non-default settings only in Debug Settings list


## DebugShowAvatarRenderInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show avatar render cost information


## DebugShowColor

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Show color under cursor


## DebugShowControllerState

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display internal controller state values


## DebugShowMemory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show Total Allocated Memory


## DebugShowRenderInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show stats about current scene


## DebugShowRenderMatrices

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display values of current view and projection matrices.


## DebugShowTextureInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show interested texture info


## DebugShowTime

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show time info


## DebugShowXUINames

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show tooltips with XUI path to widget


## DebugStatModeActualIn

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeActualOut

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeAgentUpdatesSec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeAsset

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeBandwidth

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeBoundMem

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeCachedObjs

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeChildAgents

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeFPS

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeFormattedMem

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeGLMem

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeKTrisDrawnFr

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeKTrisDrawnSec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeLayers

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeLowLODObjects

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeMainAgents

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeMaterials

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeMemoryAllocated

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeNewObjs

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeObjOccluded

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeObjUnoccluded

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeObjects

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeOcclusionQueries

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePTBandwidth

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePTFPS

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePTKTrisDrawnFr

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePTKTrisDrawnSec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePTNewObjs

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePTTextureCount

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePTTotalObjs

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePacketLoss

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePacketsIn

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePacketsOut

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePhysicsFPS

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePingSim

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModePinnedObjects

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeRawCount

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeRawMem

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimActiveObjects

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimActiveScripts

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimAgentMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimFPS

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimFrameMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimImagesMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimInPPS

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimNetMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimObjects

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimOutPPS

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimPCTScriptsRun

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimPendingDownloads

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimPendingUploads

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimPumpIOMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimScriptEvents

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimScriptMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimAIStepMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimOtherMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimPCTSteppedCharacters

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimPhysicsMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimPhysicsOtherMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimPhysicsShapeUpdateMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimPhysicsStepMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSimSkippedSilhouettSteps

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSleepMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimSpareMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeSimTotalUnackedBytes

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeTexture

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeTextureCount

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeTimeDialation

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatModeTotalObjs

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatObjCacheMiss

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatTextureCacheHits

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugStatTextureCacheReadLatency

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater


## DebugViews

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display debugging info for views.


## DebugWebRTCRequireEstablishedSpatialSession

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Only report proximal channel when a spatial session is established (FIRE-36672)


## DebugWindowProc

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log windows messages


## DeepLTranslateAPIKey

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: DeepL Translation service data to use with the DeepL Translator API


## DefaultFemaleAvatar

- Type: String | Default value: `Female Shape & Outfit` | Persisted: 1

- Comment: Default Female Avatar


## DefaultLoginLocation

- Type: String | Default value: `` | Persisted: 0

- Comment: Startup destination default (if not specified on command line)


## DefaultMaleAvatar

- Type: String | Default value: `Male Shape & Outfit` | Persisted: 1

- Comment: Default Male Avatar


## DefaultUploadPermissionsConverted

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Default upload permissions have been converted to default creation permissions


## DeferProfilingUntilConnected

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable profiling data collection only after server connects. Lowers memory overhead and allows profiling from a specific point in time


## DestinationGuideURL

- Type: String | Default value: `https://secondlife.com/destinations/whats-hot-now?ctx=viewer` | Persisted: 1

- Comment: Destination guide contents


## DialogStackIconVisible

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal, volatile control that defines if the dialog stack browser icon is visible.


## DisableAllRenderFeatures

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disables all rendering features.


## DisableAllRenderTypes

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disables all rendering types.


## DisableCameraConstraints

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable the normal bounds put on the camera by avatar position


## DisableCameraJoystickCenterReset

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable center reset on camera joysticks (bullseye) in camera controls.


## DisableCrashLogger

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Do not send crash report to Linden server


## DisableExternalBrowser

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable opening an external browser.


## DisableLookAtAnimation

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Avatar follows cursor with avatars eyes, when disabled, avatar will look forward


## DisableTextHyperlinkActions

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable highlighting and linking of URLs in XUI text boxes


## DiskCacheDirName

- Type: String | Default value: `cache` | Persisted: 1

- Comment: The name of the disk cache (within the standard Viewer disk cache directory)


## DiskCachePercentOfTotal

- Type: F32 | Default value: `35.0` | Persisted: 1

- Comment: The percent of total cache size (defined by CacheSize) to use for the disk cache (ex: asset storage, excludes textures) (UNUSED)


## DiskCacheVersion

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Version number of disk cache


## DisplayTimecode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display time code on screen


## Disregard128DefaultDrawDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to use the auto default to 128 draw distance


## Disregard96DefaultDrawDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to use the auto default to 96 draw distance


## DoubleClickAutoPilot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Obsolete)Enable double-click auto pilot


## DoubleClickShowWorldMap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable double-click to show world map from mini map


## DoubleClickTeleport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable double-click to teleport where allowed (afects minimap and people panel)


## DynamicCameraStrength

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Amount camera lags behind avatar motion (0 = none, 30 = avatar velocity)


## EditCameraMovement

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When entering build mode, camera moves up above avatar


## EditLinkedParts

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Select individual parts of linked objects


## EffectScriptChatParticles

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: 1 = normal behavior, 0 = disable display of swirling lights when scripts communicate


## EmbeddedLandmarkCopyToInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Copies an embedded landmark to inventory before previewing it


## EmbeddedTextureStealsFocus

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Embedded texture preview will receive focus when opened


## EmotesUseItalic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Chat emotes are emphasized by using italic font style.


## EmulateCoreCount

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: For debugging -- number of cores to restrict the main process to, or 0 for no limit.  Requires restart.


## EnableAltZoom

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use Alt+mouse to look at and zoom in on objects


## EnableAppearance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable opening appearance from web link


## EnableAvatarPay

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable paying other avatars from web link


## EnableAvatarShare

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable sharing from web link


## EnableButtonFlashing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow UI to flash buttons to get your attention


## EnableClassifieds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable creation of new classified ads from web link


## EnableCollisionSounds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Play sounds on collision


## EnableDiscord

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When set, connect to Discord to enable Rich Presence (UNUSED)


## EnableDiskCacheDebugInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When set, display additional cache debugging information


## EnableGestureSounds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Play sounds from gestures


## EnableGrab

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Ctrl+mouse to grab and manipulate objects


## EnableGroupChatPopups

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable Incoming Group Chat Popups


## EnableIMChatPopups

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable Incoming IM Chat Popups


## EnableInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable opening inventory from web link


## EnableLookAtTarget

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to animate the avatar head and send look at targets when moving the cursor or focusing on objects (UNUSED)


## EnableMouselook

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow first person perspective and mouse control of camera


## EnablePlaceProfile

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable viewing of place profile from web link


## EnableSelectionHints

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to send editing hints to animate the arm when editing an object. (UNUSED)


## EnableUIHints

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles UI hint popups


## EnableVisualLeakDetector

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: EnableVisualLeakDetector


## EnableVoiceChat

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable talking to other residents with a microphone


## EnvironmentPersistAcrossLogin

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep Environment settings consistent across sessions


## EventURL

- Type: String | Default value: `https://events.[GRID]/viewer/embed/event/[EVENT_ID]` | Persisted: 0

- Comment: URL for Event website, displayed in the event floater


## EveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Everyone can copy the newly created objects


## ExodusLookAtLines

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render lines for LookAt focus points.


## ExodusMouselookIFF

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Draw tracking markers in mouselook for people in range if combat features are enabled


## ExodusMouselookIFFRange

- Type: F32 | Default value: `380.0` | Persisted: 1

- Comment: Draw tracking markers in mouselook for people in range if combat features are enabled


## ExodusMouselookTextHAlign

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Text alignment for target information text in mouselook if combat features are enabled


## ExodusMouselookTextOffsetX

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Text X offset for target information text in mouselook if combat features are enabled


## ExodusMouselookTextOffsetY

- Type: F32 | Default value: `-150.0` | Persisted: 1

- Comment: Text Y offset for target information text in mouselook if combat features are enabled


## ExternalEditor

- Type: String | Default value: `` | Persisted: 1

- Comment: Path to program used to edit LSL scripts and XUI files, e.g.: /usr/bin/gedit --new-window "%s"


## ExternalEditorConvertTabsToSpaces

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the script sent to the viewer from an external editor will automatically have all tabs being replaced by the default number of spaces (usually 4).


## ExternalEditorTightIntegration

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When true, Edit in External Editor launches VS Code via the code CLI with a vscode:// URI instead of using the configured external editor.


## ExternalWebsocketForwardDebug

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Forward messages and runtime errors for a script to JSONRPC client.


## ExternalWebsocketSyncEnable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the Websocket JSONRPC server when doing external script editing.


## ExternalWebsocketSyncLocal

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Should the JSONRPC server listen only for local connections.


## ExternalWebsocketSyncPort

- Type: S32 | Default value: `9020` | Persisted: 1

- Comment: Port that the JSONRPC server listens on when editing


## FMODProfilerEnable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable profiler tool if using FMOD Studio


## FMODResampleMethod

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Sets the method used for internal resampler 0(Linear), 1(Cubic), 2(Spline) for FMOD Studio


## FSAdvancedTooltips

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show extended information in hovertips about objects (classic Phoenix style)


## FSAdvancedWorldmapRegionInfo

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows additional region infos on the world map (agent count and maturity level)


## FSAllowDoubleClickOnScriptedObjects

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, allows double-click movement action (walk/teleport) to scripted objects


## FSAllowEEPWaterDerender

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow EEP assets to disable water rendering to increase FPS


## FSAlwaysFly

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Fly Override, for no-fly zones. Must be activated each time.


## FSAlwaysShowInboxButton

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the Received Items folder aka Inbox is always shown at the bottom of the inventory, even if it is shown as folder in the inventory itself.


## FSAlwaysShowTPCancel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Always show the TP cancel button even if the sim says it cant be canceled. The sim will always know if it can and will ignore cancel requests on death/god TPs anyways. Ignores RLVa (i.e. RLV restrictions can still disable it).


## FSAlwaysTrackPayments

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Always track payments even if the money tracker is closed


## FSAnimatedScriptDialogs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Animates script dialogs V1 style. Only effective when dialogs in top right are activated.


## FSAnimationPreviewExpanded

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand or collapse the advanced animation information in the animation preview floater by default


## FSAnnounceIncomingIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Opens the IM floater and announces an incoming IM as soon as somebody is starting to write an IM to you.


## FSAppearanceShowHints

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, show visual hints (avatar images) in appearance editor


## FSAreaSearchAdvanced

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Displays the advanced settings tab


## FSAreaSearchColumnConfig

- Type: U32 | Default value: `1023` | Persisted: 1

- Comment: Stores the column visibility for the area search


## FSAreaSearch_ClickAction

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Area Search Filter: Mouse click action


## FSAreaSearch_ExcludeAttachments

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Area Search Filter: Exclude attachments


## FSAreaSearch_ExcludeChildPrims

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Area Search Filter: Exclude child prims


## FSAreaSearch_ExcludeNeighborRegions

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Area Search Filter: Exclude neighbor regions


## FSAreaSearch_ExcludePhysical

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Area Search Filter: Exclude physical objects


## FSAreaSearch_ExcludeReflectionProbes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Exclude reflection probes


## FSAreaSearch_ExcludeTemporary

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Area Search Filter: Exclude temporary objects


## FSAreaSearch_FilterDistance

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Filter by distance


## FSAreaSearch_FilterForSale

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Only show objects that are for sale


## FSAreaSearch_MaximumDistance

- Type: S32 | Default value: `999999` | Persisted: 1

- Comment: Area Search Filter: Maximum distance


## FSAreaSearch_MaximumPrice

- Type: S32 | Default value: `999999` | Persisted: 1

- Comment: Area Search Filter: Maximum price


## FSAreaSearch_MinimumDistance

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Minimum distance


## FSAreaSearch_MinimumPrice

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Minimum price


## FSAreaSearch_OnlyAttachments

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only attachments


## FSAreaSearch_OnlyCopiable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only copiable objects


## FSAreaSearch_OnlyCurrentParcel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only objects in the current parcel


## FSAreaSearch_OnlyLocked

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only locked objects


## FSAreaSearch_OnlyMOAP

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only objects that have shared media applied


## FSAreaSearch_OnlyModifiable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only  modifiable objects


## FSAreaSearch_OnlyPhantom

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only phantom objects


## FSAreaSearch_OnlyPhysical

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only physical objects


## FSAreaSearch_OnlyReflectionProbes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only reflection probes


## FSAreaSearch_OnlyTemporary

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only temporary objects


## FSAreaSearch_OnlyTransferable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Area Search Filter: Find only transferable objects


## FSAudioMusicFadeIn

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Fade in time in seconds for music streams


## FSAudioMusicFadeOut

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Fade out time in seconds for music streams


## FSAutoOrderIMTabs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use automatic tab ordering for IM tabs inside the conversations floater.


## FSAutoOrderIMTabsAtTop

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Add new IM tabs as first in their chat type group.


## FSAutoOrderIMTabsPriorities

- Type: String | Default value: `210` | Persisted: 1

- Comment: Priority for automatic ordering IM tabs. Higher priority means the tab will be inserted before lower priority. Default is Groups[0]=2 Conferences[1]=1 IMs[2]=0


## FSAutoUnmuteAmbient

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If Ambient sounds are muted, unmute on TP. Default (false)


## FSAutoUnmuteSounds

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If Sound Effects are muted, unmute on TP. Default (false)


## FSAvatarTurnSpeed

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Modify the speed at which the avatar responds to turning movements. 0-100 percent of max rate. Default is 0.


## FSBeamColorFile

- Type: String | Default value: `Rainbow` | Persisted: 1

- Comment: Beam file for the shape of your beam


## FSBeamShape

- Type: String | Default value: `Phoenix` | Persisted: 1

- Comment: Beam file for the shape of your beam


## FSBeamShapeScale

- Type: F32 | Default value: `1.3` | Persisted: 1

- Comment: How Big You Want to let the beam be


## FSBetterGroupNoticesToIMLog

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Improved logging of group notices to group IM log.


## FSBeyondNearbyChatColorDiminishFactor

- Type: F32 | Default value: `0.8` | Persisted: 1

- Comment: The factor the color for nearby chat diminishes if the sender is beyond chat range


## FSBlockClickSit

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Prevents sitting on left-click.


## FSBrowserHomePage

- Type: String | Default value: `https://duckduckgo.com` | Persisted: 1

- Comment: Home page for the built in web browser


## FSBubblesHideConsoleAndToasts

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, using bubble chat will hide the chat output in the Nearby Chat console and toasts


## FSBuildPrefs_ActualRoot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show the axis on the actual root of a linkset instead of mass center


## FSBuildPrefs_Alpha

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: New object created default alpha


## FSBuildPrefs_Color

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: New object created default color


## FSBuildPrefs_EditHandleScaling

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Factor to scale editing handles.


## FSBuildPrefs_EditTextShadowing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether the hint-text while building has a drop-shadow.


## FSBuildPrefs_FullBright

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: New object created default fullbright


## FSBuildPrefs_Glow

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: New object created default glow


## FSBuildPrefs_Material

- Type: String | Default value: `Wood` | Persisted: 1

- Comment: Default Setting For New Objects to be created, physical flag


## FSBuildPrefs_Phantom

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: New object created default of phantom


## FSBuildPrefs_Physical

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: New object created default of physical


## FSBuildPrefs_PivotIsPercent

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Consider the Pivot points values as a percentage


## FSBuildPrefs_PivotX

- Type: F32 | Default value: `50` | Persisted: 1

- Comment: Pivot point on the X axis


## FSBuildPrefs_PivotY

- Type: F32 | Default value: `50` | Persisted: 1

- Comment: Pivot point on the Y axis


## FSBuildPrefs_PivotZ

- Type: F32 | Default value: `50` | Persisted: 1

- Comment: Pivot point on the Z axis


## FSBuildPrefs_Shiny

- Type: String | Default value: `None` | Persisted: 1

- Comment: New object created default shiny


## FSBuildPrefs_Temporary

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: New object created default of temporary


## FSBuildPrefs_Xsize

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Default Size For New Objects to be created X


## FSBuildPrefs_Ysize

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Default Size For New Objects to be created Y


## FSBuildPrefs_Zsize

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Default Size For New Objects to be created Z


## FSBuildToolDecimalPrecision

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Decimal digits to display on various build tool controls (0-7)


## FSChatHistoryShowYou

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show localized "You" instead of your avatar's username (like CHUI)


## FSChatWindow

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Show chat in multiple windows(by default) or in one multi-tabbed window(requires restart)


## FSChatbarGestureAutoCompleteEnable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Toggles gesture auto complete in chat bar


## FSChatbarNamePrediction

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles name prediction in nearby chat


## FSClientTagsVisibility

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Show client tags: 0=Client tags Off, 1=That are on the TPVD (needs FSUseLegacyClienttags), 2=That are on the client_tag.xml (needs FSUseLegacyClienttags), 3=That using the new system


## FSCloseChatOnReturnInMouselook

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When CloseChatOnReturn is enabled, only deselect nearby chat in mouselook


## FSCloseChatOnReturnOnlyForNearbyChatControl

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When CloseChatOnReturn is enabled, only deselect nearby chat bar


## FSCloudColorEnd

- Type: Color4 | Default value: `0.766 0.328 0.23 0.9` | Persisted: 1

- Comment: End color (and alpha) of the avatar loading/bakefail "cloud" particle effect.


## FSCloudColorStart

- Type: Color4 | Default value: `0.666 0.228 0.13 0.1` | Persisted: 1

- Comment: Start color (and alpha) of the avatar loading/bakefail "cloud" particle effect.


## FSCmdLine

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable usage of chat bar as a command line


## FSCmdLineAO

- Type: String | Default value: `cao` | Persisted: 1

- Comment: Turn AO on/off


## FSCmdLineAnnounceChannel

- Type: S32 | Default value: `362395` | Persisted: 1

- Comment: Chat channel where chat command output is announced.


## FSCmdLineAnnounceToChannel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Echo chat command output to a script channel.


## FSCmdLineBandWidth

- Type: String | Default value: `bw` | Persisted: 1

- Comment: Change max. bandwidth quickly


## FSCmdLineCalc

- Type: String | Default value: `calc` | Persisted: 1

- Comment: Calculates an expression


## FSCmdLineClearChat

- Type: String | Default value: `clrchat` | Persisted: 1

- Comment: Clear chat transcript to stop lag from chat spam


## FSCmdLineCopyCam

- Type: String | Default value: `cpcampos` | Persisted: 1

- Comment: Copies the current camera location to the clipboard as pos|focus|roll


## FSCmdLineDrawDistance

- Type: String | Default value: `dd` | Persisted: 1

- Comment: Change draw distance quickly


## FSCmdLineGround

- Type: String | Default value: `flr` | Persisted: 1

- Comment: Teleport to ground function command


## FSCmdLineHeight

- Type: String | Default value: `gth` | Persisted: 1

- Comment: Teleport to height function command


## FSCmdLineKeyToName

- Type: String | Default value: `key2name` | Persisted: 1

- Comment: Use a fast key to name query


## FSCmdLineMapTo

- Type: String | Default value: `mapto` | Persisted: 1

- Comment: Teleport to a region by name rapidly


## FSCmdLineMapToKeepPos

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to use current local position on teleport to the new region


## FSCmdLineMedia

- Type: String | Default value: `/media` | Persisted: 1

- Comment: Chat command for setting a media url


## FSCmdLineMusic

- Type: String | Default value: `/music` | Persisted: 1

- Comment: Chat command for setting a music url


## FSCmdLineOfferTp

- Type: String | Default value: `offertp` | Persisted: 1

- Comment: Offer a teleport to target avatar


## FSCmdLinePasteCam

- Type: String | Default value: `pstcampos` | Persisted: 1

- Comment: Restores the camera from a pos|focus|roll


## FSCmdLinePlatformSize

- Type: F32 | Default value: `30` | Persisted: 1

- Comment: How wide the rezzed platform will appear to be.


## FSCmdLinePos

- Type: String | Default value: `gtp` | Persisted: 1

- Comment: Teleport to position function command


## FSCmdLineRezPlatform

- Type: String | Default value: `rezplat` | Persisted: 1

- Comment: Rez a platform underneath you


## FSCmdLineRollDice

- Type: String | Default value: `rolld` | Persisted: 1

- Comment: Rolls dice - cmd [number of dice] [number of faces]. Example: cmd 1 20. Lack of parameters is equal to cmd 1 6 (standard die).


## FSCmdLineTP2

- Type: String | Default value: `tp2` | Persisted: 1

- Comment: Teleport to a person by name, partials work.


## FSCmdLineTeleportHome

- Type: String | Default value: `tph` | Persisted: 1

- Comment: Teleport to home function command


## FSCmdLineTrackPos

- Type: String | Default value: `trkpos` | Persisted: 1

- Comment: Track a position or avatar on the world map.


## FSCmdTeleportToCam

- Type: String | Default value: `tp2cam` | Persisted: 1

- Comment: Teleport to your camera


## FSCollisionMessagesInChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows collision messages in nearby chat.


## FSColorClienttags

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Color Client tags by: 0=Off, 1=Single color per Viewer, 2=User defined color (one color per UUID), 3=New Tagsystem Color


## FSColorIMsDistinctly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Color IM/Group messages distinctly in the console.


## FSColorUsername

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Color username distinctly from the rest of the tag


## FSComboboxSubstringSearch

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allows fulltext search on comboboxes


## FSCommitForSaleOnChange

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables old SL default behavior. Objects set for sale will take effect on change instead of requiring a confirm first.


## FSConfirmPayments

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables confirmation dialogs for payments.


## FSConsoleClassicDrawMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables classic console draw mode (single background block over all lines with width of the longest line)


## FSContactListShowSearch

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows the search filter in the legacy contact list.


## FSContactSetsColorizeChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to color a friends chat based on their friends groups


## FSContactSetsColorizeFriends

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to color a friends list entry based on their friends groups


## FSContactSetsColorizeMiniMap

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to color a friends mini map icon based on their friends groups


## FSContactSetsColorizeNameTag

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to color a friends name tag based on their friends groups


## FSContactSetsColorizeRadar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to color a friends name in the radar list based on their friends groups


## FSContactSetsListColorizeOffline

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to use a custom color for offline contacts in Contact Sets lists. A custom contact set color takes precedence when set.


## FSContactSetsListOfflineColor

- Type: Color4 | Default value: `0.5 0.5 0.5 1.0` | Persisted: 1

- Comment: Custom color for offline contacts in Contact Sets lists when FSContactSetsListColorizeOffline is enabled.


## FSContactSetsListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide profile icons in Contact Sets lists


## FSContactSetsNotificationNearbyChat

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the On/Offline notifications caused by Contactsets in Nearby Chat


## FSContactSetsNotificationToast

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show the On/Offline notifications caused by Contactsets as Toast message


## FSContactSetsProfilePlacement

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Where to show contact sets in the profile groups list: 0=below groups, 1=hidden, 2=above groups


## FSContactsSortOrder

- Type: U32 | Default value: `3` | Persisted: 1

- Comment: Specifies sort order for friends (0 = by display name, 1 = username, 2 = by online status then display, 3 = by online status then username)


## FSConversationLogLifetime

- Type: U32 | Default value: `120` | Persisted: 1

- Comment: Number of days transcripts are preserved in the conversation log before being purged


## FSCopyObjKeySeparator

- Type: String | Default value: `,` | Persisted: 1

- Comment: This chunk of text goes between keys when you use the Copy Key button with multiple objects selected.


## FSCreateCallingCards

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Don't create calling cards when friending other avatars (requires restart)


## FSCreateGiveInventoryParticleEffect

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the viewer will create particle effects around the avatar if inventory is transferred to another avatar.


## FSCreateOctreeLog

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Create a log of octree operation. This can cause huge frame stalls on edit


## FSDefaultObjectTexture

- Type: String | Default value: `89556747-24cb-43ed-920b-47caed15465f` | Persisted: 1

- Comment: Default texture that will be applied to rezzed prims. (UUID texture reference)


## FSDestroyGLTexturesImmediately

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, GL textures will be removed from memory immediately when its fetched texture is removed. This might result in textures behind you being unloaded.


## FSDestroyGLTexturesThreshold

- Type: F32 | Default value: `0.9` | Persisted: 1

- Comment: Threshold, at what texture memory load level GL textures will be removed from memory if FSDestroyGLTexturesImmediately is set to TRUE.


## FSDisableAvatarTrackerAtCloseIn

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Disables the tracking beacon if distance to target avatar is less than 3m.


## FSDisableBeaconAfterTeleport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disables the beacon of the teleport destination after a teleport.


## FSDisableBlockListAutoOpen

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disables automatic opening of the block list when muting people or objects.


## FSDisableIMChiclets

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, Firestorm will not show any group / IM chat chiclets (notifications envelope and sum of IMs will remain on the screen).


## FSDisableLabeledChatLinks

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When true, wiki-style bracketed links ([https://host label]) in IMs, group chat, ad-hoc conferences and group notices keep their label, but hovering shows an instant large hint previewing the real destination URL; helps spot misleading link text.


## FSDisableLabeledChatLinksNearbyChat

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When true, wiki-style bracketed links ([https://host label]) in nearby (local) chat and object text keep their label, but hovering shows an instant large hint previewing the real destination URL; helps spot misleading link text.


## FSDisableLoginScreens

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable login screen progress bar


## FSDisableLogoutScreens

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable logout screen progress bar


## FSDisableMouseWheelCameraZoom

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, Firestorm will not use mouse wheel to zoom in/out the camera.


## FSDisableNeighbourRegionConnections

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Do not connect to neighbouring regions, only to the current region (limits region crossing) - experimental


## FSDisableReturnObjectNotification

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable 'Object has been returned to your inventory Lost and Found folder' notifications


## FSDisableRiggedMeshMatrixCaching

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disable the caching of Rigged mesh matrix pallettes.Non-persistant.


## FSDisableTeleportScreens

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable teleport screens


## FSDisableTurningAroundWhenWalkingBackwards

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disables your avatar turning around locally when moving backwards.


## FSDisableWMIProbing

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disables VRAM detection via WMI probing on Windows systems


## FSDiskCacheHighWaterPercent

- Type: F32 | Default value: `95.0` | Persisted: 1

- Comment: Trigger point above which we should start to clear out older cache entries


## FSDiskCacheLowWaterPercent

- Type: F32 | Default value: `70.0` | Persisted: 1

- Comment: Level to drain cache to once it goes over the high water limit.


## FSDiskCacheSize

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: Controls amount of hard drive space reserved for local asset caching in MB


## FSDismissGroupNoticeAttachmentsToTrash

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, dismissing group notices with attachments will move attachment to trash folder


## FSDoNotHideMapOnTeleport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the world map won't be closed when teleporting


## FSDontIgnoreAdHocFromFriends

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow my friends to start conference chats with me.


## FSDontNagWhenPurging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, emptying trash will not double check before deleting. WARNING: You should only use this if you are a regular trash emptier and are confident that you will not lose things


## FSDoubleClickAddInventoryClothing

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to add clothes instead of wearing them


## FSDoubleClickAddInventoryObjects

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to add objects instead of wearing them


## FSDrawDistanceVRAMOptimization

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables a feature that reduces your draw distance when VRAM becomes full


## FSEditGrid

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Allows editing a grid from the grid manager


## FSEmphasizeShoutWhisper

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables bolding shouted chat and italicizing whispered chat


## FSEnableAggressiveComplexityUpdates

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable active complexity calculations. This may have a significant detrimental performance impact if enabled.


## FSEnableEmojiWindowPopupWhileTyping

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables automatic opening of emoji chooser window while typing in chat bars.


## FSEnableGrowl

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables Growl notifications


## FSEnableLogThrottle

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables throttling for writing to the log file to prevent spam


## FSEnableMovingFolderLinks

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable moving of folder links via drag and drop


## FSEnableObjectExports

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable object imports and exports (WARNING: This feature is unstable and under active development. Use at your own risk!)


## FSEnablePerGroupSnoozeDuration

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables input of a snooze duration per group.


## FSEnableRightclickMenuInMouselook

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables pie or context menus on alt right click in mouselook


## FSEnableRightclickOnTransparentObjects

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, right-clicks on transparent objects will open the context menu


## FSEnableVolumeControls

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If true, Firestorm will show volume controls (sounds, media, stream) in upper right corner of the screen. Useful, if skin already has its own controls.


## FSEnabledLanguages

- Type: LLSD | Default value: `az de en es fr it ja pl pt ru zh` | Persisted: 0

- Comment: Languages that are enabled and can be used in this install.


## FSEnforceStrictObjectCheck

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Force malformed prims to be treated as invalid. This setting derenders all malformed prims, even those that might not cause obvious issues. Setting to false will allow bad prims to render but can cause crashes. (Disabled on OpenSim)


## FSEnvironmentManualTransitionTime

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Timespan for blending between day/water/sky settings when manually changed. 0 is immediate.


## FSEventPollCoreRetries

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: DEBUG: EventQueueGet llcorehttp retry count. 0 keeps current 7.2.3 behavior; 5 matches 7.2.2 behaviour.


## FSExperimentalDragTexture

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, allows to click-drag or click-scale (together with caps lock) a texture face in build mode. This feature is still experimental and should be used with caution.


## FSExperimentalLostAttachmentsFix

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the experimental fix for attachments getting detached on teleports and region crossings.


## FSExperimentalLostAttachmentsFixKillDelay

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Delay in seconds after a teleport for that kill object messages to detach attachments are being ignored.


## FSExperimentalLostAttachmentsFixReport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, reports attachments that were attempted to get detached during a teleport or region crossing to nearby chat.


## FSExperimentalOutfitsReturn

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: FIRE-36116 - debounce redundant refreshList calls


## FSExperimentalRegionCrossingMovementFix

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Enables the experimental fix for region crossing movements being bogus due to false predictions by the viewer (0 = Disabled (Unlimited prediction), 1 = Enabled (Predict until error gets too large))


## FSExportContents

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Export object contents in linkset backups


## FSFadeAudioStream

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use fading when changing the parcel audio stream.


## FSFadeGroupNotices

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Fade group notices. (V3 default: true)


## FSFilePickerOpenDirectory

- Type: String | Default value: `` | Persisted: 1

- Comment: The last used directory for opening a file


## FSFilePickerSaveDirectory

- Type: String | Default value: `` | Persisted: 1

- Comment: The last used directory for saving a file


## FSFilterGrowlKeywordDuplicateIMs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Filters duplicate IMs in Growl if they have already been shown as part of a keyword alert.


## FSFirstRunAfterSettingsRestore

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Specifies that you have not run the viewer since you performed a settings restore


## FSFlashOnMessage

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flash/Bounce the app icon when a new message is received and Firestorm is not in focus


## FSFlashOnObjectIM

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Flash/Bounce the app icon when a new instant message from an object is received and Firestorm is not in focus.


## FSFlashOnScriptDialog

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flash/Bounce the app icon when a script dialog is received and Firestorm is not in focus


## FSFlyAfterTeleport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Always fly after teleporting.


## FSFocusPointFollowsPointer

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Allows the Depth of Field focus to actively follow the mouse point


## FSFocusPointLocked

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Whether the focus point used for DoF is currently Locked in place


## FSFocusPointRender

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Draw a small crosshair where the DoF focus is


## FSFolderViewItemHeight

- Type: S32 | Default value: `20` | Persisted: 1

- Comment: Controls the height of folder items, for instance in inventory


## FSFontChatLineSpacingPixels

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Line spacing pixels for chat text (requires restart)


## FSFontLineSpacingAdjustment

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Line spacing pixels for UI text (requires restart


## FSFontSettingsFile

- Type: String | Default value: `fonts.xml` | Persisted: 1

- Comment: The font settings file with the font currently being used.


## FSFontSizeAdjustment

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Number of points to add to the defualt font sizes


## FSForcedVideoMemory

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Overrides the video memory detection on Windows if a value greater 0 is passed (in case DirectX memory detection fails or is wrong)


## FSFriendListColumnShowDisplayName

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the display name column in the legacy friend list.


## FSFriendListColumnShowFullName

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the full name column in the legacy friend list.


## FSFriendListColumnShowPermissions

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, show permission columns in the contacts list


## FSFriendListColumnShowUserName

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the username column in the legacy friend list.


## FSFriendListFullNameFormat

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Defines the order of how the full name in the contacts list is shown (0 = username (display name), 1 = display name (username))


## FSFriendListSortOrder

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Defines the sort order of the contacts list (0 = username, 1 = display name)


## FSGridBuilderURL

- Type: String | Default value: `https://phoenixviewer.com/app/fsdata/fs_grid_builder.html` | Persisted: 1

- Comment: Fetch an html page of grids from this URL.


## FSGroupNoticesToIMLog

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show group notices in group chats, in addition to toasts.


## FSGroupNotifyNoTransparency

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, group notices will be shown opaque and ignore the floater opacity settings.


## FSGrowlWhenActive

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If Growl notifications are active, show them even when the window is active.


## FSHideHelpButtons

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When enabled, hides the help button from floaters (requires restart)


## FSHighlightGroupMods

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable group moderator message highlighting


## FSHudTextBackgroundOpacity

- Type: F32 | Default value: `0.75` | Persisted: 1

- Comment: Opacity of floating text background (0.0 = completely transparent, 1.0 = completely opaque)


## FSHudTextFadeDistance

- Type: F32 | Default value: `8.0` | Persisted: 1

- Comment: Sets the distance where HUD text starts to fade


## FSHudTextFadeRange

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: Sets the range it takes for a HUD text to fade from fully visible to invisible


## FSHudTextShowBackground

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Displays a black/white background behind the prim floating text to make the text more readable


## FSHudTextUseHoverHighlight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When an object is being hovered over, highlight the HUD text by moving to the foreground and disable alpha


## FSIMChatFlashOnFriendStatusChange

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flash IM tab when friend goes online or offline.


## FSIMChatHistoryFade

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Amount to fade IM text into the background of the chat transcript floater (0.25-1.0, 0.25 for really light, 1 for fully visible).


## FSIMOpacity

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Opacity of the IM floater


## FSIMSystemMessageBrackets

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables surrounding system messages with square brackets in chat transcript if using V1 style chat history. []


## FSIMTabNameFormat

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Controls in what format the name on IM tabs will be shown: 0 = Display Name, 1 = Username, 2 = Display Name (Username), 3 = Username (Display name)


## FSIgnoreAdHocSessions

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Automatically ignore and leave all conference (ad-hoc) chats.


## FSIgnoreClientsideMeshValidation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Treat the errors from Clientside mesh validation as warnings and do not block upload. This setting allows you to fall back on server side checks and per Grid quality control levels.


## FSIgnoreFinishAnimation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable the wait for pre-jump or landing. Credit to Zwagoth Klaar for coding this.


## FSIgnoreSimulatorCameraConstraints

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignores the 'push' the simulator applies to your camera to keep it out of objects.(Requires restart to work correctly)


## FSImActiveOpacityOverride

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When enabled, uses the Active Opacity value when IM window is focused


## FSImageDecodeThreads

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Amount of threads to use for image decoding. 0 = auto, >= 1 number of threads. Needs restart


## FSImportBuildOffset

- Type: Vector3 | Default value: `5.0 0.0 2.0` | Persisted: 1

- Comment: Distance from user the importer begins to build


## FSImpostorAvatarExclude

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Allows for Animesh User or Control Avatars to be excluded from using impostor rendering. Values are: (0 - None, 1 - User, 2 - Control, 3 - Both).


## FSInspectAvatarSlurlOpensProfile

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Open the full profile of an avatar directly when clicking on its name


## FSInspectColumnConfig

- Type: U32 | Default value: `1023` | Persisted: 1

- Comment: Stores the column visibility of the inspect window


## FSInternalCanEditObjectFaces

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Internal control to show/hide object texture/material edit controls


## FSInternalFaceHasBPNormalMap

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Internal control to store a flag about the edited face having a Blinn-Phong normal map or not


## FSInternalFaceHasBPSpecularMap

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Internal control to store a flag about the edited face having a Blinn-Phong specular map or not


## FSInternalFontSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: The font settings file with the font currently being used in this session.


## FSInternalLegacyNotificationWell

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal state of FSLegacyNotificationWell


## FSInternalShowNavbarFavoritesPanel

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Internal control to show/hide navigation bar favorites panel


## FSInternalShowNavbarNavigationPanel

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal control to show/hide navigation bar navigation panel


## FSInternalSkinCurrent

- Type: String | Default value: `` | Persisted: 0

- Comment: The currently selected skin in the current session.


## FSInternalSkinCurrentTheme

- Type: String | Default value: `` | Persisted: 0

- Comment: The selected theme for the current skin in the current session.


## FSInventoryThumbnailTooltipsDelay

- Type: F32 | Default value: `0.7` | Persisted: 1

- Comment: Sets the delay of the inventory item thumbnail tooltip


## FSKeepUnpackedCacheFiles

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, the viewer won't delete unpacked cache files when logging out (improves overall performance and fixes sound bugs)


## FSLandmarkCreatedNotification

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display a notification if a landmark is added to your inventory.


## FSLargeOutfitsWarningInThisSession

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal; Suppresses the 'too many outfits' warning (does not persist across sessions)


## FSLastSearchTab

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected tab in search window


## FSLastSnapshotPanel

- Type: String | Default value: `` | Persisted: 1

- Comment: The last snapshot panel that was opened and will be restored the next time the snapshot floater is opened.


## FSLastSnapshotToFacebookHeight

- Type: S32 | Default value: `768` | Persisted: 1

- Comment: The height of the last Facebook snapshot, in px


## FSLastSnapshotToFacebookResolution

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: At what resolution should snapshots be posted on Facebook. 0=Current Window, 1=320x240, 2=640x480, 3=800x600, 4=1024x768, 5=1280x1024, 6=1600x1200, 7=Custom


## FSLastSnapshotToFacebookWidth

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: The width of the last Facebook snapshot, in px


## FSLastSnapshotToFlickrHeight

- Type: S32 | Default value: `768` | Persisted: 1

- Comment: The height of the last Flickr snapshot, in px


## FSLastSnapshotToFlickrResolution

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: At what resolution should snapshots be posted on Flickr. 0=Current Window, 1=320x240, 2=640x480, 3=800x600, 4=1024x768, 5=1280x1024, 6=1600x1200, 7=Custom


## FSLastSnapshotToFlickrWidth

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: The width of the last Flickr snapshot, in px


## FSLastSnapshotToPrimfeedHeight

- Type: S32 | Default value: `768` | Persisted: 1

- Comment: The height of the last Primfeed snapshot, in px


## FSLastSnapshotToPrimfeedResolution

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: At what resolution should snapshots be posted on Primfeed. 0=Current Window, 1=320x240, 2=640x480, 3=800x600, 4=1024x768, 5=1280x1024, 6=1600x1200, 7=Custom


## FSLastSnapshotToPrimfeedWidth

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: The width of the last Primfeed snapshot, in px


## FSLastSnapshotToTwitterHeight

- Type: S32 | Default value: `768` | Persisted: 1

- Comment: The height of the last Twitter snapshot, in px


## FSLastSnapshotToTwitterResolution

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: At what resolution should snapshots be posted on Twitter. 0=Current Window, 1=320x240, 2=640x480, 3=800x600, 4=1024x768, 5=1280x1024, 6=1600x1200, 7=Custom


## FSLastSnapshotToTwitterWidth

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: The width of the last Twitter snapshot, in px


## FSLatencyOneTimeFixRun

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: One time fix has run for this install for script dialog colors on Latency


## FSLegacyEdgeSnap

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use old method for adjusting edge snap regions.


## FSLegacyMinimize

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Minimize floaters to bottom left instead of top left.


## FSLegacyNameCacheExpiration

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use the legacy avatar name cache expiration (expiration at least 60 mins.)


## FSLegacyNametagPosition

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the legacy nametag behavior of staying fixed at the avatar's position instead of following animation movements.


## FSLegacyNotificationWell

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the legacy notifications and system messages well


## FSLegacyNotificationWellAutoResize

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the automatic resizing of the legacy notifications and system messages well


## FSLegacyRadarFriendColoring

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use old style for friends on the radar. Uses same color as minimap.


## FSLegacyRadarLindenColoring

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Color Lindens on the radar the same as the minimap.


## FSLegacySearchActionOnTeleport

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Controls what action Legacy Search should take when teleporting: 0 = No effect, 1 = Close floater, 2 Minimise floater


## FSLetterKeysFocusNearbyChatBar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the chat bar in the Nearby Chat window will be preferred if it contains a chat bar and LetterKeysAffectsMovementNotFocusChatBar is FALSE.


## FSLimitFramerate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable framerate limitation defined by FramePerSecondLimit


## FSLimitTextureVRAMUsage

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, limits the amount of VRAM used for textures to the value of RenderMaxVRAMBudget.


## FSLinuxEnableWin32VoiceProxy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Win32 SLVoice.exe for voice. Needs wine (https://www.winehq.org/) installed, as SLVoice.exe is started inside wine.


## FSLinuxEnableWin64VoiceProxy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Win64 SLVoice.exe for voice. Needs wine (https://www.winehq.org/) installed, as SLVoice.exe is started inside wine.


## FSLocalMeshApplyJointOffsets

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: use joint offsets if they are present


## FSLocalMeshAutoReload

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Automatically reload local mesh files when they change on disk.


## FSLocalMeshAutoReloadPeriod

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: How often, in seconds, the viewer should scan local mesh files for changes.


## FSLocalMeshScaleAlwaysMeters

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore the units specified by the Collada file. Useful when importing from tools such as Maya


## FSLogAutoAcceptInventoryToChat

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, auto-accepted inventory items will be logged to nearby chat.


## FSLogGroupImToChatConsole

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Defines if group IM notifications should be sent to the nearby chat console (v1-style) or toasts (v2-style).


## FSLogIMInChatHistory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, IM will also be logged in the nearby chat transcript if logging nearby chat and showing IMs in nearby chat is enabled.


## FSLogImToChatConsole

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Defines if IM notifications should be sent to the nearby chat console (v1-style) or toasts (v2-style).


## FSLogSnapshotsToLocal

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log filename of saved snapshots in to chat history


## FSLoginDontSavePassword

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal setting used to indicate that passwords shouldn't be saved if --login cmdline switch is used.


## FSLookAtTargetLimitDistance

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Limit look at target distance from head to value of LookAtTargetMaxDistance


## FSLookAtTargetMaxDistance

- Type: F32 | Default value: `1` | Persisted: 1

- Comment: Max lookat distance in meters


## FSManipRotateJointUseNaturalDirection

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: use the natural bone direction instead of world rotation


## FSManipShowJointMarkers

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show small markers where the selectable joints are.


## FSMarkObjects

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Mark unnamed objects with (No Name)


## FSMaxAnimationPriority

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: Allow uploading animations with higher priority (up to 6) NOTE: Only priorities up to level 5 are supported! (Default: 4)


## FSMaxBeamsPerSecond

- Type: F32 | Default value: `40` | Persisted: 1

- Comment: How many selection beam updates to send in a second


## FSMaxPendingIMMessages

- Type: S32 | Default value: `25` | Persisted: 1

- Comment: Maximum number of pending IM or group messages before a minimized or not visible chat window will be updated


## FSMenuBackgroundAlpha

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Alpha (opacity) of menu backgrounds including context menus and the top menu bar (0.0 = fully transparent, 1.0 = fully opaque)


## FSMeshHighLodSuffix

- Type: String | Default value: `` | Persisted: 1

- Comment: Suffix to use for High LOD models and files (DAE).


## FSMeshImportScaleFixup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Adjust normals on import, fixes underlying issue, not recommended in case underlying rendering gets fixed.


## FSMeshLowLodSuffix

- Type: String | Default value: `LOD1` | Persisted: 1

- Comment: Suffix to use for Low LOD models and files (DAE).


## FSMeshLowestLodSuffix

- Type: String | Default value: `LOD0` | Persisted: 1

- Comment: Suffix to use for Lowest LOD models and files (DAE).


## FSMeshMediumLodSuffix

- Type: String | Default value: `LOD2` | Persisted: 1

- Comment: Suffix to use for Medium LOD models and files (DAE).


## FSMeshPhysicsSuffix

- Type: String | Default value: `PHYS` | Persisted: 1

- Comment: Suffix to use for Physics models and files (DAE).


## FSMeshPreviewUVGuideFile

- Type: String | Default value: `salt_and_pepper.jpg` | Persisted: 1

- Comment: filename of the texture to use as a UV guide for mesh preview.


## FSMeshUploadAutoEnableWeights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically set weights enabled for meshes with rigging info


## FSMeshUploadAutoShowWeightsWhenEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically show weights in preview for meshes with rigging info


## FSMeshUploadUseGLODAsDefault

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use the 'reliable' (GLOD) method for LODs as the default when opening Collada files.


## FSMilkshakeRadarToasts

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When enabled, radar alerts will be sent as notification toasts.


## FSMiniMapChatRing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show chat range ring on minimap


## FSMiniMapOpacity

- Type: F32 | Default value: `0.66` | Persisted: 1

- Comment: The opacity for the minimap background


## FSMiniMapShoutRing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show shout range ring on minimap


## FSMiniMapWhisperRing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show whisper range ring on minimap


## FSMinimapPickScale

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Controls the pick radius on the minimap


## FSModNameStyle

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: 
      Font style settings for moderators' name if FSHighlightGroupMods enabled.
      0=NORMAL
      1=BOLD
      2=ITALIC
      3=BOLD ITALIC
      4=UNDERLINE
      5=BOLD UNDERLINE
      6=ITALIC UNDERLINE
      7=BOLD ITALIC UNDERLINE
    


## FSModTextStyle

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: 
      Font style settings for moderators' name if FSHighlightGroupMods enabled.
      0=NORMAL
      1=BOLD
      2=ITALIC
      3=BOLD ITALIC
      4=UNDERLINE
      5=BOLD UNDERLINE
      6=ITALIC UNDERLINE
      7=BOLD ITALIC UNDERLINE
    


## FSMouselookCombatFeatures

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable combat features (target distance etc.) when in mouselook


## FSMuteAllGroups

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable ALL group chats.


## FSMuteGroupWhenNoticesDisabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When 'Receive group notices' is disabled, disable group chat as well.


## FSNameTagShowLegacyUsernames

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show legacy name (Firstname Lastname) in user tags instead of username


## FSNameTagZOffsetCorrection

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Changes the default Z-offset of the avatar nametags.


## FSNearbyChatToastsOffset

- Type: S32 | Default value: `20` | Persisted: 1

- Comment: Vertical offset of the nearby chat toasts


## FSNearbyChatbar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Set to true to add a chat bar to the Nearby Chat window


## FSNetMapDoubleClickAction

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Defines the action happening if the a double click occurs on a minimap instance (minimap floater or within people panel): 0 = Nothing, 1 = Open world map, 2 = teleport to location


## FSNetMapPhantomOpacity

- Type: U32 | Default value: `90` | Persisted: 1

- Comment: Percentage of opacity for phantom objects on netmap.


## FSNetMapPhysical

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Accent physical objects on netmap in different colors.


## FSNetMapScripted

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Accent scripted objects on netmap in different colors.


## FSNetMapTempOnRez

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Accent temp on rez objects on netmap in different colors.


## FSNoScreenShakeOnRegionRestart

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Don't shake my screen when region restart alert message is shown


## FSNoVersionPopup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disables version popup on the Firestorm Login page


## FSNotecardFontName

- Type: String | Default value: `SansSerif` | Persisted: 1

- Comment: The name of the font used for the notecard editor


## FSNotecardFontSize

- Type: String | Default value: `Medium` | Persisted: 1

- Comment: The size of the font used for the notecard editor


## FSNotifyIMFlash

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Flash FUI button if new (group) IMs arrived and conversations floater is closed (IM floater must be docked to conversations floater and IMs must be shown in tabs)


## FSNotifyIncomingObjectSpam

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Notify about throttled incoming object offers from objects.


## FSNotifyIncomingObjectSpamFrom

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Notify about throttled incoming object offers from named sources.


## FSNotifyNearbyChatFlash

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Flash FUI button if new nearby chat arrived and conversations floater is closed (nearby chat floater must be docked to conversations floater)


## FSNotifyUnreadChatMessages

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Notify about new unread chat messages in history if scrolled back


## FSNotifyUnreadIMMessages

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Notify about new unread IM messages in history if scrolled back


## FSOOCPostfix

- Type: String | Default value: `))` | Persisted: 1

- Comment: Postfix to mark OOC chat


## FSOOCPrefix

- Type: String | Default value: `((` | Persisted: 1

- Comment: Prefix to mark OOC chat


## FSOfferThrottleMaxCount

- Type: U32 | Default value: `5` | Persisted: 1

- Comment: The number of objects offered within a second duration before throttling starts.


## FSOpenIMContainerOnOfflineMessage

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Open the IM container at login when an offline message is present.


## FSOpenInventoryAfterSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the inventory window will open and show the snapshot after upload


## FSOpenSimAlwaysForceShowGrid

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Soft enable/disable the startup behaviour of OpenSim builds to allow gridlist access


## FSOutfitListSortOrder

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: How outfit list in Avatar's floater is sorted. Bitmask: 0x1 - favorites to top, 0x2 - newest first instead of alphabetical


## FSOutputDeviceUUID

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 1

- Comment: UUID of the output device used for inworld sound playback


## FSOverrideVRAMDetection

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow user to override the vRAM detection, use the FSForcedVideoMemory setting instead- use with extreme caution.


## FSParcelMusicAutoPlay

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Auto play parcel music when available


## FSParticleChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Send Selection Info on channel 9000 when editing objects (does not work if PrivatePointAtTarget is enabled)


## FSPaymentConfirmationThreshold

- Type: S32 | Default value: `200` | Persisted: 1

- Comment: Threshold when payment confirmation dialogs are triggered


## FSPaymentInfoInChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, L$ balance changes will be shown in nearby chat instead of toasts.


## FSPerfFloaterSmoothingPeriods

- Type: U32 | Default value: `50` | Persisted: 1

- Comment: Number of periods to smooth the stats over


## FSPermissionDebitDefaultDeny

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, LSL script debit permission dialogs will default to deny. If disabled, they will default to allow.


## FSPhysicsPresetUser1

- Type: String | Default value: `` | Persisted: 1

- Comment: full system path to a user provided physics mesh (DAE).


## FSPlayDefaultBentoAnimation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the viewer will run a default, priority 0 bento animation that poses hands, wings, mouth and tail in a natural position when no other bento animation is running.


## FSPoseStandLastSelectedPose

- Type: String | Default value: `` | Persisted: 1

- Comment: Last selected pose in the pose stand


## FSPoseStandLock

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When enabled, posestand will lock the avatar to the ground.


## FSPoserOnSaveConfirmOverwrite

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to confirm overwriting a save file.


## FSPoserPelvisUnlockedForBvhSave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether the mPelvis joint should be position/rotationally locked when a BVH is created.


## FSPoserSaveExternalFileAlso

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to save to an external format (like BVH or ANIM) file as well when saving a pose.


## FSPoserShowBoneHighlights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to highlight a bone with the debug beacon on selection from the UI.


## FSPoserStopPosingWhenClosed

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to stop animating with the poser when the poser window is closed.


## FSPoserTrackpadSensitivity

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: The relative sensitivity of the poser trackpad.


## FSPrettyEmojiButtonCode

- Type: U32 | Default value: `128578` | Persisted: 1

- Comment: Decimal code for the emoji button. Try 128569 or 128571 for example


## FSPrimfeedViewerApiKey

- Type: String | Default value: `xAcXYt8SBius3Lor4wHle8L96PDHYlAZuWYXIYQUdW4b09mjhQUAwiqmWp5UNYXLpq5GSUtuKHuDYLwaueACPkew93l6MRY8jfBKSH09kv0zyGglpky07X7X7Sp4Rzin` | Persisted: 1

- Comment: Viewer key for API login.


## FSRadarColorNamesByDistance

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Colors avatar nametags by distance in the radar.


## FSRadarColumnConfig

- Type: U32 | Default value: `1023` | Persisted: 1

- Comment: Stores the column visibility of the radar


## FSRadarEnhanceByBridge

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enhance radar functionality by using client LSL Bridge.


## FSRadarShowMutedAndDerendered

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, show blocked/muted or derendered avatars in radar list


## FSRegionCrossingAngleErrorLimit

- Type: F32 | Default value: `20.0` | Persisted: 1

- Comment: Region crossing angle error limit in degrees


## FSRegionCrossingPositionErrorLimit

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Region crossing position error limit in meters


## FSRegionCrossingSmoothingTime

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Region crossing smoothing filter time in seconds


## FSRegionRestartAnnounceChannel

- Type: S32 | Default value: `473405` | Persisted: 1

- Comment: Chat channel where region restart info is announced to.


## FSRemapLinuxShortcuts

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, use the special shortcuts on Linux to remap shortcuts that are already in use by the operating system (e.g. CTRL-ALT-Fx)


## FSRememberUsername

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Stores the username used for logging in.


## FSRemoveFlyHeightLimit

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Remove the 4096m high fly limit


## FSRemoveScriptBlockButton

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Removes the "block" from script dialogs.


## FSRenderBeaconText

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show beacon text in the viewer window if beacons are enabled


## FSRenderFarClipStepping

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Set to TRUE to increase performance via progressive draw distance stepping


## FSRenderFarClipSteppingInterval

- Type: U32 | Default value: `20` | Persisted: 1

- Comment: Interval in seconds between each draw distance increment


## FSRenderParcelSelectionToMaxBuildHeight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows the parcel boundary up to the maximum build height instead of just 0.66m above ground


## FSRenderVignette

- Type: Vector3 | Default value: `0.0 1.0 1.0` | Persisted: 1

- Comment: Amount of vignette to apply (X), power of vignette shading (Y), and multiplier for vignette shading (Z).


## FSRepeatedEnvTogglesShared

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether repeated presses of sky preset shortcuts should revert to shared environment


## FSReportBlockToNearbyChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reports changes to the blocklist in nearby chat


## FSReportCollisionMessages

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Report collision messages to scripts.


## FSReportCollisionMessagesChannel

- Type: S32 | Default value: `-25000` | Persisted: 1

- Comment: The channel used to report collision messages to scripts.


## FSReportIgnoredAdHocSession

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reports to nearby chat if a conference (ad-hoc) has been ignored.


## FSReportMutedGroupChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reports to nearby chat if a group chat has been muted.


## FSReportRegionRestartToChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Announces region restart to a defined chat channel.


## FSReportTotalScriptCountChanges

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reports if the change of total number of active scripts in a region exceeds the defined threshold.


## FSReportTotalScriptCountChangesThreshold

- Type: U32 | Default value: `100` | Persisted: 1

- Comment: Minimum change of total active scripts in a region before reporting.


## FSResetCameraOnMovement

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If true, Firestorm will reset camera on avatar movement.


## FSResetCameraOnTP

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If true the camera will be reset to behind the avatar on teleporting


## FSResetSkeletonOnStandUp

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Resets own avatar skeleton upon standing up and sends the reset to all surrounding avatars


## FSRestoreOpenIMs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Restore open IM windows from the previous session on startup.


## FSRevokePerms

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Revokes objects anim perms on your avatar on: 0) never, 1) on sit, 2) on stand, 3) on sit and stand.


## FSRowsPerScriptDialog

- Type: S32 | Default value: `20` | Persisted: 1

- Comment: The number of rows visible in a script dialog


## FSSaveInventoryScriptsAsMono

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Saves scripts edited directly from inventory as Mono instead of LSL


## FSSavedRenderFarClip

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Saved draw distance (used in case of logout during progressive draw distance stepping)


## FSScriptDebugWindowClearOnClose

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clear [ALL SCRIPTS] tab of script debug/error window on close.


## FSScriptDialogNoTransparency

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, script dialogs will be shown opaque and ignore the floater opacity settings.


## FSScriptEditorRecompileButton

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the save button to recompile scripts when no change in the opened script has occurred. Very useful for preproc scripts that consist of only includes. Only enabled with preproc since its pointless otherwise.


## FSScriptInfoExtended

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, extend basic script info feature with various details useful for builders.


## FSScriptingFontName

- Type: String | Default value: `Scripting` | Persisted: 1

- Comment: The name of the font used for the LSL script editor


## FSScriptingFontSize

- Type: String | Default value: `Scripting` | Persisted: 1

- Comment: The size of the font used for the LSL script editor


## FSScrollWheelExitsMouselook

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, mouselook can be left by turning the scroll wheel


## FSSearchGroupMaturity

- Type: U32 | Default value: `13` | Persisted: 1

- Comment: Setting for the user's group search maturity level (consts in indra_constants.h)


## FSSecondsinChatTimestamps

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show seconds in chat timestamps, in the chat window and logs


## FSSelectCopyableOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Only include copyable objects during selection


## FSSelectIncludeGroupOwned

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Includes group-owned objects during selection


## FSSelectLocalSearchEditorOnShortcut

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, pressing the shortcut for search (CTRL-F) will focus the search field of the active window (if available).


## FSSelectLockedOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Select only objects that are locked


## FSSendTypingState

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Send typing start and typing stop state notifications to other clients.


## FSShowAutoAcceptInventoryInNotifications

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, auto-accepted inventory items will be shown in notifications.


## FSShowAutorespondInNametag

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Does the user want to see autorespond mode in his own nametag?


## FSShowBackSLURL

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Report the SLURL of the region you completed a teleport from


## FSShowChatChannel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows/Hides the channel selector in the Nearby Chat command line


## FSShowChatRangeSpheres

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show chat range spheres (whisper, say, shout) in 3D world around avatar


## FSShowChatType

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows/Hides the chat type selector (Whisper, Say, Shout)


## FSShowConversationVoiceStateIndicator

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the voice state indicator in the conversation floater tabs


## FSShowConvoAndRadarInML

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Conversations and Radar windows stays visible when entering mouselook if it was open already.


## FSShowCurrencyBalanceInStatusbar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the current balance in the statusbar if enabled


## FSShowDisplayNameUpdateNotification

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show system notifications if somebody changes their display name.


## FSShowDummyAVsinRadar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, shows dummy (preview) avatars in radar.


## FSShowEmojiButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show or hide the emoji selection button in chat/IM windows


## FSShowGroupNameLength

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Max length of group name to be printed in chat (-1 for full group name, 0 for disabled).


## FSShowGroupTitleInTooltip

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows the group title of an avatar in the tooltip.


## FSShowIMInChatHistory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, IM will also be shown in the nearby chat transcript.


## FSShowIMSendButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows the send chat button in IM session windows


## FSShowInboxFolder

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the Received Items folder aka Inbox is shown in the inventory as folder.


## FSShowInterfaceInMouselook

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, Firestorm will show user interface in mouselook mode.


## FSShowInventoryThumbnailTooltips

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows the inventory item thumbnail as tooltip


## FSShowJoinedGroupInvitations

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, invitations to groups you are already a member in will be shown


## FSShowLibraryFolder

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide the Library root folder in the Inventory floater


## FSShowMessageCountInWindowTitle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Displays the number of unread IMs in the application window title.


## FSShowMouselookInstructions

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If true, instructions about leaving Mouseview are displayed.


## FSShowMutedChatHistory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows the muted text in nearby chat transcript if enabled.


## FSShowMyOwnVoiceVisualizer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show voice visualizer over my own avatar.


## FSShowOnscreenConsole

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Displays the on-screen console


## FSShowSelectedInBlinnPhong

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show BlinnPhong while selected (non-persistent).This setting is driven by the code, not by user


## FSShowServerVersionChangeNotice

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows a notice if the simulator version is different after a region crossing or teleport.


## FSShowStatsBarInMouselook

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Makes it so that the statistics bar stays visible when entering mouselook if it was open already.


## FSShowTimestampsIM

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show timestamps in IM


## FSShowTimestampsNearbyChat

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show timestamps in nearby chat


## FSShowTimestampsTranscripts

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show timestamps in transcripts


## FSShowToastsInFront

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show toasts in front of other floaters if enabled


## FSShowTypingStateInNameTag

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows in the nametag of an avatar if they are typing


## FSShowUploadPaymentToast

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show UploadPayment Notifications


## FSShowVoiceVisualizerWithDot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows the voice dot over avatars as part of the voice visualizer.


## FSShowWhitelistReminder

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the whitelist reminder on first install.


## FSSkinClobbersColorPrefs

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled the default color scheme for newly selected skins will be overwritten with the user's current selected colors. (default off)


## FSSkinClobbersToolbarPrefs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled the default toolbar layout for newly selected skins will be overwritten with the user's current layout. (default off)


## FSSkinCurrentReadableName

- Type: String | Default value: `Firestorm` | Persisted: 1

- Comment: The readable name of the currently selected skin.


## FSSkinCurrentThemeReadableName

- Type: String | Default value: `Grey` | Persisted: 1

- Comment: The readable name of the selected theme for the current skin.


## FSSnapshotFrameBorderColor

- Type: Color3 | Default value: `0.0 0.0 0.0` | Persisted: 1

- Comment: The color of the border for the Snapshot frame


## FSSnapshotFrameBorderWidth

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: The thickness of the line drawn around the snapshot frame


## FSSnapshotFrameGuideColor

- Type: Color3 | Default value: `1.0 1.0 0.0` | Persisted: 1

- Comment: The color of the Snapshot composition guides


## FSSnapshotFrameGuideWidth

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: The thickness of the lines drawn for the composition guides


## FSSnapshotGuideStyle

- Type: String | Default value: `rule_of_thirds` | Persisted: 1

- Comment: The framing guide layout to display inside the snapshot frame


## FSSnapshotGuideVisibility

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: The blend factor used to color the snapshot framing guides


## FSSnapshotLocalFormat

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Save snapshots to disk in this format (0 = PNG, 1 = JPEG, 2 = BMP)


## FSSnapshotLocalNamesWithTimestamps

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: include a timestamp in the filename when saving snapshots locally


## FSSnapshotShowCaptureFrame

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, masks the main screen according to the capture frame.


## FSSnapshotShowGuides

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, shows composition guides inside the snapshot frame.


## FSSortAttachmentSpotsAlphabetically

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Sorts the attachment spots in the "Attach to" menus alphabetically


## FSSortDeferalFrames

- Type: U32 | Default value: `5` | Persisted: 1

- Comment: How many frames after an update should we wait before sorting


## FSSortFSFoldersToTop

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Sorts the #FS and #RLV folders to the top like system folders.


## FSSoundCacheLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Location for caching sound files (.DSF); Uses default cache directory if empty


## FSSplashScreenHideBlogs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hide the blogs section on the splash screen


## FSSplashScreenHideDestinations

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hide the destinations section on the splash screen


## FSSplashScreenHideTopBar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hide the top bar section on the splash screen


## FSSplashScreenNoTransparency

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable transparency effects on the splash screen


## FSSplashScreenUseAllCaps

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable all caps mode on the splash screen


## FSSplashScreenUseGrayMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable grayscale mode on the splash screen


## FSSplashScreenUseHighContrast

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable high contrast mode on the splash screen


## FSSplashScreenUseLargerFonts

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use larger fonts on the splash screen


## FSSplitInventorySearchOverTabs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the search terms for inventory can be entered for each tab individually.


## FSStartupClearBrowserCache

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clear internal browser cache on next startup.


## FSStatbarLegacyMeanPerSec

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use legacy period mean per second display for stat bars.


## FSStaticEyesUUID

- Type: String | Default value: `592a9fb4-5e02-77bb-e1e5-da4d17d27336` | Persisted: 1

- Comment: Animation UUID to used to stop idle eye moment (Default is priority 2: 592a9fb4-5e02-77bb-e1e5-da4d17d27336, for priority 5 use: 3f0469e9-b434-70c0-ee52-a493aa039d22)


## FSStatisticsNoFocus

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the statistics bar will never gain focus (i.e. from closing another floater).


## FSStatusBarMenuButtonPopupOnRollover

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable rollover popups on top status bar menu icons: Quick Graphics Presets, Volume, and Media.


## FSStatusBarShowFPS

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, shows the current FPS in the main menu bar


## FSStatusBarShowFPSColors

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, display FPS number in a color based on the current status.


## FSStatusBarTimeFormat

- Type: String | Default value: `Language` | Persisted: 1

- Comment: Which time format to use for the status bar clock, e.g. 12 Hours, 24 Hours, etc. The default "Language" restores the original behavior of changing the time display mode per language.


## FSStatusbarShowSimulatorVersion

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the simulator version is included in the V1-like statusbar.


## FSStreamList

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Saved list of media streams


## FSStreamtitleHistoryLength

- Type: U32 | Default value: `10` | Persisted: 1

- Comment: The maximum number of stream titles shown in the history


## FSSupportGroupChatPrefix3

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Adds (FS 1.2.3) to support group chat


## FSSupportGroupChatPrefixTesting

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Adds (W 56789f* os) to testing group chat


## FSTPHistoryTZ

- Type: String | Default value: `slt` | Persisted: 1

- Comment: Select the timezone to be used with Teleport History. ('utc' = Coordinated Universal Time, 'slt' = Second Life Time (default), 'local' = the local timezone of the client)


## FSTagShowARW

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the avatar complexity will be shown in the nametag for every avatar.


## FSTagShowDistance

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, show distance to other avatars in their nametag.


## FSTagShowDistanceColors

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, color other avatars' nametags based on their distance


## FSTagShowOwnARW

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the avatar complexity for the own avatar will be shown in the nametag.


## FSTagShowTooComplexOnlyARW

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the avatar complexity will be shown in the nametag only for too complex avatars (Jelly Dolls)


## FSTeleportHistoryShowDate

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows the exact date and time in the teleport history.


## FSTeleportHistoryShowPosition

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows the local position within a region in the teleport history.


## FSTeleportToOffsetLateral

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Horizontal distance from the target avatar that is used for teleporting to them.


## FSTeleportToOffsetVertical

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Vertical distance from the target avatar that is used for teleporting to them.


## FSTempDerenderUntilTeleport

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, temporary derendered objects will stay derendered until teleport. If disabled, they stay derendered until the end of the session or get manually re-rendered via asset blacklist floater.


## FSTextureDefaultSaveAsFormat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: The default "save as" format for textures, in the texture preview floater or context menu in inventory. False: TGA, True: PNG.


## FSToolbarsResetOnModeChange

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled the user's current toolbar layout for newly selected modes will be overwritten with the default one for a mode. (default on)


## FSToolboxExpanded

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to show additional build tool controls


## FSTrimLegacyNames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Trim "Resident" from Legacy Names.


## FSTurnAvatarToSelectedObject

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the avatar turns towards an selected object


## FSTypeDuringEmote

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the typing animation even while emoting


## FSTypingChevronPrefix

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Adds an additional chevron prefix to the IM window as typing indicator


## FSUndeformUUID

- Type: String | Default value: `44e98907-3764-119f-1c13-cba9945d2ff4` | Persisted: 1

- Comment: Animation UUID to use for the undeform


## FSUnfocusChatHistoryOnReturn

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: De-focus chat history after sending a message


## FSUnlinkConfirmEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Unlink confirmation dialog functionality enabled?


## FSUploadAnimationOnOwnAvatar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Uploading an animation preview on own avatar if set to true, preview on dummy if false. Both plays only on the local machine.


## FSUseAis3Api

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Option to disable the use of the AISv3 inventory API. NOTE: This setting has NO EFFECT in Second Life!


## FSUseAltOOC

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Set to TRUE to use the keyboard shortcut Alt+Enter to send ((OOC)) messages to Nearby Chat.


## FSUseAntiSpamMine

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use the Anti-Spam System even for the user's own objects


## FSUseBWEmojis

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Black and White Emojis.


## FSUseBuiltInHistory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Open the conversation transcript in the built in log viewer.


## FSUseChatMentionAutoComplete

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable auto-completion when typing @ mentions in chat.


## FSUseCompactEnvironmentFloaters

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, use custom compact floaters to edit environment settings.


## FSUseCtrlShout

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Set to TRUE to use the keyboard shortcut Ctrl+Enter to Shout in Nearby Chat.


## FSUseFSLegacySearch

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Uses Firestorm's legacy search if enabled - the Linden Lab version instead if disabled


## FSUseLegacyClienttags

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: 0=Off, 1=Local Client tags, 2=Download Client tags (needs relog)


## FSUseLegacyCursors

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use 1.x style cursors instead


## FSUseLegacyInventoryAcceptMessages

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the viewer will send accept/decline response for inventory offers after the according button has been pressed and not if the item has been received at the receiver's inventory already.


## FSUseLegacyLoginPanel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the legacy layout version of the login panel will be used


## FSUseLegacyObjectProperties

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the legacy object profile floater will be used when opening object properties.


## FSUseLegacyUnsupportedHardwareChecks

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, Firestorm will perform utterly pointless checks that probably made sense in 2004.


## FSUseNearbyChatConsole

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display popup chat embedded into the read-only world console (v1-style) instead of overlayed floaters (v2-style)


## FSUseNewRegionRestartNotification

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the new region restart notification instead of the old one with toasts


## FSUseNewTexturePanel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the new Texture/Material editor panel in build mode


## FSUsePrettyEmojiButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use an emoji for the emoji button.


## FSUseReadOfflineMsgsCap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, use the ReadOfflineMsgsCap to request offline messages at login


## FSUseShiftWhisper

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Set to TRUE to use the keyboard shortcut Shift+Enter to Whisper in Nearby Chat.


## FSUseSingleLineChatEntry

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use single line chat entry instead of auto-expanding chat entry


## FSUseSmallCameraFloater

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, the camera floater will be smaller and not contain the camera preset controls.


## FSUseStandaloneBlocklistFloater

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, Firestorm will use a standalone floater for the blocklist.


## FSUseStandaloneGroupFloater

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, Firestorm will use a standalone floater for each group profile.


## FSUseStandalonePlaceDetailsFloater

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, Firestorm will use a standalone floater for each landmark details, teleport history details and parcel details view.


## FSUseStandaloneTeleportHistoryFloater

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, Firestorm will use a standalone floater for the teleport history view.


## FSUseStatsInsteadOfLagMeter

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clicking on traffic indicator (upper right) toggles Statistics window, not the Lag Meter window


## FSUseV2Friends

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Makes Comm->Friends and Comm->Groups open the v2 based windows.


## FSVolumeControlsPanelOpen

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal control for visibility of volume control panel.


## FSWearableFavoritesSortOrder

- Type: U32 | Default value: `3` | Persisted: 1

- Comment: The sort order for the wearable favorites item list


## FSWorldMapDoubleclickTeleport

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, double click teleports on the world map will be enabled (default).


## FSdataQAtest

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable testing fsdata instead of the normal fsdata


## FSllOwnerSayToScriptDebugWindowRouting

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Routing options for FSllOwnerSayToScriptDebugWindow (0 = both tabs, 1 = only object's own tab, 2 = only [ALL SCRIPTS] tab). Errors will still go to both.


## FakeInitialOutfitName

- Type: String | Default value: `` | Persisted: 1

- Comment: Pretend that this is first time login and specified name was chosen


## FastCacheFetchEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable texture fast cache fetching if set


## FilterItemsMaxTimePerFrameVisible

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Max time devoted to items filtering per frame for visible inventory listings (in milliseconds)


## FindLandArea

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables filtering of land search results by area


## FindLandPrice

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables filtering of land search results by price


## FindLandType

- Type: String | Default value: `All` | Persisted: 1

- Comment: Controls which type of land you are searching for in Find Land interface ("All", "Auction", "For Sale")


## FindOriginalOpenWindow

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sets the action for 'Find original' and 'Show in Inventory' (0 - shows item in main Inventory, 1 - opens a new single-folder window)


## FirstLoginThisInstall

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Specifies that you have not logged in with the viewer since you performed a clean install


## FirstName

- Type: String | Default value: `` | Persisted: 1

- Comment: Login first name


## FirstPersonAvatarVisible

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display avatar and attachments below neck while in mouse look


## FirstRunThisInstall

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Specifies that you have not run the viewer since you performed a clean install


## FirstSelectedDisabledPopups

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Return false if there is not disabled popup selected in the list of floater preferences popups


## FirstSelectedEnabledPopups

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Return false if there is not enable popup selected in the list of floater preferences popups


## FirstUseFlyOverride

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether the next use of the Fly Override would be the first use


## FixedWeather

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Weather effects do not change over time


## FlashCount

- Type: S32 | Default value: `8` | Persisted: 1

- Comment: Number of flashes of item. Requires restart.


## FlashPeriod

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Period at which item flash (seconds). Requires restart.


## FloaterActiveSpeakersSortAscending

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to sort up or down


## FloaterActiveSpeakersSortColumn

- Type: String | Default value: `speaking_status` | Persisted: 1

- Comment: Column name to sort on


## FloaterMapEast

- Type: String | Default value: `E` | Persisted: 1

- Comment: Floater Map East Label


## FloaterMapNorth

- Type: String | Default value: `N` | Persisted: 1

- Comment: Floater Map North Label


## FloaterMapNorthEast

- Type: String | Default value: `NE` | Persisted: 1

- Comment: Floater Map North-East Label


## FloaterMapNorthWest

- Type: String | Default value: `NW` | Persisted: 1

- Comment: Floater Map North-West Label


## FloaterMapSouth

- Type: String | Default value: `S` | Persisted: 1

- Comment: Floater Map South Label


## FloaterMapSouthEast

- Type: String | Default value: `SE` | Persisted: 1

- Comment: Floater Map South-East Label


## FloaterMapSouthWest

- Type: String | Default value: `SW` | Persisted: 1

- Comment: Floater Map South-West Label


## FloaterMapWest

- Type: String | Default value: `W` | Persisted: 1

- Comment: Floater Map West Label


## FloaterStatisticsRect

- Type: Rect | Default value: `0 400 250 0` | Persisted: 1

- Comment: Rectangle for chat transcript


## FlycamAbsolute

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Treat Flycam values as absolute positions (not deltas).


## FlycamAxisDeadZone0

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 0 dead zone.


## FlycamAxisDeadZone1

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 1 dead zone.


## FlycamAxisDeadZone2

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 2 dead zone.


## FlycamAxisDeadZone3

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 3 dead zone.


## FlycamAxisDeadZone4

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 4 dead zone.


## FlycamAxisDeadZone5

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 5 dead zone.


## FlycamAxisDeadZone6

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 6 dead zone.


## FlycamAxisScale0

- Type: F32 | Default value: `2.10` | Persisted: 1

- Comment: Flycam axis 0 scaler.


## FlycamAxisScale1

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Flycam axis 1 scaler.


## FlycamAxisScale2

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Flycam axis 2 scaler.


## FlycamAxisScale3

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Flycam axis 3 scaler.


## FlycamAxisScale4

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 4 scaler.


## FlycamAxisScale5

- Type: F32 | Default value: `0.15` | Persisted: 1

- Comment: Flycam axis 5 scaler.


## FlycamAxisScale6

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 6 scaler.


## FlycamBuildModeScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale factor to apply to flycam movements when in build mode.


## FlycamFeathering

- Type: F32 | Default value: `2.75` | Persisted: 1

- Comment: Flycam feathering (less is softer)


## FlyingAtExit

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Was flying when last logged out, so fly when logging in


## FocusOffsetRearView

- Type: Vector3D | Default value: `1.0 0.0 1.0` | Persisted: 1

- Comment: Initial focus point offset relative to avatar for the camera preset Rear View (x-axis is forward)


## FocusPosOnLogout

- Type: Vector3D | Default value: `0.0 0.0 0.0` | Persisted: 1

- Comment: Camera focus point when last logged out (global coordinates)


## FolderAutoOpenDelay

- Type: F32 | Default value: `0.75` | Persisted: 1

- Comment: Seconds before automatically expanding the folder under the mouse when performing inventory drag and drop


## FontScreenDPI

- Type: F32 | Default value: `96.0` | Persisted: 1

- Comment: Font resolution, higher is bigger (pixels per inch)


## ForceAddressSize

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Force Windows update to 32-bit or 64-bit viewer.


## ForceAssetFail

- Type: U32 | Default value: `255` | Persisted: 1

- Comment: Force wearable fetches to fail for this asset type.


## ForceInitialCOFDelay

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Number of seconds to delay initial processing of COF contents


## ForceLoginURL

- Type: String | Default value: `` | Persisted: 1

- Comment: Force a specified URL for login page content - used if exists


## ForceMissingType

- Type: U32 | Default value: `255` | Persisted: 1

- Comment: Force this wearable type to be missing from COF


## ForceShowGrid

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Always show grid dropdown on login screen


## FramePerSecondLimit

- Type: U32 | Default value: `60` | Persisted: 1

- Comment: Controls upper limit of frames per second


## FreezeTime

- Type: Boolean | Default value: `0` | Persisted: 0


## FriendsListHideUsernames

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show both Display name and Username in Friend list


## FriendsListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide online and all friends icons in the friend list


## FriendsListShowPermissions

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide permission icons in the friend list


## FriendsSortOrder

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Specifies sort order for friends (0 = by name, 1 = by online status)


## FullScreen

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Run a fullscreen session. MacOS not supported


## FullScreenAspectRatio

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Aspect ratio of fullscreen display (width / height)


## FullScreenAutoDetectAspectRatio

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Automatically detect proper aspect ratio for fullscreen display


## GLTFEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enable GLTF support.  Set to true by simulator if the simulator you are connected to supports GLTF Asset upload.  WARNING: Manually setting this to true will enable buttons that can drain your L$ balance by implicitly uploading textures without asking.


## GameControl

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Game controller settings: global per-mode action mappings plus per-device hardware config. Empty means use built-in defaults.


## GenericErrorPageURL

- Type: String | Default value: `https://common-flash-secondlife-com.s3.amazonaws.com/viewer/v2.6/agni/404.html` | Persisted: 1

- Comment: URL to set as a property on LLMediaControl to navigate to if the a page completes with a 400-499 HTTP status code


## GesturesEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created gesture


## GesturesMarketplaceURL

- Type: String | Default value: `https://marketplace.secondlife.com/products/search?search[category_id]=200&search[maturity][]=General&search[page]=1&search[per_page]=12` | Persisted: 0

- Comment: URL to the Gestures Marketplace


## GesturesNextOwnerCopy

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created gestures can be copied by next owner


## GesturesNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created gestures can be modified by next owner


## GesturesNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created gestures can be resold or given away by next owner


## GesturesShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created gestures are shared with the currently active group


## GoogleTranslateAPIKey

- Type: String | Default value: `` | Persisted: 1

- Comment: Google Translate API key


## GridCrossSections

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Highlight cross sections of prims with grid manipulation plane.


## GridDrawSize

- Type: F32 | Default value: `12.0` | Persisted: 1

- Comment: Visible extent of 2D snap grid (meters)


## GridListDownload

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to fetch a grid list from the URL specified in GridListDownloadURL.


## GridListDownloadURL

- Type: String | Default value: `http://phoenixviewer.com/app/fsdata/grids.xml` | Persisted: 1

- Comment: Fetch a grid list from this URL.


## GridMode

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Snap grid reference frame (0 = world, 1 = local, 2 = reference object)


## GridOpacity

- Type: F32 | Default value: `0.699999988079` | Persisted: 1

- Comment: Grid line opacity (0.0 = completely transparent, 1.0 = completely opaque)


## GridResolution

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Size of single grid step (meters)


## GridStatusFloaterRect

- Type: Rect | Default value: `0 520 625 0` | Persisted: 1

- Comment: Web profile floater dimensions


## GridStatusRSS

- Type: String | Default value: `https://status.secondlifegrid.net/history.atom` | Persisted: 1

- Comment: URL that points to SL Grid Status RSS


## GridStatusUpdateDelay

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Timer delay for updating Grid Status RSS.


## GridSubUnit

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display fractional grid steps, relative to grid size


## GridSubdivision

- Type: S32 | Default value: `32` | Persisted: 1

- Comment: Maximum number of times to divide single snap grid unit when GridSubUnit is true


## GroupListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide group icons in the group list


## GroupMembersSortOrder

- Type: String | Default value: `name` | Persisted: 1

- Comment: The order by which group members will be sorted (name|donated|online)


## GroupSnoozeTime

- Type: S32 | Default value: `900` | Persisted: 1

- Comment: Amount of time (in seconds) group chat will be snoozed for


## GroupTitlesTagMode

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Select Group Titles tag mode: 0 - no group tags, 1 - only my group tag, 2 - all group tags


## HUDScaleFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of HUD attachments


## HeadlessClient

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Run in headless mode by disabling GL rendering, keyboard, etc


## HeightUnits

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Determines which metric units are used: 1(TRUE) for meter and 0(FALSE) for foot.


## HelpFloaterOpen

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show Help Floater on login?


## HelpURLFormat

- Type: String | Default value: `https://wiki.firestormviewer.org/[TOPIC]` | Persisted: 1

- Comment: URL pattern for help page; arguments will be encoded; see llviewerhelp.cpp:buildHelpURL for arguments


## HideSelectedObjects

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hide Selected Objects


## HideUIControls

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Hide all menu items and buttons


## HighResSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Double resolution of snapshot from current window resolution


## HomeSidePanelURL

- Type: String | Default value: `https://viewer-sidebar.secondlife.com/sidebar.html` | Persisted: 1

- Comment: URL for the web page to display in the Home side panel


## HostID

- Type: String | Default value: `` | Persisted: 0

- Comment: Machine identifier for hosted Second Life instances


## HoverHeightAffectsCamera

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Camera view is affected by Hover Height setting


## HowToHelpURL

- Type: String | Default value: `https://wiki.firestormviewer.org/start#basic_functions` | Persisted: 1

- Comment: URL for How To help content


## HttpPipelining

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If true, viewer will attempt to pipeline HTTP requests.


## HttpProxyType

- Type: String | Default value: `Socks` | Persisted: 1

- Comment: Proxy type to use for HTTP operations


## HttpRangeRequestsDisable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, viewer will not issue GET requests with 'Range:' headers for meshes and textures.  May resolve problems with certain ISPs and networking gear.


## IMShowControlPanel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show IM Control Panel


## IMShowNamesForP2PConv

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable(disable) showing of a names in the chat.


## IMShowTime

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable(disable) timestamp showing in the chat.


## IgnoreAllNotifications

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore all notifications so we never need user input on them.


## IgnoreFOVZoomForLODs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore zoom effect(CTRL+0) when calculating lods.


## IgnorePixelDepth

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore pixel depth settings.


## ImagePipelineUseHTTP

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If TRUE use HTTP GET to fetch textures from the server


## ImporterDebugMode

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: At 0 does nothing, at 1 dumps skinning data near orifinal file, at 2 dumps skining data and positions/weights of first 5 models, at 3 dumps skinning data and models as llsd


## ImporterDebugVerboseLogging

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enable debug output to more precisely identify sources of import errors. Warning: the output can slow down import on many machines.


## ImporterLegacyMatching

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable index based model matching.


## ImporterModelLimit

- Type: U32 | Default value: `768` | Persisted: 1

- Comment: Limits amount of importer generated (when over 8 faces) models for dae and gltf files


## ImporterPreprocessDAE

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable preprocessing for DAE files to fix some ColladaDOM related problems (like support for space characters within names and ids).


## InBandwidth

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Incoming bandwidth throttle (bps)


## InactiveFloaterTransparency

- Type: F32 | Default value: `0.95` | Persisted: 1

- Comment: Transparency of inactive floaters (floaters that have no focus)


## IndirectMaxComplexity

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: Controls RenderAvatarMaxComplexity in a non-linear fashion (do not set this value)


## IndirectMaxNonImpostors

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: Controls RenderAvatarMaxNonImpostors in a non-linear fashion (do not set this value)


## InstallLanguage

- Type: String | Default value: `default` | Persisted: 1

- Comment: Language passed from installer (for UI)


## InternalShowGroupNoticesTopRight

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Holds the information if group notifications should be shown in top right corner of the screen throughout the session.


## InterpolationPhaseOut

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Seconds to phase out interpolated motion


## InterpolationTime

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: How long to extrapolate object motion after last packet received


## InventoryAddAttachmentBehavior

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Defines behavior when hitting return on an inventory item (unused in favour of FSDoubleClickAddInventoryObjects)


## InventoryAutoOpenDelay

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Seconds before automatically opening inventory when mouse is over inventory button when performing inventory drag and drop


## InventoryDebugSimulateLateOpRate

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rate at which we simulate late-completing copy/link requests in some operations


## InventoryDebugSimulateOpFailureRate

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rate at which we simulate failures of copy/link requests in some operations


## InventoryDisplayInbox

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: UNUSED - Controlled via FSShowInboxFolder and FSAlwaysShowInboxButton: Override received items inventory inbox display


## InventoryExposeFolderID

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Allows copying folder id from context menu


## InventoryFavoritesColorText

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: render favorite items using InventoryFavoriteText as color


## InventoryFavoritesUseHollowStar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show star near folders that contain favorites


## InventoryFavoritesUseStar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show star near favorited items in inventory


## InventoryLinking

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable ability to create links to folders and items via "Paste as link".


## InventoryOutboxLogging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable debug output associated with the Merchant Outbox.


## InventoryOutboxMakeVisible

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable making the Merchant Outbox visible in the inventory for debug purposes.


## InventoryOutboxMaxFolderCount

- Type: U32 | Default value: `20` | Persisted: 0

- Comment: Maximum number of subfolders allowed in a listing in the merchant outbox.


## InventoryOutboxMaxFolderDepth

- Type: U32 | Default value: `4` | Persisted: 0

- Comment: Maximum number of nested levels of subfolders allowed in a listing in the merchant outbox.


## InventoryOutboxMaxItemCount

- Type: U32 | Default value: `200` | Persisted: 0

- Comment: Maximum number of items allowed in a listing in the merchant outbox.


## InventoryOutboxMaxStockItemCount

- Type: U32 | Default value: `200` | Persisted: 0

- Comment: Maximum number of items allowed in a stock folder.


## InventoryShowFavoritesTab

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide Favorites tab in the Inventory floater


## InventoryShowRecentTab

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide Recent tab in the Inventory floater


## InventoryShowWornTab

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide Worn tab in the Inventory floater


## InventorySortOrder

- Type: U32 | Default value: `7` | Persisted: 1

- Comment: Specifies sort key for inventory items (+0 = name, +1 = date, +2 = folders always by name, +4 = system folders to top)


## InventoryTrashMaxCapacity

- Type: U32 | Default value: `5000` | Persisted: 1

- Comment: Maximum capacity of the Trash folder. User will be offered to clean it up when exceeded.


## InvertMouse

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When in mouselook, moving mouse up looks down and vice verse (FALSE = moving up looks up)


## JoinFloaterOverlayOpacity

- Type: F32 | Default value: `0.8` | Persisted: 1

- Comment: Opacity of the screen darkening overlay behind the Join floater


## JoinURL

- Type: String | Default value: `https://join.secondlife.com/` | Persisted: 1

- Comment: URL opened in the Join floater on the login screen


## JoystickAvatarEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the Joystick to control Avatar movement.


## JoystickAxis0

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 0 ([0, 5]).


## JoystickAxis1

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 1 ([0, 5]).


## JoystickAxis2

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 2 ([0, 5]).


## JoystickAxis3

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 3 ([0, 5]).


## JoystickAxis4

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 4 ([0, 5]).


## JoystickAxis5

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 5 ([0, 5]).


## JoystickAxis6

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 6 ([0, 5]).


## JoystickBuildEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the Joystick to move edited objects.


## JoystickDeviceUUID

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Preffered device ID.


## JoystickEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables Joystick Input.


## JoystickFlycamEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Enables the Joystick to control the flycam.


## JoystickInitialized

- Type: String | Default value: `` | Persisted: 1

- Comment: Whether or not a joystick has been detected and initialized.


## JoystickMouselookYaw

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pass joystick yaw to scripts in mouse look.


## JoystickRunThreshold

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Input threshold to initiate running


## Jpeg2000AdvancedCompression

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use advanced Jpeg2000 compression options (precincts, blocks, ordering, markers)


## Jpeg2000BlocksSize

- Type: S32 | Default value: `64` | Persisted: 1

- Comment: Size of encoding blocks. Assumed square and same for all levels. Must be power of 2. Max 64, Min 4.


## Jpeg2000PrecinctsSize

- Type: S32 | Default value: `256` | Persisted: 1

- Comment: Size of image precincts. Assumed square and same for all levels. Must be power of 2.


## KeepAspectForDiskSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Always keep width to height ratio in local snapshots the same, regardless of image size


## KeepAspectForEmailSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Always keep width to height ratio in postcard snapshots the same, regardless of image size


## KeepAspectForInventorySnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Always keep width to height ratio in inventory snapshots the same, regardless of image size


## KeepAspectForProfileSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Always keep width to height ratio in profile snapshots the same, regardless of image size


## KeepAspectForSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Always keep width to height ratio in snapshots the same, regardless of image size


## KeepAutoTuneLock

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: When enabled the AutoTuneLock will be maintainted all following sessions.


## LSLFindCaseInsensitivity

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use case insensitivity when searching for text


## LSLFindDirection

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Direction text will be searched for a match (0: down ; 1: up)


## LSLFontSizeName

- Type: String | Default value: `Monospace` | Persisted: 1

- Comment: UNUSED - Text font size in LSL editor


## LSLHelpURL

- Type: String | Default value: `https://wiki.secondlife.com/wiki/[LSL_STRING]` | Persisted: 1

- Comment: URL that points to LSL help files, with [LSL_STRING] corresponding to the referenced LSL function or keyword


## LagMeterShrunk

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Last large/small state for lag meter


## LandBrushForce

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Multiplier for land modification brush force.


## LandBrushSize

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Size of affected region when using terraform tool


## LandmarksSortedByDate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Reflects landmarks panel sorting order.


## Language

- Type: String | Default value: `default` | Persisted: 1

- Comment: Specifies language (for UI)


## LanguageIsPublic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Let other residents see our language information


## LastAppearanceTab

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected tab in appearance floater


## LastConnectedGrid

- Type: String | Default value: `` | Persisted: 1

- Comment: Last grid with successful connection


## LastFeatureVersion

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: [DO NOT MODIFY] Feature Table Version number for tracking rendering system changes


## LastGPUString

- Type: String | Default value: `` | Persisted: 1

- Comment: [DO NOT MODIFY] previous GPU id string for tracking hardware changes


## LastJ2CVersion

- Type: String | Default value: `` | Persisted: 1

- Comment: Last used J2C engine version


## LastMediaSettingsTab

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected tab in media settings window


## LastName

- Type: String | Default value: `` | Persisted: 1

- Comment: Login last name


## LastPrefTab

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected tab in preferences window


## LastRunVersion

- Type: String | Default value: `0.0.0` | Persisted: 1

- Comment: Version number of last instance of the viewer that you ran


## LastSelectedGrass

- Type: String | Default value: `` | Persisted: 1

- Comment: The last selected grass option from the build tools


## LastSelectedTree

- Type: String | Default value: `` | Persisted: 1

- Comment: The last selected tree option from the build tools


## LastSnapshotToDiskHeight

- Type: S32 | Default value: `768` | Persisted: 1

- Comment: The height of the last disk snapshot, in px


## LastSnapshotToDiskResolution

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: At what resolution should snapshots be taken to disk. 0=Current Window, 1=320x240, 2=640x480, 3=800x600, 4=1024x768, 5=1280x1024, 6=1600x1200, 7=Custom


## LastSnapshotToDiskWidth

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: The width of the last disk snapshot, in px


## LastSnapshotToEmailHeight

- Type: S32 | Default value: `768` | Persisted: 1

- Comment: The height of the last email snapshot, in px


## LastSnapshotToEmailResolution

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: At what resolution should snapshots be taken as postcards. 0=Current Window, 1=640x480, 2=800x600, 3=1024x768, 4=Custom


## LastSnapshotToEmailWidth

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: The width of the last email snapshot, in px


## LastSnapshotToInventoryHeight

- Type: S32 | Default value: `512` | Persisted: 1

- Comment: The height of the last texture snapshot, in px


## LastSnapshotToInventoryResolution

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: At what resolution should snapshots be taken into inventory. 0=Current Window, 1=128x128, 2=256x256, 3=512x512, 4=Custom


## LastSnapshotToInventoryWidth

- Type: S32 | Default value: `512` | Persisted: 1

- Comment: The width of the last texture snapshot, in px


## LastSnapshotToProfileHeight

- Type: S32 | Default value: `768` | Persisted: 1

- Comment: The height of the last profile snapshot, in px


## LastSnapshotToProfileResolution

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: At what resolution should snapshots be taken to the profile. 0=Current Window, 1=640x480, 2=800x600, 3=1024x768, 4=Custom


## LastSnapshotToProfileWidth

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: The width of the last profile snapshot, in px


## LastUIFeatureVersion

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: UI Feature Version number for tracking feature notification between viewer builds


## LeapCommand

- Type: LLSD | Default value: `` | Persisted: 0

- Comment: Zero or more command lines to run LLSD Event API Plugin programs.


## LeapPlaybackEventsCommand

- Type: LLSD | Default value: `` | Persisted: 0

- Comment: Command line to use leap to launch playback of event recordings


## LeaveMouselook

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Exit Mouselook mode via S or Down Arrow keys while sitting 


## LetterKeysAffectsMovementNotFocusChatBar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When printable characters keys (possibly with Shift held) are pressed, the chat bar does not take focus and movement is affected instead (WASD etc.)


## LimitDragDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Limit translation of object via translate tool


## LimitLookAtTarget

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to clamp the look at targets around the avatar head before sending (UNUSED)


## LimitLookAtTargetDistance

- Type: F32 | Default value: `2` | Persisted: 1

- Comment: Distance to limit look at target to (UNUSED)


## LimitRadarByRange

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Restrict Radar to a range near you


## LimitSelectDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Disallow selection of objects beyond max select distance


## LinkReplaceBatchPauseTime

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: The time in seconds between two batches in a link replace operation


## LinkReplaceBatchSize

- Type: U32 | Default value: `25` | Persisted: 1

- Comment: The maximum size of a batch in a link replace operation


## LipSyncAah

- Type: String | Default value: `257998776531013446642343` | Persisted: 1

- Comment: Aah (jaw opening) babble loop


## LipSyncAahPowerTransfer

- Type: String | Default value: `0000123456789` | Persisted: 1

- Comment: Transfer curve for Voice Interface power to aah lip sync amplitude


## LipSyncEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: 0 disable lip-sync, 1 enable babble loop


## LipSyncOoh

- Type: String | Default value: `1247898743223344444443200000` | Persisted: 1

- Comment: Ooh (mouth width) babble loop


## LipSyncOohAahRate

- Type: F32 | Default value: `24.0` | Persisted: 1

- Comment: Rate to babble Ooh and Aah (/sec)


## LipSyncOohPowerTransfer

- Type: String | Default value: `0012345566778899` | Persisted: 1

- Comment: Transfer curve for Voice Interface power to ooh lip sync amplitude


## LocalCacheVersion

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Version number of cache


## LocalFileSystemBrowsingEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable/disable access to the local file system via the file picker


## LocalTerrainAsset1

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.


## LocalTerrainAsset2

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.


## LocalTerrainAsset3

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.


## LocalTerrainAsset4

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.


## LocalTerrainPaintEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enables local paintmap if LocalTerrainAsset1, etc are set


## LocalTerrainTransform1OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set


## LocalTerrainTransform1OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set


## LocalTerrainTransform1Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set


## LocalTerrainTransform1ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set


## LocalTerrainTransform1ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set


## LocalTerrainTransform2OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set


## LocalTerrainTransform2OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set


## LocalTerrainTransform2Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set


## LocalTerrainTransform2ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set


## LocalTerrainTransform2ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set


## LocalTerrainTransform3OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set


## LocalTerrainTransform3OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set


## LocalTerrainTransform3Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set


## LocalTerrainTransform3ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set


## LocalTerrainTransform3ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set


## LocalTerrainTransform4OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set


## LocalTerrainTransform4OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set


## LocalTerrainTransform4Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set


## LocalTerrainTransform4ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set


## LocalTerrainTransform4ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set


## LockToolbars

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, toolbars are locked and buttons can not be dragged around, added or removed.


## LogInventoryDecline

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Log in system chat whenever an inventory offer is declined


## LogMessages

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log network traffic


## LogMetrics

- Type: String | Default value: `` | Persisted: 0

- Comment: Log viewer metrics


## LogPerformance

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Log performance analysis for a particular viewer run


## LogTextureDownloadsToSimulator

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Send a digest of texture info to the region


## LogTextureDownloadsToViewerLog

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Send texture download details to the viewer log


## LogTextureNetworkTraffic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log network traffic for textures


## LogWearableAssetSave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Save copy of saved wearables to log dir


## LoginContentVersion

- Type: String | Default value: `2` | Persisted: 0

- Comment: Version of login page web based content to display


## LoginLocation

- Type: String | Default value: `last` | Persisted: 1

- Comment: Default Login location ('last', 'home') preference


## LoginPage

- Type: String | Default value: `` | Persisted: 1

- Comment: Login authentication page.


## LoginSRVTimeout

- Type: F32 | Default value: `90.0` | Persisted: 1

- Comment: Duration in seconds of the login SRV request timeout


## LosslessJ2CUpload

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use lossless compression for small image uploads


## MFAHash

- Type: String | Default value: `` | Persisted: 0

- Comment: Override MFA state hash for authentication


## MainChatbarVisible

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal, volatile control variable to enable/disable the chat button in the toolbar.


## MainWorkTime

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Max time per frame devoted to mainloop work queue (in milliseconds)


## MainloopTimeoutDefault

- Type: F32 | Default value: `120.0` | Persisted: 1

- Comment: Timeout duration for mainloop lock detection during teleports, login and logout, in seconds.


## MainloopTimeoutStarted

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Timeout duration for mainloop lock detection when logged in and not teleporting, in seconds.


## MapScale

- Type: F32 | Default value: `128.0` | Persisted: 1

- Comment: World map zoom level (pixels per region)


## MapServerURL

- Type: String | Default value: `https://map.secondlife.com/` | Persisted: 0

- Comment: World map URL template for locating map tiles


## MapShowEvents

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show events on world map


## MapShowGridCoords

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows/hides the grid coordinates of each region on the world map.


## MapShowInfohubs

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show infohubs on the world map


## MapShowLandForSale

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show land for sale on world map


## MapShowPeople

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show other users on world map


## MapShowTelehubs

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show telehubs on world map


## Marker

- Type: String | Default value: `` | Persisted: 1

- Comment: [NOT USED]


## MarketplaceListingsLogging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable debug output associated with the Marketplace Listings (SLM) API.


## MarketplaceListingsSortOrder

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Specifies sort for marketplace listings


## MarketplaceURL

- Type: String | Default value: `https://marketplace.secondlife.com/` | Persisted: 0

- Comment: URL to the Marketplace


## MarketplaceURL_bodypartFemale

- Type: String | Default value: `https://marketplace.secondlife.com/` | Persisted: 0

- Comment: URL to the Marketplace Bodyparts Female


## MarketplaceURL_bodypartMale

- Type: String | Default value: `https://marketplace.secondlife.com/` | Persisted: 0

- Comment: URL to the Marketplace Bodyparts Male


## MarketplaceURL_clothingFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/clothing_female_avatar` | Persisted: 0

- Comment: URL to the Marketplace Clothing Female


## MarketplaceURL_clothingMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/clothing_male_avatar` | Persisted: 0

- Comment: URL to the Marketplace Clothing Male


## MarketplaceURL_eyesFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_eyes` | Persisted: 0

- Comment: URL to the Marketplace Eyes Female


## MarketplaceURL_eyesMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_eyes` | Persisted: 0

- Comment: URL to the Marketplace Eyes Male


## MarketplaceURL_glovesFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/gloves_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Gloves Female


## MarketplaceURL_glovesMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/gloves_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Gloves Male


## MarketplaceURL_hairFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_hair` | Persisted: 0

- Comment: URL to the Marketplace Hair Female


## MarketplaceURL_hairMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_hair` | Persisted: 0

- Comment: URL to the Marketplace Hair Male


## MarketplaceURL_jacketFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/jacket_womens` | Persisted: 0

- Comment: URL to the Marketplace Jacket Female


## MarketplaceURL_jacketMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/jacket_mens` | Persisted: 0

- Comment: URL to the Marketplace Jacket Male


## MarketplaceURL_objectFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/attachments` | Persisted: 0

- Comment: URL to the Marketplace Attachments Female


## MarketplaceURL_objectMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/attachments` | Persisted: 0

- Comment: URL to the Marketplace Attachments Male


## MarketplaceURL_pantsFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/pants_women` | Persisted: 0

- Comment: URL to the Marketplace Pants Female


## MarketplaceURL_pantsMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/pants_men` | Persisted: 0

- Comment: URL to the Marketplace Pants Male


## MarketplaceURL_physicsFemale

- Type: String | Default value: `http://marketplace.secondlife.com` | Persisted: 0

- Comment: URL to the Marketplace Bodyparts Female


## MarketplaceURL_physicsMale

- Type: String | Default value: `http://marketplace.secondlife.com/` | Persisted: 0

- Comment: URL to the Marketplace Bodyparts Male


## MarketplaceURL_shapeFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_shape` | Persisted: 0

- Comment: URL to the Marketplace Shape Female


## MarketplaceURL_shapeMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_shape` | Persisted: 0

- Comment: URL to the Marketplace Shape Male


## MarketplaceURL_shirtFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shirt_womens` | Persisted: 0

- Comment: URL to the Marketplace Shirt Female


## MarketplaceURL_shirtMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shirt_mens` | Persisted: 0

- Comment: URL to the Marketplace Shirt Male


## MarketplaceURL_shoesFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shoes_women` | Persisted: 0

- Comment: URL to the Marketplace Shoes Female


## MarketplaceURL_shoesMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shoes_men` | Persisted: 0

- Comment: URL to the Marketplace Shoes Male


## MarketplaceURL_skinFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_skin` | Persisted: 0

- Comment: URL to the Marketplace Skin Female


## MarketplaceURL_skinMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_skin` | Persisted: 0

- Comment: URL to the Marketplace Skins Male


## MarketplaceURL_skirtFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/skirts_women` | Persisted: 0

- Comment: URL to the Marketplace Skirt Female


## MarketplaceURL_skirtMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/skirts_women` | Persisted: 0

- Comment: URL to the Marketplace Skirt Male


## MarketplaceURL_socksFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/socks_women` | Persisted: 0

- Comment: URL to the Marketplace Socks Female


## MarketplaceURL_socksMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/socks_women` | Persisted: 0

- Comment: URL to the Marketplace Socks Male


## MarketplaceURL_tattooFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/tattoo_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Tattoo Female


## MarketplaceURL_tattooMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/tattoo_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Tattoo Male


## MarketplaceURL_underpantsFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/underwear_women` | Persisted: 0

- Comment: URL to the Marketplace Underwear Female


## MarketplaceURL_underpantsMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/underwear_men` | Persisted: 0

- Comment: URL to the Marketplace Underwear Male


## MarketplaceURL_undershirtFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/undershirt_womens` | Persisted: 0

- Comment: URL to the Marketplace Undershirt Female


## MarketplaceURL_undershirtMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/undershirt_mens` | Persisted: 0

- Comment: URL to the Marketplace Undershirt Male


## MaterialsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created GLTF material


## MaterialsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created GLTF material can be copied by next owner


## MaterialsNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created GLTF material can be modified by next owner


## MaterialsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created GLTF material can be resold or given away by next owner


## MaterialsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created GLTF materials are shared with the currently active group


## MaxAttachmentComplexity

- Type: F32 | Default value: `1.0E6` | Persisted: 1

- Comment: Attachment's render weight limit


## MaxDragDistance

- Type: F32 | Default value: `48.0` | Persisted: 1

- Comment: Maximum allowed translation distance in a single operation of translate tool (meters from start point)


## MaxHeapSize

- Type: F32 | Default value: `1.6` | Persisted: 1

- Comment: Maximum heap size on 32-bit builds (GB)


## MaxHeapSize64

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Maximum heap size on 64-bit builds (GB)


## MaxPersistentNotifications

- Type: S32 | Default value: `250` | Persisted: 1

- Comment: Maximum amount of persistent notifications


## MaxSelectDistance

- Type: F32 | Default value: `128.0` | Persisted: 1

- Comment: Maximum allowed selection distance (meters from avatar)


## MaxWearableWaitTime

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Max seconds to wait for wearable assets to fetch.


## MePanelOpened

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Indicates that Me Panel was opened at least once after Viewer was installed


## MediaAutoPlayHuds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically play HUD media


## MediaControlFadeTime

- Type: F32 | Default value: `1.5` | Persisted: 1

- Comment: Amount of time (in seconds) that the media control fades


## MediaControlTimeout

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Amount of time (in seconds) for media controls to fade with no mouse activity


## MediaEnableFilter

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable media domain filtering


## MediaEnablePopups

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, enable targeted links and JavaScript in media to open new media browser windows without a prompt.


## MediaFilterSinglePrompt

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use a single legacy style dialog for media filter prompt, instead of two seperate allow/deny and whitelist/blacklist prompts.


## MediaFirstClickInteract

- Type: S32 | Default value: `31` | Persisted: 1

- Comment: This setting controls which media (once loaded) does not require a first click to focus before interaction can begin. This allows clicks to be passed directly to media bypassing the focus click requirement. This setting is a bitfield, precomputed values are as follows: Disabled=0; Worn HUDs only=1; Owned objects=2; Friend objects=4; Group objects=8; Landowner objects=16; Any object=32767; All MOAP=32768. For complete details see lltoolpie.h enum MediaFirstClickTypes.


## MediaOnAPrimUI

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show the "link sharing" UI


## MediaPerformanceManagerDebug

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to show debug data for the media performance manager in the nearby media list.


## MediaPluginDebugging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Turn on debugging messages that may help diagnosing media issues (WARNING: May reduce performance).


## MediaPluginForceVLC

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Force use of VLC based media plugin. (Linux Only)


## MediaPluginPipeWireVolumeCatcher

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use PipeWire instead of PulseAudio for controlling web media volume.


## MediaRollOffMax

- Type: F32 | Default value: `80.0` | Persisted: 1

- Comment: Distance at which media volume is set to 0


## MediaRollOffMin

- Type: F32 | Default value: `40.0` | Persisted: 1

- Comment: Adjusts the distance at which media attenuation starts


## MediaRollOffRate

- Type: F32 | Default value: `0.02` | Persisted: 1

- Comment: Multiplier to change rate of media attenuation


## MediaShowOnOthers

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to show media on other avatars


## MediaShowOutsideParcel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show media from outside the current parcel


## MediaShowWithinParcel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show media within the current parcel


## MediaSoundsEarLocation

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Location of the virtual ear for media and sounds


## MediaTentativeAutoPlay

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: This is a tentative flag that may be temporarily set off by the user, until she teleports


## MemoryFailurePreventionEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If set, the viewer will try to throttle memory allocations when memory is low (32bit systems only)


## MemoryLogFrequency

- Type: F32 | Default value: `600.0` | Persisted: 1

- Comment: Seconds between display of Memory in log (0 for never)


## MemoryPrivatePoolEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Enable the private memory pool management


## MemoryPrivatePoolSize

- Type: U32 | Default value: `512` | Persisted: 1

- Comment: (Deprecated) Size of the private memory pool in MB (min. value is 256)


## MenuAccessKeyTime

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Time (seconds) in which the menu key must be tapped to move focus to the menu bar


## MenuSearch

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide 'Search menus' field


## Mesh2MaxConcurrentRequests

- Type: U32 | Default value: `8` | Persisted: 1

- Comment: Number of connections to use for loading meshes.


## MeshBytesPerTriangle

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Approximation of bytes per triangle to use for determining mesh streaming cost.


## MeshEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expose UI for mesh functionality (may require restart to take effect).


## MeshImportUseSLM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use cached copy of last upload for a dae if available instead of loading dae file from scratch.


## MeshMaxConcurrentRequests

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Number of connections to use for loading meshes (legacy system).


## MeshMetaDataDiscount

- Type: U32 | Default value: `384` | Persisted: 1

- Comment: Number of bytes to deduct for metadata when determining streaming cost.


## MeshMinimumByteSize

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Minimum number of bytes per LoD block when determining streaming cost.


## MeshPreviewBaseColor

- Type: Color4 | Default value: `0.5 0.5 0.5 1.0` | Persisted: 1

- Comment: base diffuse colour for the Mesh uploader


## MeshPreviewBrightnessColor

- Type: Color3 | Default value: `0.9 0.9 0.9` | Persisted: 1

- Comment: Brightness modifier


## MeshPreviewCanvasColor

- Type: Color4 | Default value: `0.169 0.169 0.169 1.0` | Persisted: 1

- Comment: Canvas colour for the Mesh uploader


## MeshPreviewDegenerateEdgeColor

- Type: Color4 | Default value: `1.0 0.0 0.0 1.0` | Persisted: 1

- Comment: Edge colour for the Mesh uploader Degenerate preview


## MeshPreviewDegenerateEdgeWidth

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: line thickness used when display Degenerate is selected in mesh preview


## MeshPreviewDegenerateFillColor

- Type: Color4 | Default value: `1.0 0.0 0.0 0.5` | Persisted: 1

- Comment: Fill colour for the Mesh uploader Degenerate preview


## MeshPreviewDegeneratePointSize

- Type: F32 | Default value: `8.0` | Persisted: 1

- Comment: Large point size used to highlight degenerate triangle vertices in Mesh preview


## MeshPreviewEdgeColor

- Type: Color4 | Default value: `0.4 0.4 0.4 1.0` | Persisted: 1

- Comment: Edge colour for the Mesh uploader preview


## MeshPreviewEdgeWidth

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: line thickness used when display edges is selected in mesh preview


## MeshPreviewPhysicsEdgeColor

- Type: Color4 | Default value: `0.0 0.25 0.5 0.25` | Persisted: 1

- Comment: Edge colour for the Mesh uploader physics preview


## MeshPreviewPhysicsEdgeWidth

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: line thickness used when display physics is selected in mesh preview


## MeshPreviewPhysicsFillColor

- Type: Color4 | Default value: `0.0 0.5 1.0 0.5` | Persisted: 1

- Comment: Fill colour for the Mesh uploader physics preview


## MeshPreviewZoomLimit

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Maximum Zoom level in preview


## MeshTriangleBudget

- Type: U32 | Default value: `250000` | Persisted: 1

- Comment: Target visible triangle budget to use when estimating streaming cost.


## MeshUploadFakeErrors

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Force upload errors (for testing)


## MeshUploadLogXML

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Verbose XML logging on mesh upload


## MeshUploadTimeOut

- Type: S32 | Default value: `600` | Persisted: 1

- Comment: Maximum time in seconds for llcurl to execute a mesh uoloading request


## MeshUseGetMesh1

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, use the legacy GetMesh capability for mesh download requests.  Semi-dynamic (read at region crossings).


## MeshUseHttpRetryAfter

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If TRUE, use Retry-After response headers when rescheduling a mesh request that fails with an HTTP 503 status.  Static.


## MigrateCacheDirectory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Check for old version of disk cache to migrate to current location


## MinObjectsForUnlinkConfirm

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Minimum amount of objects in linkset for showing confirmation dialog


## MinWindowHeight

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: SL viewer minimum window height in pixels


## MinWindowWidth

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: SL viewer minimum window width in pixels


## MiniMapAutoCenter

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Center the focal point of the minimap.


## MiniMapChatRing

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display chat distance ring on mini map


## MiniMapCollisionParcels

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show collision parcels on the mini-map as they become available


## MiniMapForSaleParcels

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show for-sale parcels with a yellow highlight on the mini-map


## MiniMapObjects

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show object layers on the mini-map


## MiniMapPrimMaxRadius

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Radius of the largest prim to show on the MiniMap. Increasing beyond 256 may cause client lag.


## MiniMapPrimMaxVertDistance

- Type: F32 | Default value: `256.0` | Persisted: 1

- Comment: Max height difference between avatar and prim to be shown on the MiniMap. Set to 0.0 to disable.


## MiniMapRotate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Rotate miniature world map to avatar direction


## MiniMapScale

- Type: F32 | Default value: `128.0` | Persisted: 1

- Comment: Miniature world map zoom level (pixels per region)


## MiniMapShowPropertyLines

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show parcel borders on the MiniMap.


## MouseLookEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal, volatile control variable to show if we are currently in mouselook.


## MouseMoon

- Type: Boolean | Default value: `0` | Persisted: 0


## MouseSensitivity

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Controls responsiveness of mouse when in mouselook mode (fraction or multiple of default mouse sensitivity)


## MouseSmooth

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Smooths out motion of mouse when in mouselook mode.


## MouseSun

- Type: Boolean | Default value: `0` | Persisted: 0


## MouseWarpMode

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Controls warping of the mouse to the center of the screen during alt-zoom and mouse look. Useful with certain input devices, mouse sharing programs like Synergy, or running under Parallels. 0 - automatic, 1 - on, 2 - off


## MultiModeDoubleClickFolder

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Sets the action for Double-click on folder in multi-folder view (0 - expands and collapses folder, 1 - opens a new window, 2 – stays in current floater but switches to SFV)


## MuteAmbient

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ambient sound effects, such as wind noise, play at 0 volume


## MuteAudio

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: All audio plays at 0 volume (streaming audio still takes up bandwidth, for example)


## MuteListLimit

- Type: S32 | Default value: `1000` | Persisted: 1

- Comment: Maximum number of entries in the mute list


## MuteMedia

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Media plays at 0 volume (streaming audio still takes up bandwidth)


## MuteMusic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Music plays at 0 volume (streaming audio still takes up bandwidth)


## MuteSounds

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sound effects play at 0 volume


## MuteUI

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: UI sound effects play at 0 volume


## MuteVoice

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Voice plays at 0 volume (streaming audio still takes up bandwidth)


## MuteWhenMinimized

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Mute audio when SL window is minimized


## NameTagDebugAVRezState

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show Avatar Rez state in name tag


## NameTagShowDisplayNames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show display names in name labels


## NameTagShowFriends

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Highlight the name tags of your friends


## NameTagShowGroupTitles

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show group titles in name labels


## NameTagShowUsernames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show usernames in avatar name tags


## NametagOverWater

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render name tag over the transparent water while camera is above the water


## NavBarShowCoordinates

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show coordinates in navigation bar


## NavBarShowParcelProperties

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show parcel property icons in navigation bar


## NearMeRange

- Type: F32 | Default value: `162` | Persisted: 1

- Comment: Search radius for nearby avatars


## NearbyListHideUsernames

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show both Display name and Username in Nearby list


## NearbyListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide people icons in nearby list


## NearbyListShowMap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide map above nearby people list (unused by firestorm)


## NearbyListShowRange

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show range field on nearby avList?


## NearbyPeopleSortOrder

- Type: U32 | Default value: `3` | Persisted: 1

- Comment: Specifies sort order for nearby people (0 = by name, 3 = by distance, 4 = by most recent)


## NearbyToastFadingTime

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Number of seconds while a nearby chat toast is fading 


## NearbyToastLifeTime

- Type: S32 | Default value: `23` | Persisted: 1

- Comment: Number of seconds while a nearby chat toast exists


## NearbyToastWidth

- Type: S32 | Default value: `33` | Persisted: 1

- Comment: Width of a the nearby chat toasts in percent of screen width


## NewCacheLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Change the location of the local disk cache to this


## NewCacheLocationTopFolder

- Type: String | Default value: `` | Persisted: 1

- Comment: Change the top folder location of the local disk cache to this


## NewObjectCreationThrottle

- Type: S32 | Default value: `200` | Persisted: 1

- Comment: maximum number of new objects created per frame, -1 to disable this throttle


## NewObjectCreationThrottleDelayTime

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: time in seconds NewObjectCreationThrottle to take effect after the progress screen is lifted


## NextLoginLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Location to log into for this session - set from command line or the login panel, cleared following a successfull login.


## NextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Newly created objects can be copied by next owner


## NextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Newly created objects can be modified by next owner


## NextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: (obsolete) Newly created objects can be resold or given away by next owner


## NoAudio

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable audio playback.


## NoHardwareProbe

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable hardware probe.


## NoInventoryLibrary

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: (Deprecated) Do not request inventory library.


## NoPreload

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable sound and image preload.


## NoQuickTime

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disable QuickTime for a particular viewer run


## NoVerifySSLCert

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Do not verify SSL peers.


## NonInteractive

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Run in a semi-headless mode where only logging in and logging out needs to work.


## NonvisibleObjectsInMemoryTime

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Number of frames non-visible objects stay in memory before being removed. 0 means max.


## NotMovingHintTimeout

- Type: F32 | Default value: `120.0` | Persisted: 1

- Comment: Number of seconds to wait for resident to move before displaying move hint.


## NotecardsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created notecard


## NotecardsNextOwnerCopy

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created notecards can be copied by next owner


## NotecardsNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created notecards can be modified by next owner


## NotecardsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created notecards can be resold or given away by next owner


## NotecardsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created notecards are shared with the currently active group


## NotificationCanEmbedInIM

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Controls notification panel embedding in IMs (0 = default, 1 = focused, 2 = never)


## NotificationChannelHeightRatio

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Notification channel and World View ratio(0.0 - always show 1 notification, 1.0 - max ratio).


## NotificationChannelRightMargin

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Space between toasts and a right border of an area where they can appear


## NotificationConferenceIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Conference IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      


## NotificationFriendIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Friend IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      


## NotificationGroupChatOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Group Chat Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      


## NotificationNearbyChatOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Nearby Chat Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      


## NotificationNonFriendIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Non Friend IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      


## NotificationObjectIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Object IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      


## NotificationTipToastLifeTime

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Number of seconds while a notification tip toast exist


## NotificationToastLifeTime

- Type: S32 | Default value: `30` | Persisted: 1

- Comment: Number of seconds while a notification toast exists


## NotifyMoneyChange

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pop up notifications for all L$ transactions


## NotifyMoneyReceived

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pop up notifications when receiving L$


## NotifyMoneySpend

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pop up notifications when spending L$


## NotifyTipDuration

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: Length of time that notification tips stay on screen (seconds)


## NumSessions

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Number of successful logins to Second Life


## NvAPICreateApplicationProfile

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Create NVIDIA application profile for optimized settings


## ObjectCacheEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable the object cache.


## ObjectCostHighColor

- Type: Color4 | Default value: `1.0 0.0 0.0 0.75` | Persisted: 1

- Comment: Color for object a high object cost.


## ObjectCostHighThreshold

- Type: F32 | Default value: `50.0` | Persisted: 1

- Comment: Threshold at which object cost is considered high (displayed in red).


## ObjectCostLowColor

- Type: Color4 | Default value: `0.0 0.5 1.0 0.5` | Persisted: 1

- Comment: Color for object with a low object cost.


## ObjectCostMidColor

- Type: Color4 | Default value: `1.0 0.75 0.0 0.65` | Persisted: 1

- Comment: Color for object with a medium object cost.


## ObjectInspectorTooltipDelay

- Type: F32 | Default value: `0.35` | Persisted: 1

- Comment: Seconds before displaying object inspector tooltip


## ObjectsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created object


## ObjectsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created objects can be copied by next owner


## ObjectsNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created objects can be modified by next owner


## ObjectsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created objects can be resold or given away by next owner


## ObjectsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created objects are shared with the currently active group


## ObscureBalanceInStatusBar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, balance will be shows as '*' (UNUSED)


## OctreeAlphaDistanceFactor

- Type: Vector3 | Default value: `0.1 0.0 64.0` | Persisted: 1

- Comment: Multiplier on alpha object distance for determining octree node size.  First two parameters are currently unused.  Third parameter is distance at which to perform detailed alpha sorting.


## OctreeAttachmentSizeFactor

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: Multiplier on attachment size for determining octree node size 


## OctreeDistanceFactor

- Type: Vector3 | Default value: `0.25 0.0 0.0` | Persisted: 1

- Comment: Multiplier on distance for determining octree node size 


## OctreeMaxNodeCapacity

- Type: U32 | Default value: `128` | Persisted: 1

- Comment: Maximum number of elements to store in a single octree node


## OctreeMinimumNodeSize

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Minimum size of any octree node


## OctreeStaticObjectSizeFactor

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Multiplier on static object size for determining octree node size 


## OmnifilterControls

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, Firestorm will show the omnifilter controls (enable, drop down) in upper right corner of the screen. Useful, if multiple omnifilter rule sets are being used.


## OmnifilterEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: The operating state of the Omnifilter.


## OmnifilterRuleSetID

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: The id of the current rule set for the Omnifilter.


## OnlineOfflinetoNearbyChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Send online/offline notifications to Nearby Chat panel (v1-style behavior)


## OnlineOfflinetoNearbyChatHistory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show online/offline notifications only in chat transcript


## OnlyShowSelectedNormals

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Only render the normals for selected objects. in conjunction with render debug normals


## OpenDebugStatAdvanced

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Advanced performance stats display


## OpenDebugStatBasic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Basic performance stats display


## OpenDebugStatMaterials

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Materials performance stats display


## OpenDebugStatNet

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Network performance stats display


## OpenDebugStatPathfinding

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Pathfinding performance stats display


## OpenDebugStatPhysicsDetails

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Physics Details performance stats display


## OpenDebugStatRender

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Render performance stats display


## OpenDebugStatSim

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Simulator performance stats display


## OpenDebugStatSimTime

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Simulator Time performance stats display


## OpenDebugStatSimTimeDetails

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Simulator Time Details performance stats display


## OpenDebugStatTexture

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Texture performance stats display


## OpenDebugStatVoice

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Voice (WebRTC) stats display


## OpenDebugStatVoiceIncoming

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Incoming audio (Voice) stats display


## OpenDebugStatVoiceOutgoing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Outgoing audio (Voice) stats display


## OpenIMOnVoice

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Open the corresponding IM window when connecting to a voice call.


## OpenRegionSettingsEnableDrawDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Obey the forced max draw distance setting in aurora-sim


## OpenSidePanelsInFloaters

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, will always open side panel contents in a floater.


## OutBandwidth

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Outgoing bandwidth throttle (bps)


## OutfitGallerySortOrder

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Gallery sorting: 0 - sort outfits by name, 1 - images frst, 2 - favorites first


## OutfitListFilterFullList

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment:  0 - show only matches. 1 - show all items in outfit as long as outfit or item inside matches.


## OutfitListSortOrder

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: How outfit list in Avatar's floater is sorted. 0 - by name 1 - favorites to top (unused in favour of FSOutfitListSortOrder)


## OutfitOperationsTimeout

- Type: S32 | Default value: `180` | Persisted: 1

- Comment: Timeout for outfit related operations.


## OverflowToastHeight

- Type: S32 | Default value: `72` | Persisted: 1

- Comment: Height of an overflow toast


## OverlayTitle

- Type: String | Default value: `Set_via_OverlayTitle_in_settings.xml` | Persisted: 1

- Comment: Controls watermark text message displayed on screen when "ShowOverlayTitle" is enabled (one word, underscores become spaces)


## OverridePieColors

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Override the pie menu color defined by the currently selected skin


## PTTCurrentlyEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Use Push to Talk mode


## PacketDropPercentage

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Percentage of packets dropped by the client.


## ParcelMediaAutoPlayEnable

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Auto play parcel media when available. 0 - Do not autoplay; 1- Autoplay; (2 - Ask; not supported)


## ParticipantListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide people icons in participant list


## PathfindingAmbiance

- Type: F32 | Default value: `0.5` | Persisted: 0

- Comment: Ambiance of lit pathfinding navmesh displays.


## PathfindingBoundaryEdge

- Type: Color4 | Default value: `1.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Color of a boundary (non-crossable) edge when displaying pathfinding navmesh.


## PathfindingConnectedEdge

- Type: Color4 | Default value: `0.86 0.86 0.86 1.0` | Persisted: 0

- Comment: Color of a connected (crossable) edge when displaying pathfinding navmesh.


## PathfindingExclusion

- Type: Color4 | Default value: `1.0 1.0 0.0 0.3` | Persisted: 0

- Comment: Color of exclusion volumes when displaying pathfinding navmesh object types.


## PathfindingFaceColor

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 0

- Comment: Color of the faces when displaying the default view of the pathfinding navmesh.


## PathfindingHeatColorBase

- Type: Color4 | Default value: `1.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Color of the least walkable value when displaying the pathfinding navmesh as a heatmap.


## PathfindingHeatColorMax

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 0

- Comment: Color of the most walkable value when displaying the pathfinding navmesh as a heatmap.


## PathfindingLineOffset

- Type: F32 | Default value: `2.3` | Persisted: 0

- Comment: Depth offset of volume outlines in pathfinding display.


## PathfindingLineWidth

- Type: F32 | Default value: `2.0` | Persisted: 0

- Comment: Width of volume outlines in pathfinding navmesh display.


## PathfindingMaterial

- Type: Color4 | Default value: `0.5 0.0 1.0 0.3` | Persisted: 0

- Comment: Color of material volumes when displaying pathfinding navmesh object types.


## PathfindingNavMeshClear

- Type: Color4 | Default value: `0.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Background color when displaying pathfinding navmesh.


## PathfindingObstacle

- Type: Color4 | Default value: `1.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Color of static obstacle objects when displaying pathfinding navmesh object types.


## PathfindingRetrieveNeighboringRegion

- Type: U32 | Default value: `99` | Persisted: 1

- Comment: Download a neighboring region when visualizing a pathfinding navmesh (default val 99 means do not download neighbors).


## PathfindingTestPathColor

- Type: Color4 | Default value: `1.0 0.59 0.0 0.9` | Persisted: 0

- Comment: Color of the pathfinding test-path when the path is valid.


## PathfindingTestPathInvalidEndColor

- Type: Color4 | Default value: `1.0 0.0 1.0 1.0` | Persisted: 0

- Comment: Color of the pathfinding test-pathing tool end-point when the path is invalid.


## PathfindingTestPathValidEndColor

- Type: Color4 | Default value: `0.78 0.47 0.0 1.0` | Persisted: 0

- Comment: Color of the pathfinding test-pathing tool end-point when the path is valid.


## PathfindingWalkable

- Type: Color4 | Default value: `0.45490196078431372549019607843137 0.93333333333333333333333333333333 0.38823529411764705882352941176471 1.0` | Persisted: 0

- Comment: Color of walkable objects when displaying pathfinding navmesh object types.


## PathfindingWaterColor

- Type: Color4 | Default value: `0.0 0.0 1.0 1.0` | Persisted: 0

- Comment: Color of water plane when displaying pathfinding navmesh.


## PathfindingXRayOpacity

- Type: F32 | Default value: `0.25` | Persisted: 0

- Comment: Opacity of xray lines in pathfinding display.


## PathfindingXRayTint

- Type: F32 | Default value: `0.8` | Persisted: 0

- Comment: Amount to darken/lighten x-ray lines in pathfinding display.


## PathfindingXRayWireframe

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Render pathfinding navmesh xray as a wireframe.


## PaymentMethodStagingURL

- Type: String | Default value: `https://secondlife-staging.com/my/lindex/buy.php?associate_for_viewer=1` | Persisted: 1

- Comment: URL for adding a payment method on the Damballah


## PaymentMethodURL

- Type: String | Default value: `https://secondlife.com/my/lindex/buy.php?associate_for_viewer=1` | Persisted: 1

- Comment: URL for adding a payment method


## PerAccountSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Persisted client settings file name (per user).


## PerfStatsCaptureEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable/disable render time data to support autotune.


## PermAllowScriptedMedia

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow scripts to control media


## PermissionsCautionEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: When enabled, changes the handling of script permission requests to help avoid accidental granting of certain permissions, such as the debit permission


## PermissionsCautionNotifyBoxHeight

- Type: S32 | Default value: `344` | Persisted: 0

- Comment: Height of caution-style notification messages


## PickerContextOpacity

- Type: F32 | Default value: `0.34999999404` | Persisted: 1

- Comment: Controls overall opacity of context frustrum connecting color and texture pickers with their swatches


## PicksPerSecondMouseMoving

- Type: F32 | Default value: `5.0` | Persisted: 1

- Comment: How often to perform hover picks while the mouse is moving (picks per second)


## PicksPerSecondMouseStationary

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: How often to perform hover picks while the mouse is stationary (picks per second)


## PieMenuFade

- Type: F32 | Default value: `0.3` | Persisted: 1

- Comment: Fade out for the pie menu background towards the edges


## PieMenuLineWidth

- Type: F32 | Default value: `2.5` | Persisted: 1

- Comment: Width of lines in pie menu display (pixels)


## PieMenuOpacity

- Type: F32 | Default value: `0.85` | Persisted: 1

- Comment: Opacity for the pie menu background


## PieMenuOuterRingShade

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, a shade around the outside of the pie menu will be drawn, adding a further visualization of sub menus.


## PieMenuPopupFontEffect

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If enabled, the labels in the pie menu slices are affected by the popup effect (they move into position).


## PingInterpolate

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Extrapolate object position along velocity vector based on ping delay


## PitchFromMousePosition

- Type: F32 | Default value: `90.0` | Persisted: 1

- Comment: Vertical range over which avatar head tracks mouse position (degrees of head rotation from top of window to bottom)


## PlainTextChatHistory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable/Disable plain text chat transcript style


## PlayChatAnim

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Your avatar plays the chat animation whenever you say, shout or whisper something in nearby chat


## PlayModeUISndAlert

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndAlert.


## PlayModeUISndBadKeystroke

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndBadKeystroke.


## PlayModeUISndChatMention

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndChatMention.


## PlayModeUISndClick

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndClick.


## PlayModeUISndClickRelease

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndClickRelease.


## PlayModeUISndFootsteps

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndFootsteps.


## PlayModeUISndFriendOffline

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndFriendOffline.


## PlayModeUISndFriendOnline

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndFriendOnline.


## PlayModeUISndFriendshipOffer

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndFriendshipOffer.


## PlayModeUISndGroupInvitation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndGroupInvitation.


## PlayModeUISndGroupNotice

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndGroupNotice.


## PlayModeUISndHealthReductionF

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndHealthReductionF.


## PlayModeUISndHealthReductionM

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndHealthReductionM.


## PlayModeUISndIncomingVoiceCall

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Plays a sound when have an incoming voice call. Holds state for Prefs > Sound/Media > UI Sounds - UISndIncomingVoiceCall.


## PlayModeUISndInvalidOp

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndInvalidOp.


## PlayModeUISndInventoryOffer

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndInventoryOffer.


## PlayModeUISndMicToggle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndMicToggle.


## PlayModeUISndMoneyChangeDown

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndMoneyChangeDown.


## PlayModeUISndMoneyChangeUp

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndMoneyChangeUp.


## PlayModeUISndMovelockToggle

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndMovelockToggle.


## PlayModeUISndNearbyChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndNearbyChat.


## PlayModeUISndNewIncomingConfIMSession

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndNewIncomingConfIMSession. 0 = Mute this sound, 1 = Play only on new session, 2 = Play on every message, 3 = Play only if not in focus. This setting is shared with Chat > Notifications > 'When receiving AdHoc Instant Messages'.


## PlayModeUISndNewIncomingGroupIMSession

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndNewIncomingGroupIMSession. 0 = Mute this sound, 1 = Play only on new session, 2 = Play on every message, 3 = Play only if not in focus.  This setting is shared with Chat > Notifications > 'When receiving Group Instant Messages'.


## PlayModeUISndNewIncomingIMSession

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndNewIncomingIMSession. 0 = Mute this sound, 1 = Play only on new session, 2 = Play on every message, 3 = Play only if not in focus.  This setting is shared with Chat > Notifications > 'When receiving Instant Messages'.


## PlayModeUISndObjectCreate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndObjectCreate.


## PlayModeUISndObjectDelete

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndObjectDelete.


## PlayModeUISndObjectRezIn

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndObjectRezIn.


## PlayModeUISndObjectRezOut

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndObjectRezOut.


## PlayModeUISndPieMenuAppear

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuAppear.


## PlayModeUISndPieMenuHide

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuHide.


## PlayModeUISndPieMenuSliceHighlight0

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight0.


## PlayModeUISndPieMenuSliceHighlight1

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight1.


## PlayModeUISndPieMenuSliceHighlight2

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight2.


## PlayModeUISndPieMenuSliceHighlight3

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight3.


## PlayModeUISndPieMenuSliceHighlight4

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight4.


## PlayModeUISndPieMenuSliceHighlight5

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight5.


## PlayModeUISndPieMenuSliceHighlight6

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight6.


## PlayModeUISndPieMenuSliceHighlight7

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndPieMenuSliceHighlight7.


## PlayModeUISndQuestionExperience

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndQuestionExperience.


## PlayModeUISndRadarAgeAlert

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled: plays the sound when the age alert for an avatar is triggered.


## PlayModeUISndRadarChatEnter

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled: plays the sound when avatars enter chat range. Also depends on RadarReportChatRangeEnter.


## PlayModeUISndRadarChatLeave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled: plays the sound when avatars leave chat range. Also depends on RadarReportChatRangeLeave.


## PlayModeUISndRadarDrawEnter

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled: plays the sound when avatars enter draw distance. Also depends on RadarReportDrawRangeEnter.


## PlayModeUISndRadarDrawLeave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled: plays the sound when avatars leave draw distance. Also depends on RadarReportDrawRangeLeave.


## PlayModeUISndRadarSimEnter

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled: plays the sound when avatars enter the region. Also depends on RadarReportSimRangeEnter.


## PlayModeUISndRadarSimLeave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled: plays the sound when avatars leave the region. Also depends on RadarReportSimRangeLeave.


## PlayModeUISndRestart

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndRestart.


## PlayModeUISndRestartOpenSim

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndRestartOpenSim.


## PlayModeUISndScriptFloaterClose

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndScriptFloaterClose.


## PlayModeUISndScriptFloaterOpen

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndScriptFloaterOpen.


## PlayModeUISndSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Take snapshots to disk without playing animation or sound. Originally QuietSnapshotsToDisk.


## PlayModeUISndStartIM

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndStartIM.


## PlayModeUISndTeleportOffer

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndTeleportOffer.


## PlayModeUISndTeleportOut

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndTeleportOut. Plays the whoosh teleport sound!


## PlayModeUISndTrackerBeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndTrackerBeacon.


## PlayModeUISndTyping

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Hear the typing sound when others type in to local chat. Originally FSPlayTypingSound.


## PlayModeUISndWindowClose

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndWindowClose.


## PlayModeUISndWindowOpen

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Holds state for Prefs > Sound/Media > UI Sounds - UISndWindowOpen.


## PlaySoundChatMention

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when got mentioned in a chat - UNUSED IN FS - see PlayModeUISndChatMention


## PlaySoundConferenceIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when conference IM received.


## PlaySoundFriendIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when friend's IM received.


## PlaySoundGroupChatIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when group chat IM received.


## PlaySoundNearbyChatIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when nearby chat IM received.


## PlaySoundNonFriendIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when non-friend's IM received.


## PlaySoundObjectIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when IM fom an object received.


## PlayTypingAnim

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Your avatar plays the typing animation whenever you type in the chat bar


## PluginAttachDebuggerToPlugins

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, attach a debugger session to each plugin process as it's launched.


## PluginInstancesCPULimit

- Type: F32 | Default value: `0.9` | Persisted: 1

- Comment: Amount of total plugin CPU usage before inworld plugins start getting turned down to "slideshow" priority.  Set to 0 to disable this check.


## PluginInstancesLow

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Limit on the number of inworld media plugins that will run at "low" priority


## PluginInstancesNormal

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Limit on the number of inworld media plugins that will run at "normal" or higher priority


## PluginInstancesTotal

- Type: U32 | Default value: `8` | Persisted: 1

- Comment: Hard limit on the number of plugins that will be instantiated at once for inworld media


## PluginUseReadThread

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use a separate thread to read incoming messages from plugins


## PoolSizeAIS

- Type: U32 | Default value: `20` | Persisted: ?

- Comment: Coroutine Pool size for AIS


## PoolSizeAssetStorage

- Type: U32 | Default value: `12` | Persisted: ?

- Comment: Coroutine Pool size for AssetStorage requests


## PoolSizeUpload

- Type: U32 | Default value: `1` | Persisted: ?

- Comment: Coroutine Pool size for Upload


## PostFirstLoginIntroURL

- Type: String | Default value: `` | Persisted: 1

- Comment: URL of intro presentation after first time users first login


## PostFirstLoginIntroViewed

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flag indicating if user has seen intro presentation after first time users first login


## PrecachingDelay

- Type: F32 | Default value: `6.0` | Persisted: 1

- Comment: Delay when logging in to load world before showing it (seconds)


## PreferredBrowserBehavior

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Use system browser for any links (0), use builtin browser for SL links and system one for others (1) or use builtin browser only (2).


## PreferredMaturity

- Type: U32 | Default value: `13` | Persisted: 1

- Comment: Setting for the user's preferred maturity level (consts in indra_constants.h)


## PresetCameraActive

- Type: String | Default value: `Rear View` | Persisted: 1

- Comment: Name of currently selected preference


## PresetGraphicActive

- Type: String | Default value: `` | Persisted: 1

- Comment: Name of currently selected preference


## PreviewAmbientColor

- Type: Color4 | Default value: `0.3 0.3 0.3 1.0` | Persisted: 1

- Comment: Ambient color of preview render.


## PreviewDiffuse0

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffuse color of preview light 0.


## PreviewDiffuse1

- Type: Color4 | Default value: `0.25 0.25 0.25 1.0` | Persisted: 1

- Comment: Diffuse color of preview light 1.


## PreviewDiffuse2

- Type: Color4 | Default value: `0.33 0.33 0.33 1.0` | Persisted: 1

- Comment: Diffuse color of preview light 2.


## PreviewDirection0

- Type: Vector3 | Default value: `-0.75 1 1.0` | Persisted: 1

- Comment: Direction of light 0 for preview render.


## PreviewDirection1

- Type: Vector3 | Default value: `0.5 -0.6 0.4` | Persisted: 1

- Comment: Direction of light 1 for preview render.


## PreviewDirection2

- Type: Vector3 | Default value: `0.5 -0.8 0.3` | Persisted: 1

- Comment: Direction of light 2 for preview render.


## PreviewRenderSize

- Type: S32 | Default value: `2048` | Persisted: 1

- Comment: Resolution of the image rendered for the mesh upload preview (must be a power of 2)


## PreviewSpecular0

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffuse color of preview light 0.


## PreviewSpecular1

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffuse color of preview light 1.


## PreviewSpecular2

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffuse color of preview light 2.


## PreviousInstallChecked

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether viewer checked previous install on the same channel for NSIS


## PrimMediaControlsUseHoverControlSet

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not hovering over prim media uses minimal "hover" controls or the authored control set.


## PrimMediaDragNDrop

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable drag and drop of URLs onto prim faces


## PrimMediaMasterEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not Media on a Prim is enabled.


## PrimMediaMaxRetries

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Maximum number of retries for media queries.


## PrimMediaMaxRoundRobinQueueSize

- Type: U32 | Default value: `100000` | Persisted: 1

- Comment: Maximum number of objects the viewer will continuously update media for


## PrimMediaMaxSortedQueueSize

- Type: U32 | Default value: `100000` | Persisted: 1

- Comment: Maximum number of objects the viewer will load media for initially


## PrimMediaRequestQueueDelay

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Timer delay for fetching media from the queue (in seconds).


## PrimMediaRetryTimerDelay

- Type: F32 | Default value: `5.0` | Persisted: 1

- Comment: Timer delay for retrying on media queries (in seconds).


## PrimTextMaxDrawDistance

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Maximum draw distance beyond which PRIM_TEXT won't be rendered


## PrivacyPolicyURL

- Type: String | Default value: `https://lindenlab.com/privacy` | Persisted: 1

- Comment: URL pointing to Privacy Policy page


## PrivateLocalLookAtTarget

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, your avatar's lookat target will not affect your local display. Head/Eye movement that normally would follow a lookat target will not be shown to you.


## PrivateLookAtTarget

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, viewer shows simulated look-at behavior to others.


## PrivatePointAtTarget

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, viewer won't show the editing arm motion.


## ProbeHardwareOnStartup

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Query current hardware configuration on application startup


## ProfilingActive

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: notes whether profiling is currently active. Used by the dev menu item


## PurgeCacheOnNextStartup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clear local file cache next time viewer is run


## PurgeCacheOnStartup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clear local file cache every time viewer is run


## PurgeDiskCacheOnStartup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to LRU purge the disk cache during startup on main thread


## PushToTalkButton

- Type: String | Default value: `MiddleMouse` | Persisted: 1

- Comment: (Obsolete)Which button or keyboard key is used for push-to-talk


## PushToTalkToggle

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Should the push-to-talk toolbar button behave as a toggle


## QAMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable Testing Features.


## QAModeEventHostPort

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: (Deprecated) Port on which lleventhost should listen


## QAModeFakeSystemFolderIssues

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Simulates system folder issues in inventory


## QAModeMetrics

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables QA features (logging, faster cycling) for metrics collector


## QAModeTermCode

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: On LL_ERRS, terminate with this code instead of OS message box


## QuickBuyCurrency

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Use BuyCurrencyHTML instead


## QuickPrefsEditMode

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Internal, volatile control that defines if the quickprefs floater is in edit mode.


## QuickPrefsSelectedControl

- Type: String | Default value: `` | Persisted: 0

- Comment: Internal, volatile control that holds the currently selected control. Used for enabling/disabling editor widgets.


## QuitAfterSeconds

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: The duration allowed before quitting.


## QuitAfterSecondsOfAFK

- Type: F32 | Default value: `0` | Persisted: 1

- Comment: The duration allowed after being AFK before quitting.


## QuitOnLoginActivated

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Quit if login page is activated (used when auto login is on and users must not be able to login manually)


## RLVaBlockedExperiences

- Type: String | Default value: `bfe25fb4-222c-11e5-85a2-fa4c4ccaa202` | Persisted: 1

- Comment: List of experiences blocked from interacting with RLVa


## RLVaCompatibilityModeList

- Type: String | Default value: `` | Persisted: 1

- Comment: Contains a list of creators or partial items names that require compatibility mode handling (see wiki for more information and syntax)


## RLVaDebugDeprecateExplicitPoint

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore attachment point names on inventory items and categories (incomplete)


## RLVaDebugHideUnsetDuplicate

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Suppresses reporting "unset" or "duplicate" command restrictions when RestrainedLoveDebug is TRUE


## RLVaEnableCompositeFolders

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables composite folders for shared inventory


## RLVaEnableIMQuery

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables a limited number of configuration queries via IM (e.g. @version)


## RLVaEnableLegacyNaming

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables legacy naming convention for folders


## RLVaEnableSharedWear

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Attachments in the shared #RLV folder can be force-attached without needing to specify an attachment point


## RLVaEnableTemporaryAttachments

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allows temporary attachments (regardless of origin) to issue RLV commands


## RLVaExperienceMaturityThreshold

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Specifies the minimum maturity an experience has to be before it can interact with RLVa (0: never; 1: PG; 2: Mature; 3: Adult)


## RLVaExperimentalCommands

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the experimental command set


## RLVaHideLockedAttachments

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hides non-detachable worn attachments from @getattach


## RLVaHideLockedLayers

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hides "remove outfit" restricted worn clothing layers from @getoufit


## RLVaSharedInvAutoRename

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically renames shared inventory items when worn


## RLVaShowAssertionFailures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Notify the user when an assertion fails


## RLVaShowRedirectChatTyping

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sends typing start messages (and optionally plays the typing animation) when @redirchat restricted


## RLVaSplitRedirectChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Splits long nearby chat lines across multiple messages when @redir* restricted


## RLVaTopLevelMenu

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the RLVa specific menu as a top level menu


## RLVaWearReplaceUnlocked

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Don't block wear replace when at least one attachment on the target attachment point is non-detachable


## RadarAlertChannel

- Type: S32 | Default value: `-777777777` | Persisted: 1

- Comment: Channel for whispering radar alerts


## RadarAvatarAgeAlert

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles whether radar sends out chat alerts when it detects an avatar younger than a pre-defined age


## RadarAvatarAgeAlertValue

- Type: S32 | Default value: `7` | Persisted: 1

- Comment: Defines how old an avatar may be at maximum for the age alert to get triggered


## RadarEnterChannelAlert

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles whether radar sends out chat alerts when it detects a new avatar


## RadarLeaveChannelAlert

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles whether radar sends out chat alerts when it detects an avatar has left


## RadarLegacyChannelAlertRefreshUUID

- Type: String | Default value: `76c78607-93f9-f55a-5238-e19b1a181389` | Persisted: 1

- Comment: UUID of sound asset that when detected, will request a full radar channel alert update


## RadarNameFormat

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: 0=DisplayName,1=Username,2=Displayname/Username,3=Username/Displayname


## RadarReportChatRangeEnter

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display a chat message when avatar enters chat distance


## RadarReportChatRangeLeave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display a chat message when avatar leaves chat distance


## RadarReportDrawRangeEnter

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display a chat message when avatar enters draw distance


## RadarReportDrawRangeLeave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display a chat message when avatar leaves draw distance


## RadarReportSimRangeEnter

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display a chat message when avatar enteres local region


## RadarReportSimRangeLeave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display a chat message when avatar leaves local region


## RadioLandBrushAction

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected land modification operation (0 = flatten, 1 = raise, 2 = lower, 3 = smooth, 4 = roughen, 5 = revert)


## RealisticMouselook

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Make the camera follow avatar body movements and animations while in mouselook


## RecentItemsSortOrder

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Specifies sort key for recent inventory items (+0 = name, +1 = date, +2 = folders always by name, +4 = system folders to top)


## RecentJumpThresholdSecs

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Seconds after jump input during which landing finish-anim is suppressed to avoid interrupting rapid successive jumps.


## RecentListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide people icons in recent list


## RecentPeopleSortOrder

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Specifies sort order for recent people (0 = by name, 2 = by most recent)


## RectangleSelectInclusive

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Select objects that have at least one vertex inside selection rectangle


## RegInClient

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Experimental: Embed registration in login screen


## RegionCheckTextureHeights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Don't allow user to set low heights greater than high


## RegionCrossingInterpolationTime

- Type: F32 | Default value: `1` | Persisted: 1

- Comment: How long to extrapolate object motion after crossing regions


## RegionTextureSize

- Type: U32 | Default value: `256` | Persisted: 1

- Comment: Terrain texture dimensions (power of 2)


## RelockMoveLockAfterRegionChange

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: TRUE: Re-lock movelock after region change - refresh avatar position and send to LSL-Client Bridge script. FALSE: Disengage the lock automatically after region change.


## RememberPassword

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep password (in encrypted form) for next login


## RememberUser

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep user name for next login


## RenderAnimateRes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Obsolete) Does nothing Animate rezing prims.


## RenderAnisotropic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [OBSOLETE] Render textures using anisotropic filtering


## RenderAnisotropicLevel

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Anisotropic filtering strength(0(Disable), 2x, 4x, 8x, 16x


## RenderAppleUseMultGL

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether we want to use multi-threaded OpenGL on Apple hardware (requires restart of SL).


## RenderAttachedLights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render lighted prims that are attached to avatars


## RenderAttachedParticles

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render particle systems that are attached to avatars


## RenderAutoHideSurfaceAreaLimit

- Type: F32 | Default value: `10.0E6` | Persisted: 1

- Comment: Maximum surface area of a set of proximal objects inworld before automatically hiding geometry to prevent system overload.


## RenderAutoMaskAlphaDeferred

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use alpha masks where appropriate in the Advanced Lighting Model


## RenderAutoMaskAlphaNonDeferred

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use alpha masks where appropriate when not using the Advanced Lighting Model


## RenderAutoMuteLogging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show extra information in viewer logs about avatar rendering costs


## RenderAutoMuteRenderWeightLimit

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: OBSOLETE. This setting has been renamed RenderAvatarMaxNonImpostors.


## RenderAutoMuteSurfaceAreaLimit

- Type: F32 | Default value: `1000.0` | Persisted: 1

- Comment: Maximum surface area of attachments before an avatar is
    rendered as a simple impostor (to not use this limit, set to zero
    or set RenderAvatarMaxComplexity to zero).


## RenderAvatarCloth

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Controls if system avatar clothes use wavy cloth


## RenderAvatarComplexityMode

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: 0 - complexity limit applies to everyone, 1 - always show friends, 2 - only show friends


## RenderAvatarFriendsOnly

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: When enabled hides all avatars that aren't friends. Does not affect inworld control avatars (animeshes), nor self.


## RenderAvatarLODFactor

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Controls level of detail of avatars (multiplier for current screen area when calculated level of detail)


## RenderAvatarMaxART

- Type: F32 | Default value: `4.699` | Persisted: 0

- Comment: Render Time Limit in microseconds (0.0 = no limit)


## RenderAvatarMaxComplexity

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Maximum Avatar Complexity; above this value, the avatar is
    rendered as a solid color outline (0 to disable this limit).


## RenderAvatarMaxNonImpostors

- Type: U32 | Default value: `12` | Persisted: 1

- Comment: Maximum number of avatars to fully render at one time;
    over this limit uses impostor rendering (simplified rendering
    with less frequent updates), reducing client lag.


## RenderAvatarMaxVisible

- Type: S32 | Default value: `0` | Persisted: 0

- Comment: OBSOLETE and UNUSED. See RenderAvatarMaxNonImpostors


## RenderAvatarPhysicsLODFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Controls level of detail of avatar physics (such as breast physics).


## RenderBakeSunlight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bake sunlight into vertex buffers for static objects.


## RenderBalanceInSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display L$ balance in snapshot


## RenderBufferVisualization

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: Outputs a selected buffer to the screen.  -1 = final render buffer.  0 = Albedo, 1 = Specular/ORM, 2 = Normal, 3 = Emissive, 4 = Eye luminance, 5 = FXAA Luminance/SMAA Edge Tex, 6 = SMAA Blend Weights


## RenderBumpmapMinDistanceSquared

- Type: F32 | Default value: `100.0` | Persisted: 1

- Comment: Maximum distance at which to render bumpmapped primitives (distance in meters, squared)


## RenderCASSharpness

- Type: F32 | Default value: `0.4` | Persisted: 1

- Comment: Level of sharpening to apply via Contrast Adaptive Sharpening (0.0(off) - 1.0)


## RenderCPUBasis

- Type: F32 | Default value: `3000.0` | Persisted: 1

- Comment: Reference CPU clockspeed to use to bias GPU class (in MHz).


## RenderCanUseGLTFPBROpaqueShaders

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Hardware has support for GLTF scene shaders


## RenderCanUseTerrainBakeShaders

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Hardware has support for Terrain Bake shaders


## RenderClass1MemoryBandwidth

- Type: F32 | Default value: `48.0` | Persisted: 1

- Comment: Memory bandwidth at which to default to Class 1 in gigabytes per second.  Used as basis for higher classes.


## RenderComplexityColorMax

- Type: Color4 | Default value: `1.0 0.0 0.0 0.5` | Persisted: 1

- Comment: Unused obsolete setting


## RenderComplexityColorMid

- Type: Color4 | Default value: `0.0 1.0 0.0 0.5` | Persisted: 1

- Comment: Unused obsolete setting


## RenderComplexityColorMin

- Type: Color4 | Default value: `0.0 0.0 1.0 0.5` | Persisted: 1

- Comment: Unused obsolete setting


## RenderComplexityStaticMax

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Unused obsolete setting


## RenderComplexityThreshold

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Unused obsolete setting


## RenderCompressTextures

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable texture compression on OpenGL 3.0 and later implementations (EXPERIMENTAL, requires restart)


## RenderCubeMap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether we can render the cube map or not


## RenderDebugAlphaMask

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Test Alpha Masking Cutoffs.


## RenderDebugGLSession

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enable strict GL debugging on the start of next session.


## RenderDebugNormalScale

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Scale of normals in debug display.


## RenderDebugPipeline

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enable strict pipeline debugging.


## RenderDebugSH

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable SH indirect lighting visualization.


## RenderDebugTextureBind

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable texture bind performance test.


## RenderDefaultProbeUpdatePeriod

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: When RenderReflectionProbeLevel is 0, amount of time in seconds to wait between updates to reflection map.


## RenderDeferred

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: DEPRECATED (only true supported) - Use deferred rendering pipeline (Advanced Lighting Model).


## RenderDeferredAlphaSoften

- Type: F32 | Default value: `0.75` | Persisted: 1

- Comment: Scalar for softening alpha surfaces (for soft particles).


## RenderDeferredAtmospheric

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute atmospheric shader in deferred renderer.


## RenderDeferredBlurLight

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute shadow softening shader in deferred renderer.


## RenderDeferredDisplayGamma

- Type: F32 | Default value: `2.2` | Persisted: 1

- Comment: Gamma ramp exponent for final correction before display gamma.


## RenderDeferredNoise

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: Noise scalar to hide banding in deferred render.


## RenderDeferredSSAO

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute screen space ambient occlusion shader in deferred renderer.


## RenderDeferredSpotShadowBias

- Type: F32 | Default value: `-64.0` | Persisted: 1

- Comment: Bias value for spot shadows (prevent shadow acne).


## RenderDeferredSpotShadowOffset

- Type: F32 | Default value: `0.8` | Persisted: 1

- Comment: Offset value for spot shadows (prevent shadow acne).


## RenderDeferredSun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute sunlight shader in deferred renderer.


## RenderDeferredSunWash

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Amount local lights are washed out by sun.


## RenderDeferredTreeShadowBias

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Bias value for tree shadows (prevent shadow acne).


## RenderDeferredTreeShadowOffset

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Offset value for tree shadows (prevent shadow acne).


## RenderDelayCreation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Throttle creation of drawables.


## RenderDepthOfField

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to use depth of field effect when Advanced Lighting Model is enabled


## RenderDepthOfFieldInEditMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to use depth of field effect when in edit mode


## RenderDepthPrePass

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: EXPERIMENTAL: Prime the depth buffer with simple prim geometry before rendering with textures.


## RenderDesaturateIrradiance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Desaturate irradiance to remove blue tint


## RenderDiffuseLuminanceScale

- Type: F32 | Default value: `0.5` | Persisted: 0

- Comment: Luminance adjustment for diffuse surfaces to aid auto-exposure behavior


## RenderDisablePostProcessing

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disable tone mapping and exposure correction when build floater is open (for artists developing materials)


## RenderDisableVintageMode

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables additional rendering pipeline features on newer machines such as HDR and emissive textures on PBR content.


## RenderDownScaleMethod

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Method to use to downscale images.  0 - FBO, 1 - PBO


## RenderDynamicExposureCoefficient

- Type: F32 | Default value: `0.5` | Persisted: 0

- Comment: Luminance coefficient for dynamic exposure


## RenderDynamicLOD

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Dynamically adjust level of detail.


## RenderEdgeDepthCutoff

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Cutoff for depth difference that amounts to an edge.


## RenderEdgeNormCutoff

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Cutoff for normal difference that amounts to an edge.


## RenderEnableEmissiveBuffer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable emissive buffer in gbuffer.  Should only be disabled in GL3 mode.


## RenderExposure

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Exposure value to send to tonemapper.


## RenderFSAASamples

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Quality of antialiasing: 0 = Low, 1 = Medium, 2 = High, 3 = Ultra


## RenderFSAAType

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Type of Antialiasing to use: 0 = None, 1 = FXAA, 2 = SMAA


## RenderFarClip

- Type: F32 | Default value: `256.0` | Persisted: 1

- Comment: Distance of far clip plane from camera (meters)


## RenderFlexTimeFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Controls level of detail of flexible objects (multiplier for amount of time spent processing flex objects)


## RenderFogRatio

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: DEPRECATED - Distance from camera where fog reaches maximum density (fraction or multiple of far clip distance)


## RenderGLContextCoreProfile

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Don't use a compatibility profile OpenGL context.  Requires restart.


## RenderGLMultiThreadedMedia

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow OpenGL to use multiple render contexts for playing media (may reduce frame stutters, doesn't play nice with Intel drivers)


## RenderGLMultiThreadedTextures

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow OpenGL to use multiple render contexts for loading textures (may reduce frame stutters, doesn't play nice with Intel drivers).


## RenderGamma

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: DEPRECATED - Sets gamma exponent for renderer


## RenderGammaFull

- Type: Boolean | Default value: `1.0` | Persisted: 1

- Comment: Use fully controllable gamma correction, instead of faster, hard-coded gamma correction of 2.


## RenderGlow

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render bloom post effect.


## RenderGlowHDR

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable HDR for glow map


## RenderGlowIterations

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Number of times to iterate the glow (higher = wider and smoother but slower)


## RenderGlowLumWeights

- Type: Vector3 | Default value: `1.0 0.0 0.0` | Persisted: 1

- Comment: Weights for each color channel to be used in calculating luminance (should add up to 1.0)


## RenderGlowMaxExtractAlpha

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Max glow alpha value for brightness extraction to auto-glow.


## RenderGlowMinLuminance

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Min luminance intensity necessary to consider an object bright enough to automatically glow. (Gets clamped at 1.0)


## RenderGlowNoise

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables glow noise (dithering). Reduces banding from glow in certain cases.


## RenderGlowResolutionPow

- Type: S32 | Default value: `9` | Persisted: 1

- Comment: Glow map resolution power of two.


## RenderGlowStrength

- Type: F32 | Default value: `0.325` | Persisted: 1

- Comment: Additive strength of glow.


## RenderGlowWarmthAmount

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Amount of warmth extraction to use (versus luminance extraction). 0 = lum, 1.0 = warmth


## RenderGlowWarmthWeights

- Type: Vector3 | Default value: `1.0 0.5 0.7` | Persisted: 1

- Comment: Weight of each color channel used before finding the max warmth


## RenderGlowWidth

- Type: F32 | Default value: `1.3` | Persisted: 1

- Comment: Glow sample size (higher = wider and softer but eventually more pixelated)


## RenderHDREnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable HDR rendering.


## RenderHDRIExposure

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Exposure adjustment of HDRI when previewing an HDRI.  Units are EV.  Sane values would be -10 to 10.


## RenderHDRIIrradianceOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Only use HDRI sky for irradiance map when RenderHDRISplitScreen is 0


## RenderHDRIRotation

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rotation (in degrees) of environment when previewing an HDRI.


## RenderHDRISplitScreen

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: What percentage of screen to render using HDRI vs EEP sky.


## RenderHDRSkySunlightScale

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: Sunlight scale fudge factor for matching with pre-PBR viewer when HDR is enabled


## RenderHUDInSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display HUD attachments in snapshot


## RenderHUDObjectsWarning

- Type: U32 | Default value: `1000` | Persisted: 1

- Comment: Viewer will warn user about HUD containing to many objects if objects count is above this value


## RenderHUDOversizedTexturesWarning

- Type: U32 | Default value: `6` | Persisted: 1

- Comment: How many textures with size 1024 * 1024 or bigger HUD can contain before notifying user


## RenderHUDParticles

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display particle systems in HUD attachments (experimental)


## RenderHUDTexturesMemoryWarning

- Type: U32 | Default value: `32000000` | Persisted: 1

- Comment: Viewer will warn user about HUD textures using memory above this value (in bytes)


## RenderHUDTexturesWarning

- Type: U32 | Default value: `200` | Persisted: 1

- Comment: Viewer will warn user about HUD containing to many textures if texture count is above this value


## RenderHeroProbeConservativeUpdateMultiplier

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: How many probe updates to wait until it's time to update faces that are not directly facing the camera.  Acts as a multiplier.  E.g., frames to the periphery of the camera updating once every 3 updates, vs ones directly facing the camera updating every update.


## RenderHeroProbeDistance

- Type: F32 | Default value: `8` | Persisted: 1

- Comment: Distance in meters for hero probes to render out to.


## RenderHeroProbeResolution

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: Resolution to render hero probes used for mirrors, water, etc.


## RenderHeroProbeUpdateRate

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: How many frames to wait for until it's time to render the probe. E.g., every other frame (1), every two frames (2), every three frames (3) etc.


## RenderHiDPI

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable support for HiDPI displays, like Retina (macOS and Linux ONLY, requires restart)


## RenderHiddenSelections

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show selection lines on objects that are behind other objects


## RenderHideGroupTitle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Don't show my group title in my name label


## RenderHighMemMinDiscardDecrement

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Minimum decrement of discard bias if excess texture memory is available


## RenderHighPrecisionPostProcess

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use 16-bit floating point buffers for post process rendering


## RenderHighlightBrightness

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: Brightness of mouseover highlights.


## RenderHighlightColor

- Type: Color4 | Default value: `0.4 0.98 0.93 1.0` | Persisted: 1

- Comment: Brightness of mouseover highlights.


## RenderHighlightFadeTime

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Transition time for mouseover highlights.


## RenderHighlightSelections

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show selection outlines on objects


## RenderHighlightThickness

- Type: F32 | Default value: `0.6` | Persisted: 1

- Comment: Thickness of mouseover highlights.


## RenderHoverGlowEnable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: DEPRECATED --- Show glow effect when hovering on interactive objects.


## RenderInitError

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Error occured while initializing GL


## RenderJellyDollsAsImpostors

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use an impostor instead of a JellyDoll for better visuals (true)


## RenderLightRadius

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render the radius of selected lights


## RenderLocalLightCount

- Type: S32 | Default value: `256` | Persisted: 1

- Comment: Number of local lights to render.


## RenderLowMemMinDiscardIncrement

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Minimum increment of discard bias if available texture memory gets low


## RenderMaxNodeSize

- Type: S32 | Default value: `65536` | Persisted: 1

- Comment: Maximum size of a single node's vertex data (in KB).


## RenderMaxOpenGLVersion

- Type: F32 | Default value: `4.6` | Persisted: 1

- Comment: Maximum OpenGL version to attempt use (minimum 3.1 maximum 4.6).  Requires restart. Windows only.


## RenderMaxPartCount

- Type: S32 | Default value: `4096` | Persisted: 1

- Comment: Maximum number of particles to display on screen


## RenderMaxTextureIndex

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Maximum texture index to use for indexed texture rendering.


## RenderMaxTextureResolution

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: Maximum texture resolution to download for non-boosted textures.


## RenderMaxVBOSize

- Type: S32 | Default value: `4096` | Persisted: 1

- Comment: Maximum size of a vertex buffer (in KB).


## RenderMaxVRAMBudget

- Type: U32 | Default value: `768` | Persisted: 1

- Comment: Maximum amount of texture memory to budget for (in MB), or autodetect if FSLimitTextureVRAMUsage is disabled.


## RenderMinFreeCommitMemoryThresholdMB

- Type: U32 | Default value: `512` | Persisted: 0

- Comment: If available Windows commit memory is below this value textures get aggressively scaled down


## RenderMinFreeMainMemoryThreshold

- Type: U32 | Default value: `512` | Persisted: 0

- Comment: If available free physical memory is below this value textures get agresively scaled down


## RenderMinimumLODTriangleCount

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Triangle count threshold at which automatic LOD generation stops


## RenderMirrors

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Renders realtime mirrors.


## RenderNameFadeDuration

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Time interval over which to fade avatar names (seconds)


## RenderNameShowSelf

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display own name above avatar


## RenderNameShowTime

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Fade avatar names after specified time (seconds)


## RenderNoAlpha

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable rendering of alpha objects (render all alpha objects as alpha masks).


## RenderNormalMapScale

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Scaler applied to height map when generating normal maps


## RenderNsightDebugSupport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: 
      Disable features which prevent nVidia nSight from being usable with SL. Requires restart.
    


## RenderObjectBump

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: DEPRECATED (only TRUE supported) Show bumpmapping on primitives


## RenderOcclusionTimeout

- Type: U32 | Default value: `8` | Persisted: 1

- Comment: Maximum number of frames to wait on an occlusion query before forcibly reading it back


## RenderParcelSelection

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display selected parcel outline


## RenderPerformanceTest

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: 
                Disable rendering of everything but in-world content for
                performance testing



## RenderPreferStreamDraw

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use GL_STREAM_DRAW in place of GL_DYNAMIC_DRAW


## RenderQualityPerformance

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Which graphics settings you've chosen. Don't use this setting to change quality directly from debug settings.


## RenderReflectionDetail

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: DEPRECATED -- use RenderTransparentWater and RenderReflectionProbeDetail -- Detail of reflection render pass.


## RenderReflectionProbeAmbiance

- Type: F32 | Default value: `0` | Persisted: 1

- Comment: Amount reflection probes contribute to ambient light.


## RenderReflectionProbeCount

- Type: U32 | Default value: `256` | Persisted: 1

- Comment: Number of probes to render.  Maximum of 256.  Clamps to the nearest power of 2.


## RenderReflectionProbeDetail

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Detail of reflections. (-1 - Disabled, 0 - Static Only, 1 - Static + Dynamic, 2 - Realtime)


## RenderReflectionProbeDrawDistance

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Camera far clip to use when updating reflection probes.


## RenderReflectionProbeDynamicAllocation

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Enable dynamic allocation of reflection probes. -1 means no dynamic allocation. Sets a buffer to allocate when a dynamic allocation occurs otherwise.


## RenderReflectionProbeLevel

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Reflection probes control.  0 - disable (one probe to rule them all), 1 - manual probes only, 2 - manual + terrain/water, 3 - Manual + Terrain/water + objects.


## RenderReflectionProbeMaxLocalLightAmbiance

- Type: F32 | Default value: `4.0` | Persisted: 0

- Comment: Maximum effective probe ambiance for local lights


## RenderReflectionProbeResolution

- Type: U32 | Default value: `128` | Persisted: 1

- Comment: Resolution of reflection probe radiance maps (requires restart).  Will be set to the next highest power of two clamped to [64, 512].  Note that changing this value may consume a massive amount of video memory.


## RenderReflectionProbeShowTransparent

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Show reflection probes in the transparency debug view


## RenderReflectionProbeVolumes

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Render influence volumes of Reflection Probes


## RenderReflectionRes

- Type: S32 | Default value: `64` | Persisted: 1

- Comment: Reflection map resolution.


## RenderReflectionsEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable/disable reflection probes - Deprecated, disabling this removes all sky ambiance, use RenderReflectionProbeLevel=0 instead


## RenderReservedTextureIndices

- Type: S32 | Default value: `14` | Persisted: 1

- Comment: Count of texture indices to reserve for shadow and reflection maps when using indexed texture rendering.  Probably only want to set from the login screen.


## RenderResolutionDivisor

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Divisor for rendering 3D scene at reduced resolution.


## RenderResolutionMultiplier

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Multiplier for rendering 3D scene at reduced resolution. Valid values: 0 < RenderResolutionMultiplier <= 1.0 


## RenderSSAOEffect

- Type: Vector3 | Default value: `0.80 1.00 0.00` | Persisted: 1

- Comment: Multiplier for (1) value and (2) saturation (HSV definition), for areas which are totally occluded.  Blends with original color for partly-occluded areas.  (Third component is unused.)


## RenderSSAOFactor

- Type: F32 | Default value: `0.30` | Persisted: 1

- Comment: Occlusion sensitivity factor for ambient occlusion (larger is more)


## RenderSSAOIrradianceMax

- Type: F32 | Default value: `0.18` | Persisted: 0

- Comment: Max factor for irradiance input to SSAO


## RenderSSAOIrradianceScale

- Type: F32 | Default value: `0.6` | Persisted: 0

- Comment: Scaling factor for irradiance input to SSAO


## RenderSSAOMaxScale

- Type: U32 | Default value: `200` | Persisted: 1

- Comment: Maximum screen radius for sampling (pixels)


## RenderSSAOScale

- Type: F32 | Default value: `500.0` | Persisted: 1

- Comment: Scaling factor for the area to sample for occluders (pixels at 1 meter away, inversely varying with distance)


## RenderScreenSpaceReflectionAdaptiveStepMultiplier

- Type: F32 | Default value: `1.6` | Persisted: 1

- Comment: Multiplier to scale adaptive stepping.


## RenderScreenSpaceReflectionDepthRejectBias

- Type: F32 | Default value: `0.001` | Persisted: 1

- Comment: Bias against the depth buffer before rejecting a sample.


## RenderScreenSpaceReflectionDistanceBias

- Type: F32 | Default value: `0.015` | Persisted: 1

- Comment: Distance bias to apply when rejecting a potential sample.


## RenderScreenSpaceReflectionGlossySamples

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: Maximum number of samples to apply for glossy SSR.


## RenderScreenSpaceReflectionIterations

- Type: S32 | Default value: `25` | Persisted: 1

- Comment: Number of times the ray march algorithm runs to find a potential hit.


## RenderScreenSpaceReflectionRayStep

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: How big the step is between each run.


## RenderScreenSpaceReflections

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Renders screen space reflections to better account for dynamic objects with reflection probes.


## RenderSculptSAThreshold

- Type: F32 | Default value: `150.0` | Persisted: 1

- Comment: The surface area at which sculpts begin to be considered for being made invisible.


## RenderShaderCacheEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable binary shader cache


## RenderShaderCacheVersion

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 1

- Comment: Current version hash for shader cache


## RenderShaderLODThreshold

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Fraction of draw distance defining the switch to a different shader LOD


## RenderShaderLightingMaxLevel

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Max lighting level to use in the shader (class 3 is default, 2 is less lights, 1 is sun/moon only.  Works around shader compiler bugs on certain platforms.)


## RenderShaderParticleThreshold

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Fraction of draw distance to not use shader on particles


## RenderShadowBias

- Type: F32 | Default value: `-0.002` | Persisted: 1

- Comment: Bias value for shadows (prevent shadow acne).


## RenderShadowBiasError

- Type: F32 | Default value: `-0.007` | Persisted: 1

- Comment: Error scale for shadow bias (based on altitude).


## RenderShadowBlurDistFactor

- Type: F32 | Default value: `0` | Persisted: 1

- Comment: Distance scaler for shadow blur.


## RenderShadowBlurSamples

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Number of samples to take for each pass of shadow blur (value range 1-16).  Actual number of samples is value * 2 - 1.


## RenderShadowBlurSize

- Type: F32 | Default value: `1.4` | Persisted: 1

- Comment: Scale of shadow softening kernel.


## RenderShadowDetail

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Detail of shadows.


## RenderShadowErrorCutoff

- Type: F32 | Default value: `5.0` | Persisted: 1

- Comment: Cutoff error value to use ortho instead of perspective projection.


## RenderShadowFOVCutoff

- Type: F32 | Default value: `0.8` | Persisted: 1

- Comment: Cutoff FOV to use ortho instead of perspective projection.


## RenderShadowGaussian

- Type: Vector3 | Default value: `3.0 2.0 0.0` | Persisted: 1

- Comment: Gaussian coefficients for the two shadow/SSAO blurring passes (z component unused).


## RenderShadowNoise

- Type: F32 | Default value: `-0.0001` | Persisted: 1

- Comment: Magnitude of noise on shadow samples.


## RenderShadowOffset

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Offset value for shadows (prevent shadow acne).


## RenderShadowOffsetError

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Error scale for shadow offset (based on altitude).


## RenderShadowProjExponent

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Exponent applied to transition between ortho and perspective shadow projections based on viewing angle and light vector.


## RenderShadowProjOffset

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Amount to scale distance to virtual origin of shadow perspective projection.


## RenderShadowResolutionScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of shadow map resolution vs. screen resolution (only positivie values are allowed)


## RenderShadowSlopeThreshold

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Cutoff slope value for points to affect perspective shadow generation


## RenderShadowSplitExponent

- Type: Vector3 | Default value: `3.0 3.0 2.0` | Persisted: 1

- Comment: Near clip plane split distances for shadow map frusta (x=perspective, y=ortho, z=transition rate).


## RenderShadowSplits

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Amount of shadow map splits to render (0 - 3).


## RenderSkyAmbientScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Ambient scale fudge factor for matching with pre-PBR viewer


## RenderSkyAutoAdjustAmbientScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Amount to scale ambient when auto-adjusting legacy skies


## RenderSkyAutoAdjustBlueDensityScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Blue Horizon Scale value to use when auto-adjusting legacy skies


## RenderSkyAutoAdjustBlueHorizonScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Blue Horizon Scale value to use when auto-adjusting legacy skies


## RenderSkyAutoAdjustHDRScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: HDR Scale value to use when auto-adjusting legacy skies


## RenderSkyAutoAdjustLegacy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, automatically adjust legacy skies (those without a probe ambiance value) to take advantage of probes and HDR.  This is the "opt-out" button for HDR and tonemapping when coupled with a sky setting that predates PBR.


## RenderSkyAutoAdjustProbeAmbiance

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Probe ambiance value when auto-adjusting legacy skies


## RenderSkyAutoAdjustSunColorScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Sun color scalar when auto-adjusting legacy skies


## RenderSkySunlightScale

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: Sunlight scale fudge factor for matching with pre-PBR viewer when HDR is disabled


## RenderSnapshotNoPost

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable tone mapping and exposure correction when snapshot is being rendered


## RenderSpecularExponent

- Type: F32 | Default value: `368.0` | Persisted: 1

- Comment: Specular exponent for generating spec map


## RenderSpecularPrecision

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Force 32-bit floating point LUT


## RenderSpecularResX

- Type: U32 | Default value: `1024` | Persisted: 1

- Comment: Spec map resolution.


## RenderSpecularResY

- Type: U32 | Default value: `256` | Persisted: 1

- Comment: Spec map resolution.


## RenderSpotLightsInNondeferred

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to support projectors as spotlights when Advanced Lighting Model is disabled


## RenderSpotShadowBias

- Type: F32 | Default value: `-0.0002` | Persisted: 1

- Comment: Bias value for shadows (prevent shadow acne).


## RenderSpotShadowOffset

- Type: F32 | Default value: `0.04` | Persisted: 1

- Comment: Offset value for shadows (prevent shadow acne).


## RenderSunDynamicRange

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Defines what percent brighter the sun is than local point lights (1.0 = 100% brighter. Value should not be less than 0. ).


## RenderTerrainDetail

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Detail applied to terrain texturing (0 = none, 1 = full)


## RenderTerrainLODFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Controls level of detail of terrain (multiplier for current screen area when calculated level of detail)


## RenderTerrainPBRDetail

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Detail level for PBR terrain. 0 is full detail. Negative values drop rendering features, in accordance with the GLTF specification when possible, which reduces the number of texture binds.


## RenderTerrainPBREnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable PBR Terrain features.


## RenderTerrainPBRNormalsEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: EXPERIMENTAL: Change normal gen for PBR Terrain.


## RenderTerrainPBRPlanarSampleCount

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: How many UV planes to sample PBR terrain textures from. 1 is "flat", 3 is triplanar mapping (aka box mapping)


## RenderTerrainPBRScale

- Type: F32 | Default value: `8.0` | Persisted: 1

- Comment: PBR terrain detail texture scale (meters)


## RenderTerrainPBRTransformsEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: EXPERIMENTAL: Enable PBR Terrain texture transforms.


## RenderTerrainPBRTriplanarBlendFactor

- Type: F32 | Default value: `8.0` | Persisted: 1

- Comment: Higher values create sharper transitions, but are more likely to produce artifacts.


## RenderTerrainScale

- Type: F32 | Default value: `12.0` | Persisted: 1

- Comment: Terrain detail texture scale (meters)


## RenderTextureVRAMDivisor

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Divisor for maximum amount of VRAM the viewer will use for textures. 1 = all the VRAM.  Used in conjunction with RenderMaxVRAMBudget.


## RenderTonemapMix

- Type: F32 | Default value: `0.7` | Persisted: 1

- Comment: Mix between linear and tonemapped colors (0.0(Linear) - 1.0(Tonemapped)


## RenderTonemapType

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: What tonemapper to use: 0 = Khronos Neutral, 1 = ACES


## RenderTrackerBeacon

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display tracking arrow and beacon to target avatar, teleport destination


## RenderTransparentWater

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render water as transparent.  Setting to false renders water as opaque with a simple texture applied.


## RenderTreeLODFactor

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Controls level of detail of vegetation (multiplier for current screen area when calculated level of detail)


## RenderUIBuffer

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Cache ui render in a screen aligned buffer.


## RenderUIInSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display user interface in snapshot


## RenderUnloadedAvatar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show avatars which haven't finished loading


## RenderUseAdvancedAtmospherics

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use fancy precomputed atmospherics and stuff.


## RenderUseExposureSkySettings

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Use exposure sky settings instead of deriving from HDR scale.


## RenderUseFarClip

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If false, frustum culling will ignore far clip plane.


## RenderUseStreamVBO

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use VBO's for stream buffers


## RenderUseTriStrips

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: DEPRECATED - now always assumed to be false - Use triangle strips for rendering prims.


## RenderUseVAO

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [EXPERIMENTAL] Use GL Vertex Array Objects.


## RenderVBOEnable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use GL Vertex Buffer Objects


## RenderVBOMappingDisable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Disable VBO glMapBufferARB


## RenderVSyncEnable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Update frames between display scans (FALSE = Update frames as fast as possible).


## RenderVolumeLODFactor

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Influences the distance at which the viewer will display a lower detail model. Higher values = more lag. IMPORTANT: Please disregard advice to increase this value, such as is commonly distributed in notecards.


## RenderVolumeSAFrameMax

- Type: F32 | Default value: `5000.0` | Persisted: 1

- Comment: The limit(per frame) at which the sum of all volumes above the surface area threshold that causes all further sculpts/volumes above the threshold to stop being drawn..


## RenderVolumeSAProtection

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables automatic derendering of prims with high surface area (can protect against some video card crashers)


## RenderVolumeSAThreshold

- Type: F32 | Default value: `75.0` | Persisted: 1

- Comment: The surface area at which volumes begin to be considered for being made invisible.


## RenderWater

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display water


## RenderWaterMaterials

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Water planar reflections include materials rendering.


## RenderWaterMipNormal

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use mip maps for water normal map.


## RenderWaterRefResolution

- Type: S32 | Default value: `512` | Persisted: 1

- Comment: Water planar reflection resolution.


## ReplaySession

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Request replay of previously-recorded pilot file


## ReportBugURL

- Type: String | Default value: `https://phoenixviewer.com/app/file-a-jira/?environment=[ENVIRONMENT]` | Persisted: 1

- Comment: URL used for filing bugs from viewer


## RequestFullRegionCache

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If set, ask sim to send full region object cache. Needs to restart viewer.


## ResetToolbarSettings

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If enabled, reset some skin-specific settings next relog


## ResetUIScaleOnFirstRun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Resets the UI scale factor on first run due to changed display scaling behavior


## ResetViewTurnsAvatar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: This option keeps the camera direction and turns the avatar when Reset View is selected (hit ESC key).


## RestoreCameraPosOnLogin

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reset camera position to location at logout


## RestoreGlobalSettings

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Defines if the global settings should be restored when doing a settings restore.


## RestorePerAccountSettings

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Defines if the per account settings should be restored when doing a settings restore.


## RestrainedLove

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles the RestrainedLove features (BDSM lockable toys support). Needs a restart of the viewer.


## RestrainedLoveCanOOC

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allows sending OOC chat when send chat restricted, or seeing OOC chat when receive chat restricted


## RestrainedLoveDebug

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles the RestrainedLove debug mode (displays the commands when in debug mode).


## RestrainedLoveForbidGiveToRLV

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When TRUE, forbids to give sub-folders to the #RLV RestrainedLove folder.


## RestrainedLoveNoSetEnv

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When TRUE, forbids to set the environment (time of day and Windlight settings) via RestrainedLove. Needs a restart of the viewer.


## RestrainedLoveReplaceWhenFolderBeginsWith

- Type: String | Default value: `` | Persisted: 1

- Comment: If a folder name begins with this string, its attach behavior will always be "replace", never "stack". Default is blank (disabled).


## RestrainedLoveShowEllipsis

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When TRUE, show "..." when someone speaks, while the avatar is prevented from hearing. When FALSE, don't show anything.


## RestrainedLoveStackWhenFolderBeginsWith

- Type: String | Default value: `+` | Persisted: 1

- Comment: If a folder name begins with this string, its attach behavior will always be "stack", never "replace". Default is "+".


## RevokePermsOnStopAnimation

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Clear animation permssions when choosing "Stop Animating Me"


## RezUnderLandGroup

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Rez objects under land group when possible.


## RotateRight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Make the agent rotate to its right.


## RotationStep

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: All rotations via rotation tool are constrained to multiples of this unit (degrees)


## RunMultipleThreads

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE keep background threads active during render. No longer used; always treated as TRUE.


## SDL2IMEChatHistoryVerticalOffset

- Type: S32 | Default value: `14` | Persisted: 1

- Comment: Chat History: Vertical offset to apply to the international input method editor for Japanese, Chinese, etc.


## SDL2IMEDefaultVerticalOffset

- Type: S32 | Default value: `18` | Persisted: 1

- Comment: Default vertical offset to apply to the international input method editor for Japanese, Chinese, etc.


## SDL2IMEEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable the international input method editor for Japanese, Chinese, etc.


## SDL2IMEMediaVerticalOffset

- Type: S32 | Default value: `-4` | Persisted: 1

- Comment: Media: Vertical offset to apply to the international input method editor for Japanese, Chinese, etc.


## SLURLDragNDrop

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable drag and drop of SLURLs onto the viewer


## SLURLPassToOtherInstance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pass execution to prevoius viewer instances if there is a given slurl


## SLURLTeleportDirectly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clicking on a slurl will teleport you directly instead of opening places panel


## SafeMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reset preferences, run in safe mode.


## SaveMinidump

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Save minidump for developer debugging on crash


## SaveMinidumpType

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Type of minidump that is created (0 - minimal, 1 - normal [default], 2 - extended)


## ScaleShowAxes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show indicator of selected scale axis when scaling


## ScaleStretchTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Stretch textures along with object when scaling


## ScaleUniform

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Scale selected objects evenly about center of selection


## SceneLoadFrontPixelThreshold

- Type: F32 | Default value: `100.0` | Persisted: 1

- Comment: in pixels, all objects in view frustum whose screen area is greater than this threshold will be loaded


## SceneLoadHighMemoryBound

- Type: U32 | Default value: `4096` | Persisted: 1

- Comment: in MB, when total memory usage above this threshold, minimum invisible objects are kept in memory 


## SceneLoadLowMemoryBound

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: in MB, when total memory usage above this threshold, start to reduce invisible objects kept in memory 


## SceneLoadMinRadius

- Type: F32 | Default value: `32.0` | Persisted: 1

- Comment: in meters, all objects (visible or invisible) within this radius will remain loaded in memory


## SceneLoadRearMaxRadiusFraction

- Type: F32 | Default value: `0.75` | Persisted: 1

- Comment: a fraction of draw distance beyond which all objects outside of view frustum will be unloaded, regardless of pixel threshold


## SceneLoadRearPixelThreshold

- Type: F32 | Default value: `400.0` | Persisted: 1

- Comment: in pixels, all objects out of view frustum whose screen area is greater than this threshold will remain loaded


## SceneLoadingMonitorEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enabled scene loading monitor if set


## SceneLoadingMonitorPixelDiffThreshold

- Type: F32 | Default value: `0.02` | Persisted: 1

- Comment: Amount of pixels changed required to consider the scene as still loading (square root of fraction of pixels on screen)


## SceneLoadingMonitorSampleTime

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Time between screen samples when monitor scene load (seconds)


## ScriptDialogLimitations

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Limits amount of dialogs per script (0 - per object, 1 - per channel, 2 - per channel for attachments, 3 - per channel for HUDs, 4 - unconstrained for HUDs, 5 - unconstrained)


## ScriptDialogsPosition

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Holds the position where script llDialog floaters will show up. 1 = docked to chiclet, 2 = top left, 3 = top right, 4 = bottom left, 5 = bottom right


## ScriptEditorDisableSyntaxHighlight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable syntax highlighting in script editor for performance testing


## ScriptHelpFollowsCursor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Scripting help window updates contents based on script editor contents under text cursor


## ScriptToastButtonWidth

- Type: S32 | Default value: `127` | Persisted: 1

- Comment: Default width of buttons in the Script dialog toast.


## ScriptsCanShowUI

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow LSL calls (such as LLMapDestination) to spawn viewer UI


## ScriptsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created script


## ScriptsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created scripts can be copied by next owner


## ScriptsNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created scripts can be modified by next owner


## ScriptsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created scripts can be resold or given away by next owner


## ScriptsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created scripts are shared with the currently active group


## SearchFromAddressBar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Can enter search queries into navigation address bar


## SearchURL

- Type: String | Default value: `https://search.[GRID]/viewer/?query_term=[QUERY]&search_type=[TYPE][COLLECTION]&maturity=[MATURITY]&lang=[LANGUAGE]&sid=[SESSION_ID]` | Persisted: 1

- Comment: URL for Search website, displayed in the Find floater


## SearchURLDebug

- Type: String | Default value: `` | Persisted: 1

- Comment: Debug URL for Search website. Overrides any other search URL if DebugSearch is true. Displayed in the Find floater


## SearchURLOpenSim

- Type: String | Default value: `http://search.metaverseink.com/opensim/results.jsp?query=[QUERY]&submit=[CATEGORY]` | Persisted: 0

- Comment: Fallback URL for Search website if the loginservice doesn't provide a search URL. Displayed in the Find floater


## SelectInvisibleObjects

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Select invisible objects


## SelectMovableOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Select only objects you can move


## SelectOwnedOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Select only objects you own


## SelectReflectionProbes

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Select reflection probes


## SelectionHighlightAlpha

- Type: F32 | Default value: `0.20000000596` | Persisted: 1

- Comment: Opacity of selection highlight (0.0 = completely transparent, 1.0 = completely opaque)


## SelectionHighlightAlphaTest

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Alpha value below which pixels are displayed on selection highlight line (0.0 = show all pixels, 1.0 = show now pixels)


## SelectionHighlightThickness

- Type: F32 | Default value: `0.00999999977648` | Persisted: 1

- Comment: Thickness of selection highlight line (fraction of view distance)


## SelectionHighlightUAnim

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rate at which texture animates along U direction in selection highlight line (fraction of texture per second)


## SelectionHighlightUScale

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Scale of texture display on selection highlight line (fraction of texture size)


## SelectionHighlightVAnim

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Rate at which texture animates along V direction in selection highlight line (fraction of texture per second)


## SelectionHighlightVScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of texture display on selection highlight line (fraction of texture size)


## ServerChoice

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: [DO NOT MODIFY] Controls which grid you connect to


## SessionSettingsFile

- Type: String | Default value: `` | Persisted: 1

- Comment: Settings that are a applied per session (not saved).


## SettingsBackupPath

- Type: String | Default value: `` | Persisted: 1

- Comment: Path where settings were last backed up.


## SettingsNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created Environment setting can be modified by next owner


## SettingsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created Environment setting can be resold or given away by next owner


## ShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Newly created objects are shared with the currently active group


## ShowAdultClassifieds

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find classifieds that are flagged as adult


## ShowAdultEvents

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find events that are flagged as adult


## ShowAdultGroups

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find groups that are flagged as adult


## ShowAdultLand

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find land sales that are flagged as adult


## ShowAdultSims

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find places or find popular that are in adult sims


## ShowAllObjectHoverTip

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show descriptive tooltip when mouse hovers over non-interactive and interactive objects.


## ShowAxes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render coordinate frame at your position


## ShowBanLines

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Show in-world ban/access borders, 0 - do not show, 1 - show on collision, 2 - show on proximity


## ShowBetaGrids

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display the beta grids in the grid selection control.


## ShowBlockedConvHistory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Specifies whether blocked agents will be shown in Call Log


## ShowChatMiniIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Toggles the display of mini icons in chat transcript


## ShowConsoleWindow

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show log in separate OS window


## ShowCrosshairs

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display crosshairs when in mouselook mode


## ShowDebugConsole

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show log in SL window


## ShowDeviceSettings

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show device settings


## ShowDiscordActivityDetails

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When set, show avatar name on Discord Rich Presence (UNUSED)


## ShowDiscordActivityState

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When set, show location on Discord Rich Presence (UNUSED)


## ShowEventRecorderMenuItems

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Whether or not Event Recorder menu choices - Start / Stop event recording should appear in the (currently) Develop menu


## ShowGroupNoticesTopRight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show group notifications to the top right corner of the screen.


## ShowHelpOnFirstLogin

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show Help Floater on first login


## ShowHoverTips

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show descriptive tooltip when mouse hovers over items in world


## ShowInInventory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Automatically opens inventory to show accepted objects


## ShowLandHoverTip

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show descriptive tooltip when mouse hovers over land


## ShowMatureClassifieds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find classifieds that are flagged as moderate


## ShowMatureEvents

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find events that are flagged as moderate


## ShowMatureGroups

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find groups that are flagged as moderate


## ShowMatureLand

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find land sales that are flagged as moderate


## ShowMatureSims

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find places or find popular that are in moderate sims


## ShowMenuBarLocation

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/Hide location info in the menu bar


## ShowMiniLocationPanel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show/hide mini-location panel


## ShowMyComplexityChanges

- Type: U32 | Default value: `10` | Persisted: 1

- Comment: How long to show notices about avatar complexity (set to zero to disable those notices)


## ShowNavbarFavoritesPanel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide navigation bar favorites panel


## ShowNavbarNavigationPanel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show/hide navigation bar navigation panel


## ShowNearClip

- Type: Boolean | Default value: `0` | Persisted: 0


## ShowNetStats

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show the Status Indicators for the Viewer and Network Usage in the Status Overlay.


## ShowNewInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically views new notecards/textures/landmarks


## ShowObjectRenderingCost

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the object rendering cost in build tools


## ShowObjectUpdates

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show when update messages are received for individual objects


## ShowOfferedInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show inventory window with last inventory offer selected when receiving inventory from other users.


## ShowOverlayTitle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Prints watermark text message on screen


## ShowPGClassifieds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find classifieds that are flagged as general


## ShowPGEvents

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find events that are flagged as general


## ShowPGGroups

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find groups that are flagged as general


## ShowPGLand

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find land sales that are flagged as general


## ShowPGSims

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find places or find popular that are in general sims


## ShowParcelOwners

- Type: Boolean | Default value: `0` | Persisted: 0


## ShowPermissions

- Type: Boolean | Default value: `0` | Persisted: 0


## ShowPhysicsShapeInEdit

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: show physics shapes while building


## ShowProfileFloaters

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows resident profiles in a floater rather than the side tray


## ShowPropertyLines

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show line overlay demarking property boundaries


## ShowRadarMinimap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Toggle visibility of the embedded minimap in the radar panel


## ShowScriptErrors

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show script errors


## ShowScriptErrorsLocation

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Show script error in chat (0) or window (1).


## ShowSearchTopBar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Toggles whether the search field is displayed at the top of the viewer


## ShowSelectionBeam

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show selection particle beam when selecting or interacting with objects.


## ShowSpecificLODInEdit

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: Force the display of a specific LOD while editing


## ShowStartLocation

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display starting location menu on login screen


## ShowStreamMetadata

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Shows stream metadata (artist, title) notifications. (0 = Off, 1 = Notification Toast, 2 = Nearby Chat)


## ShowTangentBasis

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render normal and binormal (debugging bump mapping)


## ShowTunedART

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the current render time not the pre-tuning render time in the avatar display.


## ShowTutorial

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show tutorial window on login


## ShowVoiceChannelPopup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Controls visibility of the current voice channel popup above the voice tab


## ShowVoiceVisualizersInCalls

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables in-world voice visuals, voice gestures and lip-sync while in group or P2P calls.


## ShowVolumeSettingsPopup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show individual volume slider for voice, sound effects, etc


## SimulateFBOFailure

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: [DEBUG] Make allocateScreenBuffer return false.  Used to test error handling.


## SingleModeDoubleClickOpenWindow

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sets the action for Double-click on folder in single-folder view (0 - stays in current window, 1 - opens a new window)


## SkinCurrent

- Type: String | Default value: `firestorm` | Persisted: 1

- Comment: The currently selected skin.


## SkinCurrentTheme

- Type: String | Default value: `grey` | Persisted: 1

- Comment: The selected theme for the current skin.


## SkinningSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Client skin color setting file name (per install).


## SkipBenchmark

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: if true, disables running the GPU benchmark at startup
      (default to class 1)


## SkyAmbientScale

- Type: F32 | Default value: `0.300000011921` | Persisted: 1

- Comment: Controls strength of ambient, or non-directional light from the sun and moon (fraction or multiple of default ambient level)


## SkyMoonDefaultPosition

- Type: Vector3 | Default value: `-1.0 0.0 -0.1` | Persisted: 1

- Comment: Default position of sun in sky (direction in world coordinates)


## SkyNightColorShift

- Type: Color3 | Default value: `0.67 0.67 1.0` | Persisted: 1

- Comment: Controls moonlight color (base color applied to moon as light source)


## SkyOverrideSimSunPosition

- Type: Boolean | Default value: `0` | Persisted: 0


## SkyPresetName

- Type: String | Default value: `Default` | Persisted: 1

- Comment: Sky preset to use. May be superseded by region settings or by a day cycle (see DayCycleName).


## SkySunDefaultPosition

- Type: Vector3 | Default value: `1.0 0.0 0.1` | Persisted: 1

- Comment: Default position of sun in sky (direction in world coordinates)


## SnapEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable snapping to grid


## SnapMargin

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Controls maximum distance between windows before they auto-snap together (pixels)


## SnapToMouseCursor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When snapping to grid, center object on nearest grid point to mouse cursor


## SnapshotFormat

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Save snapshots in this format (0 = PNG, 1 = JPEG, 2 = BMP)


## SnapshotLayers

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Which layers should be used for a snapshot.


## SnapshotQuality

- Type: S32 | Default value: `75` | Persisted: 1

- Comment: Quality setting of postcard JPEGs (0 = worst, 100 = best)


## SnapshotToDiskQuality

- Type: S32 | Default value: `75` | Persisted: 1

- Comment: Quality setting of snapshot to disk JPEGs (0 = worst, 100 = best)


## SnapshotToProfileIncludeLocation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Include location information with a snapshot taken to profile.


## Socks5AuthType

- Type: String | Default value: `None` | Persisted: 1

- Comment: Selected Auth mechanism for Socks5


## Socks5ProxyEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Socks5 Proxy


## Socks5ProxyHost

- Type: String | Default value: `` | Persisted: 1

- Comment: Socks 5 Proxy Host


## Socks5ProxyPort

- Type: U32 | Default value: `1080` | Persisted: 1

- Comment: Socks 5 Proxy Port


## SortFriendsFirst

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Specifies whether friends will be sorted first in Call Log


## SpeakerParticipantDefaultOrder

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Order for displaying speakers in voice controls.  0 = alphabetical. 1 = recent.


## SpeakerParticipantRemoveDelay

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Timeout to remove participants who is not in channel before removed from list of active speakers (text/voice chat)


## SpeedTest

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Performance testing mode, no network


## SpellCheck

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable spellchecking on line and text editors


## SpellCheckDictionary

- Type: String | Default value: `English (United States),Second Life Glossary` | Persisted: 1

- Comment: Current primary and secondary dictionaries used for spell checking


## StarLightShowMapDetails

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the details panel on the side of the World Map


## StartUpToastLifeTime

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Number of seconds while a Startup toast exist


## StatsAutoRun

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Play back autopilot


## StatsFile

- Type: String | Default value: `fs.txt` | Persisted: 1

- Comment: Filename for stats logging output


## StatsFrametimeEventThreshold

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: The percentage that the frametime difference must exceed in order to register a frametime event. 0.1 = 10%, 0.25 = 25%, etc.


## StatsFrametimeSampleSeconds

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: The number of seconds to sample extended frametime data (percentiles, stddev).


## StatsNumRuns

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Loop autopilot playback this number of times


## StatsPilotFile

- Type: String | Default value: `pilot.txt` | Persisted: 1

- Comment: Filename for stats logging autopilot path


## StatsPilotXMLFile

- Type: String | Default value: `pilot.xml` | Persisted: 1

- Comment: Filename for stats logging extended autopilot path


## StatsQuitAfterRuns

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Quit application after this number of autopilot playback runs


## StatsReportFileInterval

- Type: F32 | Default value: `0.2` | Persisted: 1

- Comment: Interval to save viewer stats file data


## StatsReportMaxDuration

- Type: F32 | Default value: `300` | Persisted: 1

- Comment: Maximum seconds for viewer stats file data, prevents huge file


## StatsReportSkipZeroDataSaves

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: In viewer stats data file, skip saving entry if there is no data


## StatsSessionTrackFrameStats

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Track rendering and network statistics


## StatsSummaryFile

- Type: String | Default value: `fss.txt` | Persisted: 1

- Comment: Filename for stats logging summary


## StopMicCaptureWhenMuted

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Check to stop microphone capture while muted. May cause a hiss on unmute but prevents bluetooth devices always being in voice mode.


## StreamMetadataAnnounceChannel

- Type: S32 | Default value: `362394` | Persisted: 1

- Comment: Chat channel where stream metadata is announced to.


## StreamMetadataAnnounceToChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Announces stream metadata to a defined chat channel.


## SwitchToSharedEnvAfterTeleport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Switch to Shared Environment after teleport


## SyncMaterialSettings

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: SyncMaterialSettings


## SysinfoButtonInIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows or hides the system info button in IM floaters. Used to send your system information to a support helper in IM.


## SystemLanguage

- Type: String | Default value: `en` | Persisted: 1

- Comment: Language indicated by system settings (for UI)


## TabToTextFieldsOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: TAB key takes you to next text entry field, instead of next widget


## TargetFPS

- Type: U32 | Default value: `15` | Persisted: 1

- Comment: Desired minimum FPS


## TeleportArrivalDelay

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Time to wait before displaying world during teleport (seconds)


## TeleportLocalDelay

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Delay to prevent teleports after starting an in-sim teleport. (seconds)


## TempAllowScriptedMedia

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Allow scripts to control media


## TemporaryUpload

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Temporary texture upload flag (volatile)


## TermsAndConditionsURL

- Type: String | Default value: `https://lindenlab.com/legal/second-life-terms-and-conditions` | Persisted: 1

- Comment: URL pointing to Terms and Conditions page


## TermsOfServiceURL

- Type: String | Default value: `https://lindenlab.com/tos` | Persisted: 1

- Comment: URL pointing to Terms of Service page


## TerrainColorHeightRange

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Altitude range over which a given terrain texture has effect (meters)


## TerrainColorStartHeight

- Type: F32 | Default value: `20.0` | Persisted: 1

- Comment: Starting altitude for terrain texturing (meters)


## TerrainPaintBitDepth

- Type: U32 | Default value: `5` | Persisted: 1

- Comment: Bit depth for future terrain paint map operations. Min: 1. Max: 8. Takes effect when the paint map is created or modified. Modifications to an existing paintmap of different bit depth will have lower precision.


## TerrainPaintResolution

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: Resolution of the terrain paint map in pixels. Rounded to a power of two. Min: 16. Max: RenderMaxTextureResolution. Takes effect when the paint map is created.


## TestGridStatusRSSFromFile

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: For testing only: Don't update rss xml file from server.


## TextureCameraBoost

- Type: F32 | Default value: `8.0` | Persisted: 0

- Comment: Amount to boost resolution of textures that are important to the camera.


## TextureDecodeDisabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, do not fetch and decode any textures


## TextureDisable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, do not load textures for in-world content


## TextureDiscardBackgroundedTime

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Specify how long to wait before discarding texture data after viewer is backgrounded.  (zero or negative to disable)


## TextureDiscardLevel

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Specify texture resolution (0 = highest, 5 = lowest)


## TextureDiscardMinimizedTime

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Specify how long to wait before discarding texture data after viewer is minimized.  (zero or negative to disable)


## TextureFetchConcurrency

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Maximum number of HTTP connections used for texture fetches


## TextureFetchFakeFailureRate

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Simulate HTTP fetch failures for some server bake textures.


## TextureFetchMinTimeToLog

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: If texture fetching time exceeds this value, texture fetch tester will log info


## TextureFetchUpdateMinCount

- Type: S32 | Default value: `32` | Persisted: 1

- Comment: Minimum number of textures to update per frame


## TextureLivePreview

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Preview selections in texture picker or material picker immediately


## TextureLoadFullRes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, always load textures at full resolution (discard = 0). Not persistent. Will cause excessive memory pressure.


## TextureLoggingThreshold

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Specifies the byte threshold at which texture download data should be sent to the region.


## TextureNewByteRange

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the new more accurate byte range computation for j2c discard levels


## TextureReverseByteRange

- Type: S32 | Default value: `50` | Persisted: 1

- Comment: Minimal percent of the optimal byte range allowed to render a given discard level


## TextureSaveLocation

- Type: String | Default value: `` | Persisted: 0

- Comment: Current location for bulk saving textures to disk


## TextureScaleMaxAreaFactor

- Type: F32 | Default value: `25.0` | Persisted: 1

- Comment: Limits how texture scale affects area calculation.


## TextureScaleMinAreaFactor

- Type: F32 | Default value: `0.0095` | Persisted: 1

- Comment: Limits how texture scale affects area calculation.


## ThreadPoolSizes

- Type: LLSD | Default value: `General 1 ImageDecode 9` | Persisted: 1

- Comment: Map of size overrides for specific thread pools.


## ThrottleBandwidthKBPS

- Type: F32 | Default value: `3000.0` | Persisted: 1

- Comment: Maximum allowable downstream bandwidth (kilo bits per second)


## TipToastMessageLineCount

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Max line count of text message on tip toast.


## ToastButtonWidth

- Type: S32 | Default value: `90` | Persisted: 1

- Comment: Default width of buttons in the toast. 
Notes:
If required width will be less than this one, a button will be reshaped to default size , otherwise to required. 
Change of this parameter will affect the layout of buttons in notification toast.


## ToastFadingTime

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Number of seconds while a toast is fading 


## ToastGap

- Type: S32 | Default value: `7` | Persisted: 1

- Comment: Gap between toasts on a screen (min. value is 5)


## ToolTipDelay

- Type: F32 | Default value: `0.699999988079` | Persisted: 1

- Comment: Seconds before displaying tooltip when mouse stops over UI element


## ToolTipFadeTime

- Type: F32 | Default value: `0.2` | Persisted: 1

- Comment: Seconds over which tooltip fades away


## ToolTipFastDelay

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Seconds before displaying tooltip when mouse stops over UI element (when a tooltip is already visible)


## ToolTipVisibleTimeFar

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Fade tooltip after time passes (seconds) while mouse not near tooltip


## ToolTipVisibleTimeNear

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Fade tooltip after time passes (seconds) while mouse near tooltip or original position


## ToolTipVisibleTimeOver

- Type: F32 | Default value: `1000.0` | Persisted: 1

- Comment: Fade tooltip after time passes (seconds) while mouse over tooltip


## ToolboxAutoMove

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [NOT USED]


## TrackFocusObject

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Camera tracks last object zoomed on


## TranslateChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Translate incoming chat messages


## TranslateLanguage

- Type: String | Default value: `default` | Persisted: 1

- Comment: Translate specified language


## TranslationService

- Type: String | Default value: `azure` | Persisted: 1

- Comment: Translation API to use. (google|azure)


## TuningFPSStrategy

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Strategy to use when tuning FPS. 0=Tune avatar rendering only, 1=Tune both avatar and global scene settings, 2=Tune only global scene.


## TutorialURL

- Type: String | Default value: `` | Persisted: 0

- Comment: URL for tutorial menu item, set automatically during login


## TypeAheadTimeout

- Type: F32 | Default value: `1.5` | Persisted: 1

- Comment: Time delay before clearing type-ahead buffer in lists (seconds)


## UIAutoScale

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep UI scale consistent across different resolutions


## UIButtonOrigHPad

- Type: S32 | Default value: `6` | Persisted: 1

- Comment: UI Button Original Horizontal Pad


## UICheckboxctrlHPad

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Checkbox Control Horizontal Pad


## UICheckboxctrlSpacing

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: UI Checkbox Control Spacing


## UICheckboxctrlVPad

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Checkbox Control Vertical Pad


## UICloseBoxFromTop

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Distance from top of floater to top of close box icon, pixels


## UIExtraTriangleHeight

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: UI extra triangle height


## UIExtraTriangleWidth

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI extra triangle width


## UIFloaterCloseBoxSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: Size of UI floater close box size


## UIFloaterHPad

- Type: S32 | Default value: `6` | Persisted: 1

- Comment: Size of UI floater horizontal pad


## UIFloaterTestBool

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Example saved setting for the test floater


## UIImgDefaultAlphaUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultEyesUUID

- Type: String | Default value: `6522e74d-1660-4e7f-b601-6f48c1659a77` | Persisted: 0


## UIImgDefaultGlovesUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultHairUUID

- Type: String | Default value: `7ca39b4c-bd19-4699-aff7-f93fd03d3e7b` | Persisted: 0


## UIImgDefaultJacketUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultPantsUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultShirtUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultShoesUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultSkirtUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultSocksUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgDefaultUnderwearUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0


## UIImgInvisibleUUID

- Type: String | Default value: `f54a0c32-3cd1-d49a-5b4f-7b792bebc204` | Persisted: 0


## UIImgTransparentUUID

- Type: String | Default value: `8dcd4a48-2d37-4909-9f78-f7a9eb4ef903` | Persisted: 0


## UILineEditorCursorThickness

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Line Editor Cursor Thickness


## UIMaxComboWidth

- Type: S32 | Default value: `500` | Persisted: 1

- Comment: Maximum width of combo box


## UIMinimizedWidth

- Type: S32 | Default value: `160` | Persisted: 1

- Comment: Size of UI floater minimized width


## UIMultiSliderctrlSpacing

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI multi slider ctrl spacing


## UIMultiTrackHeight

- Type: S32 | Default value: `6` | Persisted: 1

- Comment: UI multi track height


## UIPreeditMarkerBrightness

- Type: F32 | Default value: `0.4` | Persisted: 1

- Comment: UI Preedit Marker Brightness


## UIPreeditMarkerGap

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Preedit Marker Gap


## UIPreeditMarkerPosition

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI Preedit Marker Position


## UIPreeditMarkerThickness

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Preedit Marker Thickness


## UIPreeditStandoutBrightness

- Type: F32 | Default value: `0.6` | Persisted: 1

- Comment: UI Preedit Standout Brightness


## UIPreeditStandoutGap

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Preedit Standout Gap


## UIPreeditStandoutPosition

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI Preedit Standout Position


## UIPreeditStandoutThickness

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Preedit Standout Thickness


## UIPreviewMaterial

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not PBR material swatch is enabled


## UIResizeBarHeight

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Size of UI resize bar height


## UIScaleFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Size of UI relative to default layout on 1024x768 screen


## UIScrollbarSize

- Type: S32 | Default value: `15` | Persisted: 1

- Comment: UI scrollbar size


## UISliderctrlHeight

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI slider ctrl height


## UISliderctrlSpacing

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI slider ctrl spacing


## UISndAlert

- Type: String | Default value: `ed124764-705d-d497-167a-182cd9fa2e6c` | Persisted: 1

- Comment: Sound file for alerts (uuid for sound asset)


## UISndBadKeystroke

- Type: String | Default value: `2ca849ba-2885-4bc3-90ef-d4987a5b983a` | Persisted: 1

- Comment: Sound file for invalid keystroke (uuid for sound asset)


## UISndChatMention

- Type: String | Default value: `03e77cb5-592c-5b33-d271-2e46497c3fb3` | Persisted: 1

- Comment: Sound file for chat mention(uuid for sound asset)


## UISndChatPing

- Type: String | Default value: `7dd36df6-2624-5438-f988-fdf8588a0ad9` | Persisted: 1

- Comment: Sound file for chat ping(uuid for sound asset)


## UISndClick

- Type: String | Default value: `4c8c3c77-de8d-bde2-b9b8-32635e0fd4a6` | Persisted: 1

- Comment: Sound file for mouse click (uuid for sound asset)


## UISndClickRelease

- Type: String | Default value: `4c8c3c77-de8d-bde2-b9b8-32635e0fd4a6` | Persisted: 1

- Comment: Sound file for mouse button release (uuid for sound asset)


## UISndDebugSpamToggle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log UI sound effects as they are played


## UISndFootsteps

- Type: String | Default value: `e8af4a28-aa83-4310-a7c4-c047e15ea0df` | Persisted: 1

- Comment: Sound file for default footsteps (uuid for sound asset). Change requires restart to take effect.


## UISndFriendOffline

- Type: String | Default value: `ed124764-705d-d497-167a-182cd9fa2e6c` | Persisted: 1

- Comment: Sound file for friends going offline (uuid for sound asset)


## UISndFriendOnline

- Type: String | Default value: `ed124764-705d-d497-167a-182cd9fa2e6c` | Persisted: 1

- Comment: Sound file for friends coming online (uuid for sound asset)


## UISndFriendshipOffer

- Type: String | Default value: `67cc2844-00f3-2b3c-b991-6418d01e1bb7` | Persisted: 1

- Comment: Sound file for friendship offer (uuid for sound asset)


## UISndGroupInvitation

- Type: String | Default value: `c825dfbc-9827-7e02-6507-3713d18916c1` | Persisted: 1

- Comment: Sound file for group invitation (uuid for sound asset)


## UISndGroupNotice

- Type: String | Default value: `c825dfbc-9827-7e02-6507-3713d18916c1` | Persisted: 1

- Comment: Sound file for group notice (uuid for sound asset)


## UISndHealthReductionF

- Type: String | Default value: `219c5d93-6c09-31c5-fb3f-c5fe7495c115` | Persisted: 1

- Comment: Sound file for female pain (uuid for sound asset)


## UISndHealthReductionM

- Type: String | Default value: `e057c244-5768-1056-c37e-1537454eeb62` | Persisted: 1

- Comment: Sound file for male pain (uuid for sound asset)


## UISndHealthReductionThreshold

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Amount of health reduction required to trigger "pain" sound


## UISndIncomingVoiceCall

- Type: String | Default value: `c80260ba-41fd-8a46-768a-6bf236360e3a` | Persisted: 1

- Comment: Sound file for incoming voice call (uuid for sound asset)


## UISndInvalidOp

- Type: String | Default value: `4174f859-0d3d-c517-c424-72923dc21f65` | Persisted: 1

- Comment: Sound file for invalid operations (uuid for sound asset)


## UISndInventoryOffer

- Type: String | Default value: `67cc2844-00f3-2b3c-b991-6418d01e1bb7` | Persisted: 1

- Comment: Sound file for inventory offer (uuid for sound asset)


## UISndMicToggle

- Type: String | Default value: `d9f73cf8-17b4-6f7a-1565-7951226c305d` | Persisted: 1

- Comment: Sound file for microphone toggle (uuid for sound asset)


## UISndMoneyChangeDown

- Type: String | Default value: `104974e3-dfda-428b-99ee-b0d4e748d3a3` | Persisted: 1

- Comment: Sound file for L$ balance decrease (uuid for sound asset)


## UISndMoneyChangeThreshold

- Type: F32 | Default value: `50.0` | Persisted: 1

- Comment: Amount of change in L$ balance required to trigger "money" sound


## UISndMoneyChangeUp

- Type: String | Default value: `77a018af-098e-c037-51a6-178f05877c6f` | Persisted: 1

- Comment: Sound file for L$ balance increase (uuid for sound asset)


## UISndMovelockToggle

- Type: String | Default value: `4174f859-0d3d-c517-c424-72923dc21f65` | Persisted: 1

- Comment: Sound file for toggling movelock (uuid for sound asset)


## UISndNearbyChat

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file for nearby chat messages from other avatars (uuid for sound asset)


## UISndNewIncomingConfIMSession

- Type: String | Default value: `67cc2844-00f3-2b3c-b991-6418d01e1bb7` | Persisted: 1

- Comment: Sound file for new conference instant message session(uuid for sound asset)


## UISndNewIncomingGroupIMSession

- Type: String | Default value: `67cc2844-00f3-2b3c-b991-6418d01e1bb7` | Persisted: 1

- Comment: Sound file for new group instant message session(uuid for sound asset)


## UISndNewIncomingIMSession

- Type: String | Default value: `67cc2844-00f3-2b3c-b991-6418d01e1bb7` | Persisted: 1

- Comment: Sound file for new instant message session(uuid for sound asset)


## UISndObjectCreate

- Type: String | Default value: `f4a0660f-5446-dea2-80b7-6482a082803c` | Persisted: 1

- Comment: Sound file for object creation (uuid for sound asset)


## UISndObjectDelete

- Type: String | Default value: `0cb7b00a-4c10-6948-84de-a93c09af2ba9` | Persisted: 1

- Comment: Sound file for object deletion (uuid for sound asset)


## UISndObjectRezIn

- Type: String | Default value: `3c8fc726-1fd6-862d-fa01-16c5b2568db6` | Persisted: 1

- Comment: Sound file for rezzing objects (uuid for sound asset)


## UISndObjectRezOut

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 1

- Comment: Sound file for derezzing objects (uuid for sound asset)


## UISndPieMenuAppear

- Type: String | Default value: `8eaed61f-92ff-6485-de83-4dcc938a478e` | Persisted: 1

- Comment: Sound file for opening pie menu (uuid for sound asset)


## UISndPieMenuHide

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 1

- Comment: Sound file for closing pie menu (uuid for sound asset)


## UISndPieMenuSliceHighlight0

- Type: String | Default value: `d9f73cf8-17b4-6f7a-1565-7951226c305d` | Persisted: 1

- Comment: Sound file for selecting pie menu item 0 (uuid for sound asset)


## UISndPieMenuSliceHighlight1

- Type: String | Default value: `f6ba9816-dcaf-f755-7b67-51b31b6233e5` | Persisted: 1

- Comment: Sound file for selecting pie menu item 1 (uuid for sound asset)


## UISndPieMenuSliceHighlight2

- Type: String | Default value: `7aff2265-d05b-8b72-63c7-dbf96dc2f21f` | Persisted: 1

- Comment: Sound file for selecting pie menu item 2 (uuid for sound asset)


## UISndPieMenuSliceHighlight3

- Type: String | Default value: `09b2184e-8601-44e2-afbb-ce37434b8ba1` | Persisted: 1

- Comment: Sound file for selecting pie menu item 3 (uuid for sound asset)


## UISndPieMenuSliceHighlight4

- Type: String | Default value: `bbe4c7fc-7044-b05e-7b89-36924a67593c` | Persisted: 1

- Comment: Sound file for selecting pie menu item 4 (uuid for sound asset)


## UISndPieMenuSliceHighlight5

- Type: String | Default value: `d166039b-b4f5-c2ec-4911-c85c727b016c` | Persisted: 1

- Comment: Sound file for selecting pie menu item 5 (uuid for sound asset)


## UISndPieMenuSliceHighlight6

- Type: String | Default value: `242af82b-43c2-9a3b-e108-3b0c7e384981` | Persisted: 1

- Comment: Sound file for selecting pie menu item 6 (uuid for sound asset)


## UISndPieMenuSliceHighlight7

- Type: String | Default value: `c1f334fb-a5be-8fe7-22b3-29631c21cf0b` | Persisted: 1

- Comment: Sound file for selecting pie menu item 7 (uuid for sound asset)


## UISndQuestionExperience

- Type: String | Default value: `c825dfbc-9827-7e02-6507-3713d18916c1` | Persisted: 1

- Comment: Sound file for new experience notification (uuid for sound asset)


## UISndRadarAgeAlert

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file played when the age alert for an avatar is triggered (uuid for sound asset)


## UISndRadarChatEnter

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file played when avatars enter chat range (uuid for sound asset)


## UISndRadarChatLeave

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file played when avatars leave chat range (uuid for sound asset)


## UISndRadarDrawEnter

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file played when avatars enter draw distance (uuid for sound asset)


## UISndRadarDrawLeave

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file played when avatars leave draw distance (uuid for sound asset)


## UISndRadarSimEnter

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file played when avatars enter the region (uuid for sound asset)


## UISndRadarSimLeave

- Type: String | Default value: `a3f48b85-c29f-1f97-ebb6-644b7c053512` | Persisted: 1

- Comment: Sound file played when avatars leave the region (uuid for sound asset)


## UISndRestart

- Type: String | Default value: `b92a0f64-7709-8811-40c5-16afd624a45f` | Persisted: 1

- Comment: Sound file for region restarting, Second Life grid (uuid for sound asset)


## UISndRestartOpenSim

- Type: String | Default value: `4174f859-0d3d-c517-c424-72923dc21f65` | Persisted: 1

- Comment: Sound file for region restarting, OpenSim grid (uuid for sound asset)


## UISndScriptFloaterClose

- Type: String | Default value: `2c346eda-b60c-ab33-1119-b8941916a499` | Persisted: 1

- Comment: Sound file for closing a script dialog (uuid for sound asset)


## UISndScriptFloaterOpen

- Type: String | Default value: `c80260ba-41fd-8a46-768a-6bf236360e3a` | Persisted: 1

- Comment: Sound file for opening a script dialog (uuid for sound asset)


## UISndSnapshot

- Type: String | Default value: `3d09f582-3851-c0e0-f5ba-277ac5c73fb4` | Persisted: 1

- Comment: Sound file for taking a snapshot (uuid for sound asset)


## UISndStartIM

- Type: String | Default value: `c825dfbc-9827-7e02-6507-3713d18916c1` | Persisted: 1

- Comment: Sound file for starting a new IM session (uuid for sound asset)


## UISndTeleportOffer

- Type: String | Default value: `67cc2844-00f3-2b3c-b991-6418d01e1bb7` | Persisted: 1

- Comment: Sound file for teleport offer (uuid for sound asset)


## UISndTeleportOut

- Type: String | Default value: `d7a9a565-a013-2a69-797d-5332baa1a947` | Persisted: 1

- Comment: Sound file for teleporting (uuid for sound asset)


## UISndTrackerBeacon

- Type: String | Default value: `ed124764-705d-d497-167a-182cd9fa2e6c` | Persisted: 1

- Comment: Sound file for tracker beacon (uuid for sound asset)


## UISndTyping

- Type: String | Default value: `5e191c7b-8996-9ced-a177-b2ac32bfea06` | Persisted: 1

- Comment: Sound file for starting to type a chat message (uuid for sound asset)


## UISndWindowClose

- Type: String | Default value: `2c346eda-b60c-ab33-1119-b8941916a499` | Persisted: 1

- Comment: Sound file for closing a window (uuid for sound asset)


## UISndWindowOpen

- Type: String | Default value: `c80260ba-41fd-8a46-768a-6bf236360e3a` | Persisted: 1

- Comment: Sound file for opening a window (uuid for sound asset)


## UISpinctrlBtnHeight

- Type: S32 | Default value: `11` | Persisted: 1

- Comment: UI spin control button height


## UISpinctrlBtnWidth

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI spin control button width


## UISpinctrlSpacing

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI spin control spacing


## UITabCntrArrowBtnSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI Tab Container Arrow Button Size


## UITabCntrButtonPanelOverlap

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Tab Container Button Panel Overlap


## UITabCntrCloseBtnSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI Tab Container Close Button Size


## UITabCntrTabHPad

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI Tab Container Tab Horizontal Pad


## UITabCntrTabPartialWidth

- Type: S32 | Default value: `12` | Persisted: 1

- Comment: UI Tab Container Tab Partial Width


## UITabCntrVertTabMinWidth

- Type: S32 | Default value: `100` | Persisted: 1

- Comment: UI Tab Container Vertical Tab Minimum Width


## UITabCntrvArrowBtnSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI Tab Container V Arrow Button Size


## UITabCntrvPad

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: UI Tab Container V Pad


## UITabPadding

- Type: S32 | Default value: `15` | Persisted: 1

- Comment: UI Tab Padding


## UpdateAppWindowTitleBar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Updates the application window title bar with brief information about user/location


## UpdateRememberPasswordSetting

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Save 'rememeber password' setting for current user.


## UpdaterServiceSetting

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Configure updater service.


## UpdaterShowReleaseNotes

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Enables displaying of the Release notes in a web floater after update. 0 - don't show, 1 - show, 2 - show even for test viewers


## UpdaterWillingToTest

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not the updater should offer Beta upgrades.


## UploadBakedTexOld

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Forces the baked texture pipeline to upload using the old method.


## UploadsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly uploaded item


## UploadsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly uploaded items can be copied by next owner


## UploadsNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly uploaded items can be modified by next owner


## UploadsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly uploaded items can be resold or given away by next owner


## UploadsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly uploaded items are shared with the currently active group


## Use24HourClock

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: 12 vs 24. At the moment coverage is partial


## UseAltKeyForMenus

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Access menus via keyboard by tapping Alt


## UseAnimationTimeSteps

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable the use of animation timesteps to reduce render load for distant avatars.


## UseAntiSpam

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Activate the Anti-Spam System


## UseChatBubbles

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show chat above avatars head in chat bubbles


## UseCircuitCodeMaxRetries

- Type: S32 | Default value: `3` | Persisted: 0

- Comment: Max timeout count for the initial UseCircuitCode message


## UseCircuitCodeTimeout

- Type: F32 | Default value: `5.0` | Persisted: 0

- Comment: Timeout duration in seconds for the initial UseCircuitCode message


## UseDebugMenus

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Turns on "Debug" menu


## UseDefaultColorPicker

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use color picker supplied by operating system


## UseDisplayNames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use new, changeable, unicode names


## UseEnergy

- Type: Boolean | Default value: `1` | Persisted: 0


## UseFreezeFrame

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Freeze time when taking snapshots.


## UseGroupMemberPagination

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable pagination of group memeber list 50 members at a time.


## UseHTTPInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow use of http inventory transfers instead of UDP


## UseLSLBridge

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the client LSL bridge for lsl functionality


## UseLegacyIMLogNames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use legacy filenames for P2P IMs logs


## UseMediaPluginsForStreamingAudio

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use media plugins (VLC) for streaming audio.


## UseNewWalkRun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Replace standard walk/run animations with new ones.


## UseObjectCacheOcclusion

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable object cache level object culling based on occlusion (coverage) by other objects


## UseOcclusion

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable object culling based on occlusion (coverage) by other objects


## UsePeopleAPI

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the people API cap for avatar name fetching, use old legacy protocol if false. Requires restart.


## UsePhysicsCostOnly

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When displaying physics shapes in edit mode colour ramp based on physics cost not object cost.


## UsePieMenu

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the classic V1.x circular menu instead of the rectangular context menus when right clicking on land, avatars, objects or attachments.


## UseStartScreen

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to load a start screen image or not.


## UseTypingBubbles

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show typing indicator in avatar nametags


## UseWebPagesOnPrims

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [NOT USED]


## UserConnectionPort

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Port that this client transmits on.


## UserLogFile

- Type: String | Default value: `` | Persisted: 1

- Comment: User specified log file name.


## UserLoginInfo

- Type: String | Default value: `` | Persisted: 1

- Comment: User login data.


## UserLoginInfoCmdLine

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Command line supplied user login data.


## UserSessionSettingsFile

- Type: String | Default value: `` | Persisted: 1

- Comment: User settings that are a applied per session (not saved).


## VelocityInterpolate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Extrapolate object motion from last packet based on received velocity


## VersionChannelName

- Type: String | Default value: `` | Persisted: 1

- Comment: Version information generated by running the viewer


## VivoxAutoPostCrashDumps

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If true, SLVoice will automatically send crash dumps directly to Vivox.


## VivoxDebugLevel

- Type: String | Default value: `0` | Persisted: 1

- Comment: Logging level to use when launching the vivox daemon


## VivoxDebugSIPURIHostName

- Type: String | Default value: `` | Persisted: 1

- Comment: Hostname portion of vivox SIP URIs (empty string for the default).


## VivoxDebugVoiceAccountServerURI

- Type: String | Default value: `` | Persisted: 1

- Comment: URI to the vivox account management server (empty string for the default).


## VivoxLogDirectory

- Type: String | Default value: `` | Persisted: 1

- Comment: Default log path is Application Support/SecondLife/logs specify alternate absolute path here.


## VivoxShutdownTimeout

- Type: String | Default value: `5` | Persisted: 1

- Comment: shutdown timeout in miliseconds.  The amount of time to wait for the service to shutdown gracefully after the last disconnect


## VivoxVadAuto

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: A flag indicating if the automatic VAD is enabled (1) or disabled (0). The individual settings are ignored if the auto-mode is enabled


## VivoxVadHangover

- Type: U32 | Default value: `2000` | Persisted: 1

- Comment: The time (in milliseconds) that it takes or the VAD to switch back to silence from speech mode after the last speech frame has been detected


## VivoxVadNoiseFloor

- Type: U32 | Default value: `576` | Persisted: 1

- Comment: A dimensionless value between 0 and 20000 (default 576) that controls the maximum level at which the noise floor may be set at by the VAD's noise tracking


## VivoxVadSensitivity

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: A dimensionless value between 0 and 100, indicating the 'sensitivity of the VAD'. Increasing this value corresponds to decreasing the sensitivity of the VAD and 0 is turned off altogether


## VivoxVoiceHost

- Type: String | Default value: `127.0.0.1` | Persisted: 1

- Comment: Client SLVoice host to connect to


## VivoxVoicePort

- Type: U32 | Default value: `44125` | Persisted: 1

- Comment: Client SLVoice port to connect to


## VoiceAutomaticGainControl

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Voice Automatic Gain Control


## VoiceCallsRejectAdHoc

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Silently reject all incoming AdHoc (conference) voice calls.


## VoiceCallsRejectGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Silently reject all incoming group voice calls.


## VoiceCallsRejectP2P

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Silently reject all incoming P2P (avatar with avatar) voice calls.


## VoiceDisableMic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Completely disable the ability to open the mic.


## VoiceEarLocation

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Location of the virtual ear for voice


## VoiceEchoCancellation

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Voice Echo Cancellation


## VoiceHost

- Type: String | Default value: `127.0.0.1` | Persisted: 1

- Comment: Client SLVoice host to connect to


## VoiceImageLevel0

- Type: String | Default value: `041ee5a0-cb6a-9ac5-6e49-41e9320507d5` | Persisted: 1

- Comment: Texture UUID for voice image level 0


## VoiceImageLevel1

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 1


## VoiceImageLevel2

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 2


## VoiceImageLevel3

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 3


## VoiceImageLevel4

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 4


## VoiceImageLevel5

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 5


## VoiceImageLevel6

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 6


## VoiceInputAudioDevice

- Type: String | Default value: `Default` | Persisted: 1

- Comment: Audio input device to use for voice


## VoiceLogFile

- Type: String | Default value: `` | Persisted: 1

- Comment: Log file to use when launching the voice daemon


## VoiceMorphingEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Whether or not to enable Voice Morphs and show the UI.


## VoiceNoiseSuppressionLevel

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Voice Noise Suppression Level


## VoiceOutputAudioDevice

- Type: String | Default value: `Default` | Persisted: 1

- Comment: Audio output device to use for voice


## VoiceParticipantLeftRemoveDelay

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Timeout to remove participants who has left Voice chat from the list in Voice Controls Panel


## VoicePort

- Type: U32 | Default value: `44125` | Persisted: 1

- Comment: Client SLVoice port to connect to


## VoiceServerType

- Type: String | Default value: `` | Persisted: 0

- Comment: The type of voice server to use for group, conference, and p2p calls.


## VoiceVisualizerEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display voice dot indicator above an avatar


## WLSkyDetail

- Type: U32 | Default value: `64` | Persisted: 1

- Comment: [OBSOLETE]


## WarningsAsChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display warning messages in chat transcript


## WatchdogEnabled

- Type: S32 | Default value: `0` | Persisted: 0

- Comment: Controls whether the thread watchdog timer is activated. Value is S32. Set to -1 to defer to built-in default.


## WaterEditPresets

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to be able to edit the water defaults or not


## WaterFogColor

- Type: Color4 | Default value: `0.0863 0.168 0.212 0` | Persisted: 1

- Comment: Water fog color


## WaterFogDensity

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Water fog density


## WaterGLFogDensityScale

- Type: F32 | Default value: `0.02` | Persisted: 1

- Comment: Maps shader water fog density to gl fog density


## WaterGLFogDepthFloor

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Controls how dark water gl fog can get


## WaterGLFogDepthScale

- Type: F32 | Default value: `50.0` | Persisted: 1

- Comment: Controls how quickly gl fog gets dark under water


## WaterPresetName

- Type: String | Default value: `Default` | Persisted: 1

- Comment: Water preset to use. May be superseded by region settings.


## WearFolderLimit

- Type: U32 | Default value: `125` | Persisted: 1

- Comment: Limits number of items in the folder that can be replaced/added to current outfit


## WearablesEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created clothing or body part


## WearablesNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created clothing or body part can be copied by next owner


## WearablesNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created clothing or body part can be modified by next owner


## WearablesNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created clothing or body part can be resold or given away by next owner


## WearablesShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created clothing or body part is shared with the currently active group


## WebContentWindowLimit

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Maximum number of web browser windows that can be open at once in the Web content floater (0 for no limit)


## WebProfileFloaterRect

- Type: Rect | Default value: `0 680 500 0` | Persisted: 1

- Comment: Web profile floater dimensions


## WindLightUseAtmosShaders

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: DEPRECATED (only true supported) - Whether to enable or disable WindLight atmospheric shaders.


## WindowHeight

- Type: U32 | Default value: `738` | Persisted: 1

- Comment: SL viewer window height


## WindowMaximized

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: SL viewer window maximized on login


## WindowWidth

- Type: U32 | Default value: `1024` | Persisted: 1

- Comment: SL viewer window width


## WindowX

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: X coordinate of upper left corner of SL viewer window, relative to upper left corner of primary display (pixels)


## WindowY

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Y coordinate of upper left corner of SL viewer window, relative to upper left corner of primary display (pixels)


## WorldmapFilterDuplicateLandmarks

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Filter duplicate Landmarks in the Landmark list on the world map.


## XferThrottle

- Type: F32 | Default value: `150000.0` | Persisted: 1

- Comment: Maximum allowable downstream bandwidth for asset transfers (bits per second)


## YawFromMousePosition

- Type: F32 | Default value: `90.0` | Persisted: 1

- Comment: Horizontal range over which avatar head tracks mouse position (degrees of head rotation from left of window to right)


## YieldTime

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Yield some time to the local host.


## YouAreHereDistance

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Radius of distance for banner that indicates if the resident is "on" the Place.(meters from avatar to requested place)


## ZoomDirect

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Map Joystick zoom axis directly to camera zoom.


## ZoomTime

- Type: F32 | Default value: `0.40000000596` | Persisted: 1

- Comment: Time of transition between different camera modes (seconds)


## _NACL_AntiSpamAmount

- Type: U32 | Default value: `10` | Persisted: 1

- Comment: Number of messages needed over _NACL_AntiSpamTime seconds to trigger the spam system


## _NACL_AntiSpamGlobalQueue

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Do not track types of spam seperately, all actions from a single owner/source will be processed together. Anything triggering spam will cause that source to be blocked from all further methods of input. Use in cases of extreme spam only.


## _NACL_AntiSpamNewlines

- Type: U32 | Default value: `70` | Persisted: 1

- Comment: Messages with more than these number of lines will be squelched and sender blocked


## _NACL_AntiSpamSoundMulti

- Type: U32 | Default value: `6` | Persisted: 1

- Comment: Multiplier for _NACL_AntiSpamTime for sounds heard in _NACL_AntiSpamTime interval needed to trigger a block, since sounds are more common


## _NACL_AntiSpamSoundPreloadMulti

- Type: U32 | Default value: `6` | Persisted: 1

- Comment: Multiplier for _NACL_AntiSpamTime for sound preloads heard in _NACL_AntiSpamTime interval needed to trigger a block, since preloads are more common


## _NACL_AntiSpamTime

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Time inverval in seconds by which to track incoming messages. Within this inverval any messages received more than _NACL_ANtiSpamAmount times will trigger a block. Default interval is 2 seconds.


## _NACL_LSLPreprocessor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: LSL Preprocessor


## _NACL_MLFovValues

- Type: Vector3 | Default value: `1.047197551 1.047197551 0.0` | Persisted: 1

- Comment: NaCl Fov zoom values


## _NACL_PreProcEnableHDDInclude

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable #include from local disk


## _NACL_PreProcHDDIncludeLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Path for local disk includes


## _NACL_PreProcLSLLazyLists

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: LSL Lazy Lists


## _NACL_PreProcLSLOptimizer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: LSL Optimizer


## _NACL_PreProcLSLSwitch

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: LSL Switch Statements


## _NACL_PreProcLSLTextCompress

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: LSL Text Compress


## always_showable_floaters

- Type: LLSD | Default value: `snapshot postcard mini_map fs_nearby_chat fs_im_container inventory beacons avatar_picker stats script_floater world_map preferences flickr primfeed` | Persisted: 1

- Comment: Floaters that can be shown despite mouselook mode


## fsregioncornerbeacons

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show beacons at region corners to help avoid region boundary disconnects


## max_texture_dimension_X

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: Maximum texture width for user uploaded textures


## max_texture_dimension_Y

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: Maximum texture height for user uploaded textures


## moapbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight media on a prim sources


## moonbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show direction to the Moon


## particlesbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight particle generators


## physicalbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight physical objects


## renderbeacons

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight particle generators


## renderhighlights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Beacon / Highlight scripted objects with touch function


## scriptsbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight scripted objects


## scripttouchbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight scripted objects with touch function


## soundsbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight sound generators


## sourceid

- Type: String | Default value: `` | Persisted: 1

- Comment: Identify referring agency to Linden web servers


## sunbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show direction to the Sun


## teleport_offer_invitation_max_length

- Type: S32 | Default value: `178` | Persisted: 1

- Comment: Maximum length of teleport offer invitation line editor. 254 - max_location_url_length(76) = 178
