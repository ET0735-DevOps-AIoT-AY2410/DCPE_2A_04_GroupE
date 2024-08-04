import time
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import RPi.GPIO as GPIO
import password_checker as pwchecker

GPIO.setmode(GPIO.BCM)  # choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output   

incorrect_attempts = 0

username = [1, 2, 3, 4]
pin = []

lcd = LCD.lcd()
lcd.lcd_clear()

def update_lcd_with_masked_pin():
    lcd.lcd_clear()  # Clear entire LCD
    lcd.lcd_display_string("Enter Username", 1)
    lcd.lcd_display_string(''.join(map(str, pin)), 2)

def check_username():
    global incorrect_attempts
    if pin == username:
        lcd.lcd_clear()
        lcd.lcd_display_string("Correct", 1)
        time.sleep(1)
        lcd.lcd_clear()
        pin.clear()
        keypad.init(pwchecker.key_pressed)  # Switch to password entry mode
    else:
        incorrect_attempts += 1
        GPIO.output(18, 1)  # Turn on the buzzer
        time.sleep(1)  # Duration to turn on the buzzer
        GPIO.output(18, 0)  # Turn off when time is up
        lcd.lcd_clear()
        lcd.lcd_display_string("Invalid Username", 1)
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
    pin.append(key)
    update_lcd_with_masked_pin()

    if len(pin) == 4:
        check_username()
        if pin != username:
            pin.clear()
            lcd.lcd_clear()
            lcd.lcd_display_string("Enter Username", 1)
            update_lcd_with_masked_pin()