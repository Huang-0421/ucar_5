#!/usr/bin/env python2
# -*- coding: utf8 -*-

import rospy
import tf2_ros
import math
from geometry_msgs.msg import PoseStamped as GPS
from geometry_msgs.msg import Pose
from tf2_geometry_msgs import PoseStamped
from std_msgs.msg import String

start_time = None
start_pose = None
goal_pose = None
min_dist = 0.2
total_time=0

flag=0
# def start(msg):
#     global start_pose
#     global goal_pose
#     global start_time
#     global timer
    
#     start_time = rospy.Time.now()
#     goal_pose = msg.pose
#     # goal_pose.position.x = 0.000
#     # goal_pose.position.y = -0.950
#     # 启用计时器
#     timer = rospy.Timer(rospy.Duration(0.25), timer_cb) # 10 hz
#     print ('Starting time: ', start_time.to_sec(), "@", (goal_pose.position.x, goal_pose.position.y, goal_pose.position.z))
#     p = Pose()
#     trans=tf_buffer.lookup_transform('map', 'base_link', time=rospy.Time(0), timeout=rospy.Duration(5))
#     p.position.x = trans.transform.translation.x
#     p.position.y = trans.transform.translation.y
#     p.position.z = trans.transform.translation.z
#     start_pose = p


def start(msg):
    global start_pose
    global goal_pose
    global start_time
    global timer
    global flag 

    if flag==0:
        start_time = rospy.Time.now()
        goal_pose = msg.pose
        goal_pose.position.x = 0.010
        goal_pose.position.y = -0.950
        # 启用计时器
        timer = rospy.Timer(rospy.Duration(0.25), timer_cb) # 10 hz
        print ('Starting time: ', start_time.to_sec(), "@", (goal_pose.position.x, goal_pose.position.y, goal_pose.position.z))
        p = Pose()
        trans=tf_buffer.lookup_transform('map', 'base_link', time=rospy.Time(0), timeout=rospy.Duration(5))
        p.position.x = trans.transform.translation.x
        p.position.y = trans.transform.translation.y
        p.position.z = trans.transform.translation.z
        start_pose = p
        flag=1

def timer_cb(event):
    global tf_buffer
    global start_pose
    global goal_pose
    global start_time
    global timer
    global total_time
    
    if (start_time is not None) and (goal_pose is not None):
        # 检查小车位置，判断是否到达终点
        trans=tf_buffer.lookup_transform('map', 'base_link', time=rospy.Time(0), timeout=rospy.Duration(5))
        dist = math.sqrt(math.pow(trans.transform.translation.x - goal_pose.position.x, 2) + math.pow(trans.transform.translation.y - goal_pose.position.y, 2))
        # print ("dist: %.2f m  \t %.2f s" % (dist, (rospy.Time.now()-start_time).to_sec()))
        if dist < min_dist:
            print ("Goal reached:", (start_pose.position.x, start_pose.position.y, start_pose.position.z), " -> ", (goal_pose.position.x, goal_pose.position.y, goal_pose.position.z))
            print ("Elismted time: %.2f s" % (trans.header.stamp - start_time).to_sec())
            total_time+=(trans.header.stamp - start_time).to_sec()
            print("Total_time_cost: %.2fs" % total_time)
            # print ("Average speed(fullway): %.2f m/s" % (80/(trans.header.stamp - start_time).to_sec()))
            timer.shutdown()


def main():
    global tf_buffer
    
    print ("listening to /move_base_simple/goal...")
    rospy.Subscriber('/move_base_simple/goal', GPS, start)
    
    #设置tf2_listener
    tf_buffer=tf2_ros.Buffer()
    tf_listener=tf2_ros.TransformListener(tf_buffer)
    
    # rostopic info /move_base_simple/goal
    # Type: geometry_msgs/PoseStamped

    # Publishers: 
    #  * /rviz (http://wcr-GL552VW:39035/)

    # Subscribers: 
    #  * /move_base (http://wcr-GL552VW:42559/)
    #  * /rviz (http://wcr-GL552VW:39035/)
    
    
        
if __name__ == "__main__":
    rospy.init_node("ucar_timer",anonymous=True)
    main()
    rospy.spin()
    
