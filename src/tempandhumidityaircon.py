import time
from hal import hal_lcd as LCD
from hal import hal_temperature_sensor as SENSOR
from hal import hal_input as INPUT
from hal import hal_power as POWER

# Constants
LCD_ADDRESS = 0x27  # Example I2C address for the LCD
LOW_POWER_MODE = "LOW_POWER_MODE"

# Initialize LCD and sensor
LCD.init(LCD_ADDRESS)
SENSOR.init()

def display_message(line1, line2=""):
    LCD.clear()
    LCD.write(line1, line=0)
    if line2:
        LCD.write(line2, line=1)

def enter_low_power_mode():
    LCD.set_backlight(0)  # Turn off backlight
    LCD.clear()  # Clear the LCD display
    POWER.enter_state(LOW_POWER_MODE)  # Enter low power mode

def control_aircon():
    display_message("Enter desired", "temperature")
    time.sleep(2)  # Display message for 2 seconds

    desired_temp = INPUT.read_temperature()  # Hypothetical function to read user input for temperature
    display_message(f"Temp: {desired_temp} C")
    time.sleep(2)  # Display the entered temperature for 2 seconds

    enter_low_power_mode()  # Enter low power mode

    # After waking up from low power mode
    display_message("Aircon is set", f"to {desired_temp} C")

def main():  #put this part in the main code !
    while True:
        user_option = INPUT.read_option()  # Hypothetical function to read user input for option

        if user_option == 2:   
            control_aircon()
        else:
            display_message("Invalid option", "Try again")
            time.sleep(2)

if __name__ == "__main__":
    main()
