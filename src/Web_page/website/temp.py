


def read_temp_humidity():
    import time

    import RPi.GPIO as GPIO

    from website import dht11
    GPIO.setmode(GPIO.BCM)
    global dht11_inst

    dht11_inst = dht11.DHT11(pin=21)  # read data using pin 21

    ret = [-100, -100]

    result = dht11_inst.read()

    if result.is_valid():
        #print("Temperature: %-3.1f C" % result.temperature)
        #print("Humidity: %-3.1f %%" % result.humidity)

        ret = result.temperature

    return ret