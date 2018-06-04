# Connect bmp388 and esp32 via IIC.
# Download bmp388.py and downloadAndRun this demo.

import bmp388
from machine import Pin,I2C
import time

# Create I2C object
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

# Create a bmp388 object to communicate with IIC.
bmp388 = bmp388.DFRobot_BMP388_I2C(i2c)

# Read pressure and count elevation.
while 1:
  pressure = bmp388.readPressure();
  elevation = round(44330 * (1.0 - pow(pressure / 101325, 0.1903)),2)
  print("elevation : %s m" %elevation)
  time.sleep(0.5)
