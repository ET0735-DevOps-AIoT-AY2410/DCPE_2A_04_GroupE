import time
from time import sleep
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output   

incorrect_attempts = 0
password = [4, 3, 2, 1]
pin = []

lcd = LCD.lcd()

def update_lcd_with_masked_pin():
    masked_pin = '*' * len(pin)
    lcd.lcd_clear()
    lcd.lcd_display_string("Enter Password", 1)
    lcd.lcd_display_string(masked_pin, 2)

def check_password():
    global pin
    global incorrect_attempts
    if pin == password:
        lcd.lcd_clear()
        pin.clear
        lcd.lcd_display_string("2FA", 1)
        lcd.lcd_display_string("Put finger  0")
        if pin == [0]:#does not work for now it doesnt show main menu it displays enter password ****
            sleep(3)
            lcd.lcd_clear()
            lcd.lcd_display_string("main menu",1)
            pin.clear()  # Clear current pin entry
            keypad.disable()  # Disable keypad input


        # Implement further actions for granted access here
    else:
        incorrect_attempts += 1
        GPIO.output(18, 1)  # Turn on the buzzer
        time.sleep(1)  # Duration to turn on the buzzer
        GPIO.output(18, 0)  # Turn off when time is up
        lcd.lcd_clear()
        lcd.lcd_display_string("Invalid Password", 1)
        time.sleep(1)
        pin.clear()
        update_lcd_with_masked_pin()
        
        if incorrect_attempts >= 3:
            lcd.lcd_clear()
            lcd.lcd_display_string("Account Locked", 1)
            pin.clear()  # Clear current pin entry
            keypad.disable()  # Disable keypad input

def key_pressed(key):
    global pin
    pin.clear
    pin.append(key)
    update_lcd_with_masked_pin()
    if len(pin) == 4:
        check_password()
        if pin != password:
            pin.clear()
            lcd.lcd_clear()
            lcd.lcd_display_string("Enter Password", 1)
