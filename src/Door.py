import RPi.GPIO as GPIO #import RPi.GPIO module
import time
from time import sleep
from hal import hal_servo as servo
import sys

def lock_door():
    servo.set_servo_position(180)

def unlock_door():
    servo.set_servo_position(45)

if __name__ == "__main__":
    servo.init()

    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "lock":
            lock_door()
        elif action == "unlock":
            unlock_door()
        else:
            print("Unknown action.")
    else:
        print("No action specified.")