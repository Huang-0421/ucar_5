#!/usr/bin/env python
#_*_coding: UTF-8 _*_
import rospy
from std_msgs.msg import String
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
from sound_play.libsoundplay import SoundClient

f=0
soundhandle = SoundClient()

def turning():
    # global Img_publish,img_pub,img_num,run_flag,turn_flag
    base_driver_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate=rospy.Rate(100)
    print("开转！！！")
    a=0
    while (not rospy.is_shutdown()) and a<140:    #大概是270度  
        vel=Twist()
        vel.linear.y=0.0
        vel.linear.z=0.0
        vel.angular.x=0.0
        vel.angular.y=0.0
        vel.angular.z=5.0
        base_driver_pub.publish(vel)
        a=a+1
        rate.sleep()
    rospy.sleep(0.7)

def goal_callback(msg):    #更新小车位置信息
    global f
    rospy.sleep(1) 
    f=f+1
    print("回调函数启动")

if __name__ == '__main__':
    rospy.init_node('play_lzl', anonymous=True)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)    
    goal_pose = PoseStamped()
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点   

    goal_pub.publish(goal_pose)
    time.sleep(5)
    
    # while(1):
    #     if f==0:
    #         goal_pose = PoseStamped()  
    #         goal_pose.header.frame_id = "map" #E点
    #         goal_pose.pose.position.x = 3.108
    #         goal_pose.pose.position.y = -0.799
    #         goal_pose.pose.position.z = 0.000
    #         goal_pose.pose.orientation.x = 0
    #         goal_pose.pose.orientation.y = 0
    #         goal_pose.pose.orientation.z = 0.999
    #         goal_pose.pose.orientation.w = -0.032
    #         goal_pub.publish(goal_pose)
    #         rospy.loginfo("goal_pose E has pubed")
    #         f=f+1
            
    #     elif f==2: 
    #         goal_pose = PoseStamped()  
    #         goal_pose.header.frame_id = "map" #终点
    #         goal_pose.pose.position.x = -0.115
    #         goal_pose.pose.position.y = 0.020
    #         goal_pose.pose.position.z = 0.000
    #         goal_pose.pose.orientation.x = 0
    #         goal_pose.pose.orientation.y = 0
    #         goal_pose.pose.orientation.z = -0.016
    #         goal_pose.pose.orientation.w = 1.000
    #         goal_pub.publish(goal_pose)
    #         rospy.loginfo("goal_pose X has pubed")
    #         break

    rospy.spin()    