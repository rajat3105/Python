import pyautogui
from PIL import Image, ImageGrab
#import pyscreenshot as ImageGrab
import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    for i in range(270,310):
        for j in range(340,379):
            if data[i,j]<=100:
                hit('down')
                return
    for i in range(200,280):
        for j in range(380,448):
            if data[i,j]<=100:
                hit('up')
                return
    return

if _name_ == "_main_":
    print('Hey..Dino is about to start!!')
    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
