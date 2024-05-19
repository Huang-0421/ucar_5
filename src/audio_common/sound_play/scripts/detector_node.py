#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String
# from move_base_msgs.msg import MoveBaseAction
# from move_base_msgs.msg import MoveBaseGoal
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from actionlib_msgs.msg import GoalStatusArray
from darknet_ros_msgs.msg import BoundingBoxes
from darknet_ros_msgs.msg import classes


f=-1
seq1=0
seq2=0

def boxes_callback(msg):
    global f,seq1,seq2
    seq1=msg.image_header.seq
    if seq1!=1:
        if f==-1 or seq2!=seq1:
            seq2=msg.image_header.seq
            f=f+1
            print("第%d张图片识别结果"%(f))
            print(msg.bounding_boxes)
            result_pub.publish(msg)
    else:
        if msg.header.seq==0:
            seq2=msg.image_header.seq
            f=f+1
            print("第%d张图片识别结果"%(f))
            print(msg.bounding_boxes)
            result_pub.publish(msg)



if __name__ == '__main__':
    print("执行detector_node")
    rospy.init_node('detector', anonymous=True)
    rospy.Subscriber('/darknet_ros/bounding_boxes',BoundingBoxes, boxes_callback)
    result_pub = rospy.Publisher('/image_result',BoundingBoxes,queue_size=1)
    rospy.spin()  
