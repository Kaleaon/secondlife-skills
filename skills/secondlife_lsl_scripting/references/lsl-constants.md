# LSL Constants Reference (generated from secondlife/lsl-definitions)


## ACTIVE

- Type: integer | Value: `0x2`

- Meaning: Objects running a script or physically moving (using server resources). In llDetectedType(), it identifies physical objects and agents. In llSensor() or llSensorRepeat(), it searches for moving physical objects or scripted objects.

- Member of enum/flag group: DetectType


## AGENT

- Type: integer | Value: `0x1`

- Meaning: Agents (avatars). In llDetectedType, it indicates an avatar. In llSensor or llSensorRepeat, it searches for avatars by legacy name (functionally identical to AGENT_BY_LEGACY_NAME, though using AGENT_BY_LEGACY_NAME is recommended instead).

- Member of enum/flag group: DetectType


## AGENT_ALWAYS_RUN

- Type: integer | Value: `0x1000`

- Meaning: Used with llGetAgentInfo to determine if the queried avatar has 'Always Run' enabled or is using tap-tap-hold.

- Member of enum/flag group: AgentInfo


## AGENT_ATTACHMENTS

- Type: integer | Value: `0x2`

- Meaning: Used with llGetAgentInfo to determine if the queried avatar has attachments.

- Member of enum/flag group: AgentInfo


## AGENT_AUTOMATED

- Type: integer | Value: `0x4000`

- Meaning: Used with llGetAgentInfo to identify if the avatar is registered with Linden Lab as an automated/scripted agent (bot).

- Member of enum/flag group: AgentInfo


## AGENT_AUTOPILOT

- Type: integer | Value: `0x2000`

- Meaning: Used with llGetAgentInfo to determine if the avatar is in autopilot mode, which is enabled when the user selects 'Go Here' on the ground or uses double-click autopilot.

- Member of enum/flag group: AgentInfo


## AGENT_AWAY

- Type: integer | Value: `0x40`

- Meaning: Used with llGetAgentInfo to determine if the avatar is in 'away' mode, which indicates they toggled away or have been inactive for too long.

- Member of enum/flag group: AgentInfo


## AGENT_BUSY

- Type: integer | Value: `0x800`

- Meaning: Used with llGetAgentInfo to determine if the avatar is in 'busy' mode.

- Member of enum/flag group: AgentInfo


## AGENT_BY_LEGACY_NAME

- Type: integer | Value: `0x1`

- Meaning: Used to find agents by legacy name. In llDetectedType, it indicates an avatar. In llSensor or llSensorRepeat, it searches for avatars by legacy name.

- Member of enum/flag group: DetectType


## AGENT_BY_USERNAME

- Type: integer | Value: `0x10`

- Meaning: Used to find agents by username (see Avatar Names).

- Member of enum/flag group: DetectType


## AGENT_CROUCHING

- Type: integer | Value: `0x400`

- Meaning: Used with llGetAgentInfo to determine if the avatar is crouching.

- Member of enum/flag group: AgentInfo


## AGENT_FLOATING_VIA_SCRIPTED_ATTACHMENT

- Type: integer | Value: `0x8000`

- Meaning: Used with llGetAgentInfo to determine if the avatar is floating or hovering because of a scripted attachment using either llSetHoverHeight or llGroundRepel.

- Member of enum/flag group: AgentInfo


## AGENT_FLYING

- Type: integer | Value: `0x1`

- Meaning: Used with llGetAgentInfo to determine if the queried avatar is flying or hovering.

- Member of enum/flag group: AgentInfo


## AGENT_IN_AIR

- Type: integer | Value: `0x100`

- Meaning: Used with llGetAgentInfo to determine if the avatar is in the air (jumping, flying, or falling).

- Member of enum/flag group: AgentInfo


## AGENT_LIST_PARCEL

- Type: integer | Value: `1`

- Meaning: Agents on the same parcel where the script is running.

- Member of enum/flag group: AgentListScope


## AGENT_LIST_PARCEL_OWNER

- Type: integer | Value: `2`

- Meaning: Agents on any parcel in the region where the parcel owner is the same as the owner of the parcel under the scripted object.

- Member of enum/flag group: AgentListScope


## AGENT_LIST_REGION

- Type: integer | Value: `4`

- Meaning: Returns any or all agents in the region.

- Member of enum/flag group: AgentListScope


## AGENT_MOUSELOOK

- Type: integer | Value: `0x8`

- Meaning: Used with llGetAgentInfo to determine if the avatar is in mouselook.

- Member of enum/flag group: AgentInfo


## AGENT_ON_OBJECT

- Type: integer | Value: `0x20`

- Meaning: Used with llGetAgentInfo to determine if the avatar is sitting on an object and linked to it.

- Member of enum/flag group: AgentInfo


## AGENT_SCRIPTED

- Type: integer | Value: `0x4`

- Meaning: Used with llGetAgentInfo to determine if the avatar is carrying scripted objects or has scripted attachments.

- Member of enum/flag group: AgentInfo


## AGENT_SITTING

- Type: integer | Value: `0x10`

- Meaning: Used with llGetAgentInfo to determine if the avatar is sitting.

- Member of enum/flag group: AgentInfo


## AGENT_TYPING

- Type: integer | Value: `0x200`

- Meaning: Used with llGetAgentInfo to determine if the avatar is typing.

- Member of enum/flag group: AgentInfo


## AGENT_WALKING

- Type: integer | Value: `0x80`

- Meaning: Used with llGetAgentInfo to determine if the queried avatar is walking, running, or crouch walking.

- Member of enum/flag group: AgentInfo


## ALL_SIDES

- Type: integer | Value: `-1`

- Meaning: Selects all sides of an object in an applicable function.

- Member of enum/flag group: Faces


## ANIM_ON

- Type: integer | Value: `0x1`

- Meaning: Enables texture animation. This must be set to start the animation and cleared to stop it.

- Member of enum/flag group: TextureAnimMode


## ATTACH_ANY_HUD

- Type: integer | Value: `-1`

- Meaning: A special constant representing all HUD attachment points when filtering for any HUD attachment.

- Member of enum/flag group: AttachPoint


## ATTACH_AVATAR_CENTER

- Type: integer | Value: `40`

- Meaning: Attachment point for the avatar's geometric center or root.

- Member of enum/flag group: AttachPoint


## ATTACH_BACK

- Type: integer | Value: `9`

- Meaning: Attachment point for the avatar's back.

- Member of enum/flag group: AttachPoint


## ATTACH_BELLY

- Type: integer | Value: `28`

- Meaning: Attachment point for the avatar's belly, stomach, or tummy.

- Member of enum/flag group: AttachPoint


## ATTACH_CHEST

- Type: integer | Value: `1`

- Meaning: Attachment point for the avatar's chest or sternum.

- Member of enum/flag group: AttachPoint


## ATTACH_CHIN

- Type: integer | Value: `12`

- Meaning: Attachment point for the avatar's chin.

- Member of enum/flag group: AttachPoint


## ATTACH_FACE_JAW

- Type: integer | Value: `47`

- Meaning: Attachment point for the avatar's jaw.

- Member of enum/flag group: AttachPoint


## ATTACH_FACE_LEAR

- Type: integer | Value: `48`

- Meaning: Attachment point for the avatar's left ear (extended).

- Member of enum/flag group: AttachPoint


## ATTACH_FACE_LEYE

- Type: integer | Value: `50`

- Meaning: Attachment point for the avatar's left eye (extended).

- Member of enum/flag group: AttachPoint


## ATTACH_FACE_REAR

- Type: integer | Value: `49`

- Meaning: Attachment point for the avatar's right ear (extended).

- Member of enum/flag group: AttachPoint


## ATTACH_FACE_REYE

- Type: integer | Value: `51`

- Meaning: Attachment point for the avatar's right eye (extended).

- Member of enum/flag group: AttachPoint


## ATTACH_FACE_TONGUE

- Type: integer | Value: `52`

- Meaning: Attachment point for the avatar's tongue.

- Member of enum/flag group: AttachPoint


## ATTACH_GROIN

- Type: integer | Value: `53`

- Meaning: Attachment point for the avatar's groin.

- Member of enum/flag group: AttachPoint


## ATTACH_HEAD

- Type: integer | Value: `2`

- Meaning: Attachment point for the avatar's head.

- Member of enum/flag group: AttachPoint


## ATTACH_HIND_LFOOT

- Type: integer | Value: `54`

- Meaning: Attachment point for the avatar's left hind foot.

- Member of enum/flag group: AttachPoint


## ATTACH_HIND_RFOOT

- Type: integer | Value: `55`

- Meaning: Attachment point for the avatar's right hind foot.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_BOTTOM

- Type: integer | Value: `37`

- Meaning: Attachment point for HUD Bottom.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_BOTTOM_LEFT

- Type: integer | Value: `36`

- Meaning: Attachment point for HUD Bottom Left.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_BOTTOM_RIGHT

- Type: integer | Value: `38`

- Meaning: Attachment point for HUD Bottom Right.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_CENTER_1

- Type: integer | Value: `35`

- Meaning: Attachment point for HUD Center.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_CENTER_2

- Type: integer | Value: `31`

- Meaning: Attachment point for HUD Center 2.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_TOP_CENTER

- Type: integer | Value: `33`

- Meaning: Attachment point for HUD Top Center.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_TOP_LEFT

- Type: integer | Value: `34`

- Meaning: Attachment point for HUD Top Left.

- Member of enum/flag group: AttachPoint


## ATTACH_HUD_TOP_RIGHT

- Type: integer | Value: `32`

- Meaning: Attachment point for HUD Top Right.

- Member of enum/flag group: AttachPoint


## ATTACH_LEAR

- Type: integer | Value: `13`

- Meaning: Attachment point for the avatar's left ear.

- Member of enum/flag group: AttachPoint


## ATTACH_LEFT_PEC

- Type: integer | Value: `29`

- Meaning: Attachment point for the avatar's left pectoral.

- Member of enum/flag group: AttachPoint


## ATTACH_LEYE

- Type: integer | Value: `15`

- Meaning: Attachment point for the avatar's left eye.

- Member of enum/flag group: AttachPoint


## ATTACH_LFOOT

- Type: integer | Value: `7`

- Meaning: Attachment point for the avatar's left foot.

- Member of enum/flag group: AttachPoint


## ATTACH_LHAND

- Type: integer | Value: `5`

- Meaning: Attachment point for the avatar's left hand.

- Member of enum/flag group: AttachPoint


## ATTACH_LHAND_RING1

- Type: integer | Value: `41`

- Meaning: Attachment point for the avatar's left ring finger.

- Member of enum/flag group: AttachPoint


## ATTACH_LHIP

- Type: integer | Value: `25`

- Meaning: Attachment point for the avatar's left hip.

- Member of enum/flag group: AttachPoint


## ATTACH_LLARM

- Type: integer | Value: `21`

- Meaning: Attachment point for the avatar's left lower arm.

- Member of enum/flag group: AttachPoint


## ATTACH_LLLEG

- Type: integer | Value: `27`

- Meaning: Attachment point for the avatar's left lower leg.

- Member of enum/flag group: AttachPoint


## ATTACH_LPEC

- Type: integer | Value: `30`

- Meaning: Attachment point for the avatar's right pectoral (deprecated, use ATTACH_RIGHT_PEC).

- Member of enum/flag group: AttachPoint


## ATTACH_LSHOULDER

- Type: integer | Value: `3`

- Meaning: Attachment point for the avatar's left shoulder.

- Member of enum/flag group: AttachPoint


## ATTACH_LUARM

- Type: integer | Value: `20`

- Meaning: Attachment point for the avatar's left upper arm.

- Member of enum/flag group: AttachPoint


## ATTACH_LULEG

- Type: integer | Value: `26`

- Meaning: Attachment point for the avatar's left upper leg.

- Member of enum/flag group: AttachPoint


## ATTACH_LWING

- Type: integer | Value: `45`

- Meaning: Attachment point for the avatar's left wing.

- Member of enum/flag group: AttachPoint


## ATTACH_MOUTH

- Type: integer | Value: `11`

- Meaning: Attachment point for the avatar's mouth.

- Member of enum/flag group: AttachPoint


## ATTACH_NECK

- Type: integer | Value: `39`

- Meaning: Attachment point for the avatar's neck.

- Member of enum/flag group: AttachPoint


## ATTACH_NOSE

- Type: integer | Value: `17`

- Meaning: Attachment point for the avatar's nose.

- Member of enum/flag group: AttachPoint


## ATTACH_PELVIS

- Type: integer | Value: `10`

- Meaning: Attachment point for the avatar's pelvis.

- Member of enum/flag group: AttachPoint


## ATTACH_REAR

- Type: integer | Value: `14`

- Meaning: Attachment point for the avatar's right ear.

- Member of enum/flag group: AttachPoint


## ATTACH_REYE

- Type: integer | Value: `16`

- Meaning: Attachment point for the avatar's right eye.

- Member of enum/flag group: AttachPoint


## ATTACH_RFOOT

- Type: integer | Value: `8`

- Meaning: Attachment point for the avatar's right foot.

- Member of enum/flag group: AttachPoint


## ATTACH_RHAND

- Type: integer | Value: `6`

- Meaning: Attachment point for the avatar's right hand (the default attachment point).

- Member of enum/flag group: AttachPoint


## ATTACH_RHAND_RING1

- Type: integer | Value: `42`

- Meaning: Attachment point for the avatar's right ring finger.

- Member of enum/flag group: AttachPoint


## ATTACH_RHIP

- Type: integer | Value: `22`

- Meaning: Attachment point for the avatar's right hip.

- Member of enum/flag group: AttachPoint


## ATTACH_RIGHT_PEC

- Type: integer | Value: `30`

- Meaning: Attachment point for the avatar's right pectoral.

- Member of enum/flag group: AttachPoint


## ATTACH_RLARM

- Type: integer | Value: `19`

- Meaning: Attachment point for the avatar's right lower arm.

- Member of enum/flag group: AttachPoint


## ATTACH_RLLEG

- Type: integer | Value: `24`

- Meaning: Attachment point for the avatar's right lower leg.

- Member of enum/flag group: AttachPoint


## ATTACH_RPEC

- Type: integer | Value: `29`

- Meaning: Attachment point for the avatar's left pectoral (deprecated, use ATTACH_LEFT_PEC).

- Member of enum/flag group: AttachPoint


## ATTACH_RSHOULDER

- Type: integer | Value: `4`

- Meaning: Attachment point for the avatar's right shoulder.

- Member of enum/flag group: AttachPoint


## ATTACH_RUARM

- Type: integer | Value: `18`

- Meaning: Attachment point for the avatar's right upper arm.

- Member of enum/flag group: AttachPoint


## ATTACH_RULEG

- Type: integer | Value: `23`

- Meaning: Attachment point for the avatar's right upper leg.

- Member of enum/flag group: AttachPoint


## ATTACH_RWING

- Type: integer | Value: `46`

- Meaning: Attachment point for the avatar's right wing.

- Member of enum/flag group: AttachPoint


## ATTACH_TAIL_BASE

- Type: integer | Value: `43`

- Meaning: Attachment point for the avatar's tail base.

- Member of enum/flag group: AttachPoint


## ATTACH_TAIL_TIP

- Type: integer | Value: `44`

- Meaning: Attachment point for the avatar's tail tip.

- Member of enum/flag group: AttachPoint


## AVOID_CHARACTERS

- Type: integer | Value: `1`

- Member of enum/flag group: CharacterAvoidanceMode


## AVOID_DYNAMIC_OBSTACLES

- Type: integer | Value: `2`

- Member of enum/flag group: CharacterAvoidanceMode


## AVOID_NONE

- Type: integer | Value: `0`

- Member of enum/flag group: CharacterAvoidanceMode


## BEACON_MAP

- Type: integer | Value: `1`

- Meaning: Causes llMapBeacon to optionally display and focus the world map on the avatar's viewer.

- Member of enum/flag group: MapBeaconParam


## CAMERA_ACTIVE

- Type: integer | Value: `12`

- Meaning: Option flag used with llSetCameraParams to turn scripted control of the camera on or off.

- Member of enum/flag group: CameraParam


## CAMERA_BEHINDNESS_ANGLE

- Type: integer | Value: `8`

- Meaning: Sets the angle in degrees within which the camera is not constrained by changes in target rotation.

- Member of enum/flag group: CameraParam


## CAMERA_BEHINDNESS_LAG

- Type: integer | Value: `9`

- Meaning: Sets how strongly the camera is forced to stay behind the target if outside of the behindness angle.

- Member of enum/flag group: CameraParam


## CAMERA_DISTANCE

- Type: integer | Value: `7`

- Meaning: Sets how far away the camera wants to be from its target.

- Member of enum/flag group: CameraParam


## CAMERA_FOCUS

- Type: integer | Value: `17`

- Meaning: Sets camera focus (target position) in region coordinates.

- Member of enum/flag group: CameraParam


## CAMERA_FOCUS_LAG

- Type: integer | Value: `6`

- Meaning: Sets how much the camera lags as it aims toward the target.

- Member of enum/flag group: CameraParam


## CAMERA_FOCUS_LOCKED

- Type: integer | Value: `22`

- Meaning: Option flag used with llSetCameraParams to lock the camera focus so it does not move.

- Member of enum/flag group: CameraParam


## CAMERA_FOCUS_OFFSET

- Type: integer | Value: `1`

- Meaning: Adjusts the camera focus position relative to the target.

- Member of enum/flag group: CameraParam


## CAMERA_FOCUS_THRESHOLD

- Type: integer | Value: `11`

- Meaning: Sets the radius of a sphere around the camera's target position within which its focus is not affected by target motion.

- Member of enum/flag group: CameraParam


## CAMERA_PITCH

- Type: integer | Value: `0`

- Meaning: Adjusts the angular amount that the camera aims straight ahead versus straight down, maintaining the same distance (analogous to 'incidence').

- Member of enum/flag group: CameraParam


## CAMERA_POSITION

- Type: integer | Value: `13`

- Meaning: Sets camera position in region coordinates.

- Member of enum/flag group: CameraParam


## CAMERA_POSITION_LAG

- Type: integer | Value: `5`

- Meaning: Sets how much the camera lags as it moves toward its ideal position.

- Member of enum/flag group: CameraParam


## CAMERA_POSITION_LOCKED

- Type: integer | Value: `21`

- Meaning: Option flag used with llSetCameraParams to lock the camera position so it does not move.

- Member of enum/flag group: CameraParam


## CAMERA_POSITION_THRESHOLD

- Type: integer | Value: `10`

- Meaning: Sets the radius of a sphere around the camera's ideal position within which it is not affected by target motion.

- Member of enum/flag group: CameraParam


## CHANGED_ALLOWED_DROP

- Type: integer | Value: `0x40`

- Meaning: Object inventory changed because a user other than the owner (or the owner if the object is no-mod) added an item. This is only possible if enabled via llAllowInventoryDrop.

- Member of enum/flag group: ChangeType


## CHANGED_COLOR

- Type: integer | Value: `0x2`

- Meaning: Object's Blinn-Phong color or alpha parameters have changed.

- Member of enum/flag group: ChangeType


## CHANGED_INVENTORY

- Type: integer | Value: `0x1`

- Meaning: Prim inventory has changed by someone who has modification rights to it.

- Member of enum/flag group: ChangeType


## CHANGED_LINK

- Type: integer | Value: `0x20`

- Meaning: Number of prims making up the object or avatars seated on it has changed. Also occurs when duplicating a linked object or when a prim changes type or shape. Does not trigger on attach/detach, sit/unsit in attachments, or single prim duplication.

- Member of enum/flag group: ChangeType


## CHANGED_MEDIA

- Type: integer | Value: `0x800`

- Meaning: Prim Media on the prim has changed.

- Member of enum/flag group: ChangeType


## CHANGED_OWNER

- Type: integer | Value: `0x80`

- Meaning: Object has changed owners. Triggers in the original object when a user takes it, copies it, or deeds it to a group, and in the new object when it is first rezzed.

- Member of enum/flag group: ChangeType


## CHANGED_REGION

- Type: integer | Value: `0x100`

- Meaning: Object has changed regions by crossing a boundary or teleporting (if attached). Triggers only in the root prim of a linkset.

- Member of enum/flag group: ChangeType


## CHANGED_REGION_START

- Type: integer | Value: `0x400`

- Meaning: Region containing this object has just come online.

- Member of enum/flag group: ChangeType


## CHANGED_RENDER_MATERIAL

- Type: integer | Value: `0x1000`

- Meaning: Render material (prim material ID or material overrides) has changed on one or more faces.

- Member of enum/flag group: ChangeType


## CHANGED_SCALE

- Type: integer | Value: `0x8`

- Meaning: Prim scale of at least one prim in the linked object has changed. Only the root prim receives this event.

- Member of enum/flag group: ChangeType


## CHANGED_SHAPE

- Type: integer | Value: `0x4`

- Meaning: Prim base shape (PRIM_TYPE, such as box, prism, torus, taper, twist, or cut) has changed.

- Member of enum/flag group: ChangeType


## CHANGED_TELEPORT

- Type: integer | Value: `0x200`

- Meaning: Avatar this object is attached to has teleported. Triggers only in the root prim of an attachment. Does not occur for child prims or 'sit teleports'. If scripts are disabled at the destination, the event queues and triggers after moving to a script-enabled parcel.

- Member of enum/flag group: ChangeType


## CHANGED_TEXTURE

- Type: integer | Value: `0x10`

- Meaning: Prim texture parameters (shine/bump settings, repeats, flip, rotation, offset, or texture) have changed.

- Member of enum/flag group: ChangeType


## CHARACTER_ACCOUNT_FOR_SKIPPED_FRAMES

- Type: integer | Value: `14`

- Meaning: If set to FALSE, the pathfinding character will not attempt to catch up on lost time when performance is low, potentially providing more reliable (though potentially more stuttery) movement. Default is TRUE.

- Member of enum/flag group: CharacterParam


## CHARACTER_AVOIDANCE_MODE

- Type: integer | Value: `5`

- Meaning: Specifies which objects a pathfinding character avoids (other characters, dynamic obstacles like fast-moving objects and avatars, or both). Combined using bit flags; setting to AVOID_NONE disables avoidance for both categories.

- Member of enum/flag group: CharacterParam


## CHARACTER_CMD_JUMP

- Type: integer | Value: `0x01`

- Meaning: Makes the character jump. Requires a height parameter between 0.1m and 2.0m as the first element of the llExecCharacterCmd option list.

- Member of enum/flag group: CharacterCommand


## CHARACTER_CMD_SMOOTH_STOP

- Type: integer | Value: `2`

- Meaning: Stops any current pathfinding operation in a smooth fashion.

- Member of enum/flag group: CharacterCommand


## CHARACTER_CMD_STOP

- Type: integer | Value: `0x00`

- Meaning: Stops any current pathfinding operation.

- Member of enum/flag group: CharacterCommand


## CHARACTER_DESIRED_SPEED

- Type: integer | Value: `1`

- Meaning: Constant used to indicate that the following argument is the desired speed (or speed of pursuit in meters per second) for a pathfinding character.

- Member of enum/flag group: CharacterParam


## CHARACTER_DESIRED_TURN_SPEED

- Type: integer | Value: `12`

- Meaning: Specifies the character's maximum speed while turning about the Z-axis (default is 6 meters/second). Note that this is only loosely enforced, and a character may turn at higher speeds under certain conditions.

- Member of enum/flag group: CharacterParam


## CHARACTER_LENGTH

- Type: integer | Value: `3`

- Meaning: Sets the collision capsule length for a pathfinding character. If the value is less than twice the radius plus 0.1m, it automatically adjusts to twice the radius plus 0.1m.

- Member of enum/flag group: CharacterParam


## CHARACTER_MAX_ACCEL

- Type: integer | Value: `8`

- Meaning: Specifies the character's maximum acceleration rate (default is 20 m/s²).

- Member of enum/flag group: CharacterParam


## CHARACTER_MAX_DECEL

- Type: integer | Value: `9`

- Meaning: Specifies the character's maximum deceleration rate (default is 30 m/s²).

- Member of enum/flag group: CharacterParam


## CHARACTER_MAX_SPEED

- Type: integer | Value: `13`

- Meaning: Specifies the character's maximum speed (must be between 0.2 and 50 meters/second; default is 20 m/s). Affects speed when avoiding dynamic obstacles and when traversing low-walkability objects in TRAVERSAL_TYPE_FAST mode.

- Member of enum/flag group: CharacterParam


## CHARACTER_MAX_TURN_RADIUS

- Type: integer | Value: `10`

- Meaning: Specifies the character's turn radius when traveling at CHARACTER_DESIRED_TURN_SPEED (default is 1.25 meters).

- Member of enum/flag group: CharacterParam


## CHARACTER_ORIENTATION

- Type: integer | Value: `4`

- Meaning: Specifies the orientation of the collision capsule for a pathfinding character to denote how to interpret its size. Valid options are VERTICAL and HORIZONTAL.

- Member of enum/flag group: CharacterParam


## CHARACTER_RADIUS

- Type: integer | Value: `2`

- Meaning: Sets the collision capsule radius used to define the size of a pathfinding character.

- Member of enum/flag group: CharacterParam


## CHARACTER_STAY_WITHIN_PARCEL

- Type: integer | Value: `15`

- Meaning: Determines whether a character is restricted to its starting parcel (default is FALSE). If TRUE, parcel boundaries act as one-way obstacles; the character cannot voluntarily leave and pathfinding behaviors (wander, flee, evade, pursue) will only choose goal points within the parcel. If pushed out, it can re-enter but cannot voluntarily leave again.

- Member of enum/flag group: CharacterParam


## CHARACTER_TYPE

- Type: integer | Value: `6`

- Meaning: Specifies the preferred surface and terrain terrain-type for the character (default is CHARACTER_TYPE_NONE). Used to describe preferred surfaces rather than behavior (e.g., cows prefer type B, sheep herded along a road prefer type C).

- Member of enum/flag group: CharacterParam, GetClosestNavPointParam, GetStaticPathParam


## CHARACTER_TYPE_A

- Type: integer | Value: `0`

- Meaning: Used for pathfinding character types that prefer movement consistent with humanoids.

- Member of enum/flag group: CharacterType


## CHARACTER_TYPE_B

- Type: integer | Value: `1`

- Meaning: Used for pathfinding character types that prefer movement consistent with wild animals or off-road vehicles.

- Member of enum/flag group: CharacterType


## CHARACTER_TYPE_C

- Type: integer | Value: `2`

- Meaning: Used for mechanical pathfinding character types or road-going vehicles.

- Member of enum/flag group: CharacterType


## CHARACTER_TYPE_D

- Type: integer | Value: `3`

- Meaning: Used for pathfinding character types that are inconsistent with types A, B, or C.

- Member of enum/flag group: CharacterType


## CHARACTER_TYPE_NONE

- Type: integer | Value: `4`

- Meaning: Used to set no specific pathfinding character type.

- Member of enum/flag group: CharacterType


## CLICK_ACTION_BUY

- Type: integer | Value: `2`

- Meaning: Opens the buy dialog when the prim is clicked or touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_DISABLED

- Type: integer | Value: `8`

- Meaning: Disables click actions. No touches are detected or passed.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_IGNORE

- Type: integer | Value: `9`

- Meaning: Disables click actions. Clicks pass through the object to whatever is behind it, and no touches are detected.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_NONE

- Type: integer | Value: `0`

- Meaning: Performs the default action: triggers touch events when the prim is clicked or touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_OPEN

- Type: integer | Value: `4`

- Meaning: Opens the object inventory dialog when the prim is clicked or touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_OPEN_MEDIA

- Type: integer | Value: `6`

- Meaning: Opens the web media dialog or plays parcel media (without pausing) when the prim is touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_PAY

- Type: integer | Value: `3`

- Meaning: Opens the pay dialog when the prim is clicked or touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_PLAY

- Type: integer | Value: `5`

- Meaning: Enables HTML-on-a-prim or plays/pauses parcel media when the prim is clicked or touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_SIT

- Type: integer | Value: `1`

- Meaning: Causes the avatar to sit on the prim when it is clicked or touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_TOUCH

- Type: integer | Value: `0`

- Meaning: Triggers touch events when the prim is clicked or touched.

- Member of enum/flag group: ClickAction


## CLICK_ACTION_ZOOM

- Type: integer | Value: `7`

- Meaning: Zooms the avatar camera in on the object (Viewer 2) when clicked or touched.

- Member of enum/flag group: ClickAction


## COMBAT_CHANNEL

- Type: integer | Value: `2147483646`

- Meaning: A region-wide channel reserved for combat-related log events. Passing this to llRegionSay adds the message to the combat log, and scripts listening on this channel can monitor the combat log.

- Member of enum/flag group: Channel, ChannelNonPublic


## COMBAT_LOG_ID

- Type: string | Value: `45e0fcfa-2268-4490-a51c-3e51bdfe80d1`

- Meaning: ID used by all combat log messages sent from the region to the COMBAT_CHANNEL. Scripts can filter llListen calls with this ID to receive only system-generated combat log messages.


## CONTENT_TYPE_ATOM

- Type: integer | Value: `4`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/atom+xml'.

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_FORM

- Type: integer | Value: `7`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/x-www-form-urlencoded'.

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_HTML

- Type: integer | Value: `1`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'text/html'. Only valid for embedded browsers on content owned by the viewer; falls back to 'text/plain' otherwise.

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_JSON

- Type: integer | Value: `5`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/json'.

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_LLSD

- Type: integer | Value: `6`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/llsd+xml' (Linden Lab Structured Data).

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_RSS

- Type: integer | Value: `8`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/rss+xml'.

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_TEXT

- Type: integer | Value: `0`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'text/plain'.

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_XHTML

- Type: integer | Value: `3`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/xhtml+xml'.

- Member of enum/flag group: HTTPContentType


## CONTENT_TYPE_XML

- Type: integer | Value: `2`

- Meaning: Sets the 'Content-Type' header of subsequent LSL HTTP server responses via llHTTPResponse to 'application/xml'.

- Member of enum/flag group: HTTPContentType


## CONTROL_BACK

- Type: integer | Value: `0x2`

- Meaning: Tests for the avatar move back control (↓ or S).

- Member of enum/flag group: ControlButton


## CONTROL_DOWN

- Type: integer | Value: `0x20`

- Meaning: Tests for the avatar move down control (PgDn or C).

- Member of enum/flag group: ControlButton


## CONTROL_FWD

- Type: integer | Value: `0x1`

- Meaning: Tests for the avatar move forward control (↑ or W).

- Member of enum/flag group: ControlButton


## CONTROL_LBUTTON

- Type: integer | Value: `0x10000000`

- Meaning: Tests for the avatar left mouse button control.

- Member of enum/flag group: ControlButton


## CONTROL_LEFT

- Type: integer | Value: `0x4`

- Meaning: Tests for the avatar move left control (Shift + ← or Shift + A).

- Member of enum/flag group: ControlButton


## CONTROL_ML_LBUTTON

- Type: integer | Value: `0x40000000`

- Meaning: Tests for the avatar left mouse button control while in mouselook.

- Member of enum/flag group: ControlButton


## CONTROL_RIGHT

- Type: integer | Value: `0x8`

- Meaning: Tests for the avatar move right control (Shift + → or Shift + D).

- Member of enum/flag group: ControlButton


## CONTROL_ROT_LEFT

- Type: integer | Value: `0x100`

- Meaning: Tests for the avatar rotate left control (← or A).

- Member of enum/flag group: ControlButton


## CONTROL_ROT_RIGHT

- Type: integer | Value: `0x200`

- Meaning: Tests for the avatar rotate right control (→ or D).

- Member of enum/flag group: ControlButton


## CONTROL_UP

- Type: integer | Value: `0x10`

- Meaning: Tests for the avatar move up control (PgUp or E).

- Member of enum/flag group: ControlButton


## DAMAGEABLE

- Type: integer | Value: `0x20`

- Meaning: Identifies objects in the world that can process damage. In llDetectedType, it indicates a damageable agent, or an object containing a script with on_damage or final_damage events. Can also filter llSensor/llSensorRepeat calls.

- Member of enum/flag group: DetectType


## DAMAGE_TYPE_ACID

- Type: integer | Value: `1`

- Meaning: Damage caused by a caustic substance, such as acid.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_BLUDGEONING

- Type: integer | Value: `2`

- Meaning: Damage caused by a blunt object, such as a club.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_COLD

- Type: integer | Value: `3`

- Meaning: Damage inflicted by exposure to extreme cold.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_ELECTRIC

- Type: integer | Value: `4`

- Meaning: Damage caused by electricity.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_EMOTIONAL

- Type: integer | Value: `14`

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_FIRE

- Type: integer | Value: `5`

- Meaning: Damage inflicted by exposure to heat or flames.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_FORCE

- Type: integer | Value: `6`

- Meaning: Damage inflicted by a great force or impact (Vertical Sim / SLMC).

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_GENERIC

- Type: integer | Value: `0`

- Meaning: Generic or legacy damage.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_IMPACT

- Type: integer | Value: `-1`

- Meaning: System damage generated by impact with land, terrain, or a prim.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_NECROTIC

- Type: integer | Value: `7`

- Meaning: Damage caused by a direct assault on the life-force.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_PIERCING

- Type: integer | Value: `8`

- Meaning: Damage caused by a piercing object such as a bullet, spear, or arrow (Vertical Sim / SLMC).

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_POISON

- Type: integer | Value: `9`

- Meaning: Damage caused by poison.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_PSYCHIC

- Type: integer | Value: `10`

- Meaning: Damage caused by a direct assault on the mind.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_RADIANT

- Type: integer | Value: `11`

- Meaning: Damage caused by radiation or extreme light.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_SLASHING

- Type: integer | Value: `12`

- Meaning: Damage caused by a slashing object such as a sword or axe.

- Member of enum/flag group: DamageType


## DAMAGE_TYPE_SONIC

- Type: integer | Value: `13`

- Meaning: Damage caused by loud noises, like a Crash Worship concert.

- Member of enum/flag group: DamageType


## DATA_BORN

- Type: integer | Value: `3`

- Meaning: Used with llRequestAgentData to return the agent's account creation ('born on') date as a string in ISO 8601 format (YYYY-MM-DD), based on Pacific Time (not UTC).

- Member of enum/flag group: AgentData


## DATA_NAME

- Type: integer | Value: `2`

- Meaning: Used with llRequestAgentData to return the requested agent's legacy name.

- Member of enum/flag group: AgentData


## DATA_ONLINE

- Type: integer | Value: `1`

- Meaning: Used with llRequestAgentData to return whether the requested agent is online (returns an integer boolean string: TRUE if online, FALSE if offline).

- Member of enum/flag group: AgentData


## DATA_PAYINFO

- Type: integer | Value: `8`

- Meaning: Used with llRequestAgentData to return a string containing the integer mask flag for payment status (contains PAYMENT_INFO_ON_FILE, PAYMENT_INFO_USED, or both).

- Member of enum/flag group: AgentData


## DATA_RATING

- Type: integer | Value: `4`

- Meaning: Deprecated. Used with llRequestAgentData to return the string '0, 0, 0, 0, 0, 0'. It formerly returned a comma-separated list of positive and negative ratings (behavior, appearance, and building) before ratings were removed from SL.

- Member of enum/flag group: AgentData


## DATA_RESERVED_0

- Type: integer | Value: `9`

- Meaning: Reserved for Linden use.

- Member of enum/flag group: AgentData


## DATA_SIM_POS

- Type: integer | Value: `5`

- Meaning: Used with llRequestSimulatorData to return the region's global position as a vector.

- Member of enum/flag group: SimulatorData


## DATA_SIM_RATING

- Type: integer | Value: `7`

- Meaning: Used with llRequestSimulatorData to return the simulator rating string ('PG', 'MATURE', 'ADULT', or 'UNKNOWN').

- Member of enum/flag group: SimulatorData


## DATA_SIM_STATUS

- Type: integer | Value: `6`

- Meaning: Used with llRequestSimulatorData to return the simulator status as a string.

- Member of enum/flag group: SimulatorData


## DEBUG_CHANNEL

- Type: integer | Value: `2147483647`

- Meaning: A chat channel reserved for script debugging and error messages. Passing this to llSay, llWhisper, or llShout prints text to the Script Warning/Error Window and broadcasts it to nearby avatars' script consoles.

- Member of enum/flag group: Channel, ChannelNonPublic


## DEG_TO_RAD

- Type: float | Value: `0.017453293`

- Meaning: Constant 0.017453293 (precise value is PI/180). Multiply a value in degrees by this number to convert it to radians.


## DENSITY

- Type: integer | Value: `1`

- Meaning: Used with llSetPhysicsMaterial to indicate that the density parameter is enabled (which overrides the previous value). Must be between 1.0 and 22587.0 kg/m³.

- Member of enum/flag group: PhysicsMaterialParam


## DEREZ_DIE

- Type: integer | Value: `0`

- Meaning: Used with llDerezObject to immediately delete (kill) the object.

- Member of enum/flag group: DerezMode


## DEREZ_MAKE_TEMP

- Type: integer | Value: `1`

- Meaning: Used with llDerezObject to mark the object as temporary, allowing the simulator to clean it up at a later time.

- Member of enum/flag group: DerezMode


## DEREZ_TO_INVENTORY

- Type: integer | Value: `2`

- Meaning: Used with llDerezObject to return the targeted object to the rezzer's (derezzer's) inventory, saving its current state.

- Member of enum/flag group: DerezMode


## ENVIRONMENT_DAYINFO

- Type: integer | Value: `200`

- Meaning: Day cycle and time information: day_length (seconds in the environment's day cycle), day_offset (seconds offset from GMT), and secs_since_midnight (seconds elapsed since the last day cycle midnight).

- Member of enum/flag group: EnvironmentParamReadOnly


## ENV_INVALID_AGENT

- Type: integer | Value: `-4`

- Meaning: Unable to find the specified agent, or could not find an agent with the specified ID.

- Member of enum/flag group: EnvironmentError


## ENV_INVALID_RULE

- Type: integer | Value: `-5`

- Meaning: There was an issue with one of the rules, or an attempt was made to change an unknown property.

- Member of enum/flag group: EnvironmentError


## ENV_NOT_EXPERIENCE

- Type: integer | Value: `-1`

- Meaning: Attempted to change environments outside an experience, or the script is not running as part of an experience with a valid experience key.

- Member of enum/flag group: EnvironmentError


## ENV_NO_ENVIRONMENT

- Type: integer | Value: `-3`

- Meaning: Environmental settings inventory object could not be found, or there is no environment on this parcel to modify.

- Member of enum/flag group: EnvironmentError


## ENV_NO_EXPERIENCE_LAND

- Type: integer | Value: `-7`

- Meaning: Experience has not been enabled or cannot run on the land.

- Member of enum/flag group: EnvironmentError


## ENV_NO_EXPERIENCE_PERMISSION

- Type: integer | Value: `-2`

- Meaning: Agent has not granted permission to change environments.

- Member of enum/flag group: EnvironmentError


## ENV_NO_PERMISSIONS

- Type: integer | Value: `-9`

- Meaning: Script lacks permissions to modify the environment at this location, or an attempt was made to remove altitude track 0 or 1.

- Member of enum/flag group: EnvironmentError


## ENV_OK

- Type: integer | Value: `1`

- Meaning: Agent, parcel, or region will attempt to change the applied environment.

- Member of enum/flag group: EnvironmentError


## ENV_THROTTLE

- Type: integer | Value: `-8`

- Meaning: Scripts have exceeded the throttle limit. Wait and retry the request.

- Member of enum/flag group: EnvironmentError


## ENV_VALIDATION_FAIL

- Type: integer | Value: `-6`

- Meaning: Could not validate the environmental settings or values passed.

- Member of enum/flag group: EnvironmentError


## EOF

- Type: string | Value: `\n\n\n`

- Meaning: Value returned by llGetNotecardLine (through the dataserver event) and llGetNotecardLineSync when the requested line is past the end of the notecard. Equal to three newline characters ("\n\n\n").


## ERR_GENERIC

- Type: integer | Value: `-1`

- Meaning: An inexplicable and generic error where nothing is known about the cause.

- Member of enum/flag group: ReturnObjectsError


## ERR_MALFORMED_PARAMS

- Type: integer | Value: `-3`

- Meaning: Return value for llReturnObject* functions indicating that the parameters passed are malformed.

- Member of enum/flag group: ReturnObjectsError


## ERR_PARCEL_PERMISSIONS

- Type: integer | Value: `-2`

- Meaning: Return value for llReturnObject* functions indicating a lack of permissions to perform the task on the specified parcel.

- Member of enum/flag group: ReturnObjectsError


## ERR_RUNTIME_PERMISSIONS

- Type: integer | Value: `-4`

- Meaning: Return value for llReturnObject* functions indicating the script lacks the runtime permissions required to perform the requested task.

- Member of enum/flag group: ReturnObjectsError


## ERR_THROTTLED

- Type: integer | Value: `-5`

- Meaning: Return value for llReturnObject* functions indicating that the task has been throttled and should be retried later.

- Member of enum/flag group: ReturnObjectsError


## ESTATE_ACCESS_ALLOWED_AGENT_ADD

- Type: integer | Value: `4`

- Meaning: Used as an input parameter for llManageEstateAccess to add an agent to the estate's Allowed Residents list.

- Member of enum/flag group: EstateAccessParam


## ESTATE_ACCESS_ALLOWED_AGENT_REMOVE

- Type: integer | Value: `8`

- Meaning: Used as an input parameter for llManageEstateAccess to remove an agent from the estate's Allowed Residents list.

- Member of enum/flag group: EstateAccessParam


## ESTATE_ACCESS_ALLOWED_GROUP_ADD

- Type: integer | Value: `16`

- Meaning: Used as an input parameter for llManageEstateAccess to add a group to the estate's Allowed Groups list.

- Member of enum/flag group: EstateAccessParam


## ESTATE_ACCESS_ALLOWED_GROUP_REMOVE

- Type: integer | Value: `32`

- Meaning: Used as an input parameter for llManageEstateAccess to remove a group from the estate's Allowed Groups list.

- Member of enum/flag group: EstateAccessParam


## ESTATE_ACCESS_BANNED_AGENT_ADD

- Type: integer | Value: `64`

- Meaning: Used as an input parameter for llManageEstateAccess to add an agent to the estate's Banned Residents list.

- Member of enum/flag group: EstateAccessParam


## ESTATE_ACCESS_BANNED_AGENT_REMOVE

- Type: integer | Value: `128`

- Meaning: Used as an input parameter for llManageEstateAccess to remove an agent from the estate's Banned Residents list.

- Member of enum/flag group: EstateAccessParam


## FALSE

- Type: integer | Value: `0`

- Meaning: Constant representing a boolean FALSE value. Used in conditional structures or variables to improve readability over the integer value (0).


## FILTER_FLAGS

- Type: integer | Value: `2`

- Meaning: Flags used to control which attachments are returned.

- Member of enum/flag group: AttachedListFilterParam


## FILTER_FLAG_HUDS

- Type: integer | Value: `0x0001`

- Meaning: Filter flag used with llGetAttachedListFiltered to include HUDs with matching experiences in the returned result.

- Member of enum/flag group: AttachedListFilterFlag


## FILTER_INCLUDE

- Type: integer | Value: `1`

- Meaning: Filter parameter used to include a specific attachment point.

- Member of enum/flag group: AttachedListFilterParam


## FORCE_DIRECT_PATH

- Type: integer | Value: `1`

- Meaning: Forces the pathfinding character to navigate in a straight line toward the specified position (can be set to TRUE or FALSE).

- Member of enum/flag group: CharacterNavigateParam


## FRICTION

- Type: integer | Value: `2`

- Meaning: Used with llSetPhysicsMaterial to enable the friction override. The value must be between 0.0 and 255.0.

- Member of enum/flag group: PhysicsMaterialParam


## GAME_CONTROL_AXIS_ADVANCE

- Type: integer | Value: `1`

- Meaning: Forward/backward movement. Modal axis index 1 for AVATAR, MOUSELOOK, and CAPTIVE modes.


## GAME_CONTROL_AXIS_BOOM

- Type: integer | Value: `4`

- Meaning: Camera up/down movement. Modal axis index 4 for FLYCAM mode.


## GAME_CONTROL_AXIS_DOLLY

- Type: integer | Value: `1`

- Meaning: Camera forward/backward movement. Modal axis index 1 for FLYCAM mode.


## GAME_CONTROL_AXIS_LEFTX

- Type: integer | Value: `0`

- Meaning: Left stick X axis. Canonical axis index 0.

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_LEFTY

- Type: integer | Value: `1`

- Meaning: Left stick Y axis. Canonical axis index 1.

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_LEFT_TRIGGER

- Type: integer | Value: `4`

- Meaning: Left trigger. Canonical axis index 4.

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_LOOK

- Type: integer | Value: `3`

- Meaning: Looking up/down. Modal axis index 3 for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_AXIS_PAN

- Type: integer | Value: `2`

- Meaning: Camera pan left/right. Modal axis index 2 for FLYCAM mode.


## GAME_CONTROL_AXIS_RIGHTX

- Type: integer | Value: `2`

- Meaning: Right stick X axis. Canonical axis index 2.

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_RIGHTY

- Type: integer | Value: `3`

- Meaning: Right stick Y axis. Canonical axis index 3.

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_RIGHT_TRIGGER

- Type: integer | Value: `5`

- Meaning: Right trigger. Canonical axis index 5.

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_RISE

- Type: integer | Value: `4`

- Meaning: Up/down movement. Modal axis index 4 for AVATAR, MOUSELOOK, and CAPTIVE modes.


## GAME_CONTROL_AXIS_ROLL

- Type: integer | Value: `5`

- Meaning: Camera roll. Modal axis index 5 for FLYCAM mode.


## GAME_CONTROL_AXIS_STRAFE

- Type: integer | Value: `0`

- Meaning: Left/right movement. Modal axis index 0 for AVATAR, MOUSELOOK, and CAPTIVE modes.


## GAME_CONTROL_AXIS_TILT

- Type: integer | Value: `3`

- Meaning: Camera tilt up/down. Modal axis index 3 for FLYCAM mode.


## GAME_CONTROL_AXIS_TRIGGERLEFT

- Type: integer | Value: `4`

- Meaning: Left trigger. Canonical axis index 4 (deprecated, use GAME_CONTROL_AXIS_LEFT_TRIGGER).

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_TRIGGERRIGHT

- Type: integer | Value: `5`

- Meaning: Right trigger. Canonical axis index 5 (deprecated, use GAME_CONTROL_AXIS_RIGHT_TRIGGER).

- Member of enum/flag group: GameControlAxis


## GAME_CONTROL_AXIS_TRUCK

- Type: integer | Value: `0`

- Meaning: Camera lateral (left/right) movement. Modal axis index 0 for FLYCAM mode.


## GAME_CONTROL_AXIS_TURN

- Type: integer | Value: `2`

- Meaning: Turning left/right. Modal axis index 2 for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_AXIS_ZOOM

- Type: integer | Value: `6`

- Meaning: Camera zoom in/out. Modal axis index 6 for AVATAR, MOUSELOOK, CAPTIVE, and FLYCAM modes.


## GAME_CONTROL_BUTTON_A

- Type: integer | Value: `0x1`

- Meaning: Bottom face button (deprecated, use GAME_CONTROL_BUTTON_SOUTH).

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_ADVANCE_BACK

- Type: integer | Value: `0x1000`

- Meaning: Move backward. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_ADVANCE_FORWARD

- Type: integer | Value: `0x800`

- Meaning: Move forward. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_B

- Type: integer | Value: `0x2`

- Meaning: Right face button (deprecated, use GAME_CONTROL_BUTTON_EAST).

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_BACK

- Type: integer | Value: `0x10`

- Meaning: Select/back button (deprecated, use GAME_CONTROL_BUTTON_SELECT).

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_CROUCH

- Type: integer | Value: `0x2`

- Meaning: Crouch. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_CURSOR_BUTTON_LEFT

- Type: integer | Value: `0x200`

- Meaning: Left mouse button click. Modal button for MOUSELOOK and CURSOR modes.


## GAME_CONTROL_BUTTON_CURSOR_BUTTON_RIGHT

- Type: integer | Value: `0x400`

- Meaning: Right mouse button click. Modal button for MOUSELOOK and CURSOR modes.


## GAME_CONTROL_BUTTON_DOLLY_BACK

- Type: integer | Value: `0x1000`

- Meaning: Camera dolly backward. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_DOLLY_FORWARD

- Type: integer | Value: `0x800`

- Meaning: Camera dolly forward. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_DPAD_DOWN

- Type: integer | Value: `0x1000`

- Meaning: D-pad down.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_DPAD_LEFT

- Type: integer | Value: `0x2000`

- Meaning: D-pad left.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_DPAD_RIGHT

- Type: integer | Value: `0x4000`

- Meaning: D-pad right.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_DPAD_UP

- Type: integer | Value: `0x800`

- Meaning: D-pad up.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_EAST

- Type: integer | Value: `0x2`

- Meaning: Right face button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_GUIDE

- Type: integer | Value: `0x20`

- Meaning: Home/guide button (deprecated, use GAME_CONTROL_BUTTON_HOME).

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_HOME

- Type: integer | Value: `0x20`

- Meaning: Home/guide button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_JUMP

- Type: integer | Value: `0x1`

- Meaning: Jump. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_LEFTSHOULDER

- Type: integer | Value: `0x200`

- Meaning: Left shoulder/bumper button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_LEFTSTICK

- Type: integer | Value: `0x80`

- Meaning: Left analog stick click.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_MISC1

- Type: integer | Value: `0x8000`

- Meaning: Miscellaneous button 1.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_NORTH

- Type: integer | Value: `0x8`

- Meaning: Top face button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_PADDLE1

- Type: integer | Value: `0x10000`

- Meaning: Paddle button 1.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_PADDLE2

- Type: integer | Value: `0x20000`

- Meaning: Paddle button 2.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_PADDLE3

- Type: integer | Value: `0x40000`

- Meaning: Paddle button 3.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_PADDLE4

- Type: integer | Value: `0x80000`

- Meaning: Paddle button 4.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_PAN_LEFT

- Type: integer | Value: `0x4`

- Meaning: Camera pan left. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_PAN_RIGHT

- Type: integer | Value: `0x2`

- Meaning: Camera pan right. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_RESET

- Type: integer | Value: `0x80`

- Meaning: Reset camera to default view. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_RIGHTSHOULDER

- Type: integer | Value: `0x400`

- Meaning: Right shoulder/bumper button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_RIGHTSTICK

- Type: integer | Value: `0x100`

- Meaning: Right analog stick click.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_ROLL_CCW

- Type: integer | Value: `0x200`

- Meaning: Roll camera counter-clockwise. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_ROLL_CW

- Type: integer | Value: `0x400`

- Meaning: Roll camera clockwise. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_SELECT

- Type: integer | Value: `0x10`

- Meaning: Select/back button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_SIT

- Type: integer | Value: `0x4`

- Meaning: Toggle sitting. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_SOUTH

- Type: integer | Value: `0x1`

- Meaning: Bottom face button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_START

- Type: integer | Value: `0x40`

- Meaning: Start/menu button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_STRAFE_LEFT

- Type: integer | Value: `0x2000`

- Meaning: Strafe left. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_STRAFE_RIGHT

- Type: integer | Value: `0x4000`

- Meaning: Strafe right. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_TOGGLE_ALT_ZOOM

- Type: integer | Value: `0x10`

- Meaning: Toggle alt-zoom. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_TOGGLE_CURSOR

- Type: integer | Value: `0x10`

- Meaning: Toggle cursor mode. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_TOGGLE_FLYCAM

- Type: integer | Value: `0x100`

- Meaning: Toggle flycam mode. Modal button for all modes.


## GAME_CONTROL_BUTTON_TOGGLE_FOLLOW

- Type: integer | Value: `0x40`

- Meaning: Toggle camera follow mode. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_TOGGLE_MOUSELOOK

- Type: integer | Value: `0x40`

- Meaning: Toggle mouselook mode. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_TOGGLE_SPEAK

- Type: integer | Value: `0x20`

- Meaning: Toggle voice speak. Modal button for AVATAR, MOUSELOOK, CAPTIVE, and CURSOR modes.


## GAME_CONTROL_BUTTON_TOUCHPAD

- Type: integer | Value: `0x100000`

- Meaning: Touchpad click.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_TRUCK_LEFT

- Type: integer | Value: `0x2000`

- Meaning: Camera truck left. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_TRUCK_RIGHT

- Type: integer | Value: `0x4000`

- Meaning: Camera truck right. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_WEST

- Type: integer | Value: `0x4`

- Meaning: Left face button.

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_X

- Type: integer | Value: `0x4`

- Meaning: Left face button (deprecated, use GAME_CONTROL_BUTTON_WEST).

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_Y

- Type: integer | Value: `0x8`

- Meaning: Top face button (deprecated, use GAME_CONTROL_BUTTON_NORTH).

- Member of enum/flag group: GameControlButton


## GAME_CONTROL_BUTTON_ZOOM_IN

- Type: integer | Value: `0x8`

- Meaning: Zoom camera in. Modal button for FLYCAM mode.


## GAME_CONTROL_BUTTON_ZOOM_OUT

- Type: integer | Value: `0x1`

- Meaning: Zoom camera out. Modal button for FLYCAM mode.


## GAME_CONTROL_MODE_AVATAR

- Type: integer | Value: `0`

- Member of enum/flag group: GameControlMode


## GAME_CONTROL_MODE_CAPTIVE

- Type: integer | Value: `3`

- Member of enum/flag group: GameControlMode


## GAME_CONTROL_MODE_CURSOR

- Type: integer | Value: `4`

- Member of enum/flag group: GameControlMode


## GAME_CONTROL_MODE_FLYCAM

- Type: integer | Value: `2`

- Member of enum/flag group: GameControlMode


## GAME_CONTROL_MODE_MOUSELOOK

- Type: integer | Value: `1`

- Member of enum/flag group: GameControlMode


## GCNP_GET_WALKABILITY

- Type: integer | Value: `2`

- Member of enum/flag group: GetClosestNavPointParam


## GCNP_RADIUS

- Type: integer | Value: `0`

- Meaning: Used with llGetClosestNavPoint to limit how far out to search for a navigation point.

- Member of enum/flag group: GetClosestNavPointParam


## GCNP_STATIC

- Type: integer | Value: `1`

- Meaning: Used with llGetClosestNavPoint to specify that the test should use the static navmesh, ignoring all dynamic obstacles.

- Member of enum/flag group: GetClosestNavPointParam


## GRAVITY_MULTIPLIER

- Type: integer | Value: `8`

- Meaning: Used with llSetPhysicsMaterial to enable the gravity multiplier override. The value must be between -1.0 and +28.0.

- Member of enum/flag group: PhysicsMaterialParam


## HORIZONTAL

- Type: integer | Value: `1`

- Meaning: Constant indicating that the collision capsule orientation for a pathfinding character is horizontal.

- Member of enum/flag group: CharacterOrientation


## HTTP_ACCEPT

- Type: integer | Value: `8`

- Meaning: Used with llHTTPRequest to override the default Accept header with custom MIME types (such as application/json, text/html, etc.). Responses with unlisted content types will return status 415.

- Member of enum/flag group: HTTPRequestParam


## HTTP_BODY_MAXLENGTH

- Type: integer | Value: `2`

- Meaning: Sets the maximum (UTF-8 encoded) byte length of the HTTP response body. The maximum limit depends on the VM being used (Mono Max: 16384 bytes, LSO Max: 4096 bytes).

- Member of enum/flag group: HTTPRequestParam


## HTTP_BODY_TRUNCATED

- Type: integer | Value: `0`

- Meaning: Indicates the response body truncation point in bytes.

- Member of enum/flag group: HTTPResponseError


## HTTP_CUSTOM_HEADER

- Type: integer | Value: `5`

- Meaning: Adds custom HTTP headers to the request (up to 8 per request). At the SLua level, provide a string-keyed table mapping header names to values; the serializer emits one HTTP_CUSTOM_HEADER/key/value triple per entry. Some default or sensitive headers are blocked for security reasons.

- Member of enum/flag group: HTTPRequestParam


## HTTP_EXTENDED_ERROR

- Type: integer | Value: `9`

- Meaning: If set to TRUE, llHTTPRequest always returns a key. If an error occurs during the request, detailed error information (delivered in an RFC 7807 JSON block) is reported through the http_response event using that key.

- Member of enum/flag group: HTTPRequestParam


## HTTP_METHOD

- Type: integer | Value: `0`

- Meaning: Specifies the HTTP method ('GET', 'POST', 'PUT', or 'DELETE') for the request.

- Member of enum/flag group: HTTPRequestParam


## HTTP_MIMETYPE

- Type: integer | Value: `1`

- Meaning: Specifies the request Content-Type MIME type. Text types should define a charset (e.g., 'text/plain;charset=utf-8'). Use 'application/x-www-form-urlencoded' to emulate HTML forms.

- Member of enum/flag group: HTTPRequestParam


## HTTP_PRAGMA_NO_CACHE

- Type: integer | Value: `6`

- Meaning: Controls whether the 'Pragma: no-cache' header is sent with the HTTP request. When SendHeader is TRUE (default), the header is sent; when FALSE, it is omitted.

- Member of enum/flag group: HTTPRequestParam


## HTTP_USER_AGENT

- Type: integer | Value: `7`

- Meaning: Appends a custom string to the default LSL User-Agent header value. Must follow HTTP standard syntax (e.g., 'My-Script-Name/1.0'). Spaces are not allowed and will cause a script error; use hyphens instead.

- Member of enum/flag group: HTTPRequestParam


## HTTP_VERBOSE_THROTTLE

- Type: integer | Value: `4`

- Meaning: If set to TRUE, shouts error messages to DEBUG_CHANNEL if the outgoing request rate exceeds the server limit. If FALSE, these error messages are suppressed.

- Member of enum/flag group: HTTPRequestParam


## HTTP_VERIFY_CERT

- Type: integer | Value: `3`

- Meaning: If set to TRUE, the server's SSL certificate must be verifiable using a standard certificate authority when making HTTPS requests. If FALSE, any SSL certificate is accepted.

- Member of enum/flag group: HTTPRequestParam


## IMG_USE_BAKED_AUX1

- Type: string | Value: `9742065b-19b5-297c-858a-29711d539043`


## IMG_USE_BAKED_AUX2

- Type: string | Value: `03642e83-2bd1-4eb9-34b4-4c47ed586d2d`


## IMG_USE_BAKED_AUX3

- Type: string | Value: `edd51b77-fc10-ce7a-4b3d-011dfc349e4f`


## IMG_USE_BAKED_EYES

- Type: string | Value: `52cc6bb6-2ee5-e632-d3ad-50197b1dcb8a`


## IMG_USE_BAKED_HAIR

- Type: string | Value: `09aac1fb-6bce-0bee-7d44-caac6dbb6c63`


## IMG_USE_BAKED_HEAD

- Type: string | Value: `5a9f4a74-30f2-821c-b88d-70499d3e7183`


## IMG_USE_BAKED_LEFTARM

- Type: string | Value: `ff62763f-d60a-9855-890b-0c96f8f8cd98`


## IMG_USE_BAKED_LEFTLEG

- Type: string | Value: `8e915e25-31d1-cc95-ae08-d58a47488251`


## IMG_USE_BAKED_LOWER

- Type: string | Value: `24daea5f-0539-cfcf-047f-fbc40b2786ba`


## IMG_USE_BAKED_SKIRT

- Type: string | Value: `43529ce8-7faa-ad92-165a-bc4078371687`


## IMG_USE_BAKED_UPPER

- Type: string | Value: `ae2de45c-d252-50b8-5c6e-19f39ce79317`


## INVENTORY_ALL

- Type: integer | Value: `-1`

- Meaning: Used with inventory functions to specify that all types of inventory items should be retrieved.

- Member of enum/flag group: InventoryType


## INVENTORY_ANIMATION

- Type: integer | Value: `20`

- Meaning: Used with inventory functions to filter or retrieve items of the ANIMATION type.

- Member of enum/flag group: InventoryType


## INVENTORY_BODYPART

- Type: integer | Value: `13`

- Meaning: Used with inventory functions to filter or retrieve items of the BODYPART type.

- Member of enum/flag group: InventoryType


## INVENTORY_CLOTHING

- Type: integer | Value: `5`

- Meaning: Used with inventory functions to filter or retrieve items of the CLOTHING type.

- Member of enum/flag group: InventoryType


## INVENTORY_GESTURE

- Type: integer | Value: `21`

- Meaning: Used with inventory functions to filter or retrieve items of the GESTURE type.

- Member of enum/flag group: InventoryType


## INVENTORY_LANDMARK

- Type: integer | Value: `3`

- Meaning: Used with inventory functions to filter or retrieve items of the LANDMARK type.

- Member of enum/flag group: InventoryType


## INVENTORY_MATERIAL

- Type: integer | Value: `57`

- Meaning: Used with inventory functions to filter or retrieve items of the MATERIAL type.

- Member of enum/flag group: InventoryType


## INVENTORY_NONE

- Type: integer | Value: `-1`

- Meaning: Value returned by inventory functions indicating that the specified inventory item does not exist.

- Member of enum/flag group: InventoryType


## INVENTORY_NOTECARD

- Type: integer | Value: `7`

- Meaning: Used with inventory functions to filter or retrieve items of the NOTECARD type.

- Member of enum/flag group: InventoryType


## INVENTORY_OBJECT

- Type: integer | Value: `6`

- Meaning: Used with inventory functions to filter or retrieve items of the OBJECT type.

- Member of enum/flag group: InventoryType


## INVENTORY_SCRIPT

- Type: integer | Value: `10`

- Meaning: Used with inventory functions to filter or retrieve items of the SCRIPT type.

- Member of enum/flag group: InventoryType


## INVENTORY_SETTING

- Type: integer | Value: `56`

- Meaning: Used with inventory functions to filter or retrieve items of the SETTING type.

- Member of enum/flag group: InventoryType


## INVENTORY_SOUND

- Type: integer | Value: `1`

- Meaning: Used with inventory functions to filter or retrieve items of the SOUND type.

- Member of enum/flag group: InventoryType


## INVENTORY_TEXTURE

- Type: integer | Value: `0`

- Meaning: Used with inventory functions to filter or retrieve items of the TEXTURE type.

- Member of enum/flag group: InventoryType


## JSON_APPEND

- Type: integer | Value: `-1`

- Meaning: A specifier for llJsonSetValue indicating the given value should be appended to the array at the specified level. If the target value is not an array, the existing data will be overwritten and replaced by the new array.


## JSON_ARRAY

- Type: string | Value: `\u{FDD2}`

- Meaning: Used with llList2Json to indicate that the provided list should be encoded and returned as a string-serialized JSON array.


## JSON_DELETE

- Type: string | Value: `\u{FDD8}`

- Meaning: A constant used to delete a value within a JSON text string.


## JSON_FALSE

- Type: string | Value: `\u{FDD7}`

- Meaning: Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a boolean FALSE.


## JSON_INVALID

- Type: string | Value: `\u{FDD0}`

- Meaning: Indicates an invalid state or parameter. Returned by llList2Json when inputs are not well-formed, by llJsonValueType for an invalid JSON type, or by llJsonGetValue when attempting to access a nonexistent location.


## JSON_NULL

- Type: string | Value: `\u{FDD5}`

- Meaning: Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a JSON null.


## JSON_NUMBER

- Type: string | Value: `\u{FDD3}`

- Meaning: Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a number.


## JSON_OBJECT

- Type: string | Value: `\u{FDD1}`

- Meaning: Used with llList2Json to indicate that the provided list is a strided list of key-value pairs to be encoded and returned as a JSON object.


## JSON_STRING

- Type: string | Value: `\u{FDD4}`

- Meaning: Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a string.


## JSON_TRUE

- Type: string | Value: `\u{FDD6}`

- Meaning: Return value for llJsonValueType indicating that the value at the specified address in a JSON string is a boolean TRUE.


## KFM_CMD_PAUSE

- Type: integer | Value: `2`

- Meaning: Command used with KFM_COMMAND in llSetKeyframedMotion to pause the keyframed motion without resetting it to the start.

- Member of enum/flag group: KeyframedMotionCommand


## KFM_CMD_PLAY

- Type: integer | Value: `0`

- Meaning: Command used with KFM_COMMAND in llSetKeyframedMotion to resume a motion previously stopped by KFM_CMD_STOP or paused by KFM_CMD_PAUSE.

- Member of enum/flag group: KeyframedMotionCommand


## KFM_CMD_STOP

- Type: integer | Value: `1`

- Meaning: Command used with KFM_COMMAND in llSetKeyframedMotion to stop the keyframed motion and reset it to the start.

- Member of enum/flag group: KeyframedMotionCommand


## KFM_COMMAND

- Type: integer | Value: `0`

- Meaning: Option flag in llSetKeyframedMotion followed by KFM_CMD_STOP, KFM_CMD_PLAY, or KFM_CMD_PAUSE to play, stop, or pause the motion.

- Member of enum/flag group: KeyframedMotionParam


## KFM_DATA

- Type: integer | Value: `2`

- Meaning: Option flag in llSetKeyframedMotion followed by a bitwise combination of KFM_TRANSLATION and KFM_ROTATION to specify keyframe data. If absent, both rotation and translation data must be provided.

- Member of enum/flag group: KeyframedMotionParam


## KFM_FORWARD

- Type: integer | Value: `0`

- Meaning: Playback mode used with KFM_MODE in llSetKeyframedMotion (default). It plays the frames sequentially from 1 to N and then stops.

- Member of enum/flag group: KeyframedMotionMode


## KFM_LOOP

- Type: integer | Value: `1`

- Meaning: Playback mode used with KFM_MODE in llSetKeyframedMotion. It plays the frames sequentially from 1 to N, returns to the initial position, and repeats indefinitely.

- Member of enum/flag group: KeyframedMotionMode


## KFM_MODE

- Type: integer | Value: `1`

- Meaning: Option flag in llSetKeyframedMotion followed by KFM_LOOP, KFM_REVERSE, KFM_FORWARD, or KFM_PING_PONG to set the playback mode (defaults to KFM_FORWARD). Must be specified when the keyframe list is provided.

- Member of enum/flag group: KeyframedMotionParam


## KFM_PING_PONG

- Type: integer | Value: `2`

- Meaning: Playback mode used with KFM_MODE in llSetKeyframedMotion.

- Member of enum/flag group: KeyframedMotionMode


## KFM_REVERSE

- Type: integer | Value: `3`

- Meaning: Playback mode used with KFM_MODE in llSetKeyframedMotion. It plays the frames in reverse order (from N down to 1) and then stops.

- Member of enum/flag group: KeyframedMotionMode


## KFM_ROTATION

- Type: integer | Value: `1`

- Meaning: Specifies that rotation data is included in the moves list for llSetKeyframedMotion.

- Member of enum/flag group: KeyframedMotionData


## KFM_TRANSLATION

- Type: integer | Value: `2`

- Meaning: Specifies that translation data is included in the moves list for llSetKeyframedMotion.

- Member of enum/flag group: KeyframedMotionData


## LAND_BRUSH_LARGE

- Type: integer | Value: `2`

- Meaning: Use a large brush size (8m x 8m).

- Member of enum/flag group: ModifyLandBrush


## LAND_BRUSH_MEDIUM

- Type: integer | Value: `1`

- Meaning: Use a medium brush size (4m x 4m)..

- Member of enum/flag group: ModifyLandBrush


## LAND_BRUSH_SMALL

- Type: integer | Value: `0`

- Meaning: Use a small brush size (2m x 2m).

- Member of enum/flag group: ModifyLandBrush


## LAND_LARGE_BRUSH

- Type: integer | Value: `3`

- Meaning: Legacy large brush size (8m x 8m). Note: This constant value is incorrect; use LAND_BRUSH_LARGE instead.

- Member of enum/flag group: ModifyLandBrush


## LAND_LEVEL

- Type: integer | Value: `0`

- Meaning: Action used with llModifyLand to level the land at the prim's center.

- Member of enum/flag group: ModifyLandAction


## LAND_LOWER

- Type: integer | Value: `2`

- Meaning: Action used with llModifyLand to lower the land.

- Member of enum/flag group: ModifyLandAction


## LAND_MEDIUM_BRUSH

- Type: integer | Value: `2`

- Meaning: Legacy medium brush size (4m x 4m). Note: This constant value is incorrect; use LAND_BRUSH_MEDIUM instead.

- Member of enum/flag group: ModifyLandBrush


## LAND_NOISE

- Type: integer | Value: `4`

- Meaning: Action used with llModifyLand to randomize the terrain and make it rough.

- Member of enum/flag group: ModifyLandAction


## LAND_RAISE

- Type: integer | Value: `1`

- Meaning: Action used with llModifyLand to raise the land.

- Member of enum/flag group: ModifyLandAction


## LAND_REVERT

- Type: integer | Value: `5`

- Meaning: Action used with llModifyLand to restore the land to its baked value.

- Member of enum/flag group: ModifyLandAction


## LAND_SMALL_BRUSH

- Type: integer | Value: `1`

- Meaning: Legacy small brush size (2m x 2m). Note: This constant value is incorrect; use LAND_BRUSH_SMALL instead.

- Member of enum/flag group: ModifyLandBrush


## LAND_SMOOTH

- Type: integer | Value: `3`

- Meaning: Action used with llModifyLand to smooth the land.

- Member of enum/flag group: ModifyLandAction


## LEGACY_MASS_FACTOR

- Type: float | Value: `0.01`


## LINKSETDATA_DELETE

- Type: integer | Value: `2`

- Meaning: Action indicating a key was deleted from the linkset datastore via llLinksetDataDelete, llLinksetDataDeleteProtected, or by writing an empty value.

- Member of enum/flag group: LinksetDataAction


## LINKSETDATA_EMEMORY

- Type: integer | Value: `1`

- Meaning: Error code indicating the key and value were too large to write to the linkset datastore.

- Member of enum/flag group: LinksetDataError


## LINKSETDATA_ENOKEY

- Type: integer | Value: `2`

- Meaning: Error code indicating the key name supplied to a linkset datastore operation was empty.

- Member of enum/flag group: LinksetDataError


## LINKSETDATA_EPROTECTED

- Type: integer | Value: `3`

- Meaning: Error code indicating the key is protected from being deleted or overwritten in the linkset datastore.

- Member of enum/flag group: LinksetDataError


## LINKSETDATA_MULTIDELETE

- Type: integer | Value: `3`

- Meaning: Action indicating keys were deleted from the linkset datastore via llLinksetDataDeleteFound. The event's name is a comma-separated list of the deleted keys.

- Member of enum/flag group: LinksetDataAction


## LINKSETDATA_NOTFOUND

- Type: integer | Value: `4`

- Meaning: Error code indicating the specified key could not be found in the linkset datastore.

- Member of enum/flag group: LinksetDataError


## LINKSETDATA_NOUPDATE

- Type: integer | Value: `5`

- Meaning: Status code indicating that the linkset datastore was not updated because the written value matched the existing stored value.

- Member of enum/flag group: LinksetDataError


## LINKSETDATA_OK

- Type: integer | Value: `0`

- Meaning: Status code indicating the linkset datastore operation completed successfully.

- Member of enum/flag group: LinksetDataError


## LINKSETDATA_RESET

- Type: integer | Value: `0`

- Meaning: Action indicating all keys were deleted from the linkset datastore via llLinksetDataReset.

- Member of enum/flag group: LinksetDataAction


## LINKSETDATA_UPDATE

- Type: integer | Value: `1`

- Meaning: Action indicating a key was created or updated in the linkset datastore via llLinksetDataWrite or llLinksetDataWriteProtected.

- Member of enum/flag group: LinksetDataAction


## LINK_ALL_CHILDREN

- Type: integer | Value: `-3`

- Meaning: Refers to all child prims in the linkset (every prim except the root).

- Member of enum/flag group: Links


## LINK_ALL_OTHERS

- Type: integer | Value: `-2`

- Meaning: Refers to every other prim in the linkset, excluding the prim containing the script.

- Member of enum/flag group: Links


## LINK_ROOT

- Type: integer | Value: `1`

- Meaning: Refers to the root prim of the linkset.

- Member of enum/flag group: Link, Links


## LINK_SET

- Type: integer | Value: `-1`

- Meaning: Refers to every prim in the linkset.

- Member of enum/flag group: Links


## LINK_THIS

- Type: integer | Value: `-4`

- Meaning: Refers specifically to the single prim containing the running script.

- Member of enum/flag group: Link, Links


## LIST_STAT_GEOMETRIC_MEAN

- Type: integer | Value: `9`

- Meaning: Option used with llListStatistics to calculate the geometric mean of a list of numbers.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_MAX

- Type: integer | Value: `2`

- Meaning: Option used with llListStatistics to find the largest number in the list.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_MEAN

- Type: integer | Value: `3`

- Meaning: Option used with llListStatistics to calculate the mean (average) of the numbers in the list.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_MEDIAN

- Type: integer | Value: `4`

- Meaning: Option used with llListStatistics to calculate the median of the numbers in the list.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_MIN

- Type: integer | Value: `1`

- Meaning: Option used with llListStatistics to find the smallest number in the list.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_NUM_COUNT

- Type: integer | Value: `8`

- Meaning: Option used with llListStatistics to determine the count of float and integer elements in the list.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_RANGE

- Type: integer | Value: `0`

- Meaning: Option used with llListStatistics to calculate the range (maximum value minus minimum value) of the list.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_STD_DEV

- Type: integer | Value: `5`

- Meaning: Option used with llListStatistics to calculate the sample standard deviation of a list of numbers.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_SUM

- Type: integer | Value: `6`

- Meaning: Option used with llListStatistics to calculate the sum of the numbers in the list.

- Member of enum/flag group: ListStatisticsOperation


## LIST_STAT_SUM_SQUARES

- Type: integer | Value: `7`

- Meaning: Option used with llListStatistics to calculate the sum of the squares of the numbers in the list.

- Member of enum/flag group: ListStatisticsOperation


## LOOP

- Type: integer | Value: `0x2`

- Meaning: Used with texture animation functions to cause the animation to loop continuously.

- Member of enum/flag group: TextureAnimMode


## MASK_BASE

- Type: integer | Value: `0`

- Meaning: Permissions mask option representing base permissions.

- Member of enum/flag group: AssetPermissionCategory


## MASK_COMBINED

- Type: integer | Value: `0x10`

- Meaning: Permissions mask option to include the object's inventory contents when calculating permissions. Can be combined with other mask flags (e.g., MASK_OWNER | MASK_COMBINED).

- Member of enum/flag group: AssetPermissionCategoryFlag


## MASK_EVERYONE

- Type: integer | Value: `3`

- Meaning: Permissions mask option representing permissions held by everyone.

- Member of enum/flag group: AssetPermissionCategory


## MASK_GROUP

- Type: integer | Value: `2`

- Meaning: Permissions mask option representing active group permissions.

- Member of enum/flag group: AssetPermissionCategory


## MASK_NEXT

- Type: integer | Value: `4`

- Meaning: Permissions mask option representing permissions the next owner will inherit.

- Member of enum/flag group: AssetPermissionCategory


## MASK_OWNER

- Type: integer | Value: `1`

- Meaning: Permissions mask option representing current owner permissions.

- Member of enum/flag group: AssetPermissionCategory


## NAK

- Type: string | Value: `\n\x15\n`

- Meaning: Value returned by llGetNotecardLineSync and llFindNotecardTextSync (as a single-entry list) when the notecard is not in the region's cache. Equal to an ASCII NAK surrounded by newlines (codes 10, 21, 10).


## NAVIGATE_TO_GOAL_REACHED_DIST

- Type: integer | Value: `2`

- Member of enum/flag group: CharacterNavigateParam


## NULL_KEY

- Type: string | Value: `00000000-0000-0000-0000-000000000000`

- Meaning: A special string constant used as a null or empty key value.


## OBJECT_ACCOUNT_LEVEL

- Type: integer | Value: `41`

- Meaning: Flag used with llGetObjectDetails to retrieve an avatar's account level. Returns 0 for Basic, 1 for Premium, 5 for Plus, 10 for Premium Plus, or -1 if the target is not an avatar.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_ANIMATED_COUNT

- Type: integer | Value: `39`

- Meaning: Flag used with llGetObjectDetails. For an object, returns a boolean indicating if the root is set as 'Animated Mesh'. For an agent, returns the total number of 'Animated Mesh' attachments worn.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_ANIMATED_SLOTS_AVAILABLE

- Type: integer | Value: `40`

- Meaning: Flag used with llGetObjectDetails to get the avatar's available 'Animated Mesh' attachment slot count (returns 0 if the ID is not an avatar).

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_ATTACHED_POINT

- Type: integer | Value: `19`

- Meaning: Flag used with llGetObjectDetails. Returns the integer attachment point matching an ATTACH_* constant, or 0 if the target is not an attachment (e.g., an avatar or unattached object).

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_ATTACHED_SLOTS_AVAILABLE

- Type: integer | Value: `35`

- Meaning: Flag used with llGetObjectDetails to get an avatar's available attachment slot count. Returns 0 if the ID is not an avatar or if no slots are available.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_BODY_SHAPE_TYPE

- Type: integer | Value: `26`

- Meaning: Flag used with llGetObjectDetails to retrieve a float representing the gender/sex setting of an avatar's shape (0.0 is standard female, 1.0 is standard male, and values greater than or equal to 0.5 are considered male). Returns -1.0 if not an avatar or if no data is available.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_CHARACTER_TIME

- Type: integer | Value: `17`

- Meaning: Flag used with llGetObjectDetails to get the average CPU time (in seconds) spent on navigation if the target is a pathfinding character. Returns 0 for non-characters.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_CLICK_ACTION

- Type: integer | Value: `28`

- Meaning: Flag used with llGetObjectDetails to get the click action of a prim. Returns an integer corresponding to a CLICK_ACTION_* constant (default is 0).

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_CREATION_TIME

- Type: integer | Value: `36`

- Meaning: Flag used with llGetObjectDetails to get the object's creation time (established via build-menu rezzing or mesh uploads, not via inventory/script rezzes, copying, or modifying). Returns an empty string for avatars.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_CREATOR

- Type: integer | Value: `8`

- Meaning: Flag used with llGetObjectDetails to get the key of the prim's creator. Returns NULL_KEY if the ID is an avatar.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_DAMAGE

- Type: integer | Value: `51`

- Meaning: Flag used with llGetObjectDetails to retrieve the amount of damage a prim inflicts upon collision.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_DAMAGE_TYPE

- Type: integer | Value: `52`

- Meaning: Flag used with llGetObjectDetails to retrieve the type of damage a prim inflicts on collision. Returns an integer matching a DAMAGE_TYPE_* constant, a custom type, or a value repurposed by a combat system.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_DESC

- Type: integer | Value: `2`

- Meaning: Flag used with llGetObjectDetails to retrieve the prim's description. Returns an empty string if the ID is an avatar.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_GROUP

- Type: integer | Value: `7`

- Meaning: Flag used with llGetObjectDetails to get the prim's group key. Returns NULL_KEY if the target is an avatar (which means a workaround is required to get an avatar's active group).

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_GROUP_TAG

- Type: integer | Value: `33`

- Meaning: Flag used with llGetObjectDetails to get an avatar's active group tag/title. Returns an empty string if the target is not an avatar.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_HEALTH

- Type: integer | Value: `50`

- Meaning: Flag used with llGetObjectDetails to retrieve the current health value of an avatar or prim.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_HOVER_HEIGHT

- Type: integer | Value: `25`

- Meaning: Flag used with llGetObjectDetails to get the dynamic hover height of an avatar (default is 0.0). Returns 0.0 if not an avatar or if no data is available; does not reflect the shape's 'Hover' slider.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_LAST_OWNER_ID

- Type: integer | Value: `27`

- Meaning: Flag used with llGetObjectDetails to get the key of the previous owner. For group-owned objects, returns the avatar who deeded it. Returns NULL_KEY for avatars, untransferred objects, or objects taken to inventory and re-rezzed.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_LINK_NUMBER

- Type: integer | Value: `46`

- Meaning: Flag used with llGetObjectDetails to get the index of the prim within its linkset, or 0 if unlinked.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_LOCKED

- Type: integer | Value: `55`

- Meaning: Flag used with llGetObjectDetails to get a boolean, indicating if the object is locked.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_MASS

- Type: integer | Value: `43`

- Meaning: Flag used with llGetObjectDetails to retrieve the total mass (in kilograms) of the object's linkset.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_MATERIAL

- Type: integer | Value: `42`

- Meaning: Flag used with llGetObjectDetails to retrieve the physics material of the object, returning an integer matching a PRIM_MATERIAL_* constant.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_NAME

- Type: integer | Value: `1`

- Meaning: Flag used with llGetObjectDetails to get the prim's name, or the legacy name if the target is an avatar.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_OMEGA

- Type: integer | Value: `29`

- Meaning: Flag used with llGetObjectDetails to get the rotational (angular) velocity of an object in radians per second.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_OWNER

- Type: integer | Value: `6`

- Meaning: Flag used with llGetObjectDetails to get the owner's key. If the target is an avatar, their own key is returned. If group-owned, it returns NULL_KEY.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PATHFINDING_TYPE

- Type: integer | Value: `20`

- Meaning: Flag used with llGetObjectDetails to get the pathfinding setting of an object in the region, returning an integer matching an OPT_* constant.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PERMS

- Type: integer | Value: `53`

- Meaning: Flag used with llGetObjectDetails to retrieve the permissions of the object as five integers.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PERMS_COMBINED

- Type: integer | Value: `54`

- Meaning: Flag used with llGetObjectDetails to retrieve the permissions of the object combined with all of its inventory items as five integers.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PHANTOM

- Type: integer | Value: `22`

- Meaning: Flag used with llGetObjectDetails to get a boolean indicating if phantom is enabled on the object. Returns 0 if the target is an avatar or attachment.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PHYSICS

- Type: integer | Value: `21`

- Meaning: Flag used with llGetObjectDetails to get a boolean indicating if physics is enabled on the object. Returns 0 if the target is an avatar or attachment.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PHYSICS_COST

- Type: integer | Value: `16`

- Meaning: Flag used with llGetObjectDetails to get the physics cost of the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_POS

- Type: integer | Value: `3`

- Meaning: Flag used with llGetObjectDetails to get the prim's position in region coordinates. For an avatar outside the region, the returned position is relative to the script's region.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PRIM_COUNT

- Type: integer | Value: `30`

- Meaning: Flag used with llGetObjectDetails to get the prim count of the object. Note that the script and target object must be owned by the same owner.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_PRIM_EQUIVALENCE

- Type: integer | Value: `13`

- Meaning: Flag used with llGetObjectDetails to get the prim equivalence of the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_RENDER_WEIGHT

- Type: integer | Value: `24`

- Meaning: Flag used with llGetObjectDetails to get the render weight (Avatar Rendering Cost) of an avatar based on viewer reports. Returns 0 for objects, -1 if unknown, and is capped at 500,000.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_RETURN_PARCEL

- Type: integer | Value: `1`

- Meaning: Scope flag used with llReturnObjectsByOwner to return all objects on the same parcel as the script owned by the specified owner. Requires the script owner to be an estate manager or the parcel owner.

- Member of enum/flag group: ReturnObjectsScope


## OBJECT_RETURN_PARCEL_OWNER

- Type: integer | Value: `2`

- Meaning: Scope flag used with llReturnObjectsByOwner to return all objects owned by the specified owner that are located on parcels owned by the script's owner.

- Member of enum/flag group: ReturnObjectsScope


## OBJECT_RETURN_REGION

- Type: integer | Value: `4`

- Meaning: Scope flag used with llReturnObjectsByOwner to return all objects in the region owned by the specified owner. Only works if the script is owned by the estate owner or an estate manager.

- Member of enum/flag group: ReturnObjectsScope


## OBJECT_REZZER_KEY

- Type: integer | Value: `32`

- Meaning: Flag used with llGetObjectDetails to retrieve the key of the object or avatar that rezzed the target object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_REZ_TIME

- Type: integer | Value: `45`

- Meaning: Flag used with llGetObjectDetails to retrieve the timestamp of when the object was rezzed.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_ROOT

- Type: integer | Value: `18`

- Meaning: Flag used with llGetObjectDetails to get the ID of the root prim. For an avatar, returns the root prim of the linkset they are sitting on (or the avatar's own ID if not sitting).

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_ROT

- Type: integer | Value: `4`

- Meaning: Flag used with llGetObjectDetails to get the prim's rotation.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_RUNNING_SCRIPT_COUNT

- Type: integer | Value: `9`

- Meaning: Flag used with llGetObjectDetails to get the total number of running scripts attached to the target object or agent.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_SCALE

- Type: integer | Value: `47`

- Meaning: Flag used with llGetObjectDetails to get the size (scale) of the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_SCRIPT_MEMORY

- Type: integer | Value: `11`

- Meaning: Flag used with llGetObjectDetails to get the allocated script memory (or its upper limit) in bytes for the object or agent. This value is recomputed every 10-20 seconds.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_SCRIPT_TIME

- Type: integer | Value: `12`

- Meaning: Flag used with llGetObjectDetails to get the average script CPU time (in seconds) used per frame. Reports a 30-minute average, or the average since entering the region if present for less than 30 minutes.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_SELECT_COUNT

- Type: integer | Value: `37`

- Meaning: Flag used with llGetObjectDetails to get the total number of agents/avatars actively selecting any link in the object. Returns 0 if the target is an avatar.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_SERVER_COST

- Type: integer | Value: `14`

- Meaning: Flag used with llGetObjectDetails to get the server cost of the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_SIT_COUNT

- Type: integer | Value: `38`

- Meaning: Flag used with llGetObjectDetails to get the total number of agents sitting on any links in the object. Returns 0 if the target is an avatar.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_STREAMING_COST

- Type: integer | Value: `15`

- Meaning: Flag used with llGetObjectDetails to get the streaming (download) cost of the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_TEMP_ATTACHED

- Type: integer | Value: `34`

- Meaning: Flag used with llGetObjectDetails to get a boolean indicating whether the object is temporarily attached.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_TEMP_ON_REZ

- Type: integer | Value: `23`

- Meaning: Flag used with llGetObjectDetails to get a boolean indicating if temporary-on-rez is enabled for the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_TEXT

- Type: integer | Value: `44`

- Meaning: Flag used with llGetObjectDetails to get the floating (hover) text displayed above the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_TEXT_ALPHA

- Type: integer | Value: `49`

- Meaning: Flag used with llGetObjectDetails to get the alpha value of the floating (hover) text displayed above the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_TEXT_COLOR

- Type: integer | Value: `48`

- Meaning: Flag used with llGetObjectDetails to get the color vector of the floating (hover) text displayed above the object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_TOTAL_INVENTORY_COUNT

- Type: integer | Value: `31`

- Meaning: Flag used with llGetObjectDetails to get the total number of inventory items inside the object. Requires the script and target object to share the same owner.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_TOTAL_SCRIPT_COUNT

- Type: integer | Value: `10`

- Meaning: Flag used with llGetObjectDetails to get the total number of scripts (both running and stopped) attached to the target object or agent.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_UNKNOWN_DETAIL

- Type: integer | Value: `-1`

- Meaning: Flag returned by llGetObjectDetails when an invalid flag is requested.


## OBJECT_VELOCITY

- Type: integer | Value: `5`

- Meaning: Flag used with llGetObjectDetails to get the velocity vector of the target object.

- Member of enum/flag group: ObjectDetailsParam


## OBJECT_VOLUME_DETECT

- Type: integer | Value: `56`

- Meaning: Flag used with llGetObjectDetails to get a boolean, indicating if the object is VolumeDetect.

- Member of enum/flag group: ObjectDetailsParam


## OPT_AVATAR

- Type: integer | Value: `1`

- Meaning: Returned for avatars.

- Member of enum/flag group: ObjectPathfindingType


## OPT_CHARACTER

- Type: integer | Value: `2`

- Meaning: Returned for pathfinding characters.

- Member of enum/flag group: ObjectPathfindingType


## OPT_EXCLUSION_VOLUME

- Type: integer | Value: `6`

- Meaning: Returned for exclusion volumes.

- Member of enum/flag group: ObjectPathfindingType


## OPT_LEGACY_LINKSET

- Type: integer | Value: `0`

- Meaning: Returned for movable obstacles, movable phantoms, physical, and volumedetect objects.

- Member of enum/flag group: ObjectPathfindingType


## OPT_MATERIAL_VOLUME

- Type: integer | Value: `5`

- Meaning: Returned for material volumes.

- Member of enum/flag group: ObjectPathfindingType


## OPT_OTHER

- Type: integer | Value: `-1`

- Meaning: Returned for attachments, Linden trees, and grass.

- Member of enum/flag group: ObjectPathfindingType


## OPT_STATIC_OBSTACLE

- Type: integer | Value: `4`

- Meaning: Returned for static obstacles.

- Member of enum/flag group: ObjectPathfindingType


## OPT_WALKABLE

- Type: integer | Value: `3`

- Meaning: Returned for walkable objects.

- Member of enum/flag group: ObjectPathfindingType


## OVERRIDE_GLTF_BASE_ALPHA

- Type: integer | Value: `2`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides to set the alpha for the face(s). Only impacts rendering when the alpha mode is set to PRIM_GLTF_ALPHA_MODE_BLEND.

- Member of enum/flag group: GLTFOverride


## OVERRIDE_GLTF_BASE_ALPHA_MASK

- Type: integer | Value: `4`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides to set the alpha cutoff level on the face(s) when the alpha mode is set to mask.

- Member of enum/flag group: GLTFOverride


## OVERRIDE_GLTF_BASE_ALPHA_MODE

- Type: integer | Value: `3`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides to set the alpha mode on the face(s) to one of the valid blend modes.

- Member of enum/flag group: GLTFOverride


## OVERRIDE_GLTF_BASE_COLOR_FACTOR

- Type: integer | Value: `1`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides to set the tinting color (specified in linear RGB) used for the base color. Use llsRGB2Linear to convert colors from Blinn-Phong to PBR.

- Member of enum/flag group: GLTFOverride


## OVERRIDE_GLTF_BASE_DOUBLE_SIDED

- Type: integer | Value: `5`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides. If set to TRUE, the texture on the face(s) will be rendered as double-sided.

- Member of enum/flag group: GLTFOverride


## OVERRIDE_GLTF_EMISSIVE_FACTOR

- Type: integer | Value: `8`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides to set the tint (specified in linear RGB) used for the emissive texture on the face(s).

- Member of enum/flag group: GLTFOverride


## OVERRIDE_GLTF_METALLIC_FACTOR

- Type: integer | Value: `6`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides to adjust the metallic factor on the specified face(s) to a value between 0 and 1.

- Member of enum/flag group: GLTFOverride


## OVERRIDE_GLTF_ROUGHNESS_FACTOR

- Type: integer | Value: `7`

- Meaning: GLTF override setting used with llSetLinkGLTFOverrides to adjust the roughness factor on the specified face(s) to a value between 0 and 1.

- Member of enum/flag group: GLTFOverride


## PARCEL_COUNT_GROUP

- Type: integer | Value: `2`

- Meaning: Used with llGetParcelPrimCount to get the total land impact of objects not owned by the parcel owner but set to or owned by the parcel's group.

- Member of enum/flag group: ParcelPrimCountCategory


## PARCEL_COUNT_OTHER

- Type: integer | Value: `3`

- Meaning: Used with llGetParcelPrimCount to get the land impact of all objects that are neither owned by the parcel owner nor set to or owned by the parcel's group.

- Member of enum/flag group: ParcelPrimCountCategory


## PARCEL_COUNT_OWNER

- Type: integer | Value: `1`

- Meaning: Used with llGetParcelPrimCount to get the total land impact of objects owned by the parcel owner.

- Member of enum/flag group: ParcelPrimCountCategory


## PARCEL_COUNT_SELECTED

- Type: integer | Value: `4`

- Meaning: Used with llGetParcelPrimCount to get the total land impact of all objects currently selected or sat on.

- Member of enum/flag group: ParcelPrimCountCategory


## PARCEL_COUNT_TEMP

- Type: integer | Value: `5`

- Meaning: Used with llGetParcelPrimCount to get the total land impact of temporary (temp-on-rez) objects.

- Member of enum/flag group: ParcelPrimCountCategory


## PARCEL_COUNT_TOTAL

- Type: integer | Value: `0`

- Meaning: Used with llGetParcelPrimCount to get the total land impact of all objects on the parcel(s), excluding temporary (temp-on-rez) objects.

- Member of enum/flag group: ParcelPrimCountCategory


## PARCEL_DETAILS_AREA

- Type: integer | Value: `4`

- Meaning: Flag used with llGetParcelDetails to retrieve the parcel's area in square meters (sqm).

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_DESC

- Type: integer | Value: `1`

- Meaning: Flag used with llGetParcelDetails to retrieve the description of the parcel (up to 127 characters).

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_FLAGS

- Type: integer | Value: `12`

- Meaning: Flag used with llGetParcelDetails to retrieve the parcel flags set on this parcel (see llGetParcelFlags for listings and meanings).

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_GROUP

- Type: integer | Value: `3`

- Meaning: Flag used with llGetParcelDetails to retrieve the parcel group's 36-character key.

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_ID

- Type: integer | Value: `5`

- Meaning: Flag used with llGetParcelDetails to retrieve the parcel's 36-character UUID/key.

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_LANDING_LOOKAT

- Type: integer | Value: `10`

- Meaning: Flag used with llGetParcelDetails to retrieve the lookat vector set for the landing point (teleport routing) on this parcel, if any.

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_LANDING_POINT

- Type: integer | Value: `9`

- Meaning: Flag used with llGetParcelDetails to retrieve the landing point vector set for this parcel, if any.

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_NAME

- Type: integer | Value: `0`

- Meaning: Flag used with llGetParcelDetails to retrieve the name of the parcel (up to 63 characters).

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_OWNER

- Type: integer | Value: `2`

- Meaning: Flag used with llGetParcelDetails to retrieve the parcel owner's 36-character key.

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_PRIM_CAPACITY

- Type: integer | Value: `7`

- Meaning: Flag used with llGetParcelDetails to retrieve the total prim capacity on this and all same-owner parcels, sim-wide (see llGetParcelMaxPrims for same-parcel-only and/or sim-wide reporting).

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_PRIM_USED

- Type: integer | Value: `8`

- Meaning: Flag used with llGetParcelDetails to retrieve the total prim usage on this and all same-owner parcels, sim-wide (see llGetParcelPrimCount to get prim counts by owner, group, or temporary status).

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_SCRIPT_DANGER

- Type: integer | Value: `13`

- Meaning: Flag used with llGetParcelDetails to check if the script is in danger (due to restrictions that impact script execution) on the indicated parcel; see llScriptDanger.

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_SEE_AVATARS

- Type: integer | Value: `6`

- Meaning: Flag used with llGetParcelDetails to retrieve the 'See and chat with residents on this parcel' avatar visibility setting.

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_DETAILS_TP_ROUTING

- Type: integer | Value: `11`

- Meaning: Flag used with llGetParcelDetails to retrieve the teleport routing setting for this parcel (0 = TP_ROUTING_BLOCKED, 1 = TP_ROUTING_LANDINGP, 2 = TP_ROUTING_FREE; rules are only enforced if a landing point is set).

- Member of enum/flag group: ParcelDetailsParam


## PARCEL_FLAG_ALLOW_ALL_OBJECT_ENTRY

- Type: integer | Value: `0x08000000`

- Meaning: Flag used with llGetParcelFlags to check if the parcel allows all objects to enter.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_CREATE_GROUP_OBJECTS

- Type: integer | Value: `0x4000000`

- Meaning: Flag used with llGetParcelFlags to check if group members or scripts in group-deeded objects are allowed to create/rez objects on the parcel.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_CREATE_OBJECTS

- Type: integer | Value: `0x40`

- Meaning: Flag used with llGetParcelFlags to check if the parcel allows anyone to create objects.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_DAMAGE

- Type: integer | Value: `0x20`

- Meaning: Flag used with llGetParcelFlags to check if damage is enabled on the parcel.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_FLY

- Type: integer | Value: `0x1`

- Meaning: Flag used with llGetParcelFlags to check if flying is allowed on the parcel.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_GROUP_OBJECT_ENTRY

- Type: integer | Value: `0x10000000`

- Meaning: Flag used with llGetParcelFlags to check if the parcel restricts object entry to only group-owned and owner-owned objects.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_GROUP_SCRIPTS

- Type: integer | Value: `0x2000000`

- Meaning: Flag used with llGetParcelFlags to check if the parcel allows scripts owned by the parcel's group to run.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_LANDMARK

- Type: integer | Value: `0x8`

- Meaning: Flag used with llGetParcelFlags to check if the parcel allows landmarks to be created.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_SCRIPTS

- Type: integer | Value: `0x2`

- Meaning: Flag used with llGetParcelFlags to check if scripts (including outside scripts) are allowed to run on the parcel.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_ALLOW_TERRAFORM

- Type: integer | Value: `0x10`

- Meaning: Flag used with llGetParcelFlags to check if the parcel allows anyone to terraform the land.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_LINDEN_HOMES

- Type: integer | Value: `0x800000`

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_LOCAL_SOUND_ONLY

- Type: integer | Value: `0x8000`

- Meaning: Flag used with llGetParcelFlags to check if the parcel restricts spatialized sounds to the parcel (preventing outside sound from being heard inside).

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_RESTRICT_PUSHOBJECT

- Type: integer | Value: `0x200000`

- Meaning: Flag used with llGetParcelFlags to check if the parcel restricts the use of llPushObject by non-owners (or non-group officers if group-owned).

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_USE_ACCESS_GROUP

- Type: integer | Value: `0x100`

- Meaning: Flag used with llGetParcelFlags to check if the parcel limits access to group members.

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_USE_ACCESS_LIST

- Type: integer | Value: `0x200`

- Meaning: Flag used with llGetParcelFlags to check if the parcel limits access to a specific list of residents (avatars).

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_USE_BAN_LIST

- Type: integer | Value: `0x400`

- Meaning: Flag used with llGetParcelFlags to check if the parcel uses a ban list (including restricting access based on payment information).

- Member of enum/flag group: ParcelFlag


## PARCEL_FLAG_USE_LAND_PASS_LIST

- Type: integer | Value: `0x800`

- Meaning: Flag used with llGetParcelFlags to check if the parcel restricts access via purchasable land passes (sold for L$).

- Member of enum/flag group: ParcelFlag


## PARCEL_MEDIA_COMMAND_AGENT

- Type: integer | Value: `7`

- Meaning: Command used with llParcelMediaCommandList to apply the specified media command to the designated agent only.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_AUTO_ALIGN

- Type: integer | Value: `9`

- Meaning: Command used with llParcelMediaCommandList to toggle or set the parcel media option 'Auto scale content'.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_DESC

- Type: integer | Value: `12`

- Meaning: Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel media description.

- Member of enum/flag group: ParcelMediaCommand, ParcelMediaQuery


## PARCEL_MEDIA_COMMAND_LOOP

- Type: integer | Value: `3`

- Meaning: Command used with llParcelMediaCommandList to start the media stream playing from the current frame and have it loop back to the beginning when it reaches the end.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_LOOP_SET

- Type: integer | Value: `13`

- Meaning: Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel's media looping variable or loop duration (which may have functionality limitations; see VWR-19712).

- Member of enum/flag group: ParcelMediaCommand, ParcelMediaQuery


## PARCEL_MEDIA_COMMAND_PAUSE

- Type: integer | Value: `1`

- Meaning: Command used with llParcelMediaCommandList to pause the media stream on the current frame.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_PLAY

- Type: integer | Value: `2`

- Meaning: Command used with llParcelMediaCommandList to play the media stream from its current frame, stopping when the end is reached.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_SIZE

- Type: integer | Value: `11`

- Meaning: Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel media pixel resolution.

- Member of enum/flag group: ParcelMediaCommand, ParcelMediaQuery


## PARCEL_MEDIA_COMMAND_STOP

- Type: integer | Value: `0`

- Meaning: Command used with llParcelMediaCommandList to stop the media stream and rewind it to the first frame.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_TEXTURE

- Type: integer | Value: `4`

- Meaning: Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel's media texture.

- Member of enum/flag group: ParcelMediaCommand, ParcelMediaQuery


## PARCEL_MEDIA_COMMAND_TIME

- Type: integer | Value: `6`

- Meaning: Command used with llParcelMediaCommandList to jump to a specific timestamp in the media stream, specified in floating-point seconds.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_TYPE

- Type: integer | Value: `10`

- Meaning: Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel media MIME type (e.g., 'text/html').

- Member of enum/flag group: ParcelMediaCommand, ParcelMediaQuery


## PARCEL_MEDIA_COMMAND_UNLOAD

- Type: integer | Value: `8`

- Meaning: Command used with llParcelMediaCommandList to completely unload the media and restore the face's original texture.

- Member of enum/flag group: ParcelMediaCommand


## PARCEL_MEDIA_COMMAND_URL

- Type: integer | Value: `5`

- Meaning: Command used with llParcelMediaCommandList or llParcelMediaQuery to get or set the parcel's media URL.

- Member of enum/flag group: ParcelMediaCommand, ParcelMediaQuery


## PARCEL_SALE_AGENT

- Type: integer | Value: `2`

- Meaning: Option used with llSetParcelForSale to specify the agent ID authorized to buy the parcel. If none is set, any agent can purchase it.

- Member of enum/flag group: ParcelSaleParam


## PARCEL_SALE_ERROR_BAD_PARAMS

- Type: integer | Value: `5`

- Meaning: Error code indicating the parameters provided to set the parcel sale information are invalid.

- Member of enum/flag group: ParcelSaleError


## PARCEL_SALE_ERROR_INVALID_PRICE

- Type: integer | Value: `4`

- Meaning: Error code indicating the specified parcel price is invalid (e.g., less than or equal to 0).

- Member of enum/flag group: ParcelSaleError


## PARCEL_SALE_ERROR_IN_ESCROW

- Type: integer | Value: `3`

- Meaning: Error code indicating the parcel is in escrow and cannot be put up for sale.

- Member of enum/flag group: ParcelSaleError


## PARCEL_SALE_ERROR_NO_PARCEL

- Type: integer | Value: `1`

- Meaning: Error code indicating the parcel could not be found.

- Member of enum/flag group: ParcelSaleError


## PARCEL_SALE_ERROR_NO_PERMISSIONS

- Type: integer | Value: `2`

- Meaning: Error code indicating the script lacks the required permissions to set the parcel sale information.

- Member of enum/flag group: ParcelSaleError


## PARCEL_SALE_OBJECTS

- Type: integer | Value: `3`

- Meaning: Option used with llSetParcelForSale. If set to TRUE, objects on the parcel are included in the sale.

- Member of enum/flag group: ParcelSaleParam


## PARCEL_SALE_OK

- Type: integer | Value: `0`

- Meaning: Status code indicating the parcel sale information was successfully set.

- Member of enum/flag group: ParcelSaleError


## PARCEL_SALE_PRICE

- Type: integer | Value: `1`

- Meaning: Option used with llSetParcelForSale to set the parcel price. If no authorized agent is set, the price must be greater than 0.

- Member of enum/flag group: ParcelSaleParam


## PASSIVE

- Type: integer | Value: `0x4`

- Meaning: Identifies static or non-moving in-world objects (which do not consume active server resources). In llDetectedType(), indicates non-physical objects. In llSensor()/llSensorRepeat() filters, searches for non-physical, non-scripted, inactive, or non-moving physical objects.

- Member of enum/flag group: DetectType


## PASS_ALWAYS

- Type: integer | Value: `1`

- Meaning: Used with event-passing functions (e.g., llPassTouches, llPassCollisions) to ensure events are always passed from the child prim to the root prim, regardless of whether they are handled by child script handlers.

- Member of enum/flag group: PassMode


## PASS_IF_NOT_HANDLED

- Type: integer | Value: `0`

- Meaning: Used with event-passing functions (default behavior) to pass events from the child prim to the root prim only if there is no script handling the event in the child.

- Member of enum/flag group: PassMode


## PASS_NEVER

- Type: integer | Value: `2`

- Meaning: Used with event-passing functions to ensure events are never passed from the child prim to the root prim, regardless of whether they are handled by child script handlers.

- Member of enum/flag group: PassMode


## PATROL_PAUSE_AT_WAYPOINTS

- Type: integer | Value: `0`

- Meaning: Option parameter for llPatrolPoints (defaults to FALSE). If TRUE, the character slows down and momentarily pauses at each waypoint. If FALSE, the character moves to the next waypoint at full speed with no pause.

- Member of enum/flag group: CharacterPatrolPointsParam


## PAYMENT_INFO_ON_FILE

- Type: integer | Value: `1`

- Meaning: Agent data flag returned by llRequestAgentData indicating if the user has payment information on file.

- Member of enum/flag group: AgentDataPaymentInfo


## PAYMENT_INFO_USED

- Type: integer | Value: `2`

- Meaning: Agent data flag returned by llRequestAgentData indicating if the user has ever used their payment information.

- Member of enum/flag group: AgentDataPaymentInfo


## PAY_DEFAULT

- Type: integer | Value: `-2`

- Meaning: Used with llSetPayPrice to use the default value for the specified quick pay button.

- Member of enum/flag group: PayButton


## PAY_HIDE

- Type: integer | Value: `-1`

- Meaning: Used with llSetPayPrice to hide the specified quick pay button completely.

- Member of enum/flag group: PayButton


## PERMISSION_ATTACH

- Type: integer | Value: `0x00020`

- Meaning: Runtime permission that allows the script to successfully attach to or detach from the agent using llAttachToAvatar.

- Member of enum/flag group: ScriptPermission


## PERMISSION_CHANGE_JOINTS

- Type: integer | Value: `0x00100`

- Meaning: (Not yet implemented)

- Member of enum/flag group: ScriptPermission


## PERMISSION_CHANGE_LINKS

- Type: integer | Value: `0x00080`

- Meaning: Runtime permission that allows the script to successfully create, break, or modify links to other objects using llCreateLink, llBreakLink, or llBreakAllLinks.

- Member of enum/flag group: ScriptPermission


## PERMISSION_CHANGE_PERMISSIONS

- Type: integer | Value: `0x00200`

- Meaning: (Not yet implemented)

- Member of enum/flag group: ScriptPermission


## PERMISSION_CONTROL_CAMERA

- Type: integer | Value: `0x00800`

- Meaning: Runtime permission that allows the script to control the agent's camera. The agent must be sitting on or attached to the object, and permission is automatically revoked on standing up or detaching.

- Member of enum/flag group: ScriptPermission


## PERMISSION_DEBIT

- Type: integer | Value: `0x00002`

- Meaning: Runtime permission that allows the script to successfully call llGiveMoney or llTransferLindenDollars to debit the owner's account.

- Member of enum/flag group: ScriptPermission


## PERMISSION_GAME_CONTROL

- Type: integer | Value: `0x100000`

- Member of enum/flag group: ScriptPermission


## PERMISSION_OVERRIDE_ANIMATIONS

- Type: integer | Value: `0x08000`

- Meaning: Runtime permission that allows the script to configure and override default animations on the agent.

- Member of enum/flag group: ScriptPermission


## PERMISSION_PRIVILEGED_LAND_ACCESS

- Type: integer | Value: `0x80000`

- Meaning: Runtime permission that grants the script privileged access to land parcel functions, which is required to use llSetParcelForSale.

- Member of enum/flag group: ScriptPermission


## PERMISSION_RELEASE_OWNERSHIP

- Type: integer | Value: `0x00040`

- Meaning: (Not yet implemented)

- Member of enum/flag group: ScriptPermission


## PERMISSION_REMAP_CONTROLS

- Type: integer | Value: `0x00008`

- Meaning: (Not yet implemented)

- Member of enum/flag group: ScriptPermission


## PERMISSION_RETURN_OBJECTS

- Type: integer | Value: `0x10000`

- Meaning: Runtime permission required to use the llReturnObjectsByID and llReturnObjectsByOwner functions to return objects from parcels.

- Member of enum/flag group: ScriptPermission


## PERMISSION_SILENT_ESTATE_MANAGEMENT

- Type: integer | Value: `0x04000`

- Meaning: Runtime permission that allows the script to manage estate access rules via llManageEstateAccess without notifying the object owner of the changes.

- Member of enum/flag group: ScriptPermission


## PERMISSION_TAKE_CONTROLS

- Type: integer | Value: `0x00004`

- Meaning: Runtime permission that allows the script to successfully call the llTakeControls function to intercept the agent's controls.

- Member of enum/flag group: ScriptPermission


## PERMISSION_TELEPORT

- Type: integer | Value: `0x01000`

- Meaning: Runtime permission required to teleport the agent using the llTeleportAgent function.

- Member of enum/flag group: ScriptPermission


## PERMISSION_TRACK_CAMERA

- Type: integer | Value: `0x00400`

- Meaning: Runtime permission that allows the script to track the agent's camera position and rotation.

- Member of enum/flag group: ScriptPermission


## PERMISSION_TRIGGER_ANIMATION

- Type: integer | Value: `0x00010`

- Meaning: Runtime permission that allows the script to start or stop animations on the agent (such as using llStartAnimation).

- Member of enum/flag group: ScriptPermission


## PERM_ALL

- Type: integer | Value: `0x7FFFFFFF`

- Meaning: Permissions mask representing a combination of move, modify, copy, and transfer permissions.

- Member of enum/flag group: AssetPermission


## PERM_COPY

- Type: integer | Value: `0x8000`

- Meaning: Permissions mask representing copy permission.

- Member of enum/flag group: AssetPermission


## PERM_MODIFY

- Type: integer | Value: `0x4000`

- Meaning: Permissions mask representing modify permission.

- Member of enum/flag group: AssetPermission


## PERM_MOVE

- Type: integer | Value: `0x80000`

- Meaning: Permissions mask representing move permission.

- Member of enum/flag group: AssetPermission


## PERM_TRANSFER

- Type: integer | Value: `0x2000`

- Meaning: Permissions mask representing transfer permission.

- Member of enum/flag group: AssetPermission


## PI

- Type: float | Value: `3.14159265`

- Meaning: Mathematical constant pi, representing the number of radians in a half circle (semi-circle). When used in sensor functions, it specifies a full sphere scan.


## PING_PONG

- Type: integer | Value: `0x8`

- Meaning: Used with texture animation functions to cause the animation to play forward first, and then in reverse.

- Member of enum/flag group: TextureAnimMode


## PI_BY_TWO

- Type: float | Value: `1.57079633`

- Meaning: Mathematical constant pi/2, representing the number of radians in a quarter circle. When used in sensor functions, it specifies a hemisphere scan.


## PRIM_ALLOW_UNSIT

- Type: integer | Value: `39`

- Meaning: Prim parameter for allowing or restricting manual standing for avatars seated on this prim within a valid experience. Ignored if the avatar was not seated via llSitOnLink. When restriction is active, participating seated avatars cannot manually stand or select another prim to sit on.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_ALPHA_MODE

- Type: integer | Value: `38`

- Meaning: Prim parameter used to set diffuse texture alpha rendering mode attributes. Requires face, alpha_mode (PRIM_ALPHA_MODE_BLEND, _NONE, _MASK, or _EMISSIVE), and alpha_cutoff (used only for _MASK) parameters.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_ALPHA_MODE_BLEND

- Type: integer | Value: `1`

- Meaning: Prim parameter setting for PRIM_ALPHA_MODE. Directs the face to use alpha blending for diffuse texture rendering (if an alpha channel exists). Also used as the default value to clear material settings from a prim face.

- Member of enum/flag group: AlphaMode


## PRIM_ALPHA_MODE_EMISSIVE

- Type: integer | Value: `3`

- Meaning: Prim parameter setting for PRIM_ALPHA_MODE. Renders the diffuse texture's alpha channel as an emissivity mask. Pixels render with an emissivity corresponding to their opacity under all lighting conditions (fully opaque pixels effectively render as 'full bright').

- Member of enum/flag group: AlphaMode


## PRIM_ALPHA_MODE_MASK

- Type: integer | Value: `2`

- Meaning: Prim parameter setting for PRIM_ALPHA_MODE. Renders the diffuse texture's alpha channel on a binary per-pixel basis; pixels more opaque than the alpha cutoff render as fully opaque, while pixels below the cutoff render as fully transparent.

- Member of enum/flag group: AlphaMode


## PRIM_ALPHA_MODE_NONE

- Type: integer | Value: `0`

- Meaning: Prim parameter setting for PRIM_ALPHA_MODE. Directs the face to ignore the alpha channel of the diffuse texture and render as completely opaque (default setting when a material face lacks an alpha channel).

- Member of enum/flag group: AlphaMode


## PRIM_BUMP_BARK

- Type: integer | Value: `4`

- Meaning: Face bump mapping setting: bark.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_BLOBS

- Type: integer | Value: `12`

- Meaning: Face bump mapping setting: petridish (blobby amoeba-like shapes).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_BRICKS

- Type: integer | Value: `5`

- Meaning: Face bump mapping setting: bricks.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_BRIGHT

- Type: integer | Value: `1`

- Meaning: Face bump mapping setting: brightness (generated from highlights).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_CHECKER

- Type: integer | Value: `6`

- Meaning: Face bump mapping setting: checker.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_CONCRETE

- Type: integer | Value: `7`

- Meaning: Face bump mapping setting: concrete.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_DARK

- Type: integer | Value: `2`

- Meaning: Face bump mapping setting: darkness (generated from lowlights).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_DISKS

- Type: integer | Value: `10`

- Meaning: Face bump mapping setting: discs (packed circles).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_GRAVEL

- Type: integer | Value: `11`

- Meaning: Face bump mapping setting: gravel.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_LARGETILE

- Type: integer | Value: `14`

- Meaning: Face bump mapping setting: stonetile (large tile).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_NONE

- Type: integer | Value: `0`

- Meaning: Face bump mapping setting: none (no bump map).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_SHINY

- Type: integer | Value: `19`

- Meaning: Prim parameter used to get or set both the shininess and bump mapping settings of a face.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_BUMP_SIDING

- Type: integer | Value: `13`

- Meaning: Face bump mapping setting: siding.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_STONE

- Type: integer | Value: `9`

- Meaning: Face bump mapping setting: cutstone (blocks).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_STUCCO

- Type: integer | Value: `15`

- Meaning: Face bump mapping setting: stucco.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_SUCTION

- Type: integer | Value: `16`

- Meaning: Face bump mapping setting: suction (rings).

- Member of enum/flag group: PrimBump


## PRIM_BUMP_TILE

- Type: integer | Value: `8`

- Meaning: Face bump mapping setting: crustytile.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_WEAVE

- Type: integer | Value: `17`

- Meaning: Face bump mapping setting: weave.

- Member of enum/flag group: PrimBump


## PRIM_BUMP_WOOD

- Type: integer | Value: `3`

- Meaning: Face bump mapping setting: woodgrain.

- Member of enum/flag group: PrimBump


## PRIM_CAST_SHADOWS

- Type: integer | Value: `24`

- Meaning: Deprecated prim parameter representing shadow casting settings for the primitive.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_CLICK_ACTION

- Type: integer | Value: `43`

- Meaning: Prim parameter followed by a CLICK_ACTION_* constant to specify the default action taken when a user clicks or touches the prim.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_COLLISION_SOUND

- Type: integer | Value: `53`

- Meaning: Prim parameter to set the collision sound UUID and volume level for the prim.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_COLOR

- Type: integer | Value: `18`

- Meaning: Prim parameter to get or set the Blinn-Phong color and opacity of a face.

integer face – face number or ALL_SIDES
vector color – color in RGB <R, G, B> (<0.0, 0.0, 0.0> = black, <1.0, 1.0, 1.0> = white)
float alpha – from 0.0 (clear) to 1.0 (solid) (0.0 <= alpha <= 1.0)


- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_DAMAGE

- Type: integer | Value: `51`

- Meaning: Prim parameter used to get or set the damage amount and damage type delivered by the prim on collision.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_DESC

- Type: integer | Value: `28`

- Meaning: Prim parameter [PRIM_DESC, string description] to get or set the prim's description (equivalent to llGetObjectDesc/llSetObjectDesc).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_FLEXIBLE

- Type: integer | Value: `21`

- Meaning: Prim parameter to get or set the prim's flexible configuration.

integer boolean – TRUE enables, FALSE disables
integer softness – ranges from 0 to 3
float gravity – ranges from -10.0 to 10.0
float friction – ranges from 0.0 to 10.0
float wind – ranges from 0.0 to 10.0
float tension – ranges from 0.0 to 10.0
vector force


- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_FULLBRIGHT

- Type: integer | Value: `20`

- Meaning: Prim parameter [PRIM_FULLBRIGHT, integer face, integer boolean] to get or set whether full-bright rendering is enabled on the specified face.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_GLOW

- Type: integer | Value: `25`

- Meaning: Prim parameter [PRIM_GLOW, integer face, float intensity] to get or set the glow intensity on a face (the compiler integer value is 25 if the named constant is rejected).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_GLTF_ALPHA_MODE_BLEND

- Type: integer | Value: `1`

- Meaning: GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Renders the material with transparency (alpha blending) in linear color space. Transparency from the texture is multiplied by the material's opacity multiplier. Note: This mode can suffer from depth sorting and performance issues.

- Member of enum/flag group: GLTFAlphaMode


## PRIM_GLTF_ALPHA_MODE_MASK

- Type: integer | Value: `2`

- Meaning: GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Renders the material as fully opaque where the alpha value is greater than the alpha cutoff, and fully transparent otherwise.

- Member of enum/flag group: GLTFAlphaMode


## PRIM_GLTF_ALPHA_MODE_OPAQUE

- Type: integer | Value: `0`

- Meaning: GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Ignores the alpha channel entirely and renders the face material as completely opaque.

- Member of enum/flag group: GLTFAlphaMode


## PRIM_GLTF_BASE_COLOR

- Type: integer | Value: `48`

- Meaning: Prim parameter to get or set the GLTF base color override of an object's face. Requires face, texture, repeats, offsets, rotation, linear_color (in linear space; use llsRGB2Linear), alpha_mode (PRIM_GLTF_ALPHA_MODE_*), alpha_cutoff, and double_sided arguments.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_GLTF_EMISSIVE

- Type: integer | Value: `46`

- Meaning: Prim parameter to get or set the GLTF emission override of a face. Requires face, texture, repeats, offsets, rotation, and emissive_tint (specified in linear space; use llsRGB2Linear).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_GLTF_METALLIC_ROUGHNESS

- Type: integer | Value: `47`

- Meaning: Prim parameter to get or set the GLTF occlusion/metallic/roughness override of a face. Requires face, texture, repeats, offsets, rotation, metallic_factor, and roughness_factor arguments.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_GLTF_NORMAL

- Type: integer | Value: `45`

- Meaning: Prim parameter to get or set the GLTF normal map override of a face. Requires face, texture, repeats, offsets, and rotation arguments.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_HEALTH

- Type: integer | Value: `52`

- Meaning: Prim parameter used to get or set the health of the prim. Objects default to 0 health.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_HOLE_CIRCLE

- Type: integer | Value: `0x10`

- Meaning: Parameter used with certain PRIM_TYPE_* flags to make a circular hole via the hole_shape parameter.

- Member of enum/flag group: PrimTypeHole


## PRIM_HOLE_DEFAULT

- Type: integer | Value: `0x00`

- Meaning: Parameter used with certain PRIM_TYPE_* flags to make a hole of the same shape as the outer shape via the hole_shape parameter.

- Member of enum/flag group: PrimTypeHole


## PRIM_HOLE_SQUARE

- Type: integer | Value: `0x20`

- Meaning: Parameter used with certain PRIM_TYPE_* flags to make a squarish hole via the hole_shape parameter.

- Member of enum/flag group: PrimTypeHole


## PRIM_HOLE_TRIANGLE

- Type: integer | Value: `0x30`

- Meaning: Parameter used with certain PRIM_TYPE_* flags to make a triangular hole via the hole_shape parameter.

- Member of enum/flag group: PrimTypeHole


## PRIM_LINK_TARGET

- Type: integer | Value: `34`

- Meaning: Prim parameter [PRIM_LINK_TARGET, integer link_target] used to get or set properties for multiple linked prims within a single primitive parameters call.

- Member of enum/flag group: PrimParam


## PRIM_MATERIAL

- Type: integer | Value: `2`

- Meaning: Prim parameter [PRIM_MATERIAL, integer PRIM_MATERIAL_*] to get or set the prim's material. The material determines the default collision sound, sprite, friction coefficient, and restitution coefficient (elasticity) without affecting mass.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_MATERIAL_DENSITY

- Type: integer | Value: `0x1`

- Member of enum/flag group: PhysicsMaterialParam


## PRIM_MATERIAL_FLESH

- Type: integer | Value: `4`

- Meaning: Prim material constant: flesh.

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MATERIAL_FRICTION

- Type: integer | Value: `0x2`

- Member of enum/flag group: PhysicsMaterialParam


## PRIM_MATERIAL_GLASS

- Type: integer | Value: `2`

- Meaning: Prim material constant: glass (features very low friction).

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MATERIAL_GRAVITY_MULTIPLIER

- Type: integer | Value: `0x8`

- Member of enum/flag group: PhysicsMaterialParam


## PRIM_MATERIAL_LIGHT

- Type: integer | Value: `7`

- Meaning: Deprecated prim material constant. Light is now a face property instead of a prim property; equivalent functionality is achieved using [PRIM_FULLBRIGHT, ALL_SIDES, TRUE].

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MATERIAL_METAL

- Type: integer | Value: `1`

- Meaning: Prim material constant: metal.

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MATERIAL_PLASTIC

- Type: integer | Value: `5`

- Meaning: Prim material constant: plastic.

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MATERIAL_RESTITUTION

- Type: integer | Value: `0x4`

- Member of enum/flag group: PhysicsMaterialParam


## PRIM_MATERIAL_RUBBER

- Type: integer | Value: `6`

- Meaning: Prim material constant: rubber.

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MATERIAL_STONE

- Type: integer | Value: `0`

- Meaning: Prim material constant: stone.

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MATERIAL_WOOD

- Type: integer | Value: `3`

- Meaning: Prim material constant: wood.

- Member of enum/flag group: PhysicsMaterialPreset


## PRIM_MEDIA_ALT_IMAGE_ENABLE

- Type: integer | Value: `0`

- Meaning: Boolean. Gets or sets the default image state (the image a user sees before media is active) on a face. The default is specified by the server for that media type. Note: This flag is not currently implemented.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_AUTO_LOOP

- Type: integer | Value: `4`

- Meaning: Boolean. Gets or sets whether auto-looping is enabled for the face media.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_AUTO_PLAY

- Type: integer | Value: `5`

- Meaning: Boolean. Gets or sets whether media auto-plays when a resident is able to view it.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_AUTO_SCALE

- Type: integer | Value: `6`

- Meaning: Boolean. Gets or sets whether auto-scaling is enabled, which forces the media to fill the entire texture size.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_AUTO_ZOOM

- Type: integer | Value: `7`

- Meaning: Boolean. Gets or sets whether clicking the media triggers auto-zoom and auto-focus.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_CONTROLS

- Type: integer | Value: `1`

- Meaning: Integer. Gets or sets the style of media controls (can be set to PRIM_MEDIA_CONTROLS_STANDARD or PRIM_MEDIA_CONTROLS_MINI).

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_CONTROLS_MINI

- Type: integer | Value: `1`

- Meaning: Mini web navigation controls constant; does not include an address bar.

- Member of enum/flag group: PrimMediaControl


## PRIM_MEDIA_CONTROLS_STANDARD

- Type: integer | Value: `0`

- Meaning: Standard web navigation controls constant.

- Member of enum/flag group: PrimMediaControl


## PRIM_MEDIA_CURRENT_URL

- Type: integer | Value: `2`

- Meaning: String. Gets or sets the current URL displayed on the chosen face (maximum 1024 characters). Changing this URL triggers media navigation.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_FIRST_CLICK_INTERACT

- Type: integer | Value: `8`

- Meaning: Boolean. Gets or sets what happens when someone click on a playing, but unfocused media face: TRUE: Does the same thing a focused media face does, and forwards the click to the web browser. FALSE: Focuses the media prim so that future clicks are forwarded to the web browser. Note: Viewer settings affect this flag. It works by default on most prims.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_HEIGHT_PIXELS

- Type: integer | Value: `10`

- Meaning: Integer. Gets or sets the height of the media in pixels.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_HOME_URL

- Type: integer | Value: `3`

- Meaning: String. Gets or sets the home URL for the chosen face (maximum 1024 characters).

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_MAX_HEIGHT_PIXELS

- Type: integer | Value: `2048`


## PRIM_MEDIA_MAX_URL_LENGTH

- Type: integer | Value: `1024`


## PRIM_MEDIA_MAX_WHITELIST_COUNT

- Type: integer | Value: `64`


## PRIM_MEDIA_MAX_WHITELIST_SIZE

- Type: integer | Value: `1024`


## PRIM_MEDIA_MAX_WIDTH_PIXELS

- Type: integer | Value: `2048`


## PRIM_MEDIA_PARAM_MAX

- Type: integer | Value: `14`


## PRIM_MEDIA_PERMS_CONTROL

- Type: integer | Value: `14`

- Meaning: Integer. Gets or sets the permissions mask controlling who can see the media control bar (PRIM_MEDIA_PERM_ANYONE, _GROUP, _NONE, or _OWNER).

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_PERMS_INTERACT

- Type: integer | Value: `13`

- Meaning: Integer. Gets or sets the permissions mask controlling who can interact with the media (PRIM_MEDIA_PERM_ANYONE, _GROUP, _NONE, or _OWNER).

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_PERM_ANYONE

- Type: integer | Value: `4`

- Member of enum/flag group: PrimMediaPerm


## PRIM_MEDIA_PERM_GROUP

- Type: integer | Value: `2`

- Member of enum/flag group: PrimMediaPerm


## PRIM_MEDIA_PERM_NONE

- Type: integer | Value: `0`

- Member of enum/flag group: PrimMediaPerm


## PRIM_MEDIA_PERM_OWNER

- Type: integer | Value: `1`

- Member of enum/flag group: PrimMediaPerm


## PRIM_MEDIA_WHITELIST

- Type: integer | Value: `12`

- Meaning: Gets or sets the media whitelist as an array of URL strings (up to 64 URLs or 1024 characters, whichever comes first). At the SLua level, provide a {string} array; the serializer encodes it as an escaped, comma-separated string for the underlying LSL API.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_WHITELIST_ENABLE

- Type: integer | Value: `11`

- Meaning: Boolean. Gets or sets whether media navigation is restricted to the URLs listed in PRIM_MEDIA_WHITELIST.

- Member of enum/flag group: PrimMediaParam


## PRIM_MEDIA_WIDTH_PIXELS

- Type: integer | Value: `9`

- Meaning: Integer. Gets or sets the width of the media in pixels.

- Member of enum/flag group: PrimMediaParam


## PRIM_NAME

- Type: integer | Value: `27`

- Meaning: Prim parameter [PRIM_NAME, string name] to get or set the prim's name (equivalent to llGetObjectName/llSetObjectName).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_NORMAL

- Type: integer | Value: `37`

- Meaning: Prim parameter to get or set the Blinn-Phong normal map texture settings of a face. Requires face, texture, repeats, offsets, and rotation_in_radians arguments.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_OMEGA

- Type: integer | Value: `32`

- Meaning: Prim parameter to get, set, or disable a client-side physical-like rotation (analogous to llTargetOmega).

vector axis – arbitrary axis to rotate the object around
float spinrate – rate of rotation in radians per second
float gain – also modulates the final spinrate and disables the rotation behavior if zero


- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_PHANTOM

- Type: integer | Value: `5`

- Meaning: Prim parameter [PRIM_PHANTOM, integer boolean] to get or set whether phantom status is enabled.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_PHYSICS

- Type: integer | Value: `3`

- Meaning: Prim parameter [PRIM_PHYSICS, integer boolean] to get or set whether the object responds to Second Life physics.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_PHYSICS_SHAPE_CONVEX

- Type: integer | Value: `2`

- Meaning: Physics shape type setting. Uses the convex hull of the prim shape to generate its physics representation (the default for mesh objects).

- Member of enum/flag group: PhysicsShapeType


## PRIM_PHYSICS_SHAPE_NONE

- Type: integer | Value: `1`

- Meaning: Physics shape type setting. Directs the physics engine to ignore this prim entirely, preventing it from contributing to the linkset's physics shape. Note: Cannot be applied to the root prim.

- Member of enum/flag group: PhysicsShapeType


## PRIM_PHYSICS_SHAPE_PRIM

- Type: integer | Value: `0`

- Meaning: Physics shape type setting. Uses the actual visible shape of the prim to determine its physics representation (the default for all non-mesh objects).

- Member of enum/flag group: PhysicsShapeType


## PRIM_PHYSICS_SHAPE_TYPE

- Type: integer | Value: `30`

- Meaning: Prim parameter used to get or set the type of shape the physics engine uses for the prim (PRIM_PHYSICS_SHAPE_NONE, _PRIM, or _CONVEX). Mainly used for physics optimization.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_POINT_LIGHT

- Type: integer | Value: `23`

- Meaning: Prim parameter to configure local lighting.
Accepts color in linear space (use llsRGB2Linear to convert from sRGB).

integer boolean – TRUE enables, FALSE disables
vector linear_color – linear color in RGB <R, G, B&> (<0.0, 0.0, 0.0> = black, <1.0, 1.0, 1.0> = white)
float intensity – ranges from 0.0 to 1.0
float radius – ranges from 0.1 to 20.0
float falloff – ranges from 0.01 to 2.0


- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_POSITION

- Type: integer | Value: `6`

- Meaning: Prim parameter [PRIM_POSITION, vector position] to get or set the position of the prim in region coordinates (or local coordinates depending on the script context).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_POS_LOCAL

- Type: integer | Value: `33`

- Meaning: Prim parameter [PRIM_POS_LOCAL, vector position] to get or set the local position of a prim (equivalent to llGetLocalPos/llSetPos).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_PROJECTOR

- Type: integer | Value: `42`

- Meaning: Prim parameter [PRIM_PROJECTOR, string texture, float fov, float focus, float ambiance] to configure light projection settings. If the prim is not configured as a projector, the texture key will return NULL_KEY.

- Member of enum/flag group: PrimParam


## PRIM_REFLECTION_PROBE

- Type: integer | Value: `44`

- Meaning: Prim parameter to configure the object as a custom-placed reflection probe for Image-Based Lighting (IBL). Only affects objects inside its volume of influence.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_REFLECTION_PROBE_BOX

- Type: integer | Value: `1`

- Meaning: Flag option used with PRIM_REFLECTION_PROBE. When set, the reflection probe volume is a box; when unset, it defaults to a sphere.

- Member of enum/flag group: ReflectionProbeType


## PRIM_REFLECTION_PROBE_DYNAMIC

- Type: integer | Value: `2`

- Meaning: Flag option used with PRIM_REFLECTION_PROBE. When set, the probe dynamically includes avatars in its image-based lighting reflections (which carries a rendering performance cost).

- Member of enum/flag group: ReflectionProbeType


## PRIM_REFLECTION_PROBE_MIRROR

- Type: integer | Value: `4`

- Meaning: Flag option used with PRIM_REFLECTION_PROBE. When set, intersecting low-roughness PBR materials act as mirrors. Note: Mirrors do not reflect avatars unless PRIM_REFLECTION_PROBE_DYNAMIC is also enabled, and they carry a performance cost.

- Member of enum/flag group: ReflectionProbeType


## PRIM_RENDER_MATERIAL

- Type: integer | Value: `49`

- Meaning: Prim parameter [PRIM_RENDER_MATERIAL, integer face, string material] to get or set face material settings. Note: Setting this clears most PRIM_GLTF_* properties on the face, except for repeats, offsets, and rotation_in_radians.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_ROTATION

- Type: integer | Value: `8`

- Meaning: Prim parameter [PRIM_ROTATION, rotation global_rot] to get or set the global rotation of the prim (equivalent to llGetRot/llSetRot; note that setting this on child prims may be broken).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_ROT_LOCAL

- Type: integer | Value: `29`

- Meaning: Prim parameter [PRIM_ROT_LOCAL, rotation local_rot] to get or set the local rotation of a prim (equivalent to llGetLocalRot/llSetLocalRot).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_SCRIPTED_SIT_ONLY

- Type: integer | Value: `40`

- Meaning: Prim parameter restricting manual sitting on this prim. When active, sitting can only be initiated via llSitOnLink; manual sitting attempts fail. This restriction applies even outside experience-enabled regions.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_SCULPT_FLAG_ANIMESH

- Type: integer | Value: `32`

- Meaning: Read-only flag for PRIM_TYPE_SCULPT to query whether the object is an Animated Mesh (Animesh).

- Member of enum/flag group: PrimTypeSculptFlag


## PRIM_SCULPT_FLAG_INVERT

- Type: integer | Value: `64`

- Meaning: Flag for PRIM_TYPE_SCULPT to render the sculpted prim inside-out by inverting the normals of each polygon.

- Member of enum/flag group: PrimTypeSculptFlag


## PRIM_SCULPT_FLAG_MIRROR

- Type: integer | Value: `128`

- Meaning: Flag for PRIM_TYPE_SCULPT to render a mirror-image of the sculpted prim, mirrored across the X-axis.

- Member of enum/flag group: PrimTypeSculptFlag


## PRIM_SCULPT_TYPE_CYLINDER

- Type: integer | Value: `4`

- Meaning: Sculpt type option for PRIM_TYPE_SCULPT that stitches the left side to the right to produce a cylinder-shaped sculpted prim.

- Member of enum/flag group: PrimTypeSculptType


## PRIM_SCULPT_TYPE_MASK

- Type: integer | Value: `7`

- Meaning: Bitmask used when parsing sculpted prim properties (PRIM_TYPE_SCULPT) from llGetPrimitiveParams to separate the base sculpt type from modifying flags (invert or mirror).

- Member of enum/flag group: PrimTypeSculptType


## PRIM_SCULPT_TYPE_MESH

- Type: integer | Value: `5`

- Meaning: Sculpt type option for PRIM_TYPE_SCULPT indicating the object is a uploaded Mesh model.

- Member of enum/flag group: PrimTypeSculptType


## PRIM_SCULPT_TYPE_PLANE

- Type: integer | Value: `3`

- Meaning: Sculpt type option for PRIM_TYPE_SCULPT that performs no stitching or converging, producing a flat plane-shaped sculpted prim.

- Member of enum/flag group: PrimTypeSculptType


## PRIM_SCULPT_TYPE_SPHERE

- Type: integer | Value: `1`

- Meaning: Sculpt type option for PRIM_TYPE_SCULPT that stitches the left side to the right and separately converges the top and bottom to produce a sphere-shaped sculpted prim.

- Member of enum/flag group: PrimTypeSculptType


## PRIM_SCULPT_TYPE_TORUS

- Type: integer | Value: `2`

- Meaning: Sculpt type option for PRIM_TYPE_SCULPT that stitches top-to-bottom and left-to-right to produce a torus-shaped sculpted prim.

- Member of enum/flag group: PrimTypeSculptType


## PRIM_SHINY_HIGH

- Type: integer | Value: `3`

- Meaning: Sets the highest intensity legacy face shininess setting.

- Member of enum/flag group: PrimShiny


## PRIM_SHINY_LOW

- Type: integer | Value: `1`

- Meaning: Sets the lowest intensity legacy face shininess setting.

- Member of enum/flag group: PrimShiny


## PRIM_SHINY_MEDIUM

- Type: integer | Value: `2`

- Meaning: Sets a medium intensity legacy face shininess setting.

- Member of enum/flag group: PrimShiny


## PRIM_SHINY_NONE

- Type: integer | Value: `0`

- Meaning: Disables the legacy face shininess setting.

- Member of enum/flag group: PrimShiny


## PRIM_SIT_FLAGS

- Type: integer | Value: `50`

- Meaning: Prim parameter used to get or set sit-related flags currently active on the prim.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_SIT_TARGET

- Type: integer | Value: `41`

- Meaning: Prim parameter [PRIM_SIT_TARGET, integer boolean, vector offset, rotation rot] to get or set the prim's sit target. Setting the boolean to FALSE deactivates the target. Unlike llLinkSitTarget, offset <0.0, 0.0, 0.0> can be explicitly set.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_SIZE

- Type: integer | Value: `7`

- Meaning: Prim parameter [PRIM_SIZE, vector size] to get or set the prim's physical dimensions (equivalent to llGetScale/llSetScale).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_SLICE

- Type: integer | Value: `35`

- Meaning: Prim parameter [PRIM_SLICE, vector slice] to get or set the prim's slice values (a shape attribute equivalent to advanced cut).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_SPECULAR

- Type: integer | Value: `36`

- Meaning: Prim parameter to get or set the Blinn-Phong specular map texture settings of a face. Requires face, texture, repeats, offsets, rotation_in_radians, color, glossy, and environment arguments.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_TEMP_ON_REZ

- Type: integer | Value: `4`

- Meaning: Prim parameter used to get or set the object's temporary status. Temporary objects live until the next garbage collection cycle (about 1 minute), do not count against normal prim limits, but are subject to regional limits.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_TEXGEN

- Type: integer | Value: `22`

- Meaning: Prim parameter [PRIM_TEXGEN, integer face, integer mode] to get or set the texture mapping mode of the face.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_TEXGEN_DEFAULT

- Type: integer | Value: `0`

- Meaning: Texture mapping mode setting for PRIM_TEXGEN. Specifies that texture repeat units are measured in texture repeats per face.

- Member of enum/flag group: PrimTexgen


## PRIM_TEXGEN_PLANAR

- Type: integer | Value: `1`

- Meaning: Texture mapping mode setting for PRIM_TEXGEN. Specifies that texture repeat units are measured in repeats per half-meter (unlike the in-world editor, which measures in repeats per meter).

- Member of enum/flag group: PrimTexgen


## PRIM_TEXT

- Type: integer | Value: `26`

- Meaning: Prim parameter [PRIM_TEXT, string text, vector color, float alpha] to get or set the object's floating/hover text (equivalent to llSetText).

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_TEXTURE

- Type: integer | Value: `17`

- Meaning: Prim parameter [PRIM_TEXTURE, integer face, string texture, vector repeats, vector offsets, float rotation_in_radians] to get or set the Blinn-Phong diffuse texture settings of a face.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_TYPE

- Type: integer | Value: `9`

- Meaning: Prim parameter used to get or set the geometric shape type (PRIM_TYPE_*) and its associated parameters.

- Member of enum/flag group: PrimParam, PrimParamGet


## PRIM_TYPE_BOX

- Type: integer | Value: `0`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a box and configure its shape properties.

- Member of enum/flag group: PrimType


## PRIM_TYPE_CYLINDER

- Type: integer | Value: `1`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a cylinder and configure its shape properties.

- Member of enum/flag group: PrimType


## PRIM_TYPE_PRISM

- Type: integer | Value: `2`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a prism and configure its shape properties.

- Member of enum/flag group: PrimType


## PRIM_TYPE_RING

- Type: integer | Value: `6`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a ring and configure its shape properties.

- Member of enum/flag group: PrimType


## PRIM_TYPE_SCULPT

- Type: integer | Value: `7`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a sculpted prim (sculpty) or mesh of a specific type.

- Member of enum/flag group: PrimType


## PRIM_TYPE_SPHERE

- Type: integer | Value: `3`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a sphere and configure its shape properties.

- Member of enum/flag group: PrimType


## PRIM_TYPE_TORUS

- Type: integer | Value: `4`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a torus and configure its shape properties.

- Member of enum/flag group: PrimType


## PRIM_TYPE_TUBE

- Type: integer | Value: `5`

- Meaning: Shape parameter for PRIM_TYPE used to define the prim as a tube and configure its shape properties.

- Member of enum/flag group: PrimType


## PROFILE_NONE

- Type: integer | Value: `0`

- Meaning: Disables script profiling.

- Member of enum/flag group: ScriptProfileMode


## PROFILE_SCRIPT_MEMORY

- Type: integer | Value: `1`

- Meaning: Enables script memory profiling, tracking the maximum amount of memory consumed while it is active.

- Member of enum/flag group: ScriptProfileMode


## PSYS_PART_BF_DEST_COLOR

- Type: integer | Value: `2`

- Meaning: Scales the RGBA values by the RGBA values of the destination.

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BF_ONE

- Type: integer | Value: `0`

- Meaning: PSYS_PART_BF_ONE

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BF_ONE_MINUS_DEST_COLOR

- Type: integer | Value: `4`

- Meaning: Scales the RGBA values by the inverted RGBA values of the destination.

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BF_ONE_MINUS_SOURCE_ALPHA

- Type: integer | Value: `9`

- Meaning: Scales the RGBA values by the inverted alpha values of the particle source.

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BF_ONE_MINUS_SOURCE_COLOR

- Type: integer | Value: `5`

- Meaning: Scales the RGBA values by the inverted RGBA values of the particle source.

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BF_SOURCE_ALPHA

- Type: integer | Value: `7`

- Meaning: Scales the RGBA values by the alpha values of the particle source.

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BF_SOURCE_COLOR

- Type: integer | Value: `3`

- Meaning: Scales the RGBA values by the RGBA values of the particle source.

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BF_ZERO

- Type: integer | Value: `1`

- Meaning: Zeros out the source or destination RGBA values.

- Member of enum/flag group: ParticleBlendFunc


## PSYS_PART_BLEND_FUNC_DEST

- Type: integer | Value: `25`

- Meaning: Integer parameter defining the destination blending function.

- Member of enum/flag group: ParticleParam


## PSYS_PART_BLEND_FUNC_SOURCE

- Type: integer | Value: `24`

- Meaning: Integer parameter defining the source blending function.

- Member of enum/flag group: ParticleParam


## PSYS_PART_BOUNCE_MASK

- Type: integer | Value: `0x4`

- Meaning: Particle flag causing particles to bounce off a plane at the emitter object's Z height.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_EMISSIVE_MASK

- Type: integer | Value: `0x100`

- Meaning: Particle flag that makes particles full-bright and unaffected by global lighting (sunlight). Otherwise, particles are lit by current global lighting or local point lights.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_END_ALPHA

- Type: integer | Value: `4`

- Meaning: Float parameter that determines the ending alpha (transparency) of the particles.

- Member of enum/flag group: ParticleParam


## PSYS_PART_END_COLOR

- Type: integer | Value: `3`

- Meaning: Vector parameter <r, g, b> that determines the ending color of the particles.

- Member of enum/flag group: ParticleParam


## PSYS_PART_END_GLOW

- Type: integer | Value: `27`

- Meaning: Float parameter that determines the ending glow value of the particles.

- Member of enum/flag group: ParticleParam


## PSYS_PART_END_SCALE

- Type: integer | Value: `6`

- Meaning: Vector parameter <sx, sy, z> defining the ending size of the particle billboard in meters (z-axis value is ignored).

- Member of enum/flag group: ParticleParam


## PSYS_PART_FLAGS

- Type: integer | Value: `0`

- Meaning: Integer bitfield parameter specifying the simulation flags for emitted particles. Multiple flags can be combined using bitwise OR (|).

- Member of enum/flag group: ParticleParam


## PSYS_PART_FOLLOW_SRC_MASK

- Type: integer | Value: `0x10`

- Meaning: Particle flag causing particle positions to remain relative to the position and movement of the emitter. Enabling this flag disables the PSYS_SRC_BURST_RADIUS rule.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_FOLLOW_VELOCITY_MASK

- Type: integer | Value: `0x20`

- Meaning: Particle flag causing particles to rotate and orient their vertical 'top' toward their direction of movement or emission. Otherwise, they remain vertically oriented with the top of the texture facing up.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_INTERP_COLOR_MASK

- Type: integer | Value: `0x1`

- Meaning: Particle flag causing the particle's color and alpha to smoothly interpolate from their START values to their END values over its lifetime.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_INTERP_SCALE_MASK

- Type: integer | Value: `0x2`

- Meaning: Particle flag causing the particle's size/scale to transition from its START setting to its END setting over its lifetime.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_MAX_AGE

- Type: integer | Value: `7`

- Meaning: Float parameter specifying the lifetime (age in seconds) of an individual particle before it dies.

- Member of enum/flag group: ParticleParam


## PSYS_PART_RIBBON_MASK

- Type: integer | Value: `0x400`

- Meaning: Particle flag that joins emitted particles into a continuous ribbon strip. Textures stretch to join adjacent edges. Width is controlled by the 'x' start/end scale; 'y' controls maximum visibility distance. Ribbon segments are not camera-facing, mimic the emitter's Z-axis, and require horizontal movement to render.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_START_ALPHA

- Type: integer | Value: `2`

- Meaning: Float parameter that determines the starting alpha (transparency) of the particles.

- Member of enum/flag group: ParticleParam


## PSYS_PART_START_COLOR

- Type: integer | Value: `1`

- Meaning: Vector parameter <r, g, b> that determines the starting color of the particles.

- Member of enum/flag group: ParticleParam


## PSYS_PART_START_GLOW

- Type: integer | Value: `26`

- Meaning: Float parameter that determines the starting glow value of the particles.

- Member of enum/flag group: ParticleParam


## PSYS_PART_START_SCALE

- Type: integer | Value: `5`

- Meaning: Vector parameter <sx, sy, z> defining the starting size of the particle billboard in meters (z-axis value is ignored).

- Member of enum/flag group: ParticleParam


## PSYS_PART_TARGET_LINEAR_MASK

- Type: integer | Value: `0x80`

- Meaning: Particle flag causing emitted particles to move in a straight, evenly-spaced line toward the PSYS_SRC_TARGET_KEY target. Ignores non-DROP patterns, radius, burst speeds, angles, omega, acceleration, and wind. Combining with bounce while target is below emitter deflects particles upward.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_TARGET_POS_MASK

- Type: integer | Value: `0x40`

- Meaning: Particle flag causing emitted particles to change course and travel toward the target specified by PSYS_SRC_TARGET_KEY during their lifetime. If no valid or reachable target is set, particles target the emitting prim itself.

- Member of enum/flag group: ParticleFlag


## PSYS_PART_WIND_MASK

- Type: integer | Value: `0x8`

- Meaning: Particle flag that applies wind as a secondary force on the particles, damping their velocity toward the wind velocity.

- Member of enum/flag group: ParticleFlag


## PSYS_SRC_ACCEL

- Type: integer | Value: `8`

- Meaning: Vector parameter <x, y, z> specifying the constant acceleration to apply to particles.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_ANGLE_BEGIN

- Type: integer | Value: `22`

- Meaning: Float parameter specifying the angle in radians where particles will not be created (for ANGLE patterns).

- Member of enum/flag group: ParticleParam


## PSYS_SRC_ANGLE_END

- Type: integer | Value: `23`

- Meaning: Float parameter specifying the ending angle in radians to be filled with particles (for ANGLE patterns). If smaller than angle_begin, their roles are swapped.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_BURST_PART_COUNT

- Type: integer | Value: `15`

- Meaning: Integer parameter specifying the number of particles to release in each burst.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_BURST_RADIUS

- Type: integer | Value: `16`

- Meaning: Float parameter specifying the radial distance from the emitter's center at which particles are created.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_BURST_RATE

- Type: integer | Value: `13`

- Meaning: Float parameter specifying the interval in seconds between particle bursts.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_BURST_SPEED_MAX

- Type: integer | Value: `18`

- Meaning: Float parameter specifying the maximum initial speed of emitted particles.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_BURST_SPEED_MIN

- Type: integer | Value: `17`

- Meaning: Float parameter specifying the minimum initial speed of emitted particles.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_INNERANGLE

- Type: integer | Value: `10`

- Meaning: Float parameter specifying the inner angle of the arc for ANGLE or ANGLE_CONE patterns. The specified inner area will not contain particles.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_MAX_AGE

- Type: integer | Value: `19`

- Meaning: Float parameter specifying the active duration of the particle system in seconds (0.0 means forever).

- Member of enum/flag group: ParticleParam


## PSYS_SRC_OBJ_REL_MASK

- Type: integer | Value: `0x1`

- Member of enum/flag group: ParticleParam


## PSYS_SRC_OMEGA

- Type: integer | Value: `21`

- Meaning: Vector parameter setting the angular velocity used to rotate the emission axis for ANGLE and ANGLE_CONE patterns.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_OUTERANGLE

- Type: integer | Value: `11`

- Meaning: Float parameter specifying the outer angle of the arc for ANGLE or ANGLE_CONE patterns. The area between the outer and inner angles is filled with particles.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_PATTERN

- Type: integer | Value: `9`

- Meaning: Integer parameter specifying the generation pattern (PSYS_SRC_PATTERN_*) used to emit particles.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_PATTERN_ANGLE

- Type: integer | Value: `0x04`

- Meaning: Emission pattern that sprays particles outward in a flat circular, semi-circular, arc, or ray-shaped 2D area (around the prim's local X-axis) as defined by the start/end and inner/outer angle parameters.

- Member of enum/flag group: ParticleSourcePattern


## PSYS_SRC_PATTERN_ANGLE_CONE

- Type: integer | Value: `0x08`

- Meaning: Emission pattern that sprays particles outward in a 3D spherical, conical, or ring-shaped area defined by the start/end and inner/outer angle parameters. Can emulate the EXPLODE pattern if angles are set to 0.0 and PI.

- Member of enum/flag group: ParticleSourcePattern


## PSYS_SRC_PATTERN_ANGLE_CONE_EMPTY

- Type: integer | Value: `0x10`

- Meaning: Incomplete emission pattern that behaves identically to the DROP pattern. Intended to invert the ANGLE parameters to define an empty area where particles are not sprayed.

- Member of enum/flag group: ParticleSourcePattern


## PSYS_SRC_PATTERN_DROP

- Type: integer | Value: `0x01`

- Meaning: Emission pattern that drops particles at the source position with no initial velocity. Overrides burst radius, minimum speed, and maximum speed settings to 0.0.

- Member of enum/flag group: ParticleSourcePattern


## PSYS_SRC_PATTERN_EXPLODE

- Type: integer | Value: `0x02`

- Meaning: Emission pattern that shoots particles outward in all directions using the burst parameters.

- Member of enum/flag group: ParticleSourcePattern


## PSYS_SRC_TARGET_KEY

- Type: integer | Value: `20`

- Meaning: Key (UUID) of the target object that particles travel toward when PSYS_PART_TARGET_POS_MASK or PSYS_PART_TARGET_LINEAR_MASK is enabled.

- Member of enum/flag group: ParticleParam


## PSYS_SRC_TEXTURE

- Type: integer | Value: `12`

- Meaning: String parameter specifying the inventory name or UUID asset key of the texture used for the particles.

- Member of enum/flag group: ParticleParam


## PUBLIC_CHANNEL

- Type: integer | Value: `0`

- Meaning: Integer constant representing the open local chat channel. Passing this to chat functions (llSay, llWhisper, llShout) prints text to the publicly heard chat seen by nearby users and objects.

- Member of enum/flag group: Channel


## PURSUIT_FUZZ_FACTOR

- Type: integer | Value: `3`

- Meaning: Option for llPursue that selects a random destination near the PURSUIT_OFFSET (range is 0 to 1, where 1 is most random). Requires a non-zero PURSUIT_OFFSET.

- Member of enum/flag group: CharacterPursueParam


## PURSUIT_GOAL_TOLERANCE

- Type: integer | Value: `5`

- Meaning: Option for llPursue defining how close (between 0.25m and 10m) the character must be to consider the goal reached.

- Member of enum/flag group: CharacterPursueParam


## PURSUIT_INTERCEPT

- Type: integer | Value: `4`

- Meaning: Option for llPursue specifying whether the pathfinding character attempts to predict and intercept the target's future location.

- Member of enum/flag group: CharacterPursueParam


## PURSUIT_OFFSET

- Type: integer | Value: `1`

- Meaning: Option for llPursue specifying a constant position offset relative to the target for the character to navigate toward.

- Member of enum/flag group: CharacterPursueParam


## PU_EVADE_HIDDEN

- Type: integer | Value: `0x07`

- Meaning: Path update status code triggered when an llEvade character determines it has successfully hidden from its pursuer.

- Member of enum/flag group: CharacterPathUpdateType


## PU_EVADE_SPOTTED

- Type: integer | Value: `0x08`

- Meaning: Path update status code triggered when an llEvade character switches from hiding to running.

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_DYNAMIC_PATHFINDING_DISABLED

- Type: integer | Value: `10`

- Meaning: Path update failure code triggered when a character enters a region where dynamic pathfinding has been disabled in the Region Debug Console.

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_INVALID_GOAL

- Type: integer | Value: `0x03`

- Meaning: Path update failure code triggered when the specified goal is not on the region's navigation mesh (navmesh) and is unreachable.

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_INVALID_START

- Type: integer | Value: `0x02`

- Meaning: Path update failure code triggered when the character is at an unnavigable starting position (e.g., off the navmesh or too high above it).

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_NO_NAVMESH

- Type: integer | Value: `0x09`

- Meaning: Path update fatal error triggered when there is no navmesh generated for the region (typically indicates a server failure).

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_NO_VALID_DESTINATION

- Type: integer | Value: `0x06`

- Meaning: Path update failure code triggered when no reachable destinations remain (e.g., all patrol waypoints are blocked).

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_OTHER

- Type: integer | Value: `1000000`

- Meaning: Path update failure code representing an unspecified or general failure.

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_PARCEL_UNREACHABLE

- Type: integer | Value: `11`

- Meaning: Path update failure code triggered when a character is blocked from entering a parcel (e.g., the parcel is full or object entry was disabled after the navmesh was baked).

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_TARGET_GONE

- Type: integer | Value: `0x05`

- Meaning: Path update failure code triggered when an llPursue or llEvade target can no longer be tracked (e.g., they left the region or went more than ~30m outside region boundaries).

- Member of enum/flag group: CharacterPathUpdateType


## PU_FAILURE_UNREACHABLE

- Type: integer | Value: `0x04`

- Meaning: Path update failure code triggered when a previously valid goal becomes unreachable (e.g., an obstacle blocks the path).

- Member of enum/flag group: CharacterPathUpdateType


## PU_GOAL_REACHED

- Type: integer | Value: `0x01`

- Meaning: Path update status code triggered when the character reaches its goal and either stops or chooses a new goal (if wandering).

- Member of enum/flag group: CharacterPathUpdateType


## PU_SLOWDOWN_DISTANCE_REACHED

- Type: integer | Value: `0x00`

- Meaning: Path update status code triggered when the character enters the slowdown distance near its current goal.

- Member of enum/flag group: CharacterPathUpdateType


## RAD_TO_DEG

- Type: float | Value: `57.2957795`

- Meaning: 180/PI. Multiply a value in radians by this number to convert it to degrees.


## RCERR_CAST_TIME_EXCEEDED

- Type: integer | Value: `-3`

- Meaning: Raycast error indicating the parcel or agent exceeded the maximum allocated raycast time. Waiting a few frames and retrying will usually succeed as resources replenish.

- Member of enum/flag group: RayCastError


## RCERR_SIM_PERF_LOW

- Type: integer | Value: `-2`

- Meaning: Raycast error indicating the request failed due to low simulator performance. Wait before retrying, and if possible, reduce scene complexity.

- Member of enum/flag group: RayCastError


## RCERR_UNKNOWN

- Type: integer | Value: `-1`

- Meaning: Raycast error indicating an unspecified failure.

- Member of enum/flag group: RayCastError


## RC_DATA_FLAGS

- Type: integer | Value: `2`

- Meaning: Flag used with llCastRay to configure returned data.

- Member of enum/flag group: RayCastParam


## RC_DETECT_PHANTOM

- Type: integer | Value: `1`

- Meaning: Flag used with llCastRay. If set to TRUE (or non-zero), detects both phantom and volume-detect objects (they cannot be filtered individually). This overrides the RC_REJECT_NONPHYSICAL and RC_REJECT_PHYSICAL settings in RC_REJECT_TYPES.

- Member of enum/flag group: RayCastParam


## RC_GET_LINK_NUM

- Type: integer | Value: `4`

- Meaning: Flag used with llCastRay causing the results stride to include the specific link number that was hit.

- Member of enum/flag group: RayCastData


## RC_GET_NORMAL

- Type: integer | Value: `1`

- Meaning: Flag used with llCastRay causing the results stride to include the surface normal vector of the impact point.

- Member of enum/flag group: RayCastData


## RC_GET_ROOT_KEY

- Type: integer | Value: `2`

- Meaning: Flag used with llCastRay that returns the key of the hit object's root prim instead of the hit child prim.

- Member of enum/flag group: RayCastData


## RC_MAX_HITS

- Type: integer | Value: `3`

- Meaning: Flag used with llCastRay to set the maximum number of hits to return (up to 256). To avoid performance issues, keep this value small.

- Member of enum/flag group: RayCastParam


## RC_REJECT_AGENTS

- Type: integer | Value: `1`

- Meaning: Flag used with llCastRay to prevent the detection of avatars.

- Member of enum/flag group: RayCastRejectType


## RC_REJECT_LAND

- Type: integer | Value: `8`

- Meaning: Flag used with llCastRay to ignore the actual terrain ground (land).

- Member of enum/flag group: RayCastRejectType


## RC_REJECT_NONPHYSICAL

- Type: integer | Value: `4`

- Meaning: Flag used with llCastRay to ignore non-physical objects.

- Member of enum/flag group: RayCastRejectType


## RC_REJECT_PHYSICAL

- Type: integer | Value: `2`

- Meaning: Flag used with llCastRay to ignore physical objects.

- Member of enum/flag group: RayCastRejectType


## RC_REJECT_TYPES

- Type: integer | Value: `0`

- Meaning: Flag used with llCastRay to define a mask for ignoring specific types of objects and avatars.

- Member of enum/flag group: RayCastParam


## REGION_FLAG_ALLOW_DAMAGE

- Type: integer | Value: `0x1`

- Meaning: Flag used with llGetRegionFlags to check if the region is entirely damage-enabled.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_ALLOW_DIRECT_TELEPORT

- Type: integer | Value: `0x100000`

- Meaning: Flag used with llGetRegionFlags to check if direct teleportation is allowed in the region.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_BLOCK_FLY

- Type: integer | Value: `0x80000`

- Meaning: Flag used with llGetRegionFlags to check if flying is blocked/disabled in the region.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_BLOCK_FLYOVER

- Type: integer | Value: `0x8000000`

- Member of enum/flag group: RegionFlag


## REGION_FLAG_BLOCK_TERRAFORM

- Type: integer | Value: `0x40`

- Meaning: Flag used with llGetRegionFlags to check if terraforming is disabled in the region.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_DISABLE_COLLISIONS

- Type: integer | Value: `0x1000`

- Meaning: Flag used with llGetRegionFlags to check if collisions have been disabled in the region.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_DISABLE_PHYSICS

- Type: integer | Value: `0x4000`

- Meaning: Flag used with llGetRegionFlags to check if physics has been disabled in the region.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_FIXED_SUN

- Type: integer | Value: `0x10`

- Meaning: Flag used with llGetRegionFlags to check if the sun's position is fixed in the region.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_RESTRICT_PUSHOBJECT

- Type: integer | Value: `0x400000`

- Meaning: Flag used with llGetRegionFlags to check if llPushObject is restricted in the region.

- Member of enum/flag group: RegionFlag


## REGION_FLAG_SANDBOX

- Type: integer | Value: `0x100`

- Meaning: Flag used with llGetRegionFlags to check if the region is designated as a sandbox.

- Member of enum/flag group: RegionFlag


## REMOTE_DATA_CHANNEL

- Type: integer | Value: `1`

- Member of enum/flag group: RemoteDataEventType


## REMOTE_DATA_REPLY

- Type: integer | Value: `3`

- Member of enum/flag group: RemoteDataEventType


## REMOTE_DATA_REQUEST

- Type: integer | Value: `2`

- Member of enum/flag group: RemoteDataEventType


## REQUIRE_LINE_OF_SIGHT

- Type: integer | Value: `2`

- Meaning: Option flag for llPursue defining whether the character requires a physical line-of-sight to chase the target. When active, it will not target positions blocked by solid obstacles.

- Member of enum/flag group: CharacterPursueParam


## RESTITUTION

- Type: integer | Value: `4`

- Meaning: Used with llSetPhysicsMaterial to enable the restitution (bounciness) value (must be between 0.0 and 1.0) which overrides the previous value.

- Member of enum/flag group: PhysicsMaterialParam


## REVERSE

- Type: integer | Value: `0x4`

- Meaning: Used with texture animation functions to cause the animation to play in reverse (from end to start).

- Member of enum/flag group: TextureAnimMode


## REZ_ACCEL

- Type: integer | Value: `5`

- Meaning: Rez parameter specifying a constant acceleration force to apply to the rezzed object (as a [vector force, integer relative] pair). If relative is TRUE, the vector is in local coordinates.

- Member of enum/flag group: RezParam


## REZ_DAMAGE

- Type: integer | Value: `8`

- Meaning: Rez parameter specifying the float damage amount the rezzed object inflicts on an agent upon collision.

- Member of enum/flag group: RezParam


## REZ_DAMAGE_TYPE

- Type: integer | Value: `12`

- Meaning: Rez parameter specifying the integer damage type applied on collision (supports DAMAGE_TYPE_* constants, custom types, or a repurposed damage field).

- Member of enum/flag group: RezParam


## REZ_FLAGS

- Type: integer | Value: `1`

- Meaning: Rez parameter specifying the integer bitfield of flags to apply to the newly created object.

- Member of enum/flag group: RezParam


## REZ_FLAG_BLOCK_GRAB_OBJECT

- Type: integer | Value: `0x0080`

- Meaning: Rez flag that disables grabbing on the newly rezzed object.

- Member of enum/flag group: RezFlag


## REZ_FLAG_DIE_ON_COLLIDE

- Type: integer | Value: `0x0008`

- Meaning: Rez flag causing the object to die/delete after its first collision.

- Member of enum/flag group: RezFlag


## REZ_FLAG_DIE_ON_NOENTRY

- Type: integer | Value: `0x0010`

- Meaning: Rez flag causing the object to die/delete if it attempts to enter an unauthorized parcel.

- Member of enum/flag group: RezFlag


## REZ_FLAG_DIE_ON_NO_REZZER

- Type: integer | Value: `0x0100`

- Meaning: Rez flag causing the object to die if the rezzing object or agent is not present.

- Member of enum/flag group: RezFlag


## REZ_FLAG_NO_COLLIDE_FAMILY

- Type: integer | Value: `0x0040`

- Meaning: Rez flag preventing collision events from triggering when colliding with other objects created by the same rezzer.

- Member of enum/flag group: RezFlag


## REZ_FLAG_NO_COLLIDE_OWNER

- Type: integer | Value: `0x0020`

- Meaning: Rez flag preventing collision events from triggering when colliding with its owner.

- Member of enum/flag group: RezFlag


## REZ_FLAG_PHANTOM

- Type: integer | Value: `0x0004`

- Meaning: Rez flag causing the object to be created as phantom.

- Member of enum/flag group: RezFlag


## REZ_FLAG_PHYSICAL

- Type: integer | Value: `0x0002`

- Meaning: Rez flag causing the object to be created with physics enabled.

- Member of enum/flag group: RezFlag


## REZ_FLAG_TEMP

- Type: integer | Value: `0x0001`

- Meaning: Rez flag causing the object to be created as temporary.

- Member of enum/flag group: RezFlag


## REZ_LOCK_AXES

- Type: integer | Value: `11`

- Meaning: Rez parameter [vector locks] used to prevent the physical object from rotating or spinning around specified axes. Setting a coordinate to a non-zero value locks that axis.

- Member of enum/flag group: RezParam


## REZ_OMEGA

- Type: integer | Value: `7`

- Meaning: Rez parameter specifying the initial angular velocity (omega) applied to the object. Accepts [vector axis, integer relative, float spin, float gain]. If relative is TRUE, the axis vector is in local coordinates.

- Member of enum/flag group: RezParam


## REZ_PARAM

- Type: integer | Value: `0`

- Meaning: Rez parameter specifying the integer start parameter passed into the newly rezzed object's on_rez event.

- Member of enum/flag group: RezParam


## REZ_PARAM_STRING

- Type: integer | Value: `13`

- Meaning: Rez parameter specifying an initialization string (up to 1024 bytes) passed to the root prim of the newly rezzed object, readable via llGetStartString.

- Member of enum/flag group: RezParam


## REZ_POS

- Type: integer | Value: `2`

- Meaning: Rez parameter [vector position, integer relative, integer at_root] to specify where to rez the object. Can be in region coordinates or relative to the rezzing object, and centered on either the object's center or the root prim.

- Member of enum/flag group: RezParam


## REZ_ROT

- Type: integer | Value: `3`

- Meaning: Rez parameter specifying the initial rotation to apply to the newly rezzed object. Can be relative to the rezzing object or absolute.

- Member of enum/flag group: RezParam


## REZ_SOUND

- Type: integer | Value: `9`

- Meaning: Rez parameter [string name_or_uuid, float volume, integer loop] to attach and play a sound from inventory or a UUID asset key. If loop is TRUE, it loops continuously.

- Member of enum/flag group: RezParam


## REZ_SOUND_COLLIDE

- Type: integer | Value: `10`

- Meaning: Rez parameter [string name_or_uuid, float volume] specifying a sound (from inventory or a UUID asset key) to play upon collision with another object, the ground, or an avatar.

- Member of enum/flag group: RezParam


## REZ_TORQUE

- Type: integer | Value: `6`

- Member of enum/flag group: RezParam


## REZ_VEL

- Type: integer | Value: `4`

- Meaning: Rez parameter specifying the initial velocity to apply to the object. Accepts [vector velocity, integer local, integer inherit]. If inherit is TRUE, it adds the rezzing object's velocity.

- Member of enum/flag group: RezParam


## ROTATE

- Type: integer | Value: `0x20`

- Meaning: Used with texture animation functions to animate the texture's rotation. Cannot be combined with SCALE.

- Member of enum/flag group: TextureAnimMode


## SCALE

- Type: integer | Value: `0x40`

- Meaning: Used with texture animation functions to animate the texture's scale. Cannot be combined with ROTATE.

- Member of enum/flag group: TextureAnimMode


## SCRIPTED

- Type: integer | Value: `0x8`

- Meaning: Identifies scripted in-world objects. In llDetectedType(), indicates the target has at least one active script. In llSensor()/llSensorRepeat() filters, searches for objects containing active scripts that are currently running.

- Member of enum/flag group: DetectType


## SIM_STAT_ACTIVE_SCRIPT_COUNT

- Type: integer | Value: `12`

- Meaning: Returns the total number of active scripts in the region.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_AGENT_COUNT

- Type: integer | Value: `10`

- Meaning: Returns the total number of agents in the region.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_AGENT_MS

- Type: integer | Value: `7`

- Meaning: Returns the time spent in the 'agent' segment of the simulation frame.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_AGENT_UPDATES

- Type: integer | Value: `2`

- Meaning: Returns the number of agent updates per second.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_AI_MS

- Type: integer | Value: `26`

- Meaning: Returns the time spent on the AI step.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_ASSET_DOWNLOADS

- Type: integer | Value: `15`

- Meaning: Returns the pending asset download count.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_ASSET_UPLOADS

- Type: integer | Value: `16`

- Meaning: Returns the pending asset upload count.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_CHILD_AGENT_COUNT

- Type: integer | Value: `11`

- Meaning: Returns the number of child (neighboring) agents in the region.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_FRAME_MS

- Type: integer | Value: `3`

- Meaning: Returns the total frame time.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_IMAGE_MS

- Type: integer | Value: `8`

- Meaning: Returns the time spent in the 'image' segment of the simulation frame.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_IO_PUMP_MS

- Type: integer | Value: `24`

- Meaning: Returns the pump IO time.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_NET_MS

- Type: integer | Value: `4`

- Meaning: Returns the time spent in the 'network' segment of the simulation frame.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_OTHER_MS

- Type: integer | Value: `5`

- Meaning: Returns the time spent in the main simulation 'other' segment of the frame, which encapsulates task, script, and miscellaneous updates.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PACKETS_IN

- Type: integer | Value: `13`

- Meaning: Returns the average number of incoming packets per second.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PACKETS_OUT

- Type: integer | Value: `14`

- Meaning: Returns the average number of outgoing packets per second.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PCT_CHARS_STEPPED

- Type: integer | Value: `0`

- Meaning: Returns the percentage of pathfinding characters updated (or skipped) each frame, averaged over the last minute. Corresponds to the 'Characters Updated' stat in the viewer's Statistics Bar.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PHYSICS_FPS

- Type: integer | Value: `1`

- Meaning: Returns the physics simulation frames per second (FPS).

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PHYSICS_MS

- Type: integer | Value: `6`

- Meaning: Returns the time spent in the 'physics' segment of the simulation frame.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PHYSICS_OTHER_MS

- Type: integer | Value: `20`

- Meaning: Returns the average update time for the physics 'other' segment.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PHYSICS_SHAPE_MS

- Type: integer | Value: `19`

- Meaning: Returns the average update time for the physics 'shape' segment.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_PHYSICS_STEP_MS

- Type: integer | Value: `18`

- Meaning: Returns the average physics step time.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_SCRIPT_EPS

- Type: integer | Value: `21`

- Meaning: Returns the number of script events per second.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_SCRIPT_MS

- Type: integer | Value: `9`

- Meaning: Returns the time spent in the 'script' segment of the simulation frame.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_SCRIPT_RUN_PCT

- Type: integer | Value: `25`

- Meaning: Returns the percentage of scripts run during the frame.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_SLEEP_MS

- Type: integer | Value: `23`

- Meaning: Returns the time spent sleeping.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_SPARE_MS

- Type: integer | Value: `22`

- Meaning: Returns the spare time left after the frame.

- Member of enum/flag group: SimulatorStat


## SIM_STAT_UNACKED_BYTES

- Type: integer | Value: `17`

- Meaning: Returns the total number of unacknowledged bytes.

- Member of enum/flag group: SimulatorStat


## SIT_FLAG_ALLOW_UNSIT

- Type: integer | Value: `0x0002`

- Meaning: Sit flag indicating that a seated avatar is allowed to manually stand up (unsit) from a sit target. Applies only to agents who were seated via an LSL script like llSitOnLink.

- Member of enum/flag group: SitFlag


## SIT_FLAG_NO_COLLIDE

- Type: integer | Value: `0x0010`

- Meaning: Sit flag that disables the avatar's collision volume/hitbox while seated on this sit target.

- Member of enum/flag group: SitFlag


## SIT_FLAG_NO_DAMAGE

- Type: integer | Value: `0x0020`

- Meaning: Sit flag that prevents damage from being distributed or forwarded to agents sitting on this sit target.

- Member of enum/flag group: SitFlag


## SIT_FLAG_SCRIPTED_ONLY

- Type: integer | Value: `0x0004`

- Meaning: Sit flag that restricts sits to script-controlled actions only, preventing avatars from manually sitting on this prim.

- Member of enum/flag group: SitFlag


## SIT_FLAG_SIT_TARGET

- Type: integer | Value: `0x0001`

- Meaning: Read-only sit flag indicating whether the prim has an active sit target. Set or cleared using llSitTarget, llLinkSitTarget, or PRIM_SIT_TARGET, and read via llGetLinkSitFlags or PRIM_SIT_FLAGS.

- Member of enum/flag group: SitFlag


## SIT_INVALID_AGENT

- Type: integer | Value: `-4`

- Meaning: Sit error code indicating that the specified agent/avatar ID could not be found or is invalid.

- Member of enum/flag group: SitError


## SIT_INVALID_LINK

- Type: integer | Value: `-5`

- Meaning: Sit error code indicating that the link ID does not specify a valid prim, is not found, or resolves to multiple prims.

- Member of enum/flag group: SitError


## SIT_INVALID_OBJECT

- Type: integer | Value: `-7`

- Meaning: Sit error code returned when attempting to force an avatar to sit on an invalid target (such as an attachment) that cannot be sat upon.

- Member of enum/flag group: SitError


## SIT_NOT_EXPERIENCE

- Type: integer | Value: `-1`

- Meaning: Sit error code returned if the script is not running within a valid experience, lacks a valid experience key, or the experience is not permitted at the current location.

- Member of enum/flag group: SitError


## SIT_NO_ACCESS

- Type: integer | Value: `-6`

- Meaning: Sit error code indicating that the avatar lacks access to the parcel where the target prim/linkset is located.

- Member of enum/flag group: SitError


## SIT_NO_EXPERIENCE_PERMISSION

- Type: integer | Value: `-2`

- Meaning: Sit error code indicating that the agent has not granted experience permissions to force sits.

- Member of enum/flag group: SitError


## SIT_NO_SIT_TARGET

- Type: integer | Value: `-3`

- Meaning: Sit error code indicating that no open or available sit target could be found in the linkset.

- Member of enum/flag group: SitError


## SIT_OK

- Type: integer | Value: `1`

- Meaning: Sit error code indicating that the agent was seated successfully.

- Member of enum/flag group: SitError


## SKY_ABSORPTION_CONFIG

- Type: integer | Value: `16`

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_AMBIENT

- Type: integer | Value: `0`

- Meaning: Environmental setting for the ambient color used in the scene.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_BLUE

- Type: integer | Value: `22`

- Meaning: Environmental setting containing the colors used to calculate blue density and blue horizon in the sky.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_CLOUDS

- Type: integer | Value: `2`

- Meaning: Environmental cloud parameters including color, coverage percentage, scale, variance, scroll speed (X/Y), density, detail exponents, and default texture status.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_CLOUD_TEXTURE

- Type: integer | Value: `19`

- Meaning: Environmental setting containing the inventory name or UUID of the texture used for the clouds.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_DENSITY_PROFILE_COUNTS

- Type: integer | Value: `3`

- Meaning: Environmental setting representing counts for each density profile type.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_DOME

- Type: integer | Value: `4`

- Meaning: Environmental setting containing sky dome parameters: offset, radius, and maximum altitude.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_GAMMA

- Type: integer | Value: `5`

- Meaning: Environmental setting for the gamma value applied to the scene (repurposed in viewer 7.0+ as the HDR Scale value in the EEP editor).

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_GLOW

- Type: integer | Value: `6`

- Meaning: Environmental setting for sun and moon glow parameters: size and focus.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_HAZE

- Type: integer | Value: `23`

- Meaning: Environmental setting containing the values used to calculate the light scattering impact of blue density and blue horizon on the scene.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_LIGHT

- Type: integer | Value: `8`

- Meaning: Environmental setting containing lighting parameters: dominant light direction (unit vector), current light color (fade_color in sRGB), and total ambient color (sRGB).

- Member of enum/flag group: EnvironmentParamReadOnly


## SKY_MIE_CONFIG

- Type: integer | Value: `17`

- Meaning: Environmental setting for Mie scattering profile parameters.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_MOON

- Type: integer | Value: `9`

- Meaning: Environmental moon parameters: rotation, scale, brightness, is_default_texture, direction vector, ambient color, and diffuse color.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_MOON_TEXTURE

- Type: integer | Value: `20`

- Meaning: Environmental setting containing the inventory name or UUID of the texture used for the moon.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_PLANET

- Type: integer | Value: `10`

- Meaning: Environmental planet rendering parameters: planet_radius, sky_bottom_radius, and sky_top_radius.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_RAYLEIGH_CONFIG

- Type: integer | Value: `18`

- Meaning: Environmental setting for Rayleigh scattering profile parameters.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_REFLECTION_PROBE_AMBIANCE

- Type: integer | Value: `24`

- Meaning: Environmental setting for the minimum ambiance value of all reflection probes. Note: Supported in the GLTF Materials project, requiring compatible viewers and testing areas.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_REFRACTION

- Type: integer | Value: `11`

- Meaning: Environmental sky refraction parameters for rainbows and optical effects: moisture_level, droplet_radius, and ice_level.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_STAR_BRIGHTNESS

- Type: integer | Value: `13`

- Meaning: Environmental setting for the brightness value applied to stars.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_SUN

- Type: integer | Value: `14`

- Meaning: Environmental sun parameters: rotation, scale, color, is_default_texture, direction vector, ambient color, and diffuse color.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_SUN_TEXTURE

- Type: integer | Value: `21`

- Meaning: Environmental setting containing the inventory name or UUID of the texture used for the sun.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## SKY_TEXTURE_DEFAULTS

- Type: integer | Value: `1`

- Meaning: Environmental check returning 1 if the sky textures are set to their default values, or 0 if they use custom textures.

- Member of enum/flag group: EnvironmentParamReadOnly


## SKY_TRACKS

- Type: integer | Value: `15`

- Meaning: Environmental setting containing the track altitudes used for sky transitions in the region.

- Member of enum/flag group: EnvironmentParamReadOnly


## SMOOTH

- Type: integer | Value: `0x10`

- Meaning: Used with texture animation functions to cause the animation to slide smoothly in the X direction (or transition smoothly in SCALE/ROTATE modes) instead of making instant frame changes.

- Member of enum/flag group: TextureAnimMode


## SOUND_LOOP

- Type: integer | Value: `0x01`

- Meaning: Sound playback option that loops the sound continuously on the prim until stopped.

- Member of enum/flag group: PlaySoundFlag


## SOUND_PLAY

- Type: integer | Value: `0x00`

- Meaning: Sound playback option (default) that plays the sound once, attached to the prim.

- Member of enum/flag group: PlaySoundFlag


## SOUND_SYNC

- Type: integer | Value: `0x04`

- Meaning: Sound playback option that synchronizes playback to the nearest active sound master (see llLoopSoundMaster).

- Member of enum/flag group: PlaySoundFlag


## SOUND_TRIGGER

- Type: integer | Value: `0x02`

- Meaning: Sound playback option that triggers a non-attached sound once at the prim's current location (does not move with the prim). This flag overrides all other sound playback options.

- Member of enum/flag group: PlaySoundFlag


## SQRT2

- Type: float | Value: `1.41421356`

- Meaning: Mathematical constant representing the square root of 2.


## STATUS_BLOCK_GRAB

- Type: integer | Value: `0x40`

- Meaning: Status flag (default FALSE) that blocks click-and-drag grab movements on unlinked prims or the root prim of a linkset. Useful for preventing physical objects from being trivially disturbed.

- Member of enum/flag group: ObjectStatusParam


## STATUS_BLOCK_GRAB_OBJECT

- Type: integer | Value: `0x400`

- Meaning: Status flag that blocks click-and-drag grab movements on all prims across the entire linkset.

- Member of enum/flag group: ObjectStatusParam


## STATUS_BOUNDS_ERROR

- Type: integer | Value: `1002`

- Meaning: Status code indicating that one or more arguments passed to the function had a bounds error.

- Member of enum/flag group: PrimMediaError


## STATUS_CAST_SHADOWS

- Type: integer | Value: `0x200`

- Meaning: Unused legacy status flag intended to configure an object's ability to cast shadows.

- Member of enum/flag group: ObjectStatusParam


## STATUS_DIE_AT_EDGE

- Type: integer | Value: `0x80`

- Meaning: Status flag (default TRUE) that causes the object to be deleted (and not returned) if it goes off-world (useful for bullets or rockets). Overridden by STATUS_RETURN_AT_EDGE.

- Member of enum/flag group: ObjectStatusParam


## STATUS_DIE_AT_NO_ENTRY

- Type: integer | Value: `0x800`

- Meaning: Status flag (default FALSE) that causes the object to be deleted if it attempts to enter an unauthorized or full parcel. No-copy objects ignore this setting and remain in-world.

- Member of enum/flag group: ObjectStatusParam


## STATUS_DIE_ON_NO_REZZER

- Type: integer | Value: `0x1000`

- Meaning: Status flag (default FALSE) that causes the object to be deleted if the rezzing object or agent is not present.

- Member of enum/flag group: ObjectStatusParam


## STATUS_INTERNAL_ERROR

- Type: integer | Value: `1999`

- Meaning: Status code indicating an internal error occurred.

- Member of enum/flag group: PrimMediaError


## STATUS_MALFORMED_PARAMS

- Type: integer | Value: `1000`

- Meaning: Status code indicating the function was called with malformed parameters.

- Member of enum/flag group: PrimMediaError


## STATUS_NOT_FOUND

- Type: integer | Value: `1003`

- Meaning: Status code indicating that the specified object or item was not found.

- Member of enum/flag group: PrimMediaError


## STATUS_NOT_SUPPORTED

- Type: integer | Value: `1004`

- Meaning: Status code indicating the requested feature is not supported.

- Member of enum/flag group: PrimMediaError


## STATUS_OK

- Type: integer | Value: `0`

- Meaning: Status code indicating the function call completed successfully.

- Member of enum/flag group: PrimMediaError


## STATUS_PHANTOM

- Type: integer | Value: `0x10`

- Meaning: Status flag (default FALSE) that makes the entire object phantom/non-colliding when set to TRUE, allowing avatars and objects to pass through it. It is a good idea to use this for most objects that move or rotate, but are non-physical. It is also useful for simulating volumetric lighting.

- Member of enum/flag group: ObjectStatusParam


## STATUS_PHYSICS

- Type: integer | Value: `0x1`

- Meaning: Status flag (default FALSE) that controls whether the object responds to physical interactions, gravity, and forces.

- Member of enum/flag group: ObjectStatusParam


## STATUS_RETURN_AT_EDGE

- Type: integer | Value: `0x100`

- Meaning: Status flag causing the object to be returned to its owner when it goes off-world, overriding STATUS_DIE_AT_EDGE.

- Member of enum/flag group: ObjectStatusParam


## STATUS_ROTATE_X

- Type: integer | Value: `0x2`

- Meaning: Status flag (default TRUE) that allows physical rotation on the object's local X-axis. Setting to FALSE prevents physical rotation around the local X-axis. For example, a sit-and-spin device spins around the Z axis (up) but not around the X or Y axes.

- Member of enum/flag group: ObjectStatusParam


## STATUS_ROTATE_Y

- Type: integer | Value: `0x4`

- Meaning: Status flag (default TRUE) that allows physical rotation on the object's local Y-axis. Setting to FALSE prevents physical rotation around the local Y-axis. For example, a sit-and-spin device spins around the Z axis (up) but not around the X or Y axes.

- Member of enum/flag group: ObjectStatusParam


## STATUS_ROTATE_Z

- Type: integer | Value: `0x8`

- Meaning: Status flag (default TRUE) that allows physical rotation on the object's local Z-axis. Setting to FALSE prevents physical rotation around the local Z-axis.

- Member of enum/flag group: ObjectStatusParam


## STATUS_SANDBOX

- Type: integer | Value: `0x20`

- Meaning: Status flag (default FALSE) that restricts the object's physical movement to within its creation region and a short distance (10 to 20 meters) from its creation point to prevent it from escaping.

- Member of enum/flag group: ObjectStatusParam


## STATUS_TYPE_MISMATCH

- Type: integer | Value: `1001`

- Meaning: Status code indicating that one or more arguments passed to the function had a type mismatch.

- Member of enum/flag group: PrimMediaError


## STATUS_WHITELIST_FAILED

- Type: integer | Value: `2001`

- Meaning: Status code indicating a media domain whitelist check has failed.

- Member of enum/flag group: PrimMediaError


## STRING_TRIM

- Type: integer | Value: `0x03`

- Meaning: Trims whitespace off both the beginning and the end of the string.

- Member of enum/flag group: StringTrimType


## STRING_TRIM_HEAD

- Type: integer | Value: `0x01`

- Meaning: Trims whitespace/spaces off the beginning of the string.

- Member of enum/flag group: StringTrimType


## STRING_TRIM_TAIL

- Type: integer | Value: `0x02`

- Meaning: Trims whitespace/spaces off the end of the string.

- Member of enum/flag group: StringTrimType


## TARGETED_EMAIL_OBJECT_OWNER

- Type: integer | Value: `0x02`

- Meaning: Flag used with llTargetedEmail to send the email message to the owner of the calling object.

- Member of enum/flag group: EmailTarget


## TARGETED_EMAIL_ROOT_CREATOR

- Type: integer | Value: `0x01`

- Meaning: Flag used with llTargetedEmail to send the email message to the creator of the root object.

- Member of enum/flag group: EmailTarget


## TERRAIN_DETAIL_1

- Type: integer | Value: `0`

- Meaning: Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 1.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_DETAIL_2

- Type: integer | Value: `1`

- Meaning: Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 2.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_DETAIL_3

- Type: integer | Value: `2`

- Meaning: Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 3.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_DETAIL_4

- Type: integer | Value: `3`

- Meaning: Terrain parameter used with llSetGroundTexture to set the texture or material (via UUID, inventory name, or default NULL_KEY/empty string) for terrain detail layer 4.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_HEIGHT_RANGE_NE

- Type: integer | Value: `7`

- Meaning: Terrain parameter used with llSetGroundTexture to set the north-east height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_HEIGHT_RANGE_NW

- Type: integer | Value: `6`

- Meaning: Terrain parameter used with llSetGroundTexture to set the north-west height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_HEIGHT_RANGE_SE

- Type: integer | Value: `5`

- Meaning: Terrain parameter used with llSetGroundTexture to set the south-east height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_HEIGHT_RANGE_SW

- Type: integer | Value: `4`

- Meaning: Terrain parameter used with llSetGroundTexture to set the south-west height range for texture blending. Specifies low as the maximum height for texture 1, high as the minimum height for texture 4, and lets textures 2 and 3 mix in between.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_OFFSET_1

- Type: integer | Value: `16`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 1. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_OFFSET_2

- Type: integer | Value: `17`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 2. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_OFFSET_3

- Type: integer | Value: `18`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 3. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_OFFSET_4

- Type: integer | Value: `19`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV offset vector (ignoring the Z component) for drawing terrain layer 4. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_ROTATION_1

- Type: integer | Value: `12`

- Meaning: Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 1, in radians. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_ROTATION_2

- Type: integer | Value: `13`

- Meaning: Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 2, in radians. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_ROTATION_3

- Type: integer | Value: `14`

- Meaning: Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 3, in radians. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_ROTATION_4

- Type: integer | Value: `15`

- Meaning: Terrain parameter used with llSetGroundTexture to set the rotation of the PBR texture for layer 4, in radians. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_SCALE_1

- Type: integer | Value: `8`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 1. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_SCALE_2

- Type: integer | Value: `9`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 2. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_SCALE_3

- Type: integer | Value: `10`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 3. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TERRAIN_PBR_SCALE_4

- Type: integer | Value: `11`

- Meaning: Terrain parameter used with llSetGroundTexture to set the UV scale vector (repeats per meter, ignoring the Z component) for terrain layer 4. Only works for PBR textures.

- Member of enum/flag group: GroundTextureParam


## TEXTURE_BLANK

- Type: string | Value: `5748decc-f629-461c-9a36-a35a221fe21f`

- Meaning: Asset UUID representing the default 'Blank' texture.


## TEXTURE_DEFAULT

- Type: string | Value: `89556747-24cb-43ed-920b-47caed15465f`


## TEXTURE_MEDIA

- Type: string | Value: `8b5fec65-8d8d-9dc5-cda8-8fdf2716e361`

- Meaning: Asset UUID representing the default 'Default Media' texture.


## TEXTURE_PLYWOOD

- Type: string | Value: `89556747-24cb-43ed-920b-47caed15465f`

- Meaning: Asset UUID representing the default 'Plywood' texture.


## TEXTURE_TRANSPARENT

- Type: string | Value: `8dcd4a48-2d37-4909-9f78-f7a9eb4ef903`

- Meaning: Asset UUID representing the '*Default Transparent Texture' in the library (included with viewers).


## TOUCH_INVALID_FACE

- Type: integer | Value: `-1`

- Meaning: Value returned by llDetectedTouchFace when the touch position is not valid.


## TOUCH_INVALID_TEXCOORD

- Type: vector | Value: `<-1.0, -1.0, 0.0>`

- Meaning: Value returned by llDetectedTouchUV and llDetectedTouchST when the touch position is not valid.


## TOUCH_INVALID_VECTOR

- Type: vector | Value: `<0.0, 0.0, 0.0>`

- Meaning: Value returned by llDetectedTouchPos, llDetectedTouchNormal, and llDetectedTouchBinormal when the touch position is not valid.


## TP_ROUTING_BLOCKED

- Type: integer | Value: `0`

- Meaning: Teleport routing setting indicating that direct teleporting is blocked on the parcel.

- Member of enum/flag group: ParcelTeleportRouting


## TP_ROUTING_FREE

- Type: integer | Value: `2`

- Meaning: Teleport routing setting indicating that teleports are unrestricted on the parcel.

- Member of enum/flag group: ParcelTeleportRouting


## TP_ROUTING_LANDINGP

- Type: integer | Value: `1`

- Meaning: Teleport routing setting indicating that teleports are routed to the parcel's landing point (if one has been set).

- Member of enum/flag group: ParcelTeleportRouting


## TRANSFER_BAD_OPTS

- Type: integer | Value: `-1`

- Meaning: Inventory transfer error code indicating that an invalid option was passed in the options list.

- Member of enum/flag group: TransferError


## TRANSFER_BAD_ROOT

- Type: integer | Value: `-5`

- Meaning: Inventory transfer error code indicating that the root path specified in TRANSFER_DEST was invalid or resolved to nothing.

- Member of enum/flag group: TransferError


## TRANSFER_DEST

- Type: integer | Value: `0`

- Meaning: Inventory option specifying the destination root folder to transfer inventory into.

- Member of enum/flag group: GiveAgentInventoryParam


## TRANSFER_FLAGS

- Type: integer | Value: `1`

- Meaning: Inventory parameter specifying flags to control the behavior of inventory transfers.

- Member of enum/flag group: GiveAgentInventoryParam


## TRANSFER_FLAG_COPY

- Type: integer | Value: `0x0004`

- Meaning: Inventory transfer flag that copies the transferred object and places it in the recipient's inventory (implies TRANSFER_FLAG_TAKE).

- Member of enum/flag group: TransferOwnershipFlag


## TRANSFER_FLAG_RESERVED

- Type: integer | Value: `0x0001`

- Meaning: Inventory transfer flag reserved for future expansion; do not use.

- Member of enum/flag group: TransferOwnershipFlag


## TRANSFER_FLAG_TAKE

- Type: integer | Value: `0x0002`

- Meaning: Inventory transfer flag that automatically removes the object from the world and places it in the recipient's inventory once accepted.

- Member of enum/flag group: TransferOwnershipFlag


## TRANSFER_NO_ATTACHMENT

- Type: integer | Value: `-7`

- Meaning: Inventory transfer error code indicating ownership of an attached object cannot be transferred.

- Member of enum/flag group: TransferError


## TRANSFER_NO_ITEMS

- Type: integer | Value: `-4`

- Meaning: Inventory transfer error code indicating that the list was empty or contained only non-transferable items.

- Member of enum/flag group: TransferError


## TRANSFER_NO_PERMS

- Type: integer | Value: `-6`

- Meaning: Inventory transfer error code indicating the object lacks transfer permissions.

- Member of enum/flag group: TransferError


## TRANSFER_NO_TARGET

- Type: integer | Value: `-2`

- Meaning: Inventory transfer error code indicating the receiving agent could not be found in the current region.

- Member of enum/flag group: TransferError


## TRANSFER_OK

- Type: integer | Value: `0`

- Meaning: Status code indicating that the inventory transfer was successful or the transfer offer was successfully made.

- Member of enum/flag group: TransferError


## TRANSFER_THROTTLE

- Type: integer | Value: `-3`

- Meaning: Inventory transfer error code indicating that the transfer rate has exceeded the inventory transfer throttle.

- Member of enum/flag group: TransferError


## TRAVERSAL_TYPE

- Type: integer | Value: `7`

- Meaning: Pathfinding parameter specifying the character's movement traversal type. Expects TRAVERSAL_TYPE_SLOW (default), _FAST, or _NONE.

- Member of enum/flag group: CharacterParam


## TRAVERSAL_TYPE_FAST

- Type: integer | Value: `1`

- Member of enum/flag group: CharacterTraversalType


## TRAVERSAL_TYPE_NONE

- Type: integer | Value: `2`

- Member of enum/flag group: CharacterTraversalType


## TRAVERSAL_TYPE_SLOW

- Type: integer | Value: `0`

- Member of enum/flag group: CharacterTraversalType


## TRUE

- Type: integer | Value: `1`

- Meaning: Mnemonic constant representing a boolean TRUE value (integer 1). Used in conditional structures or variables to improve script readability.


## TWO_PI

- Type: float | Value: `6.28318530`

- Meaning: Mathematical constant pi*2, representing the number of radians in a full circle.


## TYPE_FLOAT

- Type: integer | Value: `2`

- Meaning: Variable type constant indicating the list entry or value is a float.

- Member of enum/flag group: ListEntryType


## TYPE_INTEGER

- Type: integer | Value: `1`

- Meaning: Variable type constant indicating the list entry or value is an integer.

- Member of enum/flag group: ListEntryType


## TYPE_INVALID

- Type: integer | Value: `0`

- Meaning: Variable type constant indicating the list entry or value is invalid.

- Member of enum/flag group: ListEntryType


## TYPE_KEY

- Type: integer | Value: `4`

- Meaning: Variable type constant indicating the list entry or value is a key.

- Member of enum/flag group: ListEntryType


## TYPE_ROTATION

- Type: integer | Value: `6`

- Meaning: Variable type constant indicating the list entry or value is a rotation.

- Member of enum/flag group: ListEntryType


## TYPE_STRING

- Type: integer | Value: `3`

- Meaning: Variable type constant indicating the list entry or value is a string.

- Member of enum/flag group: ListEntryType


## TYPE_VECTOR

- Type: integer | Value: `5`

- Meaning: Variable type constant indicating the list entry or value is a vector.

- Member of enum/flag group: ListEntryType


## URL_REQUEST_DENIED

- Type: string | Value: `URL_REQUEST_DENIED`


## URL_REQUEST_GRANTED

- Type: string | Value: `URL_REQUEST_GRANTED`


## VEHICLE_ANGULAR_DEFLECTION_EFFICIENCY

- Type: integer | Value: `32`

- Meaning: Vehicle float parameter (range 0.0 to 1.0) acting as a scalar to modulate the strength of angular deflection, reorienting the vehicle's preferred axis toward its true velocity.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_ANGULAR_DEFLECTION_TIMESCALE

- Type: integer | Value: `33`

- Meaning: Vehicle float parameter specifying the exponential timescale for the vehicle to achieve full angular deflection, reorienting its preferred axis of motion to match its true velocity.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_ANGULAR_FRICTION_TIMESCALE

- Type: integer | Value: `17`

- Meaning: Vehicle vector parameter specifying the timescales (range [0.07, infinity) seconds per axis) for the exponential decay of angular velocity about the vehicle's preferred axes (at, left, up).

- Member of enum/flag group: VehicleVectorParam


## VEHICLE_ANGULAR_MOTOR_DECAY_TIMESCALE

- Type: integer | Value: `35`

- Meaning: Vehicle float parameter specifying the exponential timescale (in seconds) for the angular motor's magnitude and effectiveness to decay toward zero.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_ANGULAR_MOTOR_DIRECTION

- Type: integer | Value: `19`

- Meaning: Vehicle vector parameter specifying the direction and magnitude of the angular velocity (in radians per second) that the vehicle's angular motor attempts to achieve.

- Member of enum/flag group: VehicleVectorParam


## VEHICLE_ANGULAR_MOTOR_TIMESCALE

- Type: integer | Value: `34`

- Meaning: Vehicle float parameter specifying the exponential timescale for the vehicle's angular motor to achieve full power and velocity.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_BANKING_EFFICIENCY

- Type: integer | Value: `38`

- Meaning: Vehicle float parameter (range -1.0 to 1.0) controlling banking efficiency, where negative values lean out of turns and positive values lean into turns. This parameter makes banking affect steering; use angular motors to bank. 0.0 means no banking.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_BANKING_MIX

- Type: integer | Value: `39`

- Meaning: Vehicle float parameter (range 0.0 (static) to 1.0) (dynamic) controlling the mix between static banking (scales only with roll angle) and dynamic banking (additionally scales with linear speed).

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_BANKING_TIMESCALE

- Type: integer | Value: `40`

- Meaning: Vehicle float parameter specifying the exponential timescale for the banking behavior to take full effect. This is another way to scale the strength of the banking effect, however it affects the term that is proportional to the difference between what the banking behavior is trying to do, and what the vehicle is actually doing.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_BUOYANCY

- Type: integer | Value: `27`

- Meaning: Vehicle float parameter (range -1.0 to 1.0) defining buoyancy, where -1.0 represents double gravity and 1.0 represents full anti-gravity.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_FLAG_BLOCK_INTERFERENCE

- Type: integer | Value: `0x400`

- Meaning: Vehicle flag that prevents attachments worn by passengers from pushing the vehicle via llPushObject or other scripting functions.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_CAMERA_DECOUPLED

- Type: integer | Value: `0x200`

- Meaning: Vehicle flag used with mouselook steering/banking. When set, the passenger's mouselook camera rotates independently of the vehicle's orientation.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT

- Type: integer | Value: `0x10`

- Meaning: Vehicle flag that forces the hover behavior to maintain a global height rather than hovering relative to the ground or water.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_HOVER_TERRAIN_ONLY

- Type: integer | Value: `0x8`

- Meaning: Vehicle flag that forces the hover behavior to ignore water height and hover exclusively relative to the terrain/land.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_HOVER_UP_ONLY

- Type: integer | Value: `0x20`

- Meaning: Vehicle flag preventing hover from pushing downward, allowing hovering vehicles to jump or fly above their designated hover height.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_HOVER_WATER_ONLY

- Type: integer | Value: `0x4`

- Meaning: Vehicle flag that forces the hover behavior to ignore terrain height and hover exclusively relative to water.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_LIMIT_MOTOR_UP

- Type: integer | Value: `0x40`

- Meaning: Vehicle flag that prevents ground vehicles from motoring upward into the sky. When combined with banking, banking strength decays when the vehicle is airborne (no longer colliding) to prevent steering mid-jump.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_LIMIT_ROLL_ONLY

- Type: integer | Value: `0x2`

- Meaning: Vehicle flag for vehicles with a vertical attractor that need to climb or dive, allowing airplanes to use the banking feature.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_MOUSELOOK_BANK

- Type: integer | Value: `0x100`

- Meaning: Vehicle flag that enables mouselook control, remapping left-right camera motions (yaw) to rotations about the vehicle's local X-axis.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_MOUSELOOK_STEER

- Type: integer | Value: `0x80`

- Meaning: Vehicle flag that enables steering via mouse, directing the angular motor to align the vehicle's local X-axis with the direction of the client-side camera.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_NO_DEFLECTION_UP

- Type: integer | Value: `0x1`

- Meaning: Vehicle flag that prevents linear deflection parallel to the world Z-axis, preventing ground vehicles (such as bumper cars) from climbing into the sky.

- Member of enum/flag group: VehicleFlag


## VEHICLE_FLAG_NO_FLY_UP

- Type: integer | Value: `0x1`

- Meaning: Obsolete legacy name for VEHICLE_FLAG_NO_DEFLECTION_UP.

- Member of enum/flag group: VehicleFlag


## VEHICLE_HOVER_EFFICIENCY

- Type: integer | Value: `25`

- Meaning: Vehicle float parameter (range 0.0 to 1.0) controlling hover damping, where 0.0 is bouncy and 1.0 is critically damped.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_HOVER_HEIGHT

- Type: integer | Value: `24`

- Meaning: Vehicle float parameter specifying the height at which the vehicle attempts to hover. Set to 0.0 to disable hover.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_HOVER_TIMESCALE

- Type: integer | Value: `26`

- Meaning: Vehicle float parameter specifying the timescale (period of time in seconds) for the vehicle to achieve its hover height.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_LINEAR_DEFLECTION_EFFICIENCY

- Type: integer | Value: `28`

- Meaning: Vehicle float parameter (range 0.0 to 1.0) modulating the efficiency and strength of linear deflection. That is, its a simple scalar for modulating the strength of linear deflection.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_LINEAR_DEFLECTION_TIMESCALE

- Type: integer | Value: `29`

- Meaning: Vehicle float parameter specifying the exponential timescale for the vehicle to redirect its linear velocity along its preferred X-axis. It is another way to specify how much time it takes for the vehicle's linear velocity to be redirected to its preferred axis of motion.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_LINEAR_FRICTION_TIMESCALE

- Type: integer | Value: `16`

- Meaning: Vehicle vector parameter specifying the timescales (range [0.07, infinity) seconds per axis) for the exponential decay of linear velocity along the vehicle's preferred axes (at, left, up).

- Member of enum/flag group: VehicleVectorParam


## VEHICLE_LINEAR_MOTOR_DECAY_TIMESCALE

- Type: integer | Value: `31`

- Meaning: Vehicle float parameter specifying the exponential timescale (in seconds) for the linear motor's magnitude and effectiveness to decay toward zero.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_LINEAR_MOTOR_DIRECTION

- Type: integer | Value: `18`

- Meaning: Vehicle vector parameter specifying the direction and magnitude of the linear velocity (range [0, 30] m/s) that the vehicle's linear motor attempts to achieve.

- Member of enum/flag group: VehicleVectorParam


## VEHICLE_LINEAR_MOTOR_OFFSET

- Type: integer | Value: `20`

- Meaning: Vehicle vector parameter specifying the offset from the vehicle's center of mass where the linear motor force is applied.

- Member of enum/flag group: VehicleVectorParam


## VEHICLE_LINEAR_MOTOR_TIMESCALE

- Type: integer | Value: `30`

- Meaning: Vehicle float parameter specifying the exponential timescale for the vehicle to reach its full linear motor velocity.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_REFERENCE_FRAME

- Type: integer | Value: `44`

- Meaning: Vehicle rotation parameter setting the orientation of the vehicle's preferred axes of motion (at, left, up) relative to its local geometric frame (x, y, z).

- Member of enum/flag group: VehicleRotationParam


## VEHICLE_TYPE_AIRPLANE

- Type: integer | Value: `4`

- Meaning: Vehicle type constant for aircraft that use linear deflection for lift, banking to turn, and no hover.

- Member of enum/flag group: VehicleType


## VEHICLE_TYPE_BALLOON

- Type: integer | Value: `5`

- Meaning: Vehicle type constant for balloons that use hover and friction but no deflection.

- Member of enum/flag group: VehicleType


## VEHICLE_TYPE_BOAT

- Type: integer | Value: `3`

- Meaning: Vehicle type constant for boats that hover over water with high friction and minor angular deflection.

- Member of enum/flag group: VehicleType


## VEHICLE_TYPE_CAR

- Type: integer | Value: `2`

- Meaning: Vehicle type constant for land vehicles that bounce along the ground and rely on external controls or timer events to drive their motors.

- Member of enum/flag group: VehicleType


## VEHICLE_TYPE_NONE

- Type: integer | Value: `0`

- Meaning: Constant used to disable and turn off vehicle physics support on the object.

- Member of enum/flag group: VehicleType


## VEHICLE_TYPE_SLED

- Type: integer | Value: `1`

- Meaning: Vehicle type constant for sliding vehicles that bump along the ground and prefer to move along their local X-axis.

- Member of enum/flag group: VehicleType


## VEHICLE_VERTICAL_ATTRACTION_EFFICIENCY

- Type: integer | Value: `36`

- Meaning: Vehicle float parameter (range 0.0 to 1.0) controlling vertical attraction stability (0.0 is wobbly/bouncy, 1.0 is critically damped/firm) to keep the vehicle upright.

- Member of enum/flag group: VehicleFloatParam


## VEHICLE_VERTICAL_ATTRACTION_TIMESCALE

- Type: integer | Value: `37`

- Meaning: Vehicle float parameter specifying the exponential timescale (in seconds) for the vehicle to rotate and align its local Z-axis (up) with the world Z-axis (vertical).

- Member of enum/flag group: VehicleFloatParam


## VERTICAL

- Type: integer | Value: `0`

- Meaning: Constant indicating that the collision capsule orientation for a pathfinding character is vertical.

- Member of enum/flag group: CharacterOrientation


## WANDER_PAUSE_AT_WAYPOINTS

- Type: integer | Value: `0`

- Meaning: Option parameter for llWanderWithin specifying whether the character should pause briefly after reaching each wander waypoint.

- Member of enum/flag group: CharacterWanderWithinParam


## WATER_BLUR_MULTIPLIER

- Type: integer | Value: `100`

- Meaning: Environmental setting specifying the multiplier applied to blur the scene when underwater.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## WATER_FOG

- Type: integer | Value: `101`

- Meaning: Environmental underwater fog parameters: color, density exponent, and modulation.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## WATER_FRESNEL

- Type: integer | Value: `102`

- Meaning: Environmental water surface Fresnel scattering parameters: offset and scale.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## WATER_NORMAL_SCALE

- Type: integer | Value: `104`

- Meaning: Environmental setting specifying the scaling vector applied to the water normal map.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## WATER_NORMAL_TEXTURE

- Type: integer | Value: `107`

- Meaning: Environmental setting containing the inventory name or UUID of the normal map texture used for water waves.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## WATER_REFRACTION

- Type: integer | Value: `105`

- Meaning: Environmental water surface refraction scale factors: scale_above and scale_below.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## WATER_TEXTURE_DEFAULTS

- Type: integer | Value: `103`

- Meaning: Environmental check returning 1 if default water wave maps are used, or 0 if a custom texture is set.

- Member of enum/flag group: EnvironmentParamReadOnly


## WATER_WAVE_DIRECTION

- Type: integer | Value: `106`

- Meaning: Environmental wave direction vectors (X is east/west, Y is north/south) specifying speeds and directions for both large and small waves.

- Member of enum/flag group: EnvironmentParamReadOnly, EnvironmentParam


## XP_ERROR_EXPERIENCES_DISABLED

- Type: integer | Value: `2`

- Meaning: Region currently has experiences disabled.

- Member of enum/flag group: ExperienceError


## XP_ERROR_EXPERIENCE_DISABLED

- Type: integer | Value: `8`

- Meaning: Experience owner has temporarily disabled the experience.

- Member of enum/flag group: ExperienceError


## XP_ERROR_EXPERIENCE_SUSPENDED

- Type: integer | Value: `9`

- Meaning: Experience has been suspended by Linden Lab customer support.

- Member of enum/flag group: ExperienceError


## XP_ERROR_INVALID_EXPERIENCE

- Type: integer | Value: `7`

- Meaning: Script is associated with an experience that no longer exists.

- Member of enum/flag group: ExperienceError


## XP_ERROR_INVALID_PARAMETERS

- Type: integer | Value: `3`

- Meaning: One of the string arguments was too big to fit in the key-value store.

- Member of enum/flag group: ExperienceError


## XP_ERROR_KEY_NOT_FOUND

- Type: integer | Value: `14`

- Meaning: Requested key does not exist.

- Member of enum/flag group: ExperienceError


## XP_ERROR_MATURITY_EXCEEDED

- Type: integer | Value: `16`

- Meaning: Content rating of the experience exceeds that of the region.

- Member of enum/flag group: ExperienceError


## XP_ERROR_NONE

- Type: integer | Value: `0`

- Meaning: No error was detected.

- Member of enum/flag group: ExperienceError


## XP_ERROR_NOT_FOUND

- Type: integer | Value: `6`

- Meaning: Sim was unable to verify the validity of the experience. Retrying after a short wait is advised.

- Member of enum/flag group: ExperienceError


## XP_ERROR_NOT_PERMITTED

- Type: integer | Value: `4`

- Meaning: This experience is not allowed to run by the requested agent, or experience permissions were denied by the user.

- Member of enum/flag group: ExperienceError


## XP_ERROR_NOT_PERMITTED_LAND

- Type: integer | Value: `17`

- Meaning: Experience is blocked or not enabled for this land, or is not allowed to run in the current region.

- Member of enum/flag group: ExperienceError


## XP_ERROR_NO_EXPERIENCE

- Type: integer | Value: `5`

- Meaning: This script is not associated with an experience.

- Member of enum/flag group: ExperienceError


## XP_ERROR_QUOTA_EXCEEDED

- Type: integer | Value: `11`

- Meaning: An attempt to write data to the key-value store failed due to the data quota being met.

- Member of enum/flag group: ExperienceError


## XP_ERROR_REQUEST_PERM_TIMEOUT

- Type: integer | Value: `18`

- Meaning: Request for experience permissions was ignored and the request timed out without modification.

- Member of enum/flag group: ExperienceError


## XP_ERROR_RETRY_UPDATE

- Type: integer | Value: `15`

- Meaning: A checked update failed due to an out of date request.

- Member of enum/flag group: ExperienceError


## XP_ERROR_STORAGE_EXCEPTION

- Type: integer | Value: `13`

- Meaning: Unable to communicate with the key-value store, or attempted to create a key that already exists.

- Member of enum/flag group: ExperienceError


## XP_ERROR_STORE_DISABLED

- Type: integer | Value: `12`

- Meaning: Key-value store is currently disabled on this region.

- Member of enum/flag group: ExperienceError


## XP_ERROR_THROTTLED

- Type: integer | Value: `1`

- Meaning: Call failed due to too many recent calls.

- Member of enum/flag group: ExperienceError


## XP_ERROR_UNKNOWN_ERROR

- Type: integer | Value: `10`

- Meaning: An unknown error occurred that is not covered by any of the other predetermined error states.

- Member of enum/flag group: ExperienceError


## ZERO_ROTATION

- Type: rotation | Value: `<0.0, 0.0, 0.0, 1.0>`

- Meaning: A rotation constant representing an identity rotation (causes no change). This is the default value for rotation variables.


## ZERO_VECTOR

- Type: vector | Value: `<0.0, 0.0, 0.0>`

- Meaning: A vector constant representing <0.0, 0.0, 0.0>. This is the default value for vector variables.
