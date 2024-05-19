#!/usr/bin/env python
from termios import VEOL
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from darknet_ros_msgs.msg import classes
# from move_base_msgs.msg import MoveBaseAction
# from move_base_msgs.msg import MoveBaseGoal
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from geometry_msgs.msg import Twist
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


def turning():
    rospy.init_node('play', anonymous=True)
    base_driver_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate=rospy.Rate(20)
    for i in range(5):
        f=0
        while (not rospy.is_shutdown()) and f<10:    #16大概是90度  
            vel=Twist()
            vel.linear.x=0.0
            vel.linear.y=0.0
            vel.linear.z=0.0
            vel.angular.x=0.0
            vel.angular.y=0.0
            vel.angular.z=6.0
            base_driver_pub.publish(vel)
            f=f+1
            print("转！！！")
            rate.sleep()
        rospy.sleep(0.6)
        

if __name__ == '__main__':
    turning()
