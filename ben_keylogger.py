import ctypes
import time

def get_key_pressed():
    for i in range(8, 191):
        if ctypes.windll.user32.GetAsyncKeyState(i) & 0x8001 != 0:
            return i
    return None

while True:
    pressed_key = get_key_pressed()

    if pressed_key is not None:
        char = chr(pressed_key)
        print("key pressed:",pressed_key,char)
          # Adjust the delay between characters if needed

    time.sleep(0.1)
