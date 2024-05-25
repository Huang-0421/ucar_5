#!/usr/bin/env python
#_*_coding: UTF-8 _*_
import rospy#导入了ROS的Python客户端库
from std_msgs.msg import String#从std_msgs包中导入String消息类型。这是ROS中的标准消息类型之一，用于发布和订阅纯文本字符串。
from sound_play.msg import SoundRequest#导入sound_play包中的SoundRequest消息。这用于与sound_play节点通信，该节点可以播放声音。
from sound_play.libsoundplay import SoundClient#从sound_play包中导入SoundClient类。这个类提供了一个Python接口，用于播放声音和语音文本。
from darknet_ros_msgs.msg import classes#导入darknet_ros_msgs包中的classes消息。这很可能是自定义消息类型，用于从Darknet ROS包（执行YOLO对象识别）接收分类信息。
from darknet_ros_msgs.msg import BoundingBoxes#导入darknet_ros_msgs包中的BoundingBoxes消息。这也是Darknet ROS相关的消息类型，通常用于传递检测到的对象及其边界框信息。
from move_base_msgs.msg import MoveBaseActionResult#从move_base_msgs包中导入MoveBaseActionResult消息类型。这与ROS的导航堆栈有关，用于获取移动基地操作的结果。
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped,Twist#导入geometry_msgs包中的几种消息类型。PoseStamped和PoseWithCovarianceStamped用于位置和方向的信息，Twist用于表示速度和角速度。
import numpy as np#导入NumPy库并缩写为np，这是Python中用于科学计算的常用库，特别是在数组和矩阵操作方面。
from sensor_msgs.msg import Image#导入sensor_msgs包中的Image消息类型。这是ROS中用于处理图像信息的标准消息类型。
from cv_bridge import CvBridge, CvBridgeError#导入cv_bridge模块，它提供了一个接口，将ROS中的图像消息类型转换为OpenCV图像格式，从而可以使用OpenCV库进行图像处理。
import cv2#导入OpenCV库，这是用于计算机视觉任务的主要库。
from actionlib_msgs.msg import GoalStatusArray#导入actionlib_msgs包中的GoalStatusArray消息类型。这用于与action服务器通信，获取有关目标状态的信息。
from  math import pi#从math模块中导入pi常量，这个常量代表了圆周率π的值。
import  os#导入Python的os模块，这个模块提供了许多函数来与操作系统交互。
import time#导入Python的time模块，这个模块提供了时间相关的函数。
import cv_bridge
from tf import TransformListener
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import PoseArray, PoseStamped, Quaternion
from sensor_msgs.msg import LaserScan
import math
## 0719更新 保守跑法见图 8张图 后F区
## B、C点均从里看向外，F区内拍对角右

terroist_flag=0
terroist_num=0
terrorist_class=""
get_list=["spontoon","bulletproof","teargas"]
aid_kit_flag=0
get_is_flag=0
twist = Twist()

#进入巡线标志位   (第四个点标志位)
goal_pose2 = PoseStamped() 
line_flag=0
#巡线变量
Kp = 0.0018
Ki = 0.000000
Kd = 0.0000000
sum_pid = 0
d_pid = 0
latter_pid = 0
num_stop=0
argv2="video_path"

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
num_terror=[0]#恐怖分子数量
aid_kit=[0]#急救包种类
count_num=[0,0,0,0] #"corn","cucumber","rice","wheat"
                    #room[0]=1 == "corn" 
                    #room[0]=2 == "cucumber" 
                    #room[0]=3 == "rice" 
                    #room[0]=4 == "wheat" 
f_count=[0,0,0,0,0]     #"terrorist", "aid kit", "truncheon", "bulletproof_vest", "tear gas"
sound_C=0
sound_D=0
sound_E=0
sound_F=0
skip_B=0
skip_C=0
skip_D=0
skip_E=0
ll=[0,0,0]
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




def area(mask):
    num1=0
    h,w=mask.shape
    h=int(3*h/4)
    w=int(3*w/4)
    mask_area=h*w
    print("area:",mask_area)
    for i in range(h):
        for j in range(w):
            if mask[i][j]!=0:
                num1=num1+1
    print("num1",num1)
    rate=num1*100/mask_area 
    return  rate
def mid(follow, mask):
    halfWidth = follow.shape[1] // 2 #图片一半的宽度
    half = halfWidth  

    # 从下往上扫描赛道,最下端取图片中线为分割线
    for y in range(follow.shape[0]-1 , -1 , -1):
        # follow.shape[0]为图像行数，图像最上面为0行，follow.shape[0]-1表示最后一行
        # -1是循环终止条件，到0后停止，第二个-1为步长，每次减少一行
        
        # V2改动:加入分割线左右各半张图片的宽度作为约束,减小邻近赛道的干扰
        if (mask[y][max(0, half - halfWidth):half] == np.zeros_like(
                mask[y][max(0, half - halfWidth):half])).all():  # 分割线左端无赛道
            left = max(0, half - halfWidth)  # 取图片左边界
        else:
            left = np.average(np.where(mask[y][0:half] == 255))  # 计算分割线左端平均位置
        if (mask[y][half:min(follow.shape[1], half + halfWidth)] == np.zeros_like(
                mask[y][half:min(follow.shape[1], half + halfWidth)])).all():  # 分割线右端无赛道
            right = min(follow.shape[1], half + halfWidth)  # 取图片右边界
        else:
            right = np.average(np.where(mask[y][half:follow.shape[1]] == 255)) + half  # 计算分割线右端平均位置

        mid = (left + right) // 2  # 计算拟合中点

        half = mid  # 递归,从下往上确定分割线
        follow[y, mid] = 255  # 画出拟合中线

        if y == 240:  # 设置指定提取中点的纵轴位置
            mid_output = mid
    cv2.circle(follow, (mid_output, 360), 5, 255, -1)  # opencv为(x,y),画出指定提取中点

    error = follow.shape[1] // 2 - mid_output  # 计算图片中点与指定提取中点的误差
    return mid_output # error为正数右转,为负数左转


def imagecallback2(msg):
    print("error")
    bridge = cv_bridge.CvBridge()
    image = bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
    image = cv2.flip(image,1)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([ 0,  0,  221])
    upper_yellow = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    cv2.imshow("mask",mask)
    follow = mask.copy()
    midoutput= mid(follow, mask)
    
    h, w, d = image.shape
    search_top = 3*h/4
    search_bot = search_top + 20
    mask[0:search_top, 0:w] = 0
    mask[search_bot:h, 0:w] = 0
   
    cy = 360
    cx=midoutput
        #cy=360
    cv2.circle(image, (cx, cy), 20, (0,0,255), -1)
    vtherror = cx - w/2
        #print cx,cy
    twist.linear.x =0.0152
    twist.angular.z = -float(vtherror) / 300 * 0.45 # 400: 0.1, 300: 0.15, 250, 0.2
    cmd_vel_pub.publish(twist)



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
            argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"恐怖分子数量1"+'.mp3'
            soundhandle.playWave(argv) 
         
        elif num_terror== 2:
            argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"恐怖分子数量2"+'.mp3'
            soundhandle.playWave(argv)
    
        elif num_terror== 3:
            argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"恐怖分子数量3"+'.mp3'
            soundhandle.playWave(argv) 
           
        
    if f == 2:
        argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"取到急救包"+'.mp3'
        soundhandle.playWave(argv) 
        

    if f==3 or f==4 or f==5 or f==6 or f==7:
        if num_terror== 1:
            argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"取到警棍"+'.mp3'
            soundhandle.playWave(argv) 
            
        elif num_terror== 2:
            argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"取到防弹衣"+'.mp3'
            soundhandle.playWave(argv) 
            
        elif num_terror== 3:
            argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"取到催泪瓦斯"+'.mp3'
            soundhandle.playWave(argv)
           
            
    if img_flag == 11:
        argv = '/home/ucar/ucar_9/src/audio_common/mp3/'+"结束"+'.mp3'
        soundhandle.playWave(argv) 





def turning():
    global Img_publish,img_pub,img_num,run_flag,turn_flag,f_room
    base_driver_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate=rospy.Rate(100)



def img_callback(data):
    global f,img_flag,Img_publish,first_image,img_flag,img_num,first_image,goal_pose,skip_B,skip_C,skip_D,skip_E,f_count,num_terror
    
    global twist,cmd_vel_pub,kp,Ki,Kd,latter_pid,d_pid,sum_pid,num_stop,area,argv2,line_flag,get_is_flag,terrorist_class
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
    if f==9 :
        if img_flag == 9:
            print("[ img_callback ]房间F已识别完成,前往终点")
            goal_pose = PoseStamped()  
            goal_pose.header.frame_id = "map" #终点
            goal_pose.pose.position.x = 0.063
            goal_pose.pose.position.y = -0.252
            goal_pose.pose.position.z = 0.000
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.703
            goal_pose.pose.orientation.w = 0.711
            goal_pub.publish(goal_pose)
            img_flag = 10


    if f==10 :
        if  img_flag == 10:
            print("start fllower line----------------------")   
            bridge = cv_bridge.CvBridge()   #bridge是一个CvBridge对象，用于将ROS图像消息转换为OpenCV图像格式
            image = bridge.imgmsg_to_cv2(data,desired_encoding='bgr8')  #将ROS图像消息转换为OpenCV图像格式
            image = cv2.resize(image, (640, 480))   #将图像大小调整为640x480
            image = cv2.flip(image,1)   #水平翻转图像
            image2=image.copy() #保存原图像

            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #将图像从BGR颜色空间转换为HSV颜色空间
            
            lower_yellow = np.array([ 0,  0,  203])
            upper_yellow = np.array([180, 30, 255])
            mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

            # cv2.imshow("mask",mask)
            follow = mask.copy()
            mid_output= mid(follow, mask)

            # BEGIN CROP
            # 
            h, w, d = image.shape
            search_top = int(3*h/4)
            search_bot = int(search_top + 20)
            mask[0:search_top, 0:w] = 0
            mask[search_bot:h, 0:w] = 0

            M = cv2.moments(mask)

            if  M['m00'] <=0:   # 代表图像中非零像素的数量
                num_stop=num_stop+1
                if  num_stop ==28:
                    print("lianxu-----------------------------------------------------------------------------------------")
                    hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
                    lower_yellow2= np.array([ 42,  27,  108])
                    upper_yellow2 = np.array([93, 92, 176])
                    mask2 = cv2.inRange(hsv2, lower_yellow2, upper_yellow2)
                    key=area(mask2)  
                    print(key)
                    if key >18:
                        print ("zhongdian")
                        twist.linear.x = 0.0
                        twist.angular.z = 0.0
                        cmd_vel_pub.publish(twist)

                        time.sleep(0.5)

                        goal_pose = PoseStamped()  
                        goal_pose.header.frame_id = "map" #F点内拍对角右
                        goal_pose.pose.position.x = 2
                        .088 #0.010
                        goal_pose.pose.position.y = -0.001 #-0.020
                        goal_pose.pose.position.z = 0.000
                        goal_pose.pose.orientation.x = 0
                        goal_pose.pose.orientation.y = 0
                        goal_pose.pose.orientation.z = 0.707 #0.716
                        goal_pose.pose.orientation.w = 0.707 #0.698
                        goal_pub.publish(goal_pose)
                        img_flag=11
                    # rospy.signal_shutdown("exit")
            else:
                num_stop=0

            cy = 240
            cx=mid_output
                #cy=360
            cv2.circle(image, (cx, cy), 20, (0,0,255), -1)
            vtherror = w/2-cx
                #print cx,cy
            twist.linear.x =0.135
            sum_pid = sum_pid + float(vtherror)
            d_pid = float(vtherror) - latter_pid
            twist.angular.z = float(vtherror) * Kp + sum_pid * Ki + d_pid * Kd# 400: 0.1, 300: 0.15, 250, 0.2
            latter_pid = float(vtherror)
            cmd_vel_pub.publish(twist)



    elif f==10:

        f=f+1
    else:
        pass




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
                rospy.sleep(0.3)
                f+=1
        elif f == 2:
                room_sound()
                rospy.sleep(0.3)
                f+=1
                
        elif f==7 or f == 8:
            f+=1
            
        elif f == 9:
            f+=1
        elif f==11:
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

if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber("/image_result",BoundingBoxes,boxes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()    
