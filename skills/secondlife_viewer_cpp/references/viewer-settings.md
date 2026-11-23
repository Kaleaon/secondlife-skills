# Viewer Settings Reference (generated from secondlife/viewer)

Generated from `indra/newview/app_settings/settings.xml` on the viewer develop branch. Each entry is a real viewer setting with its upstream comment, type, default value, and persistence flag.


## 360CaptureCameraFOV

- Type: U32 | Default value: `75` | Persisted: 1

- Comment: Field of view of the WebGL camera that converts the cubemap to an equirectangular image

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## 360CaptureDebugSaveImage

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flag if set, saves off each cube map as an image, as well as the JavaScript data URL, for debugging purposes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## 360CaptureHideAvatars

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flag if set, removes all the avatars from the 360 snapshot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## 360CaptureJPEGEncodeQuality

- Type: U32 | Default value: `95` | Persisted: 1

- Comment: Quality value to use in the JPEG encoder (0..100)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## 360CaptureNumRenderPasses

- Type: U32 | Default value: `3` | Persisted: 1

- Comment: Number of times to render the scene while taking a snapshot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## 360CaptureOutputImageWidth

- Type: U32 | Default value: `4096` | Persisted: 1

- Comment: Width of the output 360 equirectangular image

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AFKTimeout

- Type: S32 | Default value: `300` | Persisted: 1

- Comment: 
        Time before automatically setting AFK (away from keyboard) mode (seconds, 0=never).
        Valid values are: 0, 120, 300, 600, 1800
      

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AbuseReportScreenshotDelay

- Type: F32 | Default value: `0.3` | Persisted: 1

- Comment: Time delay before taking screenshot to avoid UI artifacts.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AckCollectTime

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Ack messages collection and grouping time

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ActiveFloaterTransparency

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Transparency of active floaters (floaters that have focus)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AdminMenu

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enable the debug admin menu from the main menu.  Note: This will just allow the menu to be shown; this does not grant admin privileges.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AdvanceSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display advanced parameter settings in snaphot interface

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AgentPause

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Ask the simulator to stop updating the agent while enabled

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AlertedUnsupportedHardware

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Set if there's unsupported hardware and we've already done a notification.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AllowMultipleViewers

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow multiple viewers.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AllowSelectAvatar

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Allows user to select and move avatars, move is viewer sided, does not propagate to server, also supresses avatar position updates while avatars are selected

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AllowSelfImpostor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow own render time to impostor your avatar.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AllowTapTapHoldRun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Tapping a direction key twice and holding it down makes avatar run

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AnalyzePerformance

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Request performance analysis for a particular viewer run

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AnimateTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable texture animation (debug)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AnimatedObjectsAllowLeftClick

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow left-click interaction with animated objects. Uncertain how much performance impact this will have.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AnimatedObjectsMaxLegalOffset

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Max visual offset between object position and rendered position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AnimatedObjectsMaxLegalSize

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Max bounding box size for animated object's rendered position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AppearanceCameraMovement

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When entering appearance editing mode, camera zooms in on currently selected portion of avatar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ApplyColorImmediately

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Preview selections in color picker immediately

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ArrowKeysAlwaysMove

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: While cursor is in chat entry box, arrow keys still control your avatar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AuctionShowFence

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When auctioning land, include parcel boundary marker in snapshot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelAmbient

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of environment sounds

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelDoppler

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of the Doppler effect on moving sounds (1.0 = normal, 0 = off, higher = stronger)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelMaster

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Master audio level, or overall volume

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelMedia

- Type: F32 | Default value: `0.3` | Persisted: 1

- Comment: Audio level of parcel Media

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelMic

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Audio level of microphone input

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelMusic

- Type: F32 | Default value: `0.3` | Persisted: 1

- Comment: Audio level of streaming music

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelRolloff

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of the distance fall-off of sounds (1.0 = normal, 0 = none, higher = faster)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelSFX

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of in-world sound effects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelUI

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of UI sound effects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelUnderwaterRolloff

- Type: F32 | Default value: `5.0` | Persisted: 1

- Comment: Same as AudioLevelRolloff, while the camera is underwater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelVoice

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of voice chat

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioLevelWind

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Audio level of wind noise when standing still

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioStreamingMedia

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable streaming

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AudioStreamingMusic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable streaming audio

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoAcceptNewInventory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Automatically accept new notecards/textures/landmarks

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoDisengageMic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically turn off the microphone when ending IM calls.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoLeveling

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep Flycam level.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoLogin

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Login automatically using last username/password combination

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoMimeDiscovery

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable viewer mime type discovery of media URLs

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoPilotLocksCamera

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Keep camera position locked when avatar walks to selected position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoReplace

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Replaces keywords with a configured word or phrase

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Update snapshot when camera stops moving, or any parameter changes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoTuneFPS

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow the viewer to adjust your settings to achieve target FPS

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoTuneImpostorByDistEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable/disable using MaxNonImpostor to limit avatar rendering by distance.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoTuneImpostorFarAwayDistance

- Type: F32 | Default value: `64.0` | Persisted: 0

- Comment: Avatars beyond this range will automatically be optimized

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoTuneLock

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When enabled the viewer will dynamically change settings until auto tune is explicitly turned off.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoTuneRenderFarClipMin

- Type: F32 | Default value: `32.0` | Persisted: 0

- Comment: The lowest draw distance that auto tune is allowed to use

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutoTuneRenderFarClipTarget

- Type: F32 | Default value: `256.0` | Persisted: 0

- Comment: The draw distance that auto tune will try to achieve

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AutomaticFly

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Fly by holding jump key or using "Fly" command (FALSE = fly by using "Fly" command only)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisDeadZone0

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 0 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisDeadZone1

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 1 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisDeadZone2

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 2 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisDeadZone3

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 3 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisDeadZone4

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 4 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisDeadZone5

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Avatar axis 5 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisScale0

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 0 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisScale1

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 1 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisScale2

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 2 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisScale3

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 3 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisScale4

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 4 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarAxisScale5

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Avatar axis 5 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarBakedTextureUploadTimeout

- Type: U32 | Default value: `60` | Persisted: 1

- Comment: Specifes the maximum time in seconds to wait before sending your baked textures for avatar appearance.  Set to 0 to disable and wait until all baked textures are at highest resolution.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarExtentRefreshMaxPerBatch

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: how many avatars do we want to handle in total per batch (default is 5)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarExtentRefreshPeriodBatch

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: how many frames do we spread over by default when refreshing extents (default is 4)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarFeathering

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Avatar feathering (less is softer)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarNameTagMode

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Select Avatar Name Tag Mode

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarPhysics

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable avatar physics.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarRotateThresholdFast

- Type: F32 | Default value: `2` | Persisted: 1

- Comment: Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving fast (degrees)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarRotateThresholdSlow

- Type: F32 | Default value: `60` | Persisted: 1

- Comment: Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving slowly (degrees)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarSex

- Type: U32 | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarSitRotation

- Type: LLSD | Default value: `0 0 0 1` | Persisted: 1

- Comment: Avatar real sitting rotation used in preset

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AvatarWelcomePack

- Type: String | Default value: `https://lecs-viewer-web-components.s3.amazonaws.com/v3.0/[GRID_LOWERCASE]/vawp/index.html` | Persisted: 1

- Comment: Avatar Welcome Pack contents

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## AzureTranslateAPIKey

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Azure Translation service data to use with the MS Azure Translator API

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BackgroundYieldTime

- Type: S32 | Default value: `40` | Persisted: 1

- Comment: Amount of time to yield every frame to other applications when SL is not the foreground window (milliseconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BasicUITooltips

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show tooltips for various 2D UI elements like buttons or checkboxes, won't supress tooltips like drag'n'drop, inworld, links or media

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BatchSizeAIS3

- Type: S32 | Default value: `20` | Persisted: 1

- Comment: Amount of folder ais packs into category subset request

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BlockAvatarAppearanceMessages

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignores appearance messages (for simulating Ruth)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BlockPeopleSortOrder

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Specifies sort order for recent people (0 = by name, 1 = by type)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserEnableJSObject

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: (WARNING: Advanced feature. Use if you are aware of the implications). Enable or disable the viewer to Javascript bridge object.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserFileAccessFromFileUrls

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow access to local files via file urls in the embedded browser

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserIgnoreSSLCertErrors

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: FOR TESTING ONLY: Tell the built-in web browser to ignore SSL cert errors.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserJavascriptEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable Javascript in the built-in Web browser?

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserPluginsEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable Web plugins in the built-in Web browser?

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserProxyAddress

- Type: String | Default value: `` | Persisted: 1

- Comment: Address for the Web Proxy]

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserProxyEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Web Proxy

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BrowserProxyPort

- Type: S32 | Default value: `3128` | Persisted: 1

- Comment: Port for Web Proxy

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisDeadZone0

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 0 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisDeadZone1

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 1 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisDeadZone2

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 2 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisDeadZone3

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 3 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisDeadZone4

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 4 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisDeadZone5

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Build axis 5 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisScale0

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 0 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisScale1

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 1 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisScale2

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 2 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisScale3

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 3 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisScale4

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 4 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildAxisScale5

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Build axis 5 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuildFeathering

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Build feathering (less is softer)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects can be copied by everyone

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeAnimations

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect animations

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeBodyParts

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect body parts

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeClothing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect clothing

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeGestures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect gestures

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeMaterials

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect materials

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeNotecards

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect notecards

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeObjects

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeScripts

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect scripts

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeSettings

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect environment settings

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeSounds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect sounds

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeIncludeTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk permission changes affect textures

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk changed objects can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkChangeShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bulk changed objects are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BulkUpload2KTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Bulk upload scales textures to 2K if true, to 1K if false

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuyCurrencyAddPaymentURL

- Type: String | Default value: `https://accounts.secondlife.com/packs/floater/add-payment-enabled` | Persisted: 1

- Comment: URL the viewer probes at login; a 200 means the L$ packs floater handles residents without a payment method

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuyCurrencyHTML

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use HTML based L$ packs floater instead of legacy XUI version

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## BuyCurrencyPacksURL

- Type: String | Default value: `https://accounts.secondlife.com/packs/floater?lang=[LANGUAGE]&shortfall=[SHORTFALL]` | Persisted: 1

- Comment: URL for the L$ packs purchase floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CEFRemoteDebuggingPort

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: Enable CEF remote debugging on the specified base port (1024 to 65535, 0 to disable). Each new SLPlugin gets base+N.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CacheLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Controls the location of the local disk cache

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CacheLocationTopFolder

- Type: String | Default value: `` | Persisted: 1

- Comment: Controls the top folder location of the the local disk cache

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CacheSize

- Type: U32 | Default value: `6144` | Persisted: 1

- Comment: Controls amount of hard drive space reserved for local file caching in MB

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CacheValidateCounter

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Used to distribute cache validation

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CallLogSortOrder

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Specifies sort order for Call Log (0 = by name, 1 = by date)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraAngle

- Type: F32 | Default value: `1.047197551` | Persisted: 1

- Comment: Camera field of view angle (Radians)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraDoFResScale

- Type: F32 | Default value: `0.7` | Persisted: 1

- Comment: Amount to scale down depth of field resolution.  Valid range is 0.25 (quarter res) to 1.0 (full res)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraFNumber

- Type: F32 | Default value: `9.0` | Persisted: 1

- Comment: Camera f-number value for DoF effect

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraFieldOfView

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Vertical camera field of view for DoF effect (in degrees)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraFocalLength

- Type: F32 | Default value: `50` | Persisted: 1

- Comment: Camera focal length for DoF effect (in millimeters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraFocusTransitionTime

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: How many seconds it takes the camera to transition between focal distances

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraMaxCoF

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Maximum camera circle of confusion for DoF effect

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraMouseWheelZoom

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Camera zooms in and out with mousewheel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraOffset

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render with camera offset from view frustum (rendering debug)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraOffsetBuild

- Type: Vector3 | Default value: `-6.0 0.0 6.0` | Persisted: 1

- Comment: Default camera position relative to focus point when entering build mode

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraOffsetRearView

- Type: Vector3 | Default value: `-3.0 0.0 0.75` | Persisted: 1

- Comment: Initial camera offset from avatar in Rear View

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraOffsetScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scales the default offset

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraOpacity

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Opacity of the Camera Controls floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraPosOnLogout

- Type: Vector3D | Default value: `0.0 0.0 0.0` | Persisted: 1

- Comment: Camera position when last logged out (global coordinates)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraPositionSmoothing

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Smooths camera position over time

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraPreset

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Preset camera position - view (0 - rear, 1 - front, 2 - group)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraPresetType

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Preset camera position - view (0 - rear, 1 - front, 2 - group, 3 - custom)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CameraZoomFraction

- Type: F32 | Default value: `0.9` | Persisted: 1

- Comment: Mousewheel driven fraction of zoom

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CefVerboseLog

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable/disable CEF verbose loggingk

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CertStore

- Type: String | Default value: `default` | Persisted: 1

- Comment: Specifies the Certificate Store for certificate trust verification

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ChatAutocompleteGestures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Auto-complete gestures in nearby chat

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ChatBubbleOpacity

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Opacity of chat bubble background (0.0 = completely transparent, 1.0 = completely opaque)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ChatFontSize

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Size of chat text in chat console (0 = small, 1 = big)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ChatFullWidth

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Chat console takes up full width of SL window

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ChatLoadGroupMaxMembers

- Type: S32 | Default value: `100` | Persisted: 1

- Comment: Max number of active members we'll show up for an unresponsive group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ChatOnlineNotification

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Provide notifications for when friend log on and off of SL

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ChatServiceEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable accumulated direct-message history from Chat Service for this login.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CheesyBeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable cheesy beacon effects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ClickToWalk

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: (obsolete)Click in world to walk to location

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ClientSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Client settings file name (per install).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CloseChatOnReturn

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Close chat after hitting return

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineChannel

- Type: String | Default value: `` | Persisted: 0

- Comment: Command line specified channel name

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineDisableVoice

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disable Voice.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineGridChoice

- Type: String | Default value: `` | Persisted: 0

- Comment: The user's grid choice or ip address.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineHelperURI

- Type: String | Default value: `` | Persisted: 0

- Comment: Command line specified helper web CGI prefix to use.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineLoginLocation

- Type: String | Default value: `` | Persisted: 0

- Comment: Startup destination requested on command line

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineLoginURI

- Type: LLSD | Default value: `` | Persisted: 0

- Comment: Command line specified login server and CGI prefix to use.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineSkipUpdater

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Command line skip updater check.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CmdLineUpdateService

- Type: String | Default value: `` | Persisted: 0

- Comment: Override the url base for the update query.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CollectFontVertexBuffers

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: When enabled some UI elements with cache buffers generated by fonts and reuse them. When disabled general cahce will be used with a significant overhead for hash, but it regenerates vertices each frame so it's always up to date.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CollectUIImageVertexBuffers

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: When enabled, images will cache vertex buffers and reuse them. When disabled, the general cache will be used with significant hash-lookup overhead, but vertices are regenerated each frame so they are always up to date.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ColorSettingsHideDefault

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show non-default settings only in Color Settings list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ComplexityChangesPopUpDelay

- Type: U32 | Default value: `300` | Persisted: 1

- Comment: Delay before viewer will show avatar complexity notice again

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ConnectAsGod

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log in a god if you have god access.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ConnectionPort

- Type: U32 | Default value: `13000` | Persisted: 1

- Comment: Custom connection port number

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ConnectionPortEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use the custom connection port?

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ConsoleBackgroundOpacity

- Type: F32 | Default value: `0.700` | Persisted: 1

- Comment: Opacity of chat console (0.0 = completely transparent, 1.0 = completely opaque)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ConsoleBufferSize

- Type: S32 | Default value: `40` | Persisted: 1

- Comment: Size of chat console history (lines of chat)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ConsoleMaxLines

- Type: S32 | Default value: `40` | Persisted: 1

- Comment: Max number of lines of chat text visible in console.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ConversationSortOrder

- Type: U32 | Default value: `131073` | Persisted: 1

- Comment: Specifies sort key for conversations

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CookiesEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Accept cookies from Web sites?

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CoroutineStackSize

- Type: S32 | Default value: `524288` | Persisted: 1

- Comment: Size (in bytes) for each coroutine stack

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CrashHostUrl

- Type: String | Default value: `` | Persisted: 1

- Comment: A URL pointing to a crash report handler; overrides cluster negotiation to locate crash handler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CrashOnStartup

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: User-requested crash on viewer startup

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CreateToolCopyCenters

- Type: Boolean | Default value: `1` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CreateToolCopyRotates

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CreateToolCopySelection

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CreateToolKeepSelected

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: After using create tool, keep the create tool active

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CurlRequestTimeOut

- Type: F32 | Default value: `120.0` | Persisted: 1

- Comment: Max idle time of a curl request before killed (requires restart)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CurrentGrid

- Type: String | Default value: `` | Persisted: 1

- Comment: Currently Selected Grid

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## CurrentMapServerURL

- Type: String | Default value: `` | Persisted: 0

- Comment: Current Session World map URL

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Cursor3D

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Treat Joystick values as absolute positions (not deltas).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAnimatedObjects

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show info related to animated objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAvatarAppearanceMessage

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Dump a bunch of XML files when handling appearance messages

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAvatarAppearanceServiceURLOverride

- Type: String | Default value: `` | Persisted: 1

- Comment: URL to use for baked texture requests; overrides value returned by login server.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAvatarCompositeBaked

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Colorize avatar meshes based on baked/composite state.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAvatarExperimentalServerAppearanceUpdate

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Experiment with sending full cof_contents instead of cof_version

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAvatarJoints

- Type: String | Default value: `` | Persisted: 1

- Comment: List of joints to emit additional debugging info about.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAvatarLocalTexLoadedTime

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display time for loading avatar local textures.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugAvatarRezTime

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display times for avatars to resolve.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugBeaconLineWidth

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Size of lines for Debug Beacons

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugForceAppearanceRequestFailure

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Request wrong cof version to test the failure path for server appearance update requests.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugHideEmptySystemFolders

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Hide empty system folders when on

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugObjectLODs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show info related to lod calculations for attached or animated objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugPermissions

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log permissions for selected inventory items

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugPluginDisableTimeout

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable the code which watches for plugins that are crashed or hung

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugQualityPerformance

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Allows to change performance quality directly from debug settings.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugSelectionLODs

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: Force selection to show specific LOD, -1 for off, 0 - lowest, 4 - high.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugSession

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Request debugging for a particular viewer session

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugSettingsHideDefault

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show non-default settings only in Debug Settings list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowAvatarRenderInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show avatar render cost information

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowColor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show color under cursor

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowControllerState

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display internal controller state values

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowMemory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show Total Allocated Memory

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowRenderInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show stats about current scene

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowRenderMatrices

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display values of current view and projection matrices.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowTextureInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show inertested texture info

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowTime

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show time info

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowUploadCost

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show mesh upload cost

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugShowXUINames

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show tooltips with XUI path to widget

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimAgentMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimFrameMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimImagesMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimNetMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimPumpIOMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimScriptMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimSimOtherMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimSimPhysicsMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimSimPhysicsOtherMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimSimPhysicsShapeUpdateMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimSimPhysicsStepMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimSleepMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimSpareMsec

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugStatModeSimTotalUnackedBytes

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugViews

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display debugging info for views.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DebugWindowProc

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log windows messages

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DeepLTranslateAPIKey

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: DeepL Translation service data to use with the DeepL Translator API

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DefaultFemaleAvatar

- Type: String | Default value: `Female Shape & Outfit` | Persisted: 1

- Comment: Default Female Avatar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DefaultLoginLocation

- Type: String | Default value: `` | Persisted: 0

- Comment: Startup destination default (if not specified on command line)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DefaultMaleAvatar

- Type: String | Default value: `Male Shape & Outfit` | Persisted: 1

- Comment: Default Male Avatar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DefaultUploadPermissionsConverted

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Default upload permissions have been converted to default creation permissions

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DestinationGuideURL

- Type: String | Default value: `https://secondlife.com/destinations/whats-hot-now?ctx=viewer` | Persisted: 1

- Comment: Destination guide contents

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisableAllRenderFeatures

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disables all rendering features.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisableAllRenderTypes

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disables all rendering types.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisableCameraConstraints

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable the normal bounds put on the camera by avatar position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisableCrashLogger

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Do not send crash report to Linden server

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisableExternalBrowser

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable opening an external browser.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisableLookAtAnimation

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Avatar follows cursor with avatars eyes, when disabled, avatar will look forward

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisableTextHyperlinkActions

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable highlighting and linking of URLs in XUI text boxes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DiskCacheDirName

- Type: String | Default value: `cache` | Persisted: 1

- Comment: The name of the disk cache (within the standard Viewer disk cache directory)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DiskCachePercentOfTotal

- Type: F32 | Default value: `35.0` | Persisted: 1

- Comment: The percent of total cache size (defined by CacheSize) to use for the disk cache (ex: asset storage, excludes textures)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DiskCacheVersion

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Version number of disk cache

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DisplayTimecode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display timecode on screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Disregard128DefaultDrawDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to use the auto default to 128 draw distance

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Disregard96DefaultDrawDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to use the auto default to 96 draw distance

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DoubleClickAutoPilot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Obsolete)Enable double-click auto pilot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DoubleClickShowWorldMap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable double-click to show world map from mini map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DoubleClickTeleport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable double-click to teleport where allowed (afects minimap and people panel)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## DynamicCameraStrength

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Amount camera lags behind avatar motion (0 = none, 30 = avatar velocity)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EditCameraMovement

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When entering build mode, camera moves up above avatar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EditLinkedParts

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Select individual parts of linked objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EffectScriptChatParticles

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: 1 = normal behavior, 0 = disable display of swirling lights when scripts communicate

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EmulateCoreCount

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: For debugging -- number of cores to restrict the main process to, or 0 for no limit.  Requires restart.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableAltZoom

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use Alt+mouse to look at and zoom in on objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableAppearance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable opening appearance from web link

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableAvatarPay

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable paying other avatars from web link

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableAvatarShare

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable sharing from web link

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableButtonFlashing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow UI to flash buttons to get your attention

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableClassifieds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable creation of new classified ads from web link

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableCollisionSounds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Play sounds on collision

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableDiscord

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: When set, connect to Discord to enable Rich Presence

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableDiskCacheDebugInfo

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When set, display additional cache debugging information

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableGestureSounds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Play sounds from gestures

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableGrab

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use Ctrl+mouse to grab and manipulate objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableGroupChatPopups

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable Incoming Group Chat Popups

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable opening inventory from web link

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableLookAtTarget

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to animate the avatar head and send look at targets when moving the cursor or focusing on objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableMouselook

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow first person perspective and mouse control of camera

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnablePlaceProfile

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable viewing of place profile from web link

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableSelectionHints

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to send editing hints to animate the arm when editing an object.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableUIHints

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Toggles UI hint popups

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableVisualLeakDetector

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: EnableVisualLeakDetector

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnableVoiceChat

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable talking to other residents with a microphone

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EnvironmentPersistAcrossLogin

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Keep Environment settings consistent across sessions

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EventURL

- Type: String | Default value: `https://events.[GRID]/viewer/embed/event/[EVENT_ID]` | Persisted: 0

- Comment: URL for Event website, displayed in the event floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## EveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Everyone can copy the newly created objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ExternalEditor

- Type: String | Default value: `` | Persisted: 1

- Comment: Path to program used to edit LSL scripts and XUI files, e.g.: /usr/bin/gedit --new-window "%s"

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ExternalEditorTightIntegration

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When true, Edit in External Editor launches VS Code via the code CLI with a vscode:// URI instead of using the configured external editor.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ExternalWebsocketForwardDebug

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Forward messages and runtime errors for a script to JSONRPC client.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ExternalWebsocketSyncEnable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the Websocket JSONRPC server when doing external script editing.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ExternalWebsocketSyncLocal

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Should the JSONRPC server listen only for local connections.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ExternalWebsocketSyncPort

- Type: S32 | Default value: `9020` | Persisted: 1

- Comment: Port that the JSONRPC server listens on when editing

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FMODExDecodeBufferSize

- Type: U32 | Default value: `1000` | Persisted: 1

- Comment: Sets the streaming decode buffer size (in milliseconds) for FMOD Ex or FMOD Studio

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FMODExProfilerEnable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable profiler tool if using FMOD Ex or FMOD Studio

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FakeInitialOutfitName

- Type: String | Default value: `` | Persisted: 1

- Comment: Pretend that this is first time login and specified name was chosen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FindLandArea

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables filtering of land search results by area

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FindLandPrice

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables filtering of land search results by price

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FindOriginalOpenWindow

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sets the action for 'Find original' and 'Show in Inventory' (0 - shows item in main Inventory, 1 - opens a new single-folder window)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FirstLoginThisInstall

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Specifies that you have not logged in with the viewer since you performed a clean install

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FirstName

- Type: String | Default value: `` | Persisted: 1

- Comment: Login first name

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FirstPersonAvatarVisible

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display avatar and attachments below neck while in mouselook

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FirstRunThisInstall

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Specifies that you have not run the viewer since you performed a clean install

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FirstSelectedDisabledPopups

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Return false if there is not disabled popup selected in the list of floater preferences popups

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FirstSelectedEnabledPopups

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Return false if there is not enable popup selected in the list of floater preferences popups

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FixedWeather

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Weather effects do not change over time

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlashCount

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Number of flashes of item. Requires restart.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlashPeriod

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Period at which item flash (seconds). Requires restart.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterActiveSpeakersSortAscending

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to sort up or down

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterActiveSpeakersSortColumn

- Type: String | Default value: `speaking_status` | Persisted: 1

- Comment: Column name to sort on

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapEast

- Type: String | Default value: `E` | Persisted: 1

- Comment: Floater Map East Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapNorth

- Type: String | Default value: `N` | Persisted: 1

- Comment: Floater Map North Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapNorthEast

- Type: String | Default value: `NE` | Persisted: 1

- Comment: Floater Map North-East Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapNorthWest

- Type: String | Default value: `NW` | Persisted: 1

- Comment: Floater Map North-West Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapSouth

- Type: String | Default value: `S` | Persisted: 1

- Comment: Floater Map South Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapSouthEast

- Type: String | Default value: `SE` | Persisted: 1

- Comment: Floater Map South-East Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapSouthWest

- Type: String | Default value: `SW` | Persisted: 1

- Comment: Floater Map South-West Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterMapWest

- Type: String | Default value: `W` | Persisted: 1

- Comment: Floater Map West Label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FloaterStatisticsRect

- Type: Rect | Default value: `0 400 250 0` | Persisted: 1

- Comment: Rectangle for chat history

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAbsolute

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Treat Flycam values as absolute positions (not deltas).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisDeadZone0

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 0 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisDeadZone1

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 1 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisDeadZone2

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 2 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisDeadZone3

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 3 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisDeadZone4

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 4 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisDeadZone5

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 5 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisDeadZone6

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Flycam axis 6 dead zone.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisScale0

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Flycam axis 0 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisScale1

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Flycam axis 1 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisScale2

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Flycam axis 2 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisScale3

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Flycam axis 3 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisScale4

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Flycam axis 4 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisScale5

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Flycam axis 5 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamAxisScale6

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Flycam axis 6 scaler.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamBuildModeScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale factor to apply to flycam movements when in build mode.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlycamFeathering

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Flycam feathering (less is softer)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FlyingAtExit

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Was flying when last logged out, so fly when logging in

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FocusOffsetRearView

- Type: Vector3D | Default value: `1.0 0.0 1.0` | Persisted: 1

- Comment: Initial focus point offset relative to avatar for the camera preset Rear View (x-axis is forward)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FocusPosOnLogout

- Type: Vector3D | Default value: `0.0 0.0 0.0` | Persisted: 1

- Comment: Camera focus point when last logged out (global coordinates)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FolderAutoOpenDelay

- Type: F32 | Default value: `0.75` | Persisted: 1

- Comment: Seconds before automatically expanding the folder under the mouse when performing inventory drag and drop

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FontScreenDPI

- Type: F32 | Default value: `96.0` | Persisted: 1

- Comment: Font resolution, higher is bigger (pixels per inch)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ForceAddressSize

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Force Windows update to 32-bit or 64-bit viewer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ForceAssetFail

- Type: U32 | Default value: `255` | Persisted: 1

- Comment: Force wearable fetches to fail for this asset type.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ForceLoginURL

- Type: String | Default value: `` | Persisted: 1

- Comment: Force a specified URL for login page content - used if exists

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ForceShowGrid

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Always show grid dropdown on login screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FreezeTime

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FriendsListHideUsernames

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show both Display name and Username in Friend list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FriendsListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide online and all friends icons in the friend list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FriendsListShowPermissions

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide permission icons in the friend list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FriendsSortOrder

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Specifies sort order for friends (0 = by name, 1 = by online status)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FullScreen

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Run a fullscreen session. MacOS not supported

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FullScreenAspectRatio

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Aspect ratio of fullscreen display (width / height)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## FullScreenAutoDetectAspectRatio

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Automatically detect proper aspect ratio for fullscreen display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GLTFEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enable GLTF support.  Set to true by simulator if the simulator you are connected to supports GLTF Asset upload.  WARNING: Manually setting this to true will enable buttons that can drain your L$ balance by implicitly uploading textures without asking.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GameControl

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Game controller settings: global per-mode action mappings plus per-device hardware config. Empty means use built-in defaults.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GenericErrorPageURL

- Type: String | Default value: `https://common-flash-secondlife-com.s3.amazonaws.com/viewer/v2.6/agni/404.html` | Persisted: 1

- Comment: URL to set as a property on LLMediaControl to navigate to if the a page completes with a 400-499 HTTP status code

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GesturesEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created gesture

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GesturesMarketplaceURL

- Type: String | Default value: `https://marketplace.secondlife.com/products/search?search[category_id]=200&search[maturity][]=General&search[page]=1&search[per_page]=12` | Persisted: 0

- Comment: URL to the Gestures Marketplace

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GesturesNextOwnerCopy

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created gestures can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GesturesNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created gestures can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GesturesNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created gestures can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GesturesShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created gestures are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GoogleTranslateAPIKey

- Type: String | Default value: `` | Persisted: 1

- Comment: Google Translate API key

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridCrossSections

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Highlight cross sections of prims with grid manipulation plane.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridDrawSize

- Type: F32 | Default value: `12.0` | Persisted: 1

- Comment: Visible extent of 2D snap grid (meters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridMode

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Snap grid reference frame (0 = world, 1 = local, 2 = reference object)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridOpacity

- Type: F32 | Default value: `0.699999988079` | Persisted: 1

- Comment: Grid line opacity (0.0 = completely transparent, 1.0 = completely opaque)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridResolution

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Size of single grid step (meters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridStatusFloaterRect

- Type: Rect | Default value: `0 520 625 0` | Persisted: 1

- Comment: Web profile floater dimensions

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridStatusRSS

- Type: String | Default value: `https://status.secondlifegrid.net/history.atom` | Persisted: 1

- Comment: URL that points to SL Grid Status RSS

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridStatusUpdateDelay

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Timer delay for updating Grid Status RSS.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridSubUnit

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display fractional grid steps, relative to grid size

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GridSubdivision

- Type: S32 | Default value: `32` | Persisted: 1

- Comment: Maximum number of times to divide single snap grid unit when GridSubUnit is true

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GroupListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide group icons in the group list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GroupMembersSortOrder

- Type: String | Default value: `name` | Persisted: 1

- Comment: The order by which group members will be sorted (name|donated|online)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## GroupTitlesTagMode

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Select Group Titles tag mode: 0 - no group tags, 1 - only my group tag, 2 - all group tags

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HUDScaleFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of HUD attachments

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HeadlessClient

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Run in headless mode by disabling GL rendering, keyboard, etc

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HeightUnits

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Determines which metric units are used: 1(TRUE) for meter and 0(FALSE) for foot.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HelpFloaterOpen

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show Help Floater on login?

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HelpURLFormat

- Type: String | Default value: `https://viewer-help.secondlife.com/[LANGUAGE]/[CHANNEL]/[VERSION]/[TOPIC][DEBUG_MODE]` | Persisted: 1

- Comment: URL pattern for help page; arguments will be encoded; see llviewerhelp.cpp:buildHelpURL for arguments

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HideSelectedObjects

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Hide Selected Objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HideUIControls

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Hide all menu items and buttons

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HighResSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Double resolution of snapshot from current window resolution

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HomeSidePanelURL

- Type: String | Default value: `https://viewer-sidebar.secondlife.com/sidebar.html?p=[AUTH_TOKEN]&lang=[LANGUAGE]&channel=[CHANNEL]&version=[VERSION]&major=[VERSION_MAJOR]&minor=[VERSION_MINOR]&patch=[VERSION_PATCH]&build=[VERSION_BUILD]&firstlogin=[FIRST_LOGIN]` | Persisted: 1

- Comment: URL for the web page to display in the Home side panel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HostID

- Type: String | Default value: `` | Persisted: 0

- Comment: Machine identifier for hosted Second Life instances

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HoverHeightAffectsCamera

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Camera view is affected by Hover Height setting

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HttpPipelining

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If true, viewer will attempt to pipeline HTTP requests.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HttpProxyType

- Type: String | Default value: `Socks` | Persisted: 1

- Comment: Proxy type to use for HTTP operations

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## HttpRangeRequestsDisable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, viewer will not issue GET requests with 'Range:' headers for meshes and textures.  May resolve problems with certain ISPs and networking gear.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IMShowControlPanel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show IM Control Panel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IMShowNamesForP2PConv

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable(disable) showing of a names in the chat.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IMShowTime

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable(disable) timestamp showing in the chat.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IgnoreAllNotifications

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore all notifications so we never need user input on them.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IgnoreFOVZoomForLODs

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore zoom effect(CTRL+0) when calculating lods.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IgnorePixelDepth

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ignore pixel depth settings.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ImagePipelineUseHTTP

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If TRUE use HTTP GET to fetch textures from the server

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ImporterDebugMode

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: At 0 does nothing, at 1 dumps skinning data near orifinal file, at 2 dumps skining data and positions/weights of first 5 models, at 3 dumps skinning data and models as llsd

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ImporterDebugVerboseLogging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable debug output to more precisely identify sources of import errors. Warning: the output can slow down import on many machines.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ImporterLegacyMatching

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable index based model matching.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ImporterModelLimit

- Type: U32 | Default value: `768` | Persisted: 1

- Comment: Limits amount of importer generated (when over 8 faces) models for dae and gltf files

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ImporterPreprocessDAE

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable preprocessing for DAE files to fix some ColladaDOM related problems (like support for space characters within names and ids).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InBandwidth

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Incoming bandwidth throttle (bps)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InactiveFloaterTransparency

- Type: F32 | Default value: `0.95` | Persisted: 1

- Comment: Transparency of inactive floaters (floaters that have no focus)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IndirectMaxComplexity

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: Controls RenderAvatarMaxComplexity in a non-linear fashion (do
      not set this value)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## IndirectMaxNonImpostors

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: Controls RenderAvatarMaxNonImpostors in a non-linear fashion (do
      not set this value)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InstallLanguage

- Type: String | Default value: `default` | Persisted: 1

- Comment: Language passed from installer (for UI)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InterpolationPhaseOut

- Type: F32 | Default value: `1` | Persisted: 1

- Comment: Seconds to phase out interpolated motion

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InterpolationTime

- Type: F32 | Default value: `3` | Persisted: 1

- Comment: How long to extrapolate object motion after last packet received

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryAddAttachmentBehavior

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Defines behavior when hitting return on an inventory item

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryAutoOpenDelay

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Seconds before automatically opening inventory when mouse is over inventory button when performing inventory drag and drop

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryDebugSimulateLateOpRate

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rate at which we simulate late-completing copy/link requests in some operations

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryDebugSimulateOpFailureRate

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rate at which we simulate failures of copy/link requests in some operations

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryDisplayInbox

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Override received items inventory inbox display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryExposeFolderID

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Allows copying folder id from context menu

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryFavoritesColorText

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: render favorite items using InventoryFavoriteText as color

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryFavoritesUseHollowStar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show star near folders that contain favorites

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryFavoritesUseStar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show star near favorited items in inventory

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryLinking

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable ability to create links to folders and items via "Paste as link".

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryOutboxLogging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable debug output associated with the Merchant Outbox.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryOutboxMakeVisible

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable making the Merchant Outbox and Inbox visible in the inventory for debug purposes.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryOutboxMaxFolderCount

- Type: U32 | Default value: `20` | Persisted: 0

- Comment: Maximum number of subfolders allowed in a listing in the merchant outbox.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryOutboxMaxFolderDepth

- Type: U32 | Default value: `4` | Persisted: 0

- Comment: Maximum number of nested levels of subfolders allowed in a listing in the merchant outbox.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryOutboxMaxItemCount

- Type: U32 | Default value: `200` | Persisted: 0

- Comment: Maximum number of items allowed in a listing in the merchant outbox.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryOutboxMaxStockItemCount

- Type: U32 | Default value: `200` | Persisted: 0

- Comment: Maximum number of items allowed in a stock folder.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryShowFavoritesTab

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide Favorites tab in the Inventory floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryShowRecentTab

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide Recent tab in the Inventory floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryShowWornTab

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide Worn tab in the Inventory floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventorySortOrder

- Type: U32 | Default value: `7` | Persisted: 1

- Comment: Specifies sort key for inventory items (+0 = name, +1 = date, +2 = folders always by name, +4 = system folders to top)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InventoryTrashMaxCapacity

- Type: U32 | Default value: `5000` | Persisted: 1

- Comment: Maximum capacity of the Trash folder. User will be offered to clean it up when exceeded.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## InvertMouse

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When in mouselook, moving mouse up looks down and vice verse (FALSE = moving up looks up)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoinFloaterOverlayOpacity

- Type: F32 | Default value: `0.8` | Persisted: 1

- Comment: Opacity of the screen darkening overlay behind the Join floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoinURL

- Type: String | Default value: `https://join.secondlife.com/` | Persisted: 1

- Comment: URL opened in the Join floater on the login screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAvatarEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables the Joystick to control Avatar movement.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAxis0

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 0 ([0, 5]).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAxis1

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 1 ([0, 5]).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAxis2

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 2 ([0, 5]).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAxis3

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 3 ([0, 5]).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAxis4

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 4 ([0, 5]).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAxis5

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 5 ([0, 5]).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickAxis6

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Flycam hardware axis mapping for internal axis 6 ([0, 5]).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickBuildEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables the Joystick to move edited objects.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickDeviceUUID

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: Preffered device ID.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables Joystick Input.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickFlycamEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Enables the Joystick to control the flycam.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickInitialized

- Type: String | Default value: `` | Persisted: 1

- Comment: Whether or not a joystick has been detected and initiailized.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickMouselookYaw

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pass joystick yaw to scripts in Mouselook.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## JoystickRunThreshold

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Input threshold to initiate running

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Jpeg2000AdvancedCompression

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use advanced Jpeg2000 compression options (precincts, blocks, ordering, markers)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Jpeg2000BlocksSize

- Type: S32 | Default value: `64` | Persisted: 1

- Comment: Size of encoding blocks. Assumed square and same for all levels. Must be power of 2. Max 64, Min 4.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Jpeg2000PrecinctsSize

- Type: S32 | Default value: `256` | Persisted: 1

- Comment: Size of image precincts. Assumed square and same for all levels. Must be power of 2.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## KeepAspectForSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use full window when taking snapshot, regardless of requested image size

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## KeepAutoTuneLock

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: When enabled the AutoTuneLock will be maintainted all following sessions.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LSLFindCaseInsensitivity

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use case insensitivity when searching in LSL editor

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LSLFontSizeName

- Type: String | Default value: `Monospace` | Persisted: 1

- Comment: Text font size in LSL editor

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LSLHelpURL

- Type: String | Default value: `https://wiki.secondlife.com/wiki/[LSL_STRING]` | Persisted: 1

- Comment: URL that points to LSL help files, with [LSL_STRING] corresponding to the referenced LSL function or keyword

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LagMeterShrunk

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Last large/small state for lag meter

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LandBrushForce

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Multiplier for land modification brush force.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LandBrushSize

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Size of affected region when using teraform tool

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LandmarksSortedByDate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Reflects landmarks panel sorting order.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Language

- Type: String | Default value: `default` | Persisted: 1

- Comment: Language specifier (for UI)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LanguageIsPublic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Let other residents see our language information

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastAppearanceTab

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected tab in appearance floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastFeatureVersion

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: [DO NOT MODIFY] Feature Table Version number for tracking rendering system changes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastFindPanel

- Type: String | Default value: `find_all_panel` | Persisted: 1

- Comment: Controls which find operation appears by default when clicking "Find" button 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastGPUString

- Type: String | Default value: `` | Persisted: 1

- Comment: [DO NOT MODIFY] previous GPU id string for tracking hardware changes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastMediaSettingsTab

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected tab in media settings window

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastName

- Type: String | Default value: `` | Persisted: 1

- Comment: Login last name

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastPrefTab

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected tab in preferences window

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastRunVersion

- Type: String | Default value: `0.0.0` | Persisted: 1

- Comment: Version number of last instance of the viewer that you ran

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LastUIFeatureVersion

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: UI Feature Version number for tracking feature notification between viewer builds

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LeapCommand

- Type: LLSD | Default value: `` | Persisted: 0

- Comment: Zero or more command lines to run LLSD Event API Plugin programs.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LeapPlaybackEventsCommand

- Type: LLSD | Default value: `` | Persisted: 0

- Comment: Command line to use leap to launch playback of event recordings

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LeaveMouselook

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Exit Mouselook mode via S or Down Arrow keys while sitting 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LetterKeysFocusChatBar

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: When printable characters keys (possibly with Shift held) are pressed, the chatbar takes focus

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LimitDragDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Limit translation of object via translate tool

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LimitLookAtTarget

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to clamp the look at targets around the avatar head before sending

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LimitLookAtTargetDistance

- Type: F32 | Default value: `2` | Persisted: 1

- Comment: Distance to limit look at target to

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LimitSelectDistance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Disallow selection of objects beyond max select distance

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LinkReplaceBatchPauseTime

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: The time in seconds between two batches in a link replace operation

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LinkReplaceBatchSize

- Type: U32 | Default value: `25` | Persisted: 1

- Comment: The maximum size of a batch in a link replace operation

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LipSyncAah

- Type: String | Default value: `257998776531013446642343` | Persisted: 1

- Comment: Aah (jaw opening) babble loop

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LipSyncAahPowerTransfer

- Type: String | Default value: `0000123456789` | Persisted: 1

- Comment: Transfer curve for Voice Interface power to aah lip sync amplitude

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LipSyncEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: 0 disable lip-sync, 1 enable babble loop

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LipSyncOoh

- Type: String | Default value: `1247898743223344444443200000` | Persisted: 1

- Comment: Ooh (mouth width) babble loop

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LipSyncOohAahRate

- Type: F32 | Default value: `24.0` | Persisted: 1

- Comment: Rate to babble Ooh and Aah (/sec)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LipSyncOohPowerTransfer

- Type: String | Default value: `0012345566778899` | Persisted: 1

- Comment: Transfer curve for Voice Interface power to ooh lip sync amplitude

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalCacheVersion

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Version number of cache

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalFileSystemBrowsingEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable/disable access to the local file system via the file picker

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainAsset1

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainAsset2

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainAsset3

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainAsset4

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 0

- Comment: If set to a non-null UUID, overrides the terrain asset locally for all regions with material assets. Local terrain assets are not visible to others. Please keep in mind that this debug setting may be temporary. Do not rely on this setting existing in future viewer builds.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainPaintEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enables local paintmap if LocalTerrainAsset1, etc are set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform1OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform1OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform1Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform1ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform1ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset1 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform2OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform2OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform2Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform2ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform2ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset2 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform3OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform3OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform3Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform3ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform3ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset3 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform4OffsetU

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform4OffsetV

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform4Rotation

- Type: F32 | Default value: `0.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform4ScaleU

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LocalTerrainTransform4ScaleV

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: KHR texture transform component if LocalTerrainAsset4 is set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogInventoryDecline

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Log in system chat whenever an inventory offer is declined

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogMessages

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log network traffic

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogMetrics

- Type: String | Default value: `` | Persisted: 0

- Comment: Log viewer metrics

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogPerformance

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Log performance analysis for a particular viewer run

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogTextureDownloadsToSimulator

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Send a digest of texture info to the sim

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogTextureDownloadsToViewerLog

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Send texture download details to the viewer log

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogTextureNetworkTraffic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log network traffic for textures

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LogWearableAssetSave

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Save copy of saved wearables to log dir

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LoginContentVersion

- Type: String | Default value: `2` | Persisted: 0

- Comment: Version of login page web based content to display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LoginLocation

- Type: String | Default value: `last` | Persisted: 1

- Comment: Default Login location ('last', 'home') preference

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LoginPage

- Type: String | Default value: `` | Persisted: 1

- Comment: Login authentication page.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LoginSRVTimeout

- Type: F32 | Default value: `90.0` | Persisted: 0

- Comment: Duration in seconds of the login SRV request timeout

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## LosslessJ2CUpload

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use lossless compression for small image uploads

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MFAHash

- Type: String | Default value: `` | Persisted: 0

- Comment: Override MFA state hash for authentication

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MainWorkTime

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Max time per frame devoted to mainloop work queue (in milliseconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MainloopTimeoutDefault

- Type: F32 | Default value: `120.0` | Persisted: 1

- Comment: Timeout duration for mainloop lock detection during teleports, login and logout, in seconds.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MainloopTimeoutStarted

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Timeout duration for mainloop lock detection when logged in and not teleporting, in seconds.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapScale

- Type: F32 | Default value: `128.0` | Persisted: 1

- Comment: World map zoom level (pixels per region)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapServerURL

- Type: String | Default value: `https://map.secondlife.com/` | Persisted: 0

- Comment: World map URL template for locating map tiles

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapShowEvents

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show events on world map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapShowGridCoords

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows/hides the grid coordinates of each region on the world map.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapShowInfohubs

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show infohubs on the world map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapShowLandForSale

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show land for sale on world map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapShowPeople

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show other users on world map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MapShowTelehubs

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show telehubs on world map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Marker

- Type: String | Default value: `` | Persisted: 1

- Comment: [NOT USED]

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceListingsLogging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable debug output associated with the Marketplace Listings (SLM) API.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceListingsSortOrder

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Specifies sort for marketplace listings

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL

- Type: String | Default value: `https://marketplace.secondlife.com/` | Persisted: 0

- Comment: URL to the Marketplace

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_bodypartFemale

- Type: String | Default value: `https://marketplace.secondlife.com/` | Persisted: 0

- Comment: URL to the Marketplace Bodyparts Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_bodypartMale

- Type: String | Default value: `https://marketplace.secondlife.com/` | Persisted: 0

- Comment: URL to the Marketplace Bodyparts Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_clothingFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/clothing_female_avatar` | Persisted: 0

- Comment: URL to the Marketplace Clothing Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_clothingMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/clothing_male_avatar` | Persisted: 0

- Comment: URL to the Marketplace Clothing Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_eyesFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_eyes` | Persisted: 0

- Comment: URL to the Marketplace Eyes Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_eyesMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_eyes` | Persisted: 0

- Comment: URL to the Marketplace Eyes Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_glovesFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/gloves_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Gloves Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_glovesMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/gloves_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Gloves Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_hairFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_hair` | Persisted: 0

- Comment: URL to the Marketplace Hair Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_hairMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_hair` | Persisted: 0

- Comment: URL to the Marketplace Hair Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_jacketFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/jacket_womens` | Persisted: 0

- Comment: URL to the Marketplace Jacket Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_jacketMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/jacket_mens` | Persisted: 0

- Comment: URL to the Marketplace Jacket Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_objectFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/attachments` | Persisted: 0

- Comment: URL to the Marketplace Attachments Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_objectMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/attachments` | Persisted: 0

- Comment: URL to the Marketplace Attachments Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_pantsFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/pants_women` | Persisted: 0

- Comment: URL to the Marketplace Pants Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_pantsMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/pants_men` | Persisted: 0

- Comment: URL to the Marketplace Pants Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_shapeFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_shape` | Persisted: 0

- Comment: URL to the Marketplace Shape Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_shapeMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_shape` | Persisted: 0

- Comment: URL to the Marketplace Shape Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_shirtFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shirt_womens` | Persisted: 0

- Comment: URL to the Marketplace Shirt Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_shirtMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shirt_mens` | Persisted: 0

- Comment: URL to the Marketplace Shirt Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_shoesFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shoes_women` | Persisted: 0

- Comment: URL to the Marketplace Shoes Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_shoesMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/shoes_men` | Persisted: 0

- Comment: URL to the Marketplace Shoes Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_skinFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/womens_skin` | Persisted: 0

- Comment: URL to the Marketplace Skin Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_skinMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/mens_skin` | Persisted: 0

- Comment: URL to the Marketplace Skins Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_skirtFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/skirts_women` | Persisted: 0

- Comment: URL to the Marketplace Skirt Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_skirtMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/skirts_women` | Persisted: 0

- Comment: URL to the Marketplace Skirt Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_socksFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/socks_women` | Persisted: 0

- Comment: URL to the Marketplace Socks Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_socksMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/socks_women` | Persisted: 0

- Comment: URL to the Marketplace Socks Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_tattooFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/tattoo_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Tattoo Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_tattooMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/tattoo_both_women_and_men` | Persisted: 0

- Comment: URL to the Marketplace Tattoo Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_underpantsFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/underwear_women` | Persisted: 0

- Comment: URL to the Marketplace Underwear Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_underpantsMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/underwear_men` | Persisted: 0

- Comment: URL to the Marketplace Underwear Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_undershirtFemale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/undershirt_womens` | Persisted: 0

- Comment: URL to the Marketplace Undershirt Female

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MarketplaceURL_undershirtMale

- Type: String | Default value: `https://marketplace.secondlife.com/trampoline/viewer21/undershirt_mens` | Persisted: 0

- Comment: URL to the Marketplace Undershirt Male

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaterialsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created GLTF material

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaterialsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created GLTF material can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaterialsNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created GLTF material can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaterialsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created GLTF material can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaterialsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created GLTF materials are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxAttachmentComplexity

- Type: F32 | Default value: `1.0E6` | Persisted: 1

- Comment: Attachment's render weight limit

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxDragDistance

- Type: F32 | Default value: `48.0` | Persisted: 1

- Comment: Maximum allowed translation distance in a single operation of translate tool (meters from start point)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxFPS

- Type: F32 | Default value: `-1.0` | Persisted: 1

- Comment: OBSOLETE UNUSED setting.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxHeapSize

- Type: F32 | Default value: `1.6` | Persisted: 1

- Comment: Maximum heap size on 32-bit builds (GB)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxHeapSize64

- Type: F32 | Default value: `16.0` | Persisted: 1

- Comment: Maximum heap size on 64-bit builds (GB)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxPersistentNotifications

- Type: S32 | Default value: `250` | Persisted: 1

- Comment: Maximum amount of persistent notifications

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxSelectDistance

- Type: F32 | Default value: `128.0` | Persisted: 1

- Comment: Maximum allowed selection distance (meters from avatar)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MaxWearableWaitTime

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Max seconds to wait for wearable assets to fetch.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MePanelOpened

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Indicates that Me Panel was opened at least once after Viewer was installed

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaAutoPlayHuds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically play HUD media

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaControlFadeTime

- Type: F32 | Default value: `1.5` | Persisted: 1

- Comment: Amount of time (in seconds) that the media control fades

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaControlTimeout

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Amount of time (in seconds) for media controls to fade with no mouse activity

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaEnablePopups

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, enable targeted links and javascript in media to open new media browser windows without a prompt.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaFirstClickInteract

- Type: S32 | Default value: `31` | Persisted: 1

- Comment: This setting controls which media (once loaded) does not require a first click to focus before interaction can begin. This allows clicks to be passed directly to media bypassing the focus click requirement. This setting is a bitfield, precomputed values are as follows: Disabled=0; Worn HUDs only=1; Owned objects=2; Friend objects=4; Group objects=8; Landowner objects=16; Any object=32767; All MOAP=32768. For complete details see lltoolpie.h enum MediaFirstClickTypes.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaOnAPrimUI

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show the "link sharing" UI

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaPerformanceManagerDebug

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to show debug data for the media performance manager in the nearby media list.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaPluginDebugging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Turn on debugging messages that may help diagnosing media issues (WARNING: May reduce performance).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaPluginForceVLC

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Force use of VLC based media plugin. (Linux Only)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaPluginPipeWireVolumeCatcher

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use PipeWire instead of PulseAudio for controlling web media volume.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaRollOffMax

- Type: F32 | Default value: `80.0` | Persisted: 1

- Comment: Distance at which media volume is set to 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaRollOffMin

- Type: F32 | Default value: `40.0` | Persisted: 1

- Comment: Adjusts the distance at which media attentuation starts

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaRollOffRate

- Type: F32 | Default value: `0.02` | Persisted: 1

- Comment: Multiplier to change rate of media attenuation

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaShowOnOthers

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to show media on other avatars

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaShowOutsideParcel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show media from outside the current parcel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaShowWithinParcel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show media within the current parcel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaSoundsEarLocation

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Location of the virtual ear for media and sounds

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MediaTentativeAutoPlay

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: This is a tentative flag that may be temporarily set off by the user, until she teleports

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MemoryFailurePreventionEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If set, the viewer will quit to avoid crash when memory failure happens

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MemoryLogFrequency

- Type: F32 | Default value: `600.0` | Persisted: 1

- Comment: Seconds between display of Memory in log (0 for never)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MemoryPrivatePoolEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Enable the private memory pool management

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MemoryPrivatePoolSize

- Type: U32 | Default value: `512` | Persisted: 1

- Comment: (Deprecated) Size of the private memory pool in MB (min. value is 256)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MenuAccessKeyTime

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Time (seconds) in which the menu key must be tapped to move focus to the menu bar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MenuSearch

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide 'Search menus' field

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Mesh2MaxConcurrentRequests

- Type: U32 | Default value: `8` | Persisted: 1

- Comment: Number of connections to use for loading meshes.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshBytesPerTriangle

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Approximation of bytes per triangle to use for determining mesh streaming cost.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expose UI for mesh functionality (may require restart to take effect).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshImportUseSLM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use cached copy of last upload for a dae if available instead of loading dae file from scratch.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshMaxConcurrentRequests

- Type: U32 | Default value: `32` | Persisted: 1

- Comment: Number of connections to use for loading meshes (legacy system).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshMetaDataDiscount

- Type: U32 | Default value: `384` | Persisted: 1

- Comment: Number of bytes to deduct for metadata when determining streaming cost.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshMinimumByteSize

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Minimum number of bytes per LoD block when determining streaming cost.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshTriangleBudget

- Type: U32 | Default value: `250000` | Persisted: 1

- Comment: Target visible triangle budget to use when estimating streaming cost.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshUploadFakeErrors

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Force upload errors (for testing)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshUploadLogXML

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Verbose XML logging on mesh upload

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshUploadTimeOut

- Type: S32 | Default value: `600` | Persisted: 1

- Comment: Maximum time in seconds for llcurl to execute a mesh uoloading request

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshUseGetMesh1

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, use the legacy GetMesh capability for mesh download requests.  Semi-dynamic (read at region crossings).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MeshUseHttpRetryAfter

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If TRUE, use Retry-After response headers when rescheduling a mesh request that fails with an HTTP 503 status.  Static.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MigrateCacheDirectory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Check for old version of disk cache to migrate to current location

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MinObjectsForUnlinkConfirm

- Type: S32 | Default value: `6` | Persisted: 1

- Comment: Minimum amount of objects in linkset for showing confirmation dialog

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MinWindowHeight

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: SL viewer minimum window height in pixels

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MinWindowWidth

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: SL viewer minimum window width in pixels

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MiniMapAutoCenter

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Center the focal point of the minimap.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MiniMapPrimMaxRadius

- Type: F32 | Default value: `256.0` | Persisted: 1

- Comment: Radius of the largest prim to show on the MiniMap. Increasing beyond 256 may cause client lag.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MiniMapRotate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Rotate miniature world map to avatar direction

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MiniMapScale

- Type: F32 | Default value: `128.0` | Persisted: 1

- Comment: Miniature world map zoom level (pixels per region)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MiniMapShowPropertyLines

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not to show parcel borders on the MiniMap.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MouseMoon

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MouseSensitivity

- Type: F32 | Default value: `3.0` | Persisted: 1

- Comment: Controls responsiveness of mouse when in mouselook mode (fraction or multiple of default mouse sensitivity)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MouseSmooth

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Smooths out motion of mouse when in mouselook mode.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MouseSun

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MouseWarpMode

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Controls warping of the mouse to the center of the screen during alt-zoom and mouse look. Useful with certain input devices, mouse sharing programs like Synergy, or running under Parallels. 0 - automatic, 1 - on, 2 - off

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MultiModeDoubleClickFolder

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Sets the action for Double-click on folder in multi-folder view (0 - expands and collapses folder, 1 - opens a new window, 2 – stays in current floater but switches to SFV)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteAmbient

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Ambient sound effects, such as wind noise, play at 0 volume

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteAudio

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: All audio plays at 0 volume (streaming audio still takes up bandwidth, for example)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteListLimit

- Type: S32 | Default value: `1000` | Persisted: 1

- Comment: Maximum number of entries in the mute list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteMedia

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Media plays at 0 volume (streaming audio still takes up bandwidth)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteMusic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Music plays at 0 volume (streaming audio still takes up bandwidth)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteSounds

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sound effects play at 0 volume

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteUI

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: UI sound effects play at 0 volume

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteVoice

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Voice plays at 0 volume (streaming audio still takes up bandwidth)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MuteWhenMinimized

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Mute audio when SL window is minimized

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## MyOutfitsAutofill

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Always autofill My Outfits from library when empty (else happens just once).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NameTagDebugAVRezState

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show Avatar Rez state in name tag

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NameTagShowDisplayNames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show display names in name labels

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NameTagShowFriends

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Highlight the name tags of your friends

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NameTagShowGroupTitles

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show group titles in name labels

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NameTagShowUsernames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show usernames in avatar name tags

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NametagOverWater

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render name tag over the transparent water while camera is above the water

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NavBarShowCoordinates

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show coordinates in navigation bar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NavBarShowParcelProperties

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show parcel property icons in navigation bar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NearMeRange

- Type: F32 | Default value: `130` | Persisted: 1

- Comment: Search radius for nearby avatars

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NearbyListHideUsernames

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show both Display name and Username in Nearby list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NearbyListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide people icons in nearby list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NearbyListShowMap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide map above nearby people list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NearbyPeopleSortOrder

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Specifies sort order for nearby people (0 = by name, 3 = by distance, 4 = by most recent)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NearbyToastFadingTime

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Number of seconds while a nearby chat toast is fading 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NearbyToastLifeTime

- Type: S32 | Default value: `23` | Persisted: 1

- Comment: Number of seconds while a nearby chat toast exists

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NewCacheLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Change the location of the local disk cache to this

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NewCacheLocationTopFolder

- Type: String | Default value: `` | Persisted: 1

- Comment: Change the top folder location of the local disk cache to this

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NewObjectCreationThrottle

- Type: S32 | Default value: `200` | Persisted: 1

- Comment: maximum number of new objects created per frame, -1 to disable this throttle

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NewObjectCreationThrottleDelayTime

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: time in seconds NewObjectCreationThrottle to take effect after the progress screen is lifted

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NextLoginLocation

- Type: String | Default value: `` | Persisted: 1

- Comment: Location to log into for this session - set from command line or the login panel, cleared following a successfull login.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Newly created objects can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Newly created objects can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: (obsolete) Newly created objects can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NoAudio

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable audio playback.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NoHardwareProbe

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable hardware probe.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NoInventoryLibrary

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Do not request inventory library.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NoPreload

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable sound and image preload.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NoQuickTime

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disable QuickTime for a particular viewer run

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NoVerifySSLCert

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Do not verify SSL peers.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NonInteractive

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Run in a semi-headless mode where only logging in and logging out needs to work.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NonvisibleObjectsInMemoryTime

- Type: U32 | Default value: `64` | Persisted: 1

- Comment: Number of frames non-visible objects stay in memory before being removed. 0 means max.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotMovingHintTimeout

- Type: F32 | Default value: `120.0` | Persisted: 1

- Comment: Number of seconds to wait for resident to move before displaying move hint.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotecardsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created notecard

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotecardsNextOwnerCopy

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created notecards can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotecardsNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created notecards can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotecardsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created notecards can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotecardsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created notecards are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationChannelHeightRatio

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Notification channel and World View ratio(0.0 - always show 1 notification, 1.0 - max ratio).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationChannelRightMargin

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Space between toasts and a right border of an area where they can appear

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationConferenceIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Conference IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationFriendIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Friend IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationGroupChatOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Group Chat Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationNearbyChatOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Nearby Chat Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationNonFriendIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Non Friend IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationObjectIMOptions

- Type: String | Default value: `toast` | Persisted: 1

- Comment: 
        Specifies how the UI responds to Object IM Notifications.
        Allowed values: [openconversations,toast,flash,noaction]
      

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationTipToastLifeTime

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Number of seconds while a notification tip toast exist

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotificationToastLifeTime

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Number of seconds while a notification toast exists

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotifyMoneyChange

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pop up notifications for all L$ transactions

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotifyMoneyReceived

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pop up notifications when receiving L$

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotifyMoneySpend

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pop up notifications when spending L$

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NotifyTipDuration

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: Length of time that notification tips stay on screen (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NumSessions

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Number of successful logins to Second Life

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## NvAPICreateApplicationProfile

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Create NVIDIA application profile for optimized settings

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectCacheEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable the object cache.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectCostHighColor

- Type: Color4 | Default value: `1.0 0.0 0.0 0.75` | Persisted: 1

- Comment: Color for object a high object cost.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectCostHighThreshold

- Type: F32 | Default value: `50.0` | Persisted: 1

- Comment: Threshold at which object cost is considered high (displayed in red).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectCostLowColor

- Type: Color4 | Default value: `0.0 0.5 1.0 0.5` | Persisted: 1

- Comment: Color for object with a low object cost.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectCostMidColor

- Type: Color4 | Default value: `1.0 0.75 0.0 0.65` | Persisted: 1

- Comment: Color for object with a medium object cost.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectInspectorTooltipDelay

- Type: F32 | Default value: `0.35` | Persisted: 1

- Comment: Seconds before displaying object inspector tooltip

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created object

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created objects can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectsNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created objects can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created objects can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObjectsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created objects are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ObscureBalanceInStatusBar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, balance will be shows as '*'

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OctreeAlphaDistanceFactor

- Type: Vector3 | Default value: `0.1 0.0 64.0` | Persisted: 1

- Comment: Multiplier on alpha object distance for determining octree node size.  First two parameters are currently unused.  Third parameter is distance at which to perform detailed alpha sorting.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OctreeAttachmentSizeFactor

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: Multiplier on attachment size for determining octree node size 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OctreeDistanceFactor

- Type: Vector3 | Default value: `0.25 0.0 0.0` | Persisted: 1

- Comment: Multiplier on distance for determining octree node size 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OctreeMaxNodeCapacity

- Type: U32 | Default value: `128` | Persisted: 1

- Comment: Maximum number of elements to store in a single octree node

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OctreeMinimumNodeSize

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Minimum size of any octree node

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OctreeStaticObjectSizeFactor

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Multiplier on static object size for determining octree node size 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatAdvanced

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Advanced performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatBasic

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Basic performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatMemory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Memory Usage stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatNet

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Network performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatPathfinding

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Pathfinding performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatPhysicsDetails

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Physics Details performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatRender

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Render performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatSim

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Simulator performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatSimTime

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Simulator Time performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatSimTimeDetails

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Simulator Time Details performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatTexture

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Expand Texture performance stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatVoice

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Voice (WebRTC) stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatVoiceIncoming

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Incoming audio (Voice) stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenDebugStatVoiceOutgoing

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Expand Outgoing audio (Voice) stats display

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenIMOnVoice

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Open the corresponding IM window when connecting to a voice call.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OpenSidePanelsInFloaters

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, will always open side panel contents in a floater.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OutBandwidth

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Outgoing bandwidth throttle (bps)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OutfitGallerySortOrder

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Gallery sorting: 0 - sort outfits by name, 1 - images frst, 2 - favorites first

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OutfitListFilterFullList

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment:  0 - show only matches. 1 - show all items in outfit as long as outfit or item inside matches.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OutfitListSortOrder

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: How outfit list in Avatar's floater is sorted. 0 - by name 1 - favorites to top

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OutfitOperationsTimeout

- Type: S32 | Default value: `180` | Persisted: 1

- Comment: Timeout for outfit related operations.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OverflowToastHeight

- Type: S32 | Default value: `72` | Persisted: 1

- Comment: Height of an overflow toast

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## OverlayTitle

- Type: String | Default value: `Set_via_OverlayTitle_in_settings.xml` | Persisted: 1

- Comment: Controls watermark text message displayed on screen when "ShowOverlayTitle" is enabled (one word, underscores become spaces)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PTTCurrentlyEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Use Push to Talk mode

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PacketDropPercentage

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Percentage of packets dropped by the client.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ParcelMediaAutoPlayEnable

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Auto play parcel media when available. 0 - Do not autoplay; 1- Autoplay; 2 - Ask

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ParticipantListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide people icons in participant list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingAmbiance

- Type: F32 | Default value: `0.5` | Persisted: 0

- Comment: Ambiance of lit pathfinding navmesh displays.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingBoundaryEdge

- Type: Color4 | Default value: `1.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Color of a boundary (non-crossable) edge when displaying pathfinding navmesh.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingConnectedEdge

- Type: Color4 | Default value: `0.86 0.86 0.86 1.0` | Persisted: 0

- Comment: Color of a connected (crossable) edge when displaying pathfinding navmesh.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingExclusion

- Type: Color4 | Default value: `1.0 1.0 0.0 0.3` | Persisted: 0

- Comment: Color of exclusion volumes when displaying pathfinding navmesh object types.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingFaceColor

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 0

- Comment: Color of the faces when displaying the default view of the pathfinding navmesh.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingHeatColorBase

- Type: Color4 | Default value: `1.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Color of the least walkable value when displaying the pathfinding navmesh as a heatmap.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingHeatColorMax

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 0

- Comment: Color of the most walkable value when displaying the pathfinding navmesh as a heatmap.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingLineOffset

- Type: F32 | Default value: `2.3` | Persisted: 0

- Comment: Depth offset of volume outlines in pathfinding display.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingLineWidth

- Type: F32 | Default value: `2.0` | Persisted: 0

- Comment: Width of volume outlines in pathfinding navmesh display.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingMaterial

- Type: Color4 | Default value: `0.5 0.0 1.0 0.3` | Persisted: 0

- Comment: Color of material volumes when displaying pathfinding navmesh object types.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingNavMeshClear

- Type: Color4 | Default value: `0.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Background color when displaying pathfinding navmesh.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingObstacle

- Type: Color4 | Default value: `1.0 0.0 0.0 1.0` | Persisted: 0

- Comment: Color of static obstacle objects when displaying pathfinding navmesh object types.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingRetrieveNeighboringRegion

- Type: U32 | Default value: `99` | Persisted: 1

- Comment: Download a neighboring region when visualizing a pathfinding navmesh (default val 99 means do not download neighbors).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingTestPathColor

- Type: Color4 | Default value: `1.0 0.59 0.0 0.9` | Persisted: 0

- Comment: Color of the pathfinding test-path when the path is valid.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingTestPathInvalidEndColor

- Type: Color4 | Default value: `1.0 0.0 1.0 1.0` | Persisted: 0

- Comment: Color of the pathfinding test-pathing tool end-point when the path is invalid.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingTestPathValidEndColor

- Type: Color4 | Default value: `0.78 0.47 0.0 1.0` | Persisted: 0

- Comment: Color of the pathfinding test-pathing tool end-point when the path is valid.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingWalkable

- Type: Color4 | Default value: `0.45490196078431372549019607843137 0.93333333333333333333333333333333 0.38823529411764705882352941176471 1.0` | Persisted: 0

- Comment: Color of walkable objects when displaying pathfinding navmesh object types.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingWaterColor

- Type: Color4 | Default value: `0.0 0.0 1.0 1.0` | Persisted: 0

- Comment: Color of water plane when displaying pathfinding navmesh.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingXRayOpacity

- Type: F32 | Default value: `0.25` | Persisted: 0

- Comment: Opacity of xray lines in pathfinding display.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingXRayTint

- Type: F32 | Default value: `0.8` | Persisted: 0

- Comment: Amount to darken/lighten x-ray lines in pathfinding display.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PathfindingXRayWireframe

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Render pathfinding navmesh xray as a wireframe.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PaymentMethodStagingURL

- Type: String | Default value: `https://secondlife-staging.com/my/lindex/buy.php?associate_for_viewer=1` | Persisted: 1

- Comment: URL for adding a payment method on the Damballah

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PaymentMethodURL

- Type: String | Default value: `https://secondlife.com/my/lindex/buy.php?associate_for_viewer=1` | Persisted: 1

- Comment: URL for adding a payment method

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PerAccountSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Persisted client settings file name (per user).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PerfStatsCaptureEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable/disable render time data to support autotune.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PermissionsCautionEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: When enabled, changes the handling of script permission requests to help avoid accidental granting of certain permissions, such as the debit permission

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PermissionsCautionNotifyBoxHeight

- Type: S32 | Default value: `344` | Persisted: 0

- Comment: Height of caution-style notification messages

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PickerContextOpacity

- Type: F32 | Default value: `0.34999999404` | Persisted: 1

- Comment: Controls overall opacity of context frustrum connecting color and texture pickers with their swatches

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PicksPerSecondMouseMoving

- Type: F32 | Default value: `5.0` | Persisted: 1

- Comment: How often to perform hover picks while the mouse is moving (picks per second)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PicksPerSecondMouseStationary

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: How often to perform hover picks while the mouse is stationary (picks per second)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PieMenuLineWidth

- Type: F32 | Default value: `2.5` | Persisted: 1

- Comment: Width of lines in pie menu display (pixels)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PingInterpolate

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Extrapolate object position along velocity vector based on ping delay

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PitchFromMousePosition

- Type: F32 | Default value: `90.0` | Persisted: 1

- Comment: Vertical range over which avatar head tracks mouse position (degrees of head rotation from top of window to bottom)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlainTextChatHistory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable/Disable plain text chat history style

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlayChatAnim

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Your avatar plays the chat animation whenever you say, shout or whisper something in nearby chat

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundChatMention

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when got mentioned in a chat

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundConferenceIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when conference IM received.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundFriendIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when friend's IM received.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundGroupChatIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when group chat IM received.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundIncomingVoiceCall

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Plays a sound when have an incoming voice call.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundInventoryOffer

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when have an inventory offer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundNearbyChatIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when nearby chat IM received.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundNewConversation

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Plays a sound when have a new conversation.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundNonFriendIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when non-friend's IM received.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundObjectIM

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when IM fom an object received.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlaySoundTeleportOffer

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Plays a sound when have a teleport offer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PlayTypingAnim

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Your avatar plays the typing animation whenever you type in the chat bar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PluginAttachDebuggerToPlugins

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, attach a debugger session to each plugin process as it's launched.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PluginInstancesCPULimit

- Type: F32 | Default value: `0.9` | Persisted: 1

- Comment: Amount of total plugin CPU usage before inworld plugins start getting turned down to "slideshow" priority.  Set to 0 to disable this check.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PluginInstancesLow

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Limit on the number of inworld media plugins that will run at "low" priority

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PluginInstancesNormal

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Limit on the number of inworld media plugins that will run at "normal" or higher priority

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PluginInstancesTotal

- Type: U32 | Default value: `8` | Persisted: 1

- Comment: Hard limit on the number of plugins that will be instantiated at once for inworld media

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PluginUseReadThread

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use a separate thread to read incoming messages from plugins

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PoolSizeAIS

- Type: U32 | Default value: `20` | Persisted: ?

- Comment: Coroutine Pool size for AIS

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PoolSizeAssetStorage

- Type: U32 | Default value: `12` | Persisted: ?

- Comment: Coroutine Pool size for AssetStorage requests

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PoolSizeUpload

- Type: U32 | Default value: `1` | Persisted: ?

- Comment: Coroutine Pool size for Upload

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PostFirstLoginIntroURL

- Type: String | Default value: `` | Persisted: 1

- Comment: URL of intro presenatation after first time users first login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PostFirstLoginIntroViewed

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Flag indicating if user has seen intro presenatation after first time users first login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrecachingDelay

- Type: F32 | Default value: `6.0` | Persisted: 1

- Comment: Delay when logging in to load world before showing it (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreferredBrowserBehavior

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Use system browser for any links (0), use builtin browser for SL links and system one for others (1) or use builtin browser only (2).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreferredMaturity

- Type: U32 | Default value: `13` | Persisted: 1

- Comment: Setting for the user's preferred maturity level (consts in indra_constants.h)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PresetCameraActive

- Type: String | Default value: `Rear View` | Persisted: 1

- Comment: Name of currently selected preference

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PresetGraphicActive

- Type: String | Default value: `` | Persisted: 1

- Comment: Name of currently selected preference

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewAmbientColor

- Type: Color4 | Default value: `0.0 0.0 0.0 1.0` | Persisted: 1

- Comment: Ambient color of preview render.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewDiffuse0

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffise color of preview light 0.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewDiffuse1

- Type: Color4 | Default value: `0.25 0.25 0.25 1.0` | Persisted: 1

- Comment: Diffise color of preview light 1.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewDiffuse2

- Type: Color4 | Default value: `0.33 0.33 0.33 1.0` | Persisted: 1

- Comment: Diffise color of preview light 2.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewDirection0

- Type: Vector3 | Default value: `-0.75 1 1.0` | Persisted: 1

- Comment: Direction of light 0 for preview render.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewDirection1

- Type: Vector3 | Default value: `0.5 -0.6 0.4` | Persisted: 1

- Comment: Direction of light 1 for preview render.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewDirection2

- Type: Vector3 | Default value: `0.5 -0.8 0.3` | Persisted: 1

- Comment: Direction of light 2 for preview render.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewSpecular0

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffise color of preview light 0.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewSpecular1

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffise color of preview light 1.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviewSpecular2

- Type: Color4 | Default value: `1.0 1.0 1.0 1.0` | Persisted: 1

- Comment: Diffise color of preview light 2.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PreviousInstallChecked

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether viewer checked previous install on the same channel for NSIS

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaControlsUseHoverControlSet

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not hovering over prim media uses minimal "hover" controls or the authored control set.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaDragNDrop

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable drag and drop of URLs onto prim faces

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaMasterEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not Media on a Prim is enabled.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaMaxRetries

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Maximum number of retries for media queries.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaMaxRoundRobinQueueSize

- Type: U32 | Default value: `100000` | Persisted: 1

- Comment: Maximum number of objects the viewer will continuously update media for

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaMaxSortedQueueSize

- Type: U32 | Default value: `100000` | Persisted: 1

- Comment: Maximum number of objects the viewer will load media for initially

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaRequestQueueDelay

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Timer delay for fetching media from the queue (in seconds).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimMediaRetryTimerDelay

- Type: F32 | Default value: `5.0` | Persisted: 1

- Comment: Timer delay for retrying on media queries (in seconds).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrimTextMaxDrawDistance

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Maximum draw distance beyond which PRIM_TEXT won't be rendered

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PrivacyPolicyURL

- Type: String | Default value: `https://lindenlab.com/privacy` | Persisted: 1

- Comment: URL pointing to Privacy Policy page

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ProbeHardwareOnStartup

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Query current hardware configuration on application startup

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PurgeCacheOnNextStartup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clear local file cache next time viewer is run

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PurgeCacheOnStartup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clear local file cache every time viewer is run

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PurgeDiskCacheOnStartup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not to LRU purge the disk cache during startup on main thread

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PushToTalkButton

- Type: String | Default value: `MiddleMouse` | Persisted: 1

- Comment: (Obsolete)Which button or keyboard key is used for push-to-talk

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## PushToTalkToggle

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Should the push-to-talk toolbar button behave as a toggle

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QAMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable Testing Features.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QAModeEventHostPort

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: (Deprecated) Port on which lleventhost should listen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QAModeFakeSystemFolderIssues

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Simulates system folder issues in inventory

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QAModeMetrics

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables QA features (logging, faster cycling) for metrics collector

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QAModeTermCode

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: On LL_ERRS, terminate with this code instead of OS message box

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QuickBuyCurrency

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Use BuyCurrencyHTML instead

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QuietSnapshotsToDisk

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Take snapshots to disk without playing animation or sound

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QuitAfterSeconds

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: The duration allowed before quitting.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## QuitOnLoginActivated

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Quit if login page is activated (used when auto login is on and users must not be able to login manually)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RadioLandBrushAction

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Last selected land modification operation (0 = flatten, 1 = raise, 2 = lower, 3 = smooth, 4 = roughen, 5 = revert)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RecentItemsSortOrder

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Specifies sort key for recent inventory items (+0 = name, +1 = date, +2 = folders always by name, +4 = system folders to top)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RecentJumpThresholdSecs

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Seconds after jump input during which landing finish-anim is suppressed to avoid interrupting rapid successive jumps.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RecentListShowIcons

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide people icons in recent list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RecentPeopleSortOrder

- Type: U32 | Default value: `2` | Persisted: 1

- Comment: Specifies sort order for recent people (0 = by name, 2 = by most recent)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RectangleSelectInclusive

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Select objects that have at least one vertex inside selection rectangle

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RegInClient

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Experimental: Embed registration in login screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RegionCheckTextureHeights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Don't allow user to set low heights greater than high

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RegionCrossingInterpolationTime

- Type: F32 | Default value: `1` | Persisted: 1

- Comment: How long to extrapolate object motion after crossing regions

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RegionTextureSize

- Type: U32 | Default value: `256` | Persisted: 1

- Comment: Terrain texture dimensions (power of 2)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RememberPassword

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep password (in encrypted form) for next login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RememberUser

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep user name for next login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAnimateRes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Animate rezing prims.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAnisotropic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [OBSOLETE] Render textures using anisotropic filtering

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAnisotropicLevel

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Anisotropic filtering strength(0(Disable), 2x, 4x, 8x, 16x

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAppleUseMultGL

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether we want to use multi-threaded OpenGL on Apple hardware (requires restart of SL).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAttachedLights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render lighted prims that are attached to avatars

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAttachedParticles

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render particle systems that are attached to avatars

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAutoHideSurfaceAreaLimit

- Type: F32 | Default value: `10.0E6` | Persisted: 1

- Comment: Maximum surface area of a set of proximal objects inworld before automatically hiding geometry to prevent system overload.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAutoMaskAlphaDeferred

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use alpha masks where appropriate in the Advanced Lighting Model

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAutoMaskAlphaNonDeferred

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use alpha masks where appropriate when not using the Advanced Lighting Model

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAutoMuteLogging

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show extra information in viewer logs about avatar rendering costs

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAutoMuteRenderWeightLimit

- Type: U32 | Default value: `0` | Persisted: 0

- Comment: OBSOLETE. This setting has been renamed RenderAvatarMaxNonImpostors.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAutoMuteSurfaceAreaLimit

- Type: F32 | Default value: `1000.0` | Persisted: 1

- Comment: Maximum surface area of attachments before an avatar is
    rendered as a simple impostor (to not use this limit, set to zero
    or set RenderAvatarMaxComplexity to zero).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarCloth

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Controls if system avatar clothes use wavy cloth

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarComplexityMode

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: 0 - complexity limit applies to everyone, 1 - always show friends, 2 - only show friends

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarFriendsOnly

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: When enabled hides all avatars that aren't friends. Does not affect inworld control avatars (animeshes), nor self.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarLODFactor

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Controls level of detail of avatars (multiplier for current screen area when calculated level of detail)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarMaxART

- Type: F32 | Default value: `4.699` | Persisted: 0

- Comment: Render Time Limit in microseconds (0.0 = no limit)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarMaxComplexity

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Maximum Avatar Complexity; above this value, the avatar is
    rendered as a solid color outline (0 to disable this limit).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarMaxNonImpostors

- Type: U32 | Default value: `12` | Persisted: 1

- Comment: Maximum number of avatars to fully render at one time;
    over this limit uses impostor rendering (simplified rendering
    with less frequent updates), reducing client lag.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarMaxVisible

- Type: S32 | Default value: `0` | Persisted: 0

- Comment: OBSOLETE and UNUSED. See RenderAvatarMaxNonImpostors

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderAvatarPhysicsLODFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Controls level of detail of avatar physics (such as breast physics).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderBakeSunlight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Bake sunlight into vertex buffers for static objects.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderBalanceInSnapshot

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display L$ balance in snapshot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderBufferVisualization

- Type: S32 | Default value: `-1` | Persisted: 0

- Comment: Outputs a selected buffer to the screen.  -1 = final render buffer.  0 = Albedo, 1 = Specular/ORM, 2 = Normal, 3 = Emissive, 4 = Eye luminance, 5 = FXAA Luminance/SMAA Edge Tex, 6 = SMAA Blend Weights

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderBumpmapMinDistanceSquared

- Type: F32 | Default value: `100.0` | Persisted: 1

- Comment: Maximum distance at which to render bumpmapped primitives (distance in meters, squared)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderCASSharpness

- Type: F32 | Default value: `0.4` | Persisted: 1

- Comment: Level of sharpening to apply via Contrast Adaptive Sharpening (0.0(off) - 1.0)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderCPUBasis

- Type: F32 | Default value: `3000.0` | Persisted: 1

- Comment: Reference CPU clockspeed to use to bias GPU class (in MHz).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderCanUseGLTFPBROpaqueShaders

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Hardware has support for GLTF scene shaders

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderCanUseTerrainBakeShaders

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Hardware has support for Terrain Bake shaders

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderClass1MemoryBandwidth

- Type: F32 | Default value: `48.0` | Persisted: 1

- Comment: Memory bandwidth at which to default to Class 1 in gigabytes per second.  Used as basis for higher classes.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderComplexityColorMax

- Type: Color4 | Default value: `1.0 0.0 0.0 0.5` | Persisted: 1

- Comment: Unused obsolete setting

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderComplexityColorMid

- Type: Color4 | Default value: `0.0 1.0 0.0 0.5` | Persisted: 1

- Comment: Unused obsolete setting

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderComplexityColorMin

- Type: Color4 | Default value: `0.0 0.0 1.0 0.5` | Persisted: 1

- Comment: Unused obsolete setting

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderComplexityStaticMax

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Unused obsolete setting

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderComplexityThreshold

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Unused obsolete setting

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderCompressTextures

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable texture compression on OpenGL 3.0 and later implementations (EXPERIMENTAL, requires restart)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderCubeMap

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether we can render the cube map or not

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDebugAlphaMask

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Test Alpha Masking Cutoffs.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDebugGLSession

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable strict GL debugging on the start of next session.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDebugNormalScale

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Scale of normals in debug display.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDebugPipeline

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable strict pipeline debugging.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDebugTextureBind

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable texture bind performance test.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDefaultProbeUpdatePeriod

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: When RenderReflectionProbeLevel is 0, amount of time in seconds to wait between updates to reflection map.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferred

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: DEPRECATED (only true supported) - Use deferred rendering pipeline (Advanced Lighting Model).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredAlphaSoften

- Type: F32 | Default value: `0.75` | Persisted: 1

- Comment: Scalar for softening alpha surfaces (for soft particles).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredAtmospheric

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute atmospheric shader in deferred renderer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredBlurLight

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute shadow softening shader in deferred renderer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredDisplayGamma

- Type: F32 | Default value: `2.2` | Persisted: 1

- Comment: Gamma ramp exponent for final correction before display gamma.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredNoise

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: Noise scalar to hide banding in deferred render.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredSSAO

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute screen space ambient occlusion shader in deferred renderer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredSpotShadowBias

- Type: F32 | Default value: `-64.0` | Persisted: 1

- Comment: Bias value for spot shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredSpotShadowOffset

- Type: F32 | Default value: `0.8` | Persisted: 1

- Comment: Offset value for spot shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredSun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Execute sunlight shader in deferred renderer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredSunWash

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Amount local lights are washed out by sun.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredTreeShadowBias

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Bias value for tree shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDeferredTreeShadowOffset

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Offset value for tree shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDelayCreation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Throttle creation of drawables.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDelayVBUpdate

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Delay vertex buffer updates until just before rendering

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDepthOfField

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to use depth of field effect when Advanced Lighting Model is enabled

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDepthOfFieldInEditMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to use depth of field effect when in edit mode

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDepthPrePass

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: EXPERIMENTAL: Prime the depth buffer with simple prim geometry before rendering with textures.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDesaturateIrradiance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Desaturate irradiance to remove blue tint

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDiffuseLuminanceScale

- Type: F32 | Default value: `0.5` | Persisted: 0

- Comment: Luminance adjustment for diffuse surfaces to aid auto-exposure behavior

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDisablePostProcessing

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Disable tone mapping and exposure correction when build floater is open (for artists developing materials)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDisableVintageMode

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables additional rendering pipeline features on newer machines such as HDR and emissive textures on PBR content.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDownScaleMethod

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Method to use to downscale images.  0 - FBO, 1 - PBO

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDynamicExposureCoefficient

- Type: F32 | Default value: `0.5` | Persisted: 0

- Comment: Luminance coefficient for dynamic exposure

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderDynamicLOD

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Dynamically adjust level of detail.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderEdgeDepthCutoff

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Cutoff for depth difference that amounts to an edge.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderEdgeNormCutoff

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Cutoff for normal difference that amounts to an edge.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderEnableEmissiveBuffer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable emissive buffer in gbuffer.  Should only be disabled in GL3 mode.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderExposure

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Exposure value to send to tonemapper.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderFSAASamples

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Quality of antialiasing: 0 = Low, 1 = Medium, 2 = High, 3 = Ultra

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderFSAAType

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Type of Antialiasing to use: 0 = None, 1 = FXAA, 2 = SMAA

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderFarClip

- Type: F32 | Default value: `256.0` | Persisted: 1

- Comment: Distance of far clip plane from camera (meters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderFlexTimeFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Controls level of detail of flexible objects (multiplier for amount of time spent processing flex objects)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderFogRatio

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: DEPRECATED - Distance from camera where fog reaches maximum density (fraction or multiple of far clip distance)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGLContextCoreProfile

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Don't use a compatibility profile OpenGL context.  Requires restart.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGLMultiThreadedMedia

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow OpenGL to use multiple render contexts for playing media (may reduce frame stutters, doesn't play nice with Intel drivers)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGLMultiThreadedTextures

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Allow OpenGL to use multiple render contexts for loading textures (may reduce frame stutters, doesn't play nice with Intel drivers).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGamma

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: DEPRECATED - Sets gamma exponent for renderer

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGammaFull

- Type: Boolean | Default value: `1.0` | Persisted: 1

- Comment: Use fully controllable gamma correction, instead of faster, hard-coded gamma correction of 2.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlow

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render bloom post effect.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowHDR

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable HDR for glow map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowIterations

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Number of times to iterate the glow (higher = wider and smoother but slower)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowLumWeights

- Type: Vector3 | Default value: `1.0 0.0 0.0` | Persisted: 1

- Comment: Weights for each color channel to be used in calculating luminance (should add up to 1.0)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowMaxExtractAlpha

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Max glow alpha value for brightness extraction to auto-glow.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowMinLuminance

- Type: F32 | Default value: `9999` | Persisted: 1

- Comment: Min luminance intensity necessary to consider an object bright enough to automatically glow.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowNoise

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enables glow noise (dithering). Reduces banding from glow in certain cases.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowResolutionPow

- Type: S32 | Default value: `9` | Persisted: 1

- Comment: Glow map resolution power of two.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowStrength

- Type: F32 | Default value: `0.325` | Persisted: 1

- Comment: Additive strength of glow.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowWarmthAmount

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Amount of warmth extraction to use (versus luminance extraction). 0 = lum, 1.0 = warmth

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowWarmthWeights

- Type: Vector3 | Default value: `1.0 0.5 0.7` | Persisted: 1

- Comment: Weight of each color channel used before finding the max warmth

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderGlowWidth

- Type: F32 | Default value: `1.3` | Persisted: 1

- Comment: Glow sample size (higher = wider and softer but eventually more pixelated)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHDREnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable HDR rendering.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHDRIExposure

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Exposure adjustment of HDRI when previewing an HDRI.  Units are EV.  Sane values would be -10 to 10.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHDRIIrradianceOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Only use HDRI sky for irradiance map when RenderHDRISplitScreen is 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHDRIRotation

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rotation (in degrees) of environment when previewing an HDRI.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHDRISplitScreen

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: What percentage of screen to render using HDRI vs EEP sky.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHDRSkySunlightScale

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: Sunlight scale fudge factor for matching with pre-PBR viewer when HDR is enabled

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHUDInSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display HUD attachments in snapshot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHUDObjectsWarning

- Type: U32 | Default value: `1000` | Persisted: 1

- Comment: Viewer will warn user about HUD containing to many objects if objects count is above this value

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHUDOversizedTexturesWarning

- Type: U32 | Default value: `6` | Persisted: 1

- Comment: How many textures with size 1024 * 1024 or bigger HUD can contain before notifying user

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHUDParticles

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display particle systems in HUD attachments (experimental)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHUDTexturesMemoryWarning

- Type: U32 | Default value: `32000000` | Persisted: 1

- Comment: Viewer will warn user about HUD textures using memory above this value (in bytes)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHUDTexturesWarning

- Type: U32 | Default value: `200` | Persisted: 1

- Comment: Viewer will warn user about HUD containing to many textures if texture count is above this value

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHeroProbeConservativeUpdateMultiplier

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: How many probe updates to wait until it's time to update faces that are not directly facing the camera.  Acts as a multiplier.  E.g., frames to the periphery of the camera updating once every 3 updates, vs ones directly facing the camera updating every update.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHeroProbeDistance

- Type: F32 | Default value: `8` | Persisted: 1

- Comment: Distance in meters for hero probes to render out to.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHeroProbeResolution

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: Resolution to render hero probes used for mirrors, water, etc.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHeroProbeUpdateRate

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: How many frames to wait for until it's time to render the probe. E.g., every other frame (1), every two frames (2), every three frames (3) etc.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHiDPI

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable support for HiDPI displays, like Retina (macOS and Linux ONLY, requires restart)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHiddenSelections

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show selection lines on objects that are behind other objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHideGroupTitle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Don't show my group title in my name label

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHighMemMinDiscardDecrement

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Minimum decrement of discard bias if excess texture memory is available

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHighPrecisionPostProcess

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use 16-bit floating point buffers for post process rendering

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHighlightBrightness

- Type: F32 | Default value: `4.0` | Persisted: 1

- Comment: Brightness of mouseover highlights.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHighlightColor

- Type: Color4 | Default value: `0.4 0.98 0.93 1.0` | Persisted: 1

- Comment: Brightness of mouseover highlights.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHighlightFadeTime

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Transition time for mouseover highlights.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHighlightSelections

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Show selection outlines on objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHighlightThickness

- Type: F32 | Default value: `0.6` | Persisted: 1

- Comment: Thickness of mouseover highlights.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderHoverGlowEnable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: DEPRECATED --- Show glow effect when hovering on interactive objects.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderInitError

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Error occured while initializing GL

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderLightRadius

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render the radius of selected lights

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderLocalLightCount

- Type: S32 | Default value: `256` | Persisted: 1

- Comment: Number of local lights to render.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderLowMemMinDiscardIncrement

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Minimum increment of discard bias if available texture memory gets low

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMaxNodeSize

- Type: S32 | Default value: `65536` | Persisted: 1

- Comment: Maximum size of a single node's vertex data (in KB).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMaxOpenGLVersion

- Type: F32 | Default value: `4.6` | Persisted: 1

- Comment: Maximum OpenGL version to attempt use (minimum 3.1 maximum 4.6).  Requires restart. Windows only.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMaxPartCount

- Type: S32 | Default value: `4096` | Persisted: 1

- Comment: Maximum number of particles to display on screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMaxTextureIndex

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Maximum texture index to use for indexed texture rendering.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMaxTextureResolution

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: Maximum texture resolution to download for non-boosted textures.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMaxVBOSize

- Type: S32 | Default value: `4096` | Persisted: 1

- Comment: Maximum size of a vertex buffer (in KB).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMaxVRAMBudget

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Maximum amount of texture memory to budget for (in MB), or 0 for autodetect.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMinFreeMainMemoryThreshold

- Type: U32 | Default value: `512` | Persisted: 0

- Comment: If available free physical memory is below this value textures get agresively scaled down

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMinimumLODTriangleCount

- Type: U32 | Default value: `16` | Persisted: 1

- Comment: Triangle count threshold at which automatic LOD generation stops

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderMirrors

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Renders realtime mirrors.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderNameFadeDuration

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Time interval over which to fade avatar names (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderNameShowSelf

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display own name above avatar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderNameShowTime

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Fade avatar names after specified time (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderNoAlpha

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable rendering of alpha objects (render all alpha objects as alpha masks).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderNormalMapScale

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Scaler applied to height map when generating normal maps

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderNsightDebugSupport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: 
      Disable features which prevent nVidia nSight from being usable with SL. Requires restart.
    

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderObjectBump

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: DEPRECATED (only TRUE supported) Show bumpmapping on primitives

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderOcclusionTimeout

- Type: U32 | Default value: `8` | Persisted: 1

- Comment: Maximum number of frames to wait on an occlusion query before forcibly reading it back

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderParcelSelection

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display selected parcel outline

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderPerformanceTest

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: 
                Disable rendering of everything but in-world content for
                performance testing


- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderPreferStreamDraw

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use GL_STREAM_DRAW in place of GL_DYNAMIC_DRAW

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderQualityPerformance

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Which graphics settings you've chosen. Don't use this setting to change quality directly from debug settings.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionDetail

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: DEPRECATED -- use RenderTransparentWater and RenderReflectionProbeDetail -- Detail of reflection render pass.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeAmbiance

- Type: F32 | Default value: `0` | Persisted: 1

- Comment: Amount reflection probes contribute to ambient light.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeCount

- Type: U32 | Default value: `256` | Persisted: 1

- Comment: Number of probes to render.  Maximum of 256.  Clamps to the nearest power of 2.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeDetail

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Detail of reflections. (-1 - Disabled, 0 - Static Only, 1 - Static + Dynamic, 2 - Realtime)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeDrawDistance

- Type: F32 | Default value: `64.0` | Persisted: 1

- Comment: Camera far clip to use when updating reflection probes.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeDynamicAllocation

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Enable dynamic allocation of reflection probes. -1 means no dynamic allocation. Sets a buffer to allocate when a dynamic allocation occurs otherwise.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeLevel

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Reflection probes control.  0 - disable (one probe to rule them all), 1 - manual probes only, 2 - manual + terrain/water, 3 - Manual + Terrain/water + objects.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeMaxLocalLightAmbiance

- Type: F32 | Default value: `4.0` | Persisted: 0

- Comment: Maximum effective probe ambiance for local lights

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeResolution

- Type: U32 | Default value: `128` | Persisted: 1

- Comment: Resolution of reflection probe radiance maps (requires restart).  Will be set to the next highest power of two clamped to [64, 512].  Note that changing this value may consume a massive amount of video memory.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeShowTransparent

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Show reflection probes in the transparency debug view

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionProbeVolumes

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Render influence volumes of Reflection Probes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionRes

- Type: S32 | Default value: `64` | Persisted: 1

- Comment: Reflection map resolution.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReflectionsEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable/disable reflection probes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderReservedTextureIndices

- Type: S32 | Default value: `14` | Persisted: 1

- Comment: Count of texture indices to reserve for shadow and reflection maps when using indexed texture rendering.  Probably only want to set from the login screen.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderResolutionDivisor

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Divisor for rendering 3D scene at reduced resolution.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSSAOEffect

- Type: Vector3 | Default value: `0.80 1.00 0.00` | Persisted: 1

- Comment: Multiplier for (1) value and (2) saturation (HSV definition), for areas which are totally occluded.  Blends with original color for partly-occluded areas.  (Third component is unused.)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSSAOFactor

- Type: F32 | Default value: `0.30` | Persisted: 1

- Comment: Occlusion sensitivity factor for ambient occlusion (larger is more)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSSAOIrradianceMax

- Type: F32 | Default value: `0.18` | Persisted: 0

- Comment: Max factor for irradiance input to SSAO

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSSAOIrradianceScale

- Type: F32 | Default value: `0.6` | Persisted: 0

- Comment: Scaling factor for irradiance input to SSAO

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSSAOMaxScale

- Type: U32 | Default value: `200` | Persisted: 1

- Comment: Maximum screen radius for sampling (pixels)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSSAOScale

- Type: F32 | Default value: `500.0` | Persisted: 1

- Comment: Scaling factor for the area to sample for occluders (pixels at 1 meter away, inversely varying with distance)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderScreenSpaceReflectionAdaptiveStepMultiplier

- Type: F32 | Default value: `1.6` | Persisted: 1

- Comment: Multiplier to scale adaptive stepping.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderScreenSpaceReflectionDepthRejectBias

- Type: F32 | Default value: `0.001` | Persisted: 1

- Comment: Bias against the depth buffer before rejecting a sample.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderScreenSpaceReflectionDistanceBias

- Type: F32 | Default value: `0.015` | Persisted: 1

- Comment: Distance bias to apply when rejecting a potential sample.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderScreenSpaceReflectionGlossySamples

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: Maximum number of samples to apply for glossy SSR.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderScreenSpaceReflectionIterations

- Type: S32 | Default value: `25` | Persisted: 1

- Comment: Number of times the ray march algorithm runs to find a potential hit.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderScreenSpaceReflectionRayStep

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: How big the step is between each run.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderScreenSpaceReflections

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Renders screen space reflections to better account for dynamic objects with reflection probes.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShaderCacheEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable binary shader cache

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShaderCacheVersion

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 1

- Comment: Current version hash for shader cache

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShaderLODThreshold

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Fraction of draw distance defining the switch to a different shader LOD

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShaderLightingMaxLevel

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Max lighting level to use in the shader (class 3 is default, 2 is less lights, 1 is sun/moon only.  Works around shader compiler bugs on certain platforms.)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShaderParticleThreshold

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Fraction of draw distance to not use shader on particles

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowBias

- Type: F32 | Default value: `-0.002` | Persisted: 1

- Comment: Bias value for shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowBiasError

- Type: F32 | Default value: `-0.007` | Persisted: 1

- Comment: Error scale for shadow bias (based on altitude).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowBlurDistFactor

- Type: F32 | Default value: `0` | Persisted: 1

- Comment: Distance scaler for shadow blur.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowBlurSamples

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Number of samples to take for each pass of shadow blur (value range 1-16).  Actual number of samples is value * 2 - 1.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowBlurSize

- Type: F32 | Default value: `1.4` | Persisted: 1

- Comment: Scale of shadow softening kernel.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowDetail

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: Detail of shadows.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowErrorCutoff

- Type: F32 | Default value: `5.0` | Persisted: 1

- Comment: Cutoff error value to use ortho instead of perspective projection.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowFOVCutoff

- Type: F32 | Default value: `0.8` | Persisted: 1

- Comment: Cutoff FOV to use ortho instead of perspective projection.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowGaussian

- Type: Vector3 | Default value: `3.0 2.0 0.0` | Persisted: 1

- Comment: Gaussian coefficients for the two shadow/SSAO blurring passes (z component unused).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowNoise

- Type: F32 | Default value: `-0.0001` | Persisted: 1

- Comment: Magnitude of noise on shadow samples.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowOffset

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Offset value for shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowOffsetError

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Error scale for shadow offset (based on altitude).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowProjExponent

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Exponent applied to transition between ortho and perspective shadow projections based on viewing angle and light vector.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowProjOffset

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Amount to scale distance to virtual origin of shadow perspective projection.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowResolutionScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of shadow map resolution vs. screen resolution (only positivie values are allowed)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowSlopeThreshold

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Cutoff slope value for points to affect perspective shadow generation

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowSplitExponent

- Type: Vector3 | Default value: `3.0 3.0 2.0` | Persisted: 1

- Comment: Near clip plane split distances for shadow map frusta (x=perspective, y=ortho, z=transition rate).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderShadowSplits

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Amount of shadow map splits to render (0 - 3).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAmbientScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Ambient scale fudge factor for matching with pre-PBR viewer

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAutoAdjustAmbientScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Amount to scale ambient when auto-adjusting legacy skies

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAutoAdjustBlueDensityScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Blue Horizon Scale value to use when auto-adjusting legacy skies

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAutoAdjustBlueHorizonScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Blue Horizon Scale value to use when auto-adjusting legacy skies

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAutoAdjustHDRScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: HDR Scale value to use when auto-adjusting legacy skies

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAutoAdjustLegacy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If true, automatically adjust legacy skies (those without a probe ambiance value) to take advantage of probes and HDR.  This is the "opt-out" button for HDR and tonemapping when coupled with a sky setting that predates PBR.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAutoAdjustProbeAmbiance

- Type: F32 | Default value: `0.01` | Persisted: 1

- Comment: Probe ambiance value when auto-adjusting legacy skies

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkyAutoAdjustSunColorScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Sun color scalar when auto-adjusting legacy skies

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSkySunlightScale

- Type: F32 | Default value: `1.0` | Persisted: 0

- Comment: Sunlight scale fudge factor for matching with pre-PBR viewer when HDR is disabled

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSnapshotNoPost

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable tone mapping and exposure correction when snapshot is being rendered

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSpecularExponent

- Type: F32 | Default value: `368.0` | Persisted: 1

- Comment: Specular exponent for generating spec map

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSpecularPrecision

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Force 32-bit floating point LUT

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSpecularResX

- Type: U32 | Default value: `1024` | Persisted: 1

- Comment: Spec map resolution.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSpecularResY

- Type: U32 | Default value: `256` | Persisted: 1

- Comment: Spec map resolution.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSpotLightsInNondeferred

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether to support projectors as spotlights when Advanced Lighting Model is disabled

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSpotShadowBias

- Type: F32 | Default value: `-0.0002` | Persisted: 1

- Comment: Bias value for shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSpotShadowOffset

- Type: F32 | Default value: `0.04` | Persisted: 1

- Comment: Offset value for shadows (prevent shadow acne).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderSunDynamicRange

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Defines what percent brighter the sun is than local point lights (1.0 = 100% brighter. Value should not be less than 0. ).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainDetail

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Detail applied to terrain texturing (0 = none, 1 = full)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainLODFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Controls level of detail of terrain (multiplier for current screen area when calculated level of detail)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainPBRDetail

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Detail level for PBR terrain. 0 is full detail. Negative values drop rendering features, in accordance with the GLTF specification when possible, which reduces the number of texture binds.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainPBREnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable PBR Terrain features.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainPBRNormalsEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: EXPERIMENTAL: Change normal gen for PBR Terrain.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainPBRPlanarSampleCount

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: How many UV planes to sample PBR terrain textures from. 1 is "flat", 3 is triplanar mapping (aka box mapping)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainPBRScale

- Type: F32 | Default value: `8.0` | Persisted: 1

- Comment: PBR terrain detail texture scale (meters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainPBRTransformsEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: EXPERIMENTAL: Enable PBR Terrain texture transforms.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainPBRTriplanarBlendFactor

- Type: F32 | Default value: `8.0` | Persisted: 1

- Comment: Higher values create sharper transitions, but are more likely to produce artifacts.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTerrainScale

- Type: F32 | Default value: `12.0` | Persisted: 1

- Comment: Terrain detail texture scale (meters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTextureVRAMDivisor

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Divisor for maximum amount of VRAM the viewer will use for textures. 1 = all the VRAM.  Used in conjunction with RenderMaxVRAMBudget.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTonemapMix

- Type: F32 | Default value: `0.7` | Persisted: 1

- Comment: Mix between linear and tonemapped colors (0.0(Linear) - 1.0(Tonemapped)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTonemapType

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: What tonemapper to use: 0 = Khronos Neutral, 1 = ACES

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTrackerBeacon

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display tracking arrow and beacon to target avatar, teleport destination

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTransparentWater

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Render water as transparent.  Setting to false renders water as opaque with a simple texture applied.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderTreeLODFactor

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Controls level of detail of vegetation (multiplier for current screen area when calculated level of detail)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUIBuffer

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Cache ui render in a screen aligned buffer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUIInSnapshot

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display user interface in snapshot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUnloadedAvatar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show avatars which haven't finished loading

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUseAdvancedAtmospherics

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use fancy precomputed atmospherics and stuff.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUseExposureSkySettings

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Use exposure sky settings instead of deriving from HDR scale.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUseFarClip

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If false, frustum culling will ignore far clip plane.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUseStreamVBO

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use VBO's for stream buffers

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUseTriStrips

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: DEPRECATED - now always assumed to be false - Use triangle strips for rendering prims.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderUseVAO

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [EXPERIMENTAL] Use GL Vertex Array Objects.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderVBOEnable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use GL Vertex Buffer Objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderVBOMappingDisable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Disable VBO glMapBufferARB

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderVSyncEnable

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Update frames between display scans (FALSE = Update frames as fast as possible).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderVolumeLODFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Controls level of detail of primitives (multiplier for current screen area when calculated level of detail)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderWater

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display water

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderWaterMaterials

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Water planar reflections include materials rendering.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderWaterMipNormal

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use mip maps for water normal map.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RenderWaterRefResolution

- Type: S32 | Default value: `512` | Persisted: 1

- Comment: Water planar reflection resolution.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ReplaySession

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Request replay of previously-recorded pilot file

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ReportBugURL

- Type: String | Default value: `https://feedback.secondlife.com/` | Persisted: 1

- Comment: URL used for filing bugs from viewer

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RequestFullRegionCache

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: If set, ask sim to send full region object cache. Needs to restart viewer.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ResetUIScaleOnFirstRun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Resets the UI scale factor on first run due to changed display scaling behavior

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RestoreCameraPosOnLogin

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reset camera position to location at logout

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RevokePermsOnStopAnimation

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Clear animation permssions when choosing "Stop Animating Me"

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RotateRight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Make the agent rotate to its right.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RotationStep

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: All rotations via rotation tool are constrained to multiples of this unit (degrees)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## RunMultipleThreads

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE keep background threads active during render

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SLURLDragNDrop

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable drag and drop of SLURLs onto the viewer

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SLURLPassToOtherInstance

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Pass execution to prevoius viewer instances if there is a given slurl

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SLURLTeleportDirectly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Clicking on a slurl will teleport you directly instead of opening places panel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SafeMode

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Reset preferences, run in safe mode.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SaveMinidump

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Save minidump for developer debugging on crash

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScaleShowAxes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show indicator of selected scale axis when scaling

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScaleStretchTextures

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Stretch textures along with object when scaling

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScaleUniform

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Scale selected objects evenly about center of selection

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadFrontPixelThreshold

- Type: F32 | Default value: `100.0` | Persisted: 1

- Comment: in pixels, all objects in view frustum whose screen area is greater than this threshold will be loaded

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadHighMemoryBound

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: in MB, when total memory usage above this threshold, minimum invisible objects are kept in memory 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadLowMemoryBound

- Type: U32 | Default value: `750` | Persisted: 1

- Comment: in MB, when total memory usage above this threshold, start to reduce invisible objects kept in memory 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadMinRadius

- Type: F32 | Default value: `32.0` | Persisted: 1

- Comment: in meters, all objects (visible or invisible) within this radius will remain loaded in memory

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadRearMaxRadiusFraction

- Type: F32 | Default value: `0.75` | Persisted: 1

- Comment: a fraction of draw distance beyond which all objects outside of view frustum will be unloaded, regardless of pixel threshold

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadRearPixelThreshold

- Type: F32 | Default value: `400.0` | Persisted: 1

- Comment: in pixels, all objects out of view frustum whose screen area is greater than this threshold will remain loaded

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadingMonitorEnabled

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Enabled scene loading monitor if set

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadingMonitorPixelDiffThreshold

- Type: F32 | Default value: `0.02` | Persisted: 1

- Comment: Amount of pixels changed required to consider the scene as still loading (square root of fraction of pixels on screen)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SceneLoadingMonitorSampleTime

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Time between screen samples when monitor scene load (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptDialogLimitations

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Limits amount of dialogs per script (0 - per object, 1 - per channel, 2 - per channel for attachments, 3 - per channel for HUDs, 4 -unconstrained for HUDs)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptEditorDisableSyntaxHighlight

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Disable syntax highlighting in script editor for performance testing

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptHelpFollowsCursor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Scripting help window updates contents based on script editor contents under text cursor

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptToastButtonWidth

- Type: S32 | Default value: `127` | Persisted: 1

- Comment: Default width of buttons in the Script dialog toast.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptsCanShowUI

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Allow LSL calls (such as LLMapDestination) to spawn viewer UI

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created script

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created scripts can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptsNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created scripts can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created scripts can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ScriptsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created scripts are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SearchFromAddressBar

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Can enter search queries into navigation address bar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SearchURL

- Type: String | Default value: `https://search.[GRID]/viewer/?query_term=[QUERY]&search_type=[TYPE][COLLECTION]&maturity=[MATURITY]&lang=[LANGUAGE]&g=[GODLIKE]&sid=[SESSION_ID]&rid=[REGION_ID]&pid=[PARCEL_ID]&channel=[CHANNEL]&version=[VERSION]&major=[VERSION_MAJOR]&minor=[VERSION_MINOR]&patch=[VERSION_PATCH]&build=[VERSION_BUILD]` | Persisted: 0

- Comment: URL for Search website, displayed in the Find floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectInvisibleObjects

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Select invisible objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectMovableOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Select only objects you can move

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectOwnedOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Select only objects you own

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectReflectionProbes

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Select reflection probes

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectionHighlightAlpha

- Type: F32 | Default value: `0.40000000596` | Persisted: 1

- Comment: Opacity of selection highlight (0.0 = completely transparent, 1.0 = completely opaque)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectionHighlightAlphaTest

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Alpha value below which pixels are displayed on selection highlight line (0.0 = show all pixels, 1.0 = show now pixels)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectionHighlightThickness

- Type: F32 | Default value: `0.00999999977648` | Persisted: 1

- Comment: Thickness of selection highlight line (fraction of view distance)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectionHighlightUAnim

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Rate at which texture animates along U direction in selection highlight line (fraction of texture per second)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectionHighlightUScale

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Scale of texture display on selection highlight line (fraction of texture size)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectionHighlightVAnim

- Type: F32 | Default value: `0.5` | Persisted: 1

- Comment: Rate at which texture animates along V direction in selection highlight line (fraction of texture per second)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SelectionHighlightVScale

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Scale of texture display on selection highlight line (fraction of texture size)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ServerChoice

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: [DO NOT MODIFY] Controls which grid you connect to

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SessionSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Settings that are a applied per session (not saved).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SettingsNextOwnerModify

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created Environment setting can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SettingsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created Environment setting can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (obsolete) Newly created objects are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowAdultClassifieds

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find classifieds that are flagged as adult

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowAdultEvents

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find events that are flagged as adult

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowAdultLand

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find land sales that are flagged as adult

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowAdultSims

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find places or find popular that are in adult sims

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowAllObjectHoverTip

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show descriptive tooltip when mouse hovers over non-interactive and interactive objects.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowAxes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render coordinate frame at your position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowBanLines

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Show in-world ban/access borders, 0 - do not show, 1 - show on collision, 2 - show on proximity

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowBetaGrids

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display the beta grids in the grid selection control.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowBlockedConvHistory

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Specifies whether blocked agents will be shown in Call Log

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowBuildButton

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows/hides build button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowCameraButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide view button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowConsoleWindow

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show log in separate OS window

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowCrosshairs

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display crosshairs when in mouselook mode

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowDebugConsole

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show log in SL window

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowDeviceSettings

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show device settings

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowDiscordActivityDetails

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When set, show avatar name on Discord Rich Presence

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowDiscordActivityState

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When set, show location on Discord Rich Presence

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowEventRecorderMenuItems

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Whether or not Event Recorder menu choices - Start / Stop event recording should appear in the (currently) Develop menu

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowGestureButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows/hides gesture button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowHelpOnFirstLogin

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show Help Floater on first login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowHoverTips

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show descriptive tooltip when mouse hovers over items in world

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowInInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically opens inventory to show accepted objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowLandHoverTip

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show descriptive tooltip when mouse hovers over land

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMatureClassifieds

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find classifieds that are flagged as moderate

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMatureEvents

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find events that are flagged as moderate

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMatureGroups

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Include groups that are flagged as mature to Search results

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMatureLand

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find land sales that are flagged as moderate

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMatureSims

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display results of find places or find popular that are in moderate sims

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMiniLocationPanel

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show/hide mini-location panel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMiniMapButton

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows/hides mini-map button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMoveButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows/hides move button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowMyComplexityChanges

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: How long to show notices about avatar complexity (set to zero to disable those notices)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowNavbarFavoritesPanel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide navigation bar favorites panel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowNavbarNavigationPanel

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show/hide navigation bar navigation panel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowNearClip

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowNetStats

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show the Status Indicators for the Viewer and Network Usage in the Status Overlay

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowNewInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Automatically views new notecards/textures/landmarks

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowObjectRenderingCost

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the object rendering cost  in  build tools

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowObjectUpdates

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Show when update messages are received for individual objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowOfferedInventory

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show inventory window with last inventory offer selected when receiving inventory from other users.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowOverlayTitle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Prints watermark text message on screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowPGClassifieds

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find classifieds that are flagged as general

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowPGEvents

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find events that are flagged as general

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowPGLand

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find land sales that are flagged as general

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowPGSims

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display results of find places or find popular that are in general sims

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowParcelOwners

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowPermissions

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowPropertyLines

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show line overlay demarking property boundaries

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowScriptErrors

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show script errors

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowScriptErrorsLocation

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Show script error in chat (0) or window (1).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowSearchButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows/hides search button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowSelectionBeam

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show selection particle beam when selecting or interacting with objects.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowSnapshotButton

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Shows/hides snapshot button button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowStartLocation

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display starting location menu on login screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowTangentBasis

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Render normal and binormal (debugging bump mapping)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowTunedART

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Show the current render time not the pre-tuning render time in the avatar display.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowTutorial

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show tutorial window on login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowVoiceChannelPopup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Controls visibility of the current voice channel popup above the voice tab

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowVoiceVisualizersInCalls

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enables in-world voice visualizers, voice gestures and lip-sync while in group or P2P calls.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowVolumeSettingsPopup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show individual volume slider for voice, sound effects, etc

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ShowWorldMapButton

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Shows/hides map button in the bottom tray.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SimPendingUploads

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Mode of stat in Statistics floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SimulateFBOFailure

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: [DEBUG] Make allocateScreenBuffer return false.  Used to test error handling.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SingleModeDoubleClickOpenWindow

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Sets the action for Double-click on folder in single-folder view (0 - stays in current window, 1 - opens a new window)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkinCurrent

- Type: String | Default value: `default` | Persisted: 1

- Comment: The currently selected skin.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkinningSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: Client skin color setting file name (per install).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkipBenchmark

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: if true, disables running the GPU benchmark at startup
      (default to class 1)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkyAmbientScale

- Type: F32 | Default value: `0.300000011921` | Persisted: 1

- Comment: Controls strength of ambient, or non-directional light from the sun and moon (fraction or multiple of default ambient level)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkyMoonDefaultPosition

- Type: Vector3 | Default value: `-1.0 0.0 -0.1` | Persisted: 1

- Comment: Default position of sun in sky (direction in world coordinates)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkyNightColorShift

- Type: Color3 | Default value: `0.67 0.67 1.0` | Persisted: 1

- Comment: Controls moonlight color (base color applied to moon as light source)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkyOverrideSimSunPosition

- Type: Boolean | Default value: `0` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SkySunDefaultPosition

- Type: Vector3 | Default value: `1.0 0.0 0.1` | Persisted: 1

- Comment: Default position of sun in sky (direction in world coordinates)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SnapEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable snapping to grid

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SnapMargin

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Controls maximum distance between windows before they auto-snap together (pixels)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SnapToMouseCursor

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: When snapping to grid, center object on nearest grid point to mouse cursor

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SnapshotFormat

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Save snapshots in this format (0 = PNG, 1 = JPEG, 2 = BMP)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SnapshotQuality

- Type: S32 | Default value: `75` | Persisted: 1

- Comment: Quality setting of postcard JPEGs (0 = worst, 100 = best)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SocialPhotoResolution

- Type: String | Default value: `[i800,i600]` | Persisted: 1

- Comment: Default resolution when sharing photo using the social floaters

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Socks5AuthType

- Type: String | Default value: `None` | Persisted: 1

- Comment: Selected Auth mechanism for Socks5

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Socks5ProxyEnabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use Socks5 Proxy

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Socks5ProxyHost

- Type: String | Default value: `` | Persisted: 1

- Comment: Socks 5 Proxy Host

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Socks5ProxyPort

- Type: U32 | Default value: `1080` | Persisted: 1

- Comment: Socks 5 Proxy Port

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SortFriendsFirst

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Specifies whether friends will be sorted first in Call Log

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SpeakerParticipantRemoveDelay

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Timeout to remove participants who is not in channel before removed from list of active speakers (text/voice chat)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SpeedTest

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Performance testing mode, no network

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SpellCheck

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable spellchecking on line and text editors

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SpellCheckDictionary

- Type: String | Default value: `English (United States),Second Life Glossary` | Persisted: 1

- Comment: Current primary and secondary dictionaries used for spell checking

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StartUpToastLifeTime

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Number of seconds while a StartUp toast exist

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsAutoRun

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Play back autopilot

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsFile

- Type: String | Default value: `fs.txt` | Persisted: 1

- Comment: Filename for stats logging output

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsFrametimeEventThreshold

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: The percentage that the frametime difference must exceed in order to register a frametime event. 0.1 = 10%, 0.25 = 25%, etc.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsFrametimeSampleSeconds

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: The number of seconds to sample extended frametime data (percentiles, stddev).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsNumRuns

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Loop autopilot playback this number of times

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsPilotFile

- Type: String | Default value: `pilot.txt` | Persisted: 1

- Comment: Filename for stats logging autopilot path

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsPilotXMLFile

- Type: String | Default value: `pilot.xml` | Persisted: 1

- Comment: Filename for stats logging extended autopilot path

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsQuitAfterRuns

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Quit application after this number of autopilot playback runs

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsReportFileInterval

- Type: F32 | Default value: `0.2` | Persisted: 1

- Comment: Interval to save viewer stats file data

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsReportMaxDuration

- Type: F32 | Default value: `300` | Persisted: 1

- Comment: Maximum seconds for viewer stats file data, prevents huge file

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsReportSkipZeroDataSaves

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: In viewer stats data file, skip saving entry if there is no data

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsSessionTrackFrameStats

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Track rendering and network statistics

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StatsSummaryFile

- Type: String | Default value: `fss.txt` | Persisted: 1

- Comment: Filename for stats logging summary

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## StopMicCaptureWhenMuted

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Check to stop microphone capture while muted. May cause a hiss on unmute but prevents bluetooth devices always being in voice mode.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SwitchToSharedEnvAfterTeleport

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Switch to Shared Environment after teleport

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SyncMaterialSettings

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: SyncMaterialSettings

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## SystemLanguage

- Type: String | Default value: `en` | Persisted: 1

- Comment: Language indicated by system settings (for UI)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TabToTextFieldsOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: TAB key takes you to next text entry field, instead of next widget

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TargetFPS

- Type: U32 | Default value: `15` | Persisted: 1

- Comment: Desired minimum FPS

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TeleportArrivalDelay

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: Time to wait before displaying world during teleport (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TeleportLocalDelay

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Delay to prevent teleports after starting an in-sim teleport. (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TermsAndConditionsURL

- Type: String | Default value: `https://lindenlab.com/legal/second-life-terms-and-conditions` | Persisted: 1

- Comment: URL pointing to Terms and Conditions page

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TermsOfServiceURL

- Type: String | Default value: `https://lindenlab.com/tos` | Persisted: 1

- Comment: URL pointing to Terms of Service page

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TerrainColorHeightRange

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Altitude range over which a given terrain texture has effect (meters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TerrainColorStartHeight

- Type: F32 | Default value: `20.0` | Persisted: 1

- Comment: Starting altitude for terrain texturing (meters)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TerrainPaintBitDepth

- Type: U32 | Default value: `5` | Persisted: 1

- Comment: Bit depth for future terrain paint map operations. Min: 1. Max: 8. Takes effect when the paint map is created or modified. Modifications to an existing paintmap of different bit depth will have lower precision.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TerrainPaintResolution

- Type: U32 | Default value: `2048` | Persisted: 1

- Comment: Resolution of the terrain paint map in pixels. Rounded to a power of two. Min: 16. Max: RenderMaxTextureResolution. Takes effect when the paint map is created.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TestGridStatusRSSFromFile

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: For testing only: Don't update rss xml file from server.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureCameraBoost

- Type: F32 | Default value: `8.0` | Persisted: 0

- Comment: Amount to boost resolution of textures that are important to the camera.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureDecodeDisabled

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, do not fetch and decode any textures

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureDisable

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, do not load textures for in-world content

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureDiscardBackgroundedTime

- Type: F32 | Default value: `60.0` | Persisted: 1

- Comment: Specify how long to wait before discarding texture data after viewer is backgrounded.  (zero or negative to disable)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureDiscardLevel

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Specify texture resolution (0 = highest, 5 = lowest)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureDiscardMinimizedTime

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Specify how long to wait before discarding texture data after viewer is minimized.  (zero or negative to disable)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureFetchConcurrency

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Maximum number of HTTP connections used for texture fetches

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureFetchFakeFailureRate

- Type: F32 | Default value: `0.0` | Persisted: 1

- Comment: Simulate HTTP fetch failures for some server bake textures.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureFetchMinTimeToLog

- Type: F32 | Default value: `2.0` | Persisted: 1

- Comment: If texture fetching time exceeds this value, texture fetch tester will log info

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureFetchUpdateMinCount

- Type: S32 | Default value: `32` | Persisted: 1

- Comment: Minimum number of textures to update per frame

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureLivePreview

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Preview selections in texture picker or material picker immediately

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureLoadFullRes

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: If TRUE, always load textures at full resolution (discard = 0)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureLoggingThreshold

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Specifies the byte threshold at which texture download data should be sent to the sim.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureNewByteRange

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the new more accurate byte range computation for j2c discard levels

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureReverseByteRange

- Type: S32 | Default value: `50` | Persisted: 1

- Comment: Minimal percent of the optimal byte range allowed to render a given discard level

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureSaveLocation

- Type: String | Default value: `` | Persisted: 0

- Comment: Current location for bulk saving textures to disk

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureScaleMaxAreaFactor

- Type: F32 | Default value: `25.0` | Persisted: 1

- Comment: Limits how texture scale affects area calculation.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TextureScaleMinAreaFactor

- Type: F32 | Default value: `0.0095` | Persisted: 1

- Comment: Limits how texture scale affects area calculation.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ThreadPoolSizes

- Type: LLSD | Default value: `General 1 ImageDecode 9` | Persisted: 1

- Comment: Map of size overrides for specific thread pools.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ThrottleBandwidthKBPS

- Type: F32 | Default value: `3000.0` | Persisted: 1

- Comment: Maximum allowable downstream bandwidth (kilo bits per second)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TipToastMessageLineCount

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Max line count of text message on tip toast.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToastButtonWidth

- Type: S32 | Default value: `90` | Persisted: 1

- Comment: 
                Default width of buttons in the toast.
      Notes:
      If required width will be less then this one, a button will be reshaped to default size , otherwise to required
                Change of this parameter will affect the layout of buttons in notification toast.


- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToastFadingTime

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Number of seconds while a toast is fading 

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToastGap

- Type: S32 | Default value: `7` | Persisted: 1

- Comment: Gap between toasts on a screen (min. value is 5)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToolTipDelay

- Type: F32 | Default value: `0.699999988079` | Persisted: 1

- Comment: Seconds before displaying tooltip when mouse stops over UI element

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToolTipFadeTime

- Type: F32 | Default value: `0.2` | Persisted: 1

- Comment: Seconds over which tooltip fades away

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToolTipFastDelay

- Type: F32 | Default value: `0.1` | Persisted: 1

- Comment: Seconds before displaying tooltip when mouse stops over UI element (when a tooltip is already visible)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToolTipVisibleTimeFar

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Fade tooltip after after time passes (seconds) while mouse not near tooltip

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToolTipVisibleTimeNear

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Fade tooltip after after time passes (seconds) while mouse near tooltip or original position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToolTipVisibleTimeOver

- Type: F32 | Default value: `1000.0` | Persisted: 1

- Comment: Fade tooltip after after time passes (seconds) while mouse over tooltip

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ToolboxAutoMove

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [NOT USED]

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TrackFocusObject

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Camera tracks last object zoomed on

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TranslateChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Translate incoming chat messages

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TranslateLanguage

- Type: String | Default value: `default` | Persisted: 1

- Comment: Translate Language specifier

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TranslationService

- Type: String | Default value: `azure` | Persisted: 1

- Comment: Translation API to use. (google|azure)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TuningFPSStrategy

- Type: U32 | Default value: `1` | Persisted: 1

- Comment: Strategy to use when tuning FPS. 0=Tune avatar rendering only, 1=Tune both avatar and global scene settings, 2=Tune only global scene.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TutorialURL

- Type: String | Default value: `` | Persisted: 0

- Comment: URL for tutorial menu item, set automatically during login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## TypeAheadTimeout

- Type: F32 | Default value: `1.5` | Persisted: 1

- Comment: Time delay before clearing type-ahead buffer in lists (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIAutoScale

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Keep UI scale consistent across different resolutions

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIButtonOrigHPad

- Type: S32 | Default value: `6` | Persisted: 1

- Comment: UI Button Original Horizontal Pad

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UICheckboxctrlHPad

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Checkbox Control Horizontal Pad

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UICheckboxctrlSpacing

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: UI Checkbox Control Spacing

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UICheckboxctrlVPad

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Checkbox Control Vertical Pad

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UICloseBoxFromTop

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Distance from top of floater to top of close box icon, pixels

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIExtraTriangleHeight

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: UI extra triangle height

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIExtraTriangleWidth

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI extra triangle width

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIFloaterCloseBoxSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: Size of UI floater close box size

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIFloaterHPad

- Type: S32 | Default value: `6` | Persisted: 1

- Comment: Size of UI floater horizontal pad

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIFloaterTestBool

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Example saved setting for the test floater

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultAlphaUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultEyesUUID

- Type: String | Default value: `6522e74d-1660-4e7f-b601-6f48c1659a77` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultGlovesUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultHairUUID

- Type: String | Default value: `7ca39b4c-bd19-4699-aff7-f93fd03d3e7b` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultJacketUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultPantsUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultShirtUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultShoesUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultSkirtUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultSocksUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIImgDefaultUnderwearUUID

- Type: String | Default value: `5748decc-f629-461c-9a36-a35a221fe21f` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UILineEditorCursorThickness

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Line Editor Cursor Thickness

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIMaxComboWidth

- Type: S32 | Default value: `500` | Persisted: 1

- Comment: Maximum width of combo box

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIMinimizedWidth

- Type: S32 | Default value: `160` | Persisted: 1

- Comment: Size of UI floater minimized width

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIMultiSliderctrlSpacing

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI multi slider ctrl spacing

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIMultiTrackHeight

- Type: S32 | Default value: `6` | Persisted: 1

- Comment: UI multi track height

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditMarkerBrightness

- Type: F32 | Default value: `0.4` | Persisted: 1

- Comment: UI Preedit Marker Brightness

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditMarkerGap

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Preedit Marker Gap

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditMarkerPosition

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI Preedit Marker Position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditMarkerThickness

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Preedit Marker Thickness

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditStandoutBrightness

- Type: F32 | Default value: `0.6` | Persisted: 1

- Comment: UI Preedit Standout Brightness

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditStandoutGap

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Preedit Standout Gap

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditStandoutPosition

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI Preedit Standout Position

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreeditStandoutThickness

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI Preedit Standout Thickness

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIPreviewMaterial

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Whether or not PBR material swatch is enabled

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIResizeBarHeight

- Type: S32 | Default value: `3` | Persisted: 1

- Comment: Size of UI resize bar height

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIScaleFactor

- Type: F32 | Default value: `1.0` | Persisted: 1

- Comment: Size of UI relative to default layout on 1024x768 screen

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UIScrollbarSize

- Type: S32 | Default value: `15` | Persisted: 1

- Comment: UI scrollbar size

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISliderctrlHeight

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI slider ctrl height

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISliderctrlSpacing

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI slider ctrl spacing

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndAlert

- Type: String | Default value: `ed124764-705d-d497-167a-182cd9fa2e6c` | Persisted: 1

- Comment: Sound file for alerts (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndBadKeystroke

- Type: String | Default value: `2ca849ba-2885-4bc3-90ef-d4987a5b983a` | Persisted: 1

- Comment: Sound file for invalid keystroke (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndChatMention

- Type: String | Default value: `03e77cb5-592c-5b33-d271-2e46497c3fb3` | Persisted: 1

- Comment: Sound file for chat mention(uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndChatPing

- Type: String | Default value: `7dd36df6-2624-5438-f988-fdf8588a0ad9` | Persisted: 1

- Comment: Sound file for chat ping(uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndClick

- Type: String | Default value: `4c8c3c77-de8d-bde2-b9b8-32635e0fd4a6` | Persisted: 1

- Comment: Sound file for mouse click (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndClickRelease

- Type: String | Default value: `4c8c3c77-de8d-bde2-b9b8-32635e0fd4a6` | Persisted: 1

- Comment: Sound file for mouse button release (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndDebugSpamToggle

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Log UI sound effects as they are played

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndHealthReductionF

- Type: String | Default value: `219c5d93-6c09-31c5-fb3f-c5fe7495c115` | Persisted: 1

- Comment: Sound file for female pain (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndHealthReductionM

- Type: String | Default value: `e057c244-5768-1056-c37e-1537454eeb62` | Persisted: 1

- Comment: Sound file for male pain (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndHealthReductionThreshold

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Amount of health reduction required to trigger "pain" sound

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndInvalidOp

- Type: String | Default value: `4174f859-0d3d-c517-c424-72923dc21f65` | Persisted: 1

- Comment: Sound file for invalid operations (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndMoneyChangeDown

- Type: String | Default value: `104974e3-dfda-428b-99ee-b0d4e748d3a3` | Persisted: 1

- Comment: Sound file for L$ balance increase (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndMoneyChangeThreshold

- Type: F32 | Default value: `50.0` | Persisted: 1

- Comment: Amount of change in L$ balance required to trigger "money" sound

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndMoneyChangeUp

- Type: String | Default value: `77a018af-098e-c037-51a6-178f05877c6f` | Persisted: 1

- Comment: Sound file for L$ balance decrease(uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndNewIncomingIMSession

- Type: String | Default value: `67cc2844-00f3-2b3c-b991-6418d01e1bb7` | Persisted: 1

- Comment: Sound file for new instant message session(uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndObjectCreate

- Type: String | Default value: `f4a0660f-5446-dea2-80b7-6482a082803c` | Persisted: 1

- Comment: Sound file for object creation (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndObjectDelete

- Type: String | Default value: `0cb7b00a-4c10-6948-84de-a93c09af2ba9` | Persisted: 1

- Comment: Sound file for object deletion (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndObjectRezIn

- Type: String | Default value: `3c8fc726-1fd6-862d-fa01-16c5b2568db6` | Persisted: 1

- Comment: Sound file for rezzing objects (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndObjectRezOut

- Type: String | Default value: `00000000-0000-0000-0000-000000000000` | Persisted: 1

- Comment: Sound file for derezzing objects (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndRestart

- Type: String | Default value: `b92a0f64-7709-8811-40c5-16afd624a45f` | Persisted: 1

- Comment: Sound file for region restarting (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndSnapshot

- Type: String | Default value: `3d09f582-3851-c0e0-f5ba-277ac5c73fb4` | Persisted: 1

- Comment: Sound file for taking a snapshot (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndStartIM

- Type: String | Default value: `c825dfbc-9827-7e02-6507-3713d18916c1` | Persisted: 1

- Comment: Sound file for starting a new IM session (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndTeleportOut

- Type: String | Default value: `d7a9a565-a013-2a69-797d-5332baa1a947` | Persisted: 1

- Comment: Sound file for teleporting (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndTyping

- Type: String | Default value: `5e191c7b-8996-9ced-a177-b2ac32bfea06` | Persisted: 1

- Comment: Sound file for starting to type a chat message (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndWindowClose

- Type: String | Default value: `2c346eda-b60c-ab33-1119-b8941916a499` | Persisted: 1

- Comment: Sound file for closing a window (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISndWindowOpen

- Type: String | Default value: `c80260ba-41fd-8a46-768a-6bf236360e3a` | Persisted: 1

- Comment: Sound file for opening a window (uuid for sound asset)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISpinctrlBtnHeight

- Type: S32 | Default value: `11` | Persisted: 1

- Comment: UI spin control button height

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISpinctrlBtnWidth

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI spin control button width

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UISpinctrlSpacing

- Type: S32 | Default value: `2` | Persisted: 1

- Comment: UI spin control spacing

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrArrowBtnSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI Tab Container Arrow Button Size

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrButtonPanelOverlap

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: UI Tab Container Button Panel Overlap

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrCloseBtnSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI Tab Container Close Button Size

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrTabHPad

- Type: S32 | Default value: `4` | Persisted: 1

- Comment: UI Tab Container Tab Horizontal Pad

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrTabPartialWidth

- Type: S32 | Default value: `12` | Persisted: 1

- Comment: UI Tab Container Tab Partial Width

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrVertTabMinWidth

- Type: S32 | Default value: `100` | Persisted: 1

- Comment: UI Tab Container Vertical Tab Minimum Width

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrvArrowBtnSize

- Type: S32 | Default value: `16` | Persisted: 1

- Comment: UI Tab Container V Arrow Button Size

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabCntrvPad

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: UI Tab Container V Pad

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UITabPadding

- Type: S32 | Default value: `15` | Persisted: 1

- Comment: UI Tab Padding

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UpdateAppWindowTitleBar

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Updates the application window title bar with brief information about user/location

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UpdateRememberPasswordSetting

- Type: Boolean | Default value: `0` | Persisted: 0

- Comment: Save 'rememeber password' setting for current user.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UpdaterServiceSetting

- Type: U32 | Default value: `3` | Persisted: 1

- Comment: Configure updater service.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UpdaterShowReleaseNotes

- Type: S32 | Default value: `1` | Persisted: 1

- Comment: Enables displaying of the Release notes in a web floater after update. 0 - don't show, 1 - show, 2 - show even for test viewers

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UpdaterWillingToTest

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether or not the updater should offer Beta upgrades.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UploadBakedTexOld

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Forces the baked texture pipeline to upload using the old method.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UploadsEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly uploaded item

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UploadsNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly uploaded items can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UploadsNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly uploaded items can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UploadsNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly uploaded items can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UploadsShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly uploaded items are shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## Use24HourClock

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: 12 vs 24. At the moment coverage is partial

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseAltKeyForMenus

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Access menus via keyboard by tapping Alt

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseChatBubbles

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show chat above avatars head in chat bubbles

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseCircuitCodeMaxRetries

- Type: S32 | Default value: `3` | Persisted: 0

- Comment: Max timeout count for the initial UseCircuitCode message

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseCircuitCodeTimeout

- Type: F32 | Default value: `5.0` | Persisted: 0

- Comment: Timeout duration in seconds for the initial UseCircuitCode message

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseDebugLogin

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Provides extra control over which grid to connect to

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseDebugMenus

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Turns on "Debug" menu

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseDefaultColorPicker

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Use color picker supplied by operating system

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseDisplayNames

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use new, changeable, unicode names

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseEnergy

- Type: Boolean | Default value: `1` | Persisted: 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseFreezeFrame

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Freeze time when taking snapshots.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseGroupMemberPagination

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Enable pagination of group memeber list 50 members at a time.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseNewWalkRun

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Replace standard walk/run animations with new ones.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseObjectCacheOcclusion

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable object cache level object culling based on occlusion (coverage) by other objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseOcclusion

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Enable object culling based on occlusion (coverage) by other objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UsePeopleAPI

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Use the people API cap for avatar name fetching, use old legacy protocol if false. Requires restart.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseStartScreen

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Whether to load a start screen image or not.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UseWebPagesOnPrims

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: [NOT USED]

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UserConnectionPort

- Type: U32 | Default value: `0` | Persisted: 1

- Comment: Port that this client transmits on.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UserLogFile

- Type: String | Default value: `` | Persisted: 1

- Comment: User specified log file name.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UserLoginInfo

- Type: LLSD | Default value: `` | Persisted: 1

- Comment: User login data.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## UserSessionSettingsFile

- Type: String | Default value: `` | Persisted: 0

- Comment: User settings that are a applied per session (not saved).

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VelocityInterpolate

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Extrapolate object motion from last packet based on received velocity

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VersionChannelName

- Type: String | Default value: `` | Persisted: 1

- Comment: Version information generated by running the viewer

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceAutomaticGainControl

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Voice Automatic Gain Control

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceCallsFriendsOnly

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: (Deprecated) Only accept voice calls from residents on your friends list

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceCallsRejectGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Silently reject all incoming group voice calls.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceDisableMic

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Completely disable the ability to open the mic.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceEarLocation

- Type: S32 | Default value: `0` | Persisted: 1

- Comment: Location of the virtual ear for voice

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceEchoCancellation

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Voice Echo Cancellation

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceImageLevel0

- Type: String | Default value: `041ee5a0-cb6a-9ac5-6e49-41e9320507d5` | Persisted: 1

- Comment: Texture UUID for voice image level 0

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceImageLevel1

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 1

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceImageLevel2

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 2

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceImageLevel3

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 3

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceImageLevel4

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 4

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceImageLevel5

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 5

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceImageLevel6

- Type: String | Default value: `29de489d-0491-fb00-7dab-f9e686d31e83` | Persisted: 1

- Comment: Texture UUID for voice image level 6

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceInputAudioDevice

- Type: String | Default value: `Default` | Persisted: 1

- Comment: Audio input device to use for voice

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceMorphingEnabled

- Type: Boolean | Default value: `1` | Persisted: 0

- Comment: Whether or not to enable Voice Morphs and show the UI.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceNoiseSuppressionLevel

- Type: U32 | Default value: `4` | Persisted: 1

- Comment: Voice Noise Suppression Level

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceOutputAudioDevice

- Type: String | Default value: `Default` | Persisted: 1

- Comment: Audio output device to use for voice

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceParticipantLeftRemoveDelay

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Timeout to remove participants who has left Voice chat from the list in Voice Controls Panel

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceServerType

- Type: String | Default value: `` | Persisted: 0

- Comment: The type of voice server to use for group, conference, and p2p calls.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## VoiceVisualizerEnabled

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Display voice dot indicator above an avatar

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WLSkyDetail

- Type: U32 | Default value: `64` | Persisted: 1

- Comment: [OBSOLETE]

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WarningsAsChat

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Display warning messages in chat history

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WatchdogEnabled

- Type: S32 | Default value: `0` | Persisted: 0

- Comment: Controls whether the thread watchdog timer is activated. Value is S32. Set to -1 to defer to built-in default.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WaterGLFogDensityScale

- Type: F32 | Default value: `0.02` | Persisted: 1

- Comment: Maps shader water fog density to gl fog density

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WaterGLFogDepthFloor

- Type: F32 | Default value: `0.25` | Persisted: 1

- Comment: Controls how dark water gl fog can get

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WaterGLFogDepthScale

- Type: F32 | Default value: `50.0` | Persisted: 1

- Comment: Controls how quickly gl fog gets dark under water

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WearFolderLimit

- Type: U32 | Default value: `125` | Persisted: 1

- Comment: Limits number of items in the folder that can be replaced/added to current outfit

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WearablesEveryoneCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Everyone can copy the newly created clothing or body part

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WearablesNextOwnerCopy

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created clothing or body part can be copied by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WearablesNextOwnerModify

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created clothing or body part can be modified by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WearablesNextOwnerTransfer

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Newly created clothing or body part can be resold or given away by next owner

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WearablesShareWithGroup

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Newly created clothing or body part is shared with the currently active group

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WebContentWindowLimit

- Type: S32 | Default value: `5` | Persisted: 1

- Comment: Maximum number of web browser windows that can be open at once in the Web content floater (0 for no limit)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WebProfileFloaterRect

- Type: Rect | Default value: `0 680 485 0` | Persisted: 1

- Comment: Web profile floater dimensions

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WindLightUseAtmosShaders

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: DEPRECATED (only true supported) - Whether to enable or disable WindLight atmospheric shaders.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WindowHeight

- Type: U32 | Default value: `738` | Persisted: 1

- Comment: SL viewer window height

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WindowMaximized

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: SL viewer window maximized on login

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WindowWidth

- Type: U32 | Default value: `1024` | Persisted: 1

- Comment: SL viewer window width

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WindowX

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: X coordinate of upper left corner of SL viewer window, relative to upper left corner of primary display (pixels)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## WindowY

- Type: S32 | Default value: `10` | Persisted: 1

- Comment: Y coordinate of upper left corner of SL viewer window, relative to upper left corner of primary display (pixels)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## XferThrottle

- Type: F32 | Default value: `150000.0` | Persisted: 1

- Comment: Maximum allowable downstream bandwidth for asset transfers (bits per second)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## YawFromMousePosition

- Type: F32 | Default value: `90.0` | Persisted: 1

- Comment: Horizontal range over which avatar head tracks mouse position (degrees of head rotation from left of window to right)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## YieldTime

- Type: S32 | Default value: `-1` | Persisted: 1

- Comment: Yield some time to the local host.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## YouAreHereDistance

- Type: F32 | Default value: `10.0` | Persisted: 1

- Comment: Radius of distance for banner that indicates if the resident is "on" the Place.(meters from avatar to requested place)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ZoomDirect

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Map Joystick zoom axis directly to camera zoom.

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## ZoomTime

- Type: F32 | Default value: `0.40000000596` | Persisted: 1

- Comment: Time of transition between different camera modes (seconds)

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## always_showable_floaters

- Type: LLSD | Default value: `snapshot postcard mini_map beacons` | Persisted: 1

- Comment: Floaters that can be shown despite mouselook mode

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## max_texture_dimension_X

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: Maximum texture width for user uploaded textures

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## max_texture_dimension_Y

- Type: S32 | Default value: `1024` | Persisted: 1

- Comment: Maximum texture height for user uploaded textures

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## moapbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight media on a prim sources

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## moonbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show direction to the Moon

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## particlesbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight particle generators

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## physicalbeacon

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Beacon / Highlight physical objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## renderbeacons

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight particle generators

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## renderhighlights

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Beacon / Highlight scripted objects with touch function

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## scriptsbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight scripted objects

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## scripttouchbeacon

- Type: Boolean | Default value: `1` | Persisted: 1

- Comment: Beacon / Highlight scripted objects with touch function

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## soundsbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Beacon / Highlight sound generators

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## sourceid

- Type: String | Default value: `` | Persisted: 1

- Comment: Identify referring agency to Linden web servers

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## sunbeacon

- Type: Boolean | Default value: `0` | Persisted: 1

- Comment: Show direction to the Sun

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.


## teleport_offer_invitation_max_length

- Type: S32 | Default value: `178` | Persisted: 1

- Comment: Maximum length of teleport offer invitation line editor. 254 - max_location_url_length(76) = 178

- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.
