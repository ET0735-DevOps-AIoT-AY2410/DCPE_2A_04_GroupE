import time
import requests
import spidev

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000


def get_fuel_level(channel):
    places = 2

    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]

    light_intensity = (data * 3.3) / float(1023)
    light_intensity = round(light_intensity, places)

    if light_intensity > 3 :
        return "High"
    elif 1 <= light_intensity < 3:
        return "Medium"
    else:
        return "Low"