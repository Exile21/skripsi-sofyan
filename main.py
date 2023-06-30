import time
import board
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Initialize the LCD object
lcd_columns = 16
lcd_rows = 2
i2c = board.I2C()
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

# Clear the LCD display
lcd.clear()

# Display a message
lcd.message = "Hello, world!"

# Wait for 2 seconds
time.sleep(2)

# Clear the LCD display
lcd.clear()

# Display a custom message
lcd.message = "I2C LCD\nTest"

# Wait for 2 seconds
time.sleep(2)

# Clear the LCD display
lcd.clear()

# Display scrolling text
text = "Scrolling text..."
while True:
    lcd.message = text
    # Scroll to the left
    time.sleep(0.5)
    for _ in range(len(text) - lcd_columns + 1):
        time.sleep(0.5)
        lcd.move_left()
    # Scroll to the right
    for _ in range(len(text) - lcd_columns + 1):
        time.sleep(0.5)
        lcd.move_right()

# Cleanup GPIO resources if needed
# lcd.clear()
# lcd.backlight = False
# lcd.close()
