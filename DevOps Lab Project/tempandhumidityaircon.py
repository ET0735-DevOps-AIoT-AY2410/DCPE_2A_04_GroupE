import time
from hal import hal_lcd as lcd
from hal import hal_temp_humidity_sensor as TEMP_HUMIDITY
from hal import hal_keypad as KEYPAD


tempvalue = []
optionvalue = [] 


def get_temperature():   #ADD THIS WHOLE FUNCTION IN MAIN MENU FOR LINE 4 !!!
    # Read the temperature from the sensor
    
    tempandhumidity = TEMP_HUMIDITY.read_temp_humidity()
    return tempandhumidity

def display_temperature():  #ADD THIS WHOLE FUNCTION IN MAIN MENU FOR LINE 4 !!!
    tempandhumidity = get_temperature()
    lcd.clear()
    lcd.lcd_display_string ("Temperature = %-3.1f C" % tempandhumidity.temperature, 0)
    lcd.lcd_display_string ("Humidity: %-3.1f %%" % tempandhumidity.humidity, 1)
    
    time.sleep(2)




def enter_desired_temperature():
    global key
    lcd.lcd_clear()
    lcd.lcd_display_string("Enter desired temperature:", 0)
    
    # code to capture user input
    global tempvalue
    tempvalue.append(key)
    print(tempvalue)
    
    #code to display user input
    lcd.lcd_clear()
    lcd.lcd_display_string(0, f"Aircon is set to {tempvalue} C")
    time.sleep(2)
    
    # Turn off the LCD and backlight enter low power mode
    lcd.lcd_clear()
    lcd.backlight_off()

    time.sleep(5)

def main():
    # Initialize the LCD and the temperature/humidity sensor
    lcd = lcd.lcd()  #init lcd
    TEMP_HUMIDITY.init() #init sensor
    KEYPAD.init() #initialise keypad
    
    # The display menu please fill in the main menu codes here !!
    lcd.write_line(0, "Enter 2 to control aircon")
    
    global optionvalue #value of number/s keyed in
    global option #number keyed in
    optionvalue.append(option)
    if optionvalue == "2":  #if option 2 is chosen
        
        display_temperature()
        enter_desired_temperature()

if __name__ == "__main__":
    main()
