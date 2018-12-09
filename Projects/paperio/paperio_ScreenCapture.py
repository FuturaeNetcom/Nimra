"""
Created on Sat Dec  8 17:17:06 2018

@author: simon

Project: FuturaeNetcom/4chan
"""
import numpy as np
from PIL import ImageGrab
import cv2

MONITOR = {"top": 160, "left": 160, "width": 160, "height": 135}


# main part of the programm
def main():
    list_screen_shoot = screen_record()
    list_image = procces_image(list_screen_shoot)
    show_image(list_image)
    # TODO: analyze image and edit it
    return None


# captures screen
def screen_record():
    # 800x600 windowed mode
    list_screen_shoot = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    return list_screen_shoot


# shows image
def show_image(list_image):
    cv2.imshow('window', list_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    return None


# edits image
def procces_image(list_image):
    # convert to gray
    processed_img = cv2.cvtColor(list_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img
