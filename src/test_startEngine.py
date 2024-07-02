# Mock RFID reader module
class MockRFIDReader:
    def __init__(self, card_id=830894050716):
        self.card_id = card_id

    def read(self):
        return self.card_id, "Authorized Card"

# Mock motor module
class MockMotor:
    def __init__(self):
        self.speeds = []

    def init(self):
        print("Motor initialized")

    def set_motor_speed(self, speed):
        self.speeds.append(speed)
        print(f"Motor speed set to {speed}")

# Function to replace RFID reader and motor in engine_starter
def start_engine_with_mocks(card_id):
    import engine_starter
    
    # Replace RFID reader and motor with mocks
    rfid_reader = MockRFIDReader(card_id=card_id)
    motor = MockMotor()

    # Call the start_engine function with mocks
    engine_starter.start_engine(rfid_reader, motor)
    
    return motor.speeds

# Tests
def test_start_engine_authorized():
    speeds = start_engine_with_mocks(830894050716)  # Authorized card ID
    assert speeds == [100, 0]  # Motor should start and then stop
    print("Authorized test passed")

def test_start_engine_unauthorized():
    speeds = start_engine_with_mocks(9999999999)  # Unauthorized card ID
    assert speeds == []  # Motor should not start
    print("Unauthorized test passed")

if __name__ == "__main__":
    test_start_engine_authorized()
    test_start_engine_unauthorized()
    print("All tests passed")
