

def main():
    import RPi.GPIO as GPIO #import RPi.GPIO module
    import time
    from time import sleep
    

    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT) #set GPIO 23 as output


    GPIO.output(23,1)
    sleep(5)
    GPIO.output(23,0)

    GPIO.cleanup()
