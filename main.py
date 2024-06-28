# from pynput import keyboard
import time
import winsound as sd
def s():
    fr = 600    # range : 37 ~ 32767
    du = 40     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)


def l():
    fr = 600    # range : 37 ~ 32767
    du = 100     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)


import keyboard

while True:
    key = keyboard.read_key()
    if key == "a":
        s()
        l()
        time.sleep(0.06)
    if key == "b":
        l()
        s()
        s()
        s()
        time.sleep(0.06)
    if key == "c":
        l()
        s()
        l()
        s()
        time.sleep(0.06)
    if key == "d":
        l()
        s()
        s()
        time.sleep(0.06)
    if key == "e":
        s()
        time.sleep(0.06)
    if key == "f":
        s()
        s()
        l()
        s()
        time.sleep(0.06)
    if key == "g":
        l()
        l()
        s()
        time.sleep(0.06)
    if key == "h":
        s()
        s()
        s()
        s()
        time.sleep(0.06)
    if key == "i":
        s()
        s()
        time.sleep(0.06)
    if key == "j":
        s()
        l()
        l()
        l()
        time.sleep(0.06)
    if key == "k":
        l()
        s()
        l()
        time.sleep(0.06)
    if key == "l":
        s()
        l()
        s()
        s()
        time.sleep(0.06)
    if key == "m":
        l()
        l()
        time.sleep(0.06)
    if key == "n":
        l()
        s()
        time.sleep(0.06)
    if key == "o":
        l()
        l()
        l()
        time.sleep(0.06)
    if key == "p":
        s()
        l()
        l()
        s()
        time.sleep(0.06)
    if key == "q":
        l()
        l()
        s()
        l()
        time.sleep(0.06)
    if key == "r":
        s()
        l()
        s()
        time.sleep(0.06)
    if key == "s":
        s()
        s()
        s()
        time.sleep(0.06)
    if key == "t":
        l()
        time.sleep(0.06)
    if key == "u":
        s()
        s()
        l()
        time.sleep(0.06)
    if key == "v":
        s()
        s()
        s()
        l()
        time.sleep(0.06)
    if key == "w":
        s()
        l()
        l()
        time.sleep(0.06)
    if key == "x":
        l()
        s()
        s()
        l()
        time.sleep(0.06)
    if key == "y":
        l()
        s()
        l()
        l()
        time.sleep(0.06)
    if key == "z":
        l()
        l()
        s()
        s()
        time.sleep(0.06)
    else:
        if key:
            print(key)
            key = False
    
    