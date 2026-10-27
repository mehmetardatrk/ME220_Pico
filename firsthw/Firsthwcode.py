from machine import Pin, ADC, PWM, time_pulse_us
import time

trig=Pin(21,Pin.OUT)
echo=Pin(20,Pin.IN)

servo=PWM(Pin(11))
servo.freq(50)

buzzer=PWM(Pin(9))
buzzer.duty_u16(0)

pot=ADC(Pin(26))

button=Pin(6,Pin.IN, Pin.PULL_DOWN)
greenled=Pin(5, Pin.OUT)
redled=Pin(4, Pin.OUT)

doorangle=0
lastbutton=0
visitors=0


def maprange(x, inmin, inmax, outmin, outmax):
    return (x-inmin)*(outmax-outmin)/(inmax-inmin)+outmin

def getdistance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    t = time_pulse_us(echo, 1, 30000)

    if t < 0:
        return None
    
    dist = (t * 0.0343) / 2
    return dist

def getthreshold():
    val=pot.read_u16()
    thr=maprange(val,0,65535,10,100)
    return int(round(thr))
def personpresent(dist=None, thr=None):
    if dist is None:
        dist = getdistance()
    if thr is None:
        thr = getthreshold()

    if dist is not None and dist < thr:
        return True
    return False


def setangle(angle):
    global doorangle

    if angle < 0:
        angle = 0
    if angle > 180:
        angle=180
    
    doorangle=angle

    pulse_us=maprange(angle,0,180,500,2500)
    duty=int((pulse_us/20000)*65535)
    servo.duty_u16(duty)

def beep(times):
    for i in range(times):
        buzzer.freq(1000)
        buzzer.duty_u16(30000)
        time.sleep(0.1)
        buzzer.duty_u16(0)
        time.sleep(0.1)

def opendoor():
    beep(2)
    greenled.value(1)
    redled.value(0)
    

    for angle in range (doorangle, 91, 3):
        setangle(angle)
        time.sleep(0.02)
    setangle(90)


def waittillclear():
    count=0
    while count < 30:
        if personpresent():
            count=0
        else :
            count=count+1
        time.sleep(0.1)

def closedoor():
    greenled.value(0)
    steps=0
    ledandbuzzeron= True

    for angle in range(doorangle,-1,-3):
        if personpresent():
            buzzer.duty_u16(0)
            return False

        if steps %10==0:
            if ledandbuzzeron:
                redled.value(1)
                buzzer.freq(2000)
                buzzer.duty_u16(30000)
                ledandbuzzeron=False
            else:
                redled.value(0)
                buzzer.duty_u16(0)
                ledandbuzzeron=True
        setangle(angle)
        time.sleep(0.02)
        steps=steps+1
    buzzer.duty_u16(0)
    redled.value(1)
    return True

def buttonpressed():
    global lastbutton
    current=button.value()
    pressed=False

    if current != lastbutton:
        time.sleep(0.02)  
        current = button.value()
        if current == 1 and lastbutton == 0:
            pressed = True
        lastbutton = current
    return pressed

setangle(0)
redled.value(1)
greenled.value(0)
buzzer.duty_u16(0)

while True:
    dist = getdistance()
    thr = getthreshold()
    
    
    if dist is None:
        print("dist=None thr=" + str(thr) + " cm visitors=" + str(visitors))
    else:
        print("dist=" + str(round(dist, 1)) + " cm thr=" + str(thr) + " cm visitors=" + str(visitors) +" door is closed")
    
    
    if personpresent(dist, thr) or buttonpressed():
        doorclosed = False
        
        while not doorclosed:
            opendoor()
            print("dist=" + str(round(dist, 1)) + " cm thr=" + str(thr) + " cm visitors=" + str(visitors) +" door is open")
    
            waittillclear()
            doorclosed = closedoor()
            
        visitors += 1
        redled.value(1)
        greenled.value(0)
        buzzer.duty_u16(0)
        
    time.sleep(0.2)
