import math
n = 69
a = 440*math.pow(2,(n-69)/12)
print(a)

for i in range(60,112,1):
    print(i,int(round(440*math.pow(2,(i-69)/12),0)))