from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(19))
#https://zh.wikipedia.org/zh-tw/%E9%9F%B3%E9%AB%98
buzzer.freq(10080)
buzzer.duty_u16(60000)
sleep(0.5)                                                                                 
buzzer.duty_u16(0)
sleep(0.5)