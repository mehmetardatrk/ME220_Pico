from machine import Pin, PWM, time_pulse_us
import time

trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)
buzzer = PWM(Pin(26))
buzzer.duty_u16(0)
buzzer.freq(2000)

def beep_on():
    buzzer.duty_u16(30000)

def beep_off():
    buzzer.duty_u16(0)

def get_distance_cm():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    t = time_pulse_us(echo, 1, 30000)
    if t < 0:
        return None
    return t * 0.0343 / 2

while True:
    d = get_distance_cm()

    if d > 50:
        beep_off()
        time.sleep(0.1)
    elif d >= 10:                  
        beep_on()
        time.sleep(0.05)
        beep_off()
        time.sleep(0.5)
    else:                          
        beep_on()
        time.sleep(0.1)
