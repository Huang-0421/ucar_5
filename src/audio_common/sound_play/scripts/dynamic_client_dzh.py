#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry 
import tf
import dynamic_reconfigure.client 
flag1=0

def callback(config): 
    # print('\n')
    # print(config.pose.pose.position.x)
    # print(config.pose.pose.position.y)
    # print(type(config.pose.pose.position.y))
    change_dynamic(config.pose.pose.position.x,config.pose.pose.position.y)

def change_dynamic(x,y): 
    global flag1
    # if flag1==0 and 2.5<x<3 and -0.5<y<-1.5:
    if flag1==0 and x>0:
        # client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  
        # params = {"weight_optimaltime":0.5} 
        # params = {"max_vel_x":5} 
        # client.update_configuration(params) 
        rospy.set_param("/move_base/TebLocalPlannerROS/max_vel_x", 1)
        print("\n")
        print("\n")
        print("\n")
        print("slow !!!")
        print("\n")
        print("\n")
        print("\n")
        flag1=1
    elif flag1 == 1 and y <= -1.5:
        # client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  
        # params = {"weight_optimaltime":70}  
        # params = {"max_vel_x":100} 
        # client.update_configuration(params) 
        rospy.set_param("/move_base/TebLocalPlannerROS/max_vel_x", 20)
        print("\n")
        print("\n")
        print("\n")
        print("args recover!!!")
        print("\n")
        print("\n")
        print("\n")
        flag1=2

if __name__ == "__main__":
    rospy.init_node("dynamic_client",anonymous=True)
    rospy.Subscriber("/odom",Odometry,callback)
    rospy.spin() 
    
