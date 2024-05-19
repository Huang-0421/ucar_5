// Generated by gencpp from file ucar_controller/GetMaxVel.msg
// DO NOT EDIT!


#ifndef UCAR_CONTROLLER_MESSAGE_GETMAXVEL_H
#define UCAR_CONTROLLER_MESSAGE_GETMAXVEL_H

#include <ros/service_traits.h>


#include <ucar_controller/GetMaxVelRequest.h>
#include <ucar_controller/GetMaxVelResponse.h>


namespace ucar_controller
{

struct GetMaxVel
{

typedef GetMaxVelRequest Request;
typedef GetMaxVelResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetMaxVel
} // namespace ucar_controller


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ucar_controller::GetMaxVel > {
  static const char* value()
  {
    return "c3d002ed0ab158592aaa625149bc3810";
  }

  static const char* value(const ::ucar_controller::GetMaxVel&) { return value(); }
};

template<>
struct DataType< ::ucar_controller::GetMaxVel > {
  static const char* value()
  {
    return "ucar_controller/GetMaxVel";
  }

  static const char* value(const ::ucar_controller::GetMaxVel&) { return value(); }
};


// service_traits::MD5Sum< ::ucar_controller::GetMaxVelRequest> should match
// service_traits::MD5Sum< ::ucar_controller::GetMaxVel >
template<>
struct MD5Sum< ::ucar_controller::GetMaxVelRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ucar_controller::GetMaxVel >::value();
  }
  static const char* value(const ::ucar_controller::GetMaxVelRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ucar_controller::GetMaxVelRequest> should match
// service_traits::DataType< ::ucar_controller::GetMaxVel >
template<>
struct DataType< ::ucar_controller::GetMaxVelRequest>
{
  static const char* value()
  {
    return DataType< ::ucar_controller::GetMaxVel >::value();
  }
  static const char* value(const ::ucar_controller::GetMaxVelRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ucar_controller::GetMaxVelResponse> should match
// service_traits::MD5Sum< ::ucar_controller::GetMaxVel >
template<>
struct MD5Sum< ::ucar_controller::GetMaxVelResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ucar_controller::GetMaxVel >::value();
  }
  static const char* value(const ::ucar_controller::GetMaxVelResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ucar_controller::GetMaxVelResponse> should match
// service_traits::DataType< ::ucar_controller::GetMaxVel >
template<>
struct DataType< ::ucar_controller::GetMaxVelResponse>
{
  static const char* value()
  {
    return DataType< ::ucar_controller::GetMaxVel >::value();
  }
  static const char* value(const ::ucar_controller::GetMaxVelResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UCAR_CONTROLLER_MESSAGE_GETMAXVEL_H
