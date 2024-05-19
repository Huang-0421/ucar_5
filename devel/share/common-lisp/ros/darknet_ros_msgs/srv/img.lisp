; Auto-generated. Do not edit!


(cl:in-package darknet_ros_msgs-srv)


;//! \htmlinclude img-request.msg.html

(cl:defclass <img-request> (roslisp-msg-protocol:ros-message)
  ((img
    :reader img
    :initarg :img
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass img-request (<img-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <img-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'img-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name darknet_ros_msgs-srv:<img-request> is deprecated: use darknet_ros_msgs-srv:img-request instead.")))

(cl:ensure-generic-function 'img-val :lambda-list '(m))
(cl:defmethod img-val ((m <img-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-srv:img-val is deprecated.  Use darknet_ros_msgs-srv:img instead.")
  (img m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <img-request>) ostream)
  "Serializes a message object of type '<img-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'img) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <img-request>) istream)
  "Deserializes a message object of type '<img-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'img) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<img-request>)))
  "Returns string type for a service object of type '<img-request>"
  "darknet_ros_msgs/imgRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'img-request)))
  "Returns string type for a service object of type 'img-request"
  "darknet_ros_msgs/imgRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<img-request>)))
  "Returns md5sum for a message object of type '<img-request>"
  "b243c66d754037e494b8467471231d86")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'img-request)))
  "Returns md5sum for a message object of type 'img-request"
  "b243c66d754037e494b8467471231d86")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<img-request>)))
  "Returns full string definition for message of type '<img-request>"
  (cl:format cl:nil "sensor_msgs/Image img~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'img-request)))
  "Returns full string definition for message of type 'img-request"
  (cl:format cl:nil "sensor_msgs/Image img~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <img-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'img))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <img-request>))
  "Converts a ROS message object to a list"
  (cl:list 'img-request
    (cl:cons ':img (img msg))
))
;//! \htmlinclude img-response.msg.html

(cl:defclass <img-response> (roslisp-msg-protocol:ros-message)
  ((gh
    :reader gh
    :initarg :gh
    :type darknet_ros_msgs-msg:classes
    :initform (cl:make-instance 'darknet_ros_msgs-msg:classes)))
)

(cl:defclass img-response (<img-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <img-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'img-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name darknet_ros_msgs-srv:<img-response> is deprecated: use darknet_ros_msgs-srv:img-response instead.")))

(cl:ensure-generic-function 'gh-val :lambda-list '(m))
(cl:defmethod gh-val ((m <img-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-srv:gh-val is deprecated.  Use darknet_ros_msgs-srv:gh instead.")
  (gh m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <img-response>) ostream)
  "Serializes a message object of type '<img-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gh) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <img-response>) istream)
  "Deserializes a message object of type '<img-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gh) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<img-response>)))
  "Returns string type for a service object of type '<img-response>"
  "darknet_ros_msgs/imgResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'img-response)))
  "Returns string type for a service object of type 'img-response"
  "darknet_ros_msgs/imgResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<img-response>)))
  "Returns md5sum for a message object of type '<img-response>"
  "b243c66d754037e494b8467471231d86")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'img-response)))
  "Returns md5sum for a message object of type 'img-response"
  "b243c66d754037e494b8467471231d86")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<img-response>)))
  "Returns full string definition for message of type '<img-response>"
  (cl:format cl:nil "classes gh~%~%================================================================================~%MSG: darknet_ros_msgs/classes~%int16 corn_num  ~%int16 cucumber_num~%int16 rice_num~%int16 wheat_num~%int16 corn_cut_num  ~%int16 cucumber_cut_num~%int16 rice_cut_num~%int16 wheat_cut_num~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'img-response)))
  "Returns full string definition for message of type 'img-response"
  (cl:format cl:nil "classes gh~%~%================================================================================~%MSG: darknet_ros_msgs/classes~%int16 corn_num  ~%int16 cucumber_num~%int16 rice_num~%int16 wheat_num~%int16 corn_cut_num  ~%int16 cucumber_cut_num~%int16 rice_cut_num~%int16 wheat_cut_num~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <img-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gh))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <img-response>))
  "Converts a ROS message object to a list"
  (cl:list 'img-response
    (cl:cons ':gh (gh msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'img)))
  'img-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'img)))
  'img-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'img)))
  "Returns string type for a service object of type '<img>"
  "darknet_ros_msgs/img")