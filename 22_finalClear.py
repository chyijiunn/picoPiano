from machine import Pin, PWM
from utime import sleep
import math
buzzer = PWM(Pin(21))
for i in range(16):
    exec('button' + str(i) + ' = Pin(' + str(i) + ',Pin.IN, Pin.PULL_UP)' )

n=69

def noteplay(note):
    buzzer.freq(note)
    buzzer.duty_u16(1000)
    sleep(0.08)                                                                                 
    buzzer.duty_u16(0)

while True:
    for i in range(16):
        exec('if button'+str(15-i)+'.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+i)/12),0)))')
