import time
import picoexplorer as explorer
from machine import Pin, I2C
from bmp280 import *

bus = I2C(0, scl=Pin(21), sda=Pin(20))
bmp = BMP280(bus)
bmp.use_case(BMP280_CASE_WEATHER)
bmp.oversample(BMP280_OS_HIGH)
bmp.temp_os = BMP280_TEMP_OS_8
bmp.press_os = BMP280_PRES_OS_4
bmp.standby = BMP280_STANDBY_250
bmp.iir = BMP280_IIR_FILTER_2
bmp.spi3w = BMP280_SPI3W_ON
bmp.power_mode = BMP280_POWER_NORMAL

width = explorer.get_width()
height = explorer.get_height()

display_buffer = bytearray(width * height * 2)
explorer.init(display_buffer)

while True:
    temperature = str(bmp.temperature)
    explorer.set_pen(0, 102, 204)    
    explorer.clear()
    
    explorer.set_pen(255, 255, 255)
    explorer.text(str(temperature), 20, 130, 200, 4)
    
    explorer.update()
    time.sleep(1)