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



f=0
img_flag=1
first_image=0
num_terror=0
room_1=[]  # for 恐怖分子
room_2=[]  # for 急救包
room_3=[]  # for 武器

get_weapon = 0
Img_publish=Image()
soundhandle = SoundClient()

is_terrorist = 0

def room_class(rlist):
    global f,num_terror,is_terrorist,get_weapon
    if f==1:  
        if 'terrorist_1' in rlist:
            num_terror=1
            is_terrorist = 1
        elif 'terrorist_2' in rlist:
            num_terror=2
            is_terrorist = 1
        elif 'terrorist_3' in rlist:
            num_terror=3
            is_terrorist = 1
        else:
            print("未识别到恐怖分子")
        print("恐怖分子的数量为：", num_terror)
    
    if f==3 or f==4 or f==5 or f==6 or f==7:
        if num_terror == 1:
            if 'spontoon' in rlist:
                get_weapon = 1

        if num_terror == 2:
            if 'armor' in rlist:
                get_weapon = 1

        if num_terror == 3:
            if 'bomb' in rlist:
                get_weapon = 1
    

def room_sound():
    global num_terror
    print("room_sound")
    if f==1:
        if num_terror== 1:
            argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"terrorist_1"+'.mp3'
            soundhandle.playWave(argv) 
         
        elif num_terror== 2:
            argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"terrorist_2"+'.mp3'
            soundhandle.playWave(argv)
    
        elif num_terror== 3:
            argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"terrorist_3"+'.mp3'
            soundhandle.playWave(argv) 
           
        
    if f == 2:
        argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"急救包"+'.mp3'
        soundhandle.playWave(argv) 
        

    if f==3 or f==4 or f==5 or f==6 or f==7:
        if num_terror== 1:
            argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"警棍"+'.mp3'
            soundhandle.playWave(argv) 
            
        elif num_terror== 2:
            argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"防弹衣"+'.mp3'
            soundhandle.playWave(argv) 
            
        elif num_terror== 3:
            argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"催泪瓦斯"+'.mp3'
            soundhandle.playWave(argv)
           
            
    if f == 9:
        argv = '/home/ucar/ucar_5/src/audio_common/mp3/'+"结束"+'.mp3'
        soundhandle.playWave(argv) 
  



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
            goal_pose.pose.position.x = 0.922
            goal_pose.pose.position.y = 1.452
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.026
            goal_pose.pose.orientation.w = 1.000
            goal_pub.publish(goal_pose)
            print("到达第一个点,开始识别恐怖分子")
            img_flag = 2
    
    if f==2 :
        if img_flag == 2:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #原点
            goal_pose.pose.position.x = -2.427
            goal_pose.pose.position.y = -2.117
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.689
            goal_pose.pose.orientation.w = 0.725
            goal_pub.publish(goal_pose)
            print("到达第二个点，开始取急救包")
            img_flag = 3

    if f==3 :
        if img_flag == 3:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #F点外
            goal_pose.pose.position.x = -2.347
            goal_pose.pose.position.y = 0.597
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1
            goal_pose.pose.orientation.w = 0.020
            goal_pub.publish(goal_pose)
            print("到达第三个点")
            img_flag = 4

    if f==4 :
        if img_flag == 4:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = -2.259
            goal_pose.pose.position.y = 1.056
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.924
            goal_pose.pose.orientation.w = 0.382
            goal_pub.publish(goal_pose)
            print("到达第四个点")
            img_flag = 5

    if f==5 :
        if img_flag == 5:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = -1.825
            goal_pose.pose.position.y = 0.967
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.721
            goal_pose.pose.orientation.w = 0.693
            goal_pub.publish(goal_pose)
            print("到达第五个点")
            img_flag = 6

    if f==6 :
        if img_flag == 6:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = -1.397
            goal_pose.pose.position.y = 1.210
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.343
            goal_pose.pose.orientation.w = 0.939
            goal_pub.publish(goal_pose)
            print("到达第六个点")
            img_flag = 7

    if f==7:
        if img_flag == 7:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" 
            goal_pose.pose.position.x = -1.237
            goal_pose.pose.position.y = 0.880
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.005
            goal_pose.pose.orientation.w = 1
            goal_pub.publish(goal_pose)
            print("到达第七个点")
            img_flag = 8
            
    if f==8:
        if img_flag == 8:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" 
            goal_pose.pose.position.x = 0
            goal_pose.pose.position.y = 0
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0
            goal_pose.pose.orientation.w = 1
            goal_pub.publish(goal_pose)
            print("正在前往第八个点")
            img_flag = 9
    
    if f==9:
        if img_flag == 9:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #终点
            goal_pose.pose.position.x = 2.045
            goal_pose.pose.position.y = 0.150
            goal_pose.pose.position.z = 0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.700
            goal_pose.pose.orientation.w = 0.715
            goal_pub.publish(goal_pose)
            print("正在前往终点")
            img_flag = 10
        
    else:
        pass

def goal_callback(msg):
    #更新小车位置信息
    global f,img_pub,Img_publish,img_flag,first_image,get_weapon
    
    if msg.status.status == 3:
        rospy.sleep(0.5)    
        
        if f == 0:
            f+=1
        elif f == 1:
            img_pub.publish(Img_publish)
            rospy.sleep(0.3)
            if(is_terrorist == 1):
                room_sound()
                f+=1
        elif f == 2:
                room_sound()
                f+=1
                
        elif f==7 or f == 8:
            f+=1
            
        elif f == 9:
            room_sound()
            
        else :#34567
            img_pub.publish(Img_publish)
            rospy.sleep(0.3)
            if(get_weapon == 1):
                room_sound()
                f=8
                img_flag = 8
            else:
                f+=1

def boxes_callback(msg):
    global f,img_flag,Img_publish,first_image,first_image,goal_pose,is_terrorist
    print("[ boxes_callback ]进入boxes_callback")

    if f==1:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        room_class(slist)
        if is_terrorist == 1:
            print("[ boxes_callback ]恐怖分子已识别完成")

    if f==3 or f==4 or f==5 or f==6 or f==7: 
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        room_class(slist)
        
if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber("/image_result",BoundingBoxes,boxes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    rospy.spin()    

