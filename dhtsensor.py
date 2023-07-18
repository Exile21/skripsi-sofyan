import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
dht_pin = 18

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
        
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
        else:
            print('Failed to retrieve data from humidity sensor')
            
        time.sleep(2)
except KeyboardInterrupt:
    print('Program terminated')