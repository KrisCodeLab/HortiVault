import time
import random
from machine import I2C, Pin

class HygroTempSensor:


    def __init__(self, i2c_bus=0, scl_pin=22, sda_pin=21, test_mode=False):
        self.test_mode = test_mode
        self.address = 0x44  # I2C Adresse für den CHT832X
        
        self.i2c_bus = i2c_bus
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin
        self.i2c = None


    def read(self):
        """Diese Methode in der main.py verwenden."""
        if self.test_mode:
            return self._test_read()
        return self._real_read()


    def _real_read(self):
        """Liest den CHT832X über I2C aus."""
        if self.i2c is None:
            self.i2c = I2C(self.i2c_bus, scl=Pin(self.scl_pin), sda=Pin(self.sda_pin))
            time.sleep(0.1)
            
        try:
            # 1. Start-Befehl senden (0x24 und 0x00)
            self.i2c.writeto(self.address, bytes([0x24, 0x00]))
            
            # 2. 60ms Pause (delay(60))
            time.sleep_ms(60)
            
            # 3. 6 Bytes anfordern
            buf = self.i2c.readfrom(self.address, 6)
            
            # 4. Daten zusammensetzen (Checksummen in buf[2] und buf[5] werden ignoriert)
            temp_raw = (buf[0] << 8) | buf[1]
            humi_raw = (buf[3] << 8) | buf[4]
            
            # 5. Formeln DFRobot
            temp = -45.0 + 175.0 * (temp_raw / 65535.0)
            hum = 100.0 * (humi_raw / 65535.0)
            
            return {
                "temperature": round(temp, 1),
                "humidity": round(hum, 1)
            }
            
        except Exception as e:
            print(f"[Sensor Error] HygroTemp: {e}")
            return {"temperature": None, "humidity": None}


    def _test_read(self):
        """Generiert Mock-Daten."""
        temp = round(random.uniform(18.0, 26.0), 1)
        hum = round(random.uniform(50.0, 75.0), 1)
        return {
            "temperature": temp,
            "humidity": hum
        }
