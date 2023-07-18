# Import the functions from mq2.py, mq4.py, and mq5.py
from mq2 import MQ as mq2
from mq4 import MQ as mq4
from mq9 import MQ as mq9
import time

mq2 = mq2(analogPin=0)
mq4 = mq4(analogPin=2)
mq9 = mq9(analogPin=1)
while True:
    gas_percentage = mq2.MQPercentage()
    print("MQ-2 Gas Percentage (LPG):", gas_percentage["GAS_LPG"])
    print("MQ-2 Gas Percentage (CO):", gas_percentage["CO"])
    print("MQ-2 Gas Percentage (Smoke):", gas_percentage["SMOKE"])
    gas_percentage = mq4.MQPercentage()
    print("MQ-4 Gas Percentage (Methane):", gas_percentage["METHANE"])
    print("MQ-4 Gas Percentage (CNG):", gas_percentage["CNG"])
    gas_percentage = mq9.MQPercentage()
    print("MQ-9 Gas Percentage (CO):", gas_percentage["CO"])
    print("MQ-9 Gas Percentage (Flammable):", gas_percentage["FLAMMABLE"])
    time.sleep(1)