import json

# Generate ascending synthetic training data
num_samples = 1000  # You can adjust the number of data points

training_data = []

for i in range(num_samples):
    temperature = i / num_samples * 100
    humidity = i / num_samples * 100
    gas_percentage = i / num_samples * 5
    average_co = i / num_samples
    average_methane = i / num_samples * 0.1
    label = "fire" if temperature > 45 else "normal"

    data_point = {
        "temperature": temperature,
        "humidity": humidity,
        "gasPercentage": gas_percentage,
        "averageCO": average_co,
        "averageMethane": average_methane,
        "label": label
    }

    training_data.append(data_point)

# Save generated training data to a JSON file
with open('training_data_temp_threshold.json', 'w') as f:
    json.dump(training_data, f, indent=4)

print(f"Generated {num_samples} ascending training data points with temperature threshold and saved to 'training_data_temp_threshold.json'")
