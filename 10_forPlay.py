import random
from picozero import Speaker
speaker = Speaker(21)
tempo = 60/150 #tempo = 60/150 #(時間間隔 秒，BPM 120--> 60/120，150-->60/150)

tune = ['c4','d4','e4','f4','g4','a4','b4']

for i in range(4):
    speaker.play(tune[random.randint(0,6)],tempo)
    


