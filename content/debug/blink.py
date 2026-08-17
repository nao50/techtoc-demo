# LED を 5 回点滅させる。
#
# 実行すると、この場で機器へ送られて走ります（焼き込みではありません）。
# 止めたいときは端末で Ctrl-C。
from machine import Pin
import time

led = Pin(2, Pin.OUT)

for i in range(5):
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.2)
    print("blink", i + 1)

print("done")
