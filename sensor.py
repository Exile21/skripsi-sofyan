import numpy as np

def calculate_gas_concentration(sensor_readings, gas_concentrations, raw_sensor_reading):
    # Perform curve fitting
    calibration_curve = np.polyfit(sensor_readings, gas_concentrations, 1)

    # Coefficients of the calibration equation (y = mx + c)
    slope = calibration_curve[0]
    intercept = calibration_curve[1]

    # Calculate gas concentration
    gas_concentration = slope * raw_sensor_reading + intercept

    return gas_concentration

# Raw sensor readings
sensor_readings_mq9 = [200, 210, 220, 230, 245, 255]  # Example data, replace with actual readings
# Corresponding gas concentrations
gas_concentrations_mq9 = [0.5, 7.045, 12.773, 19.045, 29.136, 35]  # Example data, replace with actual concentrations

# Raw sensor readings
sensor_readings_mq2 = [249, 250, 251, 252, 254, 255]
# Corresponding gas concentrations
gas_concentrations_mq2 = [400, 571.428, 585.714, 600, 628.571, 1000]

# Raw sensor readings
sensor_readings_mq4 = [249, 250, 251, 252, 254, 255]
# Corresponding gas concentrations
gas_concentrations_mq4 = [400, 7.045, 12.773, 19.045, 29.136, 1000]


raw_sensor_reading = 255  # Example data, replace with actual sensor reading
gas_concentration = calculate_gas_concentration(sensor_readings_mq2, gas_concentrations_mq2, raw_sensor_reading)
print("MQ-9 Gas Concentration:", gas_concentration, "PPM")