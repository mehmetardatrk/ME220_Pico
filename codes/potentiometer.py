# Yan bacaklar artı ve eksi orta bacak sinyal
from machine import ADC, Pin
import time

# ADC0 pini (GP26) analog giris olarak tanimlanir
potentiometer = ADC(Pin(26))

while True:
    # 16-bit ham analog degeri okur (0 ile 65535 arasi)
    raw_value = potentiometer.read_u16()
    
    # Okunan degeri 0 - 3.3V gerilim degerine donusturur
    voltage = (raw_value / 65535) * 3.3
    
    # Okunan degerleri konsola yazdirir
    print(f"Raw: {raw_value} | Voltage: {voltage:.2f}V")
    
    time.sleep(0.2)
