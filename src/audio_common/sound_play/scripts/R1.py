#!/usr/bin/env python
#_*_coding: UTF-8 _*_
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from darknet_ros_msgs.msg import classes
from darknet_ros_msgs.msg import BoundingBoxes
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped,Twist
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from actionlib_msgs.msg import GoalStatusArray
from  math import pi
import  os
import time


if __name__ == '__main__':
    print("执行play_Regis")
    rospy.init_node('play_Reg is', anonymous=True)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    goal_pose = PoseStamped() 
    goal_pose.header.frame_id = "map"
    goal_pose.pose.position.x = 0.694
    goal_pose.pose.position.y = 0.075
    goal_pose.pose.position.z = 0.000
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = -0.015
    goal_pose.pose.orientation.w = 1.000
    goal_pub.publish(goal_pose)
    print("22222222222222222")
    rospy.sleep(1)

    goal_pose.pose.position.x = 0.822
    goal_pose.pose.position.y = 1.272
    goal_pose.pose.position.z = 0.000
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = 0.003
    goal_pose.pose.orientation.w = 1.000
    goal_pub.publish(goal_pose)
    print("333333333333333333333")
    rospy.sleep(1)

    goal_pose.pose.position.x = 1.648
    goal_pose.pose.position.y = 1.297
    goal_pose.pose.position.z = 0.000
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = -0.019
    goal_pose.pose.orientation.w = 1
    goal_pub.publish(goal_pose)
    print("444444444444444444444444")
    rospy.sleep(1)

    goal_pose.pose.position.x = 0.822 
    goal_pose.pose.position.y = 1.272
    goal_pose.pose.position.z = 0.000
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = -0.716
    goal_pose.pose.orientation.w = 0.698
    goal_pub.publish(goal_pose)
    rospy.sleep(1)

    goal_pose.pose.position.x = 0.694
    goal_pose.pose.position.y = 0.075
    goal_pose.pose.position.z = 0.000
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = 1
    goal_pose.pose.orientation.w = 0.017
    goal_pub.publish(goal_pose)
    rospy.sleep(1)

    goal_pose.pose.position.x = 0
    goal_pose.pose.position.y = 0
    goal_pose.pose.position.z = 0
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = 0
    goal_pose.pose.orientation.w = 1
    goal_pub.publish(goal_pose)
    rospy.sleep(1)

    rospy.spin()   