from machine import SoftI2C, Pin

# Deine eingestellten Pins
i2c = SoftI2C(scl=Pin(4), sda=Pin(2), freq=10000)

print("Scanne I2C Bus...")
devices = i2c.scan()

if len(devices) == 0:
    print("Kein Sensor gefunden! (Hardware/Kabel-Problem)")
else:
    print("Geräte gefunden unter Adresse(n):")
    for device in devices:
        print(f"- Hex: {hex(device)}")