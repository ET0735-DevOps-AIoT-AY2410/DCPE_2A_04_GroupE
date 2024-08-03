import RPi.GPIO as GPIO
import time

SERVO_PIN = 26  # Update with your servo GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz
servo.start(0)

def lock_door():
    # Rotate servo to lock position
    servo.ChangeDutyCycle(12)  # Adjust based on your servo's lock position
    time.sleep(1)
    servo.ChangeDutyCycle(0)

def unlock_door():
    # Rotate servo to unlock position
    servo.ChangeDutyCycle(2)  # Adjust based on your servo's unlock position
    time.sleep(1)
    servo.ChangeDutyCycle(0)

if __name__ == '__main__':
    try:
        while True:
            command = input("Enter 'lock' or 'unlock': ").strip().lower()
            if command == 'lock':
                lock_door()
            elif command == 'unlock':
                unlock_door()
            else:
                print("Invalid command")
    except KeyboardInterrupt:
        pass
    finally:
        servo.stop()
        GPIO.cleanup()
