from machine import Pin, PWM
import time

servo = PWM(Pin(15))
servo.freq(50) # 50 Hz (20ms periyot)

def set_angle(angle):
    # 0 - 180 dereceyi 1638 - 8192 aralığına haritalandırır
    # (Pico 16-bit PWM kullanır: 0 - 65535)
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)

# 0, 90 ve 180 dereceye sırayla geçiş testi
while True:
    set_angle(0)
    time.sleep(1)
    set_angle(90)
    time.sleep(1)
    set_angle(180)
    time.sleep(1)
