;; Auto-generated. Do not edit!


(when (boundp 'darknet_ros_msgs::img)
  (if (not (find-package "DARKNET_ROS_MSGS"))
    (make-package "DARKNET_ROS_MSGS"))
  (shadow 'img (find-package "DARKNET_ROS_MSGS")))
(unless (find-package "DARKNET_ROS_MSGS::IMG")
  (make-package "DARKNET_ROS_MSGS::IMG"))
(unless (find-package "DARKNET_ROS_MSGS::IMGREQUEST")
  (make-package "DARKNET_ROS_MSGS::IMGREQUEST"))
(unless (find-package "DARKNET_ROS_MSGS::IMGRESPONSE")
  (make-package "DARKNET_ROS_MSGS::IMGRESPONSE"))

(in-package "ROS")

(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))




(defclass darknet_ros_msgs::imgRequest
  :super ros::object
  :slots (_img ))

(defmethod darknet_ros_msgs::imgRequest
  (:init
   (&key
    ((:img __img) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _img __img)
   self)
  (:img
   (&rest __img)
   (if (keywordp (car __img))
       (send* _img __img)
     (progn
       (if __img (setq _img (car __img)))
       _img)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image _img
    (send _img :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image _img
       (send _img :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image _img
     (send _img :deserialize buf ptr-) (incf ptr- (send _img :serialization-length))
   ;;
   self)
  )

(defclass darknet_ros_msgs::imgResponse
  :super ros::object
  :slots (_gh ))

(defmethod darknet_ros_msgs::imgResponse
  (:init
   (&key
    ((:gh __gh) (instance darknet_ros_msgs::classes :init))
    )
   (send-super :init)
   (setq _gh __gh)
   self)
  (:gh
   (&rest __gh)
   (if (keywordp (car __gh))
       (send* _gh __gh)
     (progn
       (if __gh (setq _gh (car __gh)))
       _gh)))
  (:serialization-length
   ()
   (+
    ;; darknet_ros_msgs/classes _gh
    (send _gh :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; darknet_ros_msgs/classes _gh
       (send _gh :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; darknet_ros_msgs/classes _gh
     (send _gh :deserialize buf ptr-) (incf ptr- (send _gh :serialization-length))
   ;;
   self)
  )

(defclass darknet_ros_msgs::img
  :super ros::object
  :slots ())

(setf (get darknet_ros_msgs::img :md5sum-) "b243c66d754037e494b8467471231d86")
(setf (get darknet_ros_msgs::img :datatype-) "darknet_ros_msgs/img")
(setf (get darknet_ros_msgs::img :request) darknet_ros_msgs::imgRequest)
(setf (get darknet_ros_msgs::img :response) darknet_ros_msgs::imgResponse)

(defmethod darknet_ros_msgs::imgRequest
  (:response () (instance darknet_ros_msgs::imgResponse :init)))

(setf (get darknet_ros_msgs::imgRequest :md5sum-) "b243c66d754037e494b8467471231d86")
(setf (get darknet_ros_msgs::imgRequest :datatype-) "darknet_ros_msgs/imgRequest")
(setf (get darknet_ros_msgs::imgRequest :definition-)
      "sensor_msgs/Image img

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
---
classes gh

================================================================================
MSG: darknet_ros_msgs/classes
int16 corn_num  
int16 cucumber_num
int16 rice_num
int16 wheat_num
int16 corn_cut_num  
int16 cucumber_cut_num
int16 rice_cut_num
int16 wheat_cut_num
")

(setf (get darknet_ros_msgs::imgResponse :md5sum-) "b243c66d754037e494b8467471231d86")
(setf (get darknet_ros_msgs::imgResponse :datatype-) "darknet_ros_msgs/imgResponse")
(setf (get darknet_ros_msgs::imgResponse :definition-)
      "sensor_msgs/Image img

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
---
classes gh

================================================================================
MSG: darknet_ros_msgs/classes
int16 corn_num  
int16 cucumber_num
int16 rice_num
int16 wheat_num
int16 corn_cut_num  
int16 cucumber_cut_num
int16 rice_cut_num
int16 wheat_cut_num
")



(provide :darknet_ros_msgs/img "b243c66d754037e494b8467471231d86")


