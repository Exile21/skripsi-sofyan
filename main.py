import logging
from mq2 import MQ as mq2
from mq4 import MQ as mq4
from mq9 import MQ as mq9
import time
from Adafruit_DHT import DHT11, read_retry

# Configure logging
logging.basicConfig(filename='sensor_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# DHT11
sensor = DHT11
dht_pin = 18

mq2 = mq2(analogPin=0)
mq4 = mq4(analogPin=2)
mq9 = mq9(analogPin=1)
try:
    while True:
        gas_percentage_mq2 = mq2.MQPercentage()
        gas_percentage_mq4 = mq4.MQPercentage()
        gas_percentage_mq9 = mq9.MQPercentage()

        humidity, temperature = read_retry(sensor, dht_pin)
        if humidity is not None and temperature is not None:
            log_msg = f'Temperature: {temperature}°C, Humidity: {humidity}%'
            print(log_msg)
            logging.info(log_msg)
        else:
            log_msg = 'Failed to retrieve data from the humidity sensor'
            print(log_msg)
            logging.error(log_msg)

        log_msg = "MQ-2 Gas Percentage (CO2): " + str(gas_percentage_mq2["SMOKE"])
        print(log_msg)
        logging.info(log_msg)

        log_msg = "Average CO: " + str(gas_percentage_mq2["CO"]) + str(gas_percentage_mq9["CO"])
        print(log_msg)
        logging.info(log_msg)

        log_msg = "Average Methane: " + str((gas_percentage_mq4["METHANE"] + gas_percentage_mq9["METHANE"]) / 2)
        print(log_msg)
        logging.info(log_msg)

        time.sleep(2)
except KeyboardInterrupt:
    print("Program stopped by the user")
    logging.info("Program stopped by the user")
finally:
    print("Program terminated")
    logging.info("Program terminated")
