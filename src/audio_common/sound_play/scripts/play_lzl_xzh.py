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


receive_flag=0
f=0
img_flag=0
img_num=0
first_image=0
fang="b1c2d3"
b_room=[0]
c_room=[0]
d_room=[0]
error_image_num=0
Img_publish=Image()
soundhandle = SoundClient()
fang3=0
fang_bedding=0
fang_dinning=0
fang_living=0
run_flag=0
turn_flag=0


def room_class(msg):
    global fang_bedding,fang_living,fang_dinning
    room=str(msg)
    if "tableware" in room:
        msg[0]=1
        fang_dinning=1
    elif "food" in room:
        msg[0]=1
        fang_dinning=1
    elif "sofa" in room:
        msg[0]=3
        fang_living=1
    elif "television" in room:
        msg[0]=3
        fang_living=1
    elif "bed" in room:
        msg[0]=2
        fang_bedding=1
    elif ("person" in room) and ("pet" in room) and ("table_chair" in room):
        msg[0]=2
        fang_bedding=1
    elif ("person" in room) and ("pet" in room):
        msg[0]=2
        fang_bedding=1


#    elif fang_dinning==1 and ("person" in room):
#        msg[0]=2
#        fang_bedding=1       
#    elif fang_bedding==1 and ("person" in room):
#        msg[0]=1
#        fang_dinning=1
#    elif fang_bedding==1 and ("pet" in room):
#        msg[0]=3
#        fang_living=1
#    elif fang_living==1 and ("pet" in room):
#        msg[0]=2
#        fang_bedding=1
    print(msg)




def room_sound():
    global  fang,b_room,c_room,d_room
    if  b_room[0]==1 and c_room[0]==1 and  d_room[0]==1:
        fang ="b1c1d1"
    elif  b_room[0]==1 and c_room[0]==1 and d_room[0]==2:
        fang ="b1c1d2"
    elif  b_room[0]==1 and c_room[0]==1 and d_room[0]==3:
        fang ="b1c1d3"
    elif  b_room[0]==1 and c_room[0]==2 and d_room[0]==1:
        fang ="b1c2d1"
    elif  b_room[0]==1 and c_room[0]==2 and d_room[0]==2:
        fang ="b1c2d2"
    elif  b_room[0]==1 and c_room[0]==2 and d_room[0]==3:
        fang ="b1c2d3"
    elif  b_room[0]==1 and c_room[0]==3 and d_room[0]==1:
        fang ="b1c3d1"
    elif  b_room[0]==1 and c_room[0]==3 and d_room[0]==2:
        fang ="b1c3d2"
    elif  b_room[0]==1 and c_room[0]==3 and d_room[0]==3:
        fang ="b1c3d3"
    elif  b_room[0]==2 and c_room[0]==1 and  d_room[0]==1:
        fang ="b2c1d1"
    elif  b_room[0]==2 and c_room[0]==1 and d_room[0]==2:
        fang ="b2c1d2"
    elif  b_room[0]==2 and c_room[0]==1 and d_room[0]==3:
        fang ="b2c1d3"
    elif  b_room[0]==2 and c_room[0]==2 and d_room[0]==1:
        fang ="b2c2d1"
    elif  b_room[0]==2 and c_room[0]==2 and d_room[0]==2:
        fang ="b2c2d2"
    elif  b_room[0]==2 and c_room[0]==2 and d_room[0]==3:
        fang ="b2c2d3"
    elif  b_room[0]==2 and c_room[0]==3 and d_room[0]==1:
        fang ="b2c3d1"
    elif  b_room[0]==2 and c_room[0]==3 and d_room[0]==2:
        fang ="b2c3d2"
    elif  b_room[0]==2 and c_room[0]==3 and d_room[0]==3:
        fang ="b2c3d3"
    elif  b_room[0]==3 and c_room[0]==1 and  d_room[0]==1:
        fang ="b3c1d1"
    elif  b_room[0]==3 and c_room[0]==1 and d_room[0]==2:
        fang ="b3c1d2"
    elif  b_room[0]==3 and c_room[0]==1 and d_room[0]==3:
        fang ="b3c1d3"
    elif  b_room[0]==3 and c_room[0]==2 and d_room[0]==1:
        fang ="b3c2d1"
    elif  b_room[0]==3 and c_room[0]==2 and d_room[0]==2:
        fang ="b3c2d2"
    elif  b_room[0]==3 and c_room[0]==2 and d_room[0]==3:
        fang ="b3c2d3"
    elif  b_room[0]==3 and c_room[0]==3 and d_room[0]==1:
        fang ="b3c3d1"
    elif  b_room[0]==3 and c_room[0]==3 and d_room[0]==2:
        fang ="b3c3d2"
    elif  b_room[0]==3 and c_room[0]==3 and d_room[0]==3:
        fang ="b3c3d3"
    elif (b_room[0]==1 and c_room[0]==2) or (b_room[0]==1 and d_room[0]==3) or (c_room[0]==2 and d_room[0]==3):
        fang ="b1c2d3"
    elif (b_room[0]==1 and c_room[0]==3) or (b_room[0]==1 and d_room[0]==2) or (c_room[0]==3 and d_room[0]==2):
        fang ="b1c3d2"
    elif (b_room[0]==2 and c_room[0]==1) or (b_room[0]==2 and d_room[0]==3) or (c_room[0]==1 and d_room[0]==3):
        fang ="b2c1d3"
    elif (b_room[0]==2 and c_room[0]==3) or (b_room[0]==2 and d_room[0]==1) or (c_room[0]==3 and d_room[0]==1):
        fang ="b2c3d1"
    elif (b_room[0]==3 and c_room[0]==2) or (b_room[0]==3 and d_room[0]==1) or (c_room[0]==2 and d_room[0]==1):
        fang ="b3c2d1"
    elif (b_room[0]==3 and c_room[0]==1) or (b_room[0]==3 and d_room[0]==2) or (c_room[0]==1 and d_room[0]==2):
        fang ="b3c1d2"
    elif b_room[0]==1:
        fang ="b1c2d3"
    elif c_room[0]==1:
        fang="b2c1d3"
    elif d_room[0]==1:
        fang ="b3c2d1"
    elif b_room[0]==2:
        fang ="b2c1d3"
    elif c_room[0]==2:
        fang="b1c2d3"
    elif d_room[0]==2:
        fang ="b3c1d2"
    elif b_room[0]==3:
        fang ="b3c2d1"
    elif c_room[0]==3:
        fang="b1c3d2"
    elif d_room[0]==3:
        fang ="b1c2d3"


def turning():
    global Img_publish,img_pub,img_num,run_flag,turn_flag
    base_driver_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate=rospy.Rate(100)
    if f==0:
        for i in range(1):
            a=0
            print("开转！！！")
            if turn_flag==0:
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
                rospy.sleep(0.7)
                img_pub.publish(Img_publish)
                img_num=img_num+1
                print ('第%d张图片发布'%(img_num))
            else:
                break
    
    if f==1:
        for i in range(2):
            a=0
            print("开转！！！")
            if turn_flag==0:
                while (not rospy.is_shutdown()) and a<60:    #50大概是90度  
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
                rospy.sleep(0.7)
                img_pub.publish(Img_publish)
                img_num=img_num+1
                print ('第%d张图片发布'%(img_num))
            else:
                break

    if f==2:
        for i in range(2):
            a=0
            print("开转！！！")
            if turn_flag==0:
                while (not rospy.is_shutdown()) and a<45:    #50大概是90度  
                    vel=Twist()
                    vel.linear.x=0.0
                    vel.linear.y=0.0
                    vel.linear.z=0.0
                    vel.angular.x=0.0
                    vel.angular.y=0.0
                    vel.angular.z=-5.0
                    base_driver_pub.publish(vel)
                    a=a+1
                    rate.sleep()
                rospy.sleep(0.7)
                img_pub.publish(Img_publish)
                img_num=img_num+1
                print ('第%d张图片发布'%(img_num))
            else:
                break



def img_callback(data):
    global f,img_flag,Img_publish,fang,b_room,c_room,d_room,first_image,fang_list,img_flag,img_num,first_image,goal_pose
    
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
        if img_flag == 0:
            img_flag = 1
            # Img_publish = data
            # img_pub.publish(Img_publish)
            # print ('第%d张图片发布'%(img_num))
            goal_pose = PoseStamped()                    #第二个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 3.032
            goal_pose.pose.position.y = -5.01
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.68
            goal_pose.pose.orientation.w = 0.72
            goal_pub.publish(goal_pose)

    elif f==2 :
        if img_flag == 1:
            img_flag = 2
            goal_pose = PoseStamped()          #第三个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 0.99
            goal_pose.pose.position.y = -4.05
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.42
            goal_pose.pose.orientation.w = 0.90
            goal_pub.publish(goal_pose)

    elif f==3 :
        if img_flag == 2:
            img_flag = 3
            goal_pose = PoseStamped()               #终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.10
            goal_pose.pose.position.y = -0.950
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.000
            goal_pub.publish(goal_pose)

    elif f==4:

        print('B房间识别情况')
        print(b_room)
        print('C房间识别情况')
        print(c_room)
        print('D房间识别情况')
        print(d_room)
        room_sound()
        print(fang)
        argv = '/home/ucar/ucar_ws/src/audio_common/mp3/'+fang+'.mp3'
        soundhandle.playWave(argv) 
        # os.system("ffplay "+argv)
        print ('到达终点')
        f=f+1
    else:
        pass

def boxes_callback(msg):
    global seq,b_room,c_room,d_room,f,img_flag,error_image_num,fang3,fang33,flag_3,goal_pose,error_image_num,run_flag,turn_flag,receive_flag
    seq=msg.image_header.seq+error_image_num      #加上该变量已修正跳过检查的图片数目
    if seq>=2 and seq<=3 and receive_flag==0:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        b_room.append(slist)
        room_class(b_room)
        if b_room[0]!=0:
            goal_pose = PoseStamped()                    #第二个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 3.032
            goal_pose.pose.position.y = -5.01
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.68
            goal_pose.pose.orientation.w = 0.72
            goal_pub.publish(goal_pose)
            f=0
            img_flag=0
            turn_flag=1
            receive_flag=1
            error_image_num+=3-seq
            print("房间b已识别完成,前往房间c")
            print(b_room)
            run_flag=1

    if seq>=4 and seq<=6 and receive_flag==0:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        c_room.append(slist)
        room_class(c_room)      
        if c_room[0]!=0 and fang3==0:
            goal_pose = PoseStamped()               #第三个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 0.99
            goal_pose.pose.position.y = -4.05
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.42
            goal_pose.pose.orientation.w = 0.90
            goal_pub.publish(goal_pose)
            f=1
            img_flag=1
            turn_flag=1
            receive_flag=1
            error_image_num+=6-seq
            print("房间c已识别完成,前往房间d")
            print(c_room)
            run_flag=1

    if seq>=7 and seq<=9 and receive_flag==0:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        d_room.append(slist)
        room_class(d_room)
        if d_room[0]!=0:
            goal_pose = PoseStamped()               #终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.10
            goal_pose.pose.position.y = -0.950
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.017
            goal_pub.publish(goal_pose)
            f=2
            img_flag=2
            receive_flag=1
            turn_flag=1
            error_image_num+=9-seq
            print("房间d已识别完成,前往终点")
            print(d_room)
            run_flag=1


def goal_callback(msg):
    #更新小车位置信息
    global f,img_num,img_pub,Img_publish,turn_flag,receive_flag
    print("fffffffffffff")
    print(f)
    if msg.status.status == 3:    

        if f==3:
            receive_flag=0
            f=f+1

        if f<=2:
            receive_flag=0
            rospy.sleep(0.7)
            img_pub.publish(Img_publish)
            img_num=img_num+1
            print ('第%d张图片发布'%(img_num))
            print('到达第%d个位置'%(f+1))

            receive_flag=0
            turning()
            turn_flag=0
            f=f+1







if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber("/image_result",BoundingBoxes,boxes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    rospy.spin()    
