
"use strict";

let GetSensorTF = require('./GetSensorTF.js')
let GetBatteryInfo = require('./GetBatteryInfo.js')
let SetLEDMode = require('./SetLEDMode.js')
let SetSensorTF = require('./SetSensorTF.js')
let SetMaxVel = require('./SetMaxVel.js')
let GetMaxVel = require('./GetMaxVel.js')

module.exports = {
  GetSensorTF: GetSensorTF,
  GetBatteryInfo: GetBatteryInfo,
  SetLEDMode: SetLEDMode,
  SetSensorTF: SetSensorTF,
  SetMaxVel: SetMaxVel,
  GetMaxVel: GetMaxVel,
};
