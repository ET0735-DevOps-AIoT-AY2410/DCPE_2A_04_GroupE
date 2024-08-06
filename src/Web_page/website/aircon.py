

def main(temperature):
    import RPi.GPIO as GPIO
    import time
    from time import sleep
    LED_PIN = 24
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    pwm = GPIO.PWM(LED_PIN, 1000)
    pwm.start(0)
    temp = int(temperature)

    if temp <= 22:
        brightness = 10  # Dim
    elif 23 <= temp <= 25:
        brightness = 40 # Less dim
    else:
        brightness = 100  # Bright

    pwm.ChangeDutyCycle(brightness)
    
    # Keep the brightness for a while, adjust according to your needs
    time.sleep(5)
    
    pwm.stop()
    GPIO.cleanup()
    return brightness

if __name__ == "__main__":
    main()