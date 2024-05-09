from machine import Pin, PWM
buzzer = PWM(Pin(21))
buzzer.freq(262)#頻率表可參照 https://zh.wikipedia.org/zh-tw/音高
buzzer.duty_u16(1000)