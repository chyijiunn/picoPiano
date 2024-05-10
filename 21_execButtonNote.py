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
            
    '''
	if button(15-i).value() == 0:noteplay(int(round(440*math.pow(2,(n-69+i)/12),0)))
    if button15.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+0)/12),0)))
    if button14.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+1)/12),0)))
    if button13.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+2)/12),0)))
    if button12.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+3)/12),0)))
    if button11.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+4)/12),0)))
    if button10.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+5)/12),0)))
    if button9.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+6)/12),0)))
    if button8.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+7)/12),0)))
    if button7.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+8)/12),0)))
    if button6.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+9)/12),0)))
    if button5.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+10)/12),0)))
    if button4.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+11)/12),0)))
    if button3.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+12)/12),0)))
    if button2.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+13)/12),0)))
    if button1.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+14)/12),0)))
    if button0.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+15)/12),0)))


while 1:
    for i in range(16):
        if exec('button' + str(i) + '==0:noteplay(int(round(440*math.pow(2,('+str(i)+'+n-69)/12),0)))')
    
'''    

