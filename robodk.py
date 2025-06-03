# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:05:48 2024

@author: gunsto
"""

# You can also use the new version of the API:
from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
RDK = robolink.Robolink()# Any interaction with RoboDK must be done through RDK:


# get the robot by name:
robot = RDK.Item('',robolink.ITEM_TYPE_ROBOT)

print(robot.Valid())

# get the home target and the welding targets:
home = RDK.Item('Home')
target = RDK.Item('Target 1')

print(home.Pose())

# get the pose of the target (4x4 matrix representing position and orientation):
poseref = target.Pose()

# move the robot to home, then to the Target 1:
robot.MoveJ(home)
robot.MoveJ(target)

#make an hexagon around the Target 1:
for i in range(7):
    ang = i*2*robomath.pi/6 #angle: 0, 60, 120, ...
    posei = poseref*robomath.rotz(ang)*robomath.transl(200,0,0)*robomath.rotz(-ang)
    robot.MoveL(posei)

# move back to the center, then home:
robot.MoveL(target)
robot.MoveJ(home)