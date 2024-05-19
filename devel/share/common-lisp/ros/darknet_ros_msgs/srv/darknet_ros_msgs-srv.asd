
(cl:in-package :asdf)

(defsystem "darknet_ros_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :darknet_ros_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "img" :depends-on ("_package_img"))
    (:file "_package_img" :depends-on ("_package"))
  ))