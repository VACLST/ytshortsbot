import errors
import time

try:
    import pyautogui
except ModuleNotFoundError:
    raise errors.PagNotInstalled("You didn\'t install PyAutoGui. Refrain to code 1 in README.md")


def press(key, times=1, shift=False):
    if shift:
        with pyautogui.hold('shift'):
            for i in range(times):
                pyautogui.press(key)
    else:
        for i in range(times):
            pyautogui.press(key)


def scroll(vert=True, ticks=2):
    if vert:
        pyautogui.vscroll(ticks)
    else:
        pyautogui.hscroll(ticks)


@DeprecationWarning
def hold(key, duration=3):
    while duration > 0:
        pyautogui.press(key)
        duration -= 1
        time.sleep(1)


def write(string="Hello, world!"):
    for i in list(string):
        press(i)
