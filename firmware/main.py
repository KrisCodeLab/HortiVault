import time
import json
import sensor_manager
import gc

print("hortivault – System bootet...")

# Sensoreinstellungen laden und Sensoren initialisieren
active_sensors = sensor_manager.load_and_build()

print("\nAlle Sensoren initialisiert. Starte Messzyklus...\n")

# Sensormesswerte kontinuierlich auslesen und ausgeben
while True:
    sensor_data = {}
    
    for sensor_name, sensor_obj in active_sensors.items():
        try:
            sensor_data[sensor_name] = sensor_obj.read()
        except Exception as e:
            sensor_data[sensor_name] = {"error": str(e)}
    
    if sensor_data:
        try:
            print(json.dumps(sensor_data))
        # Excpetion, falls der Server nicht erreichbar ist oder der Puffer blockiert ist
        except OSError as e:
            print(json.dumps({"error": str(e)}))
    else:
        print("[Warnung] Keine Sensoren aktiv.")
        
    gc.collect()
    time.sleep(5)