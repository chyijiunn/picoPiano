from picozero import Speaker
speaker = Speaker(21)
tempo = 3 #設定為節奏時間

speaker.play('c4', tempo) #節奏時間統一由上方輸入，可以直接輸一曲子，但先將之當成物件
speaker.off()#演奏完畢關閉法八