from picozero import Speaker
from random import randint
speaker = Speaker(20)
tempo = 60/120 
ly = ['c1','d1','e1','f1','g1','a1','b1','c2','d2','e2','f2','g2','a2','b2','c3','d3','e3','f3','g3','a3','b3','c4','d4','e4','f4','g4','a4','b4','c5','d5','e5','f5','g5','a5','b5','c6','d6','e6','f6','g6','a6','b6','c7','d7','e7','f7','g7','a7','b7']

a1 = []
a2 = []
a3 = []
for i in range(4):
    a1.append(ly[randint(0,48)])
    a2.append(ly[randint(0,48)])
    a3.append(ly[randint(0,48)])

print(a1)
for k in range(4):
    speaker.play(a1[k],tempo)
for k in range(4):
    speaker.play(a1[k],tempo)
print(a2)
for k in range(4):
    speaker.play(a2[k],tempo)

print(a3)
for k in range(4):
    speaker.play(a3[k],tempo)
for k in range(4):
    speaker.play(a3[k],tempo)
print(a2)
for k in range(4):
    speaker.play(a2[k],tempo)

