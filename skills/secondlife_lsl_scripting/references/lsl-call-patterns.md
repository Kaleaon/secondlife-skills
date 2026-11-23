# LSL Function Call Patterns (generated from secondlife/lsl-definitions)

For every LSL function: the canonical signature, a minimal call pattern built from its real argument names and types, its return handling, and its cost fields. Patterns are illustrative skeletons, combine them with the full examples in examples-lsl.md and the purpose text in lsl-functions.md.


## llAbs

```lsl
// Returns the absolute (positive) integer value of val.

integer result = llAbs(val);

```

- Arguments: `val` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llAcos

```lsl
// Returns the arccosine of val in radians.

float result = llAcos(val);

```

- Arguments: `val` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_trig


## llAddToLandBanList

```lsl
// Adds the avatar to the parcel ban list for the specified number of hours. A value of 0 hours adds the avatar indefinitely. Banned users teleporting to the parcel are redirected to a neighboring parcel; the minimum accepted duration is 0.01 hours (approximately 36 seconds).

llAddToLandBanList(avatar, hours);

```

- Arguments: `avatar` (key), `hours` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: land_moderation, parcel

- Delay: budget 0.1 s of script stall per call in event handlers.


## llAddToLandPassList

```lsl
// Adds the avatar to the land pass list for the specified number of hours (or indefinitely if hours is 0).

llAddToLandPassList(avatar, hours);

```

- Arguments: `avatar` (key), `hours` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: land_moderation, parcel

- Delay: budget 0.1 s of script stall per call in event handlers.


## llAdjustDamage

```lsl
// Modifies the amount of damage applied by the current on_damage event after it completes processing, specified by the damage event index number.

llAdjustDamage(number, new_damage);

```

- Arguments: `number` (integer), `new_damage` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: combat, detected


## llAdjustSoundVolume

```lsl
// Adjusts the volume of the currently playing attached sound (has no effect on sounds started with llTriggerSound).

llAdjustSoundVolume(volume);

```

- Arguments: `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: sound

- Delay: budget 0.1 s of script stall per call in event handlers.


## llAgentInExperience

```lsl
// Returns TRUE if the specified agent is in the experience and the experience can run in the current region/location; returns FALSE otherwise.

integer result = llAgentInExperience(agent);

```

- Arguments: `agent` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, experience


## llAllowInventoryDrop

```lsl
// If add is TRUE, allows users without object modify permissions to drop inventory items into the prim. If FALSE, restricts inventory dropping to users with modify permissions.

llAllowInventoryDrop(add);

```

- Arguments: `add` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llAngleBetween

```lsl
// Returns the angle, in radians, between rotations start_rot and and end_rot.

float result = llAngleBetween(start_rot, end_rot);

```

- Arguments: `start_rot` (rotation), `end_rot` (rotation)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion


## llApplyImpulse

```lsl
// Applies a linear impulse (momentum) to a physical object. If local is TRUE, the impulse is applied in local coordinates; otherwise, it is applied in global region coordinates.

llApplyImpulse(momentum, is_local);

```

- Arguments: `momentum` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llApplyRotationalImpulse

```lsl
// Applies a rotational impulse (force) to a physical object. If local is TRUE, the rotational impulse is applied in local coordinates; otherwise, it is applied in global region coordinates.

llApplyRotationalImpulse(force, is_local);

```

- Arguments: `force` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llAsin

```lsl
// Returns the arcsine of val in radians.

float result = llAsin(val);

```

- Arguments: `val` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_trig


## llAtan2

```lsl
// Returns the arctangent of y/x in radians, using the signs to determine the quadrant. Note the argument order: Y is the first parameter, X is the second parameter.

float result = llAtan2(y, x);

```

- Arguments: `y` (float), `x` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_trig


## llAttachToAvatar

```lsl
// Attaches the object to the avatar who has granted the PERMISSION_ATTACH permission. Takes the object into the user's inventory and attaches it at attach_point.

llAttachToAvatar(attach_point);

```

- Arguments: `attach_point` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: attachments, avatar


## llAttachToAvatarTemp

```lsl
// Attaches the object temporarily to an avatar who has granted the PERMISSION_ATTACH permission. No permanent inventory is created, and the object disappears on detach or disconnect. Can be used on non-owners (changing ownership to the wearer).

llAttachToAvatarTemp(attach_point);

```

- Arguments: `attach_point` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: attachments, avatar


## llAvatarOnLinkSitTarget

```lsl
// Returns the UUID of the avatar seated on the specified link's sit target, or NULL_KEY if no avatar is sitting there.

key result = llAvatarOnLinkSitTarget(link);

```

- Arguments: `link` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, linkset, sit


## llAvatarOnSitTarget

```lsl
// Returns the UUID of the avatar seated on the prim's sit target (defined via llSitTarget), or NULL_KEY if no avatar is sitting there or the prim lacks a sit target.

key result = llAvatarOnSitTarget();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, prim, sit


## llAxes2Rot

```lsl
// Returns the rotation defined by the coordinate axes fwd, left, and up.

rotation result = llAxes2Rot(fwd, left, up);

```

- Arguments: `fwd` (vector), `left` (vector), `up` (vector)

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion


## llAxisAngle2Rot

```lsl
// Returns the rotation that rotates angle radians around the axis vector.

rotation result = llAxisAngle2Rot(axis, angle);

```

- Arguments: `axis` (vector), `angle` (float)

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion


## llBase64ToInteger

```lsl
// Returns an integer representing the Base64-decoded big-endian value of str. Returns zero if str is longer than 8 characters; the return value is unpredictable if str contains fewer than 6 characters.

integer result = llBase64ToInteger(str);

```

- Arguments: `str` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llBase64ToString

```lsl
// Decodes the Base64-encoded string str into a conventional string, interpreting the bytes as a UTF-8 character sequence. Unprintable characters are converted to question marks.

string result = llBase64ToString(str);

```

- Arguments: `str` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llBreakAllLinks

```lsl
// Delinks all prims in the linkset. Requires the PERMISSION_CHANGE_LINKS runtime permission, which must be requested and granted by the owner.

llBreakAllLinks();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset


## llBreakLink

```lsl
// Delinks the prim specified by the link number link. Requires the PERMISSION_CHANGE_LINKS runtime permission.

llBreakLink(link);

```

- Arguments: `link` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset


## llCSV2List

```lsl
// Parses the comma-separated string src and returns it as a list.

list result = llCSV2List(src);

```

- Arguments: `src` (string)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llCastRay

```lsl
// Casts a ray into the physics world from start to end and reports collision data for intersections with objects based on options. Returns a list of strided values [UUID_1, {link_number_1}, hit_position_1, {hit_normal_1}, ..., status_code]. A negative status_code indicates an error; otherwise, it represents the number of hits.

list result = llCastRay(start_pos, end_pos, options);

```

- Arguments: `start_pos` (vector), `end_pos` (vector), `options` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, sensor


## llCeil

```lsl
// Returns val rounded toward positive infinity. In other words, returns the smallest integer greater than or equal to val.

integer result = llCeil(val);

```

- Arguments: `val` (float)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llChar

```lsl
// Constructs and returns a single-character string from the given Unicode codepoint ordinal.

string result = llChar(val);

```

- Arguments: `val` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llClearCameraParams

```lsl
// Resets all camera parameters to default values and turns off scripted camera control. Requires the PERMISSION_CONTROL_CAMERA runtime permission (automatically granted for attached or sat-on objects).

llClearCameraParams();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llClearExperience

```lsl
// 

llClearExperience(agentid, experienceid);

```

- Arguments: `agentid` (key), `experienceid` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: experience


## llClearExperiencePermissions

```lsl
// 

llClearExperiencePermissions(agentid);

```

- Arguments: `agentid` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: experience


## llClearLinkMedia

```lsl
// Deletes the media and clears all parameters from the given face on the linked prim. Returns an integer STATUS_* flag detailing the success or failure of the operation.

integer result = llClearLinkMedia(link, face);

```

- Arguments: `link` (integer), `face` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, media, prim_media


## llClearPrimMedia

```lsl
// Deletes the media and clears all parameters from the specified face. Returns an integer STATUS_* flag detailing the success or failure of the operation.

integer result = llClearPrimMedia(face);

```

- Arguments: `face` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 1.0 s | Categories: media, prim, prim_media

- Delay: budget 1.0 s of script stall per call in event handlers.


## llCloseRemoteDataChannel

```lsl
// Deprecated. Closes the specified XML-RPC channel.

llCloseRemoteDataChannel(channel);

```

- Arguments: `channel` (key)

- Returns: void | Energy: 10.0 | Sleep: 1.0 s | Categories: script_communication

- Delay: budget 1.0 s of script stall per call in event handlers.


## llCloud

```lsl
// Returns a float representing the cloud density at the prim's position offset by the vector offset.

float result = llCloud(offset);

```

- Arguments: `offset` (vector)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llCollisionFilter

```lsl
// Sets the collision filter, either exclusively or inclusively. If accept is TRUE, only collisions matching name and id are processed; if FALSE, matches are excluded. Pass an empty string or NULL_KEY to name or id to skip filtering on that parameter.

llCollisionFilter(name, id, accept);

```

- Arguments: `name` (string), `id` (key), `accept` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, sensor


## llCollisionSound

```lsl
// Suppresses default collision sounds and replaces default impact sounds with impact_sound at the volume level specified by impact_volume. Supply an empty string to only suppress collision sounds.

llCollisionSound(impact_sound, impact_volume);

```

- Arguments: `impact_sound` (string), `impact_volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, sound


## llCollisionSprite

```lsl
// Suppresses default collision sprites and replaces them with impact_sprite (which must be in the prim's inventory). Supply an empty string to only suppress collision sprites.

llCollisionSprite(impact_sprite);

```

- Arguments: `impact_sprite` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: effects, sound


## llComputeHash

```lsl
// Returns a hex-encoded hash digest string of message using the specified cryptographic algorithm.

string result = llComputeHash(message, algorithm);

```

- Arguments: `message` (string), `algorithm` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llCos

```lsl
// Returns the cosine of theta. Theta is in radians.

float result = llCos(theta);

```

- Arguments: `theta` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_trig


## llCreateCharacter

```lsl
// Converts the linkset containing the script into a pathfinding character entity (required to use pathfinding functions) using the specified options.

llCreateCharacter(options);

```

- Arguments: `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llCreateKeyValue

```lsl
// Starts an asynchronous transaction to create a key-value pair (k and v) associated with the script's experience. Returns a key query handle for the dataserver event. Fails with XP_ERROR_STORAGE_EXCEPTION if the key already exists.

key result = llCreateKeyValue(k, v);

```

- Arguments: `k` (string), `v` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, experience, experience_data


## llCreateLink

```lsl
// Attempts to link the object containing the script with target. Requires the PERMISSION_CHANGE_LINKS runtime permission.

llCreateLink(target, parent);

```

- Arguments: `target` (key), `parent` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: linkset

- Delay: budget 0.1 s of script stall per call in event handlers.


## llDamage

```lsl
// Generates a damage event delivering the specified amount of damage and damage_type to the targeted avatar or task in the same region.

llDamage(target, damage, damage_type);

```

- Arguments: `target` (key), `damage` (float), `damage_type` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: combat


## llDataSizeKeyValue

```lsl
// Starts an asynchronous transaction to request the used and total data storage allocated for the experience. Returns a key query handle for the dataserver event.

key result = llDataSizeKeyValue();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, experience, experience_data


## llDeleteCharacter

```lsl
// Converts the linkset back to a standard physical object, removing all pathfinding properties.

llDeleteCharacter();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llDeleteKeyValue

```lsl
// Starts an asynchronous transaction to delete the key-value pair associated with key k in the experience. Returns a key query handle for the dataserver event.

key result = llDeleteKeyValue(k);

```

- Arguments: `k` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, experience, experience_data


## llDeleteSubList

```lsl
// Returns a copy of the list src with the slice from start_index to end_index (inclusive) removed. Negative indices count backward from the end of the list. If start_index is greater than end_index, the deletion excludes the specified range.

list result = llDeleteSubList(src, start_index, end_index);

```

- Arguments: `src` (list), `start_index` (integer), `end_index` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llDeleteSubString

```lsl
// Returns a copy of the string src with the characters from start_index to end_index (inclusive) removed. Negative indices count backward from the end of the string. If start_index is greater than end_index, the deletion excludes the specified range.

string result = llDeleteSubString(src, start_index, end_index);

```

- Arguments: `src` (string), `start_index` (integer), `end_index` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llDerezObject

```lsl
// Derezzes (deletes or returns) a targeted object in the region previously rezzed by a script in this linkset, returning TRUE on success or FALSE on failure.

integer result = llDerezObject(id, flags);

```

- Arguments: `id` (key), `flags` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory, rez


## llDetachFromAvatar

```lsl
// Detaches the object containing the script from the avatar. Requires the PERMISSION_ATTACH runtime permission (automatically granted to attached objects). Note that the detached object is completely removed from the region and not dropped on the ground.

llDetachFromAvatar();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: attachments, avatar


## llDetectedDamage

```lsl
// Returns a list containing pending damage information for the event specified by number, including the current damage, the damage type, and the original damage delivered.

list result = llDetectedDamage(number);

```

- Arguments: `number` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: combat, detected


## llDetectedGrab

```lsl
// Returns a vector representing the grab offset of the user touching the object. Only works in touch events and returns <0.0, 0.0, 0.0> if number is not a valid index.

vector result = llDetectedGrab(number);

```

- Arguments: `number` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, touch


## llDetectedGroup

```lsl
// Returns TRUE if the detected object or avatar specified by number has the same active group as the prim containing the script. Returns FALSE if the group is not active or if they are not in the group.

integer result = llDetectedGroup(number);

```

- Arguments: `number` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDetectedKey

```lsl
// Returns the key (UUID) of the detected object or avatar specified by number, or NULL_KEY if number is not a valid index.

key result = llDetectedKey(number);

```

- Arguments: `number` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, uuid


## llDetectedLinkNumber

```lsl
// Returns the link number (integer) of the triggered event (touches and collisions only) specified by number. Returns 0 for non-linked objects, 1 for the root prim, and 2+ for child prims. Returns 0 if not supported by the event.

integer result = llDetectedLinkNumber(number);

```

- Arguments: `number` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDetectedName

```lsl
// Returns a string representing the name of the detected object or avatar specified by item. Returns an empty string if item is not a valid index.

string result = llDetectedName(item);

```

- Arguments: `item` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDetectedOwner

```lsl
// Returns the key (UUID) of the owner of the detected object specified by number. Returns an invalid key if number is not a valid index.

key result = llDetectedOwner(number);

```

- Arguments: `number` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, detected


## llDetectedPos

```lsl
// Returns the vector position (in region coordinates) of the detected object or avatar specified by number, or <0.0, 0.0, 0.0> if number is not a valid index.

vector result = llDetectedPos(number);

```

- Arguments: `number` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDetectedRezzer

```lsl
// Returns the key (UUID) of the object or avatar that rezzed the detected object specified by number.

key result = llDetectedRezzer(number);

```

- Arguments: `number` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDetectedRot

```lsl
// Returns the rotation of the detected object or avatar specified by number, or <0.0, 0.0, 0.0, 1.0> if number is not a valid offset index.

rotation result = llDetectedRot(number);

```

- Arguments: `number` (integer)

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDetectedTouchBinormal

```lsl
// Returns the surface binormal vector (tangent to the surface, pointing along the positive T (V) direction of tangent space) at the touched location specified by index. Can be used with llDetectedTouchNormal to determine the tangent space.

vector result = llDetectedTouchBinormal(index);

```

- Arguments: `index` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, touch


## llDetectedTouchFace

```lsl
// Returns the integer index of the face clicked by the avatar in the touch event specified by index.

integer result = llDetectedTouchFace(index);

```

- Arguments: `index` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, touch


## llDetectedTouchNormal

```lsl
// Returns the surface normal vector (perpendicular to the surface) at the touched location specified by index. Can be used with llDetectedTouchBinormal to determine the tangent space.

vector result = llDetectedTouchNormal(index);

```

- Arguments: `index` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, touch


## llDetectedTouchPos

```lsl
// Returns the vector position where the object was touched (specified by index) in region coordinates, or in screen-space coordinates if the object is attached as a HUD.

vector result = llDetectedTouchPos(index);

```

- Arguments: `index` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, touch


## llDetectedTouchST

```lsl
// Returns the surface coordinates (<s, t, 0.0>) where the prim was touched, specified by index. X and Y contain the horizontal (s) and vertical (t) face coordinates, typically in the interval [0.0, 1.0]. Returns TOUCH_INVALID_TEXCOORD if coordinates cannot be determined.

vector result = llDetectedTouchST(index);

```

- Arguments: `index` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, touch


## llDetectedTouchUV

```lsl
// Returns the texture coordinates (<u, v, 0.0>) where the prim was touched, specified by index. X and Y contain the horizontal (u) and vertical (v) texture coordinates, typically in the interval [0.0, 1.0] (affected by repeats and rotation). Returns TOUCH_INVALID_TEXCOORD if coordinates cannot be determined.

vector result = llDetectedTouchUV(index);

```

- Arguments: `index` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected, touch


## llDetectedType

```lsl
// Returns an integer bitfield representing the types (AGENT, ACTIVE, PASSIVE, or SCRIPTED) of the detected object or avatar specified by number. Returns 0 if number is not a valid index.

integer result = llDetectedType(number);

```

- Arguments: `number` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDetectedVel

```lsl
// Returns the vector velocity of the detected object or avatar specified by number, or <0.0, 0.0, 0.0> if number is not a valid offset index.

vector result = llDetectedVel(number);

```

- Arguments: `number` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: detected


## llDialog

```lsl
// Shows a dialog box on the screen of the specified agent, displaying msg along with up to 12 choice buttons. Clicking a button chats its label on channel. The chat originates at the object's position, but uses the agent's name and UUID, so it can be heard as long as the agent is still in the region.

llDialog(agent, msg, buttons, channel);

```

- Arguments: `agent` (key), `msg` (string), `buttons` (list), `channel` (integer)

- Returns: void | Energy: 10.0 | Sleep: 1.0 s | Categories: avatar_communication, chat, user_interface

- Delay: budget 1.0 s of script stall per call in event handlers.


## llDie

```lsl
// Deletes the entire object containing the script (the object does not go to inventory). Use llBreakLink first to delete only a single prim.

llDie();

```

- Returns: void | Energy: 0.0 | Sleep: 0.0 s | Categories: rez


## llDumpList2String

```lsl
// Returns a string that is the list src converted to a single string, with separator placed between each entry.

string result = llDumpList2String(src, separator);

```

- Arguments: `src` (list), `separator` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llEdgeOfWorld

```lsl
// Checks if the border reached along the vector dir from the vector pos is the edge of the world (i.e., has no neighboring simulator). Returns TRUE if it hits the edge of the world, or FALSE if there is a neighboring simulator.

integer result = llEdgeOfWorld(pos, dir);

```

- Arguments: `pos` (vector), `dir` (vector)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llEjectFromLand

```lsl
// Ejects the specified avatar from land/parcels owned by the object's owner (group or resident).

llEjectFromLand(avatar);

```

- Arguments: `avatar` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: land_moderation, parcel


## llEmail

```lsl
// Sends an email with the given destination address, subject, and body msg. The email will be sent from `{ll.GetKey()}@lsl.secondlife.com`. This can be used for script communication; see llGetNextEmail()

llEmail(address, subject, msg);

```

- Arguments: `address` (string), `subject` (string), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 20.0 s | Categories: avatar_communication, script_communication

- Delay: budget 20.0 s of script stall per call in event handlers.


## llEscapeURL

```lsl
// Returns a string representing the escaped/encoded version of url, replacing spaces with '%20' and non-alphanumeric characters with their '%xx' hexadecimal UTF-8 equivalent.

string result = llEscapeURL(url);

```

- Arguments: `url` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: web


## llEuler2Rot

```lsl
// Returns the quaternion representation of the Euler angles (in radians) within vec.

rotation result = llEuler2Rot(vec);

```

- Arguments: `vec` (vector)

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, quaternion


## llEvade

```lsl
// Directs a pathfinding character to evade target, attempting to hide from its pursuer if a hiding spot is available (i.e., no line of sight from the character's head to the pursuer's head, and no direct path on the navmesh).

llEvade(target, options);

```

- Arguments: `target` (key), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llExecCharacterCmd

```lsl
// Sends a command (specified by command) to the pathing system with options. Currently only supports stopping pathfinding or making the character jump.

llExecCharacterCmd(command, options);

```

- Arguments: `command` (integer), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llFabs

```lsl
// Returns the absolute (positive) value of val.

float result = llFabs(val);

```

- Arguments: `val` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llFindNotecardTextCount

```lsl
// Asynchronously requests the number of matches of pattern in the notecard name. Returns a key query handle for the dataserver event.

key result = llFindNotecardTextCount(name, pattern, options);

```

- Arguments: `name` (string), `pattern` (string), `options` (list)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, notecard


## llFindNotecardTextSync

```lsl
// Synchronously searches the notecard name in the region's cache for matches of pattern, without raising a dataserver event. Returns a strided list of the form [line, column, length, ...] with one stride per match, a list containing NAK if the notecard is not cached, or an empty list if there are no matches.

list result = llFindNotecardTextSync(name, pattern, start, count, options);

```

- Arguments: `name` (string), `pattern` (string), `start` (integer), `count` (integer), `options` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, notecard


## llFleeFrom

```lsl
// Directs a pathfinding character to keep the specified distance from the target position vector (within the region or adjacent regions).

llFleeFrom(position, distance, options);

```

- Arguments: `position` (vector), `distance` (float), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llFloor

```lsl
// Returns val rounded toward negative infinity. In other words, returns the largest integer less than or equal to val.

integer result = llFloor(val);

```

- Arguments: `val` (float)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llForceMouselook

```lsl
// Sets whether any avatar sitting on this prim is forced into mouselook mode. Setting mouselook to TRUE forces the mode; FALSE (default) allows the avatar to keep their current camera mode.

llForceMouselook(mouselook);

```

- Arguments: `mouselook` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llFrand

```lsl
// Returns a pseudo-random float in the range [0.0, mag) or (mag, 0.0] depending on the sign of mag. The value is inclusive of 0.0 but exclusive of mag.

float result = llFrand(mag);

```

- Arguments: `mag` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llGenerateKey

```lsl
// Generates and returns a unique versioned UUID key (utilizing SHA-1 hashing). Due to being versioned, it will not return NULL_KEY; however, the exact UUID version is an implementation detail that should not be relied upon.

key result = llGenerateKey();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: uuid


## llGetAccel

```lsl
// Returns a vector representing the acceleration of the object in the region's frame of reference.

vector result = llGetAccel();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: physics


## llGetAgentInfo

```lsl
// Returns an integer bitfield containing status information about the agent specified by id (such as AGENT_FLYING, AGENT_ATTACHMENTS, AGENT_SITTING, etc.).

integer result = llGetAgentInfo(id);

```

- Arguments: `id` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llGetAgentLanguage

```lsl
// Returns a string representing the language code of the preferred interface language set by the avatar.

string result = llGetAgentLanguage(avatar);

```

- Arguments: `avatar` (key)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llGetAgentList

```lsl
// Requests a list of avatar UUID keys for agents currently in the region, limited by scope. Returns a list of keys or a list containing an error message string.

list result = llGetAgentList(scope, options);

```

- Arguments: `scope` (integer), `options` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, parcel, region


## llGetAgentSize

```lsl
// Returns a vector representing the estimated bounding box size of the specified avatar, or ZERO_VECTOR if they are not in the same region.

vector result = llGetAgentSize(avatar);

```

- Arguments: `avatar` (key)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llGetAlpha

```lsl
// Returns a float representing the Blinn-Phong alpha (transparency) of face. If face is ALL_SIDES, returns the mean average of all faces.

float result = llGetAlpha(face);

```

- Arguments: `face` (integer)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetAndResetTime

```lsl
// Returns the elapsed script time in seconds as a float, then resets the script timer to zero.

float result = llGetAndResetTime();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llGetAnimation

```lsl
// Returns a string representing the name of the currently playing locomotion animation for the specified avatar.

string result = llGetAnimation(avatar);

```

- Arguments: `avatar` (key)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, avatar_animation, permissions


## llGetAnimationList

```lsl
// Returns a list of keys (UUIDs) representing all active animations currently playing on the specified avatar.

list result = llGetAnimationList(avatar);

```

- Arguments: `avatar` (key)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, avatar_animation, permissions


## llGetAnimationOverride

```lsl
// Returns a string representing the name of the animation currently overriding the specified anim_state. Requires the PERMISSION_OVERRIDE_ANIMATIONS or PERMISSION_TRIGGER_ANIMATION runtime permission.

string result = llGetAnimationOverride(anim_state);

```

- Arguments: `anim_state` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, avatar_animation, permissions


## llGetAttached

```lsl
// Returns the integer attachment point (an ATTACH_* constant) that the object is attached to, or 0 if it is unattached or pending detachment.

integer result = llGetAttached();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: attachments


## llGetAttachedList

```lsl
// Returns a list of object keys (UUIDs) worn by the specified avatar, in the order they were attached. HUDs are not included because they are neither public nor visible. Returns a list containing an error message string on failure.

list result = llGetAttachedList(avatar);

```

- Arguments: `avatar` (key)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: attachments, avatar


## llGetAttachedListFiltered

```lsl
// Returns a list of object keys (UUIDs) worn by the specified avatar, in the order they were attached, filtered by options. Returns a list containing an error message string on failure.

list result = llGetAttachedListFiltered(avatar, options);

```

- Arguments: `avatar` (key), `options` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: attachments, avatar


## llGetBoundingBox

```lsl
// Returns the bounding box of object (including any linked prims) relative to its root prim in local coordinates, formatted as [ (vector) min_corner, (vector) max_corner ].

list result = llGetBoundingBox(object);

```

- Arguments: `object` (key)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: object


## llGetCameraAspect

```lsl
// Returns a float representing the camera's current aspect ratio (width/height) of the agent who granted PERMISSION_TRACK_CAMERA. Returns 0.0 if permissions are not granted.

float result = llGetCameraAspect();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llGetCameraFOV

```lsl
// Returns a float representing the camera's current field of view (FOV) in radians of the agent who granted PERMISSION_TRACK_CAMERA. Returns 0.0 if permissions are not granted.

float result = llGetCameraFOV();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llGetCameraPos

```lsl
// Returns a vector representing the camera's current position in region coordinates of the agent who granted PERMISSION_TRACK_CAMERA. Returns ZERO_VECTOR if permissions are not granted.

vector result = llGetCameraPos();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llGetCameraRot

```lsl
// Returns a rotation representing the camera's current orientation of the agent who granted PERMISSION_TRACK_CAMERA. Returns ZERO_ROTATION if permissions are not granted.

rotation result = llGetCameraRot();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llGetCenterOfMass

```lsl
// Returns the vector position (in region coordinates) of the center of mass. Returns the individual child prim's center of mass if called from a child, or the entire linkset's center of mass if called from the root.

vector result = llGetCenterOfMass();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: object, physics


## llGetClosestNavPoint

```lsl
// Returns a list containing the closest vector position on the navigation mesh (navmesh) to the specified point (expressed in region-local space), or an empty list if none is found. Configured using options.

list result = llGetClosestNavPoint(point, options);

```

- Arguments: `point` (vector), `options` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llGetColor

```lsl
// Returns the Blinn-Phong RGB color vector of face (values between 0.0 and 1.0). If face is ALL_SIDES, returns the mean average of all faces.

vector result = llGetColor(face);

```

- Arguments: `face` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetCreator

```lsl
// Returns the key (UUID) of the prim's original creator.

key result = llGetCreator();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: prim


## llGetDate

```lsl
// Returns a string representing the current date in the UTC time zone in the format 'YYYY-MM-DD'.

string result = llGetDate();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGetDayLength

```lsl
// Returns an integer representing the number of seconds in the environmental day cycle applied to the current parcel.

integer result = llGetDayLength();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGetDayOffset

```lsl
// Returns an integer representing the offset duration (in seconds) added to calculate the current environmental time on this parcel.

integer result = llGetDayOffset();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGetDisplayName

```lsl
// Returns the display name string of the avatar specified by id if they are in the region or cached; returns an empty string otherwise (use llRequestDisplayName if the avatar is absent).

string result = llGetDisplayName(id);

```

- Arguments: `id` (key)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llGetEnergy

```lsl
// Returns a float representing the remaining physics energy of the object as a percentage (0.0 to 1.0) of its maximum capacity.

float result = llGetEnergy();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llGetEnv

```lsl
// Returns a string containing the requested regional data specified by name.

string result = llGetEnv(name);

```

- Arguments: `name` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetEnvironment

```lsl
// Returns a list containing the current environment parameters for the parcel or region at pos, retrieved in the order specified by params.

list result = llGetEnvironment(pos, params);

```

- Arguments: `pos` (vector), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, parcel_appearance


## llGetExperienceDetails

```lsl
// Returns a list of details for the specified experience_id, formatted as [string experience_name, key owner_id, key experience_id, integer state, string state_message, key group_id].

list result = llGetExperienceDetails(experience_id);

```

- Arguments: `experience_id` (key)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: experience


## llGetExperienceErrorMessage

```lsl
// Returns a text description of the specified experience error code, or a description of XP_ERROR_UNKNOWN_ERROR if the error is invalid.

string result = llGetExperienceErrorMessage(error);

```

- Arguments: `error` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: experience


## llGetExperienceList

```lsl
// 

list result = llGetExperienceList(agentid);

```

- Arguments: `agentid` (key)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: experience


## llGetForce

```lsl
// Returns a vector representing the constant force currently applied to the object (if the object is physical).

vector result = llGetForce();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: physics


## llGetFreeMemory

```lsl
// Returns an integer representing the number of free bytes of memory currently available to the script.

integer result = llGetFreeMemory();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llGetFreeURLs

```lsl
// Returns an integer representing the number of available HTTP URLs (remaining for the owner if the object is attached, or for the region if unattached).

integer result = llGetFreeURLs();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: script, web


## llGetGMTclock

```lsl
// Returns a float representing the time in seconds since midnight GMT (truncated to whole seconds).

float result = llGetGMTclock();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGetGameControlMode

```lsl
// Returns a GAME_CONTROL_MODE_* integer indicating the current game-control mode for the avatar specified by id.

integer result = llGetGameControlMode(id);

```

- Arguments: `id` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, game_control, input


## llGetGameControlModeAxes

```lsl
// Returns a list of floats representing the modal axes for the current game-control mode of the avatar specified by id. Element count and index meanings vary by mode; use the GAME_CONTROL_AXIS_* constants as indices.

list result = llGetGameControlModeAxes(id);

```

- Arguments: `id` (key)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, game_control, input


## llGetGameControlModeButtons

```lsl
// Returns a bitmask of the modal buttons currently active for the current game-control mode of the avatar specified by id. Bit meanings vary by mode; use the GAME_CONTROL_BUTTON_* constants as masks.

integer result = llGetGameControlModeButtons(id);

```

- Arguments: `id` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, game_control, input


## llGetGeometricCenter

```lsl
// Returns a vector representing the geometric center of the object relative to its root prim.

vector result = llGetGeometricCenter();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: physics


## llGetHTTPHeader

```lsl
// Returns a string representing the value of the specified header associated with the HTTP request_id.

string result = llGetHTTPHeader(request_id, header);

```

- Arguments: `request_id` (key), `header` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: web


## llGetHealth

```lsl
// Returns a float representing the current health of the avatar or object specified by id.

float result = llGetHealth(id);

```

- Arguments: `id` (key)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: combat


## llGetInventoryAcquireTime

```lsl
// Returns the time when the item was placed in the prim's inventory, as a UTC timestamp string of the form "YYYY-MM-DDThh:mm:ssZ"

string result = llGetInventoryAcquireTime(item);

```

- Arguments: `item` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llGetInventoryCreator

```lsl
// Returns the key (UUID) of the creator of the specified inventory item.

key result = llGetInventoryCreator(item);

```

- Arguments: `item` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llGetInventoryDesc

```lsl
// Returns the description string of the specified inventory item.

string result = llGetInventoryDesc(item);

```

- Arguments: `item` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llGetInventoryKey

```lsl
// Returns the key (UUID) of the specified inventory item.

key result = llGetInventoryKey(item);

```

- Arguments: `item` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llGetInventoryName

```lsl
// Returns the name of the inventory item of the specified type (INVENTORY_*) at the specified inventory index.

string result = llGetInventoryName(type, index);

```

- Arguments: `type` (integer), `index` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llGetInventoryNumber

```lsl
// Returns the count of items of the specified type (INVENTORY_*) in the prim's inventory.

integer result = llGetInventoryNumber(type);

```

- Arguments: `type` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llGetInventoryPermMask

```lsl
// Returns the specified item's permission flags for the specified group.

integer result = llGetInventoryPermMask(item, group);

```

- Arguments: `item` (string), `group` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: asset_permissions, prim_inventory


## llGetInventoryType

```lsl
// Returns an integer representing the INVENTORY_* type of the named inventory item.

integer result = llGetInventoryType(item);

```

- Arguments: `item` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llGetKey

```lsl
// Returns the key (UUID) of the prim containing the script.

key result = llGetKey();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, uuid


## llGetLandOwnerAt

```lsl
// Returns the key (UUID) of the land owner at the vector pos, or NULL_KEY if the land is public.

key result = llGetLandOwnerAt(pos);

```

- Arguments: `pos` (vector)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llGetLinkKey

```lsl
// Returns the key (UUID) of the linked prim or avatar specified by link.

key result = llGetLinkKey(link);

```

- Arguments: `link` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, uuid


## llGetLinkMedia

```lsl
// Returns a list containing the media parameters of the specified face on the linked prim link, retrieved in the order requested by params.

list result = llGetLinkMedia(link, face, params);

```

- Arguments: `link` (integer), `face` (integer), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, media, prim_media


## llGetLinkName

```lsl
// Returns a string containing the name of the linked prim specified by link.

string result = llGetLinkName(link);

```

- Arguments: `link` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset


## llGetLinkNumber

```lsl
// Returns the integer link number of the prim containing the script (0 for unlinked, 1 for the root, and 2+ for children).

integer result = llGetLinkNumber();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: prim


## llGetLinkNumberOfSides

```lsl
// Returns an integer representing the number of sides (faces) of the linked prim specified by link.

integer result = llGetLinkNumberOfSides(link);

```

- Arguments: `link` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llGetLinkPrimitiveParams

```lsl
// Returns a list of primitive parameters requested in params for the linked prim specified by link (equivalent to llGetPrimitiveParams).

list result = llGetLinkPrimitiveParams(link, params);

```

- Arguments: `link` (integer), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llGetLinkSitFlags

```lsl
// Returns an integer representing the active sit flags currently set on the linked prim specified by link.

integer result = llGetLinkSitFlags(link);

```

- Arguments: `link` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, sit


## llGetListEntryType

```lsl
// Returns an integer representing the variable type (TYPE_*) of the list entry at index in the list src.

integer result = llGetListEntryType(src, index);

```

- Arguments: `src` (list), `index` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llGetListLength

```lsl
// Returns an integer representing the total number of elements in the list src.

integer result = llGetListLength(src);

```

- Arguments: `src` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llGetLocalPos

```lsl
// Returns a position vector relative to the root prim. If called from the root prim, it returns the global region position (or the position relative to the attachment point if attached).

vector result = llGetLocalPos();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: prim


## llGetLocalRot

```lsl
// Returns a rotation representing the local orientation of a child prim relative to the root prim, or the object's overall rotation if called from the root.

rotation result = llGetLocalRot();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: prim


## llGetMass

```lsl
// Returns a float representing the mass of the object (in lindograms). Returns the total linkset mass if called from the root, or the individual prim's mass if called from a child prim. Returns the wearer's mass if inside an attachment.

float result = llGetMass();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, physics


## llGetMassMKS

```lsl
// Returns a float representing the mass of the object in kilograms. Functionally identical to llGetMass except for using MKS (metric) units.

float result = llGetMassMKS();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, physics


## llGetMaxScaleFactor

```lsl
// Returns a float representing the maximum scale factor that can be applied to the object via llScaleByFactor without violating size or linkability limits.

float result = llGetMaxScaleFactor();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llGetMemoryLimit

```lsl
// Returns an integer representing the maximum memory limit (in bytes) that the script is allowed to allocate.

integer result = llGetMemoryLimit();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llGetMinScaleFactor

```lsl
// Returns a float representing the minimum scale factor that can be applied to the object via llScaleByFactor without violating size limits.

float result = llGetMinScaleFactor();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llGetMoonDirection

```lsl
// Returns a normalized vector representing the current direction of the parcel's moon, taking altitude into account. Falls back to the region's moon direction if no custom parcel environment is set.

vector result = llGetMoonDirection();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, parcel_appearance


## llGetMoonRotation

```lsl
// Returns a rotation representing the orientation applied to the moon on the current parcel and altitude track. Falls back to the region's moon rotation if no custom parcel environment is set.

rotation result = llGetMoonRotation();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, parcel_appearance


## llGetNextEmail

```lsl
// Requests the next queued email via the email event. Emails must
1. Be sent to `{ll.GetKey()}@lsl.secondlife.com`
2. Be sent from the specified sender Address (or any address if blank)
3. Have the specified subject Subject (or any subject if blank)

llGetNextEmail(address, subject);

```

- Arguments: `address` (string), `subject` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script_communication


## llGetNotecardLine

```lsl
// Asynchronously requests the text of line in the notecard name. Returns a key query handle for the dataserver event, which receives EOF if line is past the end of the notecard.

key result = llGetNotecardLine(name, line);

```

- Arguments: `name` (string), `line` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.1 s | Categories: data_storage, dataserver, notecard

- Delay: budget 0.1 s of script stall per call in event handlers.


## llGetNotecardLineSync

```lsl
// Synchronously reads the text of line in the notecard name from the region's cache, without raising a dataserver event. Returns NAK if the notecard is not cached, or EOF if line is past the end of the notecard.

string result = llGetNotecardLineSync(name, line);

```

- Arguments: `name` (string), `line` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, notecard


## llGetNumberOfNotecardLines

```lsl
// Asynchronously requests the number of lines in the notecard name. Returns a key query handle for the dataserver event.

key result = llGetNumberOfNotecardLines(name);

```

- Arguments: `name` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.1 s | Categories: data_storage, dataserver, notecard

- Delay: budget 0.1 s of script stall per call in event handlers.


## llGetNumberOfPrims

```lsl
// Returns an integer representing the total number of prims and seated avatars in the linkset containing the script.

integer result = llGetNumberOfPrims();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset


## llGetNumberOfSides

```lsl
// Returns an integer representing the total number of sides (faces) of the prim containing the script.

integer result = llGetNumberOfSides();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetObjectAnimationNames

```lsl
// Returns a list of strings representing the names or UUIDs of all active animations currently playing on the object.

list result = llGetObjectAnimationNames();

```

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: object_animation


## llGetObjectDesc

```lsl
// Returns a string containing the description of the specific prim containing the script.

string result = llGetObjectDesc();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_properties


## llGetObjectDetails

```lsl
// Returns a list containing the requested parameters of the specified avatar or object id, retrieved in the order requested by params.

list result = llGetObjectDetails(id, params);

```

- Arguments: `id` (key), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: object, prim_properties


## llGetObjectLinkKey

```lsl
// Returns the key (UUID) of the linked child prim specified by link within the linkset identified by object_id.

key result = llGetObjectLinkKey(object_id, link);

```

- Arguments: `object_id` (key), `link` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: object, uuid


## llGetObjectMass

```lsl
// Returns a float representing the mass of the avatar or object specified by id.

float result = llGetObjectMass(id);

```

- Arguments: `id` (key)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: object, physics


## llGetObjectName

```lsl
// Returns a string containing the name of the specific prim containing the script.

string result = llGetObjectName();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_properties


## llGetObjectPermMask

```lsl
// Returns the script's object's permission flags for the specified group.

integer result = llGetObjectPermMask(group);

```

- Arguments: `group` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: asset_permissions, linkset


## llGetObjectPrimCount

```lsl
// Returns an integer representing the total number of prims in the object containing the specified prim.

integer result = llGetObjectPrimCount(prim);

```

- Arguments: `prim` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: object


## llGetOmega

```lsl
// Returns a vector representing the physical rotation (angular velocity) of the object in radians per second.

vector result = llGetOmega();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llGetOwner

```lsl
// Returns the key (UUID) of the object's current owner.

key result = llGetOwner();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, uuid


## llGetOwnerKey

```lsl
// Returns the key (UUID) of the owner of the prim specified by id.

key result = llGetOwnerKey(id);

```

- Arguments: `id` (key)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: object, uuid


## llGetParcelDetails

```lsl
// Returns a list containing the requested parcel details specified by params (retrieved in the same order) for the parcel at the vector pos.

list result = llGetParcelDetails(pos, params);

```

- Arguments: `pos` (vector), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llGetParcelFlags

```lsl
// Returns an integer bitfield of parcel flags (PARCEL_FLAG_*) for the parcel at the position pos.

integer result = llGetParcelFlags(pos);

```

- Arguments: `pos` (vector)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llGetParcelMaxPrims

```lsl
// Returns an integer representing the maximum combined land impact (prim limit) allowed for objects on the parcel at pos, determined either for the single parcel or sim-wide based on sim_wide.

integer result = llGetParcelMaxPrims(pos, sim_wide);

```

- Arguments: `pos` (vector), `sim_wide` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llGetParcelMusicURL

```lsl
// Returns a string containing the parcel's streaming music (audio) URL. The object owner must also be the land owner (or share the same group deeding).

string result = llGetParcelMusicURL();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llGetParcelPrimCount

```lsl
// Returns an integer representing the total land impact of objects on the parcel at pos in the specified category. If sim_wide is TRUE, returns combined usage for all regional parcels owned by the parcel owner; if FALSE, returns usage for only the specified parcel.

integer result = llGetParcelPrimCount(pos, category, sim_wide);

```

- Arguments: `pos` (vector), `category` (integer), `sim_wide` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llGetParcelPrimOwners

```lsl
// Returns a list of up to 100 strides (formatted as [key owner, integer land_impact]) representing owners of objects on the parcel at pos, sorted by owner key. Requires owner-like permissions for the parcel and the script owner's presence in the region.

list result = llGetParcelPrimOwners(pos);

```

- Arguments: `pos` (vector)

- Returns: list | Energy: 10.0 | Sleep: 2.0 s | Categories: parcel

- Delay: budget 2.0 s of script stall per call in event handlers.


## llGetPermissions

```lsl
// Returns an integer bitfield representing the permissions (PERMISSION_*) currently granted to the script.

integer result = llGetPermissions();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: permissions


## llGetPermissionsKey

```lsl
// Returns the key (UUID) of the avatar that last granted or declined permissions to the script, or NULL_KEY if the permissions request was ignored or cancelled.

key result = llGetPermissionsKey();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, permissions


## llGetPhysicsMaterial

```lsl
// Returns a list of the format [float gravity_multiplier, float restitution, float friction, float density] detailing the physical characteristics of the object.

list result = llGetPhysicsMaterial();

```

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, prim


## llGetPos

```lsl
// Returns a vector representing the current position of the object in region coordinates.

vector result = llGetPos();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: prim


## llGetPrimMediaParams

```lsl
// Returns a list containing the media parameters of the specified face, retrieved in the order requested by params. Returns an empty list if no media exists on the face.

list result = llGetPrimMediaParams(face, params);

```

- Arguments: `face` (integer), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 1.0 s | Categories: media, prim, prim_media

- Delay: budget 1.0 s of script stall per call in event handlers.


## llGetPrimitiveParams

```lsl
// Returns a list of primitive attribute values matching the requested params list.

list result = llGetPrimitiveParams(params);

```

- Arguments: `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.2 s | Categories: prim, prim_appearance, prim_properties

- Delay: budget 0.2 s of script stall per call in event handlers.


## llGetRegionAgentCount

```lsl
// Returns an integer representing the current number of avatars in the region.

integer result = llGetRegionAgentCount();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetRegionCorner

```lsl
// Returns a vector (in meters) representing the global grid coordinates of the south-west corner of the current region (Z component is always 0.0).

vector result = llGetRegionCorner();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetRegionDayLength

```lsl
// Returns an integer representing the total number of seconds in the region-wide day cycle.

integer result = llGetRegionDayLength();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: region, time


## llGetRegionDayOffset

```lsl
// Returns an integer representing the offset duration (in seconds) added to calculate the current environmental time for the region.

integer result = llGetRegionDayOffset();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: region, time


## llGetRegionFPS

```lsl
// Returns a float representing the average region simulator frames per second (FPS).

float result = llGetRegionFPS();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetRegionFlags

```lsl
// Returns an integer bitfield representing the region flags (REGION_FLAG_*) currently enabled for the region containing the object.

integer result = llGetRegionFlags();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetRegionMoonDirection

```lsl
// Returns a normalized vector representing the current direction of the region's moon, taking altitude into account.

vector result = llGetRegionMoonDirection();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: region, region_appearance


## llGetRegionMoonRotation

```lsl
// Returns a rotation representing the orientation applied to the moon at the region level, taking altitude track into account.

rotation result = llGetRegionMoonRotation();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: region, region_appearance


## llGetRegionName

```lsl
// Returns a string containing the name of the current region.

string result = llGetRegionName();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetRegionSunDirection

```lsl
// Returns a normalized vector representing the current direction of the region's sun, taking altitude into account.

vector result = llGetRegionSunDirection();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: region, region_appearance


## llGetRegionSunRotation

```lsl
// Returns a rotation representing the orientation applied to the sun at the region level, taking altitude track into account.

rotation result = llGetRegionSunRotation();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: region, region_appearance


## llGetRegionTimeDilation

```lsl
// Returns a float representing the current physics time dilation of the region, ranging from 0.0 (full dilation / slow) to 1.0 (no dilation / real-world speed).

float result = llGetRegionTimeDilation();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetRegionTimeOfDay

```lsl
// Returns a float with subsecond precision representing the elapsed seconds since region environmental midnight or region uptime (whichever is smaller). If the region's sun position is fixed, returns region uptime.

float result = llGetRegionTimeOfDay();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: region, time


## llGetRenderMaterial

```lsl
// Returns a string representing the render material on face (returns the inventory name if it is in the prim's inventory, or its key UUID otherwise).

string result = llGetRenderMaterial(face);

```

- Arguments: `face` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetRootPosition

```lsl
// Returns a vector representing the position (in region coordinates) of the root prim of the linkset containing the script.

vector result = llGetRootPosition();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset


## llGetRootRotation

```lsl
// Returns a rotation representing the orientation (relative to the region) of the root prim of the linkset containing the script.

rotation result = llGetRootRotation();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset


## llGetRot

```lsl
// Returns a rotation representing the prim's orientation relative to the region's axes.

rotation result = llGetRot();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: prim


## llGetSPMaxMemory

```lsl
// Returns an integer representing the maximum memory (in bytes) used by the script while the memory profiler was last active (only valid after using PROFILE_SCRIPT_MEMORY).

integer result = llGetSPMaxMemory();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llGetScale

```lsl
// Returns a vector representing the physical scale (dimensions in meters) of the prim containing the script.

vector result = llGetScale();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: prim


## llGetScriptName

```lsl
// Returns a string containing the name of the script calling this function.

string result = llGetScriptName();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory, script


## llGetScriptState

```lsl
// Returns a boolean integer indicating whether the specified script in the prim's inventory is running (returns TRUE if running, FALSE otherwise).

integer result = llGetScriptState(script);

```

- Arguments: `script` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory, script


## llGetSimStats

```lsl
// Returns a float containing the value of the requested region statistic specified by stat_type.

float result = llGetSimStats(stat_type);

```

- Arguments: `stat_type` (integer)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGetSimulatorHostname

```lsl
// Returns a string containing the hostname of the server machine running the script (e.g., 'sim225.agni.lindenlab.com').

string result = llGetSimulatorHostname();

```

- Returns: string | Energy: 10.0 | Sleep: 10.0 s | Categories: region

- Delay: budget 10.0 s of script stall per call in event handlers.


## llGetStartParameter

```lsl
// Returns an integer representing the start/rez parameter passed to the object on creation (returns 0 if rezzed by an agent).

integer result = llGetStartParameter();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: rez, script


## llGetStartString

```lsl
// Returns the initialization string passed to the object's root prim on rez with llRezObjectWithParams (via REZ_PARAM_STRING; returns an empty string if rezzed by an agent).

string result = llGetStartString();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: rez, script


## llGetStaticPath

```lsl
// Returns a list of position vectors representing pathfinding waypoints between start and end on the static navmesh for a character of the specified radius. Ignores movable obstacles and can be used in any region regardless of dynamic pathfinding status.

list result = llGetStaticPath(start_pos, end_pos, radius, params);

```

- Arguments: `start_pos` (vector), `end_pos` (vector), `radius` (float), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llGetStatus

```lsl
// Returns a boolean integer indicating whether the specified status flag status is enabled for the object.

integer result = llGetStatus(status);

```

- Arguments: `status` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, physics


## llGetSubString

```lsl
// Returns a copy of the substring from src within the inclusive codepoint range start_index..end_index. Negative indices count backward from the end of the string. If start_index is greater than end_index, the substring is the excluded range.

string result = llGetSubString(src, start_index, end_index);

```

- Arguments: `src` (string), `start_index` (integer), `end_index` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llGetSunDirection

```lsl
// Returns a normalized vector representing the current direction of the parcel's sun, taking altitude into account. Falls back to the region's sun direction if no custom parcel environment is set.

vector result = llGetSunDirection();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, parcel_appearance


## llGetSunRotation

```lsl
// Returns a rotation representing the orientation applied to the sun on the current parcel and altitude track. Falls back to the region's sun rotation if no custom parcel environment is set.

rotation result = llGetSunRotation();

```

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, parcel_appearance


## llGetTexture

```lsl
// Returns a string representing the Blinn-Phong diffuse texture on face (returns the inventory name if it is a texture in the prim's inventory, or its key UUID otherwise).

string result = llGetTexture(face);

```

- Arguments: `face` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetTextureOffset

```lsl
// Returns a vector containing the texture offsets of face in the X (horizontal U) and Y (vertical V) components (Z is unused).

vector result = llGetTextureOffset(face);

```

- Arguments: `face` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetTextureRot

```lsl
// Returns a float representing the texture rotation angle (in radians) on face.

float result = llGetTextureRot(face);

```

- Arguments: `face` (integer)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetTextureScale

```lsl
// Returns a vector containing the texture scales of face in the X and Y components (Z is unused).

vector result = llGetTextureScale(face);

```

- Arguments: `face` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llGetTime

```lsl
// Returns a float representing the elapsed script time in seconds with subsecond precision (since the script started, was reset, or since the last call to llResetTime or llGetAndResetTime).

float result = llGetTime();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llGetTimeOfDay

```lsl
// Returns a float with subsecond precision representing the elapsed seconds since parcel environmental midnight or region uptime (whichever is smaller). If the parcel's sun position is fixed, returns region uptime.

float result = llGetTimeOfDay();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGetTimestamp

```lsl
// Returns a string containing the current date and time in the UTC time zone formatted as an ISO 8601 timestamp ('YYYY-MM-DDThh:mm:ss.ff..fZ').

string result = llGetTimestamp();

```

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGetTorque

```lsl
// Returns a vector representing the physical torque force currently acting on the object (if the object is physical).

vector result = llGetTorque();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llGetUnixTime

```lsl
// Returns an integer representing the current Unix timestamp (the number of seconds elapsed since 00:00:00 Jan 1, 1970 UTC).

integer result = llGetUnixTime();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGetUsedMemory

```lsl
// Returns an integer representing the total number of bytes of memory currently used by the script (non-Mono scripts always return 16,384 bytes).

integer result = llGetUsedMemory();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llGetUsername

```lsl
// Returns a string representing the unique username of the avatar specified by id if they are connected to the region or cached; returns an empty string otherwise (use llRequestUsername if the avatar is absent).

string result = llGetUsername(id);

```

- Arguments: `id` (key)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llGetVel

```lsl
// Returns a vector representing the velocity of the object (in meters per second) relative to the global region coordinates. For physical objects, returns the velocity of its center of mass.

vector result = llGetVel();

```

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llGetVisualParams

```lsl
// Returns a list containing the values of the visual parameters requested in params for the agent specified by agentid.

list result = llGetVisualParams(agentid, params);

```

- Arguments: `agentid` (key), `params` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llGetWallclock

```lsl
// Returns a float representing the time in seconds since midnight Pacific Time (PST/PDT), which is equivalent to Second Life Time (SLT) truncated to whole seconds.

float result = llGetWallclock();

```

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: time


## llGiveAgentInventory

```lsl
// Gives the specified inventory items to the agent as a new folder named folder, as permitted by the permissions system. Customizes the transfer using options.

integer result = llGiveAgentInventory(agent, folder, items, options);

```

- Arguments: `agent` (key), `folder` (string), `items` (list), `options` (list)

- Returns: integer | Energy: 10.0 | Sleep: 3.0 s | Categories: avatar_inventory, prim_inventory

- Delay: budget 3.0 s of script stall per call in event handlers.


## llGiveInventory

```lsl
// Gives the specified inventory item to the target, as permitted by the permissions system. The target can be any agent or an object located in the same region.

llGiveInventory(target, item);

```

- Arguments: `target` (key), `item` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_inventory, prim_inventory


## llGiveInventoryList

```lsl
// Gives the list of inventory items to target as a new folder named folder. If target is an object, the items are passed directly into its inventory and no folder is created. The target must be an agent or an object in the same region.

llGiveInventoryList(target, folder, items);

```

- Arguments: `target` (key), `folder` (string), `items` (list)

- Returns: void | Energy: 10.0 | Sleep: 3.0 s | Categories: avatar_inventory, prim_inventory

- Delay: budget 3.0 s of script stall per call in event handlers.


## llGiveMoney

```lsl
// Transfers the specified amount of L$ from the script owner to the destination avatar. Silently fails if the PERMISSION_DEBIT permission has not been granted. Returns 0 (use llTransferLindenDollars to match transactions to transaction_result events).

integer result = llGiveMoney(destination, amount);

```

- Arguments: `destination` (key), `amount` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, money, permissions


## llGodLikeRezObject

```lsl
// Rezzes an object directly from a UUID specified by id at the position pos, provided the owner has the god-bit set.

llGodLikeRezObject(id, pos);

```

- Arguments: `id` (key), `pos` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory, rez


## llGround

```lsl
// Returns a float representing the ground height directly below the prim's position offset by the vector offset.

float result = llGround(offset);

```

- Arguments: `offset` (vector)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGroundContour

```lsl
// Returns a vector representing the ground contour direction (the direction with no change in elevation) directly below the prim's position offset by the vector offset.

vector result = llGroundContour(offset);

```

- Arguments: `offset` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGroundNormal

```lsl
// Returns a vector representing the ground surface normal vector directly below the current position offset by the vector offset.

vector result = llGroundNormal(offset);

```

- Arguments: `offset` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGroundRepel

```lsl
// Critically damps the object's vertical motion to height (using critical damping timescale tau) if it is within height * 0.5 of the terrain (or water level if water is TRUE). Only works on physics-enabled objects; do not use with vehicles.

llGroundRepel(height, water, tau);

```

- Arguments: `height` (float), `water` (integer), `tau` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llGroundSlope

```lsl
// Returns a vector representing the ground slope directly below the prim's position offset by the vector offset.

vector result = llGroundSlope(offset);

```

- Arguments: `offset` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llHMAC

```lsl
// Returns a Base64-encoded HMAC hash of msg using the secret key private_key and the specified digest algorithm (md5, sha1, sha224, sha256, sha384, or sha512).

string result = llHMAC(private_key, msg, algorithm);

```

- Arguments: `private_key` (string), `msg` (string), `algorithm` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llHTTPRequest

```lsl
// Sends an HTTP request to the specified url containing body and configured via parameters. Raises an http_response event and returns a key query handle identifying the request.

key result = llHTTPRequest(url, parameters, body);

```

- Arguments: `url` (string), `parameters` (list), `body` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: script_communication, web


## llHTTPResponse

```lsl
// Responds to the incoming HTTP request identified by request_id with the HTTP status code status and the payload body.

llHTTPResponse(request_id, status, body);

```

- Arguments: `request_id` (key), `status` (integer), `body` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: media, prim_media, script_communication, web


## llHash

```lsl
// Returns an integer representing the 32-bit hash value of the string val (returns 0 if the string is empty).

integer result = llHash(val);

```

- Arguments: `val` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llInsertString

```lsl
// Returns a copy of dst with src inserted at the given codepoint index.

string result = llInsertString(dst, index, src);

```

- Arguments: `dst` (string), `index` (integer), `src` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llInstantMessage

```lsl
// Sends an instant message containing msg to the agent identified by their key.

llInstantMessage(agent, msg);

```

- Arguments: `agent` (key), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 2.0 s | Categories: avatar_communication

- Delay: budget 2.0 s of script stall per call in event handlers.


## llIntegerToBase64

```lsl
// Returns an 8-character Base64 string representing the big-endian encoded value of number.

string result = llIntegerToBase64(number);

```

- Arguments: `number` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llIsFriend

```lsl
// Returns TRUE if agent_id and the owner of the script are friends, and FALSE otherwise.

integer result = llIsFriend(agent_id);

```

- Arguments: `agent_id` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llIsLinkGLTFMaterial

```lsl
// Checks the specified face on the linked prim link. Returns TRUE if the face material is a PBR render material, or FALSE if it uses Blinn-Phong diffuse textures.

integer result = llIsLinkGLTFMaterial(link, face);

```

- Arguments: `link` (integer), `face` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llJson2List

```lsl
// Parses the JSON string src and returns a list representing its top-level elements.

list result = llJson2List(src);

```

- Arguments: `src` (string)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, json


## llJsonGetValue

```lsl
// Parses the JSON string json and returns the value found by traversing the specified path of specifiers as a string.

string result = llJsonGetValue(json, specifiers);

```

- Arguments: `json` (string), `specifiers` (list)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, json


## llJsonSetValue

```lsl
// Returns a new JSON string representing json with the target located at specifiers set to value. Supports JSON_APPEND to append elements. Writing JSON_DELETE deletes the target. Overwriting array bounds or setting non-array levels with array indices returns JSON_INVALID.

string result = llJsonSetValue(json, specifiers, value);

```

- Arguments: `json` (string), `specifiers` (list), `value` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, json


## llJsonValueType

```lsl
// Parses the JSON string json and returns the JSON type constant (JSON_*) representing the value found at specifiers.

string result = llJsonValueType(json, specifiers);

```

- Arguments: `json` (string), `specifiers` (list)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, json


## llKey2Name

```lsl
// Returns a string containing the name of the prim or avatar specified by id. The target must be a valid, rezzed entity in the current region, otherwise an empty string is returned. Avatars return their legacy name.

string result = llKey2Name(id);

```

- Arguments: `id` (key)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: object


## llKeyCountKeyValue

```lsl
// Starts an asynchronous transaction requesting the total count of keys in the experience data store. Returns a key query handle for the dataserver event.

key result = llKeyCountKeyValue();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, experience, experience_data


## llKeysKeyValue

```lsl
// Starts an asynchronous transaction to retrieve count keys from the experience data store starting at the zero-based index first. Returns a key query handle for the dataserver event. Fails with XP_ERROR_KEY_NOT_FOUND if out of bounds.

key result = llKeysKeyValue(first, count);

```

- Arguments: `first` (integer), `count` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, experience, experience_data


## llLinear2sRGB

```lsl
// Returns a sRGB colorspace vector converted from the linear RGB colorspace argument.

vector result = llLinear2sRGB(color);

```

- Arguments: `color` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, math, prim_appearance, vector


## llLinkAdjustSoundVolume

```lsl
// Adjusts the volume of the currently playing sound attached to the linked prim link (has no effect on sounds started with llTriggerSound).

llLinkAdjustSoundVolume(link, volume);

```

- Arguments: `link` (integer), `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llLinkParticleSystem

```lsl
// Creates or updates a particle system on the linked prim link based on the list of rules. An empty list removes the particle system.

llLinkParticleSystem(link, rules);

```

- Arguments: `link` (integer), `rules` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: effects, particles


## llLinkPlaySound

```lsl
// Plays the specified sound on the linked prim link (once or looping) at volume. Only one sound can be attached to a prim at a time; new attachments or calling llStopSound stops previous playback. Controlled by flags.

llLinkPlaySound(link, sound, volume, flags);

```

- Arguments: `link` (integer), `sound` (string), `volume` (float), `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llLinkSetSoundQueueing

```lsl
// Enables or disables sound queuing on the linked prim link. When set to TRUE, sounds will queue and play in sequence.

llLinkSetSoundQueueing(link, queue);

```

- Arguments: `link` (integer), `queue` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llLinkSetSoundRadius

```lsl
// Limits the audibility radius of attached and triggered scripted sounds to distance radius (in meters) around the linked prim link.

llLinkSetSoundRadius(link, radius);

```

- Arguments: `link` (integer), `radius` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llLinkSitTarget

```lsl
// Sets the sit target position (offset) and orientation (rot) for the linked prim link, relative to the prim's own position and rotation. Clear by setting offset to <0.0, 0.0, 0.0>.

llLinkSitTarget(link, offset, rot);

```

- Arguments: `link` (integer), `offset` (vector), `rot` (rotation)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, sit


## llLinkStopSound

```lsl
// Stops the playback of any currently playing attached sound on the linked prim link.

llLinkStopSound(link);

```

- Arguments: `link` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llLinksetDataAvailable

```lsl
// Returns the number of bytes remaining in the linkset datastore.

integer result = llLinksetDataAvailable();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataCountFound

```lsl
// Returns the number of keys in the linkset datastore that match the regular expression pattern.

integer result = llLinksetDataCountFound(pattern);

```

- Arguments: `pattern` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataCountKeys

```lsl
// Returns the number of keys in the linkset datastore.

integer result = llLinksetDataCountKeys();

```

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataDelete

```lsl
// Deletes the unprotected key name from the linkset datastore, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

integer result = llLinksetDataDelete(name);

```

- Arguments: `name` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataDeleteFound

```lsl
// Deletes all keys in the linkset datastore that match the regular expression pattern, triggering a linkset_data event if the datastore changes. Protected keys are only deleted if their passphrase matches pass. Returns a list [num_deleted, num_failed_protected].

list result = llLinksetDataDeleteFound(pattern, pass);

```

- Arguments: `pattern` (string), `pass` (string)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataDeleteProtected

```lsl
// Deletes the protected key name from the linkset datastore using the passphrase pass, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

integer result = llLinksetDataDeleteProtected(name, pass);

```

- Arguments: `name` (string), `pass` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataFindKeys

```lsl
// Returns an alphabetically sorted list of up to count keys from the linkset datastore that match the regular expression pattern, starting at index start (returns all matching keys if count < 1).

list result = llLinksetDataFindKeys(pattern, start, count);

```

- Arguments: `pattern` (string), `start` (integer), `count` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataListKeys

```lsl
// Returns an alphabetically sorted list of up to count keys from the linkset datastore, starting at index start (returns all keys if count < 1).

list result = llLinksetDataListKeys(start, count);

```

- Arguments: `start` (integer), `count` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataRead

```lsl
// Returns the value of the unprotected key name from the linkset datastore. Returns an empty string if the key is not found or is protected.

string result = llLinksetDataRead(name);

```

- Arguments: `name` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataReadProtected

```lsl
// Returns the value of the protected key name from the linkset datastore using the passphrase pass. Returns an empty string if the key is not found or pass does not match.

string result = llLinksetDataReadProtected(name, pass);

```

- Arguments: `name` (string), `pass` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataReset

```lsl
// Deletes all keys from the linkset datastore, triggering a linkset_data event.

llLinksetDataReset();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataWrite

```lsl
// Creates or updates the unprotected key name in the linkset datastore with value, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

integer result = llLinksetDataWrite(name, value);

```

- Arguments: `name` (string), `value` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llLinksetDataWriteProtected

```lsl
// Creates or updates the protected key name in the linkset datastore with value using the passphrase pass, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

integer result = llLinksetDataWriteProtected(name, value, pass);

```

- Arguments: `name` (string), `value` (string), `pass` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, linkset, linkset_data


## llList2CSV

```lsl
// Returns a string of comma-separated values taken in order from the list src.

string result = llList2CSV(src);

```

- Arguments: `src` (list)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, list


## llList2Float

```lsl
// Returns the float value at index in the list src. Returns 0.0 if the index is out of bounds or if the value cannot be type-cast.

float result = llList2Float(src, index);

```

- Arguments: `src` (list), `index` (integer)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, list


## llList2Integer

```lsl
// Returns the integer value at index in the list src. Returns 0 if the index is out of bounds or if the value cannot be type-cast.

integer result = llList2Integer(src, index);

```

- Arguments: `src` (list), `index` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, list


## llList2Json

```lsl
// Converts the list values into a JSON string of the specified type (either a JSON_ARRAY or a JSON_OBJECT). Returns JSON_INVALID if an error is encountered.

string result = llList2Json(type, values);

```

- Arguments: `type` (string), `values` (list)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, json, list


## llList2Key

```lsl
// Returns the key (UUID) value at index in the list src. Returns a null string/key if the index is out of bounds or if the value cannot be type-cast.

key result = llList2Key(src, index);

```

- Arguments: `src` (list), `index` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, list


## llList2List

```lsl
// Returns a new list containing the subset of entries from src within the inclusive range specified by the start and end indices. Negative indices count backward from the end.

list result = llList2List(src, start_index, end_index);

```

- Arguments: `src` (list), `start_index` (integer), `end_index` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llList2ListSlice

```lsl
// Returns a list containing the slice_index'th element of every stride within the inclusive range from start to end in the strided list src. Stride must be a positive integer.

list result = llList2ListSlice(src, start_index, end_index, stride, slice_index);

```

- Arguments: `src` (list), `start_index` (integer), `end_index` (integer), `stride` (integer), `slice_index` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llList2ListStrided

```lsl
// Returns a new list containing the first element of every stride in the strided list src within the inclusive range from start to end.

list result = llList2ListStrided(src, start_index, end_index, stride);

```

- Arguments: `src` (list), `start_index` (integer), `end_index` (integer), `stride` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llList2Rot

```lsl
// Returns the rotation value at index in the list src. Returns ZERO_ROTATION if the index is out of bounds or if the value cannot be type-cast.

rotation result = llList2Rot(src, index);

```

- Arguments: `src` (list), `index` (integer)

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, list


## llList2String

```lsl
// Returns the string value at index in the list src. Returns an empty string if the index is out of bounds.

string result = llList2String(src, index);

```

- Arguments: `src` (list), `index` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, list


## llList2Vector

```lsl
// Returns the vector value at index in the list src. Returns ZERO_VECTOR if the index is out of bounds or if the value cannot be type-cast.

vector result = llList2Vector(src, index);

```

- Arguments: `src` (list), `index` (integer)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, list


## llListFindList

```lsl
// Returns the integer index of the first instance of list test within the list src (returns -1 if not found).

integer result = llListFindList(src, test);

```

- Arguments: `src` (list), `test` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListFindListNext

```lsl
// Returns the integer index of the specified instance of list test within the list src (returns -1 if not found).

integer result = llListFindListNext(src, test, instance);

```

- Arguments: `src` (list), `test` (list), `instance` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListFindStrided

```lsl
// Returns the integer index of the first instance of list test in the strided list src within the range from start to end (stepping through by stride). Returns -1 if not found.

integer result = llListFindStrided(src, test, start_index, end_index, stride);

```

- Arguments: `src` (list), `test` (list), `start_index` (integer), `end_index` (integer), `stride` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListInsertList

```lsl
// Returns a new list containing all elements of dest with the elements of src inserted starting at index start. Does not modify dest itself.

list result = llListInsertList(dest, src, start);

```

- Arguments: `dest` (list), `src` (list), `start` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListRandomize

```lsl
// Returns a randomized copy of the list src by blocks of size stride. If the list length is not perfectly divisible by stride, no randomization occurs.

list result = llListRandomize(src, stride);

```

- Arguments: `src` (list), `stride` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListReplaceList

```lsl
// Returns a copy of the list dest with the inclusive range from start to end removed, and the elements of src inserted in its place at start.

list result = llListReplaceList(dest, src, start_index, end_index);

```

- Arguments: `dest` (list), `src` (list), `start_index` (integer), `end_index` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListSort

```lsl
// Returns a copy of the list src, sorted into blocks of stride in ascending order (if ascending is TRUE) or descending order (if FALSE). Only works if the first entry of each block shares the same datatype.

list result = llListSort(src, stride, ascending);

```

- Arguments: `src` (list), `stride` (integer), `ascending` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListSortStrided

```lsl
// Returns a copy of the list src sorted into blocks of stride by the element at stride_index in each block. Sorted in ascending order (if ascending is TRUE) or descending order (if FALSE).

list result = llListSortStrided(src, stride, stride_index, ascending);

```

- Arguments: `src` (list), `stride` (integer), `stride_index` (integer), `ascending` (integer)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: list


## llListStatistics

```lsl
// Returns the numeric result of the statistical aggregate function operation (a LIST_STAT_* constant) on the numeric list src.

float result = llListStatistics(operation, src);

```

- Arguments: `operation` (integer), `src` (list)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: list, math


## llListen

```lsl
// Creates a listener on channel from name and id for msg. Returns an integer listener handle used to control or remove the listener. Empty strings or NULL_KEY filters do not filter on those parameters.

integer result = llListen(channel, name, id, msg);

```

- Arguments: `channel` (integer), `name` (string), `id` (key), `msg` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, chat, script_communication


## llListenControl

```lsl
// Enables or disables the listener specified by the integer handle. If active is TRUE, the listener is activated; if FALSE, it is deactivated.

llListenControl(handle, active);

```

- Arguments: `handle` (integer), `active` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, chat, script_communication


## llListenRemove

```lsl
// Completely removes the listener specified by the integer handle.

llListenRemove(handle);

```

- Arguments: `handle` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, chat, script_communication


## llLoadURL

```lsl
// Shows a dialog box displaying message to the avatar avatar offering to open the specified url. Clicking yes launches the URL in their default web browser.

llLoadURL(avatar, message, url);

```

- Arguments: `avatar` (key), `message` (string), `url` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: avatar_communication, user_interface, web

- Delay: budget 0.1 s of script stall per call in event handlers.


## llLog

```lsl
// Returns natural (base e) logarithm of val. If negative, return 0.0.

float result = llLog(val);

```

- Arguments: `val` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llLog10

```lsl
// Returns base-10 (common) logarithm of val. If negative, return 0.0.

float result = llLog10(val);

```

- Arguments: `val` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llLookAt

```lsl
// Causes the object to orient its positive Z-axis (up axis) toward the target vector, keeping its positive X-axis (forward axis) below the horizon. Tracks target until llStopLookAt is called or strength is set to 0.0.

llLookAt(target, strength, damping);

```

- Arguments: `target` (vector), `strength` (float), `damping` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llLoopSound

```lsl
// Plays the attached sound looping indefinitely at the specified volume. Only one sound can be attached to a prim at a time; new loops adjust the volume of the currently playing sound without restarting it.

llLoopSound(sound, volume);

```

- Arguments: `sound` (string), `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llLoopSoundMaster

```lsl
// Plays the attached sound looping indefinitely at the specified volume and declares it a Sync Master, forcing slave sounds to synchronize with it.

llLoopSoundMaster(sound, volume);

```

- Arguments: `sound` (string), `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llLoopSoundSlave

```lsl
// Plays the attached sound looping indefinitely at the specified volume, synchronized to the most audible active Sync Master in range.

llLoopSoundSlave(sound, volume);

```

- Arguments: `sound` (string), `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llMD5String

```lsl
// Returns a string of 32 hex characters representing the MD5 checksum of src salted with nonce (formatted as ':' + nonce).

string result = llMD5String(src, nonce);

```

- Arguments: `src` (string), `nonce` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llMakeExplosion

```lsl
// Deprecated. Generates a circular explosion of particles. Use llParticleSystem instead.

llMakeExplosion(particles, scale, vel, lifetime, arc, texture, offset);

```

- Arguments: `particles` (integer), `scale` (float), `vel` (float), `lifetime` (float), `arc` (float), `texture` (string), `offset` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: effects

- Delay: budget 0.1 s of script stall per call in event handlers.


## llMakeFire

```lsl
// Deprecated. Generates fire-like particles. Use llParticleSystem instead.

llMakeFire(particles, scale, vel, lifetime, arc, texture, offset);

```

- Arguments: `particles` (integer), `scale` (float), `vel` (float), `lifetime` (float), `arc` (float), `texture` (string), `offset` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: effects

- Delay: budget 0.1 s of script stall per call in event handlers.


## llMakeFountain

```lsl
// Deprecated. Generates a fountain of particles. Use llParticleSystem instead.

llMakeFountain(particles, scale, vel, lifetime, arc, bounce, texture, offset, bounce_offset);

```

- Arguments: `particles` (integer), `scale` (float), `vel` (float), `lifetime` (float), `arc` (float), `bounce` (integer), `texture` (string), `offset` (vector), `bounce_offset` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: effects

- Delay: budget 0.1 s of script stall per call in event handlers.


## llMakeSmoke

```lsl
// Deprecated. Generates smoke-like particles. Use llParticleSystem instead.

llMakeSmoke(particles, scale, vel, lifetime, arc, texture, offset);

```

- Arguments: `particles` (integer), `scale` (float), `vel` (float), `lifetime` (float), `arc` (float), `texture` (string), `offset` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: effects

- Delay: budget 0.1 s of script stall per call in event handlers.


## llManageEstateAccess

```lsl
// Adds or removes agents from the estate's access or ban lists, or groups from the estate's group access list, specified by the action. Returns TRUE if successful, or FALSE if throttled, if the action/ID is invalid, or if the script owner lacks estate management rights.

integer result = llManageEstateAccess(action, avatar);

```

- Arguments: `action` (integer), `avatar` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: land_moderation


## llMapBeacon

```lsl
// Displays an in-world beacon and optionally opens the world map for the avatar touching or wearing the object, centered on region_name with pos highlighted. Only works for attached scripts or during touch events.

llMapBeacon(region_name, pos, options);

```

- Arguments: `region_name` (string), `pos` (vector), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 1.0 s | Categories: avatar_communication, user_interface

- Delay: budget 1.0 s of script stall per call in event handlers.


## llMapDestination

```lsl
// Opens the world map for the avatar touching or wearing the object, centered on simname with pos highlighted. Only works for attached scripts or during touch events. Note: look_at currently has no effect.

llMapDestination(simname, pos, look_at);

```

- Arguments: `simname` (string), `pos` (vector), `look_at` (vector)

- Returns: void | Energy: 10.0 | Sleep: 1.0 s | Categories: avatar_communication, teleport, user_interface

- Delay: budget 1.0 s of script stall per call in event handlers.


## llMessageLinked

```lsl
// Triggers a link_message event, sending num, str, and id to the scripts in the prim(s) specified by link to allow scripts within the same object to communicate.

llMessageLinked(link, num, str, id);

```

- Arguments: `link` (integer), `num` (integer), `str` (string), `id` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script_communication


## llMinEventDelay

```lsl
// Sets the minimum delay time between events being handled (minimums and defaults vary by event type).

llMinEventDelay(delay);

```

- Arguments: `delay` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llModPow

```lsl
// Returns base raised to the power exponent, modulo modulus (i.e., (b^e)%m). All inputs are wrapped to unsigned 32-bit integer range [0..4294967295]. Output is wrapped to signed 32-bit integer range [-2147483648..2147483647]. Will never overflow, unlike (b^e), which can overflow to inf.

integer result = llModPow(base, exponent, modulus);

```

- Arguments: `base` (integer), `exponent` (integer), `modulus` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llModifyLand

```lsl
// Modifies the terrain using the specified land action and brush size (0, 1, or 2, corresponding to 2m x 2m, 4m x 4m, or 8m x 8m).

llModifyLand(action, brush);

```

- Arguments: `action` (integer), `brush` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llMoveToTarget

```lsl
// Critically damps the physical object's motion to position target in tau seconds. Setting tau to 0.0 stops the critical damping; recommended tau values are greater than 0.2.

llMoveToTarget(target, tau);

```

- Arguments: `target` (vector), `tau` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llName2Key

```lsl
// Requests the key (UUID) of the avatar name in the current region. Returns NULL_KEY if no matching agent is present. Formats are 'First Last' or 'first.last' (assumes 'Resident' if last name is omitted; case-insensitive).

key result = llName2Key(name);

```

- Arguments: `name` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar


## llNavigateTo

```lsl
// Directs a pathfinding character to navigate to the position pos (located in the current or adjacent regions) using the parameters specified in options.

llNavigateTo(pos, options);

```

- Arguments: `pos` (vector), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llOffsetTexture

```lsl
// Sets the texture horizontal (u) and vertical (v) offsets for the chosen face. If face is ALL_SIDES, offsets all faces.

llOffsetTexture(u, v, face);

```

- Arguments: `u` (float), `v` (float), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: prim, prim_appearance

- Delay: budget 0.2 s of script stall per call in event handlers.


## llOpenFloater

```lsl
// Opens the specified viewer floater_name loaded with url and configured via params. Returns an integer error code, or 0 if successful.

integer result = llOpenFloater(floater_name, url, params);

```

- Arguments: `floater_name` (string), `url` (string), `params` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication


## llOpenRemoteDataChannel

```lsl
// Deprecated. Creates a channel to listen for incoming XML-RPC calls, triggering a remote_data event with the channel ID once available.

llOpenRemoteDataChannel();

```

- Returns: void | Energy: 10.0 | Sleep: 1.0 s | Categories: script_communication

- Delay: budget 1.0 s of script stall per call in event handlers.


## llOrd

```lsl
// Returns the ordinal (Unicode copepoint integer) of the character at index in the string val. Negative indices count backward from the end of the string.

integer result = llOrd(val, index);

```

- Arguments: `val` (string), `index` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llOverMyLand

```lsl
// Returns TRUE if the avatar or object specified by key id is over land owned by the script owner, or FALSE otherwise.

integer result = llOverMyLand(id);

```

- Arguments: `id` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llOwnerSay

```lsl
// Sends the chat message msg privately to the object owner (the owner must be currently in the same region for the message to be received).

llOwnerSay(msg);

```

- Arguments: `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication


## llParcelMediaCommandList

```lsl
// Controls the playback of movies and other multimedia resources on a parcel or for an agent, using the PARCEL_MEDIA_COMMAND_* settings specified in commandList.

llParcelMediaCommandList(commandList);

```

- Arguments: `commandList` (list)

- Returns: void | Energy: 10.0 | Sleep: 2.0 s | Categories: media, parcel, parcel_media

- Delay: budget 2.0 s of script stall per call in event handlers.


## llParcelMediaQuery

```lsl
// Queries the media properties of the parcel containing the script, returning a list of values in the order requested by query. Only works if the object is owned by the landowner or deeded to the land's group.

list result = llParcelMediaQuery(query);

```

- Arguments: `query` (list)

- Returns: list | Energy: 10.0 | Sleep: 2.0 s | Categories: media, parcel, parcel_media

- Delay: budget 2.0 s of script stall per call in event handlers.


## llParseString2List

```lsl
// Breaks the string src into a list of substrings, discarding any separators, keeping spacers, and omitting any empty null values. separators and spacers accept up to 8 string entries each.

list result = llParseString2List(src, separators, spacers);

```

- Arguments: `src` (string), `separators` (list), `spacers` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llParseStringKeepNulls

```lsl
// Breaks the string src into a list of substrings, discarding separators and keeping spacers, while preserving empty null values (unlike llParseString2List). separators and spacers accept up to 8 string entries each.

list result = llParseStringKeepNulls(src, separators, spacers);

```

- Arguments: `src` (string), `separators` (list), `spacers` (list)

- Returns: list | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llParticleSystem

```lsl
// Creates or updates a particle system on the prim containing the script based on rules. An empty list removes the particle system.

llParticleSystem(rules);

```

- Arguments: `rules` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: effects, particles


## llPassCollisions

```lsl
// Sets the pass-collisions attribute. If pass is TRUE, collision events are passed from child prims to the root; if FALSE (default), they only trigger events in the affected child prim.

llPassCollisions(pass);

```

- Arguments: `pass` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, sensor


## llPassTouches

```lsl
// Sets the pass-touches attribute. If pass is TRUE, touch events are passed from child prims to the root; if FALSE (default), they only trigger events in the affected child prim.

llPassTouches(pass);

```

- Arguments: `pass` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: touch


## llPatrolPoints

```lsl
// Directs a pathfinding character to patrol sequentially through the coordinates specified in patrolPoints, configured by options.

llPatrolPoints(patrolPoints, options);

```

- Arguments: `patrolPoints` (list), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llPlaySound

```lsl
// Plays the specified sound once at volume, attached to the object. Only one sound can be attached to a prim at a time; new sounds or calling llStopSound stops previous playback. A second call with the same sound adjusts the volume without restarting it.

llPlaySound(sound, volume);

```

- Arguments: `sound` (string), `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llPlaySoundSlave

```lsl
// Plays the attached sound once at volume, synchronized to the next loop point of the most audible active Sync Master.

llPlaySoundSlave(sound, volume);

```

- Arguments: `sound` (string), `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llPointAt

```lsl
// Directs the avatar owning the object to point at the vector pos.

llPointAt(pos);

```

- Arguments: `pos` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llPow

```lsl
// Returns base raised to the power exponent. If result is imaginary, returns NaN.

float result = llPow(base, exponent);

```

- Arguments: `base` (float), `exponent` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llPreloadSound

```lsl
// Causes nearby viewers in range to preload the specified sound from the object's inventory to prevent playback delays.

llPreloadSound(sound);

```

- Arguments: `sound` (string)

- Returns: void | Energy: 10.0 | Sleep: 1.0 s | Categories: sound

- Delay: budget 1.0 s of script stall per call in event handlers.


## llPursue

```lsl
// Directs a pathfinding character to pursue and chase target, configured by the parameters specified in options.

llPursue(target, options);

```

- Arguments: `target` (key), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llPushObject

```lsl
// Applies physical impulse (force) and ang_impulse (rotational force) to the specified target avatar or object.

llPushObject(target, impulse, ang_impulse, is_local);

```

- Arguments: `target` (key), `impulse` (vector), `ang_impulse` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llReadKeyValue

```lsl
// Starts an asynchronous transaction to read the value associated with key k in the experience. Returns a key query handle for the dataserver event. Fails with XP_ERROR_KEY_NOT_FOUND if the key does not exist.

key result = llReadKeyValue(k);

```

- Arguments: `k` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, experience, experience_data


## llRefreshPrimURL

```lsl
// Legacy function intended to reload the web page displayed on the prim's faces (currently non-functional).

llRefreshPrimURL();

```

- Returns: void | Energy: 10.0 | Sleep: 20.0 s | Categories: media, prim_media, web

- Delay: budget 20.0 s of script stall per call in event handlers.


## llRegionSay

```lsl
// Broadcasts the message msg to all scripts listening on channel Channel within the region. PUBLIC_CHANNEL (0) cannot be used, so, only scripts can receive the message.

llRegionSay(channel, msg);

```

- Arguments: `channel` (integer), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: chat, script_communication


## llRegionSayTo

```lsl
// Sends the message msg on Channel privately to the targeted agent or object (if within the region). If target is an agent and channel is non-zero, the message can also be heard by any attachments worn by the avatar.

llRegionSayTo(target, channel, msg);

```

- Arguments: `target` (key), `channel` (integer), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, chat, script_communication


## llReleaseCamera

```lsl
// Deprecated. Intended to return camera control back to the avatar (use llClearCameraParams instead).

llReleaseCamera(avatar);

```

- Arguments: `avatar` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llReleaseControls

```lsl
// Stops taking inputs (previously acquired via llTakeControls) from the avatar, dequeuing any remaining control events and revoking the PERMISSION_TAKE_CONTROLS permission.

llReleaseControls();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, input, permissions


## llReleaseURL

```lsl
// Releases the specified url (previously obtained via llRequestURL), rendering it no longer usable.

llReleaseURL(url);

```

- Arguments: `url` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: media, web


## llRemoteDataReply

```lsl
// Deprecated. Sends an XML-RPC reply on channel to message_id with payload string sdata and integer idata.

llRemoteDataReply(channel, message_id, sdata, idata);

```

- Arguments: `channel` (key), `message_id` (key), `sdata` (string), `idata` (integer)

- Returns: void | Energy: 10.0 | Sleep: 3.0 s | Categories: script_communication

- Delay: budget 3.0 s of script stall per call in event handlers.


## llRemoteDataSetRegion

```lsl
// Deprecated. Used with XML-RPC to reregister remote data channels if the object moves to another region.

llRemoteDataSetRegion();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script_communication


## llRemoteLoadScript

```lsl
// Deprecated.

llRemoteLoadScript(target, script, running, start_param);

```

- Arguments: `target` (key), `script` (string), `running` (integer), `start_param` (integer)

- Returns: void | Energy: 10.0 | Sleep: 3.0 s | Categories: prim_inventory, script

- Delay: budget 3.0 s of script stall per call in event handlers.


## llRemoteLoadScriptPin

```lsl
// Copies the script into target, setting it running (if running is TRUE) with the start_param, provided the script owner has modify permissions on target and target's PIN matches pin (set via llSetRemoteScriptAccessPin).

llRemoteLoadScriptPin(target, script, pin, running, start_param);

```

- Arguments: `target` (key), `script` (string), `pin` (integer), `running` (integer), `start_param` (integer)

- Returns: void | Energy: 10.0 | Sleep: 3.0 s | Categories: prim, prim_inventory, script

- Delay: budget 3.0 s of script stall per call in event handlers.


## llRemoveFromLandBanList

```lsl
// Removes the specified avatar from the land parcel's ban list.

llRemoveFromLandBanList(avatar);

```

- Arguments: `avatar` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: land_moderation, parcel

- Delay: budget 0.1 s of script stall per call in event handlers.


## llRemoveFromLandPassList

```lsl
// Removes the specified avatar from the land parcel's pass/access list.

llRemoveFromLandPassList(avatar);

```

- Arguments: `avatar` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: land_moderation, parcel

- Delay: budget 0.1 s of script stall per call in event handlers.


## llRemoveInventory

```lsl
// Permanently deletes the named inventory item from the prim's inventory.

llRemoveInventory(item);

```

- Arguments: `item` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory


## llRemoveVehicleFlags

```lsl
// Disables the specified vehicle flags (sets them to FALSE) using the bitwise mask flags.

llRemoveVehicleFlags(flags);

```

- Arguments: `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, vehicles


## llReplaceAgentEnvironment

```lsl
// Replaces the region and parcel environment seen by the specified agent_id as part of an experience, transitioning the settings over transition seconds. Passing NULL_KEY or an empty string for environment restores defaults.

integer result = llReplaceAgentEnvironment(agent_id, transition, environment);

```

- Arguments: `agent_id` (key), `transition` (float), `environment` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, experience, parcel_appearance, region_appearance


## llReplaceEnvironment

```lsl
// Replaces the environment on the parcel containing position (or the entire region if position is <-1.0, -1.0, -1.0>) for the specified track_no. Modifies day_length and day_offset if specified. Requires edit permissions on the parcel or estate management rights.

integer result = llReplaceEnvironment(position, environment, track_no, day_length, day_offset);

```

- Arguments: `position` (vector), `environment` (string), `track_no` (integer), `day_length` (integer), `day_offset` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, parcel_appearance


## llReplaceSubString

```lsl
// Returns a copy of src with count occurrences of pattern replaced by replacement_pattern. Setting count to 0 replaces all occurrences; positive counts process left-to-right, while negative counts process right-to-left.

string result = llReplaceSubString(src, pattern, replacement_pattern, count);

```

- Arguments: `src` (string), `pattern` (string), `replacement_pattern` (string), `count` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llRequestAgentData

```lsl
// Asynchronously requests the specified data category (DATA_*) about the agent id. Triggers a dataserver event with the results and returns a key query handle.

key result = llRequestAgentData(id, data);

```

- Arguments: `id` (key), `data` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.1 s | Categories: avatar, dataserver

- Delay: budget 0.1 s of script stall per call in event handlers.


## llRequestDisplayName

```lsl
// Asynchronously requests the display name of the agent specified by id, triggering a dataserver event with the results. The agent does not need to be online or in the region. Returns a key query handle.

key result = llRequestDisplayName(id);

```

- Arguments: `id` (key)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, dataserver


## llRequestExperiencePermissions

```lsl
// Requests permission from the specified agent to participate in the experience. These permissions are persistent and apply grid-wide across all scripts in the experience, automatically triggering experience_permissions or experience_permissions_denied.

llRequestExperiencePermissions(agent, name);

```

- Arguments: `agent` (key), `name` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, experience, permissions


## llRequestInventoryData

```lsl
// Asynchronously requests data for the named inventory item, triggering a dataserver event. Currently, only landmark items are supported (which return local region coordinates). Returns a key query handle.

key result = llRequestInventoryData(item);

```

- Arguments: `item` (string)

- Returns: key | Energy: 10.0 | Sleep: 1.0 s | Categories: dataserver, prim_inventory

- Delay: budget 1.0 s of script stall per call in event handlers.


## llRequestPermissions

```lsl
// Requests permissions (a bitfield specified by permissions) from the agent in the same region, calling run_time_permissions if granted. This call does not pause script execution.

llRequestPermissions(agent, permissions);

```

- Arguments: `agent` (key), `permissions` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: permissions


## llRequestSecureURL

```lsl
// Asynchronously requests one secure HTTPS (SSL, port 12043) URL for use by this object, triggering an http_request event. Returns a key query handle.

key result = llRequestSecureURL();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: media, script_communication, web


## llRequestSimulatorData

```lsl
// Asynchronously requests data (using a DATA_SIM_* constant) about the region. Triggers a dataserver event and returns a key query handle.

key result = llRequestSimulatorData(region, data);

```

- Arguments: `region` (string), `data` (integer)

- Returns: key | Energy: 10.0 | Sleep: 1.0 s | Categories: dataserver, region

- Delay: budget 1.0 s of script stall per call in event handlers.


## llRequestURL

```lsl
// Asynchronously requests one HTTP URL for use by this script, triggering an http_request event. Returns a key query handle.

key result = llRequestURL();

```

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: media, script_communication, web


## llRequestUserKey

```lsl
// Asynchronously requests the Agent ID key (UUID) for the agent specified by their current or historical username, returning NULL_KEY if not found. Returns a key query handle for the dataserver event.

key result = llRequestUserKey(username);

```

- Arguments: `username` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, dataserver, uuid


## llRequestUsername

```lsl
// Asynchronously requests the unique single-word username of the agent identified by id, triggering a dataserver event. The agent does not need to be online or in the region. Returns a key query handle.

key result = llRequestUsername(id);

```

- Arguments: `id` (key)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, dataserver


## llResetAnimationOverride

```lsl
// Resets the animation override for anim_state to its default value (use 'ALL' to reset all states). Requires the PERMISSION_OVERRIDE_ANIMATIONS permission.

llResetAnimationOverride(anim_state);

```

- Arguments: `anim_state` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_animation, permissions


## llResetLandBanList

```lsl
// Removes all blocked residents from the land parcel's ban list.

llResetLandBanList();

```

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: land_moderation, parcel

- Delay: budget 0.1 s of script stall per call in event handlers.


## llResetLandPassList

```lsl
// Removes all residents from the land parcel's access/pass list.

llResetLandPassList();

```

- Returns: void | Energy: 10.0 | Sleep: 0.1 s | Categories: land_moderation, parcel

- Delay: budget 0.1 s of script stall per call in event handlers.


## llResetOtherScript

```lsl
// Resets the named script name in the prim's inventory.

llResetOtherScript(script);

```

- Arguments: `script` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory, script


## llResetScript

```lsl
// Resets the current script.

llResetScript();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llResetTime

```lsl
// Resets the script's elapsed time timer back to zero.

llResetTime();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llReturnObjectsByID

```lsl
// Returns objects specified by the list of UUIDs objects to their owners. Requires the PERMISSION_RETURN_OBJECTS permission, and the script owner must own the parcel or be an estate manager/region owner.

integer result = llReturnObjectsByID(objects);

```

- Arguments: `objects` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: land_moderation, rez


## llReturnObjectsByOwner

```lsl
// Returns objects owned by owner within the specified scope (parcel, parcel owner, or region). Requires the PERMISSION_RETURN_OBJECTS permission, and the script owner must own the parcel or be an estate manager/region owner.

integer result = llReturnObjectsByOwner(owner, scope);

```

- Arguments: `owner` (key), `scope` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: land_moderation, rez


## llRezAtRoot

```lsl
// Instantiates the named inventory object with the root prim at pos with velocity vel and rotation rot, passing start_param as the on_rez start parameter. The vel parameter is ignored if the rezzed object is non-physical.

llRezAtRoot(item, pos, vel, rot, start_param);

```

- Arguments: `item` (string), `pos` (vector), `vel` (vector), `rot` (rotation), `start_param` (integer)

- Returns: void | Energy: 200.0 | Sleep: 0.1 s | Categories: prim_inventory, rez

- Delay: budget 0.1 s of script stall per call in event handlers.


## llRezObject

```lsl
// Instantiates the named inventory object with the bounding box centered at pos with velocity vel and rotation rot, passing param as the on_rez start parameter. The vel parameter is ignored if the rezzed object is non-physical.

llRezObject(item, pos, vel, rot, start_param);

```

- Arguments: `item` (string), `pos` (vector), `vel` (vector), `rot` (rotation), `start_param` (integer)

- Returns: void | Energy: 200.0 | Sleep: 0.1 s | Categories: prim_inventory, rez

- Delay: budget 0.1 s of script stall per call in event handlers.


## llRezObjectWithParams

```lsl
// Instantiates the named inventory object (defaulting to the rezzing prim's position unless REZ_POS is specified) using the initial set of parameters specified in options. Returns the key of the rezzed object, or a blank key on failure.

key result = llRezObjectWithParams(item, options);

```

- Arguments: `item` (string), `options` (list)

- Returns: key | Energy: 200.0 | Sleep: 0.1 s | Categories: combat, prim_inventory, rez

- Delay: budget 0.1 s of script stall per call in event handlers.


## llRot2Angle

```lsl
// Returns the angle, in radians, that q rotates.

float result = llRot2Angle(q);

```

- Arguments: `q` (rotation)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion


## llRot2Axis

```lsl
// Returns the unit vector axis that q rotates around.

vector result = llRot2Axis(q);

```

- Arguments: `q` (rotation)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion, vector


## llRot2Euler

```lsl
// Returns a vector of Euler angles (roll, pitch, yaw) of q. The angles will be in radians.

vector result = llRot2Euler(q);

```

- Arguments: `q` (rotation)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, quaternion


## llRot2Fwd

```lsl
// Returns the unit vector pointing toward positive X (forward) in the coordinate space of rotation q. Equivalent to <1, 0, 0> * q.

vector result = llRot2Fwd(q);

```

- Arguments: `q` (rotation)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion, vector


## llRot2Left

```lsl
// Returns the unit vector pointing toward positive Y (left) in the coordinate space of rotation q. Equivalent to <0, 1, 0> * q.

vector result = llRot2Left(q);

```

- Arguments: `q` (rotation)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion, vector


## llRot2Up

```lsl
// Returns the unit vector pointing toward positive Z (up) in the coordinate space of rotation q. Equivalent to <0, 0, 1> * q.

vector result = llRot2Up(q);

```

- Arguments: `q` (rotation)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion, vector


## llRotBetween

```lsl
// Returns the shortest-path quaternion that rotates start_vec onto end_vec.

rotation result = llRotBetween(start_vec, end_vec);

```

- Arguments: `start_vec` (vector), `end_vec` (vector)

- Returns: rotation | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, math_trig, quaternion


## llRotLookAt

```lsl
// Causes the object to smoothly rotate to target_direction with a force defined by strength and damping. A strength of 0.0 cancels the rotation target. Rotation is maintained until stopped with llStopLookAt.

llRotLookAt(target_direction, strength, damping);

```

- Arguments: `target_direction` (rotation), `strength` (float), `damping` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llRotTarget

```lsl
// Registers the rotation rot with a leeway tolerance error (in radians) as a target, triggering at_rot_target and not_at_rot_target events. Returns an integer handle to unregister the target via llRotTargetRemove.

integer result = llRotTarget(rot, error);

```

- Arguments: `rot` (rotation), `error` (float)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llRotTargetRemove

```lsl
// Removes the rotational target specified by the integer handle registered with llRotTarget.

llRotTargetRemove(handle);

```

- Arguments: `handle` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llRotateTexture

```lsl
// Sets the texture rotation of face to the specified angle (in radians). If face is ALL_SIDES, rotates the texture on all faces.

llRotateTexture(angle, face);

```

- Arguments: `angle` (float), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: prim, prim_appearance

- Delay: budget 0.2 s of script stall per call in event handlers.


## llRound

```lsl
// Returns val rounded to the nearest integer. Halfway values are rounded toward infinity.

integer result = llRound(val);

```

- Arguments: `val` (float)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llSHA1String

```lsl
// Returns a string of 40 hex characters representing the SHA-1 security hash of src.

string result = llSHA1String(src);

```

- Arguments: `src` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llSHA256String

```lsl
// Returns a string of 64 hex characters representing the SHA-256 security hash of src.

string result = llSHA256String(src);

```

- Arguments: `src` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llSameGroup

```lsl
// Returns TRUE if the agent or object specified by uuid is in the same region (simulator) and shares the same active group as the prim containing the script; returns FALSE otherwise.

integer result = llSameGroup(uuid);

```

- Arguments: `uuid` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: object


## llSay

```lsl
// Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv("chat_range"), which is 20m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.

llSay(channel, msg);

```

- Arguments: `channel` (integer), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, chat, script_communication


## llScaleByFactor

```lsl
// Attempts to uniformly resize the entire object by scaling_factor, maintaining size-position ratios of the prims. Fails if the linkset is physical, a pathfinding character, in keyframed motion, would exceed prim scale/linkability limits, or would overflow parcel capacity.

integer result = llScaleByFactor(scaling_factor);

```

- Arguments: `scaling_factor` (float)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llScaleTexture

```lsl
// Sets the diffuse texture horizontal u and vertical v scales (repeats) on the specified face of the prim. Setting face to ALL_SIDES updates all sides. Negative scale values flip the texture.

llScaleTexture(u, v, face);

```

- Arguments: `u` (float), `v` (float), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: prim, prim_appearance

- Delay: budget 0.2 s of script stall per call in event handlers.


## llScriptDanger

```lsl
// Returns TRUE if the vector position pos is over public land, sandbox land, land restricting edit/build permissions, or land that disables outside scripts.

integer result = llScriptDanger(pos);

```

- Arguments: `pos` (vector)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, script


## llScriptProfiler

```lsl
// Enables or disables the script's profiling state using flags (supports PROFILE_SCRIPT_MEMORY on Mono, or PROFILE_NONE). Active profiling can significantly reduce script performance.

llScriptProfiler(flags);

```

- Arguments: `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llSendRemoteData

```lsl
// Deprecated. Sends an XML-RPC request to dest on channel, containing the channel ID as a string, integer idata, and string sdata. Returns a key representing the message_id.

key result = llSendRemoteData(channel, dest, idata, sdata);

```

- Arguments: `channel` (key), `dest` (string), `idata` (integer), `sdata` (string)

- Returns: key | Energy: 10.0 | Sleep: 3.0 s | Categories: script_communication

- Delay: budget 3.0 s of script stall per call in event handlers.


## llSensor

```lsl
// Performs a single scan from the prim's forward vector for name and id of type within radius meters and arc radians. Results trigger a sensor or no_sensor event. Passing empty filters (blank name, 0 type, or NULL_KEY id) disables that filter.

llSensor(name, id, type, radius, arc);

```

- Arguments: `name` (string), `id` (key), `type` (integer), `radius` (float), `arc` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sensor


## llSensorRemove

```lsl
// Removes the periodic sensor previously configured by llSensorRepeat.

llSensorRemove();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sensor


## llSensorRepeat

```lsl
// Sets up a repeating periodic scan every rate seconds for name and id of type within radius meters and arc radians of the forward vector. Results trigger sensor or no_sensor events.

llSensorRepeat(name, id, type, radius, arc, rate);

```

- Arguments: `name` (string), `id` (key), `type` (integer), `radius` (float), `arc` (float), `rate` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sensor


## llSetAgentEnvironment

```lsl
// Sets an individual agent's environmental settings using the attributes in params over a duration of transition seconds. Must be used as part of an experience; passing an empty list removes overrides.

integer result = llSetAgentEnvironment(agent_id, transition, params);

```

- Arguments: `agent_id` (key), `transition` (float), `params` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, experience, parcel_appearance, region_appearance


## llSetAgentRot

```lsl
// Sets the rotation of the avatar to rot, controlled by flags.

llSetAgentRot(rot, flags);

```

- Arguments: `rot` (rotation), `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, movement, physics


## llSetAlpha

```lsl
// Sets the diffuse texture alpha (opacity) of face. If face is ALL_SIDES, applies to all faces. Values are clamped between 0.1 and 1.0 (where 1.0 is fully opaque).

llSetAlpha(alpha, face);

```

- Arguments: `alpha` (float), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llSetAngularVelocity

```lsl
// Sets the angular velocity of a physical object to initial_omega (mass-independent). If local is TRUE, applied in local coordinates; if FALSE, applied in global coordinates. Has no effect on non-physical objects.

llSetAngularVelocity(initial_omega, is_local);

```

- Arguments: `initial_omega` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llSetAnimationOverride

```lsl
// Overrides the default animation for anim_state with anim (which must be in the object's inventory or a built-in animation). Requires the PERMISSION_OVERRIDE_ANIMATIONS permission.

llSetAnimationOverride(anim_state, anim);

```

- Arguments: `anim_state` (string), `anim` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_animation, permissions


## llSetBuoyancy

```lsl
// Sets the buoyancy of a physical object (requires physics to be enabled). A value of 0.0 offers no buoyancy, < 1.0 sinks, 1.0 counteracts gravity, and > 1.0 rises.

llSetBuoyancy(buoyancy);

```

- Arguments: `buoyancy` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: physics


## llSetCameraAtOffset

```lsl
// Sets the target offset vector (in local coordinates) that a seated avatar's camera will look at.

llSetCameraAtOffset(offset);

```

- Arguments: `offset` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: camera


## llSetCameraEyeOffset

```lsl
// Sets the eye offset vector (in local coordinates) where a seated avatar's camera is positioned.

llSetCameraEyeOffset(offset);

```

- Arguments: `offset` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: camera


## llSetCameraParams

```lsl
// Sets multiple camera parameters simultaneously using the list of rules. Requires the PERMISSION_CONTROL_CAMERA runtime permission.

llSetCameraParams(rules);

```

- Arguments: `rules` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llSetClickAction

```lsl
// Sets the action (a CLICK_ACTION_* flag) performed when an avatar left-clicks the prim.

llSetClickAction(action);

```

- Arguments: `action` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: input, money, prim_properties, touch, user_interface


## llSetColor

```lsl
// Sets the Blinn-Phong diffuse RGB color of face. If face is ALL_SIDES, applies the color to all faces.

llSetColor(color, face);

```

- Arguments: `color` (vector), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llSetContentType

```lsl
// Sets the 'Content-Type' header of subsequent HTTP server responses (via llHTTPResponse) for request_id using the specified content_type (a CONTENT_TYPE_* constant).

llSetContentType(request_id, content_type);

```

- Arguments: `request_id` (key), `content_type` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: media, prim_media, web


## llSetDamage

```lsl
// Sets the amount of damage delivered when this object hits an avatar. The object is immediately destroyed upon inflicting damage, and no collision event is triggered.

llSetDamage(damage);

```

- Arguments: `damage` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: combat


## llSetEnvironment

```lsl
// Overrides the environmental settings at position for a parcel (or region if position is <-1.0, -1.0, z>) using the parameters in params. Passing an empty params list removes previous overrides.

integer result = llSetEnvironment(position, params);

```

- Arguments: `position` (vector), `params` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel, parcel_appearance


## llSetExperienceKey

```lsl
// 

integer result = llSetExperienceKey(experienceid);

```

- Arguments: `experienceid` (key)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: experience


## llSetForce

```lsl
// Applies a constant linear force to a physical object. If local is TRUE, force is applied relative to local coordinates; if FALSE, applied relative to region coordinates.

llSetForce(force, is_local);

```

- Arguments: `force` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llSetForceAndTorque

```lsl
// Sets both the constant linear force and constant torque acting on a physical object. If local is TRUE, forces are applied in local coordinates; if FALSE, in global coordinates.

llSetForceAndTorque(force, torque, is_local);

```

- Arguments: `force` (vector), `torque` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llSetGroundTexture

```lsl
// Changes the painted terrain textures on the region based on changes. The script owner must have estate management rights. Returns an integer status.

integer result = llSetGroundTexture(changes);

```

- Arguments: `changes` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llSetHoverHeight

```lsl
// Critically damps the physical object's vertical movement to hover at height (above ground, or above water if water is TRUE) in tau seconds. Do not use with vehicles; call llStopHover to cancel.

llSetHoverHeight(height, water, tau);

```

- Arguments: `height` (float), `water` (integer), `tau` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llSetInventoryPermMask

```lsl
// Sets the specified item's permission flags for the specified group.

llSetInventoryPermMask(item, group, flags);

```

- Arguments: `item` (string), `group` (integer), `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: asset_permissions, prim_inventory


## llSetKeyframedMotion

```lsl
// Smoothly moves a non-physical object between the positions, orientations, and times specified in the keyframes list, configured via options. Collisions with keyframed objects are ignored. An empty keyframes list terminates the motion.

llSetKeyframedMotion(keyframes, options);

```

- Arguments: `keyframes` (list), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llSetLinkAlpha

```lsl
// Sets the Blinn-Phong alpha (transparency) of face on the linked prim link.

llSetLinkAlpha(link, alpha, face);

```

- Arguments: `link` (integer), `alpha` (float), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llSetLinkCamera

```lsl
// Sets the camera eye position offset eye and looking-at position offset at for avatars who sit on the linked prim link.

llSetLinkCamera(link, eye, at);

```

- Arguments: `link` (integer), `eye` (vector), `at` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: camera, sit


## llSetLinkColor

```lsl
// Sets the Blinn-Phong diffuse RGB color of face on the linked prim link.

llSetLinkColor(link, color, face);

```

- Arguments: `link` (integer), `color` (vector), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llSetLinkGLTFOverrides

```lsl
// Sets or removes individual GLTF override parameters specified by params on face of the linked prim link.

llSetLinkGLTFOverrides(link, face, params);

```

- Arguments: `link` (integer), `face` (integer), `params` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance


## llSetLinkMedia

```lsl
// Sets the media parameters specified by params on face of the linked prim link without a script delay. Returns an integer STATUS_* flag detailing success or failure.

integer result = llSetLinkMedia(link, face, params);

```

- Arguments: `link` (integer), `face` (integer), `params` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, media, prim_media, web


## llSetLinkPrimitiveParams

```lsl
// Deprecated (use llSetLinkPrimitiveParamsFast instead). Sets primitive parameters for the linked prim link according to rules.

llSetLinkPrimitiveParams(link, rules);

```

- Arguments: `link` (integer), `rules` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: linkset, prim_appearance, prim_properties

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetLinkPrimitiveParamsFast

```lsl
// Sets primitive parameters for the linked prim link according to rules with no built-in script sleep delay.

llSetLinkPrimitiveParamsFast(link, rules);

```

- Arguments: `link` (integer), `rules` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, prim_appearance, prim_properties


## llSetLinkRenderMaterial

```lsl
// Applies material (UUID or inventory name) to face of the linked prim link. Note: This clears most PRIM_GLTF_* properties on the face except for repeats, offsets, and rotation.

llSetLinkRenderMaterial(link, material, face);

```

- Arguments: `link` (integer), `material` (string), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: linkset, prim_appearance

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetLinkSitFlags

```lsl
// Sets the sit target flags for the linked prim link inside the linkset.

llSetLinkSitFlags(link, flags);

```

- Arguments: `link` (integer), `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, sit


## llSetLinkTexture

```lsl
// Applies texture (UUID or inventory name) to face of the linked prim link.

llSetLinkTexture(link, texture, face);

```

- Arguments: `link` (integer), `texture` (string), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: linkset, prim_appearance

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetLinkTextureAnim

```lsl
// Animates the texture on face of the linked prim link by setting the scale and offset according to mode. Parameters sizex/sizey define frames, start defines the start frame/angle, length defines duration, and rate defines playback speed.

llSetLinkTextureAnim(link, mode, face, sizex, sizey, start, length, rate);

```

- Arguments: `link` (integer), `mode` (integer), `face` (integer), `sizex` (integer), `sizey` (integer), `start` (float), `length` (float), `rate` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: effects, linkset, prim_appearance


## llSetLocalRot

```lsl
// Sets the rotation of a child prim relative to its root prim using rot.

llSetLocalRot(rot);

```

- Arguments: `rot` (rotation)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: movement, prim

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetMemoryLimit

```lsl
// Requests that limit bytes are reserved for the script. Returns TRUE on success or FALSE on failure (has no effect in LSO).

integer result = llSetMemoryLimit(limit);

```

- Arguments: `limit` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: script


## llSetObjectDesc

```lsl
// Sets the description of the prim containing the script to description (limited to 127 characters).

llSetObjectDesc(description);

```

- Arguments: `description` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_properties


## llSetObjectName

```lsl
// Sets the name of the prim containing the script to name.

llSetObjectName(name);

```

- Arguments: `name` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_properties


## llSetObjectPermMask

```lsl
// Sets the scripts's object's permission flags for the specified group.

llSetObjectPermMask(group, flags);

```

- Arguments: `group` (integer), `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: asset_permissions, linkset


## llSetParcelForSale

```lsl
// Sets the parcel the object is on for sale. If ForSale is TRUE, puts the land up for sale using Options (price, buyer, objects included). Setting ForSale to FALSE removes the parcel from sale. Requires parcel ownership and the PERMISSION_PRIVILEGED_LAND_ACCESS permission. Returns an error code or 0 if successful.

integer result = llSetParcelForSale(ForSale, Options);

```

- Arguments: `ForSale` (integer), `Options` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: parcel


## llSetParcelMusicURL

```lsl
// Sets the streaming audio (music) URL for the parcel containing the object. The object owner must match the landowner or land group.

llSetParcelMusicURL(url);

```

- Arguments: `url` (string)

- Returns: void | Energy: 10.0 | Sleep: 2.0 s | Categories: media, parcel, parcel_media

- Delay: budget 2.0 s of script stall per call in event handlers.


## llSetPayPrice

```lsl
// Suggests default amounts for the pay text input field price and the four payment dialog quick_pay_buttons when an avatar pays this object.

llSetPayPrice(price, quick_pay_buttons);

```

- Arguments: `price` (integer), `quick_pay_buttons` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: money, prim_properties, user_interface


## llSetPhysicsMaterial

```lsl
// Configures the physical characteristics of an object. The mask bitfield specifies which of the other parameters (gravity_multiplier, restitution, friction, or density) should be applied to the object.

llSetPhysicsMaterial(mask, gravity_multiplier, restitution, friction, density);

```

- Arguments: `mask` (integer), `gravity_multiplier` (float), `restitution` (float), `friction` (float), `density` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, prim, prim_properties


## llSetPos

```lsl
// Moves the non-physical object or prim toward the vector pos (up to 10m). If called in a child prim, pos is treated as root-relative; if called from the root prim, the entire object is moved.

llSetPos(pos);

```

- Arguments: `pos` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: movement, prim

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetPrimMediaParams

```lsl
// Sets the media parameters specified by params on the designated face of the prim. Returns an integer STATUS_* flag detailing success or failure.

integer result = llSetPrimMediaParams(face, params);

```

- Arguments: `face` (integer), `params` (list)

- Returns: integer | Energy: 10.0 | Sleep: 1.0 s | Categories: media, prim, prim_media, web

- Delay: budget 1.0 s of script stall per call in event handlers.


## llSetPrimURL

```lsl
// Deprecated (use llSetPrimMediaParams instead). Updates the URL displayed on the prim's faces.

llSetPrimURL(url);

```

- Arguments: `url` (string)

- Returns: void | Energy: 10.0 | Sleep: 20.0 s | Categories: media, prim, prim_media, web

- Delay: budget 20.0 s of script stall per call in event handlers.


## llSetPrimitiveParams

```lsl
// Deprecated (use llSetLinkPrimitiveParamsFast instead). Sets the prim's attributes according to rules.

llSetPrimitiveParams(rules);

```

- Arguments: `rules` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: prim, prim_appearance, prim_properties

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetRegionPos

```lsl
// Tries to move the entire object so that its root prim is within 0.1m of the vector position (underground positions are set to ground level). Returns TRUE on success or FALSE on failure.

integer result = llSetRegionPos(position);

```

- Arguments: `position` (vector)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, prim


## llSetRemoteScriptAccessPin

```lsl
// Sets the prim's remote script access PIN to pin (a non-zero value enables loading via llRemoteLoadScriptPin, while zero disables it).

llSetRemoteScriptAccessPin(pin);

```

- Arguments: `pin` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: prim_inventory, script

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetRenderMaterial

```lsl
// Applies material (UUID or inventory name) to face of the prim. Note: This clears most PRIM_GLTF_* properties on the face except for repeats, offsets, and rotation.

llSetRenderMaterial(material, face);

```

- Arguments: `material` (string), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: prim, prim_appearance

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetRot

```lsl
// Sets the rotation of the prim to rot. If in a child prim, rot is treated as root-relative; if in the root prim of a non-physical object, rotates the entire object.

llSetRot(rot);

```

- Arguments: `rot` (rotation)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: movement, prim

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetScale

```lsl
// Sets the physical scale (dimensions) of the prim containing the script to size.

llSetScale(size);

```

- Arguments: `size` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, prim_appearance


## llSetScriptState

```lsl
// Sets the running state of the named script in the prim's inventory. If running is TRUE, the script is enabled; if FALSE, it is disabled.

llSetScriptState(script, running);

```

- Arguments: `script` (string), `running` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_inventory, script


## llSetSitText

```lsl
// Displays the string text instead of 'Sit' (or 'Sit Here') in the viewer's right-click context menu.

llSetSitText(text);

```

- Arguments: `text` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, sit, user_interface


## llSetSoundQueueing

```lsl
// Sets whether attached sounds wait for the current sound to end before playing (enables queuing if queue is TRUE, disables if FALSE). The queue is one level deep.

llSetSoundQueueing(queue);

```

- Arguments: `queue` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llSetSoundRadius

```lsl
// Limits the audibility radius of attached and triggered scripted sounds to distance radius.

llSetSoundRadius(radius);

```

- Arguments: `radius` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llSetStatus

```lsl
// Sets the object status attributes specified by status to value.

llSetStatus(status, value);

```

- Arguments: `status` (integer), `value` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: linkset, physics, prim_properties


## llSetText

```lsl
// Displays floating text above the prim with the specified color vector and transparency alpha.

llSetText(text, color, alpha);

```

- Arguments: `text` (string), `color` (vector), `alpha` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, effects, prim_appearance, prim_properties


## llSetTexture

```lsl
// Applies the Blinn-Phong diffuse texture to face of the prim.

llSetTexture(texture, face);

```

- Arguments: `texture` (string), `face` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.2 s | Categories: prim, prim_appearance

- Delay: budget 0.2 s of script stall per call in event handlers.


## llSetTextureAnim

```lsl
// Animates the texture on face of the prim by setting its scale and offset. mode defines options, sizex/sizey define frames, start defines the start frame/angle, length defines duration, and rate defines playback speed.

llSetTextureAnim(mode, face, sizex, sizey, start, length, rate);

```

- Arguments: `mode` (integer), `face` (integer), `sizex` (integer), `sizey` (integer), `start` (float), `length` (float), `rate` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: effects, prim, prim_appearance


## llSetTimerEvent

```lsl
// Sets a timer to trigger a timer event periodically every sec seconds. Passing 0.0 stops further timer events.

llSetTimerEvent(sec);

```

- Arguments: `sec` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: script, time


## llSetTorque

```lsl
// Applies a constant torque rotational force to a physical object. If local is TRUE, torque is applied in local coordinates; if FALSE, applied in global coordinates.

llSetTorque(torque, is_local);

```

- Arguments: `torque` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llSetTouchText

```lsl
// Displays the string text instead of 'Touch' in the right-click context menu.

llSetTouchText(text);

```

- Arguments: `text` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim_properties, touch, user_interface


## llSetVehicleFlags

```lsl
// Enables the vehicle flags specified in the Flags bitmask.

llSetVehicleFlags(flags);

```

- Arguments: `flags` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: vehicles


## llSetVehicleFloatParam

```lsl
// Sets the specified vehicle float parameter param to value.

llSetVehicleFloatParam(param, value);

```

- Arguments: `param` (integer), `value` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: vehicles


## llSetVehicleRotationParam

```lsl
// Sets the specified vehicle rotation parameter param to rot.

llSetVehicleRotationParam(param, rot);

```

- Arguments: `param` (integer), `rot` (rotation)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: vehicles


## llSetVehicleType

```lsl
// Sets the vehicle physics preset type to one of the default vehicle types.

llSetVehicleType(type);

```

- Arguments: `type` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: vehicles


## llSetVehicleVectorParam

```lsl
// Sets the specified vehicle vector parameter param to vec.

llSetVehicleVectorParam(param, vec);

```

- Arguments: `param` (integer), `vec` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: vehicles


## llSetVelocity

```lsl
// Sets the linear velocity of a physical object to velocity. If local is TRUE, velocity is treated as a local directional vector; if FALSE, as a global region directional vector. Has no effect on non-physical objects.

llSetVelocity(velocity, is_local);

```

- Arguments: `velocity` (vector), `is_local` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llShout

```lsl
// Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv("shout_range"), which is 100m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.

llShout(channel, msg);

```

- Arguments: `channel` (integer), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, chat, script_communication


## llSignRSA

```lsl
// Returns the Base64-encoded RSA signature of msg using the PEM-formatted private_key and the specified digest algorithm (sha1, sha224, sha256, sha384, or sha512). Can be paired with llVerifyRSA to pass verifiable messages.

string result = llSignRSA(private_key, msg, algorithm);

```

- Arguments: `private_key` (string), `msg` (string), `algorithm` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llSin

```lsl
// Returns the sine of theta. Theta is in radians.

float result = llSin(theta);

```

- Arguments: `theta` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_trig


## llSitOnLink

```lsl
// Forces the avatar specified by agent_id (who must be participating in the experience) to sit on the sit target of the prim indicated by link. If occupied, searches down the linkset for an available sit target. Returns an integer.

integer result = llSitOnLink(agent_id, link);

```

- Arguments: `agent_id` (key), `link` (integer)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: experience, sit


## llSitTarget

```lsl
// Sets the sit target position (offset) and rotation (rot) relative to the prim's position and orientation. Clears the sit target if offset is ZERO_VECTOR.

llSitTarget(offset, rot);

```

- Arguments: `offset` (vector), `rot` (rotation)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: prim, sit


## llSleep

```lsl
// Puts the script to sleep for sec seconds (at least until the next server-frame, ~0.02222 seconds). The script is inactive during this time. If sec is 0.0 or less, the script does not sleep.

llSleep(sec);

```

- Arguments: `sec` (float)

- Returns: void | Energy: 0.0 | Sleep: 0.0 s | Categories: script, time


## llSound

```lsl
// Deprecated (use llPlaySound instead). Plays the specified sound at volume, with options to loop or queue the sound.

llSound(sound, volume, queue, loop);

```

- Arguments: `sound` (string), `volume` (float), `queue` (integer), `loop` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llSoundPreload

```lsl
// Deprecated (use llPreloadSound instead). Preloads the specified sound on viewers within range.

llSoundPreload(sound);

```

- Arguments: `sound` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llSqrt

```lsl
// Returns the square root of val. If negative, return NaN.

float result = llSqrt(val);

```

- Arguments: `val` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math


## llStartAnimation

```lsl
// Starts the animation anim (inventory or built-in) on the avatar who granted the script the PERMISSION_TRIGGER_ANIMATION permission (automatically granted for attached or sat-on objects).

llStartAnimation(anim);

```

- Arguments: `anim` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, avatar_animation, permissions


## llStartObjectAnimation

```lsl
// Starts the specified animation anim (inventory or built-in) on the rigged mesh object associated with the current script.

llStartObjectAnimation(anim);

```

- Arguments: `anim` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: object_animation


## llStopAnimation

```lsl
// Stops the specified animation anim (inventory, built-in, or UUID) on the avatar who granted the script the PERMISSION_TRIGGER_ANIMATION permission (automatically granted for attached or sat-on objects).

llStopAnimation(anim);

```

- Arguments: `anim` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, avatar_animation, permissions


## llStopHover

```lsl
// Stops the hover behavior (such as that initiated by llSetHoverHeight).

llStopHover();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llStopLookAt

```lsl
// Stops causing the object to look at or point toward a target (canceling llLookAt or llRotLookAt).

llStopLookAt();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llStopMoveToTarget

```lsl
// Stops the critically damped movement of the object toward a target (canceling llMoveToTarget). Use llStopLookAt to stop rotational tracking.

llStopMoveToTarget();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llStopObjectAnimation

```lsl
// Stops the specified animation anim (inventory, built-in, or UUID) on the rigged mesh object associated with the current script.

llStopObjectAnimation(anim);

```

- Arguments: `anim` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: object_animation


## llStopPointAt

```lsl
// Stops the avatar who owns the object from pointing.

llStopPointAt();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llStopSound

```lsl
// Stops playback of the currently playing attached sound.

llStopSound();

```

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llStringLength

```lsl
// Returns the number of unicode codepoints in the string.

integer result = llStringLength(str);

```

- Arguments: `str` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llStringToBase64

```lsl
// Returns the Base64 representation string of str, interpreting it as a UTF-8 byte sequence.

string result = llStringToBase64(str);

```

- Arguments: `str` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llStringTrim

```lsl
// Returns a copy of the string src with leading, trailing, or both types of whitespace (including spaces, tabs, and line feeds) eliminated, according to the specified trim type.

string result = llStringTrim(src, type);

```

- Arguments: `src` (string), `type` (integer)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llSubStringIndex

```lsl
// Returns the codepoint index of the first occurrence of pattern inside the string source. Returns -1 if not found. No regex.

integer result = llSubStringIndex(source, pattern);

```

- Arguments: `source` (string), `pattern` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llTakeCamera

```lsl
// Deprecated (use llSetCameraParams instead). Formerly used to take control of the agent's camera.

llTakeCamera(avatar);

```

- Arguments: `avatar` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions


## llTakeControls

```lsl
// Intercepts inputs (keyboard/mouse clicks) from the agent, specifically those specified by controls. The boolean accept determines if events are generated, and pass_on determines if inputs also perform their default functions. Requires the PERMISSION_TAKE_CONTROLS runtime permission.

llTakeControls(controls, accept, pass_on);

```

- Arguments: `controls` (integer), `accept` (integer), `pass_on` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, input, permissions


## llTan

```lsl
// Returns the tangent of theta. Theta is in radians.

float result = llTan(theta);

```

- Arguments: `theta` (float)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_trig


## llTarget

```lsl
// Registers a positional target at position with a leeway radius range. This triggers at_target and not_at_target events. Returns an integer handle to unregister the target via llTargetRemove.

integer result = llTarget(position, range);

```

- Arguments: `position` (vector), `range` (float)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: movement


## llTargetOmega

```lsl
// Applies a smooth client-side rotation around the local axis at a rate equal to spinrate multiplied by the magnitude of axis (in radians per second) with a force defined by gain. Set spinrate to 0.0 to cancel.

llTargetOmega(axis, spinrate, gain);

```

- Arguments: `axis` (vector), `spinrate` (float), `gain` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement, physics


## llTargetRemove

```lsl
// Removes the positional target specified by the integer handle registered with llTarget.

llTargetRemove(handle);

```

- Arguments: `handle` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: movement


## llTargetedEmail

```lsl
// Sends an email to with the given subject subject and body msg to the target (which can designate the owner or creator of the object). The email will be sent from `{ll.GetKey()}@lsl.secondlife.com`.

llTargetedEmail(target, subject, msg);

```

- Arguments: `target` (integer), `subject` (string), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 20.0 s | Categories: avatar_communication

- Delay: budget 20.0 s of script stall per call in event handlers.


## llTeleportAgent

```lsl
// Teleports the owning agent (who must grant PERMISSION_TELEPORT) to a landmark in the object's inventory. If landmark is empty, teleports them to position within the current region. Upon arrival, the agent is turned to face look_at. Can only teleport the owner.

llTeleportAgent(agent, landmark, position, look_at);

```

- Arguments: `agent` (key), `landmark` (string), `position` (vector), `look_at` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, permissions, teleport


## llTeleportAgentGlobalCoords

```lsl
// Teleports the owning agent (who must grant PERMISSION_TELEPORT) to region_coordinates within a target region specified by global_coordinates. Upon landing, the agent faces the direction look_at. Can only teleport the owner.

llTeleportAgentGlobalCoords(agent, global_coordinates, region_coordinates, look_at);

```

- Arguments: `agent` (key), `global_coordinates` (vector), `region_coordinates` (vector), `look_at` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, permissions, teleport


## llTeleportAgentHome

```lsl
// Teleports the avatar (who must be standing on land owned by the script owner) directly to their designated home location without warning (similar to a God Summons).

llTeleportAgentHome(avatar);

```

- Arguments: `avatar` (key)

- Returns: void | Energy: 100.0 | Sleep: 5.0 s | Categories: avatar, land_moderation, teleport

- Delay: budget 5.0 s of script stall per call in event handlers.


## llTextBox

```lsl
// Opens an input text box dialog displaying msg to the agent. Submitting text chats the input string on channel as if said by the agent. The chat originates at the object's position, but uses the agent's name and UUID, so it can be heard as long as the agent is still in the region.

llTextBox(agent, msg, channel);

```

- Arguments: `agent` (key), `msg` (string), `channel` (integer)

- Returns: void | Energy: 10.0 | Sleep: 1.0 s | Categories: avatar_communication, chat, user_interface

- Delay: budget 1.0 s of script stall per call in event handlers.


## llToLower

```lsl
// Returns a lowercase copy of the string src. Converts all unicode characters, not just ASCII.

string result = llToLower(src);

```

- Arguments: `src` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llToUpper

```lsl
// Returns an uppercase copy of the string src. Converts all unicode characters, not just ASCII.

string result = llToUpper(src);

```

- Arguments: `src` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: string


## llTransferLindenDollars

```lsl
// Transfers amount of L$ from the script owner to the destination avatar, requiring the PERMISSION_DEBIT permission. Returns a key query handle matching the resulting transaction_result event.

key result = llTransferLindenDollars(destination, amount);

```

- Arguments: `destination` (key), `amount` (integer)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: money, permissions


## llTransferOwnership

```lsl
// Transfers ownership of the object (or a copy of it, depending on Flags) to the specified agent. Returns an integer indicating the success or failure of the transfer.

integer result = llTransferOwnership(agent, flags, options);

```

- Arguments: `agent` (key), `flags` (integer), `options` (list)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: asset_permissions


## llTriggerSound

```lsl
// Plays specified sound once at volume, centered at the object's current position but not attached (does not move with the object and cannot be stopped or adjusted). Does not affect attached sounds.

llTriggerSound(sound, volume);

```

- Arguments: `sound` (string), `volume` (float)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llTriggerSoundLimited

```lsl
// Plays the specified sound once at volume, centered at the object but not attached, restricted to the axis-aligned bounding box defined by the coordinates top_north_east and bottom_south_west.

llTriggerSoundLimited(sound, volume, top_north_east, bottom_south_west);

```

- Arguments: `sound` (string), `volume` (float), `top_north_east` (vector), `bottom_south_west` (vector)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: sound


## llUnSit

```lsl
// Forces the agent specified by id to stand up if they are sitting on the object containing the script, or are currently over land owned by the object's owner.

llUnSit(id);

```

- Arguments: `id` (key)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, sit


## llUnescapeURL

```lsl
// Returns a string representing the unescaped/decoded version of url, replacing '%20' with spaces and decoding raw UTF-8 characters.

string result = llUnescapeURL(url);

```

- Arguments: `url` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: web


## llUpdateCharacter

```lsl
// Updates settings for a pathfinding character using the parameters specified in options.

llUpdateCharacter(options);

```

- Arguments: `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llUpdateKeyValue

```lsl
// Starts an asynchronous transaction to update the key k to value v inside the experience datastore. If checked is TRUE, the update fails with XP_ERROR_RETRY_UPDATE unless the existing value matches original_value.

key result = llUpdateKeyValue(k, v, checked, original_value);

```

- Arguments: `k` (string), `v` (string), `checked` (integer), `original_value` (string)

- Returns: key | Energy: 10.0 | Sleep: 0.0 s | Categories: data_storage, dataserver, experience, experience_data


## llVecDist

```lsl
// Returns a float representing the undirected, non-negative distance between vectors vec_a and vec_b.

float result = llVecDist(vec_a, vec_b);

```

- Arguments: `vec_a` (vector), `vec_b` (vector)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, vector


## llVecMag

```lsl
// Returns the magnitude (geometric length) of vec.

float result = llVecMag(vec);

```

- Arguments: `vec` (vector)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, vector


## llVecNorm

```lsl
// Returns the normalized unit vector pointing the same direction as vec. If <0, 0, 0>, return <0, 0, 0>.

vector result = llVecNorm(vec);

```

- Arguments: `vec` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: math, math_3d, vector


## llVerifyRSA

```lsl
// Returns TRUE if the Base64-formatted signature is verified as valid for the message msg when using the digest algorithm and public_key. Returns FALSE otherwise.

integer result = llVerifyRSA(public_key, msg, signature, algorithm);

```

- Arguments: `public_key` (string), `msg` (string), `signature` (string), `algorithm` (string)

- Returns: integer | Energy: 10.0 | Sleep: 0.0 s | Categories: cryptography


## llVolumeDetect

```lsl
// If detect is TRUE, enables VolumeDetect (object becomes phantom and physical objects/avatars can pass through it). Triggers collision_start on initial intersection and collision_end when intersection stops (standard collision events are suppressed while intersecting).

llVolumeDetect(detect);

```

- Arguments: `detect` (integer)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: physics, sensor


## llWanderWithin

```lsl
// Directs a pathfinding character to wander around a central coordinate origin, restricted within the bounding distance limits of dist and configured by options.

llWanderWithin(origin, dist, options);

```

- Arguments: `origin` (vector), `dist` (vector), `options` (list)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: pathfinding


## llWater

```lsl
// Returns a float representing the water height directly below the prim's position offset by the vector offset.

float result = llWater(offset);

```

- Arguments: `offset` (vector)

- Returns: float | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llWhisper

```lsl
// Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv("whisper_range"), which is 10m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.

llWhisper(channel, msg);

```

- Arguments: `channel` (integer), `msg` (string)

- Returns: void | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar_communication, chat, script_communication


## llWind

```lsl
// Returns a vector representing the wind velocity at the prim's position offset by the vector offset.

vector result = llWind(offset);

```

- Arguments: `offset` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: region


## llWorldPosToHUD

```lsl
// Returns the local position vector that places the center of the HUD object directly over the world coordinate world_pos as viewed by the current camera. Requires the PERMISSION_TRACK_CAMERA runtime permission.

vector result = llWorldPosToHUD(world_pos);

```

- Arguments: `world_pos` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: avatar, camera, permissions, user_interface


## llXorBase64

```lsl
// Correctly performs a bitwise exclusive OR (XOR) on Base64 strings str1 and str2, returning the result as a Base64 string. The string str2 repeats if it is shorter than str1.

string result = llXorBase64(str1, str2);

```

- Arguments: `str1` (string), `str2` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llXorBase64Strings

```lsl
// Deprecated (use llXorBase64 instead). Retained for backwards compatibility. Incorrectly performs a bitwise exclusive OR (XOR) on Base64 strings str1 and str2.

string result = llXorBase64Strings(str1, str2);

```

- Arguments: `str1` (string), `str2` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.3 s | Categories: data_conversion

- Delay: budget 0.3 s of script stall per call in event handlers.


## llXorBase64StringsCorrect

```lsl
// Deprecated (use llXorBase64 instead). Correctly performs (unless nulls are present) a bitwise exclusive OR (XOR) on Base64 strings str1 and str2.

string result = llXorBase64StringsCorrect(str1, str2);

```

- Arguments: `str1` (string), `str2` (string)

- Returns: string | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion


## llsRGB2Linear

```lsl
// Returns a linear RGB colorspace vector converted from the sRGB colorspace argument.

vector result = llsRGB2Linear(color);

```

- Arguments: `color` (vector)

- Returns: vector | Energy: 10.0 | Sleep: 0.0 s | Categories: data_conversion, math, prim_appearance, vector
