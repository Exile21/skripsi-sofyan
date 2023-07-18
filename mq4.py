import smbus
import time
import math

pcf8591_address = 0x48
bus = smbus.SMBus(1)

def read_analog(adc_channel):
    bus.write_byte(pcf8591_address, adc_channel)
    bus.read_byte(pcf8591_address)  # dummy read to start conversion
    analog_value = bus.read_byte(pcf8591_address)
    return analog_value

class MQ():
    MQ_PIN = 0
    RL_VALUE = 5
    RO_CLEAN_AIR_FACTOR = 9.83
    CALIBRATION_SAMPLE_TIMES = 50
    CALIBRATION_SAMPLE_INTERVAL = 500
    READ_SAMPLE_INTERVAL = 50
    READ_SAMPLE_TIMES = 5
    GAS_METHANE = 0
    GAS_CNG = 1

    def __init__(self, Ro=10, analogPin=0):
        self.Ro = Ro
        self.MQ_PIN = analogPin

        print("Calibrating...")
        self.Ro = self.MQCalibration(self.MQ_PIN)
        print("Calibration is done...\n")
        print("Ro = %f kohm" % self.Ro)

    def MQPercentage(self):
        val = {}
        read = self.MQRead(self.MQ_PIN)
        val["METHANE"] = self.MQGetGasPercentage(read / self.Ro, self.GAS_METHANE)
        val["CNG"] = self.MQGetGasPercentage(read / self.Ro, self.GAS_CNG)
        return val

    def MQResistanceCalculation(self, raw_adc):
        return float(self.RL_VALUE * (1023.0 - raw_adc) / float(raw_adc))

    def MQCalibration(self, mq_pin):
        val = 0.0
        for i in range(self.CALIBRATION_SAMPLE_TIMES):
            val += self.MQResistanceCalculation(read_analog(mq_pin))
            time.sleep(self.CALIBRATION_SAMPLE_INTERVAL / 1000.0)

        val = val / self.CALIBRATION_SAMPLE_TIMES
        val = val / self.RO_CLEAN_AIR_FACTOR
        return val

    def MQRead(self, mq_pin):
        rs = 0.0
        for i in range(self.READ_SAMPLE_TIMES):
            rs += self.MQResistanceCalculation(read_analog(mq_pin))
            time.sleep(self.READ_SAMPLE_INTERVAL / 1000.0)

        rs = rs / self.READ_SAMPLE_TIMES
        return rs

    def MQGetGasPercentage(self, rs_ro_ratio, gas_id):
        if gas_id == self.GAS_METHANE:
            return self.MQGetPercentage(rs_ro_ratio, [2.3, 0.21, -0.47])
        elif gas_id == self.GAS_CNG:
            return self.MQGetPercentage(rs_ro_ratio, [2.3, 0.72, -0.34])
        return 0

    def MQGetPercentage(self, rs_ro_ratio, pcurve):
        return math.pow(10, (((math.log(rs_ro_ratio) - pcurve[1]) / pcurve[2]) + pcurve[0]))

mq = MQ(analogPin=2)
while True:
    gas_percentage = mq.MQPercentage()
    print("MQ-4 Gas Percentage (Methane):", gas_percentage["METHANE"])
    print("MQ-4 Gas Percentage (CNG):", gas_percentage["CNG"])
    time.sleep(1)
