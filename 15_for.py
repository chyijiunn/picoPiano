import random
tune = ['c4','d4','e4','f4','g4','a4','b4']

for i in range(4):#對 i 來說，每次會 +1，先從 0 開始，到 4 之前，共 4 次
    x = random.randint(0,6)
    print(tune[x])

