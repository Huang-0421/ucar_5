// Generated by gencpp from file sound_play/SoundRequestActionGoal.msg
// DO NOT EDIT!


#ifndef SOUND_PLAY_MESSAGE_SOUNDREQUESTACTIONGOAL_H
#define SOUND_PLAY_MESSAGE_SOUNDREQUESTACTIONGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <actionlib_msgs/GoalID.h>
#include <sound_play/SoundRequestGoal.h>

namespace sound_play
{
template <class ContainerAllocator>
struct SoundRequestActionGoal_
{
  typedef SoundRequestActionGoal_<ContainerAllocator> Type;

  SoundRequestActionGoal_()
    : header()
    , goal_id()
    , goal()  {
    }
  SoundRequestActionGoal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , goal_id(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
  _goal_id_type goal_id;

   typedef  ::sound_play::SoundRequestGoal_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct SoundRequestActionGoal_

typedef ::sound_play::SoundRequestActionGoal_<std::allocator<void> > SoundRequestActionGoal;

typedef boost::shared_ptr< ::sound_play::SoundRequestActionGoal > SoundRequestActionGoalPtr;
typedef boost::shared_ptr< ::sound_play::SoundRequestActionGoal const> SoundRequestActionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sound_play::SoundRequestActionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sound_play::SoundRequestActionGoal_<ContainerAllocator1> & lhs, const ::sound_play::SoundRequestActionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.goal_id == rhs.goal_id &&
    lhs.goal == rhs.goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sound_play::SoundRequestActionGoal_<ContainerAllocator1> & lhs, const ::sound_play::SoundRequestActionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sound_play

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7ff89ce2a5f72c86a28be8ae82658bf8";
  }

  static const char* value(const ::sound_play::SoundRequestActionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7ff89ce2a5f72c86ULL;
  static const uint64_t static_value2 = 0xa28be8ae82658bf8ULL;
};

template<class ContainerAllocator>
struct DataType< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sound_play/SoundRequestActionGoal";
  }

  static const char* value(const ::sound_play::SoundRequestActionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"SoundRequestGoal goal\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: sound_play/SoundRequestGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"SoundRequest sound_request\n"
"\n"
"================================================================================\n"
"MSG: sound_play/SoundRequest\n"
"# IMPORTANT: You should never have to generate this message yourself.\n"
"# Use the sound_play::SoundClient C++ helper or the\n"
"# sound_play.libsoundplay.SoundClient Python helper.\n"
"\n"
"# Sounds\n"
"int8 BACKINGUP = 1\n"
"int8 NEEDS_UNPLUGGING = 2\n"
"int8 NEEDS_PLUGGING = 3\n"
"int8 NEEDS_UNPLUGGING_BADLY = 4\n"
"int8 NEEDS_PLUGGING_BADLY = 5\n"
"\n"
"# Sound identifiers that have special meaning\n"
"int8 ALL = -1 # Only legal with PLAY_STOP\n"
"int8 PLAY_FILE = -2\n"
"int8 SAY = -3\n"
"\n"
"int8 sound # Selects which sound to play (see above)\n"
"\n"
"# Commands\n"
"int8 PLAY_STOP = 0 # Stop this sound from playing\n"
"int8 PLAY_ONCE = 1 # Play the sound once\n"
"int8 PLAY_START = 2 # Play the sound in a loop until a stop request occurs\n"
"\n"
"int8 command # Indicates what to do with the sound\n"
"\n"
"# Volume at which to play the sound, with 0 as mute and 1.0 as 100%.\n"
"float32 volume\n"
"\n"
"string arg # file name or text to say\n"
"string arg2 # other arguments\n"
;
  }

  static const char* value(const ::sound_play::SoundRequestActionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.goal_id);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SoundRequestActionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sound_play::SoundRequestActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sound_play::SoundRequestActionGoal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
    s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::sound_play::SoundRequestGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SOUND_PLAY_MESSAGE_SOUNDREQUESTACTIONGOAL_H
