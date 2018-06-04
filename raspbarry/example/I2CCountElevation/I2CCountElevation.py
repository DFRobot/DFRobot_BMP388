# Connect bmp388 and esp32 via I2C.
#
# Elevation is calculated based on temperature and sea level pressure
# The example can count an approximate elevation.
# Formula:
# P=P0*(1-H/44300)^5.256
#
# Warning:
#   This demo only supports python3.
#   Run this demo: python3 I2CCountElevation.py.
#
# connect:
#   raspberry       bmp388
#   3.3v(1)         VCC
#   GND(6)          GND
#   SCL(5)          SCL
#   SDA(3)          SDA

import bmp388
import time

# Create a bmp388 object to communicate with I2C.
bmp388 = bmp388.DFRobot_BMP388_I2C()

# Read pressure and count elevation.
while 1:
  pressure = bmp388.readPressure();
  elevation = round(44330 * (1.0 - pow(pressure / 101325, 0.1903)),2)
  print("elevation : %s m" %elevation)
  time.sleep(0.5)
