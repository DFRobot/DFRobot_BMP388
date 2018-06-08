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
  /*Initialize bmp388*/
  if(bmp388.begin()){
    Serial.println("Initialize error!");
    while(1);
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