import smbus
import time

# Define the I2C address and LCD size
I2C_ADDR = 0x27
LCD_WIDTH = 16
LCD_LINES = 2

# Define some constants for LCD control
LCD_CHR = 1
LCD_CMD = 0
LCD_BACKLIGHT = 0x08  # On
ENABLE = 0b00000100  # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# LCD line addresses
LCD_LINE_1 = 0x80  # Line 1 address
LCD_LINE_2 = 0xC0  # Line 2 address

# Open I2C interface
bus = smbus.SMBus(1)

def lcd_init():
    # Initialize the display
    lcd_byte(0x33, LCD_CMD)  # 110011 Initialize
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialize
    lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 001100 Display On, Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = the data
    # mode = 1 for data, 0 for command

    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

if __name__ == '__main__':
    try:
        lcd_init()
        while True:
            lcd_string("Hello, World!", LCD_LINE_1)
            time.sleep(2)
            lcd_string("Raspberry Pi", LCD_LINE_2)
            time.sleep(2)

    except KeyboardInterrupt:
        pass

    finally:
        lcd_byte(0x01, LCD_CMD)
