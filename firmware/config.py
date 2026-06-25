# ==========================================
# HortiVault - ESP32 WROOM Configuration
# ==========================================

# --- SYSTEM-MODUS ---
# True  = Simulation
# False = Live-Betrieb 
TEST_MODE = True  

# --- HARDWARE PINS ---

# 1. Bus-Systeme (I2C)
I2C_BUS = 0
PIN_SCL = 22
PIN_SDA = 21

# 2. Analoge Eingänge (ADC)
PIN_SOIL = 34      
PIN_LIGHT = 35    

# 3. Digitale Sensoren
PIN_WATER_TRIG = 16 # Wasserstand Trigger
PIN_WATER_ECHO = 17 # Wasserstand Echo

# --- NETZWERK (Für Projektphase 9) ---
WIFI_SSID = "Dein_WLAN_Name"
WIFI_PASS = "Dein_WLAN_Passwort"
BACKEND_URL = "BACKEND_URL"