# Import the functions from mq2.py, mq4.py, and mq5.py
from mq2 import MQ as mq2
from mq4 import MQ as mq4
from mq9 import MQ as mq9
from irsensor import detect_flame
import time
from sklearn.neural_network import RBFRegressor
import numpy as np
import RPi.GPIO as GPIO
import Adafruit_DHT

# DHT11
sensor = Adafruit_DHT.DHT11
dht_pin = 18

# IR SENSOR
GPIO.setmode(GPIO.BCM)
flame_pin = 5
GPIO.setup(flame_pin, GPIO.IN)

# MQ SENSORS
mq2 = mq2(analogPin=0)
mq4 = mq4(analogPin=2)
mq9 = mq9(analogPin=1)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
        gas_percentage_mq9 = mq9.MQPercentage()
        gas_percentage_mq4 = mq4.MQPercentage()
        gas_percentage_mq2 = mq2.MQPercentage()
        
        if GPIO.input(flame_pin) == GPIO.LOW:
            print('Fire detected')
        else:
            print('No fire detected')
        
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
        else:
            print('Failed to retrieve data from humidity sensor')
            
        print("MQ-2 Gas Percentage (LPG):", gas_percentage_mq2["GAS_LPG"])
        print("MQ-2 Gas Percentage (CO):", gas_percentage_mq2["CO"])
        print("MQ-2 Gas Percentage (Smoke):", gas_percentage_mq2["SMOKE"])
        print("MQ-4 Gas Percentage (Methane):", gas_percentage_mq4["METHANE"])
        print("MQ-4 Gas Percentage (CNG):", gas_percentage_mq4["CNG"])
        print("MQ-9 Gas Percentage (CO):", gas_percentage_mq9["CO"])
        print("MQ-9 Gas Percentage (Flammable):", gas_percentage_mq9["FLAMMABLE"])
        
        time.sleep(1)
except KeyboardInterrupt:
    print('Program terminated')
finally:
    GPIO.cleanup()