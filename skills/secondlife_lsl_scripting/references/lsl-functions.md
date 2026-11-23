# LSL Function Reference (generated from secondlife/lsl-definitions)

Generated from `lsl_definitions.yaml` in https://github.com/secondlife/lsl-definitions (MIT). Every entry carries the canonical signature, tooltip, energy cost, sleep delay, function ID, and categories exactly as upstream defines them. Guidance lines are derived from the function's category and cost fields.


## llAbs

```lsl
integer llAbs(integer val)
```

- Purpose: Returns the absolute (positive) integer value of val.

- Argument `val` (integer): Integer to convert.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 6 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.abs`. Double precision; fastcall.


## llAcos

```lsl
float llAcos(float val)
```

- Purpose: Returns the arccosine of val in radians.

- Argument `val` (float): A number in the range [-1.0, 1.0].

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 172 | Native: True | Pure (no side effects): False

- Categories: math, math_trig

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.acos`. Double precision; fastcall.


## llAddToLandBanList

```lsl
void llAddToLandBanList(key avatar, float hours)
```

- Purpose: Adds the avatar to the parcel ban list for the specified number of hours. A value of 0 hours adds the avatar indefinitely. Banned users teleporting to the parcel are redirected to a neighboring parcel; the minimum accepted duration is 0.01 hours (approximately 36 seconds).

- Argument `avatar` (key): UUID of the avatar to add to the ban list.

- Argument `hours` (float): Duration, in hours, to ban the avatar for (0 for indefinite).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 310 | Native: False | Pure (no side effects): False

- Categories: land_moderation, parcel

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llAddToLandPassList

```lsl
void llAddToLandPassList(key avatar, float hours)
```

- Purpose: Adds the avatar to the land pass list for the specified number of hours (or indefinitely if hours is 0).

- Argument `avatar` (key): UUID of the avatar to add to the pass list.

- Argument `hours` (float): Duration, in hours, to allow the avatar for (range [0.0, 144.0], 0 for indefinite).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 240 | Native: False | Pure (no side effects): False

- Categories: land_moderation, parcel

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llAdjustDamage

```lsl
void llAdjustDamage(integer number, float new_damage)
```

- Purpose: Modifies the amount of damage applied by the current on_damage event after it completes processing, specified by the damage event index number.

- Argument `number` (integer): Index of the damage event to modify.

- Argument `new_damage` (float): New damage value to be applied or distributed after on_damage processing.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 555 | Native: False | Pure (no side effects): False

- Categories: combat, detected


## llAdjustSoundVolume

```lsl
void llAdjustSoundVolume(float volume)
```

- Purpose: Adjusts the volume of the currently playing attached sound (has no effect on sounds started with llTriggerSound).

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 207 | Native: False | Pure (no side effects): False

- Categories: sound

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llAgentInExperience

```lsl
integer llAgentInExperience(key agent)
```

- Purpose: Returns TRUE if the specified agent is in the experience and the experience can run in the current region/location; returns FALSE otherwise.

- Argument `agent` (key): UUID of the avatar in the same region to query.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 392 | Native: False | Pure (no side effects): False

- Categories: avatar, experience

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llAllowInventoryDrop

```lsl
void llAllowInventoryDrop(integer add)
```

- Purpose: If add is TRUE, allows users without object modify permissions to drop inventory items into the prim. If FALSE, restricts inventory dropping to users with modify permissions.

- Argument `add` (integer): Boolean. If TRUE, allows anyone to drop inventory items into the prim (even without modify rights). If FALSE, restricts inventory dropping to those with modify permissions.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 176 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llAngleBetween

```lsl
float llAngleBetween(rotation start_rot, rotation end_rot)
```

- Purpose: Returns the angle, in radians, between rotations start_rot and and end_rot.

- Argument `start_rot` (rotation): Starting rotation.

- Argument `end_rot` (rotation): Ending rotation.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 174 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llApplyImpulse

```lsl
void llApplyImpulse(vector momentum, integer is_local)
```

- Purpose: Applies a linear impulse (momentum) to a physical object. If local is TRUE, the impulse is applied in local coordinates; otherwise, it is applied in global region coordinates.

- Argument `momentum` (vector): Linear impulse vector to apply.

- Argument `is_local` (integer): Boolean. If TRUE, momentum is treated as a local directional vector; if FALSE, it is treated as a global region vector.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 72 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llApplyRotationalImpulse

```lsl
void llApplyRotationalImpulse(vector force, integer is_local)
```

- Purpose: Applies a rotational impulse (force) to a physical object. If local is TRUE, the rotational impulse is applied in local coordinates; otherwise, it is applied in global region coordinates.

- Argument `force` (vector): Rotational impulse vector to apply.

- Argument `is_local` (integer): Boolean. If TRUE, the force is treated as a local directional vector; if FALSE, it is treated as a global region vector.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 73 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llAsin

```lsl
float llAsin(float val)
```

- Purpose: Returns the arcsine of val in radians.

- Argument `val` (float): A number in the range [-1.0, 1.0].

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 173 | Native: True | Pure (no side effects): False

- Categories: math, math_trig

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.asin`. Double precision; fastcall.


## llAtan2

```lsl
float llAtan2(float y, float x)
```

- Purpose: Returns the arctangent of y/x in radians, using the signs to determine the quadrant. Note the argument order: Y is the first parameter, X is the second parameter.

- Argument `y` (float): Y coordinate.

- Argument `x` (float): X coordinate.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 3 | Native: True | Pure (no side effects): True

- Categories: math, math_trig

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.atan2`. Double precision; fastcall.


## llAttachToAvatar

```lsl
void llAttachToAvatar(integer attach_point)
```

- Purpose: Attaches the object to the avatar who has granted the PERMISSION_ATTACH permission. Takes the object into the user's inventory and attaches it at attach_point.

- Argument `attach_point` (integer): ATTACH_* constant or integer value representing the target attachment point.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 113 | Native: False | Pure (no side effects): False

- Categories: attachments, avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llAttachToAvatarTemp

```lsl
void llAttachToAvatarTemp(integer attach_point)
```

- Purpose: Attaches the object temporarily to an avatar who has granted the PERMISSION_ATTACH permission. No permanent inventory is created, and the object disappears on detach or disconnect. Can be used on non-owners (changing ownership to the wearer).

- Argument `attach_point` (integer): ATTACH_* constant or integer value representing the target attachment point.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 391 | Native: False | Pure (no side effects): False

- Categories: attachments, avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llAvatarOnLinkSitTarget

```lsl
key llAvatarOnLinkSitTarget(integer link)
```

- Purpose: Returns the UUID of the avatar seated on the specified link's sit target, or NULL_KEY if no avatar is sitting there.

- Argument `link` (integer): Index of the prim in the linkset (1 for root, >1 for children), or a LINK_* flag.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 376 | Native: False | Pure (no side effects): False

- Categories: avatar, linkset, sit

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llAvatarOnSitTarget

```lsl
key llAvatarOnSitTarget()
```

- Purpose: Returns the UUID of the avatar seated on the prim's sit target (defined via llSitTarget), or NULL_KEY if no avatar is sitting there or the prim lacks a sit target.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 239 | Native: False | Pure (no side effects): False

- Categories: avatar, prim, sit

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llAxes2Rot

```lsl
rotation llAxes2Rot(vector fwd, vector left, vector up)
```

- Purpose: Returns the rotation defined by the coordinate axes fwd, left, and up.

- Argument `fwd` (vector): Forward/back directional vector of the rotation.

- Argument `left` (vector): Left/right directional vector of the rotation.

- Argument `up` (vector): Up/down directional vector of the rotation.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 17 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llAxisAngle2Rot

```lsl
rotation llAxisAngle2Rot(vector axis, float angle)
```

- Purpose: Returns the rotation that rotates angle radians around the axis vector.

- Argument `axis` (vector): Axis vector to rotate around.

- Argument `angle` (float): Angle to rotate, in radians.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 169 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llBase64ToInteger

```lsl
integer llBase64ToInteger(string str)
```

- Purpose: Returns an integer representing the Base64-decoded big-endian value of str. Returns zero if str is longer than 8 characters; the return value is unpredictable if str contains fewer than 6 characters.

- Argument `str` (string): Base64-encoded string to decode.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 281 | Native: False | Pure (no side effects): True

- Categories: data_conversion

- SLua: deprecated in favour of ``. Use 'llbase64.decode' and 'string.unpack' or 'buffer.readi32' instead.


## llBase64ToString

```lsl
string llBase64ToString(string str)
```

- Purpose: Decodes the Base64-encoded string str into a conventional string, interpreting the bytes as a UTF-8 character sequence. Unprintable characters are converted to question marks.

- Argument `str` (string): Base64-encoded string to decode.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 261 | Native: False | Pure (no side effects): True

- Categories: data_conversion

- SLua: deprecated in favour of `llbase64.decode`. 


## llBreakAllLinks

```lsl
void llBreakAllLinks()
```

- Purpose: Delinks all prims in the linkset. Requires the PERMISSION_CHANGE_LINKS runtime permission, which must be requested and granted by the owner.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 143 | Native: False | Pure (no side effects): False

- Categories: linkset


## llBreakLink

```lsl
void llBreakLink(integer link)
```

- Purpose: Delinks the prim specified by the link number link. Requires the PERMISSION_CHANGE_LINKS runtime permission.

- Argument `link` (integer): The link number (0: unlinked, 1: root prim, >1: child prims and seated avatars) to delink.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 142 | Native: False | Pure (no side effects): False

- Categories: linkset


## llCSV2List

```lsl
list llCSV2List(string src)
```

- Purpose: Parses the comma-separated string src and returns it as a list.

- Argument `src` (string): String of comma-separated values to parse.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 196 | Native: False | Pure (no side effects): True

- Categories: data_conversion


## llCastRay

```lsl
list llCastRay(vector start_pos, vector end_pos, list options)
```

- Purpose: Casts a ray into the physics world from start to end and reports collision data for intersections with objects based on options. Returns a list of strided values [UUID_1, {link_number_1}, hit_position_1, {hit_normal_1}, ..., status_code]. A negative status_code indicates an error; otherwise, it represents the number of hits.

- Argument `start_pos` (vector): Starting location vector of the ray.

- Argument `end_pos` (vector): Ending location vector of the ray.

- Argument `options` (list): A list of option flags and their parameters to configure the raycast.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 363 | Native: False | Pure (no side effects): False

- Categories: physics, sensor


## llCeil

```lsl
integer llCeil(float val)
```

- Purpose: Returns val rounded toward positive infinity. In other words, returns the smallest integer greater than or equal to val.

- Argument `val` (float): Number to round up.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 10 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.ceil`. Fastcall.


## llChar

```lsl
string llChar(integer val)
```

- Purpose: Constructs and returns a single-character string from the given Unicode codepoint ordinal.

- Argument `val` (integer): Unicode codepoint integer (ordinal) to convert.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 526 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llClearCameraParams

```lsl
void llClearCameraParams()
```

- Purpose: Resets all camera parameters to default values and turns off scripted camera control. Requires the PERMISSION_CONTROL_CAMERA runtime permission (automatically granted for attached or sat-on objects).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 314 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llClearExperience

```lsl
void llClearExperience(key agentid, key experienceid)
```

- Argument `agentid` (key): 

- Argument `experienceid` (key): 

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 411 | Native: False | Pure (no side effects): False

- Categories: experience

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.

- Deprecated in LSL: True


## llClearExperiencePermissions

```lsl
void llClearExperiencePermissions(key agentid)
```

- Argument `agentid` (key): 

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 385 | Native: False | Pure (no side effects): False

- Categories: experience

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.

- Deprecated in LSL: True


## llClearLinkMedia

```lsl
integer llClearLinkMedia(integer link, integer face)
```

- Purpose: Deletes the media and clears all parameters from the given face on the linked prim. Returns an integer STATUS_* flag detailing the success or failure of the operation.

- Argument `link` (integer): The link number (0: unlinked, 1: root prim, >1: child prims) or a LINK_* flag representing the target prim.

- Argument `face` (integer): Face number to clear.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 373 | Native: False | Pure (no side effects): False

- Categories: linkset, media, prim_media


## llClearPrimMedia

```lsl
integer llClearPrimMedia(integer face)
```

- Purpose: Deletes the media and clears all parameters from the specified face. Returns an integer STATUS_* flag detailing the success or failure of the operation.

- Argument `face` (integer): Face number (side) to clear.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 352 | Native: False | Pure (no side effects): False

- Categories: media, prim, prim_media

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llCloseRemoteDataChannel

```lsl
void llCloseRemoteDataChannel(key channel)
```

- Purpose: Deprecated. Closes the specified XML-RPC channel.

- Argument `channel` (key): XML-RPC channel ID to close.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 257 | Native: False | Pure (no side effects): False

- Categories: script_communication

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: True


## llCloud

```lsl
float llCloud(vector offset)
```

- Purpose: Returns a float representing the cloud density at the prim's position offset by the vector offset.

- Argument `offset` (vector): Offset relative to the prim's position, expressed in local coordinates.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 43 | Native: False | Pure (no side effects): False

- Categories: region

- Deprecated in LSL: True


## llCollisionFilter

```lsl
void llCollisionFilter(string name, key id, integer accept)
```

- Purpose: Sets the collision filter, either exclusively or inclusively. If accept is TRUE, only collisions matching name and id are processed; if FALSE, matches are excluded. Pass an empty string or NULL_KEY to name or id to skip filtering on that parameter.

- Argument `name` (string): Specific object name or avatar legacy name to filter for.

- Argument `id` (key): Group, avatar, or object UUID to filter by.

- Argument `accept` (integer): Boolean. If TRUE, only collisions matching the name and id filters are processed; if FALSE, matching collisions are excluded.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 110 | Native: False | Pure (no side effects): False

- Categories: physics, sensor


## llCollisionSound

```lsl
void llCollisionSound(string impact_sound, float impact_volume)
```

- Purpose: Suppresses default collision sounds and replaces default impact sounds with impact_sound at the volume level specified by impact_volume. Supply an empty string to only suppress collision sounds.

- Argument `impact_sound` (string): UUID of a sound, the name of a sound in the prim's inventory, or an empty string to suppress sounds.

- Argument `impact_volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 160 | Native: False | Pure (no side effects): False

- Categories: physics, sound


## llCollisionSprite

```lsl
void llCollisionSprite(string impact_sprite)
```

- Purpose: Suppresses default collision sprites and replaces them with impact_sprite (which must be in the prim's inventory). Supply an empty string to only suppress collision sprites.

- Argument `impact_sprite` (string): UUID of a texture, the name of a texture in the prim's inventory, or an empty string to suppress sprites.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 161 | Native: False | Pure (no side effects): False

- Categories: effects, sound

- Deprecated in LSL: True


## llComputeHash

```lsl
string llComputeHash(string message, string algorithm)
```

- Purpose: Returns a hex-encoded hash digest string of message using the specified cryptographic algorithm.

- Argument `message` (string): Message string to be hashed.

- Argument `algorithm` (string): Cryptographic digest algorithm to use (e.g., md5, sha1, sha224, sha256, sha384, or sha512).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 548 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llCos

```lsl
float llCos(float theta)
```

- Purpose: Returns the cosine of theta. Theta is in radians.

- Argument `theta` (float): Angle in radians.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 1 | Native: True | Pure (no side effects): True

- Categories: math, math_trig

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.cos`. Double precision; fastcall.


## llCreateCharacter

```lsl
void llCreateCharacter(list options)
```

- Purpose: Converts the linkset containing the script into a pathfinding character entity (required to use pathfinding functions) using the specified options.

- Argument `options` (list): A list of key-value pairs specifying the character's configuration options.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 399 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llCreateKeyValue

```lsl
key llCreateKeyValue(string k, string v)
```

- Purpose: Starts an asynchronous transaction to create a key-value pair (k and v) associated with the script's experience. Returns a key query handle for the dataserver event. Fails with XP_ERROR_STORAGE_EXCEPTION if the key already exists.

- Argument `k` (string): Unique key name for the key-value pair.

- Argument `v` (string): Value for the key-value pair (maximum 2047 characters, or 4095 characters if using Mono).

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 387 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, experience, experience_data

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llCreateLink

```lsl
void llCreateLink(key target, integer parent)
```

- Purpose: Attempts to link the object containing the script with target. Requires the PERMISSION_CHANGE_LINKS runtime permission.

- Argument `target` (key): UUID of the target prim/object in the same region.

- Argument `parent` (integer): Boolean. If TRUE, the script's object becomes the root prim; if FALSE, target becomes the root.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 141 | Native: False | Pure (no side effects): False

- Categories: linkset

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llDamage

```lsl
void llDamage(key target, float damage, integer damage_type)
```

- Purpose: Generates a damage event delivering the specified amount of damage and damage_type to the targeted avatar or task in the same region.

- Argument `target` (key): Key of the target avatar or task to receive damage.

- Argument `damage` (float): Amount of damage to inflict (can exceed 100, unlike collision-based damage).

- Argument `damage_type` (integer): Type of damage to deliver to the target (can correspond to a DAMAGE_TYPE_* constant).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 671 | Native: False | Pure (no side effects): False

- Categories: combat


## llDataSizeKeyValue

```lsl
key llDataSizeKeyValue()
```

- Purpose: Starts an asynchronous transaction to request the used and total data storage allocated for the experience. Returns a key query handle for the dataserver event.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 600 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, experience, experience_data

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llDeleteCharacter

```lsl
void llDeleteCharacter()
```

- Purpose: Converts the linkset back to a standard physical object, removing all pathfinding properties.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 405 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llDeleteKeyValue

```lsl
key llDeleteKeyValue(string k)
```

- Purpose: Starts an asynchronous transaction to delete the key-value pair associated with key k in the experience. Returns a key query handle for the dataserver event.

- Argument `k` (string): Key of the key-value pair to delete.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 390 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, experience, experience_data

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llDeleteSubList

```lsl
list llDeleteSubList(list src, integer start_index, integer end_index)
```

- Purpose: Returns a copy of the list src with the slice from start_index to end_index (inclusive) removed. Negative indices count backward from the end of the list. If start_index is greater than end_index, the deletion excludes the specified range.

- Argument `src` (list): Source list to copy and modify.

- Argument `start_index` (integer): Starting index of the slice to remove (inclusive).

- Argument `end_index` (integer): Ending index of the slice to remove (inclusive).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 193 | Native: True | Pure (no side effects): True

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `table.remove`. Unnecessary table copying.


## llDeleteSubString

```lsl
string llDeleteSubString(string src, integer start_index, integer end_index)
```

- Purpose: Returns a copy of the string src with the characters from start_index to end_index (inclusive) removed. Negative indices count backward from the end of the string. If start_index is greater than end_index, the deletion excludes the specified range.

- Argument `src` (string): Source string to modify.

- Argument `start_index` (integer): Starting codepoint index of the substring to remove (inclusive). Supports negative indexing.

- Argument `end_index` (integer): Ending codepoint index of the substring to remove (inclusive). Supports negative indexing.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 95 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llDerezObject

```lsl
integer llDerezObject(key id, integer flags)
```

- Purpose: Derezzes (deletes or returns) a targeted object in the region previously rezzed by a script in this linkset, returning TRUE on success or FALSE on failure.

- Argument `id` (key): UUID of the object in the region to derez.

- Argument `flags` (integer): Derez behavior flags matching DEREZ_* constants.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 509 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, rez


## llDetachFromAvatar

```lsl
void llDetachFromAvatar()
```

- Purpose: Detaches the object containing the script from the avatar. Requires the PERMISSION_ATTACH runtime permission (automatically granted to attached objects). Note that the detached object is completely removed from the region and not dropped on the ground.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 114 | Native: False | Pure (no side effects): False

- Categories: attachments, avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llDetectedDamage

```lsl
list llDetectedDamage(integer number)
```

- Purpose: Returns a list containing pending damage information for the event specified by number, including the current damage, the damage type, and the original damage delivered.

- Argument `number` (integer): Index of the detection information.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 554 | Native: False | Pure (no side effects): False

- Categories: combat, detected


## llDetectedGrab

```lsl
vector llDetectedGrab(integer number)
```

- Purpose: Returns a vector representing the grab offset of the user touching the object. Only works in touch events and returns <0.0, 0.0, 0.0> if number is not a valid index.

- Argument `number` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 37 | Native: False | Pure (no side effects): False

- Categories: detected, touch


## llDetectedGroup

```lsl
integer llDetectedGroup(integer number)
```

- Purpose: Returns TRUE if the detected object or avatar specified by number has the same active group as the prim containing the script. Returns FALSE if the group is not active or if they are not in the group.

- Argument `number` (integer): Index of the detection information.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 39 | Native: False | Pure (no side effects): False

- Categories: detected


## llDetectedKey

```lsl
key llDetectedKey(integer number)
```

- Purpose: Returns the key (UUID) of the detected object or avatar specified by number, or NULL_KEY if number is not a valid index.

- Argument `number` (integer): Index of the detection information.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 32 | Native: False | Pure (no side effects): False

- Categories: detected, uuid


## llDetectedLinkNumber

```lsl
integer llDetectedLinkNumber(integer number)
```

- Purpose: Returns the link number (integer) of the triggered event (touches and collisions only) specified by number. Returns 0 for non-linked objects, 1 for the root prim, and 2+ for child prims. Returns 0 if not supported by the event.

- Argument `number` (integer): Index of the detection information.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 40 | Native: False | Pure (no side effects): False

- Categories: detected


## llDetectedName

```lsl
string llDetectedName(integer item)
```

- Purpose: Returns a string representing the name of the detected object or avatar specified by item. Returns an empty string if item is not a valid index.

- Argument `item` (integer): Index of the detection information.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 31 | Native: False | Pure (no side effects): False

- Categories: detected


## llDetectedOwner

```lsl
key llDetectedOwner(integer number)
```

- Purpose: Returns the key (UUID) of the owner of the detected object specified by number. Returns an invalid key if number is not a valid index.

- Argument `number` (integer): Index of the detection information.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 33 | Native: False | Pure (no side effects): False

- Categories: avatar, detected

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llDetectedPos

```lsl
vector llDetectedPos(integer number)
```

- Purpose: Returns the vector position (in region coordinates) of the detected object or avatar specified by number, or <0.0, 0.0, 0.0> if number is not a valid index.

- Argument `number` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 35 | Native: False | Pure (no side effects): False

- Categories: detected


## llDetectedRezzer

```lsl
key llDetectedRezzer(integer number)
```

- Purpose: Returns the key (UUID) of the object or avatar that rezzed the detected object specified by number.

- Argument `number` (integer): Index of the detection information.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 553 | Native: False | Pure (no side effects): False

- Categories: detected


## llDetectedRot

```lsl
rotation llDetectedRot(integer number)
```

- Purpose: Returns the rotation of the detected object or avatar specified by number, or <0.0, 0.0, 0.0, 1.0> if number is not a valid offset index.

- Argument `number` (integer): Index of the detection information.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 38 | Native: False | Pure (no side effects): False

- Categories: detected


## llDetectedTouchBinormal

```lsl
vector llDetectedTouchBinormal(integer index)
```

- Purpose: Returns the surface binormal vector (tangent to the surface, pointing along the positive T (V) direction of tangent space) at the touched location specified by index. Can be used with llDetectedTouchNormal to determine the tangent space.

- Argument `index` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 341 | Native: False | Pure (no side effects): False

- Categories: detected, touch


## llDetectedTouchFace

```lsl
integer llDetectedTouchFace(integer index)
```

- Purpose: Returns the integer index of the face clicked by the avatar in the touch event specified by index.

- Argument `index` (integer): Index of the detection information.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 338 | Native: False | Pure (no side effects): False

- Categories: detected, touch


## llDetectedTouchNormal

```lsl
vector llDetectedTouchNormal(integer index)
```

- Purpose: Returns the surface normal vector (perpendicular to the surface) at the touched location specified by index. Can be used with llDetectedTouchBinormal to determine the tangent space.

- Argument `index` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 340 | Native: False | Pure (no side effects): False

- Categories: detected, touch


## llDetectedTouchPos

```lsl
vector llDetectedTouchPos(integer index)
```

- Purpose: Returns the vector position where the object was touched (specified by index) in region coordinates, or in screen-space coordinates if the object is attached as a HUD.

- Argument `index` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 339 | Native: False | Pure (no side effects): False

- Categories: detected, touch


## llDetectedTouchST

```lsl
vector llDetectedTouchST(integer index)
```

- Purpose: Returns the surface coordinates (<s, t, 0.0>) where the prim was touched, specified by index. X and Y contain the horizontal (s) and vertical (t) face coordinates, typically in the interval [0.0, 1.0]. Returns TOUCH_INVALID_TEXCOORD if coordinates cannot be determined.

- Argument `index` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 342 | Native: False | Pure (no side effects): False

- Categories: detected, touch


## llDetectedTouchUV

```lsl
vector llDetectedTouchUV(integer index)
```

- Purpose: Returns the texture coordinates (<u, v, 0.0>) where the prim was touched, specified by index. X and Y contain the horizontal (u) and vertical (v) texture coordinates, typically in the interval [0.0, 1.0] (affected by repeats and rotation). Returns TOUCH_INVALID_TEXCOORD if coordinates cannot be determined.

- Argument `index` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 337 | Native: False | Pure (no side effects): False

- Categories: detected, touch


## llDetectedType

```lsl
integer llDetectedType(integer number)
```

- Purpose: Returns an integer bitfield representing the types (AGENT, ACTIVE, PASSIVE, or SCRIPTED) of the detected object or avatar specified by number. Returns 0 if number is not a valid index.

- Argument `number` (integer): Index of the detection information.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 34 | Native: False | Pure (no side effects): False

- Categories: detected


## llDetectedVel

```lsl
vector llDetectedVel(integer number)
```

- Purpose: Returns the vector velocity of the detected object or avatar specified by number, or <0.0, 0.0, 0.0> if number is not a valid offset index.

- Argument `number` (integer): Index of the detection information.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 36 | Native: False | Pure (no side effects): False

- Categories: detected


## llDialog

```lsl
void llDialog(key agent, string msg, list buttons, integer channel)
```

- Purpose: Shows a dialog box on the screen of the specified agent, displaying msg along with up to 12 choice buttons. Clicking a button chats its label on channel. The chat originates at the object's position, but uses the agent's name and UUID, so it can be heard as long as the agent is still in the region.

- Argument `agent` (key): UUID of the agent in the same region.

- Argument `msg` (string): Text message to display in the dialog box.

- Argument `buttons` (list): A list of up to 12 strings representing button labels.

- Argument `channel` (integer): Output chat channel (any 32-bit signed integer value) where button clicks are chatted.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 247 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, user_interface

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llDie

```lsl
void llDie()
```

- Purpose: Deletes the entire object containing the script (the object does not go to inventory). Use llBreakLink first to delete only a single prim.

- Returns: void

- Energy cost: 0.0 | Script sleep after call: 0.0 s | Function ID: 41 | Native: False | Pure (no side effects): False

- Categories: rez


## llDumpList2String

```lsl
string llDumpList2String(list src, string separator)
```

- Purpose: Returns a string that is the list src converted to a single string, with separator placed between each entry.

- Argument `src` (list): Source list to convert.

- Argument `separator` (string): Separator string to place between list entries.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 245 | Native: True | Pure (no side effects): False

- Categories: data_conversion


## llEdgeOfWorld

```lsl
integer llEdgeOfWorld(vector pos, vector dir)
```

- Purpose: Checks if the border reached along the vector dir from the vector pos is the edge of the world (i.e., has no neighboring simulator). Returns TRUE if it hits the edge of the world, or FALSE if there is a neighboring simulator.

- Argument `pos` (vector): Position vector in region coordinates.

- Argument `dir` (vector): Direction vector.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 205 | Native: False | Pure (no side effects): False

- Categories: region


## llEjectFromLand

```lsl
void llEjectFromLand(key avatar)
```

- Purpose: Ejects the specified avatar from land/parcels owned by the object's owner (group or resident).

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 213 | Native: False | Pure (no side effects): False

- Categories: land_moderation, parcel


## llEmail

```lsl
void llEmail(string address, string subject, string msg)
```

- Purpose: Sends an email with the given destination address, subject, and body msg. The email will be sent from `{ll.GetKey()}@lsl.secondlife.com`. This can be used for script communication; see llGetNextEmail()

- Argument `address` (string): Destination email address.

- Argument `subject` (string): Subject of the email.

- Argument `msg` (string): Message body of the email.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 20.0 s | Function ID: 119 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, script_communication

- Delay warning: this call sleeps the script for 20.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llEscapeURL

```lsl
string llEscapeURL(string url)
```

- Purpose: Returns a string representing the escaped/encoded version of url, replacing spaces with '%20' and non-alphanumeric characters with their '%xx' hexadecimal UTF-8 equivalent.

- Argument `url` (string): Unescaped URL string to escape.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 307 | Native: False | Pure (no side effects): True

- Categories: web


## llEuler2Rot

```lsl
rotation llEuler2Rot(vector vec)
```

- Purpose: Returns the quaternion representation of the Euler angles (in radians) within vec.

- Argument `vec` (vector): Vector of Euler angles to convert, in radians.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 16 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, quaternion

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llEvade

```lsl
void llEvade(key target, list options)
```

- Purpose: Directs a pathfinding character to evade target, attempting to hide from its pursuer if a hiding spot is available (i.e., no line of sight from the character's head to the pursuer's head, and no direct path on the navmesh).

- Argument `target` (key): UUID of the group, avatar, or object to evade.

- Argument `options` (list): No options currently available (should be empty list).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 407 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llExecCharacterCmd

```lsl
void llExecCharacterCmd(integer command, list options)
```

- Purpose: Sends a command (specified by command) to the pathing system with options. Currently only supports stopping pathfinding or making the character jump.

- Argument `command` (integer): Pathfinding command to execute.

- Argument `options` (list): A list of options for the command (e.g., jump height for CHARACTER_CMD_JUMP).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 404 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llFabs

```lsl
float llFabs(float val)
```

- Purpose: Returns the absolute (positive) value of val.

- Argument `val` (float): Number to convert.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 7 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.abs`. Double precision; fastcall.


## llFindNotecardTextCount

```lsl
key llFindNotecardTextCount(string name, string pattern, list options)
```

- Purpose: Asynchronously requests the number of matches of pattern in the notecard name. Returns a key query handle for the dataserver event.

- Argument `name` (string): Name of the notecard in the prim's inventory, or a UUID.

- Argument `pattern` (string): Regular expression pattern to search for.

- Argument `options` (list): A list of options to control the search (currently unused, should be []).

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 507 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, notecard


## llFindNotecardTextSync

```lsl
list llFindNotecardTextSync(string name, string pattern, integer start, integer count, list options)
```

- Purpose: Synchronously searches the notecard name in the region's cache for matches of pattern, without raising a dataserver event. Returns a strided list of the form [line, column, length, ...] with one stride per match, a list containing NAK if the notecard is not cached, or an empty list if there are no matches.

- Argument `name` (string): Name of the notecard in the prim's inventory, or a UUID.

- Argument `pattern` (string): Regular expression pattern to search for.

- Argument `start` (integer): Index of the first match to return.

- Argument `count` (integer): Maximum number of matches to return (if 0, returns the first 64 matches).

- Argument `options` (list): A list of options to control the search (currently unused, should be []).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 508 | Native: False | Pure (no side effects): False

- Categories: data_storage, notecard


## llFleeFrom

```lsl
void llFleeFrom(vector position, float distance, list options)
```

- Purpose: Directs a pathfinding character to keep the specified distance from the target position vector (within the region or adjacent regions).

- Argument `position` (vector): Position vector in region coordinates from which to flee.

- Argument `distance` (float): Distance in meters to keep from the position.

- Argument `options` (list): No options currently available (should be empty list).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 402 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llFloor

```lsl
integer llFloor(float val)
```

- Purpose: Returns val rounded toward negative infinity. In other words, returns the largest integer less than or equal to val.

- Argument `val` (float): Number to round down.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 9 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.floor`. Fastcall.


## llForceMouselook

```lsl
void llForceMouselook(integer mouselook)
```

- Purpose: Sets whether any avatar sitting on this prim is forced into mouselook mode. Setting mouselook to TRUE forces the mode; FALSE (default) allows the avatar to keep their current camera mode.

- Argument `mouselook` (integer): Boolean. If TRUE, forces a sitting avatar into mouselook; if FALSE, allows them to keep their current camera mode.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 294 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llFrand

```lsl
float llFrand(float mag)
```

- Purpose: Returns a pseudo-random float in the range [0.0, mag) or (mag, 0.0] depending on the sign of mag. The value is inclusive of 0.0 but exclusive of mag.

- Argument `mag` (float): Float magnitude of the random range.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 8 | Native: False | Pure (no side effects): False

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llGenerateKey

```lsl
key llGenerateKey()
```

- Purpose: Generates and returns a unique versioned UUID key (utilizing SHA-1 hashing). Due to being versioned, it will not return NULL_KEY; however, the exact UUID version is an implementation detail that should not be relied upon.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 383 | Native: False | Pure (no side effects): False

- Categories: uuid


## llGetAccel

```lsl
vector llGetAccel()
```

- Purpose: Returns a vector representing the acceleration of the object in the region's frame of reference.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 78 | Native: False | Pure (no side effects): False

- Categories: physics


## llGetAgentInfo

```lsl
integer llGetAgentInfo(key id)
```

- Purpose: Returns an integer bitfield containing status information about the agent specified by id (such as AGENT_FLYING, AGENT_ATTACHMENTS, AGENT_SITTING, etc.).

- Argument `id` (key): UUID of the avatar in the same region.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 206 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAgentLanguage

```lsl
string llGetAgentLanguage(key avatar)
```

- Purpose: Returns a string representing the language code of the preferred interface language set by the avatar.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 336 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAgentList

```lsl
list llGetAgentList(integer scope, list options)
```

- Purpose: Requests a list of avatar UUID keys for agents currently in the region, limited by scope. Returns a list of keys or a list containing an error message string.

- Argument `scope` (integer): Scope flag (AGENT_LIST_PARCEL, AGENT_LIST_PARCEL_OWNER, or AGENT_LIST_REGION) to filter the returned agents.

- Argument `options` (list): A list of options to apply (currently unused).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 412 | Native: False | Pure (no side effects): False

- Categories: avatar, parcel, region

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAgentSize

```lsl
vector llGetAgentSize(key avatar)
```

- Purpose: Returns a vector representing the estimated bounding box size of the specified avatar, or ZERO_VECTOR if they are not in the same region.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 218 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAlpha

```lsl
float llGetAlpha(integer face)
```

- Purpose: Returns a float representing the Blinn-Phong alpha (transparency) of face. If face is ALL_SIDES, returns the mean average of all faces.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 50 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetAndResetTime

```lsl
float llGetAndResetTime()
```

- Purpose: Returns the elapsed script time in seconds as a float, then resets the script timer to zero.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 84 | Native: False | Pure (no side effects): False

- Categories: script


## llGetAnimation

```lsl
string llGetAnimation(key avatar)
```

- Purpose: Returns a string representing the name of the currently playing locomotion animation for the specified avatar.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 162 | Native: False | Pure (no side effects): False

- Categories: avatar, avatar_animation, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAnimationList

```lsl
list llGetAnimationList(key avatar)
```

- Purpose: Returns a list of keys (UUIDs) representing all active animations currently playing on the specified avatar.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 266 | Native: False | Pure (no side effects): False

- Categories: avatar, avatar_animation, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAnimationOverride

```lsl
string llGetAnimationOverride(string anim_state)
```

- Purpose: Returns a string representing the name of the animation currently overriding the specified anim_state. Requires the PERMISSION_OVERRIDE_ANIMATIONS or PERMISSION_TRIGGER_ANIMATION runtime permission.

- Argument `anim_state` (string): Animation state string to query.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 500 | Native: False | Pure (no side effects): False

- Categories: avatar, avatar_animation, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAttached

```lsl
integer llGetAttached()
```

- Purpose: Returns the integer attachment point (an ATTACH_* constant) that the object is attached to, or 0 if it is unattached or pending detachment.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 224 | Native: False | Pure (no side effects): False

- Categories: attachments


## llGetAttachedList

```lsl
list llGetAttachedList(key avatar)
```

- Purpose: Returns a list of object keys (UUIDs) worn by the specified avatar, in the order they were attached. HUDs are not included because they are neither public nor visible. Returns a list containing an error message string on failure.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 523 | Native: False | Pure (no side effects): False

- Categories: attachments, avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetAttachedListFiltered

```lsl
list llGetAttachedListFiltered(key avatar, list options)
```

- Purpose: Returns a list of object keys (UUIDs) worn by the specified avatar, in the order they were attached, filtered by options. Returns a list containing an error message string on failure.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Argument `options` (list): A list of options to filter the returned attachments.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 518 | Native: False | Pure (no side effects): False

- Categories: attachments, avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetBoundingBox

```lsl
list llGetBoundingBox(key object)
```

- Purpose: Returns the bounding box of object (including any linked prims) relative to its root prim in local coordinates, formatted as [ (vector) min_corner, (vector) max_corner ].

- Argument `object` (key): UUID of the avatar or prim in the same region.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 277 | Native: False | Pure (no side effects): False

- Categories: object

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llGetCameraAspect

```lsl
float llGetCameraAspect()
```

- Purpose: Returns a float representing the camera's current aspect ratio (width/height) of the agent who granted PERMISSION_TRACK_CAMERA. Returns 0.0 if permissions are not granted.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 545 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetCameraFOV

```lsl
float llGetCameraFOV()
```

- Purpose: Returns a float representing the camera's current field of view (FOV) in radians of the agent who granted PERMISSION_TRACK_CAMERA. Returns 0.0 if permissions are not granted.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 546 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetCameraPos

```lsl
vector llGetCameraPos()
```

- Purpose: Returns a vector representing the camera's current position in region coordinates of the agent who granted PERMISSION_TRACK_CAMERA. Returns ZERO_VECTOR if permissions are not granted.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 303 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetCameraRot

```lsl
rotation llGetCameraRot()
```

- Purpose: Returns a rotation representing the camera's current orientation of the agent who granted PERMISSION_TRACK_CAMERA. Returns ZERO_ROTATION if permissions are not granted.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 304 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetCenterOfMass

```lsl
vector llGetCenterOfMass()
```

- Purpose: Returns the vector position (in region coordinates) of the center of mass. Returns the individual child prim's center of mass if called from a child, or the entire linkset's center of mass if called from the root.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 183 | Native: False | Pure (no side effects): False

- Categories: object, physics

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llGetClosestNavPoint

```lsl
list llGetClosestNavPoint(vector point, list options)
```

- Purpose: Returns a list containing the closest vector position on the navigation mesh (navmesh) to the specified point (expressed in region-local space), or an empty list if none is found. Configured using options.

- Argument `point` (vector): Position vector in region-local coordinates.

- Argument `options` (list): A list of GCNP_* flags and parameters to configure the search limits.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 408 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llGetColor

```lsl
vector llGetColor(integer face)
```

- Purpose: Returns the Blinn-Phong RGB color vector of face (values between 0.0 and 1.0). If face is ALL_SIDES, returns the mean average of all faces.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 52 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetCreator

```lsl
key llGetCreator()
```

- Purpose: Returns the key (UUID) of the prim's original creator.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 272 | Native: False | Pure (no side effects): False

- Categories: prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetDate

```lsl
string llGetDate()
```

- Purpose: Returns a string representing the current date in the UTC time zone in the format 'YYYY-MM-DD'.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 204 | Native: False | Pure (no side effects): False

- Categories: time


## llGetDayLength

```lsl
integer llGetDayLength()
```

- Purpose: Returns an integer representing the number of seconds in the environmental day cycle applied to the current parcel.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 703 | Native: False | Pure (no side effects): False

- Categories: time


## llGetDayOffset

```lsl
integer llGetDayOffset()
```

- Purpose: Returns an integer representing the offset duration (in seconds) added to calculate the current environmental time on this parcel.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 705 | Native: False | Pure (no side effects): False

- Categories: time


## llGetDisplayName

```lsl
string llGetDisplayName(key id)
```

- Purpose: Returns the display name string of the avatar specified by id if they are in the region or cached; returns an empty string otherwise (use llRequestDisplayName if the avatar is absent).

- Argument `id` (key): UUID of the avatar in the same region or otherwise known to the region.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 360 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetEnergy

```lsl
float llGetEnergy()
```

- Purpose: Returns a float representing the remaining physics energy of the object as a percentage (0.0 to 1.0) of its maximum capacity.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 149 | Native: False | Pure (no side effects): False

- Categories: script


## llGetEnv

```lsl
string llGetEnv(string name)
```

- Purpose: Returns a string containing the requested regional data specified by name.

- Argument `name` (string): Name of the regional data to request (unrecognized strings return an empty string).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 362 | Native: False | Pure (no side effects): False

- Categories: region


## llGetEnvironment

```lsl
list llGetEnvironment(vector pos, list params)
```

- Purpose: Returns a list containing the current environment parameters for the parcel or region at pos, retrieved in the order specified by params.

- Argument `pos` (vector): Position vector in region coordinates (X/Y determine the parcel, or region if X/Y are -1; Z determines the sky track altitude).

- Argument `params` (list): A list of environmental attributes to retrieve.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 711 | Native: False | Pure (no side effects): False

- Categories: parcel, parcel_appearance


## llGetExperienceDetails

```lsl
list llGetExperienceDetails(key experience_id)
```

- Purpose: Returns a list of details for the specified experience_id, formatted as [string experience_name, key owner_id, key experience_id, integer state, string state_message, key group_id].

- Argument `experience_id` (key): UUID of the experience to query (can be NULL_KEY to retrieve details for the script's own experience).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 409 | Native: False | Pure (no side effects): False

- Categories: experience

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llGetExperienceErrorMessage

```lsl
string llGetExperienceErrorMessage(integer error)
```

- Purpose: Returns a text description of the specified experience error code, or a description of XP_ERROR_UNKNOWN_ERROR if the error is invalid.

- Argument `error` (integer): XP_ERROR_* error code constant to translate.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 603 | Native: False | Pure (no side effects): False

- Categories: experience

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llGetExperienceList

```lsl
list llGetExperienceList(key agentid)
```

- Argument `agentid` (key): 

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 410 | Native: False | Pure (no side effects): False

- Categories: experience

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.

- Deprecated in LSL: True


## llGetForce

```lsl
vector llGetForce()
```

- Purpose: Returns a vector representing the constant force currently applied to the object (if the object is physical).

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 65 | Native: False | Pure (no side effects): False

- Categories: physics


## llGetFreeMemory

```lsl
integer llGetFreeMemory()
```

- Purpose: Returns an integer representing the number of free bytes of memory currently available to the script.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 225 | Native: False | Pure (no side effects): False

- Categories: script


## llGetFreeURLs

```lsl
integer llGetFreeURLs()
```

- Purpose: Returns an integer representing the number of available HTTP URLs (remaining for the owner if the object is attached, or for the region if unattached).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 344 | Native: False | Pure (no side effects): False

- Categories: script, web


## llGetGMTclock

```lsl
float llGetGMTclock()
```

- Purpose: Returns a float representing the time in seconds since midnight GMT (truncated to whole seconds).

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 282 | Native: False | Pure (no side effects): False

- Categories: time


## llGetGameControlMode

```lsl
integer llGetGameControlMode(key id)
```

- Purpose: Returns a GAME_CONTROL_MODE_* integer indicating the current game-control mode for the avatar specified by id.

- Argument `id` (key): UUID of the avatar whose game-controller state to query.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 804 | Native: False | Pure (no side effects): False

- Categories: avatar, game_control, input

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetGameControlModeAxes

```lsl
list llGetGameControlModeAxes(key id)
```

- Purpose: Returns a list of floats representing the modal axes for the current game-control mode of the avatar specified by id. Element count and index meanings vary by mode; use the GAME_CONTROL_AXIS_* constants as indices.

- Argument `id` (key): UUID of the avatar whose game-controller state to query.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 806 | Native: False | Pure (no side effects): False

- Categories: avatar, game_control, input

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetGameControlModeButtons

```lsl
integer llGetGameControlModeButtons(key id)
```

- Purpose: Returns a bitmask of the modal buttons currently active for the current game-control mode of the avatar specified by id. Bit meanings vary by mode; use the GAME_CONTROL_BUTTON_* constants as masks.

- Argument `id` (key): UUID of the avatar whose game-controller state to query.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 805 | Native: False | Pure (no side effects): False

- Categories: avatar, game_control, input

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetGeometricCenter

```lsl
vector llGetGeometricCenter()
```

- Purpose: Returns a vector representing the geometric center of the object relative to its root prim.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 278 | Native: False | Pure (no side effects): False

- Categories: physics


## llGetHTTPHeader

```lsl
string llGetHTTPHeader(key request_id, string header)
```

- Purpose: Returns a string representing the value of the specified header associated with the HTTP request_id.

- Argument `request_id` (key): Unique key of the HTTP request.

- Argument `header` (string): Lowercase name of the HTTP header to retrieve.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 349 | Native: False | Pure (no side effects): False

- Categories: web


## llGetHealth

```lsl
float llGetHealth(key id)
```

- Purpose: Returns a float representing the current health of the avatar or object specified by id.

- Argument `id` (key): UUID of the agent or object to query.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 552 | Native: False | Pure (no side effects): False

- Categories: combat


## llGetInventoryAcquireTime

```lsl
string llGetInventoryAcquireTime(string item)
```

- Purpose: Returns the time when the item was placed in the prim's inventory, as a UTC timestamp string of the form "YYYY-MM-DDThh:mm:ssZ"

- Argument `item` (string): Name of the item in the prim's inventory.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 529 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llGetInventoryCreator

```lsl
key llGetInventoryCreator(string item)
```

- Purpose: Returns the key (UUID) of the creator of the specified inventory item.

- Argument `item` (string): Name of the item in the prim's inventory.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 291 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llGetInventoryDesc

```lsl
string llGetInventoryDesc(string item)
```

- Purpose: Returns the description string of the specified inventory item.

- Argument `item` (string): Name of the item in the prim's inventory.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 543 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llGetInventoryKey

```lsl
key llGetInventoryKey(string item)
```

- Purpose: Returns the key (UUID) of the specified inventory item.

- Argument `item` (string): Name of the item in the prim's inventory.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 175 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llGetInventoryName

```lsl
string llGetInventoryName(integer type, integer index)
```

- Purpose: Returns the name of the inventory item of the specified type (INVENTORY_*) at the specified inventory index.

- Argument `type` (integer): INVENTORY_* type constant of the item.

- Argument `index` (integer): Index of the item of that type.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 147 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llGetInventoryNumber

```lsl
integer llGetInventoryNumber(integer type)
```

- Purpose: Returns the count of items of the specified type (INVENTORY_*) in the prim's inventory.

- Argument `type` (integer): INVENTORY_* type constant to count.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 146 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llGetInventoryPermMask

```lsl
integer llGetInventoryPermMask(string item, integer group)
```

- Purpose: Returns the specified item's permission flags for the specified group.

- Argument `item` (string): Name of the item in the prim's inventory.

- Argument `group` (integer): MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to get.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 289 | Native: False | Pure (no side effects): False

- Categories: asset_permissions, prim_inventory


## llGetInventoryType

```lsl
integer llGetInventoryType(string item)
```

- Purpose: Returns an integer representing the INVENTORY_* type of the named inventory item.

- Argument `item` (string): Name of the item in the prim's inventory.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 301 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llGetKey

```lsl
key llGetKey()
```

- Purpose: Returns the key (UUID) of the prim containing the script.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 121 | Native: False | Pure (no side effects): False

- Categories: prim, uuid

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetLandOwnerAt

```lsl
key llGetLandOwnerAt(vector pos)
```

- Purpose: Returns the key (UUID) of the land owner at the vector pos, or NULL_KEY if the land is public.

- Argument `pos` (vector): Position vector in region coordinates.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 216 | Native: False | Pure (no side effects): False

- Categories: parcel


## llGetLinkKey

```lsl
key llGetLinkKey(integer link)
```

- Purpose: Returns the key (UUID) of the linked prim or avatar specified by link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 144 | Native: False | Pure (no side effects): False

- Categories: linkset, uuid


## llGetLinkMedia

```lsl
list llGetLinkMedia(integer link, integer face, list params)
```

- Purpose: Returns a list containing the media parameters of the specified face on the linked prim link, retrieved in the order requested by params.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `face` (integer): Face number (side) of the prim.

- Argument `params` (list): A list of PRIM_MEDIA_* property constants to retrieve values for.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 372 | Native: False | Pure (no side effects): False

- Categories: linkset, media, prim_media


## llGetLinkName

```lsl
string llGetLinkName(integer link)
```

- Purpose: Returns a string containing the name of the linked prim specified by link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 145 | Native: False | Pure (no side effects): False

- Categories: linkset


## llGetLinkNumber

```lsl
integer llGetLinkNumber()
```

- Purpose: Returns the integer link number of the prim containing the script (0 for unlinked, 1 for the root, and 2+ for children).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 139 | Native: False | Pure (no side effects): False

- Categories: prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetLinkNumberOfSides

```lsl
integer llGetLinkNumberOfSides(integer link)
```

- Purpose: Returns an integer representing the number of sides (faces) of the linked prim specified by link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 357 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llGetLinkPrimitiveParams

```lsl
list llGetLinkPrimitiveParams(integer link, list params)
```

- Purpose: Returns a list of primitive parameters requested in params for the linked prim specified by link (equivalent to llGetPrimitiveParams).

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag to retrieve parameters from.

- Argument `params` (list): A list of PRIM_* flags specifying the attributes to retrieve.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 354 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llGetLinkSitFlags

```lsl
integer llGetLinkSitFlags(integer link)
```

- Purpose: Returns an integer representing the active sit flags currently set on the linked prim specified by link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 551 | Native: False | Pure (no side effects): False

- Categories: linkset, sit


## llGetListEntryType

```lsl
integer llGetListEntryType(list src, integer index)
```

- Purpose: Returns an integer representing the variable type (TYPE_*) of the list entry at index in the list src.

- Argument `src` (list): Source list containing the element of interest.

- Argument `index` (integer): Zero-based index of the entry.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 194 | Native: True | Pure (no side effects): True

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `typeof`. 


## llGetListLength

```lsl
integer llGetListLength(list src)
```

- Purpose: Returns an integer representing the total number of elements in the list src.

- Argument `src` (list): List to measure.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 185 | Native: True | Pure (no side effects): True

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Use '#' or 'rawlen' instead. Metatable support.


## llGetLocalPos

```lsl
vector llGetLocalPos()
```

- Purpose: Returns a position vector relative to the root prim. If called from the root prim, it returns the global region position (or the position relative to the attachment point if attached).

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 60 | Native: False | Pure (no side effects): False

- Categories: prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetLocalRot

```lsl
rotation llGetLocalRot()
```

- Purpose: Returns a rotation representing the local orientation of a child prim relative to the root prim, or the object's overall rotation if called from the root.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 63 | Native: False | Pure (no side effects): False

- Categories: prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetMass

```lsl
float llGetMass()
```

- Purpose: Returns a float representing the mass of the object (in lindograms). Returns the total linkset mass if called from the root, or the individual prim's mass if called from a child prim. Returns the wearer's mass if inside an attachment.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 109 | Native: False | Pure (no side effects): False

- Categories: linkset, physics


## llGetMassMKS

```lsl
float llGetMassMKS()
```

- Purpose: Returns a float representing the mass of the object in kilograms. Functionally identical to llGetMass except for using MKS (metric) units.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 382 | Native: False | Pure (no side effects): False

- Categories: linkset, physics


## llGetMaxScaleFactor

```lsl
float llGetMaxScaleFactor()
```

- Purpose: Returns a float representing the maximum scale factor that can be applied to the object via llScaleByFactor without violating size or linkability limits.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 591 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llGetMemoryLimit

```lsl
integer llGetMemoryLimit()
```

- Purpose: Returns an integer representing the maximum memory limit (in bytes) that the script is allowed to allocate.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 370 | Native: False | Pure (no side effects): False

- Categories: script


## llGetMinScaleFactor

```lsl
float llGetMinScaleFactor()
```

- Purpose: Returns a float representing the minimum scale factor that can be applied to the object via llScaleByFactor without violating size limits.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 590 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llGetMoonDirection

```lsl
vector llGetMoonDirection()
```

- Purpose: Returns a normalized vector representing the current direction of the parcel's moon, taking altitude into account. Falls back to the region's moon direction if no custom parcel environment is set.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 701 | Native: False | Pure (no side effects): False

- Categories: parcel, parcel_appearance


## llGetMoonRotation

```lsl
rotation llGetMoonRotation()
```

- Purpose: Returns a rotation representing the orientation applied to the moon on the current parcel and altitude track. Falls back to the region's moon rotation if no custom parcel environment is set.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 709 | Native: False | Pure (no side effects): False

- Categories: parcel, parcel_appearance


## llGetNextEmail

```lsl
void llGetNextEmail(string address, string subject)
```

- Purpose: Requests the next queued email via the email event. Emails must
1. Be sent to `{ll.GetKey()}@lsl.secondlife.com`
2. Be sent from the specified sender Address (or any address if blank)
3. Have the specified subject Subject (or any subject if blank)

- Argument `address` (string): Sender email address filter, or "" for any address.

- Argument `subject` (string): Email subject filter, or "" for any subject.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 120 | Native: False | Pure (no side effects): False

- Categories: script_communication


## llGetNotecardLine

```lsl
key llGetNotecardLine(string name, integer line)
```

- Purpose: Asynchronously requests the text of line in the notecard name. Returns a key query handle for the dataserver event, which receives EOF if line is past the end of the notecard.

- Argument `name` (string): Name of the notecard in the prim's inventory, or a UUID.

- Argument `line` (integer): Index of the line to read.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 217 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, notecard

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGetNotecardLineSync

```lsl
string llGetNotecardLineSync(string name, integer line)
```

- Purpose: Synchronously reads the text of line in the notecard name from the region's cache, without raising a dataserver event. Returns NAK if the notecard is not cached, or EOF if line is past the end of the notecard.

- Argument `name` (string): Name of the notecard in the prim's inventory, or a UUID.

- Argument `line` (integer): Index of the line to read.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 549 | Native: False | Pure (no side effects): False

- Categories: data_storage, notecard


## llGetNumberOfNotecardLines

```lsl
key llGetNumberOfNotecardLines(string name)
```

- Purpose: Asynchronously requests the number of lines in the notecard name. Returns a key query handle for the dataserver event.

- Argument `name` (string): Name of the notecard in the prim's inventory, or a UUID.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 276 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, notecard

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGetNumberOfPrims

```lsl
integer llGetNumberOfPrims()
```

- Purpose: Returns an integer representing the total number of prims and seated avatars in the linkset containing the script.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 275 | Native: False | Pure (no side effects): False

- Categories: linkset


## llGetNumberOfSides

```lsl
integer llGetNumberOfSides()
```

- Purpose: Returns an integer representing the total number of sides (faces) of the prim containing the script.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 168 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetObjectAnimationNames

```lsl
list llGetObjectAnimationNames()
```

- Purpose: Returns a list of strings representing the names or UUIDs of all active animations currently playing on the object.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 506 | Native: False | Pure (no side effects): False

- Categories: object_animation


## llGetObjectDesc

```lsl
string llGetObjectDesc()
```

- Purpose: Returns a string containing the description of the specific prim containing the script.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 270 | Native: False | Pure (no side effects): False

- Categories: prim, prim_properties

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetObjectDetails

```lsl
list llGetObjectDetails(key id, list params)
```

- Purpose: Returns a list containing the requested parameters of the specified avatar or object id, retrieved in the order requested by params.

- Argument `id` (key): UUID of the avatar or prim (in the same or adjacent regions) to query.

- Argument `params` (list): A list of OBJECT_* flags specifying the attributes to retrieve.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 332 | Native: False | Pure (no side effects): False

- Categories: object, prim_properties

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llGetObjectLinkKey

```lsl
key llGetObjectLinkKey(key object_id, integer link)
```

- Purpose: Returns the key (UUID) of the linked child prim specified by link within the linkset identified by object_id.

- Argument `object_id` (key): UUID of the target prim or linkset.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag of the prim to retrieve.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 532 | Native: False | Pure (no side effects): False

- Categories: object, uuid

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llGetObjectMass

```lsl
float llGetObjectMass(key id)
```

- Purpose: Returns a float representing the mass of the avatar or object specified by id.

- Argument `id` (key): UUID of the avatar or object to query.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 295 | Native: False | Pure (no side effects): False

- Categories: object, physics

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llGetObjectName

```lsl
string llGetObjectName()
```

- Purpose: Returns a string containing the name of the specific prim containing the script.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 202 | Native: False | Pure (no side effects): False

- Categories: prim, prim_properties

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetObjectPermMask

```lsl
integer llGetObjectPermMask(integer group)
```

- Purpose: Returns the script's object's permission flags for the specified group.

- Argument `group` (integer): MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to get.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 287 | Native: False | Pure (no side effects): False

- Categories: asset_permissions, linkset


## llGetObjectPrimCount

```lsl
integer llGetObjectPrimCount(key prim)
```

- Purpose: Returns an integer representing the total number of prims in the object containing the specified prim.

- Argument `prim` (key): UUID of the prim in the same region.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 323 | Native: False | Pure (no side effects): False

- Categories: object

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llGetOmega

```lsl
vector llGetOmega()
```

- Purpose: Returns a vector representing the physical rotation (angular velocity) of the object in radians per second.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 79 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llGetOwner

```lsl
key llGetOwner()
```

- Purpose: Returns the key (UUID) of the object's current owner.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 117 | Native: False | Pure (no side effects): False

- Categories: linkset, uuid


## llGetOwnerKey

```lsl
key llGetOwnerKey(key id)
```

- Purpose: Returns the key (UUID) of the owner of the prim specified by id.

- Argument `id` (key): UUID of the prim in the same region.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 182 | Native: False | Pure (no side effects): False

- Categories: object, uuid

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llGetParcelDetails

```lsl
list llGetParcelDetails(vector pos, list params)
```

- Purpose: Returns a list containing the requested parcel details specified by params (retrieved in the same order) for the parcel at the vector pos.

- Argument `pos` (vector): Position vector in region coordinates (only the X and Y components are used).

- Argument `params` (list): A list of PARCEL_DETAILS_* flags specifying the attributes to retrieve.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 327 | Native: False | Pure (no side effects): False

- Categories: parcel


## llGetParcelFlags

```lsl
integer llGetParcelFlags(vector pos)
```

- Purpose: Returns an integer bitfield of parcel flags (PARCEL_FLAG_*) for the parcel at the position pos.

- Argument `pos` (vector): Position vector in region coordinates (the Z component is ignored).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 317 | Native: False | Pure (no side effects): False

- Categories: parcel


## llGetParcelMaxPrims

```lsl
integer llGetParcelMaxPrims(vector pos, integer sim_wide)
```

- Purpose: Returns an integer representing the maximum combined land impact (prim limit) allowed for objects on the parcel at pos, determined either for the single parcel or sim-wide based on sim_wide.

- Argument `pos` (vector): Position vector in region coordinates (the Z component is ignored).

- Argument `sim_wide` (integer): Boolean. If TRUE, returns the combined land impact limit for all parcels owned by the parcel owner in the region; if FALSE, returns only the limit for the specified parcel.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 326 | Native: False | Pure (no side effects): False

- Categories: parcel


## llGetParcelMusicURL

```lsl
string llGetParcelMusicURL()
```

- Purpose: Returns a string containing the parcel's streaming music (audio) URL. The object owner must also be the land owner (or share the same group deeding).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 396 | Native: False | Pure (no side effects): False

- Categories: parcel


## llGetParcelPrimCount

```lsl
integer llGetParcelPrimCount(vector pos, integer category, integer sim_wide)
```

- Purpose: Returns an integer representing the total land impact of objects on the parcel at pos in the specified category. If sim_wide is TRUE, returns combined usage for all regional parcels owned by the parcel owner; if FALSE, returns usage for only the specified parcel.

- Argument `pos` (vector): Position vector in region coordinates (the Z component is ignored).

- Argument `category` (integer): PARCEL_COUNT_* category flag.

- Argument `sim_wide` (integer): Boolean. If TRUE, searches all parcels in the region owned by the targeted parcel's owner; if FALSE, searches only the specified parcel.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 325 | Native: False | Pure (no side effects): False

- Categories: parcel


## llGetParcelPrimOwners

```lsl
list llGetParcelPrimOwners(vector pos)
```

- Purpose: Returns a list of up to 100 strides (formatted as [key owner, integer land_impact]) representing owners of objects on the parcel at pos, sorted by owner key. Requires owner-like permissions for the parcel and the script owner's presence in the region.

- Argument `pos` (vector): Position vector in region coordinates.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 2.0 s | Function ID: 324 | Native: False | Pure (no side effects): False

- Categories: parcel

- Delay warning: this call sleeps the script for 2.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGetPermissions

```lsl
integer llGetPermissions()
```

- Purpose: Returns an integer bitfield representing the permissions (PERMISSION_*) currently granted to the script.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 138 | Native: False | Pure (no side effects): False

- Categories: permissions


## llGetPermissionsKey

```lsl
key llGetPermissionsKey()
```

- Purpose: Returns the key (UUID) of the avatar that last granted or declined permissions to the script, or NULL_KEY if the permissions request was ignored or cancelled.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 137 | Native: False | Pure (no side effects): False

- Categories: avatar, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetPhysicsMaterial

```lsl
list llGetPhysicsMaterial()
```

- Purpose: Returns a list of the format [float gravity_multiplier, float restitution, float friction, float density] detailing the physical characteristics of the object.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 381 | Native: False | Pure (no side effects): False

- Categories: physics, prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetPos

```lsl
vector llGetPos()
```

- Purpose: Returns a vector representing the current position of the object in region coordinates.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 59 | Native: False | Pure (no side effects): False

- Categories: prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetPrimMediaParams

```lsl
list llGetPrimMediaParams(integer face, list params)
```

- Purpose: Returns a list containing the media parameters of the specified face, retrieved in the order requested by params. Returns an empty list if no media exists on the face.

- Argument `face` (integer): Face number (side) of the prim.

- Argument `params` (list): A list of PRIM_MEDIA_* property constants to retrieve values for.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 351 | Native: False | Pure (no side effects): False

- Categories: media, prim, prim_media

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGetPrimitiveParams

```lsl
list llGetPrimitiveParams(list params)
```

- Purpose: Returns a list of primitive attribute values matching the requested params list.

- Argument `params` (list): A list of PRIM_* flags specifying the attributes to retrieve.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 279 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance, prim_properties

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGetRegionAgentCount

```lsl
integer llGetRegionAgentCount()
```

- Purpose: Returns an integer representing the current number of avatars in the region.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 334 | Native: False | Pure (no side effects): False

- Categories: region


## llGetRegionCorner

```lsl
vector llGetRegionCorner()
```

- Purpose: Returns a vector (in meters) representing the global grid coordinates of the south-west corner of the current region (Z component is always 0.0).

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 199 | Native: False | Pure (no side effects): False

- Categories: region


## llGetRegionDayLength

```lsl
integer llGetRegionDayLength()
```

- Purpose: Returns an integer representing the total number of seconds in the region-wide day cycle.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 704 | Native: False | Pure (no side effects): False

- Categories: region, time


## llGetRegionDayOffset

```lsl
integer llGetRegionDayOffset()
```

- Purpose: Returns an integer representing the offset duration (in seconds) added to calculate the current environmental time for the region.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 706 | Native: False | Pure (no side effects): False

- Categories: region, time


## llGetRegionFPS

```lsl
float llGetRegionFPS()
```

- Purpose: Returns a float representing the average region simulator frames per second (FPS).

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 228 | Native: False | Pure (no side effects): False

- Categories: region


## llGetRegionFlags

```lsl
integer llGetRegionFlags()
```

- Purpose: Returns an integer bitfield representing the region flags (REGION_FLAG_*) currently enabled for the region containing the object.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 318 | Native: False | Pure (no side effects): False

- Categories: region


## llGetRegionMoonDirection

```lsl
vector llGetRegionMoonDirection()
```

- Purpose: Returns a normalized vector representing the current direction of the region's moon, taking altitude into account.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 702 | Native: False | Pure (no side effects): False

- Categories: region, region_appearance


## llGetRegionMoonRotation

```lsl
rotation llGetRegionMoonRotation()
```

- Purpose: Returns a rotation representing the orientation applied to the moon at the region level, taking altitude track into account.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 710 | Native: False | Pure (no side effects): False

- Categories: region, region_appearance


## llGetRegionName

```lsl
string llGetRegionName()
```

- Purpose: Returns a string containing the name of the current region.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 226 | Native: False | Pure (no side effects): False

- Categories: region


## llGetRegionSunDirection

```lsl
vector llGetRegionSunDirection()
```

- Purpose: Returns a normalized vector representing the current direction of the region's sun, taking altitude into account.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 700 | Native: False | Pure (no side effects): False

- Categories: region, region_appearance


## llGetRegionSunRotation

```lsl
rotation llGetRegionSunRotation()
```

- Purpose: Returns a rotation representing the orientation applied to the sun at the region level, taking altitude track into account.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 708 | Native: False | Pure (no side effects): False

- Categories: region, region_appearance


## llGetRegionTimeDilation

```lsl
float llGetRegionTimeDilation()
```

- Purpose: Returns a float representing the current physics time dilation of the region, ranging from 0.0 (full dilation / slow) to 1.0 (no dilation / real-world speed).

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 227 | Native: False | Pure (no side effects): False

- Categories: region


## llGetRegionTimeOfDay

```lsl
float llGetRegionTimeOfDay()
```

- Purpose: Returns a float with subsecond precision representing the elapsed seconds since region environmental midnight or region uptime (whichever is smaller). If the region's sun position is fixed, returns region uptime.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 712 | Native: False | Pure (no side effects): False

- Categories: region, time


## llGetRenderMaterial

```lsl
string llGetRenderMaterial(integer face)
```

- Purpose: Returns a string representing the render material on face (returns the inventory name if it is in the prim's inventory, or its key UUID otherwise).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 760 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetRootPosition

```lsl
vector llGetRootPosition()
```

- Purpose: Returns a vector representing the position (in region coordinates) of the root prim of the linkset containing the script.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 268 | Native: False | Pure (no side effects): False

- Categories: linkset


## llGetRootRotation

```lsl
rotation llGetRootRotation()
```

- Purpose: Returns a rotation representing the orientation (relative to the region) of the root prim of the linkset containing the script.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 269 | Native: False | Pure (no side effects): False

- Categories: linkset


## llGetRot

```lsl
rotation llGetRot()
```

- Purpose: Returns a rotation representing the prim's orientation relative to the region's axes.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 62 | Native: False | Pure (no side effects): False

- Categories: prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetSPMaxMemory

```lsl
integer llGetSPMaxMemory()
```

- Purpose: Returns an integer representing the maximum memory (in bytes) used by the script while the memory profiler was last active (only valid after using PROFILE_SCRIPT_MEMORY).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 365 | Native: False | Pure (no side effects): False

- Categories: script


## llGetScale

```lsl
vector llGetScale()
```

- Purpose: Returns a vector representing the physical scale (dimensions in meters) of the prim containing the script.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 48 | Native: False | Pure (no side effects): False

- Categories: prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetScriptName

```lsl
string llGetScriptName()
```

- Purpose: Returns a string containing the name of the script calling this function.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 167 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, script


## llGetScriptState

```lsl
integer llGetScriptState(string script)
```

- Purpose: Returns a boolean integer indicating whether the specified script in the prim's inventory is running (returns TRUE if running, FALSE otherwise).

- Argument `script` (string): Name of the script in the prim's inventory.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 250 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, script


## llGetSimStats

```lsl
float llGetSimStats(integer stat_type)
```

- Purpose: Returns a float containing the value of the requested region statistic specified by stat_type.

- Argument `stat_type` (integer): SIM_STAT_* flag of the statistic to retrieve.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 415 | Native: False | Pure (no side effects): False

- Categories: region


## llGetSimulatorHostname

```lsl
string llGetSimulatorHostname()
```

- Purpose: Returns a string containing the hostname of the server machine running the script (e.g., 'sim225.agni.lindenlab.com').

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 10.0 s | Function ID: 283 | Native: False | Pure (no side effects): False

- Categories: region

- Delay warning: this call sleeps the script for 10.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGetStartParameter

```lsl
integer llGetStartParameter()
```

- Purpose: Returns an integer representing the start/rez parameter passed to the object on creation (returns 0 if rezzed by an agent).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 134 | Native: False | Pure (no side effects): False

- Categories: rez, script


## llGetStartString

```lsl
string llGetStartString()
```

- Purpose: Returns the initialization string passed to the object's root prim on rez with llRezObjectWithParams (via REZ_PARAM_STRING; returns an empty string if rezzed by an agent).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 556 | Native: False | Pure (no side effects): False

- Categories: rez, script


## llGetStaticPath

```lsl
list llGetStaticPath(vector start_pos, vector end_pos, float radius, list params)
```

- Purpose: Returns a list of position vectors representing pathfinding waypoints between start and end on the static navmesh for a character of the specified radius. Ignores movable obstacles and can be used in any region regardless of dynamic pathfinding status.

- Argument `start_pos` (vector): Starting position vector.

- Argument `end_pos` (vector): Target end position vector.

- Argument `radius` (float): Radius of the character path, between 0.125m and 5.0m.

- Argument `params` (list): A list specifying the CHARACTER_TYPE parameter (defaults to CHARACTER_TYPE_NONE).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 413 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llGetStatus

```lsl
integer llGetStatus(integer status)
```

- Purpose: Returns a boolean integer indicating whether the specified status flag status is enabled for the object.

- Argument `status` (integer): Single STATUS_* flag to check.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 46 | Native: False | Pure (no side effects): False

- Categories: linkset, physics


## llGetSubString

```lsl
string llGetSubString(string src, integer start_index, integer end_index)
```

- Purpose: Returns a copy of the substring from src within the inclusive codepoint range start_index..end_index. Negative indices count backward from the end of the string. If start_index is greater than end_index, the substring is the excluded range.

- Argument `src` (string): Source string to slice.

- Argument `start_index` (integer): Starting codepoint index (inclusive). Supports negative indexing.

- Argument `end_index` (integer): Ending codepoint index (inclusive). Supports negative indexing.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 94 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llGetSunDirection

```lsl
vector llGetSunDirection()
```

- Purpose: Returns a normalized vector representing the current direction of the parcel's sun, taking altitude into account. Falls back to the region's sun direction if no custom parcel environment is set.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 177 | Native: False | Pure (no side effects): False

- Categories: parcel, parcel_appearance


## llGetSunRotation

```lsl
rotation llGetSunRotation()
```

- Purpose: Returns a rotation representing the orientation applied to the sun on the current parcel and altitude track. Falls back to the region's sun rotation if no custom parcel environment is set.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 707 | Native: False | Pure (no side effects): False

- Categories: parcel, parcel_appearance


## llGetTexture

```lsl
string llGetTexture(integer face)
```

- Purpose: Returns a string representing the Blinn-Phong diffuse texture on face (returns the inventory name if it is a texture in the prim's inventory, or its key UUID otherwise).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 57 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetTextureOffset

```lsl
vector llGetTextureOffset(integer face)
```

- Purpose: Returns a vector containing the texture offsets of face in the X (horizontal U) and Y (vertical V) components (Z is unused).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 178 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetTextureRot

```lsl
float llGetTextureRot(integer face)
```

- Purpose: Returns a float representing the texture rotation angle (in radians) on face.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 180 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetTextureScale

```lsl
vector llGetTextureScale(integer face)
```

- Purpose: Returns a vector containing the texture scales of face in the X and Y components (Z is unused).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 179 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llGetTime

```lsl
float llGetTime()
```

- Purpose: Returns a float representing the elapsed script time in seconds with subsecond precision (since the script started, was reset, or since the last call to llResetTime or llGetAndResetTime).

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 82 | Native: False | Pure (no side effects): False

- Categories: script


## llGetTimeOfDay

```lsl
float llGetTimeOfDay()
```

- Purpose: Returns a float with subsecond precision representing the elapsed seconds since parcel environmental midnight or region uptime (whichever is smaller). If the parcel's sun position is fixed, returns region uptime.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 80 | Native: False | Pure (no side effects): False

- Categories: time


## llGetTimestamp

```lsl
string llGetTimestamp()
```

- Purpose: Returns a string containing the current date and time in the UTC time zone formatted as an ISO 8601 timestamp ('YYYY-MM-DDThh:mm:ss.ff..fZ').

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 273 | Native: False | Pure (no side effects): False

- Categories: time


## llGetTorque

```lsl
vector llGetTorque()
```

- Purpose: Returns a vector representing the physical torque force currently acting on the object (if the object is physical).

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 75 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llGetUnixTime

```lsl
integer llGetUnixTime()
```

- Purpose: Returns an integer representing the current Unix timestamp (the number of seconds elapsed since 00:00:00 Jan 1, 1970 UTC).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 316 | Native: False | Pure (no side effects): False

- Categories: time

- SLua: deprecated in favour of `os.time`. Int32 will wrap on 2038-01-19


## llGetUsedMemory

```lsl
integer llGetUsedMemory()
```

- Purpose: Returns an integer representing the total number of bytes of memory currently used by the script (non-Mono scripts always return 16,384 bytes).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 366 | Native: False | Pure (no side effects): False

- Categories: script


## llGetUsername

```lsl
string llGetUsername(key id)
```

- Purpose: Returns a string representing the unique username of the avatar specified by id if they are connected to the region or cached; returns an empty string otherwise (use llRequestUsername if the avatar is absent).

- Argument `id` (key): UUID of the avatar in the same region or otherwise known to the region.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 358 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetVel

```lsl
vector llGetVel()
```

- Purpose: Returns a vector representing the velocity of the object (in meters per second) relative to the global region coordinates. For physical objects, returns the velocity of its center of mass.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 77 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llGetVisualParams

```lsl
list llGetVisualParams(key agentid, list params)
```

- Purpose: Returns a list containing the values of the visual parameters requested in params for the agent specified by agentid.

- Argument `agentid` (key): UUID of the avatar in the same region.

- Argument `params` (list): A list of visual parameter IDs or names to retrieve values for.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 530 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGetWallclock

```lsl
float llGetWallclock()
```

- Purpose: Returns a float representing the time in seconds since midnight Pacific Time (PST/PDT), which is equivalent to Second Life Time (SLT) truncated to whole seconds.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 81 | Native: False | Pure (no side effects): False

- Categories: time


## llGiveAgentInventory

```lsl
integer llGiveAgentInventory(key agent, string folder, list items, list options)
```

- Purpose: Gives the specified inventory items to the agent as a new folder named folder, as permitted by the permissions system. Customizes the transfer using options.

- Argument `agent` (key): UUID of the target agent in the same region.

- Argument `folder` (string): Name of the destination folder to be created

- Argument `items` (list): The names of the items in the prim's inventory to transfer.

- Argument `options` (list): A list of options to configure the inventory transfer.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 3.0 s | Function ID: 517 | Native: False | Pure (no side effects): False

- Categories: avatar_inventory, prim_inventory

- Delay warning: this call sleeps the script for 3.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGiveInventory

```lsl
void llGiveInventory(key target, string item)
```

- Purpose: Gives the specified inventory item to the target, as permitted by the permissions system. The target can be any agent or an object located in the same region.

- Argument `target` (key): UUID of the target agent or prim.

- Argument `item` (string): Name of the item in the prim's inventory to transfer.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 150 | Native: False | Pure (no side effects): False

- Categories: avatar_inventory, prim_inventory


## llGiveInventoryList

```lsl
void llGiveInventoryList(key target, string folder, list items)
```

- Purpose: Gives the list of inventory items to target as a new folder named folder. If target is an object, the items are passed directly into its inventory and no folder is created. The target must be an agent or an object in the same region.

- Argument `target` (key): UUID of the target agent or prim in the same region.

- Argument `folder` (string): Name of the destination folder to be created (ignored if the target is an object).

- Argument `items` (list): The names of the items in the prim's inventory to transfer.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 3.0 s | Function ID: 231 | Native: False | Pure (no side effects): False

- Categories: avatar_inventory, prim_inventory

- Delay warning: this call sleeps the script for 3.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llGiveMoney

```lsl
integer llGiveMoney(key destination, integer amount)
```

- Purpose: Transfers the specified amount of L$ from the script owner to the destination avatar. Silently fails if the PERMISSION_DEBIT permission has not been granted. Returns 0 (use llTransferLindenDollars to match transactions to transaction_result events).

- Argument `destination` (key): UUID of the destination avatar.

- Argument `amount` (integer): Number of L$ to transfer (must be greater than 0).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 99 | Native: False | Pure (no side effects): False

- Categories: avatar, money, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llGodLikeRezObject

```lsl
void llGodLikeRezObject(key id, vector pos)
```

- Purpose: Rezzes an object directly from a UUID specified by id at the position pos, provided the owner has the god-bit set.

- Argument `id` (key): Asset UUID of the object to rez.

- Argument `pos` (vector): Position vector in region coordinates where the object will be rezzed.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 135 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, rez


## llGround

```lsl
float llGround(vector offset)
```

- Purpose: Returns a float representing the ground height directly below the prim's position offset by the vector offset.

- Argument `offset` (vector): Offset relative to the prim's position, expressed in local coordinates.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 42 | Native: False | Pure (no side effects): False

- Categories: region


## llGroundContour

```lsl
vector llGroundContour(vector offset)
```

- Purpose: Returns a vector representing the ground contour direction (the direction with no change in elevation) directly below the prim's position offset by the vector offset.

- Argument `offset` (vector): Offset relative to the prim's position, expressed in local coordinates.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 223 | Native: False | Pure (no side effects): False

- Categories: region


## llGroundNormal

```lsl
vector llGroundNormal(vector offset)
```

- Purpose: Returns a vector representing the ground surface normal vector directly below the current position offset by the vector offset.

- Argument `offset` (vector): Offset relative to the prim's position, expressed in local coordinates.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 222 | Native: False | Pure (no side effects): False

- Categories: region


## llGroundRepel

```lsl
void llGroundRepel(float height, integer water, float tau)
```

- Purpose: Critically damps the object's vertical motion to height (using critical damping timescale tau) if it is within height * 0.5 of the terrain (or water level if water is TRUE). Only works on physics-enabled objects; do not use with vehicles.

- Argument `height` (float): Target distance in meters above the ground or water.

- Argument `water` (integer): Boolean. If TRUE, damp relative to the higher of land and water; if FALSE, damp relative to land only.

- Argument `tau` (float): Timescale in seconds to critically damp the movement.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 230 | Native: False | Pure (no side effects): False

- Categories: region


## llGroundSlope

```lsl
vector llGroundSlope(vector offset)
```

- Purpose: Returns a vector representing the ground slope directly below the prim's position offset by the vector offset.

- Argument `offset` (vector): Offset relative to the prim's position, expressed in local coordinates.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 221 | Native: False | Pure (no side effects): False

- Categories: region


## llHMAC

```lsl
string llHMAC(string private_key, string msg, string algorithm)
```

- Purpose: Returns a Base64-encoded HMAC hash of msg using the secret key private_key and the specified digest algorithm (md5, sha1, sha224, sha256, sha384, or sha512).

- Argument `private_key` (string): PEM-formatted secret key to use for the HMAC hash.

- Argument `msg` (string): Message string to be hashed.

- Argument `algorithm` (string): Cryptographic digest algorithm to use.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 538 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llHTTPRequest

```lsl
key llHTTPRequest(string url, list parameters, string body)
```

- Purpose: Sends an HTTP request to the specified url containing body and configured via parameters. Raises an http_response event and returns a key query handle identifying the request.

- Argument `url` (string): Destination HTTP or HTTPS URL.

- Argument `parameters` (list): A list of HTTP_* configuration flags and value pairs, or an HTTPRequestParams dictionary.

- Argument `body` (string): String contents of the request body.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 320 | Native: False | Pure (no side effects): False

- Categories: script_communication, web


## llHTTPResponse

```lsl
void llHTTPResponse(key request_id, integer status, string body)
```

- Purpose: Responds to the incoming HTTP request identified by request_id with the HTTP status code status and the payload body.

- Argument `request_id` (key): Unique key identifying the incoming HTTP request.

- Argument `status` (integer): Integer HTTP status code (such as 200, 400, or 404) to respond with.

- Argument `body` (string): String contents of the response body.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 348 | Native: False | Pure (no side effects): False

- Categories: media, prim_media, script_communication, web


## llHash

```lsl
integer llHash(string val)
```

- Purpose: Returns an integer representing the 32-bit hash value of the string val (returns 0 if the string is empty).

- Argument `val` (string): String to hash.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 528 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llInsertString

```lsl
string llInsertString(string dst, integer index, string src)
```

- Purpose: Returns a copy of dst with src inserted at the given codepoint index.

- Argument `dst` (string): Target destination string.

- Argument `index` (integer): Codepoint index where insertion starts.

- Argument `src` (string): Source string to insert.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 96 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llInstantMessage

```lsl
void llInstantMessage(key agent, string msg)
```

- Purpose: Sends an instant message containing msg to the agent identified by their key.

- Argument `agent` (key): UUID of the destination agent.

- Argument `msg` (string): Text message string to send.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 2.0 s | Function ID: 118 | Native: False | Pure (no side effects): False

- Categories: avatar_communication

- Delay warning: this call sleeps the script for 2.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llIntegerToBase64

```lsl
string llIntegerToBase64(integer number)
```

- Purpose: Returns an 8-character Base64 string representing the big-endian encoded value of number.

- Argument `number` (integer): Integer number to encode.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 280 | Native: False | Pure (no side effects): True

- Categories: data_conversion

- SLua: deprecated in favour of ``. Use 'llbase64.encode' and 'string.pack' or 'buffer.writei32' instead.


## llIsFriend

```lsl
integer llIsFriend(key agent_id)
```

- Purpose: Returns TRUE if agent_id and the owner of the script are friends, and FALSE otherwise.

- Argument `agent_id` (key): UUID of the agent to check.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 542 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llIsLinkGLTFMaterial

```lsl
integer llIsLinkGLTFMaterial(integer link, integer face)
```

- Purpose: Checks the specified face on the linked prim link. Returns TRUE if the face material is a PBR render material, or FALSE if it uses Blinn-Phong diffuse textures.

- Argument `link` (integer): Link number (or LINK_* flag) of the prim to inspect.

- Argument `face` (integer): Face number (or ALL_SIDES) of the prim to inspect.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 559 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llJson2List

```lsl
list llJson2List(string src)
```

- Purpose: Parses the JSON string src and returns a list representing its top-level elements.

- Argument `src` (string): JSON string to parse.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 513 | Native: False | Pure (no side effects): True

- Categories: data_conversion, json

- Guidance (json): JSON in LSL is string based and slow on large documents. Keep payloads small and validate with llJsonValueType first.

- SLua: deprecated in favour of `lljson.decode`. 


## llJsonGetValue

```lsl
string llJsonGetValue(string json, list specifiers)
```

- Purpose: Parses the JSON string json and returns the value found by traversing the specified path of specifiers as a string.

- Argument `json` (string): JSON string to query.

- Argument `specifiers` (list): A list of key names or array indices specifying the path to the desired value.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 511 | Native: False | Pure (no side effects): True

- Categories: data_conversion, json

- Guidance (json): JSON in LSL is string based and slow on large documents. Keep payloads small and validate with llJsonValueType first.

- SLua: deprecated in favour of `lljson.decode`. Also, the indices are zero-based.


## llJsonSetValue

```lsl
string llJsonSetValue(string json, list specifiers, string value)
```

- Purpose: Returns a new JSON string representing json with the target located at specifiers set to value. Supports JSON_APPEND to append elements. Writing JSON_DELETE deletes the target. Overwriting array bounds or setting non-array levels with array indices returns JSON_INVALID.

- Argument `json` (string): Source JSON string to modify.

- Argument `specifiers` (list): A list of key names or array indices specifying the path to add, update, or delete.

- Argument `value` (string): New value to set, or the JSON_DELETE constant to delete the targeted element.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 510 | Native: False | Pure (no side effects): True

- Categories: data_conversion, json

- Guidance (json): JSON in LSL is string based and slow on large documents. Keep payloads small and validate with llJsonValueType first.

- SLua: deprecated in favour of `lljson.encode`. Also, the indices are zero-based.


## llJsonValueType

```lsl
string llJsonValueType(string json, list specifiers)
```

- Purpose: Parses the JSON string json and returns the JSON type constant (JSON_*) representing the value found at specifiers.

- Argument `json` (string): JSON string containing the value to query.

- Argument `specifiers` (list): A list of key names or array indices specifying the path to the value.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 512 | Native: False | Pure (no side effects): True

- Categories: data_conversion, json

- Guidance (json): JSON in LSL is string based and slow on large documents. Keep payloads small and validate with llJsonValueType first.

- SLua: deprecated in favour of ``. Use 'lljson.decode' and 'typeof' instead. Also, the indices are zero-based.


## llKey2Name

```lsl
string llKey2Name(key id)
```

- Purpose: Returns a string containing the name of the prim or avatar specified by id. The target must be a valid, rezzed entity in the current region, otherwise an empty string is returned. Avatars return their legacy name.

- Argument `id` (key): UUID of the target avatar or prim in the same region.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 210 | Native: False | Pure (no side effects): False

- Categories: object

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llKeyCountKeyValue

```lsl
key llKeyCountKeyValue()
```

- Purpose: Starts an asynchronous transaction requesting the total count of keys in the experience data store. Returns a key query handle for the dataserver event.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 601 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, experience, experience_data

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llKeysKeyValue

```lsl
key llKeysKeyValue(integer first, integer count)
```

- Purpose: Starts an asynchronous transaction to retrieve count keys from the experience data store starting at the zero-based index first. Returns a key query handle for the dataserver event. Fails with XP_ERROR_KEY_NOT_FOUND if out of bounds.

- Argument `first` (integer): Zero-based start index of the keys to retrieve.

- Argument `count` (integer): Number of keys to retrieve.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 602 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, experience, experience_data

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llLinear2sRGB

```lsl
vector llLinear2sRGB(vector color)
```

- Purpose: Returns a sRGB colorspace vector converted from the linear RGB colorspace argument.

- Argument `color` (vector): Color vector in the linear RGB space to convert.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 715 | Native: False | Pure (no side effects): False

- Categories: data_conversion, math, prim_appearance, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llLinkAdjustSoundVolume

```lsl
void llLinkAdjustSoundVolume(integer link, float volume)
```

- Purpose: Adjusts the volume of the currently playing sound attached to the linked prim link (has no effect on sounds started with llTriggerSound).

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag of the prim to adjust.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 535 | Native: False | Pure (no side effects): False

- Categories: sound


## llLinkParticleSystem

```lsl
void llLinkParticleSystem(integer link, list rules)
```

- Purpose: Creates or updates a particle system on the linked prim link based on the list of rules. An empty list removes the particle system.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `rules` (list): A list of particle system rules and data pairs [rule1, data1, ...], or a ParticleParams dictionary.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 355 | Native: False | Pure (no side effects): False

- Categories: effects, particles


## llLinkPlaySound

```lsl
void llLinkPlaySound(integer link, string sound, float volume, integer flags)
```

- Purpose: Plays the specified sound on the linked prim link (once or looping) at volume. Only one sound can be attached to a prim at a time; new attachments or calling llStopSound stops previous playback. Controlled by flags.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Argument `flags` (integer): Bitwise flags (combination of SOUND_*) controlling the sound playback.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 533 | Native: False | Pure (no side effects): False

- Categories: sound


## llLinkSetSoundQueueing

```lsl
void llLinkSetSoundQueueing(integer link, integer queue)
```

- Purpose: Enables or disables sound queuing on the linked prim link. When set to TRUE, sounds will queue and play in sequence.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `queue` (integer): Boolean. If TRUE, sound queuing is enabled; if FALSE, it is disabled.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 537 | Native: False | Pure (no side effects): False

- Categories: sound


## llLinkSetSoundRadius

```lsl
void llLinkSetSoundRadius(integer link, float radius)
```

- Purpose: Limits the audibility radius of attached and triggered scripted sounds to distance radius (in meters) around the linked prim link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `radius` (float): Maximum distance in meters at which the sounds can be heard.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 536 | Native: False | Pure (no side effects): False

- Categories: sound


## llLinkSitTarget

```lsl
void llLinkSitTarget(integer link, vector offset, rotation rot)
```

- Purpose: Sets the sit target position (offset) and orientation (rot) for the linked prim link, relative to the prim's own position and rotation. Clear by setting offset to <0.0, 0.0, 0.0>.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `offset` (vector): Offset position vector in local prim coordinates.

- Argument `rot` (rotation): Rotation relative to the prim's rotation.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 375 | Native: False | Pure (no side effects): False

- Categories: linkset, sit


## llLinkStopSound

```lsl
void llLinkStopSound(integer link)
```

- Purpose: Stops the playback of any currently playing attached sound on the linked prim link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 534 | Native: False | Pure (no side effects): False

- Categories: sound


## llLinksetDataAvailable

```lsl
integer llLinksetDataAvailable()
```

- Purpose: Returns the number of bytes remaining in the linkset datastore.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 654 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataCountFound

```lsl
integer llLinksetDataCountFound(string pattern)
```

- Purpose: Returns the number of keys in the linkset datastore that match the regular expression pattern.

- Argument `pattern` (string): Regular expression (regex) matching the keys to count.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 661 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataCountKeys

```lsl
integer llLinksetDataCountKeys()
```

- Purpose: Returns the number of keys in the linkset datastore.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 653 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataDelete

```lsl
integer llLinksetDataDelete(string name)
```

- Purpose: Deletes the unprotected key name from the linkset datastore, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

- Argument `name` (string): Name of the key to delete.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 652 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataDeleteFound

```lsl
list llLinksetDataDeleteFound(string pattern, string pass)
```

- Purpose: Deletes all keys in the linkset datastore that match the regular expression pattern, triggering a linkset_data event if the datastore changes. Protected keys are only deleted if their passphrase matches pass. Returns a list [num_deleted, num_failed_protected].

- Argument `pattern` (string): Regular expression (regex) matching the keys to delete.

- Argument `pass` (string): Optional passphrase required to delete matching protected keys.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 662 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataDeleteProtected

```lsl
integer llLinksetDataDeleteProtected(string name, string pass)
```

- Purpose: Deletes the protected key name from the linkset datastore using the passphrase pass, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

- Argument `name` (string): Name of the protected key to delete.

- Argument `pass` (string): Passphrase required to delete the protected key.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 660 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataFindKeys

```lsl
list llLinksetDataFindKeys(string pattern, integer start, integer count)
```

- Purpose: Returns an alphabetically sorted list of up to count keys from the linkset datastore that match the regular expression pattern, starting at index start (returns all matching keys if count < 1).

- Argument `pattern` (string): Regular expression (regex) matching the keys to return.

- Argument `start` (integer): Index of the first matching key to return.

- Argument `count` (integer): Maximum number of keys to return (or less than 1 to retrieve all matching keys).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 657 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataListKeys

```lsl
list llLinksetDataListKeys(integer start, integer count)
```

- Purpose: Returns an alphabetically sorted list of up to count keys from the linkset datastore, starting at index start (returns all keys if count < 1).

- Argument `start` (integer): Index of the first key to return.

- Argument `count` (integer): Maximum number of keys to return (or less than 1 to retrieve all keys).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 656 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataRead

```lsl
string llLinksetDataRead(string name)
```

- Purpose: Returns the value of the unprotected key name from the linkset datastore. Returns an empty string if the key is not found or is protected.

- Argument `name` (string): Name of the key to read.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 651 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataReadProtected

```lsl
string llLinksetDataReadProtected(string name, string pass)
```

- Purpose: Returns the value of the protected key name from the linkset datastore using the passphrase pass. Returns an empty string if the key is not found or pass does not match.

- Argument `name` (string): Name of the protected key to read.

- Argument `pass` (string): Passphrase required to read the protected key.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 659 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataReset

```lsl
void llLinksetDataReset()
```

- Purpose: Deletes all keys from the linkset datastore, triggering a linkset_data event.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 655 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataWrite

```lsl
integer llLinksetDataWrite(string name, string value)
```

- Purpose: Creates or updates the unprotected key name in the linkset datastore with value, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

- Argument `name` (string): Name of the key to write.

- Argument `value` (string): Value to write to the key (an empty string deletes the key).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 650 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llLinksetDataWriteProtected

```lsl
integer llLinksetDataWriteProtected(string name, string value, string pass)
```

- Purpose: Creates or updates the protected key name in the linkset datastore with value using the passphrase pass, triggering a linkset_data event if the datastore changes. Returns an integer success or failure code.

- Argument `name` (string): Name of the protected key to write.

- Argument `value` (string): Value to write to the key (an empty string deletes the key).

- Argument `pass` (string): Passphrase used to protect or update the key.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 658 | Native: False | Pure (no side effects): False

- Categories: data_storage, linkset, linkset_data


## llList2CSV

```lsl
string llList2CSV(list src)
```

- Purpose: Returns a string of comma-separated values taken in order from the list src.

- Argument `src` (list): Source list to convert.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 195 | Native: False | Pure (no side effects): True

- Categories: data_conversion, list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.


## llList2Float

```lsl
float llList2Float(list src, integer index)
```

- Purpose: Returns the float value at index in the list src. Returns 0.0 if the index is out of bounds or if the value cannot be type-cast.

- Argument `src` (list): Source list containing the element of interest.

- Argument `index` (integer): Zero-based index of the entry.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 187 | Native: True | Pure (no side effects): True

- Categories: data_conversion, list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Use '[]' and 'tonumber' instead.


## llList2Integer

```lsl
integer llList2Integer(list src, integer index)
```

- Purpose: Returns the integer value at index in the list src. Returns 0 if the index is out of bounds or if the value cannot be type-cast.

- Argument `src` (list): Source list containing the element of interest.

- Argument `index` (integer): Zero-based index of the entry.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 186 | Native: True | Pure (no side effects): True

- Categories: data_conversion, list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Use '[]', 'tonumber', and 'math.modf' instead.


## llList2Json

```lsl
string llList2Json(string type, list values)
```

- Purpose: Converts the list values into a JSON string of the specified type (either a JSON_ARRAY or a JSON_OBJECT). Returns JSON_INVALID if an error is encountered.

- Argument `type` (string): JSON target type (JSON_ARRAY or JSON_OBJECT).

- Argument `values` (list): List of values to serialize.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 514 | Native: False | Pure (no side effects): True

- Categories: data_conversion, json, list

- Guidance (json): JSON in LSL is string based and slow on large documents. Keep payloads small and validate with llJsonValueType first.

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `lljson.encode`. 


## llList2Key

```lsl
key llList2Key(list src, integer index)
```

- Purpose: Returns the key (UUID) value at index in the list src. Returns a null string/key if the index is out of bounds or if the value cannot be type-cast.

- Argument `src` (list): Source list containing the element of interest.

- Argument `index` (integer): Zero-based index of the entry.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 189 | Native: True | Pure (no side effects): True

- Categories: data_conversion, list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Use '[]' and 'touuid' instead.


## llList2List

```lsl
list llList2List(list src, integer start_index, integer end_index)
```

- Purpose: Returns a new list containing the subset of entries from src within the inclusive range specified by the start and end indices. Negative indices count backward from the end.

- Argument `src` (list): Source list to slice.

- Argument `start_index` (integer): Zero-based start index (inclusive).

- Argument `end_index` (integer): Zero-based end index (inclusive).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 192 | Native: True | Pure (no side effects): True

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Use 'unpack' (fastcall) or 'table.move' instead. Prefer structured tables over strided lists.


## llList2ListSlice

```lsl
list llList2ListSlice(list src, integer start_index, integer end_index, integer stride, integer slice_index)
```

- Purpose: Returns a list containing the slice_index'th element of every stride within the inclusive range from start to end in the strided list src. Stride must be a positive integer.

- Argument `src` (list): Source strided list.

- Argument `start_index` (integer): Zero-based start index (inclusive).

- Argument `end_index` (integer): Zero-based end index (inclusive).

- Argument `stride` (integer): Number of entries per stride (defaults to 1 if less than 1).

- Argument `slice_index` (integer): Zero-based element index within each stride to extract (negatives count backward from the end of the stride).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 801 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Prefer structured tables over strided lists.


## llList2ListStrided

```lsl
list llList2ListStrided(list src, integer start_index, integer end_index, integer stride)
```

- Purpose: Returns a new list containing the first element of every stride in the strided list src within the inclusive range from start to end.

- Argument `src` (list): Source strided list.

- Argument `start_index` (integer): Zero-based start index (inclusive).

- Argument `end_index` (integer): Zero-based end index (inclusive).

- Argument `stride` (integer): Number of entries per stride (defaults to 1 if less than 1).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 198 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Prefer structured tables over strided lists.


## llList2Rot

```lsl
rotation llList2Rot(list src, integer index)
```

- Purpose: Returns the rotation value at index in the list src. Returns ZERO_ROTATION if the index is out of bounds or if the value cannot be type-cast.

- Argument `src` (list): Source list containing the element of interest.

- Argument `index` (integer): Zero-based index of the entry.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 191 | Native: True | Pure (no side effects): True

- Categories: data_conversion, list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `[]`. 


## llList2String

```lsl
string llList2String(list src, integer index)
```

- Purpose: Returns the string value at index in the list src. Returns an empty string if the index is out of bounds.

- Argument `src` (list): Source list containing the element of interest.

- Argument `index` (integer): Zero-based index of the entry.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 188 | Native: True | Pure (no side effects): True

- Categories: data_conversion, list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Use '[]' and 'tostring' instead.


## llList2Vector

```lsl
vector llList2Vector(list src, integer index)
```

- Purpose: Returns the vector value at index in the list src. Returns ZERO_VECTOR if the index is out of bounds or if the value cannot be type-cast.

- Argument `src` (list): Source list containing the element of interest.

- Argument `index` (integer): Zero-based index of the entry.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 190 | Native: True | Pure (no side effects): True

- Categories: data_conversion, list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `[]`. 


## llListFindList

```lsl
integer llListFindList(list src, list test)
```

- Purpose: Returns the integer index of the first instance of list test within the list src (returns -1 if not found).

- Argument `src` (list): List to search within.

- Argument `test` (list): List elements to search for.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 201 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `table.find`. Prefer dictionaries or single-item searches.


## llListFindListNext

```lsl
integer llListFindListNext(list src, list test, integer instance)
```

- Purpose: Returns the integer index of the specified instance of list test within the list src (returns -1 if not found).

- Argument `src` (list): List to search within.

- Argument `test` (list): List elements to search for.

- Argument `instance` (integer): Zero-based occurrence index of the match to find.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 803 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `table.find`. Prefer dictionaries or single-item searches.


## llListFindStrided

```lsl
integer llListFindStrided(list src, list test, integer start_index, integer end_index, integer stride)
```

- Purpose: Returns the integer index of the first instance of list test in the strided list src within the range from start to end (stepping through by stride). Returns -1 if not found.

- Argument `src` (list): List to search within.

- Argument `test` (list): List elements to search for.

- Argument `start_index` (integer): Zero-based start index of the range to search.

- Argument `end_index` (integer): Zero-based end index of the range to search.

- Argument `stride` (integer): Number of entries per stride in the list.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 800 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of ``. Prefer dictionary lookups over strided list searches.


## llListInsertList

```lsl
list llListInsertList(list dest, list src, integer start)
```

- Purpose: Returns a new list containing all elements of dest with the elements of src inserted starting at index start. Does not modify dest itself.

- Argument `dest` (list): Target destination list.

- Argument `src` (list): Source list to insert.

- Argument `start` (integer): Zero-based index where insertion begins.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 200 | Native: True | Pure (no side effects): True

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `table.insert`. Unnecessary table copying. Fastcall.


## llListRandomize

```lsl
list llListRandomize(list src, integer stride)
```

- Purpose: Returns a randomized copy of the list src by blocks of size stride. If the list length is not perfectly divisible by stride, no randomization occurs.

- Argument `src` (list): Source list to randomize.

- Argument `stride` (integer): Size of each randomized block (defaults to 1 if less than 1).

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 197 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.


## llListReplaceList

```lsl
list llListReplaceList(list dest, list src, integer start_index, integer end_index)
```

- Purpose: Returns a copy of the list dest with the inclusive range from start to end removed, and the elements of src inserted in its place at start.

- Argument `dest` (list): Target destination list.

- Argument `src` (list): Source list to insert.

- Argument `start_index` (integer): Zero-based start index (inclusive) of the replaced range.

- Argument `end_index` (integer): Zero-based end index (inclusive) of the replaced range.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 296 | Native: True | Pure (no side effects): True

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `t[n] = x`. Unnecessary table copying.


## llListSort

```lsl
list llListSort(list src, integer stride, integer ascending)
```

- Purpose: Returns a copy of the list src, sorted into blocks of stride in ascending order (if ascending is TRUE) or descending order (if FALSE). Only works if the first entry of each block shares the same datatype.

- Argument `src` (list): List to be sorted.

- Argument `stride` (integer): Number of entries per block/stride (defaults to 1 if less than 1).

- Argument `ascending` (integer): Boolean. If TRUE, sorts in ascending order; if FALSE, sorts in descending order.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 184 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.


## llListSortStrided

```lsl
list llListSortStrided(list src, integer stride, integer stride_index, integer ascending)
```

- Purpose: Returns a copy of the list src sorted into blocks of stride by the element at stride_index in each block. Sorted in ascending order (if ascending is TRUE) or descending order (if FALSE).

- Argument `src` (list): List to be sorted.

- Argument `stride` (integer): Number of entries per block/stride (defaults to 1 if less than 1).

- Argument `stride_index` (integer): Zero-based index of the element within each stride to use as the sort key (negatives count backward from the end of the stride).

- Argument `ascending` (integer): Boolean. If TRUE, sorts in ascending order; if FALSE, sorts in descending order.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 802 | Native: False | Pure (no side effects): False

- Categories: list

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- SLua: deprecated in favour of `table.sort`. Prefer structured tables over strided lists.


## llListStatistics

```lsl
float llListStatistics(integer operation, list src)
```

- Purpose: Returns the numeric result of the statistical aggregate function operation (a LIST_STAT_* constant) on the numeric list src.

- Argument `operation` (integer): LIST_STAT_* constant of the statistical operation to perform.

- Argument `src` (list): List of numbers to analyze.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 315 | Native: False | Pure (no side effects): False

- Categories: list, math

- Guidance (list): Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llListen

```lsl
integer llListen(integer channel, string name, key id, string msg)
```

- Purpose: Creates a listener on channel from name and id for msg. Returns an integer listener handle used to control or remove the listener. Empty strings or NULL_KEY filters do not filter on those parameters.

- Argument `channel` (integer): Chat channel (any 32-bit signed integer value) to listen on. Exact range is -2147483648 to 2147483647.

- Argument `name` (string): Specific prim name or agent legacy name to filter by (or empty string for no filter).

- Argument `id` (key): Specific agent or prim UUID to filter by (or NULL_KEY for no filter).

- Argument `msg` (string): Specific chat message string to filter by (or empty string for no filter).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 25 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, script_communication


## llListenControl

```lsl
void llListenControl(integer handle, integer active)
```

- Purpose: Enables or disables the listener specified by the integer handle. If active is TRUE, the listener is activated; if FALSE, it is deactivated.

- Argument `handle` (integer): Integer listener handle returned by llListen.

- Argument `active` (integer): Boolean. If TRUE, activates the listener; if FALSE, deactivates it.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 26 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, script_communication


## llListenRemove

```lsl
void llListenRemove(integer handle)
```

- Purpose: Completely removes the listener specified by the integer handle.

- Argument `handle` (integer): Integer listener handle returned by llListen to remove.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 27 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, script_communication


## llLoadURL

```lsl
void llLoadURL(key avatar, string message, string url)
```

- Purpose: Shows a dialog box displaying message to the avatar avatar offering to open the specified url. Clicking yes launches the URL in their default web browser.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Argument `message` (string): Text message to display in the dialog box.

- Argument `url` (string): Web URL to open.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 297 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, user_interface, web

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llLog

```lsl
float llLog(float val)
```

- Purpose: Returns natural (base e) logarithm of val. If negative, return 0.0.

- Argument `val` (float): Number to compute the logarithm of.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 265 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.log`. Double precision; fastcall.


## llLog10

```lsl
float llLog10(float val)
```

- Purpose: Returns base-10 (common) logarithm of val. If negative, return 0.0.

- Argument `val` (float): Number to compute the logarithm of.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 264 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.log10`. Double precision; fastcall.


## llLookAt

```lsl
void llLookAt(vector target, float strength, float damping)
```

- Purpose: Causes the object to orient its positive Z-axis (up axis) toward the target vector, keeping its positive X-axis (forward axis) below the horizon. Tracks target until llStopLookAt is called or strength is set to 0.0.

- Argument `target` (vector): Target position vector in region coordinates to look at.

- Argument `strength` (float): Force of rotation (0.0 cancels the tracking; values around half the object's mass are typical).

- Argument `damping` (float): Timescale in seconds to critically damp the orientation.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 105 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llLoopSound

```lsl
void llLoopSound(string sound, float volume)
```

- Purpose: Plays the attached sound looping indefinitely at the specified volume. Only one sound can be attached to a prim at a time; new loops adjust the volume of the currently playing sound without restarting it.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 87 | Native: False | Pure (no side effects): False

- Categories: sound


## llLoopSoundMaster

```lsl
void llLoopSoundMaster(string sound, float volume)
```

- Purpose: Plays the attached sound looping indefinitely at the specified volume and declares it a Sync Master, forcing slave sounds to synchronize with it.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 88 | Native: False | Pure (no side effects): False

- Categories: sound


## llLoopSoundSlave

```lsl
void llLoopSoundSlave(string sound, float volume)
```

- Purpose: Plays the attached sound looping indefinitely at the specified volume, synchronized to the most audible active Sync Master in range.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 89 | Native: False | Pure (no side effects): False

- Categories: sound


## llMD5String

```lsl
string llMD5String(string src, integer nonce)
```

- Purpose: Returns a string of 32 hex characters representing the MD5 checksum of src salted with nonce (formatted as ':' + nonce).

- Argument `src` (string): Source string to hash.

- Argument `nonce` (integer): Nonce string used as a salt.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 258 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llMakeExplosion

```lsl
void llMakeExplosion(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset)
```

- Purpose: Deprecated. Generates a circular explosion of particles. Use llParticleSystem instead.

- Argument `particles` (integer): 

- Argument `scale` (float): 

- Argument `vel` (float): 

- Argument `lifetime` (float): 

- Argument `arc` (float): 

- Argument `texture` (string): Name of a texture in the prim's inventory, or a UUID.

- Argument `offset` (vector): Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 100 | Native: False | Pure (no side effects): False

- Categories: effects

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.ParticleSystem'}


## llMakeFire

```lsl
void llMakeFire(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset)
```

- Purpose: Deprecated. Generates fire-like particles. Use llParticleSystem instead.

- Argument `particles` (integer): 

- Argument `scale` (float): 

- Argument `vel` (float): 

- Argument `lifetime` (float): 

- Argument `arc` (float): 

- Argument `texture` (string): Name of a texture in the prim's inventory, or a UUID.

- Argument `offset` (vector): Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 103 | Native: False | Pure (no side effects): False

- Categories: effects

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.ParticleSystem'}


## llMakeFountain

```lsl
void llMakeFountain(integer particles, float scale, float vel, float lifetime, float arc, integer bounce, string texture, vector offset, float bounce_offset)
```

- Purpose: Deprecated. Generates a fountain of particles. Use llParticleSystem instead.

- Argument `particles` (integer): 

- Argument `scale` (float): 

- Argument `vel` (float): 

- Argument `lifetime` (float): 

- Argument `arc` (float): 

- Argument `bounce` (integer): 

- Argument `texture` (string): Name of a texture in the prim's inventory, or a UUID.

- Argument `offset` (vector): Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).

- Argument `bounce_offset` (float): 

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 101 | Native: False | Pure (no side effects): False

- Categories: effects

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.ParticleSystem'}


## llMakeSmoke

```lsl
void llMakeSmoke(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset)
```

- Purpose: Deprecated. Generates smoke-like particles. Use llParticleSystem instead.

- Argument `particles` (integer): 

- Argument `scale` (float): 

- Argument `vel` (float): 

- Argument `lifetime` (float): 

- Argument `arc` (float): 

- Argument `texture` (string): Name of a texture in the prim's inventory, or a UUID.

- Argument `offset` (vector): Offset relative to the prim's position (expressed in local coordinates; completely ignored by the system).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 102 | Native: False | Pure (no side effects): False

- Categories: effects

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.ParticleSystem'}


## llManageEstateAccess

```lsl
integer llManageEstateAccess(integer action, key avatar)
```

- Purpose: Adds or removes agents from the estate's access or ban lists, or groups from the estate's group access list, specified by the action. Returns TRUE if successful, or FALSE if throttled, if the action/ID is invalid, or if the script owner lacks estate management rights.

- Argument `action` (integer): An ESTATE_ACCESS_* action flag specifying the operation to perform.

- Argument `avatar` (key): UUID of the avatar or group to add or remove.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 393 | Native: False | Pure (no side effects): False

- Categories: land_moderation


## llMapBeacon

```lsl
void llMapBeacon(string region_name, vector pos, list options)
```

- Purpose: Displays an in-world beacon and optionally opens the world map for the avatar touching or wearing the object, centered on region_name with pos highlighted. Only works for attached scripts or during touch events.

- Argument `region_name` (string): Name of the region where the beacon is displayed.

- Argument `pos` (vector): Position vector in region coordinates to highlight.

- Argument `options` (list): A list of options to configure the map beacon.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 516 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, user_interface

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llMapDestination

```lsl
void llMapDestination(string simname, vector pos, vector look_at)
```

- Purpose: Opens the world map for the avatar touching or wearing the object, centered on simname with pos highlighted. Only works for attached scripts or during touch events. Note: look_at currently has no effect.

- Argument `simname` (string): Name of the target simulator region.

- Argument `pos` (vector): Position vector in region coordinates to highlight.

- Argument `look_at` (vector): Position in local coordinates (currently unused/ignored).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 309 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, teleport, user_interface

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llMessageLinked

```lsl
void llMessageLinked(integer link, integer num, string str, key id)
```

- Purpose: Triggers a link_message event, sending num, str, and id to the scripts in the prim(s) specified by link to allow scripts within the same object to communicate.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag controlling which prim(s) receive the message.

- Argument `num` (integer): An integer value passed as the second parameter of the link_message event.

- Argument `str` (string): A string value passed as the third parameter of the link_message event.

- Argument `id` (key): A key value passed as the fourth parameter of the link_message event.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 164 | Native: False | Pure (no side effects): False

- Categories: script_communication


## llMinEventDelay

```lsl
void llMinEventDelay(float delay)
```

- Purpose: Sets the minimum delay time between events being handled (minimums and defaults vary by event type).

- Argument `delay` (float): Minimum delay duration in seconds.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 125 | Native: False | Pure (no side effects): False

- Categories: script


## llModPow

```lsl
integer llModPow(integer base, integer exponent, integer modulus)
```

- Purpose: Returns base raised to the power exponent, modulo modulus (i.e., (b^e)%m). All inputs are wrapped to unsigned 32-bit integer range [0..4294967295]. Output is wrapped to signed 32-bit integer range [-2147483648..2147483647]. Will never overflow, unlike (b^e), which can overflow to inf.

- Argument `base` (integer): 32-bit unsigned integer base.

- Argument `exponent` (integer): 32-bit unsigned integer exponent.

- Argument `modulus` (integer): 32-bit unsigned integer modulus.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 300 | Native: False | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llModifyLand

```lsl
void llModifyLand(integer action, integer brush)
```

- Purpose: Modifies the terrain using the specified land action and brush size (0, 1, or 2, corresponding to 2m x 2m, 4m x 4m, or 8m x 8m).

- Argument `action` (integer): LAND_* action flag to perform (e.g., LAND_LEVEL, LAND_RAISE, LAND_LOWER, LAND_SMOOTH, LAND_NOISE, or LAND_REVERT).

- Argument `brush` (integer): Brush size (0, 1, or 2, representing 2m x 2m, 4m x 4m, or 8m x 8m).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 159 | Native: False | Pure (no side effects): False

- Categories: region


## llMoveToTarget

```lsl
void llMoveToTarget(vector target, float tau)
```

- Purpose: Critically damps the physical object's motion to position target in tau seconds. Setting tau to 0.0 stops the critical damping; recommended tau values are greater than 0.2.

- Argument `target` (vector): Target position vector in region coordinates.

- Argument `tau` (float): Timescale in seconds to critically damp the movement.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 70 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llName2Key

```lsl
key llName2Key(string name)
```

- Purpose: Requests the key (UUID) of the avatar name in the current region. Returns NULL_KEY if no matching agent is present. Formats are 'First Last' or 'first.last' (assumes 'Resident' if last name is omitted; case-insensitive).

- Argument `name` (string): Name of the avatar (e.g., 'First Last' or 'first.last').

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 524 | Native: False | Pure (no side effects): False

- Categories: avatar

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llNavigateTo

```lsl
void llNavigateTo(vector pos, list options)
```

- Purpose: Directs a pathfinding character to navigate to the position pos (located in the current or adjacent regions) using the parameters specified in options.

- Argument `pos` (vector): Destination position vector in region coordinates.

- Argument `options` (list): A list of parameters to configure pathfinding behavior (currently only FORCE_DIRECT_PATH is supported).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 398 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llOffsetTexture

```lsl
void llOffsetTexture(float u, float v, integer face)
```

- Purpose: Sets the texture horizontal (u) and vertical (v) offsets for the chosen face. If face is ALL_SIDES, offsets all faces.

- Argument `u` (float): Horizontal (U) offset, typically in the interval [-1.0, 1.0].

- Argument `v` (float): Vertical (V) offset, typically in the interval [-1.0, 1.0].

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 55 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llOpenFloater

```lsl
integer llOpenFloater(string floater_name, string url, list params)
```

- Purpose: Opens the specified viewer floater_name loaded with url and configured via params. Returns an integer error code, or 0 if successful.

- Argument `floater_name` (string): Identifier string of the viewer floater to open.

- Argument `url` (string): URL to load within the opened floater.

- Argument `params` (list): Options or parameters to apply to the opened floater.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 604 | Native: False | Pure (no side effects): False

- Categories: avatar_communication


## llOpenRemoteDataChannel

```lsl
void llOpenRemoteDataChannel()
```

- Purpose: Deprecated. Creates a channel to listen for incoming XML-RPC calls, triggering a remote_data event with the channel ID once available.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 254 | Native: False | Pure (no side effects): False

- Categories: script_communication

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: True


## llOrd

```lsl
integer llOrd(string val, integer index)
```

- Purpose: Returns the ordinal (Unicode copepoint integer) of the character at index in the string val. Negative indices count backward from the end of the string.

- Argument `val` (string): Source string.

- Argument `index` (integer): Codepoint index of the character to convert. Supports negative indexing.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 527 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llOverMyLand

```lsl
integer llOverMyLand(key id)
```

- Purpose: Returns TRUE if the avatar or object specified by key id is over land owned by the script owner, or FALSE otherwise.

- Argument `id` (key): UUID of the group, avatar, or object to check.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 215 | Native: False | Pure (no side effects): False

- Categories: parcel


## llOwnerSay

```lsl
void llOwnerSay(string msg)
```

- Purpose: Sends the chat message msg privately to the object owner (the owner must be currently in the same region for the message to be received).

- Argument `msg` (string): Text message string to send to the object owner.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 292 | Native: False | Pure (no side effects): False

- Categories: avatar_communication

- SLua: deprecated in favour of `print`. 


## llParcelMediaCommandList

```lsl
void llParcelMediaCommandList(list commandList)
```

- Purpose: Controls the playback of movies and other multimedia resources on a parcel or for an agent, using the PARCEL_MEDIA_COMMAND_* settings specified in commandList.

- Argument `commandList` (list): A list containing integer PARCEL_MEDIA_COMMAND_* flags and their corresponding parameters.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 2.0 s | Function ID: 298 | Native: False | Pure (no side effects): False

- Categories: media, parcel, parcel_media

- Delay warning: this call sleeps the script for 2.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llParcelMediaQuery

```lsl
list llParcelMediaQuery(list query)
```

- Purpose: Queries the media properties of the parcel containing the script, returning a list of values in the order requested by query. Only works if the object is owned by the landowner or deeded to the land's group.

- Argument `query` (list): A list of PARCEL_MEDIA_COMMAND_* attributes to query.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 2.0 s | Function ID: 299 | Native: False | Pure (no side effects): False

- Categories: media, parcel, parcel_media

- Delay warning: this call sleeps the script for 2.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llParseString2List

```lsl
list llParseString2List(string src, list separators, list spacers)
```

- Purpose: Breaks the string src into a list of substrings, discarding any separators, keeping spacers, and omitting any empty null values. separators and spacers accept up to 8 string entries each.

- Argument `src` (string): Source string to parse.

- Argument `separators` (list): A list of up to 8 strings representing separators to be discarded.

- Argument `spacers` (list): A list of up to 8 strings representing spacers to be preserved in the list.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 214 | Native: False | Pure (no side effects): True

- Categories: data_conversion


## llParseStringKeepNulls

```lsl
list llParseStringKeepNulls(string src, list separators, list spacers)
```

- Purpose: Breaks the string src into a list of substrings, discarding separators and keeping spacers, while preserving empty null values (unlike llParseString2List). separators and spacers accept up to 8 string entries each.

- Argument `src` (string): Source string to parse.

- Argument `separators` (list): A list of up to 8 strings representing separators to be discarded.

- Argument `spacers` (list): A list of up to 8 strings representing spacers to be preserved in the list.

- Returns: list

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 285 | Native: False | Pure (no side effects): True

- Categories: data_conversion


## llParticleSystem

```lsl
void llParticleSystem(list rules)
```

- Purpose: Creates or updates a particle system on the prim containing the script based on rules. An empty list removes the particle system.

- Argument `rules` (list): A list of particle system rules and data pairs [rule1, data1, ...].

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 229 | Native: False | Pure (no side effects): False

- Categories: effects, particles


## llPassCollisions

```lsl
void llPassCollisions(integer pass)
```

- Purpose: Sets the pass-collisions attribute. If pass is TRUE, collision events are passed from child prims to the root; if FALSE (default), they only trigger events in the affected child prim.

- Argument `pass` (integer): A PASS_* flag (e.g., PASS_ALWAYS, PASS_IF_NOT_HANDLED, or PASS_NEVER).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 166 | Native: False | Pure (no side effects): False

- Categories: physics, sensor


## llPassTouches

```lsl
void llPassTouches(integer pass)
```

- Purpose: Sets the pass-touches attribute. If pass is TRUE, touch events are passed from child prims to the root; if FALSE (default), they only trigger events in the affected child prim.

- Argument `pass` (integer): A PASS_* flag (e.g., PASS_ALWAYS, PASS_IF_NOT_HANDLED, or PASS_NEVER).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 154 | Native: False | Pure (no side effects): False

- Categories: touch


## llPatrolPoints

```lsl
void llPatrolPoints(list patrolPoints, list options)
```

- Purpose: Directs a pathfinding character to patrol sequentially through the coordinates specified in patrolPoints, configured by options.

- Argument `patrolPoints` (list): A list of at least two position vectors representing the patrol path.

- Argument `options` (list): A list of PATROL_* flags and parameters to configure the patrol behavior.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 403 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llPlaySound

```lsl
void llPlaySound(string sound, float volume)
```

- Purpose: Plays the specified sound once at volume, attached to the object. Only one sound can be attached to a prim at a time; new sounds or calling llStopSound stops previous playback. A second call with the same sound adjusts the volume without restarting it.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 86 | Native: False | Pure (no side effects): False

- Categories: sound


## llPlaySoundSlave

```lsl
void llPlaySoundSlave(string sound, float volume)
```

- Purpose: Plays the attached sound once at volume, synchronized to the next loop point of the most audible active Sync Master.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 90 | Native: False | Pure (no side effects): False

- Categories: sound


## llPointAt

```lsl
void llPointAt(vector pos)
```

- Purpose: Directs the avatar owning the object to point at the vector pos.

- Argument `pos` (vector): Position vector to point at.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 131 | Native: False | Pure (no side effects): False

- Categories: movement, physics

- Deprecated in LSL: True


## llPow

```lsl
float llPow(float base, float exponent)
```

- Purpose: Returns base raised to the power exponent. If result is imaginary, returns NaN.

- Argument `base` (float): Base number.

- Argument `exponent` (float): Exponent number.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 5 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `^`. Double precision; operator.


## llPreloadSound

```lsl
void llPreloadSound(string sound)
```

- Purpose: Causes nearby viewers in range to preload the specified sound from the object's inventory to prevent playback delays.

- Argument `sound` (string): Name of the sound in the prim's inventory, or a UUID.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 93 | Native: False | Pure (no side effects): False

- Categories: sound

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llPursue

```lsl
void llPursue(key target, list options)
```

- Purpose: Directs a pathfinding character to pursue and chase target, configured by the parameters specified in options.

- Argument `target` (key): UUID of the group, avatar, or object to pursue.

- Argument `options` (list): A list of options to configure pursuit behavior.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 400 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llPushObject

```lsl
void llPushObject(key target, vector impulse, vector ang_impulse, integer is_local)
```

- Purpose: Applies physical impulse (force) and ang_impulse (rotational force) to the specified target avatar or object.

- Argument `target` (key): UUID of the target avatar or object in the same region.

- Argument `impulse` (vector): Linear impulse vector representing the direction and force of the push.

- Argument `ang_impulse` (vector): Angular impulse vector representing the rotational force.

- Argument `is_local` (integer): Boolean. If TRUE, forces are applied relative to the target's local axes; if FALSE, relative to region axes.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 165 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llReadKeyValue

```lsl
key llReadKeyValue(string k)
```

- Purpose: Starts an asynchronous transaction to read the value associated with key k in the experience. Returns a key query handle for the dataserver event. Fails with XP_ERROR_KEY_NOT_FOUND if the key does not exist.

- Argument `k` (string): Key of the key-value pair to read.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 388 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, experience, experience_data

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llRefreshPrimURL

```lsl
void llRefreshPrimURL()
```

- Purpose: Legacy function intended to reload the web page displayed on the prim's faces (currently non-functional).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 20.0 s | Function ID: 306 | Native: False | Pure (no side effects): False

- Categories: media, prim_media, web

- Delay warning: this call sleeps the script for 20.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.SetPrimMediaParams'}


## llRegionSay

```lsl
void llRegionSay(integer channel, string msg)
```

- Purpose: Broadcasts the message msg to all scripts listening on channel Channel within the region. PUBLIC_CHANNEL (0) cannot be used, so, only scripts can receive the message.

- Argument `channel` (integer): Chat channel (any 32-bit signed integer value except zero) to chat the message on.

- Argument `msg` (string): Text message string to broadcast.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 331 | Native: False | Pure (no side effects): False

- Categories: chat, script_communication


## llRegionSayTo

```lsl
void llRegionSayTo(key target, integer channel, string msg)
```

- Purpose: Sends the message msg on Channel privately to the targeted agent or object (if within the region). If target is an agent and channel is non-zero, the message can also be heard by any attachments worn by the avatar.

- Argument `target` (key): UUID of the target agent or prim in the same region.

- Argument `channel` (integer): Chat channel (any 32-bit signed integer value) to chat the message on.

- Argument `msg` (string): Text message string to send.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 364 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, script_communication


## llReleaseCamera

```lsl
void llReleaseCamera(key avatar)
```

- Purpose: Deprecated. Intended to return camera control back to the avatar (use llClearCameraParams instead).

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 116 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Deprecated in LSL: {'use': 'll.ClearCameraParams', 'selene-replace': ['ll.ClearCameraParams()']}


## llReleaseControls

```lsl
void llReleaseControls()
```

- Purpose: Stops taking inputs (previously acquired via llTakeControls) from the avatar, dequeuing any remaining control events and revoking the PERMISSION_TAKE_CONTROLS permission.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 112 | Native: False | Pure (no side effects): False

- Categories: avatar, input, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llReleaseURL

```lsl
void llReleaseURL(string url)
```

- Purpose: Releases the specified url (previously obtained via llRequestURL), rendering it no longer usable.

- Argument `url` (string): URL string to release.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 347 | Native: False | Pure (no side effects): False

- Categories: media, web


## llRemoteDataReply

```lsl
void llRemoteDataReply(key channel, key message_id, string sdata, integer idata)
```

- Purpose: Deprecated. Sends an XML-RPC reply on channel to message_id with payload string sdata and integer idata.

- Argument `channel` (key): XML-RPC channel ID.

- Argument `message_id` (key): XML-RPC message ID.

- Argument `sdata` (string): String payload data to reply with.

- Argument `idata` (integer): Integer payload data to reply with.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 3.0 s | Function ID: 256 | Native: False | Pure (no side effects): False

- Categories: script_communication

- Delay warning: this call sleeps the script for 3.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: True


## llRemoteDataSetRegion

```lsl
void llRemoteDataSetRegion()
```

- Purpose: Deprecated. Used with XML-RPC to reregister remote data channels if the object moves to another region.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 263 | Native: False | Pure (no side effects): False

- Categories: script_communication

- Deprecated in LSL: True


## llRemoteLoadScript

```lsl
void llRemoteLoadScript(key target, string script, integer running, integer start_param)
```

- Purpose: Deprecated.

- Argument `target` (key): UUID of the target prim.

- Argument `script` (string): Name of the script in the prim's inventory.

- Argument `running` (integer): Boolean. If TRUE, sets the copied script to run immediately; if FALSE, leaves it stopped.

- Argument `start_param` (integer): Integer start parameter passed to the copied script (readable via llGetStartParameter).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 3.0 s | Function ID: 251 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, script

- Delay warning: this call sleeps the script for 3.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: True


## llRemoteLoadScriptPin

```lsl
void llRemoteLoadScriptPin(key target, string script, integer pin, integer running, integer start_param)
```

- Purpose: Copies the script into target, setting it running (if running is TRUE) with the start_param, provided the script owner has modify permissions on target and target's PIN matches pin (set via llSetRemoteScriptAccessPin).

- Argument `target` (key): UUID of the target prim in the same region.

- Argument `script` (string): Name of the script in the prim's inventory.

- Argument `pin` (integer): Integer PIN code (must match the PIN set on the ObjectID via llSetRemoteScriptAccessPin).

- Argument `running` (integer): Boolean. If TRUE, sets the copied script to run immediately; if FALSE, leaves it stopped.

- Argument `start_param` (integer): Integer start parameter passed to the copied script (readable via llGetStartParameter).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 3.0 s | Function ID: 253 | Native: False | Pure (no side effects): False

- Categories: prim, prim_inventory, script

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 3.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRemoveFromLandBanList

```lsl
void llRemoveFromLandBanList(key avatar)
```

- Purpose: Removes the specified avatar from the land parcel's ban list.

- Argument `avatar` (key): UUID of the avatar to remove.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 312 | Native: False | Pure (no side effects): False

- Categories: land_moderation, parcel

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRemoveFromLandPassList

```lsl
void llRemoveFromLandPassList(key avatar)
```

- Purpose: Removes the specified avatar from the land parcel's pass/access list.

- Argument `avatar` (key): UUID of the avatar to remove.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 311 | Native: False | Pure (no side effects): False

- Categories: land_moderation, parcel

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRemoveInventory

```lsl
void llRemoveInventory(string item)
```

- Purpose: Permanently deletes the named inventory item from the prim's inventory.

- Argument `item` (string): Name of the item in the prim's inventory to remove.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 151 | Native: False | Pure (no side effects): False

- Categories: prim_inventory


## llRemoveVehicleFlags

```lsl
void llRemoveVehicleFlags(integer flags)
```

- Purpose: Disables the specified vehicle flags (sets them to FALSE) using the bitwise mask flags.

- Argument `flags` (integer): A bitwise mask of VEHICLE_FLAG_* constants to disable.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 237 | Native: False | Pure (no side effects): False

- Categories: physics, vehicles


## llReplaceAgentEnvironment

```lsl
integer llReplaceAgentEnvironment(key agent_id, float transition, string environment)
```

- Purpose: Replaces the region and parcel environment seen by the specified agent_id as part of an experience, transitioning the settings over transition seconds. Passing NULL_KEY or an empty string for environment restores defaults.

- Argument `agent_id` (key): UUID of an agent in the region participating in the experience.

- Argument `transition` (float): Duration in seconds over which to transition to the new environment.

- Argument `environment` (string): Name of an environmental setting in inventory, or its asset UUID (or empty string/NULL_KEY to clear).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 713 | Native: False | Pure (no side effects): False

- Categories: avatar, experience, parcel_appearance, region_appearance

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llReplaceEnvironment

```lsl
integer llReplaceEnvironment(vector position, string environment, integer track_no, integer day_length, integer day_offset)
```

- Purpose: Replaces the environment on the parcel containing position (or the entire region if position is <-1.0, -1.0, -1.0>) for the specified track_no. Modifies day_length and day_offset if specified. Requires edit permissions on the parcel or estate management rights.

- Argument `position` (vector): Position vector of the target parcel (the Z component is ignored; use <-1.0, -1.0, -1.0> for the entire region).

- Argument `environment` (string): Name of an environmental setting in inventory, or its asset UUID (or empty string/NULL_KEY to clear).

- Argument `track_no` (integer): The elevation track to change (0: water, 1: ground, 2: 1000m, 3: 2000m, 4: 3000m, -1: all tracks).

- Argument `day_length` (integer): Day cycle length in seconds (-1 to leave unchanged).

- Argument `day_offset` (integer): Day cycle offset in seconds from UTC (-1 to leave unchanged).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 718 | Native: False | Pure (no side effects): False

- Categories: parcel, parcel_appearance


## llReplaceSubString

```lsl
string llReplaceSubString(string src, string pattern, string replacement_pattern, integer count)
```

- Purpose: Returns a copy of src with count occurrences of pattern replaced by replacement_pattern. Setting count to 0 replaces all occurrences; positive counts process left-to-right, while negative counts process right-to-left.

- Argument `src` (string): Original source string to search.

- Argument `pattern` (string): Substring pattern to find and replace.

- Argument `replacement_pattern` (string): New substring that replaces the pattern.

- Argument `count` (integer): Maximum number of replacements to make (0 for all, positive for left-to-right, negative for right-to-left).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 541 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llRequestAgentData

```lsl
key llRequestAgentData(key id, integer data)
```

- Purpose: Asynchronously requests the specified data category (DATA_*) about the agent id. Triggers a dataserver event with the results and returns a key query handle.

- Argument `id` (key): UUID of the agent.

- Argument `data` (integer): DATA_* category flag of the requested information.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 155 | Native: False | Pure (no side effects): False

- Categories: avatar, dataserver

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRequestDisplayName

```lsl
key llRequestDisplayName(key id)
```

- Purpose: Asynchronously requests the display name of the agent specified by id, triggering a dataserver event with the results. The agent does not need to be online or in the region. Returns a key query handle.

- Argument `id` (key): UUID of the avatar to query.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 361 | Native: False | Pure (no side effects): False

- Categories: avatar, dataserver

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llRequestExperiencePermissions

```lsl
void llRequestExperiencePermissions(key agent, string name)
```

- Purpose: Requests permission from the specified agent to participate in the experience. These permissions are persistent and apply grid-wide across all scripts in the experience, automatically triggering experience_permissions or experience_permissions_denied.

- Argument `agent` (key): UUID of the agent to request permissions from.

- Argument `name` (string): Deprecated parameter (no longer used).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 384 | Native: False | Pure (no side effects): False

- Categories: avatar, experience, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llRequestInventoryData

```lsl
key llRequestInventoryData(string item)
```

- Purpose: Asynchronously requests data for the named inventory item, triggering a dataserver event. Currently, only landmark items are supported (which return local region coordinates). Returns a key query handle.

- Argument `item` (string): Name of the item in the prim's inventory.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 156 | Native: False | Pure (no side effects): False

- Categories: dataserver, prim_inventory

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRequestPermissions

```lsl
void llRequestPermissions(key agent, integer permissions)
```

- Purpose: Requests permissions (a bitfield specified by permissions) from the agent in the same region, calling run_time_permissions if granted. This call does not pause script execution.

- Argument `agent` (key): UUID of the agent in the same region.

- Argument `permissions` (integer): Bitfield containing the PERMISSION_* constants to request.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 136 | Native: False | Pure (no side effects): False

- Categories: permissions


## llRequestSecureURL

```lsl
key llRequestSecureURL()
```

- Purpose: Asynchronously requests one secure HTTPS (SSL, port 12043) URL for use by this object, triggering an http_request event. Returns a key query handle.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 346 | Native: False | Pure (no side effects): False

- Categories: media, script_communication, web


## llRequestSimulatorData

```lsl
key llRequestSimulatorData(string region, integer data)
```

- Purpose: Asynchronously requests data (using a DATA_SIM_* constant) about the region. Triggers a dataserver event and returns a key query handle.

- Argument `region` (string): Case-sensitive region name.

- Argument `data` (integer): DATA_SIM_* flag of the requested simulator data.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 293 | Native: False | Pure (no side effects): False

- Categories: dataserver, region

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRequestURL

```lsl
key llRequestURL()
```

- Purpose: Asynchronously requests one HTTP URL for use by this script, triggering an http_request event. Returns a key query handle.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 345 | Native: False | Pure (no side effects): False

- Categories: media, script_communication, web


## llRequestUserKey

```lsl
key llRequestUserKey(string username)
```

- Purpose: Asynchronously requests the Agent ID key (UUID) for the agent specified by their current or historical username, returning NULL_KEY if not found. Returns a key query handle for the dataserver event.

- Argument `username` (string): Current or historical username of the avatar to resolve.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 525 | Native: False | Pure (no side effects): False

- Categories: avatar, dataserver, uuid

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llRequestUsername

```lsl
key llRequestUsername(key id)
```

- Purpose: Asynchronously requests the unique single-word username of the agent identified by id, triggering a dataserver event. The agent does not need to be online or in the region. Returns a key query handle.

- Argument `id` (key): UUID of the avatar to query.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 359 | Native: False | Pure (no side effects): False

- Categories: avatar, dataserver

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llResetAnimationOverride

```lsl
void llResetAnimationOverride(string anim_state)
```

- Purpose: Resets the animation override for anim_state to its default value (use 'ALL' to reset all states). Requires the PERMISSION_OVERRIDE_ANIMATIONS permission.

- Argument `anim_state` (string): Animation state string (or 'ALL') to reset.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 502 | Native: False | Pure (no side effects): False

- Categories: avatar_animation, permissions


## llResetLandBanList

```lsl
void llResetLandBanList()
```

- Purpose: Removes all blocked residents from the land parcel's ban list.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 321 | Native: False | Pure (no side effects): False

- Categories: land_moderation, parcel

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llResetLandPassList

```lsl
void llResetLandPassList()
```

- Purpose: Removes all residents from the land parcel's access/pass list.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.1 s | Function ID: 322 | Native: False | Pure (no side effects): False

- Categories: land_moderation, parcel

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llResetOtherScript

```lsl
void llResetOtherScript(string script)
```

- Purpose: Resets the named script name in the prim's inventory.

- Argument `script` (string): Name of the target script in the prim's inventory.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 249 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, script


## llResetScript

```lsl
void llResetScript()
```

- Purpose: Resets the current script.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 163 | Native: False | Pure (no side effects): False

- Categories: script


## llResetTime

```lsl
void llResetTime()
```

- Purpose: Resets the script's elapsed time timer back to zero.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 83 | Native: False | Pure (no side effects): False

- Categories: script


## llReturnObjectsByID

```lsl
integer llReturnObjectsByID(list objects)
```

- Purpose: Returns objects specified by the list of UUIDs objects to their owners. Requires the PERMISSION_RETURN_OBJECTS permission, and the script owner must own the parcel or be an estate manager/region owner.

- Argument `objects` (list): A list of object UUID keys to return.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 520 | Native: False | Pure (no side effects): False

- Categories: land_moderation, rez


## llReturnObjectsByOwner

```lsl
integer llReturnObjectsByOwner(key owner, integer scope)
```

- Purpose: Returns objects owned by owner within the specified scope (parcel, parcel owner, or region). Requires the PERMISSION_RETURN_OBJECTS permission, and the script owner must own the parcel or be an estate manager/region owner.

- Argument `owner` (key): UUID of the avatar or group whose objects will be returned.

- Argument `scope` (integer): OBJECT_RETURN_* scope flag (such as OBJECT_RETURN_PARCEL, OBJECT_RETURN_PARCEL_OWNER, or OBJECT_RETURN_REGION).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 521 | Native: False | Pure (no side effects): False

- Categories: land_moderation, rez


## llRezAtRoot

```lsl
void llRezAtRoot(string item, vector pos, vector vel, rotation rot, integer start_param)
```

- Purpose: Instantiates the named inventory object with the root prim at pos with velocity vel and rotation rot, passing start_param as the on_rez start parameter. The vel parameter is ignored if the rezzed object is non-physical.

- Argument `item` (string): Name of the object in the prim's inventory to rez.

- Argument `pos` (vector): Position vector in region coordinates where the root of the object will be placed.

- Argument `vel` (vector): Initial velocity vector for the rezzed object.

- Argument `rot` (rotation): Initial rotation of the rezzed object.

- Argument `start_param` (integer): Start parameter passed to the rezzed object's on_rez event (accessible via llGetStartParameter).

- Returns: void

- Energy cost: 200.0 | Script sleep after call: 0.1 s | Function ID: 286 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, rez

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRezObject

```lsl
void llRezObject(string item, vector pos, vector vel, rotation rot, integer start_param)
```

- Purpose: Instantiates the named inventory object with the bounding box centered at pos with velocity vel and rotation rot, passing param as the on_rez start parameter. The vel parameter is ignored if the rezzed object is non-physical.

- Argument `item` (string): Name of the object in the prim's inventory to rez.

- Argument `pos` (vector): Position vector in region coordinates where the center of the object will be placed.

- Argument `vel` (vector): Initial velocity vector (maximum magnitude ~200m/s).

- Argument `rot` (rotation): Initial rotation of the rezzed object.

- Argument `start_param` (integer): Start parameter passed to the rezzed object's on_rez event (accessible via llGetStartParameter).

- Returns: void

- Energy cost: 200.0 | Script sleep after call: 0.1 s | Function ID: 104 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, rez

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRezObjectWithParams

```lsl
key llRezObjectWithParams(string item, list options)
```

- Purpose: Instantiates the named inventory object (defaulting to the rezzing prim's position unless REZ_POS is specified) using the initial set of parameters specified in options. Returns the key of the rezzed object, or a blank key on failure.

- Argument `item` (string): Name of the object in the prim's inventory to rez.

- Argument `options` (list): A list of REZ_* options to configure the rezzed object's attributes.

- Returns: key

- Energy cost: 200.0 | Script sleep after call: 0.1 s | Function ID: 544 | Native: False | Pure (no side effects): False

- Categories: combat, prim_inventory, rez

- Delay warning: this call sleeps the script for 0.1 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRot2Angle

```lsl
float llRot2Angle(rotation q)
```

- Purpose: Returns the angle, in radians, that q rotates.

- Argument `q` (rotation): Rotation to evaluate.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 171 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llRot2Axis

```lsl
vector llRot2Axis(rotation q)
```

- Purpose: Returns the unit vector axis that q rotates around.

- Argument `q` (rotation): Rotation to evaluate.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 170 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llRot2Euler

```lsl
vector llRot2Euler(rotation q)
```

- Purpose: Returns a vector of Euler angles (roll, pitch, yaw) of q. The angles will be in radians.

- Argument `q` (rotation): Rotation to convert.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 15 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, quaternion

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llRot2Fwd

```lsl
vector llRot2Fwd(rotation q)
```

- Purpose: Returns the unit vector pointing toward positive X (forward) in the coordinate space of rotation q. Equivalent to <1, 0, 0> * q.

- Argument `q` (rotation): Rotation to convert.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 18 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `quaternion.tofwd`. 


## llRot2Left

```lsl
vector llRot2Left(rotation q)
```

- Purpose: Returns the unit vector pointing toward positive Y (left) in the coordinate space of rotation q. Equivalent to <0, 1, 0> * q.

- Argument `q` (rotation): Rotation to convert.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 19 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `quaternion.toleft`. 


## llRot2Up

```lsl
vector llRot2Up(rotation q)
```

- Purpose: Returns the unit vector pointing toward positive Z (up) in the coordinate space of rotation q. Equivalent to <0, 0, 1> * q.

- Argument `q` (rotation): Rotation to convert.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 20 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `quaternion.toup`. 


## llRotBetween

```lsl
rotation llRotBetween(vector start_vec, vector end_vec)
```

- Purpose: Returns the shortest-path quaternion that rotates start_vec onto end_vec.

- Argument `start_vec` (vector): Starting vector.

- Argument `end_vec` (vector): Ending vector.

- Returns: rotation

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 21 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, math_trig, quaternion

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.


## llRotLookAt

```lsl
void llRotLookAt(rotation target_direction, float strength, float damping)
```

- Purpose: Causes the object to smoothly rotate to target_direction with a force defined by strength and damping. A strength of 0.0 cancels the rotation target. Rotation is maintained until stopped with llStopLookAt.

- Argument `target_direction` (rotation): Target rotation to align the object with.

- Argument `strength` (float): Force of rotation (0.0 cancels the tracking; values around half the object's mass are typical).

- Argument `damping` (float): Timescale in seconds to critically damp the rotation.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 127 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llRotTarget

```lsl
integer llRotTarget(rotation rot, float error)
```

- Purpose: Registers the rotation rot with a leeway tolerance error (in radians) as a target, triggering at_rot_target and not_at_rot_target events. Returns an integer handle to unregister the target via llRotTargetRemove.

- Argument `rot` (rotation): Target rotation to track.

- Argument `error` (float): Tolerance angle in radians defining when the target rotation is considered reached.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 68 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llRotTargetRemove

```lsl
void llRotTargetRemove(integer handle)
```

- Purpose: Removes the rotational target specified by the integer handle registered with llRotTarget.

- Argument `handle` (integer): Integer target handle returned by llRotTarget to remove.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 69 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llRotateTexture

```lsl
void llRotateTexture(float angle, integer face)
```

- Purpose: Sets the texture rotation of face to the specified angle (in radians). If face is ALL_SIDES, rotates the texture on all faces.

- Argument `angle` (float): Rotation angle expressed in radians.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 56 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llRound

```lsl
integer llRound(float val)
```

- Purpose: Returns val rounded to the nearest integer. Halfway values are rounded toward infinity.

- Argument `val` (float): Number to round.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 11 | Native: False | Pure (no side effects): False

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.round`. Fastcall.


## llSHA1String

```lsl
string llSHA1String(string src)
```

- Purpose: Returns a string of 40 hex characters representing the SHA-1 security hash of src.

- Argument `src` (string): Source string to hash.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 343 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llSHA256String

```lsl
string llSHA256String(string src)
```

- Purpose: Returns a string of 64 hex characters representing the SHA-256 security hash of src.

- Argument `src` (string): Source string to hash.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 531 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llSameGroup

```lsl
integer llSameGroup(key uuid)
```

- Purpose: Returns TRUE if the agent or object specified by uuid is in the same region (simulator) and shares the same active group as the prim containing the script; returns FALSE otherwise.

- Argument `uuid` (key): UUID of the group, avatar, or prim to check.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 219 | Native: False | Pure (no side effects): False

- Categories: object

- Guidance (object): Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.


## llSay

```lsl
void llSay(integer channel, string msg)
```

- Purpose: Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv("chat_range"), which is 20m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.

- Argument `channel` (integer): Chat channel (any 32-bit signed integer value) to chat the message on.

- Argument `msg` (string): Text message string to broadcast.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 23 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, script_communication


## llScaleByFactor

```lsl
integer llScaleByFactor(float scaling_factor)
```

- Purpose: Attempts to uniformly resize the entire object by scaling_factor, maintaining size-position ratios of the prims. Fails if the linkset is physical, a pathfinding character, in keyframed motion, would exceed prim scale/linkability limits, or would overflow parcel capacity.

- Argument `scaling_factor` (float): Multiplier scale factor to apply to the prim sizes and their local positions.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 592 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llScaleTexture

```lsl
void llScaleTexture(float u, float v, integer face)
```

- Purpose: Sets the diffuse texture horizontal u and vertical v scales (repeats) on the specified face of the prim. Setting face to ALL_SIDES updates all sides. Negative scale values flip the texture.

- Argument `u` (float): Horizontal (U) texture repeats scale value, in the interval [-100.0, 100.0].

- Argument `v` (float): Vertical (V) texture repeats scale value, in the interval [-100.0, 100.0].

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 54 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llScriptDanger

```lsl
integer llScriptDanger(vector pos)
```

- Purpose: Returns TRUE if the vector position pos is over public land, sandbox land, land restricting edit/build permissions, or land that disables outside scripts.

- Argument `pos` (vector): Position vector in region coordinates to check.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 246 | Native: False | Pure (no side effects): False

- Categories: parcel, script


## llScriptProfiler

```lsl
void llScriptProfiler(integer flags)
```

- Purpose: Enables or disables the script's profiling state using flags (supports PROFILE_SCRIPT_MEMORY on Mono, or PROFILE_NONE). Active profiling can significantly reduce script performance.

- Argument `flags` (integer): PROFILE_* flag (such as PROFILE_NONE or PROFILE_SCRIPT_MEMORY) to set the profiling state.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 367 | Native: False | Pure (no side effects): False

- Categories: script


## llSendRemoteData

```lsl
key llSendRemoteData(key channel, string dest, integer idata, string sdata)
```

- Purpose: Deprecated. Sends an XML-RPC request to dest on channel, containing the channel ID as a string, integer idata, and string sdata. Returns a key representing the message_id.

- Argument `channel` (key): XML-RPC channel ID.

- Argument `dest` (string): Destination XML-RPC URL or server.

- Argument `idata` (integer): Integer payload data.

- Argument `sdata` (string): String payload data.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 3.0 s | Function ID: 255 | Native: False | Pure (no side effects): False

- Categories: script_communication

- Delay warning: this call sleeps the script for 3.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: True


## llSensor

```lsl
void llSensor(string name, key id, integer type, float radius, float arc)
```

- Purpose: Performs a single scan from the prim's forward vector for name and id of type within radius meters and arc radians. Results trigger a sensor or no_sensor event. Passing empty filters (blank name, 0 type, or NULL_KEY id) disables that filter.

- Argument `name` (string): Specific object or avatar name to filter for (or empty string for no filter).

- Argument `id` (key): UUID of the group, avatar, or object to filter by (or NULL_KEY for no filter).

- Argument `type` (integer): Integer bitfield type mask containing AGENT, AGENT_BY_LEGACY_NAME, AGENT_BY_USERNAME, ACTIVE, PASSIVE, or SCRIPTED (0 for no filter).

- Argument `radius` (float): Maximum distance in meters to scan (range [0.0, 96.0]).

- Argument `arc` (float): Maximum angle in radians relative to the local X-axis to scan (range [0.0, PI]).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 28 | Native: False | Pure (no side effects): False

- Categories: sensor


## llSensorRemove

```lsl
void llSensorRemove()
```

- Purpose: Removes the periodic sensor previously configured by llSensorRepeat.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 30 | Native: False | Pure (no side effects): False

- Categories: sensor


## llSensorRepeat

```lsl
void llSensorRepeat(string name, key id, integer type, float radius, float arc, float rate)
```

- Purpose: Sets up a repeating periodic scan every rate seconds for name and id of type within radius meters and arc radians of the forward vector. Results trigger sensor or no_sensor events.

- Argument `name` (string): Specific object or avatar name to filter for (or empty string for no filter).

- Argument `id` (key): UUID of the group, avatar, or object to filter by (or NULL_KEY for no filter).

- Argument `type` (integer): Integer bitfield type mask containing AGENT, AGENT_BY_LEGACY_NAME, AGENT_BY_USERNAME, ACTIVE, PASSIVE, or SCRIPTED (0 for no filter).

- Argument `radius` (float): Maximum distance in meters to scan (range [0.0, 96.0]).

- Argument `arc` (float): Maximum angle in radians relative to the local X-axis to scan (range [0.0, PI]).

- Argument `rate` (float): Interval in seconds between repeated scans.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 29 | Native: False | Pure (no side effects): False

- Categories: sensor


## llSetAgentEnvironment

```lsl
integer llSetAgentEnvironment(key agent_id, float transition, list params)
```

- Purpose: Sets an individual agent's environmental settings using the attributes in params over a duration of transition seconds. Must be used as part of an experience; passing an empty list removes overrides.

- Argument `agent_id` (key): UUID of the agent participating in the experience.

- Argument `transition` (float): Transition duration in seconds.

- Argument `params` (list): A list of environmental parameters to apply.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 714 | Native: False | Pure (no side effects): False

- Categories: avatar, experience, parcel_appearance, region_appearance

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llSetAgentRot

```lsl
void llSetAgentRot(rotation rot, integer flags)
```

- Purpose: Sets the rotation of the avatar to rot, controlled by flags.

- Argument `rot` (rotation): Target rotation to turn the avatar to face.

- Argument `flags` (integer): Flags to configure the rotation behavior.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 515 | Native: False | Pure (no side effects): False

- Categories: avatar, movement, physics

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llSetAlpha

```lsl
void llSetAlpha(float alpha, integer face)
```

- Purpose: Sets the diffuse texture alpha (opacity) of face. If face is ALL_SIDES, applies to all faces. Values are clamped between 0.1 and 1.0 (where 1.0 is fully opaque).

- Argument `alpha` (float): Transparency value to set, from 0.0 (clear) to 1.0 (solid; clamped to a minimum of 0.1).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 51 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetAngularVelocity

```lsl
void llSetAngularVelocity(vector initial_omega, integer is_local)
```

- Purpose: Sets the angular velocity of a physical object to initial_omega (mass-independent). If local is TRUE, applied in local coordinates; if FALSE, applied in global coordinates. Has no effect on non-physical objects.

- Argument `initial_omega` (vector): Angular velocity vector to apply (in radians per second).

- Argument `is_local` (integer): Boolean. If TRUE, initial_omega is treated as a local vector; if FALSE, as a global region vector.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 379 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llSetAnimationOverride

```lsl
void llSetAnimationOverride(string anim_state, string anim)
```

- Purpose: Overrides the default animation for anim_state with anim (which must be in the object's inventory or a built-in animation). Requires the PERMISSION_OVERRIDE_ANIMATIONS permission.

- Argument `anim_state` (string): Animation state to override.

- Argument `anim` (string): Name of an animation in the prim's inventory, or a built-in animation name.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 501 | Native: False | Pure (no side effects): False

- Categories: avatar_animation, permissions


## llSetBuoyancy

```lsl
void llSetBuoyancy(float buoyancy)
```

- Purpose: Sets the buoyancy of a physical object (requires physics to be enabled). A value of 0.0 offers no buoyancy, < 1.0 sinks, 1.0 counteracts gravity, and > 1.0 rises.

- Argument `buoyancy` (float): Float buoyancy value to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 122 | Native: False | Pure (no side effects): False

- Categories: physics


## llSetCameraAtOffset

```lsl
void llSetCameraAtOffset(vector offset)
```

- Purpose: Sets the target offset vector (in local coordinates) that a seated avatar's camera will look at.

- Argument `offset` (vector): Offset position vector in local coordinates relative to the prim.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 244 | Native: False | Pure (no side effects): False

- Categories: camera


## llSetCameraEyeOffset

```lsl
void llSetCameraEyeOffset(vector offset)
```

- Purpose: Sets the eye offset vector (in local coordinates) where a seated avatar's camera is positioned.

- Argument `offset` (vector): Offset position vector in local coordinates relative to the prim.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 243 | Native: False | Pure (no side effects): False

- Categories: camera


## llSetCameraParams

```lsl
void llSetCameraParams(list rules)
```

- Purpose: Sets multiple camera parameters simultaneously using the list of rules. Requires the PERMISSION_CONTROL_CAMERA runtime permission.

- Argument `rules` (list): A strided list of rules and data pairs configuring the camera.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 313 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llSetClickAction

```lsl
void llSetClickAction(integer action)
```

- Purpose: Sets the action (a CLICK_ACTION_* flag) performed when an avatar left-clicks the prim.

- Argument `action` (integer): CLICK_ACTION_* flag representing the action to apply.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 333 | Native: False | Pure (no side effects): False

- Categories: input, money, prim_properties, touch, user_interface


## llSetColor

```lsl
void llSetColor(vector color, integer face)
```

- Purpose: Sets the Blinn-Phong diffuse RGB color of face. If face is ALL_SIDES, applies the color to all faces.

- Argument `color` (vector): Color vector in RGB <R, G, B> (values from 0.0 to 1.0).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 49 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetContentType

```lsl
void llSetContentType(key request_id, integer content_type)
```

- Purpose: Sets the 'Content-Type' header of subsequent HTTP server responses (via llHTTPResponse) for request_id using the specified content_type (a CONTENT_TYPE_* constant).

- Argument `request_id` (key): Unique key identifying the incoming HTTP request.

- Argument `content_type` (integer): CONTENT_TYPE_* constant representing the Internet media type to use.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 374 | Native: False | Pure (no side effects): False

- Categories: media, prim_media, web


## llSetDamage

```lsl
void llSetDamage(float damage)
```

- Purpose: Sets the amount of damage delivered when this object hits an avatar. The object is immediately destroyed upon inflicting damage, and no collision event is triggered.

- Argument `damage` (float): Float damage value to set (range -100.0 for full heal to 100.0 for instant kill).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 157 | Native: False | Pure (no side effects): False

- Categories: combat


## llSetEnvironment

```lsl
integer llSetEnvironment(vector position, list params)
```

- Purpose: Overrides the environmental settings at position for a parcel (or region if position is <-1.0, -1.0, z>) using the parameters in params. Passing an empty params list removes previous overrides.

- Argument `position` (vector): Position vector in region coordinates to specify the target parcel, or <-1.0, -1.0, z> for the entire region (where z specifies the sky track, or -1 for all tracks).

- Argument `params` (list): A list of environmental attributes and values to apply (or empty to clear).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 717 | Native: False | Pure (no side effects): False

- Categories: parcel, parcel_appearance


## llSetExperienceKey

```lsl
integer llSetExperienceKey(key experienceid)
```

- Argument `experienceid` (key): 

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 386 | Native: False | Pure (no side effects): False

- Categories: experience

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.

- Deprecated in LSL: True


## llSetForce

```lsl
void llSetForce(vector force, integer is_local)
```

- Purpose: Applies a constant linear force to a physical object. If local is TRUE, force is applied relative to local coordinates; if FALSE, applied relative to region coordinates.

- Argument `force` (vector): Directional force vector to apply.

- Argument `is_local` (integer): Boolean. If TRUE, force is treated as a local vector; if FALSE, as a global region vector.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 64 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llSetForceAndTorque

```lsl
void llSetForceAndTorque(vector force, vector torque, integer is_local)
```

- Purpose: Sets both the constant linear force and constant torque acting on a physical object. If local is TRUE, forces are applied in local coordinates; if FALSE, in global coordinates.

- Argument `force` (vector): Directional linear force vector.

- Argument `torque` (vector): Torque rotational force vector.

- Argument `is_local` (integer): Boolean. If TRUE, force and torque are treated as local vectors; if FALSE, as global region vectors.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 76 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llSetGroundTexture

```lsl
integer llSetGroundTexture(list changes)
```

- Purpose: Changes the painted terrain textures on the region based on changes. The script owner must have estate management rights. Returns an integer status.

- Argument `changes` (list): A list of terrain detail properties and values to change.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 558 | Native: False | Pure (no side effects): False

- Categories: region


## llSetHoverHeight

```lsl
void llSetHoverHeight(float height, integer water, float tau)
```

- Purpose: Critically damps the physical object's vertical movement to hover at height (above ground, or above water if water is TRUE) in tau seconds. Do not use with vehicles; call llStopHover to cancel.

- Argument `height` (float): Distance to hover above the ground or water.

- Argument `water` (integer): Boolean. If TRUE, hovers above water too; if FALSE, water is ignored.

- Argument `tau` (float): Timescale in seconds to critically damp the movement.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 123 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llSetInventoryPermMask

```lsl
void llSetInventoryPermMask(string item, integer group, integer flags)
```

- Purpose: Sets the specified item's permission flags for the specified group.

- Argument `item` (string): Name of the item in the prim's inventory.

- Argument `group` (integer): MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to set.

- Argument `flags` (integer): Bitfield of permissions (PERM_* flags) to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 290 | Native: False | Pure (no side effects): False

- Categories: asset_permissions, prim_inventory


## llSetKeyframedMotion

```lsl
void llSetKeyframedMotion(list keyframes, list options)
```

- Purpose: Smoothly moves a non-physical object between the positions, orientations, and times specified in the keyframes list, configured via options. Collisions with keyframed objects are ignored. An empty keyframes list terminates the motion.

- Argument `keyframes` (list): A strided list of the form [vector position, rotation orientation, float time] representing sequential relative keyframes (minimum time is 1/9s).

- Argument `options` (list): A list of options (KFM_* constants) to modify playback behavior.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 394 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llSetLinkAlpha

```lsl
void llSetLinkAlpha(integer link, float alpha, integer face)
```

- Purpose: Sets the Blinn-Phong alpha (transparency) of face on the linked prim link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `alpha` (float): Transparency value to set, from 0.0 (clear) to 1.0 (solid).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 274 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llSetLinkCamera

```lsl
void llSetLinkCamera(integer link, vector eye, vector at)
```

- Purpose: Sets the camera eye position offset eye and looking-at position offset at for avatars who sit on the linked prim link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `eye` (vector): Eye offset position vector in local coordinates relative to the prim.

- Argument `at` (vector): Look-at offset position vector in local coordinates relative to the prim.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 377 | Native: False | Pure (no side effects): False

- Categories: camera, sit


## llSetLinkColor

```lsl
void llSetLinkColor(integer link, vector color, integer face)
```

- Purpose: Sets the Blinn-Phong diffuse RGB color of face on the linked prim link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `color` (vector): Color vector in RGB <R, G, B> (values from 0.0 to 1.0).

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 140 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llSetLinkGLTFOverrides

```lsl
void llSetLinkGLTFOverrides(integer link, integer face, list params)
```

- Purpose: Sets or removes individual GLTF override parameters specified by params on face of the linked prim link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `face` (integer): Face number or ALL_SIDES.

- Argument `params` (list): A list of overrides and their corresponding values to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 560 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance


## llSetLinkMedia

```lsl
integer llSetLinkMedia(integer link, integer face, list params)
```

- Purpose: Sets the media parameters specified by params on face of the linked prim link without a script delay. Returns an integer STATUS_* flag detailing success or failure.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `face` (integer): Face number (side) of the prim.

- Argument `params` (list): A set of property-value pairs (in no particular order) specifying media parameters, or a PrimMediaParams dictionary.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 371 | Native: False | Pure (no side effects): False

- Categories: linkset, media, prim_media, web


## llSetLinkPrimitiveParams

```lsl
void llSetLinkPrimitiveParams(integer link, list rules)
```

- Purpose: Deprecated (use llSetLinkPrimitiveParamsFast instead). Sets primitive parameters for the linked prim link according to rules.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `rules` (list): A list of PRIM_* rules and data to apply.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 328 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance, prim_properties

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.SetLinkPrimitiveParamsFast', 'selene-replace': ['ll.SetLinkPrimitiveParamsFast(%...)']}


## llSetLinkPrimitiveParamsFast

```lsl
void llSetLinkPrimitiveParamsFast(integer link, list rules)
```

- Purpose: Sets primitive parameters for the linked prim link according to rules with no built-in script sleep delay.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `rules` (list): A list of PRIM_* rules and data to apply.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 353 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance, prim_properties


## llSetLinkRenderMaterial

```lsl
void llSetLinkRenderMaterial(integer link, string material, integer face)
```

- Purpose: Applies material (UUID or inventory name) to face of the linked prim link. Note: This clears most PRIM_GLTF_* properties on the face except for repeats, offsets, and rotation.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `material` (string): Name of a material in the prim's inventory, or a UUID.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 762 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetLinkSitFlags

```lsl
void llSetLinkSitFlags(integer link, integer flags)
```

- Purpose: Sets the sit target flags for the linked prim link inside the linkset.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `flags` (integer): A bitfield of sit flags (SIT_FLAG_*) to apply.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 550 | Native: False | Pure (no side effects): False

- Categories: linkset, sit


## llSetLinkTexture

```lsl
void llSetLinkTexture(integer link, string texture, integer face)
```

- Purpose: Applies texture (UUID or inventory name) to face of the linked prim link.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag.

- Argument `texture` (string): Name of a texture in the prim's inventory, or a UUID.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 329 | Native: False | Pure (no side effects): False

- Categories: linkset, prim_appearance

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetLinkTextureAnim

```lsl
void llSetLinkTextureAnim(integer link, integer mode, integer face, integer sizex, integer sizey, float start, float length, float rate)
```

- Purpose: Animates the texture on face of the linked prim link by setting the scale and offset according to mode. Parameters sizex/sizey define frames, start defines the start frame/angle, length defines duration, and rate defines playback speed.

- Argument `link` (integer): Link number (1 for root, >1 for children) or a LINK_* flag to animate.

- Argument `mode` (integer): Bitfield of texture animation mode flags (ANIM_ON, LOOP, etc.).

- Argument `face` (integer): Face number or ALL_SIDES.

- Argument `sizex` (integer): Number of horizontal frames (ignored for ROTATE and SCALE).

- Argument `sizey` (integer): Number of vertical frames (ignored for ROTATE and SCALE).

- Argument `start` (float): Start frame number (or radians for ROTATE).

- Argument `length` (float): Number of frames to display (or radians for ROTATE).

- Argument `rate` (float): Playback rate in frames per second (or radians/sec for ROTATE, UV coords/sec for SMOOTH). Must not be zero.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 356 | Native: False | Pure (no side effects): False

- Categories: effects, linkset, prim_appearance


## llSetLocalRot

```lsl
void llSetLocalRot(rotation rot)
```

- Purpose: Sets the rotation of a child prim relative to its root prim using rot.

- Argument `rot` (rotation): Local rotation to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 284 | Native: False | Pure (no side effects): False

- Categories: movement, prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetMemoryLimit

```lsl
integer llSetMemoryLimit(integer limit)
```

- Purpose: Requests that limit bytes are reserved for the script. Returns TRUE on success or FALSE on failure (has no effect in LSO).

- Argument `limit` (integer): Integer memory limit in bytes to reserve (must be less than the 64KB maximum).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 369 | Native: False | Pure (no side effects): False

- Categories: script


## llSetObjectDesc

```lsl
void llSetObjectDesc(string description)
```

- Purpose: Sets the description of the prim containing the script to description (limited to 127 characters).

- Argument `description` (string): New description string (up to 127 characters).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 271 | Native: False | Pure (no side effects): False

- Categories: prim, prim_properties

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetObjectName

```lsl
void llSetObjectName(string name)
```

- Purpose: Sets the name of the prim containing the script to name.

- Argument `name` (string): New name string.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 203 | Native: False | Pure (no side effects): False

- Categories: prim, prim_properties

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetObjectPermMask

```lsl
void llSetObjectPermMask(integer group, integer flags)
```

- Purpose: Sets the scripts's object's permission flags for the specified group.

- Argument `group` (integer): MASK_* group (e.g., MASK_BASE, MASK_OWNER, MASK_GROUP, MASK_EVERYONE, or MASK_NEXT) to set.

- Argument `flags` (integer): Bitfield of permissions (PERM_* flags) to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 288 | Native: False | Pure (no side effects): False

- Categories: asset_permissions, linkset


## llSetParcelForSale

```lsl
integer llSetParcelForSale(integer ForSale, list Options)
```

- Purpose: Sets the parcel the object is on for sale. If ForSale is TRUE, puts the land up for sale using Options (price, buyer, objects included). Setting ForSale to FALSE removes the parcel from sale. Requires parcel ownership and the PERMISSION_PRIVILEGED_LAND_ACCESS permission. Returns an error code or 0 if successful.

- Argument `ForSale` (integer): Boolean. If TRUE, puts the parcel up for sale; if FALSE, removes it from sale.

- Argument `Options` (list): A list of options to configure the sale (e.g., price, authorized buyer, and object inclusion).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 561 | Native: False | Pure (no side effects): False

- Categories: parcel


## llSetParcelMusicURL

```lsl
void llSetParcelMusicURL(string url)
```

- Purpose: Sets the streaming audio (music) URL for the parcel containing the object. The object owner must match the landowner or land group.

- Argument `url` (string): Streaming audio URL string.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 2.0 s | Function ID: 267 | Native: False | Pure (no side effects): False

- Categories: media, parcel, parcel_media

- Delay warning: this call sleeps the script for 2.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetPayPrice

```lsl
void llSetPayPrice(integer price, list quick_pay_buttons)
```

- Purpose: Suggests default amounts for the pay text input field price and the four payment dialog quick_pay_buttons when an avatar pays this object.

- Argument `price` (integer): Default price integer shown in the text field (can accept PAY_* constants or positive values).

- Argument `quick_pay_buttons` (list): A list of four integer values or PAY_* constants specifying the button payment choices.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 302 | Native: False | Pure (no side effects): False

- Categories: money, prim_properties, user_interface


## llSetPhysicsMaterial

```lsl
void llSetPhysicsMaterial(integer mask, float gravity_multiplier, float restitution, float friction, float density)
```

- Purpose: Configures the physical characteristics of an object. The mask bitfield specifies which of the other parameters (gravity_multiplier, restitution, friction, or density) should be applied to the object.

- Argument `mask` (integer): Bitwise mask combination specifying which of the floats (DENSITY, FRICTION, RESTITUTION, or GRAVITY_MULTIPLIER) to apply.

- Argument `gravity_multiplier` (float): Gravity multiplier float value (range [-1.0, +28.0], default is 1.0).

- Argument `restitution` (float): Elasticity restitution float value (range [0.0, 1.0]).

- Argument `friction` (float): Friction coefficient float value (range [0.0, 255.0]).

- Argument `density` (float): Density float value in kg/m³ (range [1.0, 22587.0]).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 380 | Native: False | Pure (no side effects): False

- Categories: physics, prim, prim_properties

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetPos

```lsl
void llSetPos(vector pos)
```

- Purpose: Moves the non-physical object or prim toward the vector pos (up to 10m). If called in a child prim, pos is treated as root-relative; if called from the root prim, the entire object is moved.

- Argument `pos` (vector): Position vector to move to (in region coordinates, or local coordinates if in a child prim).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 58 | Native: False | Pure (no side effects): False

- Categories: movement, prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetPrimMediaParams

```lsl
integer llSetPrimMediaParams(integer face, list params)
```

- Purpose: Sets the media parameters specified by params on the designated face of the prim. Returns an integer STATUS_* flag detailing success or failure.

- Argument `face` (integer): Face number (side) of the prim.

- Argument `params` (list): A set of property-value pairs (in no particular order) specifying media parameters.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 350 | Native: False | Pure (no side effects): False

- Categories: media, prim, prim_media, web

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetPrimURL

```lsl
void llSetPrimURL(string url)
```

- Purpose: Deprecated (use llSetPrimMediaParams instead). Updates the URL displayed on the prim's faces.

- Argument `url` (string): Web URL to display.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 20.0 s | Function ID: 305 | Native: False | Pure (no side effects): False

- Categories: media, prim, prim_media, web

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 20.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.SetPrimMediaParams', 'selene-replace': ['ll.SetPrimMediaParams(ALL_SIDES, {PRIM_MEDIA_CURRENT_URL, %1})']}


## llSetPrimitiveParams

```lsl
void llSetPrimitiveParams(list rules)
```

- Purpose: Deprecated (use llSetLinkPrimitiveParamsFast instead). Sets the prim's attributes according to rules.

- Argument `rules` (list): A list of PRIM_* rules and data to apply.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 259 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance, prim_properties

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.SetLinkPrimitiveParamsFast', 'selene-replace': ['ll.SetLinkPrimitiveParamsFast(%...)']}


## llSetRegionPos

```lsl
integer llSetRegionPos(vector position)
```

- Purpose: Tries to move the entire object so that its root prim is within 0.1m of the vector position (underground positions are set to ground level). Returns TRUE on success or FALSE on failure.

- Argument `position` (vector): Target position vector in region coordinates (can cross up to 10m over a region border).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 397 | Native: False | Pure (no side effects): False

- Categories: movement, prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetRemoteScriptAccessPin

```lsl
void llSetRemoteScriptAccessPin(integer pin)
```

- Purpose: Sets the prim's remote script access PIN to pin (a non-zero value enables loading via llRemoteLoadScriptPin, while zero disables it).

- Argument `pin` (integer): Integer PIN code (non-zero enables, zero disables).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 252 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, script

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetRenderMaterial

```lsl
void llSetRenderMaterial(string material, integer face)
```

- Purpose: Applies material (UUID or inventory name) to face of the prim. Note: This clears most PRIM_GLTF_* properties on the face except for repeats, offsets, and rotation.

- Argument `material` (string): Name of a material in the prim's inventory, or a UUID.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 761 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetRot

```lsl
void llSetRot(rotation rot)
```

- Purpose: Sets the rotation of the prim to rot. If in a child prim, rot is treated as root-relative; if in the root prim of a non-physical object, rotates the entire object.

- Argument `rot` (rotation): Target rotation.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 61 | Native: False | Pure (no side effects): False

- Categories: movement, prim

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetScale

```lsl
void llSetScale(vector size)
```

- Purpose: Sets the physical scale (dimensions) of the prim containing the script to size.

- Argument `size` (vector): Target size vector.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 47 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetScriptState

```lsl
void llSetScriptState(string script, integer running)
```

- Purpose: Sets the running state of the named script in the prim's inventory. If running is TRUE, the script is enabled; if FALSE, it is disabled.

- Argument `script` (string): Name of the script in the prim's inventory.

- Argument `running` (integer): Boolean. If TRUE, enables the script; if FALSE, disables it.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 148 | Native: False | Pure (no side effects): False

- Categories: prim_inventory, script


## llSetSitText

```lsl
void llSetSitText(string text)
```

- Purpose: Displays the string text instead of 'Sit' (or 'Sit Here') in the viewer's right-click context menu.

- Argument `text` (string): Context menu text to display.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 242 | Native: False | Pure (no side effects): False

- Categories: prim, sit, user_interface

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetSoundQueueing

```lsl
void llSetSoundQueueing(integer queue)
```

- Purpose: Sets whether attached sounds wait for the current sound to end before playing (enables queuing if queue is TRUE, disables if FALSE). The queue is one level deep.

- Argument `queue` (integer): Boolean. If TRUE, sound queuing is enabled; if FALSE, it is disabled.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 208 | Native: False | Pure (no side effects): False

- Categories: sound


## llSetSoundRadius

```lsl
void llSetSoundRadius(float radius)
```

- Purpose: Limits the audibility radius of attached and triggered scripted sounds to distance radius.

- Argument `radius` (float): Maximum distance in meters at which the sounds can be heard.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 209 | Native: False | Pure (no side effects): False

- Categories: sound


## llSetStatus

```lsl
void llSetStatus(integer status, integer value)
```

- Purpose: Sets the object status attributes specified by status to value.

- Argument `status` (integer): Bitmask representing the STATUS_* flag(s) to change.

- Argument `value` (integer): Boolean. If TRUE, enables the status; if FALSE, disables it.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 45 | Native: False | Pure (no side effects): False

- Categories: linkset, physics, prim_properties


## llSetText

```lsl
void llSetText(string text, vector color, float alpha)
```

- Purpose: Displays floating text above the prim with the specified color vector and transparency alpha.

- Argument `text` (string): Floating text string to display.

- Argument `color` (vector): Color vector in RGB <R, G, B> (values from 0.0 to 1.0).

- Argument `alpha` (float): Transparency value to set, from 0.0 (clear) to 1.0 (solid).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 152 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, effects, prim_appearance, prim_properties


## llSetTexture

```lsl
void llSetTexture(string texture, integer face)
```

- Purpose: Applies the Blinn-Phong diffuse texture to face of the prim.

- Argument `texture` (string): Name of a texture in the prim's inventory, or a UUID.

- Argument `face` (integer): Face number or ALL_SIDES.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.2 s | Function ID: 53 | Native: False | Pure (no side effects): False

- Categories: prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.

- Delay warning: this call sleeps the script for 0.2 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llSetTextureAnim

```lsl
void llSetTextureAnim(integer mode, integer face, integer sizex, integer sizey, float start, float length, float rate)
```

- Purpose: Animates the texture on face of the prim by setting its scale and offset. mode defines options, sizex/sizey define frames, start defines the start frame/angle, length defines duration, and rate defines playback speed.

- Argument `mode` (integer): Bitfield of texture animation mode flags (ANIM_ON, LOOP, etc.).

- Argument `face` (integer): Face number or ALL_SIDES.

- Argument `sizex` (integer): Number of horizontal frames (ignored for ROTATE and SCALE).

- Argument `sizey` (integer): Number of vertical frames (ignored for ROTATE and SCALE).

- Argument `start` (float): Start frame number (or radians for ROTATE).

- Argument `length` (float): Number of frames to display (or radians for ROTATE).

- Argument `rate` (float): Playback rate in frames per second (or radians/sec for ROTATE, UV coords/sec for SMOOTH). Must not be zero.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 211 | Native: False | Pure (no side effects): False

- Categories: effects, prim, prim_appearance

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSetTimerEvent

```lsl
void llSetTimerEvent(float sec)
```

- Purpose: Sets a timer to trigger a timer event periodically every sec seconds. Passing 0.0 stops further timer events.

- Argument `sec` (float): Interval in seconds between timer events (0.0 to disable).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 107 | Native: False | Pure (no side effects): False

- Categories: script, time


## llSetTorque

```lsl
void llSetTorque(vector torque, integer is_local)
```

- Purpose: Applies a constant torque rotational force to a physical object. If local is TRUE, torque is applied in local coordinates; if FALSE, applied in global coordinates.

- Argument `torque` (vector): Torque rotational force vector.

- Argument `is_local` (integer): Boolean. If TRUE, torque is treated as a local vector; if FALSE, as a global region vector.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 74 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llSetTouchText

```lsl
void llSetTouchText(string text)
```

- Purpose: Displays the string text instead of 'Touch' in the right-click context menu.

- Argument `text` (string): Context menu text to display.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 241 | Native: False | Pure (no side effects): False

- Categories: prim_properties, touch, user_interface


## llSetVehicleFlags

```lsl
void llSetVehicleFlags(integer flags)
```

- Purpose: Enables the vehicle flags specified in the Flags bitmask.

- Argument `flags` (integer): A bitwise mask of VEHICLE_FLAG_* constants to enable.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 236 | Native: False | Pure (no side effects): False

- Categories: vehicles


## llSetVehicleFloatParam

```lsl
void llSetVehicleFloatParam(integer param, float value)
```

- Purpose: Sets the specified vehicle float parameter param to value.

- Argument `param` (integer): VEHICLE_* float parameter constant to set.

- Argument `value` (float): Float value to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 233 | Native: False | Pure (no side effects): False

- Categories: vehicles


## llSetVehicleRotationParam

```lsl
void llSetVehicleRotationParam(integer param, rotation rot)
```

- Purpose: Sets the specified vehicle rotation parameter param to rot.

- Argument `param` (integer): VEHICLE_* rotation parameter constant to set.

- Argument `rot` (rotation): Rotation value to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 235 | Native: False | Pure (no side effects): False

- Categories: vehicles


## llSetVehicleType

```lsl
void llSetVehicleType(integer type)
```

- Purpose: Sets the vehicle physics preset type to one of the default vehicle types.

- Argument `type` (integer): VEHICLE_TYPE_* constant to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 232 | Native: False | Pure (no side effects): False

- Categories: vehicles


## llSetVehicleVectorParam

```lsl
void llSetVehicleVectorParam(integer param, vector vec)
```

- Purpose: Sets the specified vehicle vector parameter param to vec.

- Argument `param` (integer): VEHICLE_* vector parameter constant to set.

- Argument `vec` (vector): Vector value to set.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 234 | Native: False | Pure (no side effects): False

- Categories: vehicles


## llSetVelocity

```lsl
void llSetVelocity(vector velocity, integer is_local)
```

- Purpose: Sets the linear velocity of a physical object to velocity. If local is TRUE, velocity is treated as a local directional vector; if FALSE, as a global region directional vector. Has no effect on non-physical objects.

- Argument `velocity` (vector): Linear velocity vector to apply (in meters per second).

- Argument `is_local` (integer): Boolean. If TRUE, velocity is treated as a local directional vector; if FALSE, as a global region vector.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 378 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llShout

```lsl
void llShout(integer channel, string msg)
```

- Purpose: Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv("shout_range"), which is 100m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.

- Argument `channel` (integer): Chat channel (any 32-bit signed integer value) to shout the message on.

- Argument `msg` (string): Text message string to broadcast.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 24 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, script_communication


## llSignRSA

```lsl
string llSignRSA(string private_key, string msg, string algorithm)
```

- Purpose: Returns the Base64-encoded RSA signature of msg using the PEM-formatted private_key and the specified digest algorithm (sha1, sha224, sha256, sha384, or sha512). Can be paired with llVerifyRSA to pass verifiable messages.

- Argument `private_key` (string): PEM-formatted private key.

- Argument `msg` (string): Message contents to sign.

- Argument `algorithm` (string): Digest algorithm to use (sha1, sha224, sha256, sha384, or sha512).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 539 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llSin

```lsl
float llSin(float theta)
```

- Purpose: Returns the sine of theta. Theta is in radians.

- Argument `theta` (float): Angle in radians.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 0 | Native: True | Pure (no side effects): True

- Categories: math, math_trig

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.sin`. Double precision; fastcall.


## llSitOnLink

```lsl
integer llSitOnLink(key agent_id, integer link)
```

- Purpose: Forces the avatar specified by agent_id (who must be participating in the experience) to sit on the sit target of the prim indicated by link. If occupied, searches down the linkset for an available sit target. Returns an integer.

- Argument `agent_id` (key): UUID of the avatar being forced to sit.

- Argument `link` (integer): Link number for the prim containing the desired sit target.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 503 | Native: False | Pure (no side effects): False

- Categories: experience, sit

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llSitTarget

```lsl
void llSitTarget(vector offset, rotation rot)
```

- Purpose: Sets the sit target position (offset) and rotation (rot) relative to the prim's position and orientation. Clears the sit target if offset is ZERO_VECTOR.

- Argument `offset` (vector): Target position vector in local prim coordinates.

- Argument `rot` (rotation): Target rotation relative to the prim's rotation.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 238 | Native: False | Pure (no side effects): False

- Categories: prim, sit

- Guidance (prim): Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.


## llSleep

```lsl
void llSleep(float sec)
```

- Purpose: Puts the script to sleep for sec seconds (at least until the next server-frame, ~0.02222 seconds). The script is inactive during this time. If sec is 0.0 or less, the script does not sleep.

- Argument `sec` (float): Duration in seconds to put the script to sleep.

- Returns: void

- Energy cost: 0.0 | Script sleep after call: 0.0 s | Function ID: 108 | Native: False | Pure (no side effects): False

- Categories: script, time


## llSound

```lsl
void llSound(string sound, float volume, integer queue, integer loop)
```

- Purpose: Deprecated (use llPlaySound instead). Plays the specified sound at volume, with options to loop or queue the sound.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Argument `queue` (integer): Boolean. If TRUE, queues the sound; if FALSE, interrupts the currently playing sound.

- Argument `loop` (integer): Boolean. If TRUE, loops the sound.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 85 | Native: False | Pure (no side effects): False

- Categories: sound

- Deprecated in LSL: {'use': 'll.PlaySound', 'selene-replace': ['ll.PlaySound(%1, %2)', 'll.LoopSound(%1, %2)']}


## llSoundPreload

```lsl
void llSoundPreload(string sound)
```

- Purpose: Deprecated (use llPreloadSound instead). Preloads the specified sound on viewers within range.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 126 | Native: False | Pure (no side effects): False

- Categories: sound

- Deprecated in LSL: {'use': 'll.PreloadSound', 'selene-replace': ['ll.PreloadSound(%1)']}


## llSqrt

```lsl
float llSqrt(float val)
```

- Purpose: Returns the square root of val. If negative, return NaN.

- Argument `val` (float): Positive float value (must be >= 0.0).

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 4 | Native: True | Pure (no side effects): True

- Categories: math

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.sqrt`. Double precision; fastcall.


## llStartAnimation

```lsl
void llStartAnimation(string anim)
```

- Purpose: Starts the animation anim (inventory or built-in) on the avatar who granted the script the PERMISSION_TRIGGER_ANIMATION permission (automatically granted for attached or sat-on objects).

- Argument `anim` (string): Name of the animation in the prim's inventory, or the built-in animation name.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 129 | Native: False | Pure (no side effects): False

- Categories: avatar, avatar_animation, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llStartObjectAnimation

```lsl
void llStartObjectAnimation(string anim)
```

- Purpose: Starts the specified animation anim (inventory or built-in) on the rigged mesh object associated with the current script.

- Argument `anim` (string): Name of the animation in the prim's inventory, or the built-in animation name.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 504 | Native: False | Pure (no side effects): False

- Categories: object_animation


## llStopAnimation

```lsl
void llStopAnimation(string anim)
```

- Purpose: Stops the specified animation anim (inventory, built-in, or UUID) on the avatar who granted the script the PERMISSION_TRIGGER_ANIMATION permission (automatically granted for attached or sat-on objects).

- Argument `anim` (string): Name of the animation in the prim's inventory, the UUID of the animation, or the built-in animation name.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 130 | Native: False | Pure (no side effects): False

- Categories: avatar, avatar_animation, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llStopHover

```lsl
void llStopHover()
```

- Purpose: Stops the hover behavior (such as that initiated by llSetHoverHeight).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 124 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llStopLookAt

```lsl
void llStopLookAt()
```

- Purpose: Stops causing the object to look at or point toward a target (canceling llLookAt or llRotLookAt).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 106 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llStopMoveToTarget

```lsl
void llStopMoveToTarget()
```

- Purpose: Stops the critically damped movement of the object toward a target (canceling llMoveToTarget). Use llStopLookAt to stop rotational tracking.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 71 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llStopObjectAnimation

```lsl
void llStopObjectAnimation(string anim)
```

- Purpose: Stops the specified animation anim (inventory, built-in, or UUID) on the rigged mesh object associated with the current script.

- Argument `anim` (string): Name of the animation in the prim's inventory, the UUID of the animation, or the built-in animation name.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 505 | Native: False | Pure (no side effects): False

- Categories: object_animation


## llStopPointAt

```lsl
void llStopPointAt()
```

- Purpose: Stops the avatar who owns the object from pointing.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 132 | Native: False | Pure (no side effects): False

- Categories: movement, physics

- Deprecated in LSL: True


## llStopSound

```lsl
void llStopSound()
```

- Purpose: Stops playback of the currently playing attached sound.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 92 | Native: False | Pure (no side effects): False

- Categories: sound


## llStringLength

```lsl
integer llStringLength(string str)
```

- Purpose: Returns the number of unicode codepoints in the string.

- Argument `str` (string): String to measure.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 128 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.

- SLua: deprecated in favour of ``. Use 'utf8.len' or '#' or 'string.len' instead.


## llStringToBase64

```lsl
string llStringToBase64(string str)
```

- Purpose: Returns the Base64 representation string of str, interpreting it as a UTF-8 byte sequence.

- Argument `str` (string): Source string to encode.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 260 | Native: False | Pure (no side effects): True

- Categories: data_conversion

- SLua: deprecated in favour of `llbase64.encode`. 


## llStringTrim

```lsl
string llStringTrim(string src, integer type)
```

- Purpose: Returns a copy of the string src with leading, trailing, or both types of whitespace (including spaces, tabs, and line feeds) eliminated, according to the specified trim type.

- Argument `src` (string): String to trim.

- Argument `type` (integer): Trim type flag (STRING_TRIM_HEAD, STRING_TRIM_TAIL, or STRING_TRIM).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 330 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llSubStringIndex

```lsl
integer llSubStringIndex(string source, string pattern)
```

- Purpose: Returns the codepoint index of the first occurrence of pattern inside the string source. Returns -1 if not found. No regex.

- Argument `source` (string): Source string to search within.

- Argument `pattern` (string): Substring pattern to search for.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 181 | Native: False | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llTakeCamera

```lsl
void llTakeCamera(key avatar)
```

- Purpose: Deprecated (use llSetCameraParams instead). Formerly used to take control of the agent's camera.

- Argument `avatar` (key): UUID of the avatar in the same region.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 115 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Deprecated in LSL: {'use': 'll.SetCameraParams'}


## llTakeControls

```lsl
void llTakeControls(integer controls, integer accept, integer pass_on)
```

- Purpose: Intercepts inputs (keyboard/mouse clicks) from the agent, specifically those specified by controls. The boolean accept determines if events are generated, and pass_on determines if inputs also perform their default functions. Requires the PERMISSION_TAKE_CONTROLS runtime permission.

- Argument `controls` (integer): Bitfield of CONTROL_* flags to intercept.

- Argument `accept` (integer): Boolean. Determines whether control events are generated to trigger script handlers.

- Argument `pass_on` (integer): Boolean. If TRUE, the keys also perform their default functions; if FALSE, default actions are suppressed.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 111 | Native: False | Pure (no side effects): False

- Categories: avatar, input, permissions

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llTan

```lsl
float llTan(float theta)
```

- Purpose: Returns the tangent of theta. Theta is in radians.

- Argument `theta` (float): Angle in radians.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 2 | Native: True | Pure (no side effects): True

- Categories: math, math_trig

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `math.tan`. Double precision; fastcall.


## llTarget

```lsl
integer llTarget(vector position, float range)
```

- Purpose: Registers a positional target at position with a leeway radius range. This triggers at_target and not_at_target events. Returns an integer handle to unregister the target via llTargetRemove.

- Argument `position` (vector): Target position vector in region coordinates.

- Argument `range` (float): Radius tolerance in meters surrounding the target position.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 66 | Native: False | Pure (no side effects): False

- Categories: movement


## llTargetOmega

```lsl
void llTargetOmega(vector axis, float spinrate, float gain)
```

- Purpose: Applies a smooth client-side rotation around the local axis at a rate equal to spinrate multiplied by the magnitude of axis (in radians per second) with a force defined by gain. Set spinrate to 0.0 to cancel.

- Argument `axis` (vector): Local axis vector around which the object rotates.

- Argument `spinrate` (float): Rotation rate multiplier in radians per second.

- Argument `gain` (float): A float modulating the rotational strength (disables the rotation if set to 0.0).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 133 | Native: False | Pure (no side effects): False

- Categories: movement, physics


## llTargetRemove

```lsl
void llTargetRemove(integer handle)
```

- Purpose: Removes the positional target specified by the integer handle registered with llTarget.

- Argument `handle` (integer): Integer target handle returned by llTarget to remove.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 67 | Native: False | Pure (no side effects): False

- Categories: movement


## llTargetedEmail

```lsl
void llTargetedEmail(integer target, string subject, string msg)
```

- Purpose: Sends an email to with the given subject subject and body msg to the target (which can designate the owner or creator of the object). The email will be sent from `{ll.GetKey()}@lsl.secondlife.com`.

- Argument `target` (integer): Target constant (e.g., TARGETED_EMAIL_OBJECT_OWNER or TARGETED_EMAIL_ROOT_CREATOR).

- Argument `subject` (string): Subject of the email.

- Argument `msg` (string): Email message body.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 20.0 s | Function ID: 750 | Native: False | Pure (no side effects): False

- Categories: avatar_communication

- Delay warning: this call sleeps the script for 20.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llTeleportAgent

```lsl
void llTeleportAgent(key agent, string landmark, vector position, vector look_at)
```

- Purpose: Teleports the owning agent (who must grant PERMISSION_TELEPORT) to a landmark in the object's inventory. If landmark is empty, teleports them to position within the current region. Upon arrival, the agent is turned to face look_at. Can only teleport the owner.

- Argument `agent` (key): UUID of the owning avatar to teleport.

- Argument `landmark` (string): Name of the landmark in the prim's inventory, or an empty string to teleport locally.

- Argument `position` (vector): Position vector in local region coordinates to teleport to if landmark is empty.

- Argument `look_at` (vector): Position vector (or direction unit vector if teleporting out of region) the agent faces upon landing.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 368 | Native: False | Pure (no side effects): False

- Categories: avatar, permissions, teleport

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llTeleportAgentGlobalCoords

```lsl
void llTeleportAgentGlobalCoords(key agent, vector global_coordinates, vector region_coordinates, vector look_at)
```

- Purpose: Teleports the owning agent (who must grant PERMISSION_TELEPORT) to region_coordinates within a target region specified by global_coordinates. Upon landing, the agent faces the direction look_at. Can only teleport the owner.

- Argument `agent` (key): UUID of the owning avatar to teleport.

- Argument `global_coordinates` (vector): Global coordinates vector of the target region (obtained via llRequestSimulatorData).

- Argument `region_coordinates` (vector): Target coordinates vector within the destination region.

- Argument `look_at` (vector): Position vector within the region (or unit direction vector if out of region) that the agent faces upon landing.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 414 | Native: False | Pure (no side effects): False

- Categories: avatar, permissions, teleport

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llTeleportAgentHome

```lsl
void llTeleportAgentHome(key avatar)
```

- Purpose: Teleports the avatar (who must be standing on land owned by the script owner) directly to their designated home location without warning (similar to a God Summons).

- Argument `avatar` (key): UUID of the avatar to teleport.

- Returns: void

- Energy cost: 100.0 | Script sleep after call: 5.0 s | Function ID: 158 | Native: False | Pure (no side effects): False

- Categories: avatar, land_moderation, teleport

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.

- Delay warning: this call sleeps the script for 5.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llTextBox

```lsl
void llTextBox(key agent, string msg, integer channel)
```

- Purpose: Opens an input text box dialog displaying msg to the agent. Submitting text chats the input string on channel as if said by the agent. The chat originates at the object's position, but uses the agent's name and UUID, so it can be heard as long as the agent is still in the region.

- Argument `agent` (key): UUID of the agent in the same region.

- Argument `msg` (string): Text message to display in the text box.

- Argument `channel` (integer): Output chat channel (any 32-bit signed integer value) where the input text is chatted.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 1.0 s | Function ID: 335 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, user_interface

- Delay warning: this call sleeps the script for 1.0 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.


## llToLower

```lsl
string llToLower(string src)
```

- Purpose: Returns a lowercase copy of the string src. Converts all unicode characters, not just ASCII.

- Argument `src` (string): Source string to convert.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 98 | Native: True | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llToUpper

```lsl
string llToUpper(string src)
```

- Purpose: Returns an uppercase copy of the string src. Converts all unicode characters, not just ASCII.

- Argument `src` (string): Source string to convert.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 97 | Native: True | Pure (no side effects): True

- Categories: string

- Guidance (string): Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.


## llTransferLindenDollars

```lsl
key llTransferLindenDollars(key destination, integer amount)
```

- Purpose: Transfers amount of L$ from the script owner to the destination avatar, requiring the PERMISSION_DEBIT permission. Returns a key query handle matching the resulting transaction_result event.

- Argument `destination` (key): UUID of the destination avatar.

- Argument `amount` (integer): Quantity of L$ to transfer (must be greater than 0).

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 395 | Native: False | Pure (no side effects): False

- Categories: money, permissions


## llTransferOwnership

```lsl
integer llTransferOwnership(key agent, integer flags, list options)
```

- Purpose: Transfers ownership of the object (or a copy of it, depending on Flags) to the specified agent. Returns an integer indicating the success or failure of the transfer.

- Argument `agent` (key): UUID of the agent to receive ownership of the object.

- Argument `flags` (integer): Flags controlling the transfer type (such as TRANSFER_FLAG_COPY or TRANSFER_FLAG_TAKE).

- Argument `options` (list): Extra options applied to the transfer (currently unused).

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 519 | Native: False | Pure (no side effects): False

- Categories: asset_permissions


## llTriggerSound

```lsl
void llTriggerSound(string sound, float volume)
```

- Purpose: Plays specified sound once at volume, centered at the object's current position but not attached (does not move with the object and cannot be stopped or adjusted). Does not affect attached sounds.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 91 | Native: False | Pure (no side effects): False

- Categories: sound


## llTriggerSoundLimited

```lsl
void llTriggerSoundLimited(string sound, float volume, vector top_north_east, vector bottom_south_west)
```

- Purpose: Plays the specified sound once at volume, centered at the object but not attached, restricted to the axis-aligned bounding box defined by the coordinates top_north_east and bottom_south_west.

- Argument `sound` (string): Name of a sound in the prim's inventory, or a UUID.

- Argument `volume` (float): Volume level to set, between 0.0 (silent) and 1.0 (loud).

- Argument `top_north_east` (vector): Top-north-east boundary position vector in region coordinates.

- Argument `bottom_south_west` (vector): Bottom-south-west boundary position vector in region coordinates.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 212 | Native: False | Pure (no side effects): False

- Categories: sound


## llUnSit

```lsl
void llUnSit(key id)
```

- Purpose: Forces the agent specified by id to stand up if they are sitting on the object containing the script, or are currently over land owned by the object's owner.

- Argument `id` (key): UUID of the avatar to unsit.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 220 | Native: False | Pure (no side effects): False

- Categories: avatar, sit

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llUnescapeURL

```lsl
string llUnescapeURL(string url)
```

- Purpose: Returns a string representing the unescaped/decoded version of url, replacing '%20' with spaces and decoding raw UTF-8 characters.

- Argument `url` (string): Escaped URL string to decode.

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 308 | Native: False | Pure (no side effects): True

- Categories: web


## llUpdateCharacter

```lsl
void llUpdateCharacter(list options)
```

- Purpose: Updates settings for a pathfinding character using the parameters specified in options.

- Argument `options` (list): A list of key-value pairs specifying the character's new configuration options (takes same constants as llCreateCharacter).

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 406 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llUpdateKeyValue

```lsl
key llUpdateKeyValue(string k, string v, integer checked, string original_value)
```

- Purpose: Starts an asynchronous transaction to update the key k to value v inside the experience datastore. If checked is TRUE, the update fails with XP_ERROR_RETRY_UPDATE unless the existing value matches original_value.

- Argument `k` (string): Key of the key-value pair to update.

- Argument `v` (string): New value for the key-value pair.

- Argument `checked` (integer): Boolean. If TRUE, requires the existing value to match original_value to complete the update; if FALSE, creates the key if needed.

- Argument `original_value` (string): String value to compare against the existing value in the datastore.

- Returns: key

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 389 | Native: False | Pure (no side effects): False

- Categories: data_storage, dataserver, experience, experience_data

- Guidance (experience): Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.


## llVecDist

```lsl
float llVecDist(vector vec_a, vector vec_b)
```

- Purpose: Returns a float representing the undirected, non-negative distance between vectors vec_a and vec_b.

- Argument `vec_a` (vector): First vector.

- Argument `vec_b` (vector): Second vector.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 14 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `vector.magnitude`. It's a fastcall.


## llVecMag

```lsl
float llVecMag(vector vec)
```

- Purpose: Returns the magnitude (geometric length) of vec.

- Argument `vec` (vector): Vector to evaluate.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 12 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `vector.magnitude`. It's a fastcall.


## llVecNorm

```lsl
vector llVecNorm(vector vec)
```

- Purpose: Returns the normalized unit vector pointing the same direction as vec. If <0, 0, 0>, return <0, 0, 0>.

- Argument `vec` (vector): Vector to normalize.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 13 | Native: False | Pure (no side effects): True

- Categories: math, math_3d, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.

- SLua: deprecated in favour of `vector.normalize`. It's a fastcall.


## llVerifyRSA

```lsl
integer llVerifyRSA(string public_key, string msg, string signature, string algorithm)
```

- Purpose: Returns TRUE if the Base64-formatted signature is verified as valid for the message msg when using the digest algorithm and public_key. Returns FALSE otherwise.

- Argument `public_key` (string): PEM-formatted public key to use for signature verification.

- Argument `msg` (string): Message string that was signed.

- Argument `signature` (string): Base64-encoded signature to verify.

- Argument `algorithm` (string): Cryptographic digest algorithm to use.

- Returns: integer

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 540 | Native: False | Pure (no side effects): False

- Categories: cryptography


## llVolumeDetect

```lsl
void llVolumeDetect(integer detect)
```

- Purpose: If detect is TRUE, enables VolumeDetect (object becomes phantom and physical objects/avatars can pass through it). Triggers collision_start on initial intersection and collision_end when intersection stops (standard collision events are suppressed while intersecting).

- Argument `detect` (integer): Boolean. If TRUE, enables VolumeDetect; if FALSE (default), disables it.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 248 | Native: False | Pure (no side effects): False

- Categories: physics, sensor


## llWanderWithin

```lsl
void llWanderWithin(vector origin, vector dist, list options)
```

- Purpose: Directs a pathfinding character to wander around a central coordinate origin, restricted within the bounding distance limits of dist and configured by options.

- Argument `origin` (vector): Center coordinate position vector to wander about.

- Argument `dist` (vector): A vector specifying the maximum distance limits (half-extents) along each world-aligned axis from the origin.

- Argument `options` (list): A list of WANDER_* flags and parameters to configure the wander behavior.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 401 | Native: False | Pure (no side effects): False

- Categories: pathfinding


## llWater

```lsl
float llWater(vector offset)
```

- Purpose: Returns a float representing the water height directly below the prim's position offset by the vector offset.

- Argument `offset` (vector): Offset relative to the prim's position, expressed in local coordinates.

- Returns: float

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 153 | Native: False | Pure (no side effects): False

- Categories: region


## llWhisper

```lsl
void llWhisper(integer channel, string msg)
```

- Purpose: Broadcasts the message msg to all scripts or agents listening on channel within llGetEnv("whisper_range"), which is 10m on most regions. Agents listen on PUBLIC_CHANNEL (0) and DEBUG_CHANNEL (2147483647). All other channels are for script-to-script communication.

- Argument `channel` (integer): Chat channel (any 32-bit signed integer value) to whisper the message on.

- Argument `msg` (string): Text message string to broadcast.

- Returns: void

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 22 | Native: False | Pure (no side effects): False

- Categories: avatar_communication, chat, script_communication


## llWind

```lsl
vector llWind(vector offset)
```

- Purpose: Returns a vector representing the wind velocity at the prim's position offset by the vector offset.

- Argument `offset` (vector): Offset relative to the prim's position, expressed in local coordinates.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 44 | Native: False | Pure (no side effects): False

- Categories: region


## llWorldPosToHUD

```lsl
vector llWorldPosToHUD(vector world_pos)
```

- Purpose: Returns the local position vector that places the center of the HUD object directly over the world coordinate world_pos as viewed by the current camera. Requires the PERMISSION_TRACK_CAMERA runtime permission.

- Argument `world_pos` (vector): World-frame position vector to project into HUD space.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 547 | Native: False | Pure (no side effects): False

- Categories: avatar, camera, permissions, user_interface

- Guidance (avatar): Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.


## llXorBase64

```lsl
string llXorBase64(string str1, string str2)
```

- Purpose: Correctly performs a bitwise exclusive OR (XOR) on Base64 strings str1 and str2, returning the result as a Base64 string. The string str2 repeats if it is shorter than str1.

- Argument `str1` (string): First Base64 string.

- Argument `str2` (string): Second Base64 string (will repeat if shorter than str1).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 522 | Native: False | Pure (no side effects): True

- Categories: data_conversion


## llXorBase64Strings

```lsl
string llXorBase64Strings(string str1, string str2)
```

- Purpose: Deprecated (use llXorBase64 instead). Retained for backwards compatibility. Incorrectly performs a bitwise exclusive OR (XOR) on Base64 strings str1 and str2.

- Argument `str1` (string): First Base64 string.

- Argument `str2` (string): Second Base64 string (will repeat if shorter than str1).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.3 s | Function ID: 262 | Native: False | Pure (no side effects): True

- Categories: data_conversion

- Delay warning: this call sleeps the script for 0.3 s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.

- Deprecated in LSL: {'use': 'll.XorBase64', 'selene-replace': ['ll.XorBase64(%1, %2)']}


## llXorBase64StringsCorrect

```lsl
string llXorBase64StringsCorrect(string str1, string str2)
```

- Purpose: Deprecated (use llXorBase64 instead). Correctly performs (unless nulls are present) a bitwise exclusive OR (XOR) on Base64 strings str1 and str2.

- Argument `str1` (string): First Base64 string.

- Argument `str2` (string): Second Base64 string (will repeat if shorter than str1).

- Returns: string

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 319 | Native: False | Pure (no side effects): True

- Categories: data_conversion

- Deprecated in LSL: {'use': 'll.XorBase64', 'selene-replace': ['ll.XorBase64(%1, %2)']}


## llsRGB2Linear

```lsl
vector llsRGB2Linear(vector color)
```

- Purpose: Returns a linear RGB colorspace vector converted from the sRGB colorspace argument.

- Argument `color` (vector): Color vector in the sRGB colorspace to convert.

- Returns: vector

- Energy cost: 10.0 | Script sleep after call: 0.0 s | Function ID: 716 | Native: False | Pure (no side effects): False

- Categories: data_conversion, math, prim_appearance, vector

- Guidance (math): Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.
