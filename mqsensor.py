import smbus
import time

pcf8591_address = smbus.SMBus(1)

bus = smbus.SMBus(1)

def read_analog(adc_channel):
    bus.write_byte(pcf8591_address, adc_channel)
    bus.read_byte(pcf8591_address)  # dummy read to start conversion
    analog_value = bus.read_byte(pcf8591_address)
    return analog_value

while True:
    mq2_value = read_analog(0)
    mq4_value = read_analog(1)
    mq9_value = read_analog(2)
    
    print(f'MQ-2: {mq2_value}, MQ-4: {mq4_value}, MQ-9: {mq9_value}')
    
    time.sleep(1)