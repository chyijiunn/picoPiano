import machine , utime
LED = machine.Pin(25,machine.Pin.OUT)#控制內建的LED
LED.value(1)
utime.sleep(1)
LED.value(0)
utime.sleep(1)
