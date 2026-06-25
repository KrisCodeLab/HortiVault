import time
import json
import config
from sensors import HygroTempSensor 

print("HortiVault – System bootet...")

ambient_sensor = HygroTempSensor(
    i2c_bus=config.I2C_BUS, 
    scl_pin=config.PIN_SCL, 
    sda_pin=config.PIN_SDA, 
    test_mode=config.TEST_MODE
)


while True:
    data = ambient_sensor.read()
    
    payload = {
        "temperature": data["temperature"],
        "humidity": data["humidity"]
    }
    
    print(json.dumps(payload))
    
    time.sleep(5)