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
time.sleep(0.5)

# You can use an accurate altitude to calibrate sea level air pressure. 
# And then use this calibrated sea level pressure as a reference to obtain the calibrated altitude.
# In this case,525.0m is chendu accurate altitude.
seaLevel = bmp388.readSeaLevel(525.0);
print("seaLevel : %s Pa" %seaLevel)

# If there is no need to calibrate elevation, calibrated_elevation = False
calibrated_elevation = True

# Read pressure and count elevation.
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
