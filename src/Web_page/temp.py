import time
import RPi.GPIO as GPIO
import dht11

def init():
    GPIO.setmode(GPIO.BCM)
    global dht11_inst

    dht11_inst = dht11.DHT11(pin=21)  # read data using pin 21

def read_temp_humidity():

    global dht11_inst

    ret = [-100, -100]

    result = dht11_inst.read()

    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)

        ret= result.temperature

    return ret

def main():
        init()
        read_temp_humidity()
    

if __name__ == '__main__':
    main()