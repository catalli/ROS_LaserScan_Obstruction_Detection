Copyright 2013 Ali Cataltepe, licensed under Creative Commons 3.0.

SETTING UP THE MODULE
First make sure you are using ROS fuerte, and that the files config.py and erraticObstruction detection.py are in the same folder. The package you are using the script in should have rospy and sensor_msgs as a dependencies, in addition to any other dependencies your package has. Make sure both scripts are executable, and that they are in the same folder whichever script is importing them is in. Open erraticObstructionDetection.py and make the required changes to the names of the subscribed topic and the package. If the specifications of your laser scanner are different, you may also want to make changes to the config.py file.

USING THE MODULE
When writing a script which uses the functions in erraticObstructionDetection.py, write "import erraticObstructionDetection" preceding the point where the functions defined within it are first used. To use the library's functions, simply call the sensors() (by writing "erraticObstructionDetection.sensors()" in the script) function. This should provide a constantly updating "obstr" list, which other functions can then reference.
