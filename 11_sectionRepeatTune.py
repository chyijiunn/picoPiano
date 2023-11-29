from picozero import Speaker
import random
speaker = Speaker(20)
tempo = 60/120
tune = ['c1','d1','e1','f1','g1','a1','b1','c2','d2','e2','f2','g2','a2','b2','c3','d3','e3','f3','g3','a3','b3','c4','d4','e4','f4','g4','a4','b4','c5','d5','e5','f5','g5','a5','b5','c6','d6','e6','f6','g6','a6','b6','c7','d7','e7','f7','g7','a7','b7']
tune1 = []
tune2 = []

for i in range(4):
    tune1.append(random.randint(0,48))
    tune2.append(random.randint(0,48))

print(tune1)

for i in range(4):
    speaker.play(tune[tune1[i]],tempo)
for i in range(4):
    speaker.play(tune[tune1[i]],tempo)
for i in range(4):
    speaker.play(tune[tune2[i]],tempo)

speaker.off()