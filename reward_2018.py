

import math
def reward_function(params):
#############################################################################
'''
Example of using all_wheels_on_track and speed
'''

	# Read input variables
	all_wheels_on_track = params['all_wheels_on_track']
	speed = params['speed']
	waypoints = params['waypoints']
	closest_waypoints = params['closest_waypoints']
	nextwp = closest_waypoints[1]
	track_width = params['track_width']
	distance_from_center = params['distance_from_center']
	progress = params['progress']
	heading = params['heading']

	# Set the speed threshold based your action space
	SPEED_THRESHOLD_STRAIGHT = 5
	print ("PROGRESS ", progress)
	reward = 1.0
	if not all_wheels_on_track:
	# Penalize if the car goes off track
		reward = 1e-3
	else:
	# High reward if the car stays on track and goes fast
		reward += progress

	# Calculate the direction of the center line based on the closest waypoints
	next_point = waypoints[closest_waypoints[1]]
	prev_point = waypoints[closest_waypoints[0]]

	# Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
	track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
	# Convert to degree
	track_direction = math.degrees(track_direction)

	# Calculate the difference between the track direction and the heading direction of the car
	direction_diff = abs(track_direction - heading)

	# Penalize the reward if the difference is too large
	DIRECTION_THRESHOLD = 10.0
	if direction_diff > DIRECTION_THRESHOLD:
		reward *= 0.5

	# Penalize if the car is too far away from the center
	marker_1 = 0.1 * track_width
	marker_2 = 0.3 * track_width
	marker_3 = 0.5 * track_width

	if distance_from_center <= marker_1:
	   reward = reward + (progress * 2.5)
	elif distance_from_center <= marker_2:
	   reward = reward + progress * 2
	elif distance_from_center <= marker_3:
	   reward = reward + (progress * 1.5)
	else:
	   reward = 1e-3  # likely crashed/ close to off track


	if progress == 100:
		reward +=10000

	return float(reward)