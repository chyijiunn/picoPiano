from machine import Pin, PWM
from utime import sleep
from picozero import Speaker
import math
buzzer = PWM(Pin(21))
speaker = Speaker(21)
for i in range(16):
    exec('button' + str(i) + ' = Pin(' + str(i) + ',Pin.IN, Pin.PULL_UP)' )
t = 60 / 180  # 每分鐘 180 拍

tune_0 = [['a4', t / 2], ['c5', t / 2], ['e5', t], ['g5', t],['f#5', t], ['d5', t * 1.5], ['e5', t / 2], ['a4', t],['g5', t], ['f#5', t / 2], ['e5', t / 2], ['c5', t],['d5', t * 1.5], ['e5', t / 2], ['a4', t], ['g4', t * 2],['c5', t / 2], ['e5', t / 2], ['g5', t], ['b5', t],['a5', t], ['f#5', t * 1.5], ['g5', t / 2], ['c5', t],['b5', t], ['a5', t / 2], ['g5', t / 2], ['e5', t],['f#5', t * 1.5], ['g5', t / 2], ['c5', t], ['b4', t * 2]]
tune_1 = [['e5', t / 2], ['e5', t / 2], ['e5', t],['c5', t / 2],['e5', t],['g5', t * 1.5],['g4', t * 1.5],['c5', t],['g4', t * 1.5],['e4', t * 1.5],['a4', t],['b4', t / 2],['a#4', t / 2],['a4', t],['g4', t],['e5', t / 2],['g5', t / 2],['a5', t],['f5', t / 2],['g5', t / 2],['e5', t / 2],['c5', t / 2],['d5', t / 2],['b4', t * 1.5],['g4', t / 2],['e4', t * 1.5],['a4', t],['b4', t / 2],['a#4', t / 2],['a4', t],['g4', t]]

speaker.play(tune_1)
speaker.off()

n=69

def noteplay(note):
    buzzer.duty_u16(1000) # Volumn
    buzzer.freq(note)
    sleep(0.08)                                                                          
    buzzer.duty_u16(0)
    
def musicMode():
    while True:
        for i in range(2):#可增加到15，對應鍵盤 GP0~15
            exec('if button'+str(15-i)+'.value() == 0:speaker.play(tune_'+str(i)+')')
while True:
    for i in range(16):
        exec('if button'+str(15-i)+'.value() == 0:noteplay(int(round(440*math.pow(2,(n-69+i)/12),0)))')
    if button15.value() == 0 and button14.value() == 0:musicMode()#同時按下 GP 15,14 進入音樂模式
