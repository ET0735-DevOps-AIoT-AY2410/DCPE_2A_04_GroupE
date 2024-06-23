#download this before running --> pip install RPi.GPIO adafruit-circuitpython-charlcd


import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

# GPIO setup for the buzzer, LCD, and door sensors
BUZZER_PIN = 18

DOOR_SENSORS = [5, 6, 13, 19]  # GPIO pins for door sensors

# GPIO pins for the LCD
lcd_rs = 27
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 17
lcd_backlight = 4

# Define LCD column and row size
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(BUZZER_PIN, GPIO.OUT)   # Setup buzzer pin as output



for sensor in DOOR_SENSORS:
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Setup door sensor pins as input with pull-up resistors

def check_doors_locked():
    return all(GPIO.input(sensor) for sensor in DOOR_SENSORS)

def trigger_alarm():
    
    GPIO.output(BUZZER_PIN, GPIO.HIGH)   # Sound the buzzer
    
    
    lcd.clear()
    lcd.message("Car Theft Warning:\nTriggered")   # Display warning message on the LCD
    
    
    time.sleep(5)    # Keep the buzzer on for 5 seconds
    
    # Turn off the buzzer
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def main():
    try:
        while True:
            if not check_doors_locked():     # trigger alarm if the doors are unlocked
                trigger_alarm()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear()
        lcd.set_backlight(0)
        GPIO.cleanup()

if __name__ == "__main__":
    main()
