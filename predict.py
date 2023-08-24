from keras.models import load_model
from custom_layers import RBFLayer
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import csv
import pickle

saved_model = load_model("rbf_classification_model.h5", custom_objects={"RBFLayer": RBFLayer})

# Example usage of the saved model for making predictions
new_data = np.array([[3.200e+01, 4.800e+01, 2.043e-02, 6.710e-03, 1.600e-04]])

# Import the scaler from pickle
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Preprocess new data using the same scaler
scaled_new_data = scaler.transform(new_data)

# Import the labels from csv
with open('target_names.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    labels = list(reader)[0]

# Encode labels into numerical values
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
encoded_labels = to_categorical(encoded_labels)

# Make predictions
predictions = saved_model.predict(scaled_new_data)
predicted_class_index = np.argmax(predictions, axis=1)
predicted_class = label_encoder.inverse_transform(predicted_class_index)

print("Data:", new_data)
print("Predicted class:", predicted_class)