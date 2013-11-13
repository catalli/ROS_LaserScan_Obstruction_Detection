#!/usr/bin/env python
# Copyright 2013 Ali Cataltepe, licensed under Creative Commons 3.0.
# This library contains functions which allow a robot using the LaserScan
# message format for its sensors to detect obstacles to the front, left and
# right.
import config
import roslib; roslib.load_manifest(packagename)
import rospy
from sensor_msgs.msg import LaserScan

# Analyzes data sent from the sensors function, and cycles through different
# portions of it in order to check for obstacles. Afterwards, a list
# containing letters, the presence of which depends on the presence of an
# obstacle to the side represented by the adorementioned letter. The robot can
# then make decisions according to the presence or lack thereof of obstacles.
def obstrdetect(data):  
	obstr = []
	# You can configure the index numbers for the slices which will be
	# scanned in config.py
	leftend = 684
	for x in data.ranges[config.frontbegin:config.frontend]:
		if x < config.frontdistance:
			print 'Obstruction to the front!'
			obstr.append('f')
			break
	for y in data.ranges[config.rightbegin:config.rightend]:
		if y < config.rightdistance:
			print 'Obstruction to the right!'
			obstr.append('r')
			break
	for z in data.ranges [config.leftbegin:config.leftend]:
		if z < config.leftdistance:
			print 'Obstruction to the left!'
			obstr.append('l')
			break
	return obstr

# Periodically calls obstrdetect with the sensor data as arguments.
def sensors():
	rospy.init_node('sensub')	
	rospy.Subscriber('Delete and replace with the name of the topic your robot is publishing its sensor data to', LaserScan, obstrdetect)
	rospy.spin()
