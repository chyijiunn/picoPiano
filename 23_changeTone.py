from machine import Pin, PWM
from utime import sleep
import math
buzzer = PWM(Pin(21))
for i in range(16):
    exec('button' + str(i) + ' = Pin(' + str(i) + ',Pin.IN, Pin.PULL_UP)' )

tone = 4 #if C4大調
notesep = [0,2,4,5,7,9,11] #C4 midi num = 60 ,62,64,65,67,69,71 分別減去 60
notelist = []
for i in range(3):
    for j in range(7):
        notelist.append(12*(tone+1)+notesep[j])
    tone = tone +1 
del notelist[:5]

def noteplay(note):
    buzzer.freq(note)
    buzzer.duty_u16(1000)
    sleep(0.01)                                                                                 
    #buzzer.duty_u16(0)

while True:
    for i in range(16):
        exec('if button'+str(15-i)+'.value() == 0:noteplay(int(round(440*math.pow(2,((notelist[i])-69)/12),0)))')

