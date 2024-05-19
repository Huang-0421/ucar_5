#!/usr/bin/env python2

import rospy
from nav_msgs.msg import Odometry #查看位置信息
import dynamic_reconfigure.client #动态调参
flag=0

def callback(config): #将位置信息传递给判断函数
    print('\n')
    print(config.pose.pose.position)
    change_dynamic(config.pose.pose.position.x,config.pose.pose.position.y)

def change_dynamic(x,y): #判断函数
    global flag
    if flag==0 and 0.75<x<1.5 and -0.2<y<-0.5:
        client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
        params = {"acc_lim_x":0.15,"acc_lim_y":0.15,"max_vel_x":16.25,"max_vel_x_backwards":16.45,"max_vel_y":16.25}  #参数字典，填写需要修改的参数即可
        client.update_configuration(params) #使参数生效
        print("减速减速减速！！！")
        flag=1
    # if  4.70814<x<5.23000 and -0.300000<y<-0.100023:         #出弯后的位置判断
    #     client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
    #     params = {"feasibility_check_no_poses":3}  #参数字典，填写需要修改的参数即可
    #     client.update_configuration(params) #使参数生效
    #     flag=1
    #     print("出弯出弯出弯出弯出弯出弯出弯出弯出弯出弯出弯")
    # if flag==0 and 4.70814<x<5.23000 and -0.300000<y<-0.100023:         #出弯后的位置判断
    #     client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
    #     params = {"feasibility_check_no_poses":3,"max_global_plan_lookahead_dist":1.5}  #参数字典，填写需要修改的参数即可
    #     client.update_configuration(params) #使参数生效
    #     flag=1
    #     print("出弯出弯出弯出弯出弯出弯出弯出弯出弯出弯出弯")


    # if  -3.25274610519<y<-2.80851650238:         #进入房间后的位置判断
    # if  flag1==0 and -3.05274610519<y<-2.80851650238:
    #     client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
    #     params = {"max_vel_x":20,"max_vel_y":20,"max_vel_theta":20,"acc_lim_x":1.5, "acc_lim_y":1.5,"acc_lim_theta":3,"weight_max_vel_x":50,"weight_max_vel_y":50,"weight_max_vel_theta":300,"weight_acc_lim_theta":10,"weight_kinematics_nh":15,"weight_optimaltime":10,"weight_obstacle":1000,"global_plan_viapoint_sep":0.1}  #参数字典，填写需要修改的参数即可
    #     client.update_configuration(params) #使参数生效
    #     flag1=1
    #     flag=0
    #     print("进入房间")
    
    # # if   -2.80851650238<y<-2.2043466568:         #出房间时的位置判断
    # if flag==0 and-2.80851650238<y<-2.6043466568:
    #     client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
    #     params = {"max_vel_x":20,"max_vel_y":20,"max_vel_theta":20,"acc_lim_x":1.5, "acc_lim_y":1.5,"acc_lim_theta":1.0,"weight_max_vel_x":200,"weight_max_vel_y":200,"weight_max_vel_theta":10,"weight_acc_lim_theta":0.5,"weight_kinematics_nh":100,"weight_optimaltime":18,"weight_obstacle":1000,"global_plan_viapoint_sep":0.5}  #参数字典，填写需要修改的参数即可
    #     client.update_configuration(params) #使参数生效
    #     flag=1
    #     flag1=0
    #     print("出房间")
    

    
    
    # if 3.87108<x<4.32339 and -2.28000<y<-2.18000:         #出的位置判断
    #     client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
    #     params = {"max_vel_x":1.0,"max_vel_y":1.0,"max_vel_theta":1.0} #参数字典，填写需要修改的参数即可
    #     client.update_configuration(params) #使参数生效
    #     print("房间1房间1房间1房间1房间1房间1房间1房间1房间1")

    # if 2.33654<x<2.896016 and -3.0000<y<-2.92000:         #出弯后的位置判断
    #     client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
    #     params = {"max_vel_x":0.5,"max_vel_y":0.5,"max_vel_theta":0.5} #参数字典，填写需要修改的参数即可
    #     client.update_configuration(params) #使参数生效
    #     print("房间2房间2房间2房间2房间2房间2房间2房间2房间2")

    # if 1.45768<x<1.87000 and -2.28000<y<-:-2.18000:      #出弯后的位置判断
    #     client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS")  #向参数服务端申请修改，对应参数服务端名字可用rqt_reconfigure查看，应该rosparam list也行
    #     params = {"max_vel_x":1.0,"max_vel_y":1.0,"max_vel_theta":1.0} #参数字典，填写需要修改的参数即可
    #     client.update_configuration(params) #使参数生效
    #     print("房间3房间3房间3房间3房间3房间3房间3房间3房间3")
    # print(x,y,"\n") 

if __name__ == "__main__":
    rospy.init_node("dynamic_client",anonymous=True)
    rospy.Subscriber("/odom",Odometry,callback)

    # client = dynamic_reconfigure.client.Client("/move_base/TebLocalPlannerROS", timeout=30, config_callback=callback)
    # client.update_configuration({"max_vel_x":10})
    rospy.spin() 



    # x1=4.70814 x2=5.02300 y=-0.259023