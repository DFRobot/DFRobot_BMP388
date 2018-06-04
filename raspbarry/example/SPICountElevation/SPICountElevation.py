# Connect bmp388 and esp32 via SPI.
#
# Elevation is calculated based on temperature and sea level pressure
# The example can count an approximate elevation.
# Formula:
# P=P0*(1-H/44300)^5.256
#
# Warning:
#   This demo only supports python3.
#   Run this demo : python3 SPICountElevation.py.
#
# connect:
#   raspberry       bmp388
#   CS  (15)        CSB
#   3.3v(17)        VCC
#   MOSI(19)        SDI
#   MISO(21)        SDO
#   SCLK(23)        SCK
#   GND (25)        GND

import bmp388
import time

# Define chip selection pins
cs = 22

# Create a bmp388 object to communicate with SPI.
bmp388 = bmp388.DFRobot_BMP388_SPI(cs)

# Read pressure and count elevation.
while 1:
  pressure = bmp388.readPressure()
  elevation = round(44330 * (1.0 - pow(pressure / 101325, 0.1903)),2)
  print("Elevation : %s m" %elevation)  
  time.sleep(0.5)
