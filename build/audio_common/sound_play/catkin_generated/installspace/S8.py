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

## 0719更新 保守跑法见图 8张图 后F区
## 看B点对角左（正对1张），看C点对角右（正对1张），F区内拍对角左

receive_flag=0
f=0
img_flag=0
img_num=0
first_image=0
b_room=[0]
c_room=[0]
d_room=[0]
e_room=[0]
f_room=[0]       #1=="corn",2=="cucumber",3=="watermelo"
error_image_num=0
Img_publish=Image()
soundhandle = SoundClient()
run_flag=0
turn_flag=0
count_num=[0,0,0,0] #"corn","cucumber","rice","wheat"
                    #room[0]=1 == "corn" 
                    #room[0]=2 == "cucumber" 
                    #room[0]=3 == "rice" 
                    #room[0]=4 == "wheat" 
f_count=[0,0,0]     #"corn","cucumber","watermelo"
sound_B=0
sound_C=0
sound_D=0
sound_E=0
sound_F=0
skip_B=0
skip_C=0
skip_D=0
skip_E=0

def room_class(rlist):
    global count_num,f_count,f
    max_index=0
    count_num=[0,0,0,0]  #重新清0
    f_count=[0,0,0]            #重新清0
    msg=flat(rlist)
    if f>=6:  #F房间找到最多数量果实
        if 'corn1' in msg:
            f_count[0]+=2 
        if 'corn2' in msg:
            f_count[0]+=2
        if 'corn3' in msg:
            f_count[0]+=1
        if 'corn4' in msg:
            f_count[0]+=1
        if 'cucumber1' in msg:
            f_count[1]+=1
        if 'cucumber2' in msg:
            f_count[1]+=3
        if 'cucumber3' in msg:
            f_count[1]+=2
        if 'cucumber4' in msg:
            f_count[1]+=2
        f_count[2]=msg.count('watermelo')

        max_index=f_count.index(max(f_count)) #找到最大值的位置
        rlist[0]=max_index+1      #1=="corn",2=="cucumber",3=="watermelo"
        #print("f_count:")
        #print(f_count)
    else:
        #B,C,D,E房间
        count_num[0]=msg.count('corn')
        count_num[1]=msg.count('cucumber')
        count_num[2]=msg.count('rice')
        count_num[3]=msg.count('wheat')

        #print("\n count_num:")
        #print(count_num)
        #print("\n")

        if(max(count_num))>=1: 
            #print("\n end_count_num:")
            #print(count_num)
            #print("\n")
            max_index=count_num.index(max(count_num)) #找到最大值的位置
            rlist[0]=max_index+1   #1=="corn" 2=="cucumber" 3=="rice" 4=="wheat" '

    print("\n [ room_class ]after_msg:")
    print(msg)
    print("\n")

def flat(a):
    l= []
    for i in a:
        if type(i) is list:
            for j in i:
                l.append(j)
        else:
            l.append(i)
    return(l)

def room_sound():
    global  b_room,c_room,d_room,e_room,f_room,sound_B,sound_C,sound_D,sound_E,sound_F,f_count
    argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"空录音"+'.mp3'
    soundhandle.playWave(argv)      
    time.sleep(1.5)  
    argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"任务完成"+'.mp3'
    soundhandle.playWave(argv) 
    time.sleep(2)    
    argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"B区域种植的作物为"+'.mp3'
    soundhandle.playWave(argv) 
    time.sleep(2)
    sound_B = 1
    if sound_B == 1:
        if b_room[0] == 1:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"玉米"+'.mp3'
            soundhandle.playWave(argv) 
        elif b_room[0] == 2:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"黄瓜"+'.mp3'
            soundhandle.playWave(argv) 
        elif b_room[0] == 3:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"水稻"+'.mp3'
            soundhandle.playWave(argv) 
        elif b_room[0] == 4:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"小麦"+'.mp3'
            soundhandle.playWave(argv) 
        sound_C = 1
        time.sleep(1)

    if sound_C == 1:
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"C区域种植的作物为"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(2)
        if c_room[0] == 1:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"玉米"+'.mp3'
            soundhandle.playWave(argv)
        elif c_room[0] == 2:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"黄瓜"+'.mp3'
            soundhandle.playWave(argv) 
        elif c_room[0] == 3:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"水稻"+'.mp3'
            soundhandle.playWave(argv)
        elif c_room[0] == 4:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"小麦"+'.mp3'
            soundhandle.playWave(argv)
        sound_D = 1
        time.sleep(1) 

    if sound_D == 1:
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"D区域种植的作物为"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(2)
        if d_room[0] == 1:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"玉米"+'.mp3'
            soundhandle.playWave(argv) 
        elif d_room[0] == 2:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"黄瓜"+'.mp3'
            soundhandle.playWave(argv)
        elif d_room[0] == 3:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"水稻"+'.mp3'
            soundhandle.playWave(argv)
        elif d_room[0] == 4:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"小麦"+'.mp3'
            soundhandle.playWave(argv)
        sound_E = 1
        time.sleep(1) 
            
    if sound_E == 1:
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"E区域种植的作物为"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(2)
        if e_room[0] == 1:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"玉米"+'.mp3'
            soundhandle.playWave(argv) 
        elif e_room[0] == 2:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"黄瓜"+'.mp3'
            soundhandle.playWave(argv)
        elif e_room[0] == 3:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"水稻"+'.mp3'
            soundhandle.playWave(argv)
        elif e_room[0] == 4:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"小麦"+'.mp3'
            soundhandle.playWave(argv)
        sound_F = 1
        time.sleep(1) 

    if sound_F == 1:
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"F区域存放的果实为"+'.mp3'
        soundhandle.playWave(argv) 
        time.sleep(2)
        if f_room[0] == 1:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"玉米"+'.mp3'
            soundhandle.playWave(argv) 
        elif f_room[0] == 2:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"黄瓜"+'.mp3'
            soundhandle.playWave(argv)
        elif f_room[0] == 3:
            argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"西瓜"+'.mp3'
            soundhandle.playWave(argv)
        time.sleep(1)
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+"数量为"+'.mp3'
        soundhandle.playWave(argv)    
        time.sleep(1)            
        argv = '/home/ucar/ucar_wssd/src/audio_common/mp3/'+str(max(f_count))+'.mp3'
        soundhandle.playWave(argv)     




def turning():
    global Img_publish,img_pub,img_num,run_flag,turn_flag,f_room
    base_driver_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate=rospy.Rate(100)
    if f==4:    #F房间
        for i in range(1):
            a=0
            if turn_flag==0:
                print("[ turning ]F外第%d次开转！！！"%(i+1))
                while (not rospy.is_shutdown()) and a<70:    #50大概是90度  
                    vel=Twist()
                    vel.linear.x=0.0
                    vel.linear.y=0.0
                    vel.linear.z=0.0
                    vel.angular.x=0.0
                    vel.angular.y=0.0
                    vel.angular.z=5.0
                    base_driver_pub.publish(vel)
                    a=a+1
                    rate.sleep()
                rospy.sleep(0.6)
                img_pub.publish(Img_publish)
                img_num=img_num+1
                print ('[ turning ]第%d张图片发布——F外'%(img_num))
        for i in range(1):
            a=0
            if turn_flag==0:
                print("[ turning ]F外第%d次开转！！！"%(i+1))
                while (not rospy.is_shutdown()) and a<47:    #50大概是90度  
                    vel=Twist()
                    vel.linear.x=0.0
                    vel.linear.y=0.0
                    vel.linear.z=0.0
                    vel.angular.x=0.0
                    vel.angular.y=0.0
                    vel.angular.z=5.0
                    base_driver_pub.publish(vel)
                    a=a+1
                    rate.sleep()
                rospy.sleep(0.6)
                img_pub.publish(Img_publish)
                img_num=img_num+1
                print ('[ turning ]第%d张图片发布——F外'%(img_num))


def img_callback(data):
    global f,img_flag,Img_publish,b_room,c_room,d_room,first_image,img_flag,img_num,first_image,goal_pose,skip_B,skip_C,skip_D,skip_E,f_count
    Img_publish=data

    if first_image<=150 and first_image>=0:
        first_image=1+first_image
        if first_image%10==0:
            print(first_image)
    else:
        if first_image >0:
            img_pub.publish(Img_publish)
            print("first image")
            first_image=-1

    if f==1 :
        if img_flag == 0 and skip_D == 0:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #C点对角右
            goal_pose.pose.position.x = 5.219
            goal_pose.pose.position.y = -1.418
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.710
            goal_pose.pose.orientation.w = 0.705
            goal_pub.publish(goal_pose)
        img_flag = 1

    if f==2 :
        if img_flag == 1 and skip_C == 0:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #B点对角左
            goal_pose.pose.position.x = 5.503
            goal_pose.pose.position.y = -3.108
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.669
            goal_pose.pose.orientation.w = 0.743
            goal_pub.publish(goal_pose)
        img_flag = 2
    
    if f==3 :
        if img_flag == 2 and skip_B == 0:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #E门口
            goal_pose.pose.position.x = 2.651
            goal_pose.pose.position.y = -0.264
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.328
            goal_pose.pose.orientation.w = 0.945
            goal_pub.publish(goal_pose)
        img_flag = 3

    if f==4 :
        if img_flag == 3 and skip_E == 0:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #F点外
            goal_pose.pose.position.x = 1.104
            goal_pose.pose.position.y = -2.267
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.677
            goal_pose.pose.orientation.w = 0.736
            goal_pub.publish(goal_pose)
        img_flag = 4

    if f==5 :
        if img_flag == 4:
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #F点内拍对角左
            goal_pose.pose.position.x = 2.069
            goal_pose.pose.position.y = -4.718
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.506
            goal_pose.pose.orientation.w = 0.863
            goal_pub.publish(goal_pose)
        img_flag = 5

    if f==6 :
        if img_flag == 5:
            img_flag = 6
            print("[ img_callback ]房间F已识别完成,前往终点")
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #终点
            goal_pose.pose.position.x = 0.051 #0.010
            goal_pose.pose.position.y = -0.010 #-0.020
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000 #0.716
            goal_pose.pose.orientation.w = -0.014 #0.698
            goal_pub.publish(goal_pose)

    elif f==7:
        room_class(f_room)  #F房间照片拍完后进行统计
        i=0
        if b_room[0]==0:
            for i in range(1,5):
                if c_room[0]!=i and d_room[0]!=i and e_room[0]!=i:
                    b_room[0]=i
        if c_room[0]==0:
            for i in range(1,5):
                if b_room[0]!=i and d_room[0]!=i and e_room[0]!=i:
                    c_room[0]=i
        if d_room[0]==0:
            for i in range(1,5):
                if b_room[0]!=i and c_room[0]!=i and e_room[0]!=i:
                    d_room[0]=i
        if e_room[0]==0:
            for i in range(1,5):
                if b_room[0]!=i and c_room[0]!=i and d_room[0]!=i:
                    e_room[0]=i
        print('B房间识别情况')
        print(b_room)
        print('C房间识别情况')
        print(c_room)
        print('D房间识别情况')
        print(d_room)
        print('E房间识别情况')
        print(e_room)
        print('F房间识别情况')
        print(f_room)
        print('数量为：%d'%max(f_count))          
        room_sound()
        print ('到达终点')
        f=f+1
    else:
        pass

def boxes_callback(msg):
    global seq,b_room,c_room,d_room,e_room,f_room,f,img_flag,error_image_num,goal_pose,error_image_num,turn_flag,receive_flag,skip_B,skip_C,skip_D,skip_E,img_num
    print("[ boxes_callback ]进入boxes_callback")
    seq=msg.image_header.seq+error_image_num-1 #加上该变量已修正跳过检查的图片数目

    if seq==1 and receive_flag==0:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        d_room.append(slist)
        room_class(d_room)
        # if d_room[0]!=0 and img_flag==0: #D点
        #     skip_D=1
        #     goal_pose = PoseStamped()
        #     goal_pose.header.frame_id = "map" #C点对角右
        #     goal_pose.pose.position.x = 5.219
        #     goal_pose.pose.position.y = -1.418
        #     goal_pose.pose.position.z = 0.000
        #     goal_pose.pose.orientation.x = 0
        #     goal_pose.pose.orientation.y = 0
        #     goal_pose.pose.orientation.z = 0.710
        #     goal_pose.pose.orientation.w = 0.705
        #     goal_pub.publish(goal_pose)
        #     f=0
        #     img_flag=0
        #     receive_flag=1
        #     turn_flag=1
        #     error_image_num+=1-img_num-error_image_num
        print("[ boxes_callback ]房间D已识别完成,前往房间C")
        print(d_room)

    if seq==2 and receive_flag==0:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        c_room.append(slist)
        room_class(c_room)
        # if c_room[0]!=0 and img_flag==1: #C点对角右
        #     skip_C=1
        #     goal_pose = PoseStamped()
        #     goal_pose.header.frame_id = "map" #B点对角左
        #     goal_pose.pose.position.x = 5.503
        #     goal_pose.pose.position.y = -3.108
        #     goal_pose.pose.position.z = 0.000
        #     goal_pose.pose.orientation.x = 0
        #     goal_pose.pose.orientation.y = 0
        #     goal_pose.pose.orientation.z = -0.669
        #     goal_pose.pose.orientation.w = 0.743
        #     goal_pub.publish(goal_pose)
        #     f=1
        #     img_flag=1
        #     receive_flag=1
        #     turn_flag=1
        #     error_image_num+=2-img_num-error_image_num
        print("[ boxes_callback ]房间C已识别完成,前往房间B")
        print(c_room)

    if seq==3 and receive_flag==0: #B点对角左
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        b_room.append(slist)
        room_class(b_room)
        # if b_room[0]!=0 and img_flag==2:
        #     skip_B=1
        #     goal_pose = PoseStamped()  
        #     goal_pose.header.frame_id = "map" #E点回头远固定板
        #     goal_pose.pose.position.x = 3.084
        #     goal_pose.pose.position.y = -0.549
        #     goal_pose.pose.position.z = 0.000
        #     goal_pose.pose.orientation.x = 0
        #     goal_pose.pose.orientation.y = 0
        #     goal_pose.pose.orientation.z = 0.591
        #     goal_pose.pose.orientation.w = 0.807
        #     goal_pub.publish(goal_pose)
        #     f=2
        #     img_flag=2
        #     receive_flag=1
        #     turn_flag=1
        #     error_image_num+=3-img_num-error_image_num
        print("[ boxes_callback ]房间B已识别完成,前往房间E点")
        print(b_room)

    if seq==4 and receive_flag==0: #E点回头远固定板
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        e_room.append(slist)
        room_class(e_room)
        # if e_room[0]!=0 and img_flag==3:
        #     skip_E=1
        #     goal_pose = PoseStamped()  
        #     goal_pose.header.frame_id = "map" #终点
        #     goal_pose.pose.position.x = 0.071 #0.010
        #     goal_pose.pose.position.y = -0.010 #-0.020
        #     goal_pose.pose.position.z = 0.000
        #     goal_pose.pose.orientation.x = 0
        #     goal_pose.pose.orientation.y = 0
        #     goal_pose.pose.orientation.z = 1.000 #0.716
        #     goal_pose.pose.orientation.w = -0.014 #0.698
        #     goal_pub.publish(goal_pose)
        #     f=3
        #     img_flag=3
        #     receive_flag=1
        #     turn_flag=1
        #     error_image_num+=4-img_num-error_image_num
        print("[ boxes_callback ]房间E已识别完成,前往房间F点")
        print(e_room)

    if seq>=5 and seq<=7 and receive_flag==0: #F点外三张照片
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        f_room.append(slist)
        img_flag=4

    if seq==8 and receive_flag==0: #F点内一张照片
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        f_room.append(slist)
        img_flag=5

def goal_callback(msg):
    #更新小车位置信息
    global f,img_num,img_pub,Img_publish,turn_flag,receive_flag,seq,error_image_num,img_flag
    print("\n[ goal_callback ]f = %d"%f)
    if msg.status.status == 3:    
        if f==6: #到达终点
            receive_flag=0
            f=f+1
        elif f<=5:
            receive_flag=0
            turn_flag=0
            if f==4:
                rospy.sleep(0.5)
            else:
                rospy.sleep(0.25)
            img_pub.publish(Img_publish)
            img_num=img_num+1
            print ('[ goal_callback ]第%d张图片发布——定点第一张'%(img_num))
            print("[ goal_callback ]seq = %d"%seq)
            print('[ goal_callback ]到达第%d个位置'%(f+1))
            receive_flag=0
            turning()
            #turn_flag=0
            f=f+1

            print('\n')
            print("[ goal_callback ]此轮回调结束f = %d"%f)
            print("[ goal_callback ]seq = %d"%seq)
            print("[ goal_callback ]error_image_num = %d"%(error_image_num))
            print('\n')

if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber("/image_result",BoundingBoxes,boxes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    rospy.spin()    

