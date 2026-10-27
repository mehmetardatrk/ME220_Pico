from machine import Pin, PWM
import time

# Motor surucunun yon pinleri cikis olarak tanimlanir
in1 = Pin(17, Pin.OUT)
in2 = Pin(18, Pin.OUT)

# Motor hiz kontrolu icin ENA pinine 1000 Hz PWM atanir
ena = PWM(Pin(16))
ena.freq(1000)

def set_motor(speed, direction="forward"):
    # Hizi 0 ile 100 arasinda sinirlandirir
    speed = max(0, min(100, speed))
    
    # 0-100 araligindaki yuzdeyi 16-bit PWM gorev dongusune (0 - 65535) donusturur
    duty = int((speed / 100) * 65535)
    ena.duty_u16(duty)
    
    # Donus yonune gore mantik pinlerini ayarlar
    if direction == "forward":
        in1.high()
        in2.low()
    elif direction == "backward":
        in1.low()
        in2.high()
    elif direction == "stop":
        in1.low()
        in2.low()
        ena.duty_u16(0)

# 1. Ileri yonde %70 hizla calistir
print("Moving forward...")
set_motor(70, "forward")
time.sleep(2)

# 2. Motoru durdur
print("Stopping...")
set_motor(0, "stop")
time.sleep(1)

# 3. Geri yonde %50 hizla calistir
print("Moving backward...")
set_motor(50, "backward")
time.sleep(2)

# 4. Hizi kademeli artirma (Ramping)
print("Accelerating...")
in1.high()
in2.low()
for spd in range(0, 101, 10):
    duty = int((spd / 100) * 65535)
    ena.duty_u16(duty)
    time.sleep(0.2)

# 5. Sistemi tamamen kapat ve PWM sinyalini serbest birak
set_motor(0, "stop")
ena.deinit()
print("Test completed.")
