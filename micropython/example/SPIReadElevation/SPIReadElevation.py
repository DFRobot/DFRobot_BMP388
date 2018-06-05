# Connect bmp388 and esp32 via SPI.
# Connect CSB pin to IO26/D3 of esp32
# Download bmp388.py and downloadAndRun this demo.

import bmp388
from machine import Pin,SPI
import time

# Chip selection pin D3/pin26
D3 = 26

# Create SPI object
spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

# Set the chip selection pin to output.
cs = Pin(D3,Pin.OUT)

# Create a bmp388 object to communicate with SPI.
bmp388 = bmp388.DFRobot_BMP388_SPI(spi,cs)
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