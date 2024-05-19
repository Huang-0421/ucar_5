// Auto-generated. Do not edit!

// (in-package darknet_ros_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class classes {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.corn_num = null;
      this.cucumber_num = null;
      this.rice_num = null;
      this.wheat_num = null;
      this.corn_cut_num = null;
      this.cucumber_cut_num = null;
      this.rice_cut_num = null;
      this.wheat_cut_num = null;
    }
    else {
      if (initObj.hasOwnProperty('corn_num')) {
        this.corn_num = initObj.corn_num
      }
      else {
        this.corn_num = 0;
      }
      if (initObj.hasOwnProperty('cucumber_num')) {
        this.cucumber_num = initObj.cucumber_num
      }
      else {
        this.cucumber_num = 0;
      }
      if (initObj.hasOwnProperty('rice_num')) {
        this.rice_num = initObj.rice_num
      }
      else {
        this.rice_num = 0;
      }
      if (initObj.hasOwnProperty('wheat_num')) {
        this.wheat_num = initObj.wheat_num
      }
      else {
        this.wheat_num = 0;
      }
      if (initObj.hasOwnProperty('corn_cut_num')) {
        this.corn_cut_num = initObj.corn_cut_num
      }
      else {
        this.corn_cut_num = 0;
      }
      if (initObj.hasOwnProperty('cucumber_cut_num')) {
        this.cucumber_cut_num = initObj.cucumber_cut_num
      }
      else {
        this.cucumber_cut_num = 0;
      }
      if (initObj.hasOwnProperty('rice_cut_num')) {
        this.rice_cut_num = initObj.rice_cut_num
      }
      else {
        this.rice_cut_num = 0;
      }
      if (initObj.hasOwnProperty('wheat_cut_num')) {
        this.wheat_cut_num = initObj.wheat_cut_num
      }
      else {
        this.wheat_cut_num = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type classes
    // Serialize message field [corn_num]
    bufferOffset = _serializer.int16(obj.corn_num, buffer, bufferOffset);
    // Serialize message field [cucumber_num]
    bufferOffset = _serializer.int16(obj.cucumber_num, buffer, bufferOffset);
    // Serialize message field [rice_num]
    bufferOffset = _serializer.int16(obj.rice_num, buffer, bufferOffset);
    // Serialize message field [wheat_num]
    bufferOffset = _serializer.int16(obj.wheat_num, buffer, bufferOffset);
    // Serialize message field [corn_cut_num]
    bufferOffset = _serializer.int16(obj.corn_cut_num, buffer, bufferOffset);
    // Serialize message field [cucumber_cut_num]
    bufferOffset = _serializer.int16(obj.cucumber_cut_num, buffer, bufferOffset);
    // Serialize message field [rice_cut_num]
    bufferOffset = _serializer.int16(obj.rice_cut_num, buffer, bufferOffset);
    // Serialize message field [wheat_cut_num]
    bufferOffset = _serializer.int16(obj.wheat_cut_num, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type classes
    let len;
    let data = new classes(null);
    // Deserialize message field [corn_num]
    data.corn_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [cucumber_num]
    data.cucumber_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [rice_num]
    data.rice_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [wheat_num]
    data.wheat_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [corn_cut_num]
    data.corn_cut_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [cucumber_cut_num]
    data.cucumber_cut_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [rice_cut_num]
    data.rice_cut_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [wheat_cut_num]
    data.wheat_cut_num = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'darknet_ros_msgs/classes';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5de667e5e14606f356e3c7c2b8f9d715';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 corn_num  
    int16 cucumber_num
    int16 rice_num
    int16 wheat_num
    int16 corn_cut_num  
    int16 cucumber_cut_num
    int16 rice_cut_num
    int16 wheat_cut_num
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new classes(null);
    if (msg.corn_num !== undefined) {
      resolved.corn_num = msg.corn_num;
    }
    else {
      resolved.corn_num = 0
    }

    if (msg.cucumber_num !== undefined) {
      resolved.cucumber_num = msg.cucumber_num;
    }
    else {
      resolved.cucumber_num = 0
    }

    if (msg.rice_num !== undefined) {
      resolved.rice_num = msg.rice_num;
    }
    else {
      resolved.rice_num = 0
    }

    if (msg.wheat_num !== undefined) {
      resolved.wheat_num = msg.wheat_num;
    }
    else {
      resolved.wheat_num = 0
    }

    if (msg.corn_cut_num !== undefined) {
      resolved.corn_cut_num = msg.corn_cut_num;
    }
    else {
      resolved.corn_cut_num = 0
    }

    if (msg.cucumber_cut_num !== undefined) {
      resolved.cucumber_cut_num = msg.cucumber_cut_num;
    }
    else {
      resolved.cucumber_cut_num = 0
    }

    if (msg.rice_cut_num !== undefined) {
      resolved.rice_cut_num = msg.rice_cut_num;
    }
    else {
      resolved.rice_cut_num = 0
    }

    if (msg.wheat_cut_num !== undefined) {
      resolved.wheat_cut_num = msg.wheat_cut_num;
    }
    else {
      resolved.wheat_cut_num = 0
    }

    return resolved;
    }
};

module.exports = classes;
