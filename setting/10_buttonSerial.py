from picozero import Speaker
import machine
speaker = Speaker(20)
for i in range(27):
    buttonName = 'button' + str(i)
    buttonName = machine.Pin( i , machine.Pin.IN, machine.Pin.PULL_UP)

tempo = 60/120 #BPM 120

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

while True:
    if button0.value() == 0:speaker.play(c3,tempo)
    if button1.value() == 0:speaker.play(c4,tempo)
    if button2.value() == 0:speaker.play(c5,tempo)
    if button3.value() == 0:speaker.play(c6,tempo)
    if button4.value() == 0:speaker.play(d3,tempo)
    if button5.value() == 0:speaker.play(d4,tempo)
    if button6.value() == 0:speaker.play(d5,tempo)
    if button7.value() == 0:speaker.play(d6,tempo)
    if button8.value() == 0:speaker.play(e3,tempo)
    if button9.value() == 0:speaker.play(e4,tempo)
    if button10.value() == 0:speaker.play(e5,tempo)
    if button11.value() == 0:speaker.play(e6,tempo)
    if button12.value() == 0:speaker.play(f3,tempo)
    if button13.value() == 0:speaker.play(f4,tempo)
    if button14.value() == 0:speaker.play(f5,tempo)
    if button15.value() == 0:speaker.play(f6,tempo)
    if button16.value() == 0:speaker.play(g3,tempo)
    if button17.value() == 0:speaker.play(g4,tempo)
    if button18.value() == 0:speaker.play(g5,tempo)
    if button19.value() == 0:speaker.play(g6,tempo)
    if button20.value() == 0:speaker.play(a3,tempo)
    if button21.value() == 0:speaker.play(a4,tempo)
    if button22.value() == 0:speaker.play(a5,tempo)
    if button23.value() == 0:speaker.play(a6,tempo)
    if button24.value() == 0:speaker.play(b3,tempo)
    if button25.value() == 0:speaker.play(b4,tempo)
    if button26.value() == 0:speaker.play(b5,tempo)
    if button27.value() == 0:speaker.play(b6,tempo)
    speaker.off()

