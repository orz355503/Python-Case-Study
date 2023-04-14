from re import X
import pyautogui
import time
from PIL import ImageGrab
import numpy as np
from pynput.mouse import Listener, Button
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def run():
    time.sleep(2)
    while True:
        time.sleep(5)
        pyautogui.leftClick(x, y)
        time.sleep(2)
        while True:
            im = ImageGrab.grab()
            im = im.convert('RGB')
            array = np.array(im)
            print(array[532][1034][0:3])
            if array[532][1034][0] > 105 and array[532][1034][1] > 120:
                pyautogui.leftClick(x, y)
                break
            else:
                time.sleep(0.5)
                continue


def on_click(_x, _y, button, is_press):
    if button == Button.middle:
        print("setPointData")
        global x
        global y

        x = _x
        y = _y
        # print(x, y)

    if button == Button.right:
        print("startRun")
        listener.stop()
        run()
        return False
    # print(f"mouse{button}at({_x}, {_y}){'press' if is_press else ''}")


with Listener(
    on_click=on_click,
) as listener:
    listener.join()
