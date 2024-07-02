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
import cv_bridge


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

twist = Twist()

#巡线参数
Kp = 0.0018
Ki = 0.000000
Kd = 0.0000000

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
    
    if f==10 :
        if  img_flag == 10:
            print("start fllower line----------------------")   
            bridge = cv_bridge.CvBridge()   
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
            h, w, d = image.shape   # 高度、宽度、深度（图像通道数）

            #定义感兴趣的范围 (3/4h ~ 3/4h + 20)
            search_top = int(3*h/4)             # 上方限制到3/4的高度
            search_bot = int(search_top + 20)   # 下方限制到宽度为20区域
            mask[0:search_top, 0:w] = 0         # 将图像上方 search_top 以上的区域设为0（黑色），忽略该部分。
            mask[search_bot:h, 0:w] = 0         # 将图像下方 search_bot 以下的区域设为0（黑色），忽略该部分。

            M = cv2.moments(mask) # 计算感兴趣区域的图像矩，用于后续计算质心或其他特征。

            if  M['m00'] <=0:   # m00代表图像的非零像素点的总和，即图像的面积,小于等于0，表示当前帧图像中没有检测到赛道区域
                num_stop=num_stop+1 # 记录连续帧中没有检测到赛道的次数
                if  num_stop ==28:  # 28帧图像中都没有出现赛道说明到达终点
                    print("28 times without road")

                    #进一步的检测确认是否没有赛道
                    hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
                    lower_yellow2= np.array([ 42,  27,  108])
                    upper_yellow2 = np.array([93, 92, 176])
                    mask2 = cv2.inRange(hsv2, lower_yellow2, upper_yellow2)
                    rate = area(mask2)  
                    print(rate)

                    if rate > 18:   # ??为什么是大于，为什么是18，此处应该表达赛道像素点占总面积的rate小于某个阈值，则需要到达终点
                        print ("final position")
                        twist.linear.x = 0.0
                        twist.angular.z = 0.0
                        cmd_vel_pub.publish(twist)

                        time.sleep(0.5)

                        goal_pose = PoseStamped()  
                        goal_pose.header.frame_id = "map"
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

            cy = 240    #一半高的位置
            cx=mid_output   #该位置的赛道中点
                #cy=360
            cv2.circle(image, (cx, cy), 20, (0,0,255), -1)  #在图像中 cx, cy 位置绘制一个半径为20的红色实心圆，以便在图像中可视化中线位置。
            vtherror = w/2-cx   #横向误差，是图像中心的x坐标（w / 2）与赛道中线x坐标（cx）之间的差值。用于调整机器人的角速度
            
            twist.linear.x =0.135   #线速度为0.135
            sum_pid = sum_pid + float(vtherror)
            d_pid = float(vtherror) - latter_pid
            twist.angular.z = float(vtherror) * Kp + sum_pid * Ki + d_pid * Kd# 400: 0.1, 300: 0.15, 250, 0.2
            latter_pid = float(vtherror)
            cmd_vel_pub.publish(twist)
    else:
        pass

def mid(follow, mask):
    halfWidth = follow.shape[1] // 2 #图片一半的宽度
    half = halfWidth  

    # 从下往上扫描赛道,最下端取图片中线为分割线
    for y in range(follow.shape[0]-1 , -1 , -1):
        # follow.shape[0]为图像行数，图像最上面为0行，follow.shape[0]-1表示最后一行
        # -1是循环终止条件，到0后停止，第二个-1为步长，每次减少一行
        
        # V2改动:加入分割线左右各半张图片的宽度作为约束,减小邻近赛道的干扰
        if (mask[y][max(0, half - halfWidth):half] == np.zeros_like(
                mask[y][max(0, half - halfWidth):half])).all():  # 分割线左端无赛道，.all()函数用于检查前面的比较结果，如果所有元素都为True，则返回True，否则返回False。
            # 这一行代码的作用是检查mask的第y行的左半部分（从max(0, half - halfWidth)到half）是否全是0。全为0意味着这一部分没有赛道。
            left = max(0, half - halfWidth)  # 如果分割线左端没有赛道，说明赛道在图片之外，则取图片左边界为左赛道
        else:
            left = np.average(np.where(mask[y][0:half] == 255))  # 计算左赛道平均位置

        if (mask[y][half:min(follow.shape[1], half + halfWidth)] == np.zeros_like(
                mask[y][half:min(follow.shape[1], half + halfWidth)])).all(): 
            right = min(follow.shape[1], half + halfWidth)  
        else:
            right = np.average(np.where(mask[y][half:follow.shape[1]] == 255)) + half  

        mid = (left + right) // 2  # 计算当前行的赛道中点

        half = mid  # 递归,从下往上确定分割线

        follow[y, mid] = 255  # 画出拟合中线

        if y == 240:  # 设置指定提取中点的纵轴位置
            mid_output = mid
    cv2.circle(follow, (mid_output, 360), 5, 255, -1)  # opencv为(x,y),画出指定提取中点

    error = follow.shape[1] // 2 - mid_output  # 计算图片中点与指定提取中点的误差
    return mid_output # error为正数右转,为负数左转

def area(mask):
    num1 = 0    # 用于记录非零像素的数量
    h,w=mask.shape 
    # 将高度和宽度都缩小为原来的3/4，以减少计算量并专注于图像中间区域 
    h=int(3*h/4)
    w=int(3*w/4)

    mask_area=h*w   #计算调整后的区域总面积
    print("area:",mask_area)

    #使用双重循环遍历感兴趣区域的每个像素。如果像素值不为零，则计数器 num1 增加
    for i in range(h):
        for j in range(w):
            if mask[i][j]!=0:
                num1=num1+1
    print("num1",num1)
    # 计算非零像素占整个区域的百分比
    rate=num1*100/mask_area 
    return  rate

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
            f+=1
            
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
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()    

