def init():
    import hal_rfid_reader
    from hal_rfid_reader import SimpleMFRC522
    import RPi.GPIO as GPIO
    import time 
    from time import sleep

def read_rfid():
    import hal_rfid_reader
    from hal_rfid_reader import SimpleMFRC522
    reader = SimpleMFRC522()

    try:
        print("Place your card near the reader...")
        card_id, text = reader.read()
        print(f"Card ID: {card_id}")
        if card_id in [988654710544]:
            print("found")
    except Exception as e:
        print(f"Error reading RFID card: {e}")
        return False
    return card_id

if __name__ == "__main__":
    init()
    import time 
    from time import sleep
    while True:
        result = read_rfid()
        sleep(2)  # Sleep for 2 seconds to avoid rapid readings



