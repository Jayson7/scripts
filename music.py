from pygame import mixer
from mixer import *

mixer.init()

#........................................................... path of music

mixer.music.load("drake-toosie-slide.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("press 'p' to pause")
    print("press 'r' to resume")
    print("press 'v' to set volume")
    print("press 'e' to exit")


    ch = input("['p', 'r', 'v', 'e']>>> ")
    if ch == 'p':
        mixer.music.pause()
    elif ch == 'r':
        mixer.music.unpause()
    elif ch == 'v':
        v = float(input("Enter volume(0 - 1):  "))
        mixer.music.set_volume(v)

    elif ch == "e":
        mixer.music.stop()

        break

