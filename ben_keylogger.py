import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

VK_CODE = {i: i for i in range(256)}

current_sequence = []
def check_hello(char):
    expected_sequence = ['H', 'E', 'L', 'L', 'O']

    if char == expected_sequence[len(current_sequence)]:
        current_sequence.append(char)

        if current_sequence == expected_sequence:
            print("hello")
            current_sequence.clear()
    else:

        current_sequence.clear()

def low_level_keyboard_handler(nCode, wParam, lParam):

    if wParam == 256:
        key = VK_CODE[lParam[0]]
        check_hello(str(chr(key)))
        print(chr(key))
    return user32.CallNextHookEx(None, nCode, wParam, lParam)

if __name__ == '__main__':
    LOWLEVELKEYBOARDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, wintypes.WPARAM, ctypes.POINTER(ctypes.c_ulong))
    pointer = LOWLEVELKEYBOARDPROC(low_level_keyboard_handler)
    hook_id = user32.SetWindowsHookExA(13, pointer, 0, 0)  # WH_KEYBOARD_LL is 13

    msg = ctypes.wintypes.MSG()
    while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageA(ctypes.byref(msg))

    user32.UnhookWindowsHookEx(hook_id)
