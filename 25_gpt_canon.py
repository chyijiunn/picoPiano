from picozero import Speaker
import _thread
speaker = Speaker(21)
tempo = 60/150 #tempo = 60/150 #(時間間隔 秒，BPM 120--> 60/120，150-->60/150)
t = 60 / 90  # 每分鐘 120 拍

canon = [
    # 第 1-2 小節
    ['d4', t], ['a4', t], ['b4', t], ['f#4', t], ['g4', t], ['d4', t], ['g4', t], ['a4', t],
    # 第 3-4 小節
    ['b4', t], ['f#4', t], ['g4', t], ['d4', t], ['g4', t], ['a4', t], ['d5', t], ['a4', t],
    # 第 5-6 小節
    ['b4', t], ['f#4', t], ['g4', t], ['d4', t], ['g4', t], ['a4', t], ['b4', t], ['f#4', t],
    # 第 7-8 小節
    ['g4', t], ['d4', t], ['g4', t], ['a4', t], ['d5', t], ['a4', t], ['b4', t], ['f#4', t]
]

speaker.play(canon)
speaker.off()

#_thread.start_new_thread(canon, ())