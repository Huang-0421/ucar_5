#!/usr/bin/env python
#_*_coding: UTF-8 _*_
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
# from darknet_ros_msgs.msg import classes
# from darknet_ros_msgs.msg import BoundingBoxes
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped,Twist
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from actionlib_msgs.msg import GoalStatusArray
from  math import pi
import  os



fang_bedding=0
fang_dinning=0
fang_living=0


fang33=0
fang3=0
flag_3=0


f=0
img_flag=0
seq=-1
error_image_num=0#这里定义一个图像数目误差的变量，因为如果使用了快捷的图像识别，那么会使得在部分房间识别的图像数目不足三张，这样会使得在boxes_callback回调函数中图片和房间对应错误，因此加上一个error_image_num来修正减少的图片数目
first_image=0
fang="b1c2d3"
b_room=[0]
c_room=[0]
d_room=[0]
Img_publish=Image()
soundhandle = SoundClient()


def img_callback(data):
    global f,img_flag,Img_publish,fang,b_room,c_room,d_room,first_image,fang_list,fang3,fang33

    if f==1 :
        if img_flag == 0:
            img_flag = 1
            goal_pose = PoseStamped()               #第二个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.994
            goal_pose.pose.position.y = -4.303
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  -0.707
            goal_pose.pose.orientation.w = 0.707
            goal_pub.publish(goal_pose)

    elif f==2 :
        if img_flag == 1:
            img_flag = 2
            goal_pose = PoseStamped()               #第三个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.701
            goal_pose.pose.position.y = -2.589
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.677
            goal_pose.pose.orientation.w = 0.736
            goal_pub.publish(goal_pose)
    elif f==3 :
        if img_flag == 2:
            img_flag = 3
            goal_pose = PoseStamped()               #终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.100
            goal_pose.pose.position.y = -0.950
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.000
            goal_pub.publish(goal_pose)


    elif f==4:
        if img_flag == 3:
            print(fang)
            fang="b1c1d1"
            argv = '/home/ucar/ucar_ws/src/audio_common/mp3/'+fang+'.mp3'
            soundhandle.playWave(argv) 
            # os.system("ffplay "+argv)
            print ('到达终点')
            f=f+1
    else:
        pass




def goal_callback(msg):
    #更新小车位置信息
    global f
    if msg.status.status == 3:       
        if f <5:
            # rospy.sleep(1.0)
            f+=1
    print('到达第%d个位置'%(f))   
    print("第%d张图片已发布"%(f))       


if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    rospy.spin()    
