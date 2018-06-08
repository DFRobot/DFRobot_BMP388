# Connect bmp388 and esp32 via IIC/SPI.
# Connect INT pin and io27
# Download bmp388.py and downloadAndRun this demo.

import bmp388
from machine import Pin,I2C,SPI
import time

# If 1, connect BMP388 to SPI interface of esp32, else connect I2C interface
if 0:
  # Create I2C object
  i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
  
  # Create a bmp388 object to communicate with IIC.
  bmp388 = bmp388.DFRobot_BMP388_I2C(i2c)
else:
  # Chip selection pin D3/pin26
  D3 = 26

  # Create SPI object
  spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

  # Set the chip selection pin to output.
  cs = Pin(D3,Pin.OUT)

  # Create a bmp388 object to communicate with SPI.
  bmp388 = bmp388.DFRobot_BMP388_SPI(spi,cs)

INT = Pin(27,Pin.IN) 
# Read pressure and print it.
while 1:
  if(bmp388.INTReadPin(INT)):
    temp = bmp388.readTemperature()
    print("Temperature : %s C" %temp)
    pres = bmp388.readPressure()
    print("Pressure : %s Pa" %pres)
  time.sleep(0.5)