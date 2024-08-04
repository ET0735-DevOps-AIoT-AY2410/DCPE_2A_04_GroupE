import time
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import hal.hal_buzzer as buzzer
import RPi.GPIO as GPIO
import password_checker as pwchecker
import username_checker as unchecker

lcd = LCD.lcd()
lcd.lcd_clear()


def main():
    

    lcd.lcd_display_string("Enter Username", 1)

    keypad.init(unchecker.key_pressed)

    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

if __name__ == '__main__':
    main()