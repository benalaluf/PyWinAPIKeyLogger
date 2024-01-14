import ctypes
import time
from threading import Thread

user32 = ctypes.windll.user32

# Constants
KEYEVENTF_KEYUP = 0x0002
VK_RETURN = 0x0D
VK_CAPITAL = 0x14


# Function to get the current keyboard layout
def get_keyboard_layout():
    return user32.GetKeyboardLayout(0)


# Function to get the list of keyboard layouts
def get_keyboard_layout_list():
    buf_size = 256
    layouts = (ctypes.c_uint * buf_size)()
    count = user32.GetKeyboardLayoutList(buf_size, ctypes.byref(layouts))
    return [layouts[i] for i in range(count)]


# Function to get the state of a key asynchronously
def get_async_key_state(key_code):
    return user32.GetAsyncKeyState(key_code)


# Function to check if a specific word is being typed
def check_for_hello():
    hello_word = [72, 69, 76, 76, 79]  # ASCII codes for the word 'hello'
    current_layout = get_keyboard_layout()

    while True:
        for key_code in hello_word:
            if get_async_key_state(key_code) & 0x8001:
                break
        else:
            print("Hello typed!")

        time.sleep(0.1)


# Main function to capture keystrokes
def capture_keystrokes():
    # Start a separate thread to check for the word 'hello'
    hello_thread = Thread(target=check_for_hello, daemon=True)
    hello_thread.start()

    # Main loop to capture keystrokes
    while True:
        for i in range(256):
            state = get_async_key_state(i)
            if state & 0x8001:
                print(f"Key {i} pressed")
            elif state & 0x0001:
                print(f"Key {i} released")

            time.sleep(0.01)


if __name__ == "__main__":
    print("Keyboard layouts:", get_keyboard_layout_list())
    capture_keystrokes()
