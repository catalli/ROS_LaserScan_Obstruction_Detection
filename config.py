#!/usr/bin/env python
# Assign the name of your package to the 'packagename' variable.
# Assign the name of the node your laser scanner transmits data from to the
# 'subscribednode' variable.
# Assign your package's unquoted .msg file name (yourpackagename.msg) to the
# 'messagefile' variable.
# Enter the values for the boundaries of the slices denoting the front, left
# and right of your robot, and the minimum distance (m) for the laser scans
# to be considered obstructions.
packagename = 'your package name here'
subscribednode = 'your subscribed topic name here'
frontbegin = 227
frontend = 454
rightbegin = 0
rightend = 226
leftbegin = 454
leftend = 684
frontdistance = 1.0
rightdistance = 1.0
leftdistance = 1.0