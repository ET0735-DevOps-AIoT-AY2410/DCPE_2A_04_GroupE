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
def test_start_engine_multiple():
    card_ids = [830894050716, 1234567890]  # Authorized card IDs
    speeds = []
    for card_id in card_ids:
        speeds.extend(start_engine_with_mocks(card_id))
    assert speeds == [100, 0, 100, 0]  # Motor should start and then stop for each card
    print("Multiple test passed")


def test_start_engine_unauthorized():
    speeds = start_engine_with_mocks(9999999999)  # Unauthorized card ID
    assert speeds == []  # Motor should not start
    print("Unauthorized test passed")

if __name__ == "__main__":
    test_start_engine_multiple()
    test_start_engine_unauthorized()
    print("All tests passed")
