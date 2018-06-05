 /*!
  * file I2CReadElevation.ino
  * 
  * Connect BMP388 to IIC interface of Arduino, download the program.
  * Elevation is calculated based on temperature and sea level pressure.
  * The example can count an approximate elevation.
  *
  * @n Open the serial monitor, check the elevation.
  *
  * Copyright   [DFRobot](http://www.dfrobot.com), 2016
  * Copyright   GNU Lesser General Public License
  *
  * version  V0.1
  * date  2018-5-29
  */
#include "DFRobot_BMP388.h"
#include "Wire.h"
#include "SPI.h"
#include "math.h"
#include "bmp3_defs.h"

/*If there is no need to calibrate elevation, comment this line*/
#define CALIBRATE_Elevation

/*Create a bmp388 object to communicate with IIC.*/
DFRobot_BMP388 bmp388;

float seaLevel;

void setup(){
  /* Initialize the serial port*/
  Serial.begin(9600);
  /* Initialize bmp388*/
  bmp388.begin();
  /*You can use an accurate altitude to calibrate sea level air pressure. 
   *And then use this calibrated sea level pressure as a reference to obtain the calibrated altitude.
   *In this case,525.0m is chendu accurate altitude.
   */
  delay(100);
  seaLevel = bmp388.readSeaLevel(525.0);
  Serial.print("seaLevel : ");
  Serial.print(seaLevel);
  Serial.println(" Pa");
}

void loop(){
  #ifdef CALIBRATE_Elevation
  /* Read the calibrated elevation */
  float elevation = bmp388.readCalibratedElevation(seaLevel);
  Serial.print("calibrate Elevation : ");
  Serial.print(elevation);
  Serial.println(" m");
  #else
  /* Read the elevation */
  float elevation = bmp388.readElevation();
  Serial.print("Elevation : ");
  Serial.print(elevation);
  Serial.println(" m");
  #endif
  delay(100);
}

