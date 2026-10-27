from machine import Pin, I2C
import ssd1306
import time

# I2C0: SDA = GP0, SCL = GP1
i2c = I2C(
    0,
    sda=Pin(0),
    scl=Pin(1),
    freq=400000
)

# OLED: 128 x 64
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

clock = 0

while True:
    oled.fill(0)

    oled.text("Hello Pico!", 0, 0)
    oled.text("OLED is working", 0, 16)
    oled.text("clock: " + str(clock), 0, 40)

    oled.show()

    clock += 1
    time.sleep(1)
