def buzzer_on():
    global theft_detected
    import time
    from time import sleep
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output
    GPIO.output(18, GPIO.HIGH)
    theft_detected = True
    time.sleep(5)  # Buzzer active for 5 seconds
    GPIO.output(18, GPIO.LOW)
    return theft_detected



