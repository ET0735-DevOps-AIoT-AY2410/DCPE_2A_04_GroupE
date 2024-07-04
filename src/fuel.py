import time
from hal import hal_lcd as lcd
from hal import hal_ldr_sensor as ldr

def get_fuel_level(light_intensity):
    if light_intensity > 3 :
        return "High"
    elif 1 <= light_intensity < 3:
        return "Medium"
    else:
        return "Low"

def main():
    lcd_display = lcd.lcd()
    channel = 0  # Assuming that the LDR is connected to channel 0 of MCP3008

    while True:
        light_intensity = ldr.get_light_level(channel)
        fuel_level = get_fuel_level(light_intensity)

        print(f"Light Intensity: {light_intensity:.2f}V - Fuel Level: {fuel_level}")
        lcd_display.lcd_display_string(f"Fuel Level: {fuel_level}", 1)

        time.sleep(1)

if __name__ == "__main__":
    main()
