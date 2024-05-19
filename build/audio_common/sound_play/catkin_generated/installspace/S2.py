#!/usr/bin/env python2
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


f=0
img_flag=0
first_image=0
num_terror=0
room_1=[]  # for 恐怖分子
room_2=[]  # for 急救包
room_3=[]  # for 武器

get_weapon = 0
Img_publish=Image()
soundhandle = SoundClient()

get_spontoon = 0
get_armor = 0
get_bomb = 0

def room_class(rlist):
    global f,num_terror,get_spontoon,get_armor,get_bomb
    if f==2:  
        if 'terrorist_1' in rlist:
            num_terror=1
        if 'terrorist_2' in rlist:
            num_terror=2
        if 'terrorist_3' in rlist:
            num_terror=3
        print("恐怖分子的数量为：", num_terror)

    if f==4:
        if 'spontoon' in rlist:
            get_spontoon = 1
        if 'armor' in rlist:
            get_armor = 1
        if 'bomb' in rlist:
            get_bomb = 1

    

def room_sound():
    global num_terror,get_weapon
    if f==1:
        time.sleep(2)
        if num_terror== 1:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"terrorist_1"+'.mp3'
            soundhandle.playWave(argv) 
        elif num_terror== 2:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"terrorist_2"+'.mp3'
            soundhandle.playWave(argv) 
        elif num_terror== 3:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"terrorist_3"+'.mp3'
            soundhandle.playWave(argv) 
        time.sleep(3)

    elif f == 3 :
        time.sleep(3)
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"急救包"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(3)

    if f==4 and num_terror==1:
        time.sleep(3)
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"警棍"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(3)
        get_weapon = 1

    if f==5 and num_terror==2:
        time.sleep(3)
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"防弹衣"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(3)
        get_weapon = 1

    if f==6 and num_terror==3:
        time.sleep(3)
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"催泪瓦斯"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(3)
        get_weapon = 1

    if f==7:
        time.sleep(3)
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"结束"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(3)



def img_callback(data):
    global f,img_flag,Img_publish,first_image,img_flag,first_image,goal_pose
    
    Img_publish = data

    if first_image<=150 and first_image>=0:
        first_image=1+first_image
        if first_image%10==0:
            print(first_image)
    else:
        if first_image >0:
            img_pub.publish(Img_publish)
            print("first image")
            first_image = -1

    if f==1 :
        if img_flag == 1 :
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" 
            goal_pose.pose.position.x = 0.852
            goal_pose.pose.position.y = 1.552
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.010
            goal_pose.pose.orientation.w = 1
            goal_pub.publish(goal_pose)
            print("到达第二个点,识别恐怖分子")
            img_flag = 2
    
    if f==2 :
        if img_flag == 2:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #原点
            goal_pose.pose.position.x = 0
            goal_pose.pose.position.y = 0
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0
            goal_pose.pose.orientation.w = 1
            goal_pub.publish(goal_pose)
            print("到达第三个点")
            img_flag = 3

    if f==3 :
        if img_flag == 3:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #F点外
            goal_pose.pose.position.x = -2.473
            goal_pose.pose.position.y = -2.190
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.727
            goal_pose.pose.orientation.w = 0.687
            goal_pub.publish(goal_pose)
            print("到达第四个点，拿急救包")
            img_flag = 4

    if f==4:
        if img_flag == 4:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #F点外
            goal_pose.pose.position.x = 0
            goal_pose.pose.position.y = 0
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0
            goal_pose.pose.orientation.w = 0
            goal_pub.publish(goal_pose)
            print("开始循环发布图像")
            img_flag = 5

        img_pub.publish(Img_publish)
        if num_terror == 1:
            if(get_spontoon == 1):
                room_sound()
        elif num_terror == 2:
            if(get_armor == 1):
                room_sound()
        elif num_terror == 3:
            if(get_bomb == 1):
                room_sound()

    if f==7:
        if img_flag == 7:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #终点
            goal_pose.pose.position.x = 2.118
            goal_pose.pose.position.y = 0.206 
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.693
            goal_pose.pose.orientation.w = 0.721
            goal_pub.publish(goal_pose)
            print("回到终点")
            img_flag = 8
            
    else:
        pass

def goal_callback(msg):
    #更新小车位置信息
    global f,img_pub,Img_publish,img_flag,first_image
    
    if msg.status.status == 3:    
        if f==0 or f==2 or f==7:  
            f+=1
        elif f==3:
            room_sound()
            f+=1

        elif f==4:
            f+=1

        else: 
            img_pub.publish(Img_publish)
            room_sound()
            f+=1



def boxes_callback(msg):
    global f,img_flag,Img_publish,first_image,first_image,goal_pose
    print("[ boxes_callback ]进入boxes_callback")

    if f==1:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        room_class(slist)
        print("[ boxes_callback ]恐怖分子已识别完成,前往下一个点")


    if f==3: 
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        room_class(slist)
        print("[ boxes_callback ]已经取到急救包,前往下一个点")
        

    if f==4: 
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        room_class(slist)
        print("[ boxes_callback ]已经取到武器,前往下一个点")
        



if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber("/image_result",BoundingBoxes,boxes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    rospy.spin()    

