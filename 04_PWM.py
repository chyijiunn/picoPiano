from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(21))
buzzer.freq(262)
buzzer.duty_u16(1000)
sleep(0.5)                                                                                 
buzzer.duty_u16(0)
sleep(0.5)