;; Auto-generated. Do not edit!


(when (boundp 'darknet_ros_msgs::classes)
  (if (not (find-package "DARKNET_ROS_MSGS"))
    (make-package "DARKNET_ROS_MSGS"))
  (shadow 'classes (find-package "DARKNET_ROS_MSGS")))
(unless (find-package "DARKNET_ROS_MSGS::CLASSES")
  (make-package "DARKNET_ROS_MSGS::CLASSES"))

(in-package "ROS")
;;//! \htmlinclude classes.msg.html


(defclass darknet_ros_msgs::classes
  :super ros::object
  :slots (_corn_num _cucumber_num _rice_num _wheat_num _corn_cut_num _cucumber_cut_num _rice_cut_num _wheat_cut_num ))

(defmethod darknet_ros_msgs::classes
  (:init
   (&key
    ((:corn_num __corn_num) 0)
    ((:cucumber_num __cucumber_num) 0)
    ((:rice_num __rice_num) 0)
    ((:wheat_num __wheat_num) 0)
    ((:corn_cut_num __corn_cut_num) 0)
    ((:cucumber_cut_num __cucumber_cut_num) 0)
    ((:rice_cut_num __rice_cut_num) 0)
    ((:wheat_cut_num __wheat_cut_num) 0)
    )
   (send-super :init)
   (setq _corn_num (round __corn_num))
   (setq _cucumber_num (round __cucumber_num))
   (setq _rice_num (round __rice_num))
   (setq _wheat_num (round __wheat_num))
   (setq _corn_cut_num (round __corn_cut_num))
   (setq _cucumber_cut_num (round __cucumber_cut_num))
   (setq _rice_cut_num (round __rice_cut_num))
   (setq _wheat_cut_num (round __wheat_cut_num))
   self)
  (:corn_num
   (&optional __corn_num)
   (if __corn_num (setq _corn_num __corn_num)) _corn_num)
  (:cucumber_num
   (&optional __cucumber_num)
   (if __cucumber_num (setq _cucumber_num __cucumber_num)) _cucumber_num)
  (:rice_num
   (&optional __rice_num)
   (if __rice_num (setq _rice_num __rice_num)) _rice_num)
  (:wheat_num
   (&optional __wheat_num)
   (if __wheat_num (setq _wheat_num __wheat_num)) _wheat_num)
  (:corn_cut_num
   (&optional __corn_cut_num)
   (if __corn_cut_num (setq _corn_cut_num __corn_cut_num)) _corn_cut_num)
  (:cucumber_cut_num
   (&optional __cucumber_cut_num)
   (if __cucumber_cut_num (setq _cucumber_cut_num __cucumber_cut_num)) _cucumber_cut_num)
  (:rice_cut_num
   (&optional __rice_cut_num)
   (if __rice_cut_num (setq _rice_cut_num __rice_cut_num)) _rice_cut_num)
  (:wheat_cut_num
   (&optional __wheat_cut_num)
   (if __wheat_cut_num (setq _wheat_cut_num __wheat_cut_num)) _wheat_cut_num)
  (:serialization-length
   ()
   (+
    ;; int16 _corn_num
    2
    ;; int16 _cucumber_num
    2
    ;; int16 _rice_num
    2
    ;; int16 _wheat_num
    2
    ;; int16 _corn_cut_num
    2
    ;; int16 _cucumber_cut_num
    2
    ;; int16 _rice_cut_num
    2
    ;; int16 _wheat_cut_num
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _corn_num
       (write-word _corn_num s)
     ;; int16 _cucumber_num
       (write-word _cucumber_num s)
     ;; int16 _rice_num
       (write-word _rice_num s)
     ;; int16 _wheat_num
       (write-word _wheat_num s)
     ;; int16 _corn_cut_num
       (write-word _corn_cut_num s)
     ;; int16 _cucumber_cut_num
       (write-word _cucumber_cut_num s)
     ;; int16 _rice_cut_num
       (write-word _rice_cut_num s)
     ;; int16 _wheat_cut_num
       (write-word _wheat_cut_num s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _corn_num
     (setq _corn_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _cucumber_num
     (setq _cucumber_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _rice_num
     (setq _rice_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _wheat_num
     (setq _wheat_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _corn_cut_num
     (setq _corn_cut_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _cucumber_cut_num
     (setq _cucumber_cut_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _rice_cut_num
     (setq _rice_cut_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _wheat_cut_num
     (setq _wheat_cut_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get darknet_ros_msgs::classes :md5sum-) "5de667e5e14606f356e3c7c2b8f9d715")
(setf (get darknet_ros_msgs::classes :datatype-) "darknet_ros_msgs/classes")
(setf (get darknet_ros_msgs::classes :definition-)
      "int16 corn_num  
int16 cucumber_num
int16 rice_num
int16 wheat_num
int16 corn_cut_num  
int16 cucumber_cut_num
int16 rice_cut_num
int16 wheat_cut_num

")



(provide :darknet_ros_msgs/classes "5de667e5e14606f356e3c7c2b8f9d715")


