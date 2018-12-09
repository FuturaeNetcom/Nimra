"""
Created on Sun Dec  9 12:33:42 2018

@author: Simon

Project: FuturaeNetcom/4chan

"""
import pyautogui


# main part of the programm
def main():
    pyautogui.PAUSE = 0.2
    return


# turn left
def left():
    pyautogui.press('a')
    return


# turn right
def right():
    pyautogui.press('d')
    return


main()
