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

flag_3=0
f=0
img_flag=0
seq=-1
error_image_num=0#这里定义一个图像数目误差的变量，因为如果使用了快捷的图像识别，那么会使得在部分房间识别的图像数目不足三张，这样会使得在boxes_callback回调函数中图片和房间对应错误，因此加上一个error_image_num来修正减少的图片数目
first_image=0
fang="0"
b_room=[0]
c_room=[0]
d_room=[0]
Img_publish=Image()
soundhandle = SoundClient()


def room_class(msg):
    room=str(msg)
    if "tableware" in room:
        msg[0]=1
    elif "food" in room:
        msg[0]=1
    elif "bed" in room:
        msg[0]=2
    elif "sofa" in room:
        msg[0]=3
    elif "television" in room:
        msg[0]=3
    elif ("person" in room) and ("pet" in room) and ("table_chair" in room):
        msg[0]=2
    elif ("person" in room) and ("pet" in room):
        msg[0]=2
    print(msg)

def room_sound():
    global  fang,b_room,c_room,d_room
    if (b_room[0]==1 and c_room[0]==2) or (b_room[0]==1 and d_room[0]==3) or (c_room[0]==2 and d_room[0]==3):
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

def boxes_callback(msg):
    global seq,b_room,c_room,d_room,f,img_flag,error_image_num
    seq=msg.image_header.seq+error_image_num      #加上该变量已修正跳过检查的图片数目
    if seq>=2 and seq<=5:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        b_room.append(slist)
        room_class(b_room)
        if b_room[0]!=0:
            goal_pose = PoseStamped()                    #第二个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.994
            goal_pose.pose.position.y = -4.303
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.000
            goal_pose.pose.orientation.w = -1.000
            goal_pub.publish(goal_pose)
            f=4
            img_flag=4
            error_image_num+=5-seq
            print("房间b已识别完成,前往房间c")

    if seq>=6 and seq<=9:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        c_room.append(slist)
        room_class(c_room)
        if c_room[0]!=0 and b_room[0]!=0:
            goal_pose = PoseStamped()               #第三个房间门口
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.701
            goal_pose.pose.position.y = -2.589
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.677
            goal_pose.pose.orientation.w = 0.736
            goal_pub.publish(goal_pose)
            f=11
            img_flag=11
            flag_3=1
            print("前往房间d门口,跳过房间d的识别")          
        elif c_room[0]!=0:
            goal_pose = PoseStamped()               #第三个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.018
            goal_pose.pose.position.y = -3.855
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.700
            goal_pose.pose.orientation.w = 0.700
            goal_pub.publish(goal_pose)
            f=8
            img_flag=8
            error_image_num+=9-seq
            print("房间c已识别完成,前往房间d")

    if seq>=10 and seq<=13:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        d_room.append(slist)
        room_class(d_room)
        if d_room[0]!=0:
            goal_pose = PoseStamped()               #终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.100
            goal_pose.pose.position.y = -0.950
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.017
            goal_pub.publish(goal_pose)
            f=12
            img_flag=12
            error_image_num+=13-seq
            print("房间d已识别完成,前往终点")


def img_callback(data):
    global f,img_flag,Img_publish,fang,b_room,c_room,d_room,first_image

    if first_image<=150 and first_image>=0:
        first_image=1+first_image
        if first_image%10==0:
            print(first_image)
    else:
        if first_image >0:
            Img_publish = data
            img_pub.publish(Img_publish)
            print("first image")
            first_image=-1

    if f==1 :
        if img_flag == 0:
            img_flag = 1
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()                    #第一个房间的第二个方向（第一个房间的第一个方向的设置在语言启动功能包内）
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 4.711
            goal_pose.pose.position.y = -4.000
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.707
            goal_pose.pose.orientation.w = 0.707
            goal_pub.publish(goal_pose)

    elif f==2 :
        if img_flag == 1:
            img_flag = 2
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()                    #第一个房间第三个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 4.711
            goal_pose.pose.position.y = -4.000
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = 0.000
            goal_pub.publish(goal_pose)

    elif f==3 :
        if img_flag == 2:
            img_flag = 3
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()                    #第一个房间第四个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 4.711
            goal_pose.pose.position.y = -4.000
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  0.707
            goal_pose.pose.orientation.w = 0.707
            goal_pub.publish(goal_pose)

    elif f==4 :
        if img_flag == 3:
            img_flag = 4
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
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

    elif f==5 :
        if img_flag == 4:
            img_flag = 5
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #第二个房间第二个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.994
            goal_pose.pose.position.y = -4.303
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.000
            goal_pose.pose.orientation.w = -1.000
            goal_pub.publish(goal_pose)

    elif f==6 :
        if img_flag == 5:
            img_flag = 6
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #第二个房间第三个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.994
            goal_pose.pose.position.y = -4.303
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = 0.000
            goal_pub.publish(goal_pose)

    elif f==7 :
        if img_flag == 6:
            img_flag = 7
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #第二个房间第四个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.994
            goal_pose.pose.position.y = -4.303
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  0.707
            goal_pose.pose.orientation.w = 0.707
            goal_pub.publish(goal_pose)

    elif f==8 :
        if img_flag == 7:
            img_flag = 8
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #第三个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.018
            goal_pose.pose.position.y = -3.855
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.707
            goal_pose.pose.orientation.w = 0.707
            goal_pub.publish(goal_pose)

    elif f==9 :
        if img_flag == 8:
            img_flag = 9
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #第三个房间第二个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.018
            goal_pose.pose.position.y = -3.855
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = 0.000
            goal_pub.publish(goal_pose)

    elif f==10 :
        if img_flag == 9:
            img_flag = 10
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #第三个房间第三个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.018
            goal_pose.pose.position.y = -3.855
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.000
            goal_pose.pose.orientation.w = -1.000
            goal_pub.publish(goal_pose)

    elif f==11 :
        if img_flag == 10:
            img_flag = 11
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #第三个房间第四个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.018
            goal_pose.pose.position.y = -3.855
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  0.700
            goal_pose.pose.orientation.w = 0.700
            goal_pub.publish(goal_pose)

    elif f==12 and flag_3==1:
        if img_flag == 11:
            goal_pose = PoseStamped()               #直接前往终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.050
            goal_pose.pose.position.y = -0.900
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.000
            goal_pub.publish(goal_pose)

    elif f==12 :
        if img_flag == 11:
            img_flag = 12
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.030
            goal_pose.pose.position.y = -0.950
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.000
            goal_pub.publish(goal_pose)


    elif f==13:
        if img_flag == 12:
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
            print ('到达终点')
            f=f+1
    else:
        pass




def goal_callback(msg):
    #更新小车位置信息
    global f
    if msg.status.status == 3:       
        if f <13:
            rospy.sleep(1.0)
            f+=1
    print('到达第%d个位置'%(f))        


if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber("/image_result",BoundingBoxes,boxes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    rospy.spin()    
