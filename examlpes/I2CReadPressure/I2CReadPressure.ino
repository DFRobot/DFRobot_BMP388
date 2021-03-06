 /*!
  * file I2CReadPressure.ino
  * 
  * Connect BMP388 to IIC interface of Arduino, download the program.
  * @n Open serial monitor, the atmospheric pressure could be checked. 
  *
  * Copyright   [DFRobot](http://www.dfrobot.com), 2016
  * Copyright   GNU Lesser General Public License
  *
  * version  V0.1
  * date  2018-5-29
  */
#include "DFRobot_BMP388_I2C.h"
#include "DFRobot_BMP388.h"
#include "Wire.h"
#include "SPI.h"
#include "bmp3_defs.h"

/* Create a bmp388 object to communicate with IIC.*/
DFRobot_BMP388_I2C bmp388;
void setup(){
  /*Initialize the serial port*/
  Serial.begin(9600);
  /* 
   * @brief Set bmp388 IIC address
   * @param BMP3_I2C_ADDR_PRIM: pin SDO is low
   *        BMP3_I2C_ADDR_SEC: pin SDO is high
   */
  bmp388.set_iic_addr(BMP3_I2C_ADDR_SEC);
  /*Initialize bmp388*/
  while(bmp388.begin()){
    Serial.println("Initialize error!");
    delay(1000);
  }
}

void loop(){
  /* Read the atmospheric pressure, print data via serial port.*/
  float Pressure = bmp388.readPressure();
  Serial.print("Pressure : ");
  Serial.print(Pressure);
  Serial.println(" Pa");
  delay(100);
}