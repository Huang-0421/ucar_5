#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from darknet_ros_msgs.msg import classes
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from actionlib_msgs.msg import GoalStatusArray
import actionlib
from std_msgs.msg import Int32

rospy.init_node('talker', anonymous=True)
soundhandle = SoundClient()
argv = '/home/ucar/ucar_ws/src/audio_common/sound_play/scripts/meat.mp3'
volume=10
soundhandle.playWave(argv, volume)