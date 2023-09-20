from mq2 import MQ as mq2
from mq4 import MQ as mq4
from mq9 import MQ as mq9
import time
from Adafruit_DHT import DHT11, read_retry
from tensorflow.keras.models import load_model
from custom_layers import RBFLayer
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import csv
import pickle
import time
import Adafruit_CharLCD as LCD

# DHT11
sensor = DHT11
dht_pin = 18

mq2 = mq2(analogPin=0)
mq4 = mq4(analogPin=2)
mq9 = mq9(analogPin=1)

# Load the saved model
saved_model = load_model("rbf_classification_model.h5", custom_objects={"RBFLayer": RBFLayer})

# Import the scaler from pickle
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Import the labels from csv
with open('target_names.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    labels = list(reader)[0]

# Encode labels into numerical values
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
encoded_labels = to_categorical(encoded_labels)

# Initialize the LCD screen with I2C backpack module
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCDPlate()

try:
    while True:
        gas_percentage_mq2 = mq2.MQPercentage()
        gas_percentage_mq4 = mq4.MQPercentage()
        gas_percentage_mq9 = mq9.MQPercentage()

        average_co = (gas_percentage_mq2["CO"] + gas_percentage_mq9["CO"]) / 2
        average_methane = (gas_percentage_mq4["METHANE"] + gas_percentage_mq9["METHANE"]) / 2

        humidity, temperature = read_retry(sensor, dht_pin)
        if humidity is None or temperature is None:
            print("Failed to retrieve data from DHT11 sensor")
        else:
            log_msg1 = f'Temperature: {temperature}°C'
            print(log_msg1)
            log_msg2 = f'Humidity: {humidity}%'
            print(log_msg2)

        # Preprocess new data using the same scaler
        new_data = np.array([[temperature, humidity, gas_percentage_mq2["SMOKE"], average_co, average_methane]])
        scaled_new_data = scaler.transform(new_data)

        # Make predictions
        predictions = saved_model.predict(scaled_new_data)
        predicted_class_index = np.argmax(predictions, axis=1)
        predicted_class = label_encoder.inverse_transform(predicted_class_index)

        print("Predicted class:", predicted_class)

        # Print the predicted class on the LCD screen
        lcd.clear()
        lcd.message(f'Predicted class:\n{predicted_class[0]}')

        time.sleep(2)
except KeyboardInterrupt:
    print("Program stopped by the user")
finally:
    print("Program terminated")
