#!/usr/bin/env python
# Copyright 2013 Ali Cataltepe, licensed under Creative Commons 3.0.
# This library contains functions which allow a robot using the LaserScan
# message format for its sensors to detect obstacles to the front, left and
# right.
import config
import roslib; roslib.load_manifest(config.packagename)
import rospy
import math
from sensor_msgs.msg import LaserScan
from assignment1.msg import ObstructionList

# Analyzes data sent from the sensors() function, and cycles through different
# portions of it in order to check for obstacles. Adds boolean values to the
# obstr dataset. These values denote the presence or absence of an obstacle in
# a given direction. A value can be accessed by typing obstr.name (or whichever
# variable represents obstr). For example, the value of obstr.frontobstr denotes
# the presence or absence of an obstacle to the robot's front.
def obstrdetect(data):
	obstr = ObstructionList()
	obstr.frontobstr = False; obstr.rightobstr = False; obstr.leftobstr = False; obstr.frontrightobstr = False; obstr.frontleftobstr = False;
	# You can configure the index numbers for the slices which will be
	# scanned in config.py.
	for x in data.ranges[config.frontbegin:config.frontend]:
		if x < config.frontdistance:
			obstr.frontobstr = True;
			break
	for y in data.ranges[config.rightbegin:config.rightend]:
		if y < config.rightdistance:
			obstr.rightobstr = True;
			break
	for z in data.ranges[config.leftbegin:config.leftend]:
		if z < config.leftdistance:
			obstr.leftobstr = True;
			break
	for t in data.ranges[config.frontrightbegin:config.frontrightend]:
		if t < config.frontrightdistance:
			obstr.frontrightobstr = True;
			break
	for v in data.ranges[config.frontleftbegin:config.frontleftend]:
		if v < config.frontleftdistance:
            obstr.frontleftobstr = True;
			break
	obstrpub = rospy.Publisher('obstructions', ObstructionList)
	timeofpub = rospy.time.now()
	obstr.pubtime = timeofpub;
	obstrpub.publish(obstr)

# Examines outliers in the sensor data to provide more reliable results.
def datafilter(data):
	avg = sum(data.ranges)/len(data.ranges)
	varianceslist = []
	for x in data.ranges:
		varianceslist.append((x-avg)**2)
	stddev = math.sqrt(sum(varianceslist)/(len(data.ranges)-1))
	outliers = {}
	for x in range(len(data.ranges)):
		if math.fabs(data.ranges[x]-avg) > stddev*config.outlierthreshold:
			outliers.update({x:data.ranges[x]})
	outlierkeys = outliers.keys()
	outlierkeys.sort()
	for x in range(1, len(outlierkeys)-1):
		if math.fabs(outlierkeys[x]-outlierkeys[x-1]) > len(data.ranges)/10 or math.fabs(outlierkeys[x]-outlierkeys[x+1]) > len(data.ranges)/10:
			del data.ranges[x]
			data.ranges.insert(x, avg)
	filtereddata = data
	filterpub = rospy.Publisher('filteredlaser', LaserScan)
	filterpub.publish(filtereddata)
	rospy.Subscriber('filteredlaser', LaserScan, obstrdetect)

# Calls obstrdetect or datafilter with the sensor data as arguments.
def sensors():
	if config.autofilter == False:
		rospy.Subscriber(config.subscribednode, LaserScan, obstrdetect)
	elif config.autofilter == True:
		rospy.Subscriber(config.subscribednode, LaserScan, datafilter)