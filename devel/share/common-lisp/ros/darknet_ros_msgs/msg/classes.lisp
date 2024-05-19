; Auto-generated. Do not edit!


(cl:in-package darknet_ros_msgs-msg)


;//! \htmlinclude classes.msg.html

(cl:defclass <classes> (roslisp-msg-protocol:ros-message)
  ((corn_num
    :reader corn_num
    :initarg :corn_num
    :type cl:fixnum
    :initform 0)
   (cucumber_num
    :reader cucumber_num
    :initarg :cucumber_num
    :type cl:fixnum
    :initform 0)
   (rice_num
    :reader rice_num
    :initarg :rice_num
    :type cl:fixnum
    :initform 0)
   (wheat_num
    :reader wheat_num
    :initarg :wheat_num
    :type cl:fixnum
    :initform 0)
   (corn_cut_num
    :reader corn_cut_num
    :initarg :corn_cut_num
    :type cl:fixnum
    :initform 0)
   (cucumber_cut_num
    :reader cucumber_cut_num
    :initarg :cucumber_cut_num
    :type cl:fixnum
    :initform 0)
   (rice_cut_num
    :reader rice_cut_num
    :initarg :rice_cut_num
    :type cl:fixnum
    :initform 0)
   (wheat_cut_num
    :reader wheat_cut_num
    :initarg :wheat_cut_num
    :type cl:fixnum
    :initform 0))
)

(cl:defclass classes (<classes>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <classes>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'classes)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name darknet_ros_msgs-msg:<classes> is deprecated: use darknet_ros_msgs-msg:classes instead.")))

(cl:ensure-generic-function 'corn_num-val :lambda-list '(m))
(cl:defmethod corn_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:corn_num-val is deprecated.  Use darknet_ros_msgs-msg:corn_num instead.")
  (corn_num m))

(cl:ensure-generic-function 'cucumber_num-val :lambda-list '(m))
(cl:defmethod cucumber_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:cucumber_num-val is deprecated.  Use darknet_ros_msgs-msg:cucumber_num instead.")
  (cucumber_num m))

(cl:ensure-generic-function 'rice_num-val :lambda-list '(m))
(cl:defmethod rice_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:rice_num-val is deprecated.  Use darknet_ros_msgs-msg:rice_num instead.")
  (rice_num m))

(cl:ensure-generic-function 'wheat_num-val :lambda-list '(m))
(cl:defmethod wheat_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:wheat_num-val is deprecated.  Use darknet_ros_msgs-msg:wheat_num instead.")
  (wheat_num m))

(cl:ensure-generic-function 'corn_cut_num-val :lambda-list '(m))
(cl:defmethod corn_cut_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:corn_cut_num-val is deprecated.  Use darknet_ros_msgs-msg:corn_cut_num instead.")
  (corn_cut_num m))

(cl:ensure-generic-function 'cucumber_cut_num-val :lambda-list '(m))
(cl:defmethod cucumber_cut_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:cucumber_cut_num-val is deprecated.  Use darknet_ros_msgs-msg:cucumber_cut_num instead.")
  (cucumber_cut_num m))

(cl:ensure-generic-function 'rice_cut_num-val :lambda-list '(m))
(cl:defmethod rice_cut_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:rice_cut_num-val is deprecated.  Use darknet_ros_msgs-msg:rice_cut_num instead.")
  (rice_cut_num m))

(cl:ensure-generic-function 'wheat_cut_num-val :lambda-list '(m))
(cl:defmethod wheat_cut_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:wheat_cut_num-val is deprecated.  Use darknet_ros_msgs-msg:wheat_cut_num instead.")
  (wheat_cut_num m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <classes>) ostream)
  "Serializes a message object of type '<classes>"
  (cl:let* ((signed (cl:slot-value msg 'corn_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'cucumber_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rice_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'wheat_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'corn_cut_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'cucumber_cut_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rice_cut_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'wheat_cut_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <classes>) istream)
  "Deserializes a message object of type '<classes>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'corn_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cucumber_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rice_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'wheat_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'corn_cut_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cucumber_cut_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rice_cut_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'wheat_cut_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<classes>)))
  "Returns string type for a message object of type '<classes>"
  "darknet_ros_msgs/classes")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'classes)))
  "Returns string type for a message object of type 'classes"
  "darknet_ros_msgs/classes")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<classes>)))
  "Returns md5sum for a message object of type '<classes>"
  "5de667e5e14606f356e3c7c2b8f9d715")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'classes)))
  "Returns md5sum for a message object of type 'classes"
  "5de667e5e14606f356e3c7c2b8f9d715")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<classes>)))
  "Returns full string definition for message of type '<classes>"
  (cl:format cl:nil "int16 corn_num  ~%int16 cucumber_num~%int16 rice_num~%int16 wheat_num~%int16 corn_cut_num  ~%int16 cucumber_cut_num~%int16 rice_cut_num~%int16 wheat_cut_num~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'classes)))
  "Returns full string definition for message of type 'classes"
  (cl:format cl:nil "int16 corn_num  ~%int16 cucumber_num~%int16 rice_num~%int16 wheat_num~%int16 corn_cut_num  ~%int16 cucumber_cut_num~%int16 rice_cut_num~%int16 wheat_cut_num~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <classes>))
  (cl:+ 0
     2
     2
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <classes>))
  "Converts a ROS message object to a list"
  (cl:list 'classes
    (cl:cons ':corn_num (corn_num msg))
    (cl:cons ':cucumber_num (cucumber_num msg))
    (cl:cons ':rice_num (rice_num msg))
    (cl:cons ':wheat_num (wheat_num msg))
    (cl:cons ':corn_cut_num (corn_cut_num msg))
    (cl:cons ':cucumber_cut_num (cucumber_cut_num msg))
    (cl:cons ':rice_cut_num (rice_cut_num msg))
    (cl:cons ':wheat_cut_num (wheat_cut_num msg))
))
