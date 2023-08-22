import csv
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Flatten
from sklearn.metrics import classification_report, confusion_matrix
from keras.utils import to_categorical
from keras.optimizers import RMSprop
from keras.losses import MeanSquaredError
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from custom_layers import RBFLayer

# template data
# data = [
#     {
#         "temperature": 28.0,
#         "humidity": 72.0,
#         "gasPercentage": 0.05592142728955934,
#         "averageCO": 0.013767248273482555,
#         "averageMethane": 0.00018656185930989146,
#         "label": "normal"
#     },
# ]

# # save data into csv file
# with open('data.csv', 'w', newline='') as csvfile:
#     fieldnames = ['temperature', 'humidity', 'gasPercentage', 'averageCO', 'averageMethane', 'label']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for sample in data:
#         writer.writerow({'temperature': float(sample['temperature']), 'humidity': float(sample['humidity']), 'gasPercentage': float(sample['gasPercentage']), 'averageCO': float(sample['averageCO']), 'averageMethane': float(sample['averageMethane']), 'label': sample['label']})

# Load data from csv file into dictionary
data = []
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Convert data to numpy arrays
features = np.array([
    [
        sample['temperature'],
        sample['humidity'],
        sample['gasPercentage'],
        sample['averageCO'],
        sample['averageMethane']
    ]
    for sample in data
])
labels = np.array([sample['label'] for sample in data])

# Preprocess features
scaler = StandardScaler() 
# z = (x - mean) / std
# z is the standardized value of the data point.
# x is the original value of the data point.
# mean is the mean of the feature.
# std is the standard deviation of the feature.

features_scaled = scaler.fit_transform(features)

# Encode labels into numerical values
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
encoded_labels = to_categorical(encoded_labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, encoded_labels, test_size=0.2, random_state=42)

# Add a dense layer for classification
num_labels = len(np.unique(labels))
activation = 'softmax' if num_labels > 2 else 'sigmoid'

# Create the model
model = Sequential()
model.add(Flatten(input_shape=(X_train.shape[1],)))
model.add(RBFLayer(16, 0.5))
model.add(Dense(num_labels, activation=activation))

# Optimize with different learning rates
learning_rates = [0.001, 0.01, 0.1, 0.2, 0.3]

# Compile the model
model.compile(loss=MeanSquaredError(), optimizer=RMSprop(learning_rate=learning_rates[0]), metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=8, verbose=2, validation_data=(X_test, y_test))

# Plot training history
plt.figure(figsize=(12, 6))

# Plot training & validation accuracy values
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.tight_layout()
plt.show()

# # Save the trained model
model.save("rbf_classification_model.h5")

# Make predictions
predictions = model.predict(X_test)
predicted_labels = np.argmax(predictions, axis=1)
predicted_labels = label_encoder.inverse_transform(predicted_labels)
print("Predicted data:", X_test)
print("Predicted labels:", predicted_labels)

# Classification report
target_names = label_encoder.classes_
classification_report_str = classification_report(
    np.argmax(y_test, axis=1), 
    np.argmax(predictions, axis=1), 
    target_names=target_names,
    zero_division=1
)
print(classification_report_str)

# Confusion matrix
confusion = confusion_matrix(np.argmax(y_test, axis=1), np.argmax(predictions, axis=1))
plt.figure(figsize=(8, 6))
sns.heatmap(confusion, annot=True, fmt="d", cmap="Blues", xticklabels=target_names, yticklabels=target_names)
plt.ylabel('Actual Value')
plt.xlabel('Predicted Value')
plt.title('Confusion Matrix')
plt.show()

# Load the saved model
from keras.models import load_model
saved_model = load_model("rbf_classification_model.h5", custom_objects={"RBFLayer": RBFLayer})

# Example usage of the saved model for making predictions
new_data = np.array([[3.200e+01, 4.800e+01, 2.043e-02, 6.710e-03, 1.600e-04]])

# Load the same scaler used for training
scaler = StandardScaler()
scaler.fit(X_train)  # Fit the scaler on the training data

# Preprocess new data using the same scaler
scaled_new_data = scaler.transform(new_data)

# Make predictions
predictions = saved_model.predict(scaled_new_data)
predicted_class_index = np.argmax(predictions, axis=1)
predicted_class = label_encoder.inverse_transform(predicted_class_index)

print("Data:", new_data)
print("Predicted class:", predicted_class)