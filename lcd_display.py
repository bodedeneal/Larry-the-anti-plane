import smbus2
import time
from RPLCD.i2c import CharLCD

# Define LCD parameters
i2c_address = 0x27  # I2C address of your LCD (use 0x27 or 0x3F based on your module)
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD
lcd = CharLCD('PCF8574', i2c_address, cols=lcd_columns, rows=lcd_rows)

# Display a message
try:
    lcd.write_string("Hello, World!")
    time.sleep(2)
    lcd.clear()
    lcd.write_string("Raspberry Pi :)")
    time.sleep(5)
finally:
    lcd.clear()
