/*!
 * @file DFRobot_BMP388_I2C.h
 * @brief DFRobot's DFRobot_BMP388
 * @n DFRobot's Temperature, Pressure and Approx altitude
 *
 * @copyright	[DFRobot](http://www.dfrobot.com), 2016
 * @copyright	GNU Lesser General Public License
 *
 * @author [yuhao](yuhao.lu@dfrobot.com)
 * @version  V1.0
 * @date  2018-5-29
 */
#ifndef DFRobot_BMP388_I2C_H
#define DFRobot_BMP388_I2C_H

#include "DFRobot_BMP388.h"
#include "bmp3_defs.h"
#include "Arduino.h"
#include "Wire.h"
#include "SPI.h"

class DFRobot_BMP388_I2C : public DFRobot_BMP388
{
  public:
    DFRobot_BMP388_I2C();
};

#endif