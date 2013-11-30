#!/usr/bin/env python
# Assign the name of your package to the 'packagename' variable.
# Assign the name of the node your laser scanner transmits data from to the
# 'subscribednode' variable.
# Enter the values for the boundaries of the slices denoting the front,
# left, right, front-left and front-right of your robot, and the minimum
# distance (m) for the laser scans
# to be considered obstructions.
packagename = 'your package name here'
subscribednode = 'your subscribed topic name here'
frontbegin = 260
frontend = 390
rightbegin = 0
rightend = 130
leftbegin = 550
leftend = 684
frontrightbegin = 130
frontrightend = 260
frontleftbegin = 420
frontleftend = 550
frontdistance = 1.0
rightdistance = 1.0
leftdistance = 1.0
frontleftdistance = 1.0
frontrightdistance = 1.0