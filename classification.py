from sklearn.neural_network import RBFRegressor
import numpy as np

# Generate sample data
X = np.array([45, 55, 60, 15, 25, 35]).reshape(-1, 1)
y = np.array([2, 2, 2, 1, 1, 0])  # 2: Hot, 1: Medium, 0: Cold

# Create and train the RBF regressor
rbf = RBFRegressor(n_centers=10)
rbf.fit(X, y)

# Generate predictions for classification
X_test = np.array([52, 18]).reshape(-1, 1)
y_pred = rbf.predict(X_test)

# Threshold for classification
thresholds = [0.5, 1.5, 2.5]
class_labels = ['Cold', 'Medium', 'Hot']
y_pred_classes = np.zeros_like(y_pred, dtype=int)
for i in range(len(thresholds)):
    y_pred_classes[y_pred >= thresholds[i]] = i

# Print the predicted classes
for temp, temp_class in zip(X_test, y_pred_classes):
    print(f'Temperature: {temp} -> Class: {class_labels[temp_class]}')
