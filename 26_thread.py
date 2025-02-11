from picozero import Speaker
import _thread
speaker = Speaker(21)
tempo = 60/150 #tempo = 60/150 #(時間間隔 秒，BPM 120--> 60/120，150-->60/150)
t = 60 / 240  # 每分鐘 120 拍

canon_melody = [
    ['d4', t], ['e4', t], ['f#4', t], ['g4', t], ['a4', t], ['b4', t], ['a4', t], ['g4', t],
    ['f#4', t], ['e4', t], ['d4', t], ['b3', t], ['d4', t], ['e4', t], ['f#4', t], ['g4', t],
    ['a4', t], ['b4', t], ['c#5', t], ['d5', t], ['b4', t], ['a4', t], ['g4', t], ['f#4', t],
    ['e4', t], ['d4', t], ['e4', t], ['f#4', t], ['g4', t], ['a4', t], ['b4', t], ['d5', t]
]

canon_three_voices = [
    # 第一聲部（起始旋律）
    ['d4', t], ['a4', t], ['b4', t], ['f#4', t], ['g4', t], ['d4', t], ['g4', t], ['a4', t],

    # 第二聲部（延遲一個小節進入）
    ['_', t * 8], ['d4', t], ['a4', t], ['b4', t], ['f#4', t], ['g4', t], ['d4', t], ['g4', t], ['a4', t],

    # 第三聲部（再延遲一個小節進入）
    ['_', t * 16], ['d4', t], ['a4', t], ['b4', t], ['f#4', t], ['g4', t], ['d4', t], ['g4', t], ['a4', t]
]


speaker.play(canon_melody)
speaker.off()

#_thread.start_new_thread(canon, ())