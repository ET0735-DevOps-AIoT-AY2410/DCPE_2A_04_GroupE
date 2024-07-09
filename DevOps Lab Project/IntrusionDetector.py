import time
import RPi.GPIO as GPIO
from hal import hal_lcd as LCD
from hal import hal_buzzer as BUZZER
from hal import hal_keypad as KEYPAD
from hal import hal_usonic as USONIC 
import DoorForcedOpen 

BUZZER_PIN = 18  # GPIO pin for the buzzer


def intrusion_detected():
    
    seat_distance = 25 #initial distance between seat and sensor !! Assume the distance is fixed at 25 cm
    print(f"Seat distance: {seat_distance:.1f} cm")
    
    while True: #this loop constantly measures current seat distance and compares it with the initial distance to see for any changes
        current_distance = USONIC.get_distance()
        print(f"Measured distance: {current_distance:.1f} cm")
        
        # Check if distance between car seats and sensor has changed significantly, indicating an intrusion
        if abs(seat_distance - current_distance) > 5 or abs(current_distance - seat_distance) < 5:  # for detecting intrusion
            print("Intrusion detected!")
            trigger_alarm2()
            break  # Exit loop after triggering alarm for 5 seconds
        
        time.sleep(1)  # Wait for 1 second before the next distance measurement
    
    GPIO.cleanup()



def trigger_alarm2():

DoorForcedOpen.trigger_alarm()


def main():
    LCD = LCD.lcd()
    BUZZER.init()
    KEYPAD.init()
    USONIC.init()
    
    car_locked = True  # Assume the car is locked initially

    while True: #check if car locked
        
        intrusion_detected()

        time.sleep(0.1) 
