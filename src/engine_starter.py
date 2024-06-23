import time
from hal import hal_dc_motor as motor
from hal import hal_rfid_reader as rfid

def start_engine():
    print("Starting engine sequence...")

    # 1: Initialize RFID reader and check authorization
    rfid_reader = rfid.SimpleMFRC522()
    print("Reading RFID card...")
    card_id, text = rfid_reader.read()
    print(f"Card ID: {card_id}")

    # Example list of authorized IDs
    authorized_ids = [1234567890, 2345678901, 3456789012,830894050716]

    if card_id not in authorized_ids:
        print("RFID authorization failed. Engine start aborted.")
        return
    
    print("RFID authorized. Starting engine...")

    # Step 2: Initialize motor and set speed to simulate starting the engine
    motor.init()
    motor.set_motor_speed(100)  # Setting motor speed to 100% to start the engine
    time.sleep(5)  # Simulate the time taken to start the engine
    motor.set_motor_speed(0)  # Stop the motor after starting the engine

    print("Engine started successfully.")

if __name__ == "__main__":
    start_engine()
