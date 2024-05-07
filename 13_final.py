from picozero import Speaker
import machine ,utime,random
LED = machine.Pin(25,machine.Pin.OUT)#控制內建的LED
LED.value(1)

speaker = Speaker(19)
tempo = 60/120
tune = ['c1','d1','e1','f1','g1','a1','b1','c2','d2','e2','f2','g2','a2','b2','c3','d3','e3','f3','g3','a3','b3','c4','d4','e4','f4','g4','a4','b4','c5','d5','e5','f5','g5','a5','b5','c6','d6','e6','f6','g6','a6','b6','c7','d7','e7','f7','g7','a7','b7']
tune1 = []
tune2 = []
for i in range(4):
    tune1.append(random.randint(0,48))
    tune2.append(random.randint(0,48))

for i in range(4):
    speaker.play(tune[tune1[i]],tempo)
for i in range(4):
    speaker.play(tune[tune1[i]],tempo)
for i in range(4):
    speaker.play(tune[tune2[i]],tempo)
    
button0  = machine.Pin(  0 , machine.Pin.IN, machine.Pin.PULL_UP)
button1  = machine.Pin(  1 , machine.Pin.IN, machine.Pin.PULL_UP)
button2  = machine.Pin(  2 , machine.Pin.IN, machine.Pin.PULL_UP)
button3  = machine.Pin(  3 , machine.Pin.IN, machine.Pin.PULL_UP)
button4  = machine.Pin(  4 , machine.Pin.IN, machine.Pin.PULL_UP)
button5  = machine.Pin(  5 , machine.Pin.IN, machine.Pin.PULL_UP)
button6  = machine.Pin(  6 , machine.Pin.IN, machine.Pin.PULL_UP)
button7  = machine.Pin(  7 , machine.Pin.IN, machine.Pin.PULL_UP)
button8  = machine.Pin(  8 , machine.Pin.IN, machine.Pin.PULL_UP)
button9  = machine.Pin(  9 , machine.Pin.IN, machine.Pin.PULL_UP)
button10  = machine.Pin(  10 , machine.Pin.IN, machine.Pin.PULL_UP)
button11  = machine.Pin(  11 , machine.Pin.IN, machine.Pin.PULL_UP)
button12  = machine.Pin(  12 , machine.Pin.IN, machine.Pin.PULL_UP)
button13  = machine.Pin(  13 , machine.Pin.IN, machine.Pin.PULL_UP)
button14  = machine.Pin(  14 , machine.Pin.IN, machine.Pin.PULL_UP)
button15  = machine.Pin(  15 , machine.Pin.IN, machine.Pin.PULL_UP)

tempo = 0.08 

while True:
    if button15.value() == 0:speaker.play('c4',tempo)
    if button14.value() == 0:speaker.play('d4',tempo)
    if button13.value() == 0:speaker.play('e4',tempo)
    if button12.value() == 0:speaker.play('f4',tempo)
    if button11.value() == 0:speaker.play('g4',tempo)
    if button10.value() == 0:speaker.play('a4',tempo)
    if button9.value() == 0:speaker.play('b4',tempo)
    if button8.value() == 0:speaker.play('c5',tempo)
    if button7.value() == 0:speaker.play('d5',tempo)
    if button6.value() == 0:speaker.play('e5',tempo)
    if button5.value() == 0:speaker.play('f5',tempo)
    if button4.value() == 0:speaker.play('g5',tempo)
    if button3.value() == 0:speaker.play('a5',tempo)
    if button2.value() == 0:speaker.play('b5',tempo)
    if button1.value() == 0:speaker.play('c6',tempo)
    if button0.value() == 0:speaker.play('d6',tempo)
    speaker.off()

