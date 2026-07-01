import serial
import time
import threading
import queue
import json

class SerialListener:


    def __init__(self, USB_PORT, BAUD):
        self.USB_PORT = USB_PORT
        self.BAUD = BAUD
        
        self.interface = None
        self.queue = queue.Queue()


    def _listen(self):
        """USB Port aktivieren, Puffer löschen, Daten auslesen und Daten in Queue schicken"""
        while True:
            try:
                if self.interface == None:
                    self.interface = serial.Serial(self.USB_PORT, self.BAUD, timeout=1)
                    time.sleep(0.05)
                    self.interface.reset_input_buffer()
            except Exception as e:
                print(f"[ERROR]: {e} USB PORT {self.USB_PORT} nicht belegt!")
                time.sleep(5)
                continue

            while True:
                try:
                    if self.interface.in_waiting > 0:
                        time.sleep(0.05)
                        sensor_data = self.interface.readline().decode('utf-8').strip()
                        try: 
                            self.queue.put(json.loads(sensor_data))
                        except json.JSONDecodeError:
                            print(sensor_data)
                except Exception as e:
                    self.interface = None
                    print(f"[ERROR]: {e} USB PORT {self.USB_PORT} nicht belegt!")
                    break

    
    def start_listener_thread(self):
        """Thread starten und _listen ausführen"""
        new_thread = threading.Thread(target=self._listen, daemon=True)                        
        new_thread.start()


    def get_data(self):
        """Queue auslesen"""
        if not self.queue.empty():
            return self.queue.get()
        