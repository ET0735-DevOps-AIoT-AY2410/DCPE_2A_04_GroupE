#download this before implementing --> pip install RPi.GPIO adafruit-circuitpython-charlcd adafruit-circuitpython-dht

import time
import Adafruit_DHT
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

# GPIO setup for the sensor and LCD
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin for the DHT sensor

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

def low_power_mode():
    # Turn off LCD display and backlight
    lcd.clear()
    lcd.set_backlight(0)
    time.sleep(1)  # Simulate entering low power mode

def control_aircon():
    lcd.clear()
    lcd.message("Enter desired\ntemperature:")

    # Assuming the desired temperature is input via the console for this example
    desired_temp = input("Enter desired temperature: ")
    
    # Display the desired temperature on the LCD
    lcd.clear()
    lcd.message(f"Desired temp:\n{desired_temp}C")
    time.sleep(2)  # Display for 2 seconds

    # Turn off the LCD and enter Low Power Mode
    low_power_mode()

    # Display aircon set message
    lcd.set_backlight(1)
    lcd.message(f"Aircon is set\nto {desired_temp}C")

def main():
    while True:
        lcd.clear()
        lcd.message("1. Read Temp & Hum\n2. Control Aircon")
        option = input("Select option: ")

        if option == '2':
            control_aircon()
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear()
        lcd.set_backlight(0)
        GPIO.cleanup()
