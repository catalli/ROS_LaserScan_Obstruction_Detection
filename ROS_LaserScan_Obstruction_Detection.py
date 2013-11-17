#!/usr/bin/env python
# Copyright 2013 Ali Cataltepe, licensed under Creative Commons 3.0.
# This library contains functions which allow a robot using the LaserScan
# message format for its sensors to detect obstacles to the front, left and
# right.
import config
import roslib; roslib.load_manifest(config.packagename)
import rospy
from sensor_msgs.msg import LaserScan
from '''YOURPACKAGENAME'''.msg import ObstructionList

# Analyzes data sent from the sensors function, and cycles through different
# portions of it in order to check for obstacles. Adds boolean values to the
# obstr dataset. These values denote the presence or absence of an obstacle in
# a given direction. A value can be accessed by typing obstr.name (or whichever
# variable represents obstr). For example, the value of obstr.frontobstr denotes
# the presence or absence of an obstacle to the robot's front.
def obstrdetect(data):
	obstr = ObstructionList()
	obstr.frontobstr = False; obstr.rightobstr = False; obstr.leftobstr = False;
	# You can configure the index numbers for the slices which will be
	# scanned in config.py.
	for x in data.ranges[config.frontbegin:config.frontend]:
		if x < config.frontdistance:
			obstr.frontobstr = True
			break
	for y in data.ranges[config.rightbegin:config.rightend]:
		if y < config.rightdistance:
			obstr.rightobstr = True
			break
	for z in data.ranges [config.leftbegin:config.leftend]:
		if z < config.leftdistance:
			obstr.leftobstr = True
			break
	obstrpub = rospy.Publisher('obstructions', ObstructionList)
	obstrpub.publish(obstr)

# Calls obstrdetect with the sensor data as arguments.
def sensors():
	rospy.Subscriber(config.subscribednode, LaserScan, obstrdetect)