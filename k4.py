import webbrowser
import pyautogui
import time

event = webbrowser.open('https://www.google.co.in/')
time.sleep(2)

def press():
    pyautogui.click(30, 15)
    pyautogui.click(30, 15)


def ref():
    pyautogui.click(74, 47)


press()
ref()