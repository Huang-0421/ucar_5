// Generated by gencpp from file ucar_controller/SetSensorTF.msg
// DO NOT EDIT!


#ifndef UCAR_CONTROLLER_MESSAGE_SETSENSORTF_H
#define UCAR_CONTROLLER_MESSAGE_SETSENSORTF_H

#include <ros/service_traits.h>


#include <ucar_controller/SetSensorTFRequest.h>
#include <ucar_controller/SetSensorTFResponse.h>


namespace ucar_controller
{

struct SetSensorTF
{

typedef SetSensorTFRequest Request;
typedef SetSensorTFResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetSensorTF
} // namespace ucar_controller


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ucar_controller::SetSensorTF > {
  static const char* value()
  {
    return "a6cc398312db9fcdb32a0a56126c3fa5";
  }

  static const char* value(const ::ucar_controller::SetSensorTF&) { return value(); }
};

template<>
struct DataType< ::ucar_controller::SetSensorTF > {
  static const char* value()
  {
    return "ucar_controller/SetSensorTF";
  }

  static const char* value(const ::ucar_controller::SetSensorTF&) { return value(); }
};


// service_traits::MD5Sum< ::ucar_controller::SetSensorTFRequest> should match
// service_traits::MD5Sum< ::ucar_controller::SetSensorTF >
template<>
struct MD5Sum< ::ucar_controller::SetSensorTFRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ucar_controller::SetSensorTF >::value();
  }
  static const char* value(const ::ucar_controller::SetSensorTFRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ucar_controller::SetSensorTFRequest> should match
// service_traits::DataType< ::ucar_controller::SetSensorTF >
template<>
struct DataType< ::ucar_controller::SetSensorTFRequest>
{
  static const char* value()
  {
    return DataType< ::ucar_controller::SetSensorTF >::value();
  }
  static const char* value(const ::ucar_controller::SetSensorTFRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ucar_controller::SetSensorTFResponse> should match
// service_traits::MD5Sum< ::ucar_controller::SetSensorTF >
template<>
struct MD5Sum< ::ucar_controller::SetSensorTFResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ucar_controller::SetSensorTF >::value();
  }
  static const char* value(const ::ucar_controller::SetSensorTFResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ucar_controller::SetSensorTFResponse> should match
// service_traits::DataType< ::ucar_controller::SetSensorTF >
template<>
struct DataType< ::ucar_controller::SetSensorTFResponse>
{
  static const char* value()
  {
    return DataType< ::ucar_controller::SetSensorTF >::value();
  }
  static const char* value(const ::ucar_controller::SetSensorTFResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UCAR_CONTROLLER_MESSAGE_SETSENSORTF_H
