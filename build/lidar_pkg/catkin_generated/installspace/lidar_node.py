#!/usr/bin/env python2
# coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan

# 订阅者回调函数
def LidarCallback(msg):
	dist = msg.ranges[180]	# 这里我们雷达起始角度为-180，msg.ranges[180]代表0度距离
	rospy.loginfo("前方距离 = %f 米", dist)

if __name__== "__main__":
	# 初始化节点
	rospy.init_node("lidar_node")
	# 利用rospy订阅雷达话题/scan, 回调函数为LidarCallback
	lidar_sub = rospy.Subscriber("/scan",LaserScan,LidarCallback,queue_size=10)
	# 让节点保持运行
	rospy.spin()