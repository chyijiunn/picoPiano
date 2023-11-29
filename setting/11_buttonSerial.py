
'''
#print PIN define
for i in range(28):
    buttonName = 'button' + str(i)
    print(buttonName,' = machine.Pin( ' , str( i ),', machine.Pin.IN, machine.Pin.PULL_UP)')
'''
# print tune
T1 = ['c','d','e','f','g','a','b']
T2 = [1,2,3,4,5,6,7]
for i in range(len(T2)):
    for j in range(len(T1)):
        print("\'",T1[j],T2[i],"\'",',',sep='',end ='')
'''
#print if
tune = ['c3','d3','e3','f3','g3','a3','b3','c4','d4','e4','f4','g4','a4','b4','c5','d5','e5','f5','g5','a5','b5','c6','d6','e6','f6','g6','a6','b6']
for j in range(28):
    print('if button',str(j),'.value() == 0:speaker.play(',"\'",str(tune[j]),"\'",',tempo)',sep='')

tune2 = ['c4','d4','e4','f4','g4','a4','b4','c5','d5','e5','f5','g5','a5','b5','c6','d6','e6','f6','g6','a6','b6']
for j in range(len(tune2)):
    print('if button',str(15-j),'.value() == 0:speaker.play(',"\'",str(tune2[j]),"\'",',tempo)',sep='')'''