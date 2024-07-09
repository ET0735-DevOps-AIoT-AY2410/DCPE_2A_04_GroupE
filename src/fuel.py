import time
from hal import hal_lcd as lcd
from hal import hal_ldr_sensor as ldr
import requests

def get_fuel_level():
    lcd_display = lcd.lcd()
    channel = 0  # Assuming that the LDR is connected to channel 0 of MCP3008

    while True:
        light_intensity = ldr.get_light_level(channel)
        fuel_level = get_fuel_level(light_intensity)

        print(f"Light Intensity: {light_intensity:.2f}V - Fuel Level: {fuel_level}")
        lcd_display.lcd_display_string(f"Fuel Level: {fuel_level}", 1)

        time.sleep(1)


fuel_level = get_fuel_level()

# URL of your Flask endpoint
url = 'http://127.0.0.1:5000/update-fuel-level'

# Data to be sent to the Flask app
data = {'fuel_level': fuel_level}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Fuel level updated successfully.")
else:
    print("Error updating fuel level:", response.text)




#def get_fuel_level(light_intensity):
#    if light_intensity > 3 :
#        return "High"
#    elif 1 <= light_intensity < 3:
#        return "Medium"
#    else:
#        return "Low"