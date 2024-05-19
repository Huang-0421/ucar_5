#!/usr/bin/env python2
#_*_coding: UTF-8 _*_

import rospy
from std_msgs.msg import String
from darknet_ros_msgs.msg import classes
from darknet_ros_msgs.msg import BoundingBoxes

def do_check_image(msg):
    print(type(msg.bounding_boxes))

if __name__ == "__main__":
    rospy.init_node("check_image_node")
    sub = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, do_check_image)
    sub = rospy.Subscriber("/image_result", BoundingBoxes, do_check_image)
    rospy.spin()