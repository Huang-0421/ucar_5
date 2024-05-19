#!/usr/bin/env python

import rospy
#from nav_msgs.msg import Odometry 
from nav_msgs.msg import * 
import tf
import dynamic_reconfigure.client 
flag1=0

def callback(config): 
    print('\n')
    print('\n')
    print('\n')
    print(config)
    # change_dynamic(config.pose.pose.position.x,config.pose.pose.position.y)

# def change_dynamic(x,y): 
#     global flag1
#     if flag1==0 and 2.5<x<3 and -0.5<y<-1.5:
#         client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  
#         params = {"weight_optimaltime":0.5}  
#         client.update_configuration(params) 
#         print("\n")
#         print("\n")
#         print("\n")
#         print("\n")
#         print("\n")
#         print("\n")
#         flag1=1
#     elif flag1 == 1 and y <= -1.5:
#         client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  
#         params = {"weight_optimaltime":70}  
#         client.update_configuration(params) 
#         print("\n")
#         print("\n")
#         print("\n")
#         print("\n")
#         print("\n")
#         print("\n")
#         flag1=2

if __name__ == "__main__":
    rospy.init_node("dynamic_client",anonymous=True)
    rospy.Subscriber("/odom",Odometry,callback)
    rospy.spin() 
