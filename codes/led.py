from machine import Pin

# Pin tanımlamaları
yesil_led = Pin(5, Pin.OUT)
kirmizi_led = Pin(4, Pin.OUT)

# LED'leri yak
yesil_led.value(1)
kirmizi_led.value(1)

# Konsola yazdır
print("wiring OK")
