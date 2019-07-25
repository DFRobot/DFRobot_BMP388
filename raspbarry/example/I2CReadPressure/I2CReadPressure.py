# Connect bmp388 and esp32 via I2C.
#
# Warning:
#   This demo only supports python3.
#   Run this demo : python3 I2CReadPressure.py
#
# connect:
#   raspberry(pin)       bmp388
#   3.3v(1)              VCC
#   GND(6)               GND
#   SCL(5)               SCL
#   SDA(3)               SDA
# BMP388_I2C_ADDR = 0x76: pin SDO is low
# BMP388_I2C_ADDR = 0x77: pin SDO is high

import bmp388
import time

# Create a bmp388 object to communicate with I2C.
bmp388 = bmp388.DFRobot_BMP388_I2C(0x77)

# Read pressure and print it.
while 1:
  pres = bmp388.readPressure()
  print("Pressure : %s Pa" %pres)
  time.sleep(0.5)