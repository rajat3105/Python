import pyautogui
from PIL import Image
import pyscreenshot as ImageGrab
import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    for i in range(230,280):
        for j in range(410,440):
            if data[i,j]<100:
                hit('down')
                return
    for i in range(230,280):
        for j in range(440,520):
            if data[i,j]<100:
                hit('up')
                return
    return

if __name__ == "__main__":
    print('Hey..Dino is about to start!!')
    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
