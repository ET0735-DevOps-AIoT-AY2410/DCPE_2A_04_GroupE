def switch_Status():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    ret = 1

    if GPIO.input(22):
        ret = 0

    return ret