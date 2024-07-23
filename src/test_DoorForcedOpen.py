import DoorForcedOpen

def test_trigger_alarm(mocker):
    # Mock the LCD, BUZZER, and KEYPAD modules
    mocker.patch.object(DoorForcedOpen, 'LCD')
    mocker.patch.object(DoorForcedOpen, 'BUZZER')
    mocker.patch.object(DoorForcedOpen, 'KEYPAD')

    # Call the trigger_alarm function
    DoorForcedOpen.trigger_alarm()

    # Assert that the LCD functions were called correctly
    DoorForcedOpen.LCD.LCD_clear.assert_called_once()
    DoorForcedOpen.LCD.LCD_set_cursor.assert_called_with(0, 0)
    DoorForcedOpen.LCD.LCD_display_string.assert_called_with("Car Theft Warning:")
    DoorForcedOpen.LCD.LCD_set_cursor.assert_called_with(0, 1)
    DoorForcedOpen.LCD.LCD_display_string.assert_called_with("Triggered")

    # Assert that the BUZZER function was called with the correct argument
    DoorForcedOpen.BUZZER.turn_on_with_timer.assert_called_with(5)
