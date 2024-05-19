#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import time

f=0
flag=1

def img_callback(data):
    bridge = CvBridge()
    global f,flag
    cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
    if f<=9 and flag==1:
        cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/4060%d.jpg'%(f), cv_img)  
        print("Has been photographed %d"%(f))
        flag=0
    elif f>=10 and flag==1:
        cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/406%d.jpg'%(f), cv_img)  
        print("Has been photographed %d"%(f))
        flag=0
if __name__ == '__main__':
    rospy.init_node('play', anonymous=True)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    print("Has started")
    for i in range(0,10):
        f+=1
        time.sleep(4)
        flag=1
    rospy.spin() 


