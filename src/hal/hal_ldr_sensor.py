import spidev

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# Read MCP3008 data
def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Convert data to voltage level
def convert_volts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

# Convert voltage to light level (as a proxy for fuel level)
def get_light_level(channel):
    data = read_channel(channel)
    volts = convert_volts(data, 2)
    return volts
