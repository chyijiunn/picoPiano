import math
'''
n = 69#a4 midi 69 = 440 Hz
a = 440*math.pow(2,(n-69)/12)#formula
print(n , a)#test
'''
tone = 4 #if C4大調
notesep = [0,2,4,5,7,9,11] #midi num = 60 ,62,64,65,67,69,71 分別減去 60 
'''
for j in range(7):
    b = 12*(tone+1)+notelist[j]
    print(b)
'''    
notelist = []
for i in range(3):
    for j in range(7):
        notelist.append(12*(tone+1)+notesep[j])
    tone = tone +1 
del notelist[:5]#刪除最後五個，因為只有~GP15，共16鍵

print(len(notelist),type(notelist[0]))
'''
for i in range(60,72,1):
    print(i,int(round(440*math.pow(2,(i-69)/12),0)))

   ''' 