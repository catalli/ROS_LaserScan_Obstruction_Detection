Copyright 2013 Ali Cataltepe, licensed under Creative Commons 3.0.

SETTING UP THE MODULE
First make sure you are using ROS Fuerte, and that the files config.py and ROS-LaserScan-Obstruction-Detection.py are in the same folder. The package you are using the script in should have rospy and sensor_msgs as a dependencies, in addition to any other dependencies your package has. Make sure both scripts are executable, and that they are in the same folder whichever script importing them is in. Go to config.py and edit the variables according to the specifications of your laser scanner.

USING THE MODULE
When writing a script which uses the functions in ROS-LaserScan-Obstruction-Detection.py, write "import ROS-LaserScan-Obstruction-Detection” preceding the point where the functions defined within it are first used. To use the library's functions, simply call the sensors() function by writing “ROS-LaserScan-Obstruction-Detection.sensors()" in the script. This should provide a constantly updating "obstr" list, which other functions can then reference.