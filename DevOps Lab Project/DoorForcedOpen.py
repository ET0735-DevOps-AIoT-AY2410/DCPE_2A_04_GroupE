import time
import RPi.GPIO as GPIO
from hal import hal_lcd as LCD
from hal import hal_buzzer as BUZZER
from hal import hal_keypad as KEYPAD

BUZZER_PIN = 18  # GPIO pin for the buzzer

def trigger_alarm():
    # Display warning message on LCD
    LCD.LCD_clear()
    LCD.LCD_set_cursor(0, 0) 
    LCD.LCD_display_string("Car Theft Warning:")
    LCD.LCD_set_cursor(0, 1)
    LCD.LCD_display_string("Triggered")
    BUZZER.turn_on_with_timer(5) # sounds buzzer for 5 sec
    
def main():
    LCD = LCD.lcd()
    BUZZER.init()
    KEYPAD.init()
    
    car_locked = True  # Assume the car is locked initially

    while True: #check if car locked
        
        key_pressed = KEYPAD.get_key() #check if '8' key is pressed (8 key pressed is assumed as a break in )

        if car_locked and key_pressed == '8':
            trigger_alarm()

        time.sleep(0.1) 

if __name__ == "__main__":
    main()
    

