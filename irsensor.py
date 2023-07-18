import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
flame_pin = 5

GPIO.setup(flame_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(flame_pin) == GPIO.LOW:
            print('Fire detected')
        else:
            print('No fire detected')
            
        time.sleep(1)
except KeyboardInterrupt:
    print('Program terminated')