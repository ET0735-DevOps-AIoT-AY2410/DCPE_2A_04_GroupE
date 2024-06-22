import time
from threading import Thread
from time import sleep
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import RPi.GPIO as GPIO


user_input = []

lcd = LCD.lcd()
lcd.lcd_clear()


def init():
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)  # set GPIO 24 as output

def key_pressed(key):

    user_input.append(key)
    if key==1:
        GPIO.output(24, 1)
        lcd.lcd_clear()
        lcd.lcd_display_string("Door is unlocked", 1)
    elif key==2:
        lcd.lcd_clear()
        lcd.lcd_display_string("Door is locked", 1)
        for i in range(5):
            GPIO.output(24, 0)
            sleep(0.5)
            GPIO.output(24, 1)
            sleep(0.5)
        GPIO.output(24, 0)

def main():
    init()
    lcd = LCD.lcd()
    lcd.lcd_clear()

    lcd.lcd_display_string("Enter '1' to unlock the door", 1)
    lcd.lcd_display_string("Enter '2' to lock the door", 2)

    keypad.init(key_pressed)

    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    
if __name__ == "__main__":
    main()
