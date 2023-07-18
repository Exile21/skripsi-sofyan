import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ir_pin = 5

GPIO.setup(ir_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(ir_pin) == GPIO.HIGH:
            print('Obstacle detected')
        else:
            print('Obstacle not detected')
            
        time.sleep(1)
except KeyboardInterrupt:
    print('Program terminated')