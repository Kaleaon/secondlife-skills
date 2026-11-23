# LSL Events Reference (generated from secondlife/lsl-definitions)


## at_rot_target(integer handle, rotation targetrot, rotation ourrot)

- Purpose: Triggered when the script's rotation (ourrot) comes within a defined angle (error) of the target rotation (targetrot) set by a call to llRotTarget (which returns the associated handle).

- Event ID: 22 | Categories: movement

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## at_target(integer tnum, vector targetpos, vector ourpos)

- Purpose: Triggered when the scripted object's position (ourpos) comes within the defined range of the target position (targetpos) set by llTarget (which returns the associated handle tnum).

- Event ID: 20 | Categories: movement

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## attach(key avatar)

- Purpose: Triggered whenever the object is attached to or detached from an avatar. Passes the UUID key of the avatar if attached, or NULL_KEY if detached.

- Event ID: 26 | Categories: attachments

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## changed(integer changes)

- Purpose: Triggered when various properties of the object change. The parameter changes is a bitfield of CHANGED_* flags.

- Event ID: 25 | Categories: asset_permissions, linkset, media, prim_appearance, prim_inventory, prim_media, region, teleport, script, sit

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## collision(integer num_detected)

- Purpose: Triggered continuously while an avatar or another object is colliding with the object containing the script. Passes num_detected, representing the number of detected collisions.

- Event ID: 7 | Categories: detected, physics, sensor

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## collision_end(integer num_detected)

- Purpose: Triggered when an avatar or another object stops colliding with the object containing the script. Passes num_detected, representing the number of detected collisions.

- Event ID: 8 | Categories: detected, physics, sensor

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## collision_start(integer num_detected)

- Purpose: Triggered when an avatar or another object first begins colliding with the object containing the script. Passes num_detected, representing the number of detected collisions.

- Event ID: 6 | Categories: detected, physics, sensor

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## control(key id, integer level, integer edge)

- Purpose: Triggered to pass captured avatar control inputs into the script. The parameter level indicates held controls, and edge indicates change in controls (both are bitfields of CONTROL_* constants).

- Event ID: 17 | Categories: avatar, input

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## dataserver(key queryid, string data)

- Purpose: Triggered when requested data is returned to the script (e.g., from llRequestAgentData, llRequestInventoryData, or llGetNotecardLine).

- Event ID: 27 | Categories: dataserver

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## email(string time, string address, string subject, string msg, integer num_left)

- Purpose: Receive an email requested by llGetNextEmail(). NumberRemaining indicates the number of emails remaining in the queue for llGetNextEmail() to retrieve.

- Event ID: 19 | Categories: script_communication

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## experience_permissions(key agent_id)

- Purpose: Triggered when the agent specified by agent_id approves an experience permissions request (interactively or automatically if previously approved).

- Event ID: 35 | Categories: avatar, experience, permissions

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## experience_permissions_denied(key agent_id, integer reason)

- Purpose: Triggered when the agent specified by agent_id denies experience permissions, or when permission is blocked for other reasons (specified by the error code reason).

- Event ID: 38 | Categories: avatar, experience, permissions

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## final_damage(integer num_detected)

- Purpose: Triggered after all on_damage events across all scripts have completed and damage is actively applied to the avatar or distributed among seated avatars. Collision detected functions (llDetected*) and llDetectedDamage are available.

- Event ID: 43 | Categories: combat, detected

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## game_control(key id, integer button_levels, list axes)

- Purpose: Triggered when a compatible viewer sends game controller input changes for the avatar specified by id. Only triggers for scripts in attachments or seats.

- Event ID: 40 | Categories: avatar, game_control, input

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## http_request(key request_id, string method, string body)

- Purpose: Triggered when the script's registered URL receives an incoming HTTP request identified by request_id.

- Event ID: 34 | Categories: script_communication, web

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## http_response(key request_id, integer status, list metadata, string body)

- Purpose: Triggered when an HTTP response body is received for a pending request_id, or if the request fails or times out.

- Event ID: 33 | Categories: script_communication, web

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## land_collision(vector pos)

- Purpose: Triggered in the root prim when a physical object or attached avatar is colliding with the ground at position pos.

- Event ID: 10 | Categories: physics

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## land_collision_end(vector pos)

- Purpose: Triggered in the root prim when a physical object or attached avatar stops colliding with the ground at position pos.

- Event ID: 11 | Categories: physics

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## land_collision_start(vector pos)

- Purpose: Triggered in the root prim when a physical object or attached avatar first begins colliding with the ground at position pos.

- Event ID: 9 | Categories: physics

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## link_message(integer sender_num, integer num, string str, key id)

- Purpose: Triggered when the script receives a link message from sender_num, containing the parameters num, str, and id sent via llMessageLinked.

- Event ID: 28 | Categories: script_communication

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## linkset_data(integer action, string name, string value)

- Purpose: Fires in all scripts in the linkset whenever the linkset datastore is modified via an llLinksetData function. Passes the action taken, the affected key name, and the new value.

- Event ID: 39 | Categories: data_storage, linkset, linkset_data

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## listen(integer channel, string name, key id, string msg)

- Purpose: Triggered when a chat message matching active llListen filters is received on channel. Passes the sender's name and UUID key id, along with the spoken string msg.

- Event ID: 13 | Categories: avatar_communication, chat, script_communication

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## money(key id, integer amount)

- Purpose: Triggered when a resident specified by id pays an amount of Linden dollars (L$) to the prim.

- Event ID: 18 | Categories: money

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## moving_end()

- Purpose: Triggered whenever the physical or moving object containing the script stops moving.

- Event ID: 30 | Categories: movement, pathfinding

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## moving_start()

- Purpose: Triggered whenever the physical or moving object containing the script starts moving.

- Event ID: 29 | Categories: movement, pathfinding

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## no_sensor()

- Purpose: Triggered when active sensors (from llSensor or llSensorRepeat) complete a scan without finding any matching targets.

- Event ID: 16 | Categories: detected, sensor

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## not_at_rot_target()

- Purpose: Triggered continuously while the object's rotation is outside the leeway angle of targets set via llRotTarget.

- Event ID: 23 | Categories: movement

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## not_at_target()

- Purpose: Triggered continuously while the object's position has not yet reached the range of targets set via llTarget.

- Event ID: 21 | Categories: movement

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## object_rez(key id)

- Purpose: Triggered when this object successfully rezzes another object from its inventory. Passes the key (UUID) id of the newly rezzed object.

- Event ID: 31 | Categories: rez

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## on_damage(integer num_detected)

- Purpose: Triggered when damage has been inflicted on an avatar or task, but before it is applied or distributed. Collision detected functions (llDetected*), llDetectedDamage, and llAdjustDamage are available. Passes num_detected, representing the number of pending damage events.

- Event ID: 42 | Categories: combat, detected

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## on_death()

- Purpose: Triggered on all worn attachments when the wearing avatar's health reaches 0.

- Event ID: 41 | Categories: combat

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## on_rez(integer start_param)

- Purpose: Triggered when the object is rezzed into the world (by a script or user). Passes start_param from the rezzing call (or 0 if rezzed from inventory). Also triggers on attachments during login or when attached from inventory.

- Event ID: 14 | Categories: rez, script

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## path_update(integer type, list reserved)

- Purpose: Triggered to inform the script of changes or failures in the pathfinding character's status.

- Event ID: 37 | Categories: pathfinding

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## remote_data(integer event_type, key channel, key message_id, string sender, integer idata, string sdata)

- Purpose: Deprecated. Triggered by incoming XML-RPC calls, passing event_type, channel, message_id, sender, idata, and sdata.

- Event ID: 32 | Categories: script_communication

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## run_time_permissions(integer perm)

- Purpose: Triggered when an agent grants or denies runtime permissions requested by llRequestPermissions. Passes the active integer permissions bitfield perm (returns 0 if no permissions are currently granted).

- Event ID: 24 | Categories: permissions

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## sensor(integer num_detected)

- Purpose: Triggered when objects matching constraints of llSensor or llSensorRepeat are successfully detected. Passes num_detected, representing the number of detected targets.

- Event ID: 15 | Categories: detected, sensor

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## state_entry()

- Purpose: Triggered immediately whenever a new state is entered (including at script start). It is always the first event handled.

- Event ID: 1 | Categories: script

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.

- SLua: this event model does not carry to SLua in the same form. Check slua_definitions.yaml before porting.


## state_exit()

- Purpose: Triggered when the state command is used to transition out of the current state. Handled before entering the new state's state_entry.

- Event ID: 2 | Categories: script

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.

- SLua: this event model does not carry to SLua in the same form. Check slua_definitions.yaml before porting.


## timer()

- Purpose: Triggered at regular periodic intervals configured by llSetTimerEvent.

- Event ID: 12 | Categories: script, time

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## touch(integer num_detected)

- Purpose: Triggered continuously while an avatar touches the object. Passes num_detected, representing the number of touching agents.

- Event ID: 4 | Categories: detected, touch, user_interface

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## touch_end(integer num_detected)

- Purpose: Triggered when an avatar stops touching the object. Passes num_detected, representing the number of touching agents.

- Event ID: 5 | Categories: detected, touch, user_interface

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## touch_start(integer num_detected)

- Purpose: Triggered when an avatar first touches the object. Passes num_detected, representing the number of touching agents.

- Event ID: 3 | Categories: detected, touch, user_interface

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.


## transaction_result(key id, integer success, string data)

- Purpose: Triggered when an asynchronous L$ transfer (such as llTransferLindenDollars) is completed. Passes transaction info id, success status, and CSV or error data.

- Event ID: 36 | Categories: money

- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.
