from picozero import Speaker
speaker = Speaker(19)
tempo = 60/150 #tempo = 60/150 #(時間間隔 秒，BPM 120--> 60/120，150-->60/150)

tune_1 = [['a5', tempo / 2],
        ['a5', tempo],
        ['e6', tempo],
        ['d6', tempo * 1.5],
        ['f#5', tempo],
        ['a5', tempo * 1.5],
        ['d5', tempo],
        ['f#5', tempo * 1.5],
        ['e5', tempo / 2],
        ['e5', tempo * 1.5]]
tune_2 = [['d5', tempo / 2], ['d#5', tempo / 2], ['f5', tempo], ['d6', tempo], ['a#5', tempo], ['d5', tempo],
              ['f5', tempo], ['d#5', tempo], ['d#5', tempo], ['c5', tempo / 2],['d5', tempo / 2], ['d#5', tempo],
              ['c6', tempo], ['a5', tempo], ['d5', tempo], ['g5', tempo], ['f5', tempo], ['f5', tempo], ['d5', tempo / 2],
              ['d#5', tempo / 2], ['f5', tempo], ['g5', tempo], ['a5', tempo], ['a#5', tempo], ['a5', tempo], ['g5', tempo],
              ['g5', tempo], ['', tempo / 2], ['a#5', tempo / 2], ['c6', tempo / 2], ['d6', tempo / 2], ['c6', tempo / 2],
              ['a#5', tempo / 2], ['a5', tempo / 2], ['g5', tempo / 2], ['a5', tempo / 2], ['a#5', tempo / 2], ['c6', tempo],
              ['f5', tempo], ['f5', tempo], ['f5', tempo / 2], ['d#5', tempo / 2], ['d5', tempo], ['f5', tempo], ['d6', tempo],
              ['d6', tempo / 2], ['c6', tempo / 2], ['b5', tempo], ['g5', tempo], ['g5', tempo], ['c6', tempo / 2],
              ['a#5', tempo / 2], ['a5', tempo], ['f5', tempo], ['d6', tempo], ['a5', tempo], ['a#5', tempo * 1.5] 
    ]

speaker.play(tune_1)

speaker.off()