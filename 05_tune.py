from picozero import Speaker
speaker = Speaker(19)
tempo = 60/150 #tempo = 60/150 #(時間間隔 秒，BPM 120--> 60/120，150-->60/150)

tune=[['e3',tempo] ,['d3',tempo] ,['c3',tempo],['b3',tempo],['c3',tempo],['d3',tempo],['e3',tempo],['e3',tempo]    ]

speaker.play(tune)

speaker.off()