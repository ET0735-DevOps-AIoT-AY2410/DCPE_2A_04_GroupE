import time
from hal import hal_lcd as lcd
from hal import hal_moisture_sensor as moisture

# Initialize LCD
lcd_display = lcd.lcd()

# Calibration factor to adjust the baseline reading
CALIBRATION_FACTOR = 0.2  # Adjust this factor as necessary

# Number of readings to average for smoothing
NUM_READINGS = 10

# Initialize a list to store sensor readings
readings = [0] * NUM_READINGS
read_index = 0

def read_moisture_sensor():
    # Read the moisture sensor value (voltage)
    return moisture.read_sensor()

def convert_to_fuel_level(voltage):
    # Apply calibration factor
    calibrated_voltage = voltage * CALIBRATION_FACTOR
    # Ensure the voltage does not go below 0
    if calibrated_voltage < 0:
        calibrated_voltage = 0
    # Convert the voltage to a fuel level percentage (0-100%)
    # Assuming 0V corresponds to 0% fuel and 3.3V corresponds to 100% fuel
    fuel_level = (calibrated_voltage / 3.3) * 100
    return fuel_level

def get_fuel_level_category(fuel_level):
    if fuel_level < 20:       # Change threshold for "Low"
        return "Low"
    elif fuel_level < 60:     # Change threshold for "Medium"
        return "Medium"
    else:                     # Anything above 60 is "High"
        return "High"

def display_fuel_level(category):
    lcd_display.lcd_clear()
    lcd_display.lcd_display_string("Fuel Level:", 1)
    lcd_display.lcd_display_string(category, 2)

try:
    # Initialize the moisture sensor
    moisture.init()

    while True:
        # Read the moisture sensor voltage
        voltage = read_moisture_sensor()
        
        # Update the readings list with the new reading
        readings[read_index] = voltage
        read_index = (read_index + 1) % NUM_READINGS
        
        # Calculate the average of the readings
        avg_voltage = sum(readings) / NUM_READINGS
        
        # Convert the averaged voltage to a fuel level
        fuel_level = convert_to_fuel_level(avg_voltage)
        
        # Get the fuel level category
        category = get_fuel_level_category(fuel_level)
        
        # Display the fuel level category on the LCD
        display_fuel_level(category)
        
        # Print the fuel level percentage to the terminal
        print(f"Fuel Level: {fuel_level:.2f}% ({category})")
        
        # Wait before repeating the loop
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped")
