 /*!
  * file SPICountElevation.ino
  * 
  * Connect BMP388 to SPI interface of Arduino and connect CSB pin to pin3 of Arduino,
  * download the program.
  *
  * Elevation is calculated based on temperature and sea level pressure.
  * The example can count an approximate elevation.
  *
  * Formula:
  * P=P0*(1-H/44300)^5.256
  * @n pen the serial monitor, check the elevation.
  *
  * Copyright   [DFRobot](http://www.dfrobot.com), 2016
  * Copyright   GNU Lesser General Public License
  *
  * version  V0.1
  * date  2018-5-29
  */
#include "DFRobot_BMP388.h"
#include "SPI.h"
#include "Wire.h"
#include "math.h"
#include "bmp3_defs.h"

/* Create a bmp388 object of SPI interface and the SPI chip selection pin is 3 */
DFRobot_BMP388 bmp388(3);

void setup(){
  /*Initialize the serial port*/
  Serial.begin(9600);
  /*Initialize bmp388*/
  bmp388.begin();
}

void loop(){
  /*Read the atmospheric pressure, count the elevation*/
  float pressure = bmp388.readPressure();
  float elevation = 44330 * (1.0 - pow(pressure / 101325, 0.1903));
  Serial.print("Elevation : ");
  Serial.print(elevation);
  Serial.println(" m");
  delay(100);
}


