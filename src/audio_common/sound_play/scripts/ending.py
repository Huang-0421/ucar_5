#!/usr/bin/env python
#-*-coding:utf-8-*-

# 加载ros的Python基础包
import rospy
# 加载topic话题 的 msg消息
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist,Pose
from std_msgs.msg import String
from nav_msgs.msg import Odometry
#from gazebo_msgs.msg import LinkStates
from std_msgs.msg import Header
import numpy as np
import math
a=0
flag1=0

def sub_robot_pose_update(config):
        global a, flag1
        cmd = Twist()
        global  goal_posex
        global  goal_posey 
        goal_posex = 0.002
        goal_posey = 0.006
        # Find the index of the racecar 找到小车的索引
        # try:
        #     #创建msg消息对象
        #     arrayIndex = msg.name.index('robot::dummy')
        # except ValueError as e:
        #     pass
        # else:
        #     # Extract our current position information 提取我们当前的位置信息
        #     last_received_pose = msg.pose[arrayIndex]
        #     last_received_twist = msg.twist[arrayIndex]
        if (abs(config.pose.pose.position.x - goal_posex)<0.2) and (abs(config.pose.pose.position.y - goal_posey)<0.2): #对比小车位置和目标点距离
            a =1
        else:
            a=0
        if config.pose.pose.position.x > 1 and config.pose.pose.position.x<1.3 and config.pose.pose.position.y > -4 and config.pose.pose.position.y < -3: #对比小车位置和目标点距离
            flag1 =1
        else:
            flag1 = 0


     

def callback(data):
    global a, flag1
    pub_cmd = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  
    # 创建 msg 消息, 注意:ros的float64是一个结构体
    vel_msg = Twist()
    if a==1 and flag1==1 :
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        print('\n')
        print('\n')
        print('\n')
        print("vel is adjusting!!!")
        print('\n')
        print('\n')
        print('\n')
    else:
        vel_msg.linear.x = data.linear.x
        vel_msg.angular.z =data.angular.z
    pub_cmd.publish(vel_msg)
   # 发布topic话题 —— 线速度输出
    # 向topic话题 发送 msg消息

if __name__ == '__main__':
    print('\n')
    print('\n')
    print('\n')
    print("ending is working!!!")
    print('\n')
    print('\n')
    print('\n')
        # 创建node节点 
    rospy.init_node('motor_control', anonymous=True)      
    rospy.Subscriber('/odom', Odometry, sub_robot_pose_update)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    # 阻塞等待
    rospy.spin()