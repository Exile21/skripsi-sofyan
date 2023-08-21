import Adafruit_CharLCD as LCD

# Define LCD dimensions
lcd_columns = 16
lcd_rows = 2

# Initialize LCD
lcd = LCD.Adafruit_CharLCDPlate()

# Print "Hello, World!" on LCD
lcd.message('Hello,\nWorld!')
