import Adafruit_CharLCD as LCD

# Define LCD dimensions
lcd_columns = 16
lcd_rows = 2

# Initialize LCD
lcd_address = 0x27 # Replace with your LCD I2C address
lcd = LCD.Adafruit_CharLCDPlate(address=lcd_address)

# Print "Hello, World!" on LCD
lcd.message('Hello,\nWorld!')
