
#draw rectangle for bush and bird

import PIL,pyautogui
import time
from PIL import Image, ImageGrab


def hit(key):
    pyautogui.keyDown(key)
    return
#if it collides then hit up
#or hit down
#CHANGE THESE VALUES ACC to ur screen
def Collide(data):
    for i in range(600, 720):
        for j in range(335, 360):
            if data[i, j] <100:
                hit("up")
                return
    for i in range(630, 720):
        for j in range(200, 335):
            if data[i, j] <100:
                hit("down")
                return
#Grab the screenshot of the game
while True:
    time.sleep(2)
    image = ImageGrab.grab().convert('L')
    data = image.load()
    Collide(data)


