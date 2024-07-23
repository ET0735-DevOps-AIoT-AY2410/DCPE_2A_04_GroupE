import sys
import RPi.GPIO as GPIO
import time
from time import sleep

LED_PIN = 24

def set_led_brightness(temperature):
    if temperature <= 22:
        brightness = 10  # Dim
    elif 23 <= temperature <= 25:
        brightness = 40 # Less dim
    else:
        brightness = 100  # Bright

    return brightness

def main(temp):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    
    pwm = GPIO.PWM(LED_PIN, 1000)
    pwm.start(0)
    
    brightness = set_led_brightness(int(temp))
    pwm.ChangeDutyCycle(brightness)
    
    # Keep the brightness for a while, adjust according to your needs
    time.sleep(10)
    
    pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python aircon.py <temperature>")
        sys.exit(1)
    
    temperature = sys.argv[1]
    main(temperature)