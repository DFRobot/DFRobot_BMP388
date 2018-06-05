# Connect bmp388 and esp32 via I2C.
# Download bmp388.py and downloadAndRun this demo.

import bmp388
from machine import Pin,I2C
import time

# Create I2C object
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

# Create a bmp388 object to communicate with I2C.
bmp388 = bmp388.DFRobot_BMP388_I2C(i2c)
time.sleep(0.5)

# You can use an accurate altitude to calibrate sea level air pressure. 
# And then use this calibrated sea level pressure as a reference to obtain the calibrated altitude.
# In this case,525.0m is chendu accurate altitude.
seaLevel = bmp388.readSeaLevel(525.0);
print("seaLevel : %s Pa" %seaLevel)

# If there is no need to calibrate elevation, calibrated_elevation = False
calibrated_elevation = True

while 1:
  if(calibrated_elevation):
    # Read the calibrated elevation 
    elevation = bmp388.readCalibratedElevation(seaLevel)
    print("calibrate Elevation : %s m" %elevation)
  else:
    # Read the elevation 
    elevation = bmp388.readElevation();
    print("Elevation : %s m" %elevation)
  time.sleep(0.5)
