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
from lcd import update_lcd_line_2
import threading  # Import the threading module

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

# Define predicted_class as a global variable
predicted_class = "N/A"

# Define a function to continuously update the LCD without blocking
def lcd_update_thread():
    while True:
        # Update LCD line 2 with the predicted class
        update_lcd_line_2(predicted_class)
        time.sleep(2)  # Sleep for 2 seconds (if you want a delay)

# Start the LCD update thread
lcd_thread = threading.Thread(target=lcd_update_thread)
lcd_thread.daemon = True  # Set the thread as a daemon so it will exit when the main program exits
lcd_thread.start()

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
        predicted_class = label_encoder.inverse_transform(predicted_class_index)[0]

        print("Predicted class:", predicted_class)

        time.sleep(2)
except KeyboardInterrupt:
    print("Program stopped by the user")
finally:
    print("Program terminated")
