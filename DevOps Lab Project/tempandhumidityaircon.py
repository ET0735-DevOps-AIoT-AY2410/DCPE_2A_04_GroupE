import time
<<<<<<< HEAD
from hal import hal_lcd as lcd
from hal import hal_temp_humidity_sensor as TEMP_HUMIDITY
from hal import hal_keypad as KEYPAD


tempvalue = []
optionvalue = [] 




=======
import RPi.GPIO as GPIO
from hal import hal_lcd as lcd
from hal import hal_temp_humidity_sensor as TEMP_HUMIDITY
from hal import hal_keypad as KEYPAD
from hal import hal_led as LED


tempvalue = []
optionvalue = []
 

# Function to set the brightness of the LED
def set_output(tempvalue):

    if 0 <= tempvalue <= 10: #from 0 to 10 degrees led at 25 percent power
        pwm.ChangeDutyCycle(25)
        if 10 < tempvalue <= 20: #from >10 to 20 degrees led at 50 percent power
            pwm.ChangeDutyCycle(50)
            if 20 < tempvalue <= 30: #from >20 to 30 degrees led at 75 percent power
                pwm.ChangeDutyCycle(75)
                if 30 < tempvalue <= 40: #from >30 to 40 degrees led at 100 percent power
                    pwm.ChangeDutyCycle(100)
    else:
        print("Temperature level must be between 0 and 40")
        
    
>>>>>>> bug-fix-harene


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
<<<<<<< HEAD
=======
    LED.init() #initialise led
    global pwm
    pwm = GPIO.PWM(24, 1000) # Initialize PWM on the GPIO pin with a frequency of 1000 Hz
    pwm.start(0)  # Start PWM with 0% duty cycle (LED off)
>>>>>>> bug-fix-harene
    
    # The display menu please fill in the main menu codes here !!
    lcd.write_line(0, "Enter 2 to control aircon")
    
    global optionvalue #value of number/s keyed in
    global option #number keyed in
    optionvalue.append(option)
    if optionvalue == "2":  #if option 2 is chosen to control aircon temp
        enter_desired_temperature()
<<<<<<< HEAD
=======
        set_output()

    
>>>>>>> bug-fix-harene

if __name__ == "__main__":
    main()
