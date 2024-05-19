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
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud
from cv_bridge import CvBridge, CvBridgeError
import cv2
from actionlib_msgs.msg import GoalStatusArray
from  math import pi
import roslib; roslib.load_manifest('laser_assembler')
import rospy; 
from laser_assembler.srv import *
import math
from numpy import *


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


#分为12个方向
# def calculate_direction(a,b):
#     list1=[[1.000,0.000],[0.976,-0.219],[-0.853,0.522],[-0.704,0.710],[-0.513,0.859],[-0.233,0.973],[0.000,1.000],[0.229,0.973],[0.540,0.841],[0.713,0.701],[0.854,0.520],[0.975,0.224]]
#     list_point=[]
#     # a=[5,-3] 小车位置
#     # b=[3,-5] 板子位置
#     len_x=abs(a[0]-b[0])
#     len_y=abs(a[1]-b[1])
#     ten=len_y/len_x
#     ten_1=0.26795
#     ten_2=1
#     ten_3=3.73205
#     #ten(15)=0.26795,ten(45)=1,ten(75)=3.73205
#     if float(a[0])>float(b[0]) and float(a[1])>float(b[1]):
#         if ten<ten_1:
#             list_point=list1[0]
#         elif ten_1<ten<ten_2:
#             list_point=list1[1]
#         elif ten_2<ten<ten_3:
#             list_point=list1[2]
#         elif ten_3<ten:
#             list_point=list1[3]

#     elif float(a[0])<float(b[0]) and float(a[1])>float(b[1]):
#         if ten<ten_1:
#             list_point=list1[6]
#         elif ten_1<ten<ten_2:
#             list_point=list1[5]
#         elif ten_2<ten<ten_3:
#             list_point=list1[4]
#         elif ten_3<ten:
#             list_point=list1[3]
        
#     elif  float(a[0])<float(b[0]) and float(a[1])< float(b[1]):
#         if ten<ten_1:
#             list_point=list1[6]
#         elif ten_1<ten<ten_2:
#             list_point=list1[7]
#         elif ten_2<ten<ten_3:
#             list_point=list1[8]
#         elif ten_3<ten:
#             list_point=list1[9]

#     elif float(a[0])>float(b[0]) and float(a[1])<float(b[1]):
#         if ten<ten_1:
#             list_point=list1[0]
#         elif ten_1<ten<ten_2:
#             list_point=list1[11]
#         elif ten_2<ten<ten_3:
#             list_point=list1[10]
#         elif ten_3<ten:
#             list_point=list1[9]

#     return list_point

#分为24个方向
def calculate_direction(a,b):
    global f
    list1=[[1.000,0.000,0],[0.993,-0.116,1],[0.963,-0.271,2],[0.927,-0.376,3],[0.889,-0.459,4],[-0.818,0.576,5],[-0.707,0.707,6],[-0.599,0.801,7],[-0.491,0.871,8],[-0.383,0.924,9],[-0.300,0.954,10],[-0.166,0.986,11],[0.000,1.000,12],[0.133,0.991,13],[0.279,0.960,14],[0.382,0.924,15],[0.478,0.879,16],[0.579,0.815,17],[0.707,0.707,18],[0.803,0.595,19],[0.881,0.473,20],[0.928,0.371,21],[0.954,0.301,22],[0.991,0.133,23]]
    list_point=[]
    # a=[5,-3] 小车位置
    # b=[3,-5] 板子位置
    len_x=abs(a[0]-b[0])
    len_y=abs(a[1]-b[1])
    ten=len_y/len_x
    ten_1=0.13165
    ten_2=0.41421
    ten_3=0.76732
    ten_4=1.30322
    ten_5=2.41421
    ten_6=7.59575
    #ten(15)=0.26795,ten(45)=1,ten(75)=3.73205
    if f==1:
        if float(b[0])<0 and float(b[1])<0:
            if ten<ten_1:
                list_point=list1[0]
            elif ten_1<ten<ten_2:
                list_point=list1[1]
            elif ten_2<ten<ten_3:
                list_point=list1[2]
            elif ten_3<ten<ten_4:
                list_point=list1[3]
            elif ten_4<ten<ten_5:
                list_point=list1[4]
            elif ten_5<ten<ten_6:
                list_point=list1[5]
            elif ten_6<ten:
                list_point=list1[6]

        elif float(b[0])>0 and float(b[1])<0:
            if ten<ten_1:
                list_point=list1[12]
            elif ten_1<ten<ten_2:
                list_point=list1[11]
            elif ten_2<ten<ten_3:
                list_point=list1[10]
            elif ten_3<ten<ten_4:
                list_point=list1[9]
            elif ten_4<ten<ten_5:
                list_point=list1[8]
            elif ten_5<ten<ten_6:
                list_point=list1[7]
            elif ten_6<ten:
                list_point=list1[6]
            
        elif  float(b[0])>0 and float(b[1])>0:
            if ten<ten_1:
                list_point=list1[12]
            elif ten_1<ten<ten_2:
                list_point=list1[13]
            elif ten_2<ten<ten_3:
                list_point=list1[14]
            elif ten_3<ten<ten_4:
                list_point=list1[15]
            elif ten_4<ten<ten_5:
                list_point=list1[16]
            elif ten_5<ten<ten_6:
                list_point=list1[17]
            elif ten_6<ten:
                list_point=list1[18]

        elif float(b[0])<0 and float(b[1])>0:
            if ten<ten_1:
                list_point=list1[0]
            elif ten_1<ten<ten_2:
                list_point=list1[23]
            elif ten_2<ten<ten_3:
                list_point=list1[22]
            elif ten_3<ten<ten_4:
                list_point=list1[21]
            elif ten_4<ten<ten_5:
                list_point=list1[20]
            elif ten_5<ten<ten_6:
                list_point=list1[19]
            elif ten_6<ten:
                list_point=list1[18]
    else:
        if float(b[0])>0 and float(b[1])<0:
            if ten<ten_1:
                list_point=list1[0]
            elif ten_1<ten<ten_2:
                list_point=list1[1]
            elif ten_2<ten<ten_3:
                list_point=list1[2]
            elif ten_3<ten<ten_4:
                list_point=list1[3]
            elif ten_4<ten<ten_5:
                list_point=list1[4]
            elif ten_5<ten<ten_6:
                list_point=list1[5]
            elif ten_6<ten:
                list_point=list1[6]

        elif float(b[0])>0 and float(b[1])>0:
            if ten<ten_1:
                list_point=list1[12]
            elif ten_1<ten<ten_2:
                list_point=list1[11]
            elif ten_2<ten<ten_3:
                list_point=list1[10]
            elif ten_3<ten<ten_4:
                list_point=list1[9]
            elif ten_4<ten<ten_5:
                list_point=list1[8]
            elif ten_5<ten<ten_6:
                list_point=list1[7]
            elif ten_6<ten:
                list_point=list1[6]
            
        elif  float(b[0])<0 and float(b[1])>0:
            if ten<ten_1:
                list_point=list1[12]
            elif ten_1<ten<ten_2:
                list_point=list1[13]
            elif ten_2<ten<ten_3:
                list_point=list1[14]
            elif ten_3<ten<ten_4:
                list_point=list1[15]
            elif ten_4<ten<ten_5:
                list_point=list1[16]
            elif ten_5<ten<ten_6:
                list_point=list1[17]
            elif ten_6<ten:
                list_point=list1[18]

        elif float(b[0])<0 and float(b[1])<0:
            if ten<ten_1:
                list_point=list1[0]
            elif ten_1<ten<ten_2:
                list_point=list1[23]
            elif ten_2<ten<ten_3:
                list_point=list1[22]
            elif ten_3<ten<ten_4:
                list_point=list1[21]
            elif ten_4<ten<ten_5:
                list_point=list1[20]
            elif ten_5<ten<ten_6:
                list_point=list1[19]
            elif ten_6<ten:
                list_point=list1[18]


    return list_point

# 计算欧式距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB)

# 给定数据集构建一个包含k个随机质心的集合
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))#create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:,j]) 
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids

# K-均值聚类算法
# dataSet:数据集
# k:簇个数
# distMeas:距离计算方法
# createCent:创建初始质心方法
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))#create mat to assign data points 
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            # 寻找最近的质心
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        # 打印当前质心
        # print(centroids)
        # 更新质心的位置
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
    return centroids, clusterAssment


def find_direction(data):
    dataSet=array(data)
    return kMeans(dataSet,2)[0]

def point_filter(resp):
    global f
    point_list=[]       
    xlist=[]
    ylist=[]
    for i  in range(len(resp.cloud.points)):
        x=resp.cloud.points[i].x
        y=resp.cloud.points[i].y
        # if (-0.65<x<0.6 and -1.5<y<1 and f==1) or (-0.5<x<1.22 and -0.5<y<0.4 and f==4) or (-1.5<x<1.2 and -1<y<0.8 and f==7):
        if -0.8<x<0.8 and -1.8<y<1.2 and f==1:
            point=[x,y]
            point_list.append(point)
            xlist.append(x)
            ylist.append(y)

        if -0.6<x<1.5 and -0.65<y<0.4 and f==4:
            point=[x,y]
            point_list.append(point)
            xlist.append(x)
            ylist.append(y)

        if -1.65<x<1.8 and -1.1<y<0.8 and f==7:
            point=[x,y]
            point_list.append(point)
            xlist.append(x)
            ylist.append(y)
    # savetxt("data_x.txt",xlist)
    # savetxt("data_y.txt",ylist)
    # print("saved")
    print(point_list)
    return point_list

# def point_selector(data):
    

def room_class(msg):
    room=str(msg)
    if "tableware" in room:
        msg[0]=1
    elif "food" in room:
        msg[0]=1
    elif "sofa" in room:
        msg[0]=3
    elif "bed" in room:
        msg[0]=2
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
    if seq>=2 and seq<=4:
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
            f=3
            img_flag=3
            error_image_num+=4-seq
            print("房间b已识别完成,前往房间c")

    if seq>=5 and seq<=7:
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
            f=8
            img_flag=8
            flag_3=1
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
            f=6
            img_flag=6
            error_image_num+=7-seq
            print("房间c已识别完成,前往房间d")

    if seq>=8 and seq<=10:
        slist=[]
        for i in range(len(msg.bounding_boxes)):
            slist.append(msg.bounding_boxes[i].Class)
        d_room.append(slist)
        room_class(d_room)
        if d_room[0]!=0:
            goal_pose = PoseStamped()               #终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.100
            goal_pose.pose.position.y = -0.900
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.017
            goal_pub.publish(goal_pose)
            f=9
            img_flag=9
            error_image_num+=10-seq
            print("房间d已识别完成,前往终点")


def img_callback(data):
    global f,img_flag,Img_publish,fang,b_room,c_room,d_room,first_image,flag_3

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
        # client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")
        # client.update_configuration({"max_vel_x":0})



    elif f==2 :
        if img_flag == 1:
            img_flag = 2
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))

    elif f==3 :
        if img_flag == 2:
            img_flag = 3
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()                    #第二个房间第一个方向
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.994
            goal_pose.pose.position.y = -4.303
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  -0.700
            goal_pose.pose.orientation.w = 0.714
            goal_pub.publish(goal_pose)
            print("去往房间c")

    elif f==4 :
        if img_flag == 3:
            img_flag = 4
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))

    elif f==5 :
        if img_flag == 4:
            img_flag = 5
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))


    elif f==6 :
        if img_flag == 5:
            img_flag = 6
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
            goal_pose.pose.orientation.z = -0.709
            goal_pose.pose.orientation.w = 0.705
            goal_pub.publish(goal_pose)
            print("去往房间d")

    elif f==7 :
        if img_flag == 6:
            img_flag = 7
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))


    elif f==8 :
        if img_flag == 7:
            img_flag = 8
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
    

    elif f==9 and flag_3==1:
        if img_flag == 8:
            goal_pose = PoseStamped()               #直接前往终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.050
            goal_pose.pose.position.y = -0.900
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.017
            goal_pub.publish(goal_pose)

    elif f==9 :
        if img_flag == 8:
            img_flag = 9
            Img_publish = data
            img_pub.publish(Img_publish)
            print ('第%d张图片发布'%(img_flag))
            goal_pose = PoseStamped()               #终点位置
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x =  0.100
            goal_pose.pose.position.y = -0.900
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 1.000
            goal_pose.pose.orientation.w = -0.017
            goal_pub.publish(goal_pose)
            print("去往终点")

    elif f==10:
        if img_flag == 9:
            print('B房间识别情况')
            print(b_room)
            print('C房间识别情况')
            print(c_room)
            print('D房间识别情况')
            print(d_room)
            room_sound()
            print(fang)
            argv = '/home/ucar/ucar_ws/src/audio_common/mp3/'+fang+'.mp3'
            print(argv)
            soundhandle.playWave(argv) 
            print ('到达终点')
            f=f+1
    else:
        pass


def give_goal(result_list):
    global f
    if f==1:
        goal_pose = PoseStamped()                    
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = 4.711
        goal_pose.pose.position.y = -4.000
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0
        goal_pose.pose.orientation.y = 0
        goal_pose.pose.orientation.z = result_list[0][0]
        goal_pose.pose.orientation.w = result_list[0][1]
        goal_pub.publish(goal_pose)
        print("发布下一个位置1")

    if f==2:
        goal_pose = PoseStamped()                    
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = 4.711
        goal_pose.pose.position.y = -4.000
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0
        goal_pose.pose.orientation.y = 0
        goal_pose.pose.orientation.z = result_list[1][0]
        goal_pose.pose.orientation.w = result_list[1][1]
        goal_pub.publish(goal_pose)
        print("发布下一个位置2")

    if f==4:
        goal_pose = PoseStamped()                    
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = 2.994
        goal_pose.pose.position.y = -4.303
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0
        goal_pose.pose.orientation.y = 0
        goal_pose.pose.orientation.z = result_list[0][0]
        goal_pose.pose.orientation.w = result_list[0][1]
        goal_pub.publish(goal_pose)
        print("发布下一个位置4")

    if f==5:
        goal_pose = PoseStamped()                    
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = 2.994
        goal_pose.pose.position.y = -4.303
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0
        goal_pose.pose.orientation.y = 0
        goal_pose.pose.orientation.z = result_list[1][0]
        goal_pose.pose.orientation.w = result_list[1][1]
        goal_pub.publish(goal_pose)
        print("发布下一个位置5")

    if f==7:
        goal_pose = PoseStamped()                    
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = 1.018
        goal_pose.pose.position.y = -3.855
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0
        goal_pose.pose.orientation.y = 0
        goal_pose.pose.orientation.z = result_list[0][0]
        goal_pose.pose.orientation.w = result_list[0][1]
        goal_pub.publish(goal_pose)
        print("发布下一个位置7")

    if f==8:
        goal_pose = PoseStamped()                    
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = 1.018
        goal_pose.pose.position.y = -3.855
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0
        goal_pose.pose.orientation.y = 0
        goal_pose.pose.orientation.z = result_list[1][0]
        goal_pose.pose.orientation.w = result_list[1][1]
        goal_pub.publish(goal_pose)
        print("发布下一个位置8")

def goal_callback(msg):
    #更新小车位置信息
    global f
    if msg.status.status == 3:       
        if f <13:
            rospy.sleep(1.0)
            f+=1
    print('到达第%d个位置'%(f))
    if f==1 or f==4 or f==7:
        print("开始雷达定位...")
        assemble_scans = rospy.ServiceProxy('assemble_scans', AssembleScans)
        resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
        print("Got cloud with %u points"%(len(resp.cloud.points)))
        data=point_filter(resp)
        ThePoint=find_direction(data)
        print("定位结果")
        print(ThePoint)
        global result_list
        result_list=[]
        if f==1:
            for i in range(len(ThePoint)):
                result=calculate_direction([0,0],[ThePoint[i,0],ThePoint[i,1]])
                result_list.append(result)
            print(result_list)
        if f==4:
            for i in range(len(ThePoint)):
                result=calculate_direction([0,0],[ThePoint[i,0],ThePoint[i,1]])
                result_list.append(result)
            print(result_list)
        if f==7:
            for i in range(len(ThePoint)):
                result=calculate_direction([0,0],[ThePoint[i,0],ThePoint[i,1]])
                result_list.append(result)
            print(result_list)
    give_goal(result_list)





if __name__ == '__main__':
    print("执行play_lzl")
    rospy.init_node('play_lzl', anonymous=True)
    rospy.Subscriber("/image_result",BoundingBoxes,boxes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal_callback)  #判断是否到达既定目标点
    rospy.wait_for_service("assemble_scans")
    rospy.spin()    
