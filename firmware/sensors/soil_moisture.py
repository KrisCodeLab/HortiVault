import random
import time
from machine import ADC, Pin

class SoilMoistureSensor:


    def __init__(self, adc_pin, air_value, water_value, test_mode):
        self.adc_pin = ADC(Pin(adc_pin))
        self.air_value = air_value
        self.water_value = water_value
        self.test_mode = test_mode

        self.adc_pin.atten(ADC.ATTN_11DB)


    def read(self):
        """Methode für main.py. Prüft ob Sensor im Test oder Livemodus läuft."""
        if self.test_mode:
            return self._test_read()
        return self._real_read()      
    

    def _real_read(self):
        # Korrekte Kalibrierung prüfen
        if self.air_value <= self.water_value:
                print("[Warnung] Soil Moisture Sensor ist noch nicht kalibriert!")
                return {"moisture": 0.0}

        try:
            # Spannung am ADC Pin messen

            raw_moist = 0

            for _ in range(30):
                raw_moist += self.adc_pin.read()
                time.sleep(0.01)

            raw_moist = raw_moist // 30

            # Meswert in Prozentangabe umrechnen
            moist = ((self.air_value - raw_moist) / (self.air_value - self.water_value)) * 100
            moist = max(0, min(100, moist))

            return {
                "moisture": round(moist, 1)
            }
        
        except Exception as e:
            print(f"[Sensor Error] Soil Moisture Sensor: {e}")
            return {"moisture": None}


    def _test_read(self):
        """Generiert Mock-Daten für die Bodenfeuchtigkeit (20-80%)."""
        moist = round(random.uniform(20.0, 80.0), 1)

        return {
            "moisture": moist
        }

