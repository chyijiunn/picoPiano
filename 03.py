from picozero import Speaker
speaker = Speaker(21)
tempo = 5 #BPM

speaker.play('c4', tempo) #C4
speaker.off()