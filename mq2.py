import time
import math
from ADC0832 import ADC0832

class MQ():
    MQ_PIN = 0
    RL_VALUE = 5
    RO_CLEAN_AIR_FACTOR = 9.83
    CALIBRATION_SAMPLE_TIMES = 50
    CALIBRATION_SAMPLE_INTERVAL = 500
    READ_SAMPLE_INTERVAL = 50
    READ_SAMPLE_TIMES = 5
    GAS_LPG = 0
    GAS_CO = 1
    GAS_SMOKE = 2

    def __init__(self, Ro=10, analogPin=0):
        self.Ro = Ro
        self.MQ_PIN = analogPin
        self.adc = ADC0832()
        self.LPGCurve = [2.3, 0.21, -0.47]
        self.COCurve = [2.3, 0.72, -0.34]
        self.SmokeCurve = [2.3, 0.53, -0.44]

        print("Calibrating...")
        self.Ro = self.MQCalibration(self.MQ_PIN)
        print("Calibration is done...\n")
        print("Ro = %f kohm" % self.Ro)

    def MQPercentage(self):
        val = {}
        read = self.MQRead(self.MQ_PIN)
        val["GAS_LPG"] = self.MQGetGasPercentage(read / self.Ro, self.GAS_LPG)
        val["CO"] = self.MQGetGasPercentage(read / self.Ro, self.GAS_CO)
        val["SMOKE"] = self.MQGetGasPercentage(read / self.Ro, self.GAS_SMOKE)
        return val

    def MQResistanceCalculation(self, raw_adc):
        return float(self.RL_VALUE * (1023.0 - raw_adc) / float(raw_adc))

    def MQCalibration(self, mq_pin):
        val = 0.0
        for i in range(self.CALIBRATION_SAMPLE_TIMES):
            val += self.MQResistanceCalculation(self.adc.analogRead(mq_pin))
            time.sleep(self.CALIBRATION_SAMPLE_INTERVAL / 1000.0)

        val = val / self.CALIBRATION_SAMPLE_TIMES
        val = val / self.RO_CLEAN_AIR_FACTOR
        return val

    def MQRead(self, mq_pin):
        rs = 0.0
        for i in range(self.READ_SAMPLE_TIMES):
            rs += self.MQResistanceCalculation(self.adc.analogRead(mq_pin))
            time.sleep(self.READ_SAMPLE_INTERVAL / 1000.0)

        rs = rs / self.READ_SAMPLE_TIMES
        return rs

    def MQGetGasPercentage(self, rs_ro_ratio, gas_id):
        if gas_id == self.GAS_LPG:
            return self.MQGetPercentage(rs_ro_ratio, self.LPGCurve)
        elif gas_id == self.GAS_CO:
            return self.MQGetPercentage(rs_ro_ratio, self.COCurve)
        elif gas_id == self.GAS_SMOKE:
            return self.MQGetPercentage(rs_ro_ratio, self.SmokeCurve)
        return 0

    def MQGetPercentage(self, rs_ro_ratio, pcurve):
        return math.pow(10, (((math.log(rs_ro_ratio) - pcurve[1]) / pcurve[2]) + pcurve[0]))


mq = MQ()
while True:
    gas_percentage = mq.MQPercentage()
    print("MQ-2 Gas Percentage (LPG):", gas_percentage["GAS_LPG"])
    print("MQ-2 Gas Percentage (CO):", gas_percentage["CO"])
    print("MQ-2 Gas Percentage (Smoke):", gas_percentage["SMOKE"])
    time.sleep(1)
