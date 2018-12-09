"""
Created on Sun Dec  9 12:56:15 2018

@author: Simon

Project: FuturaeNetcom/4chan
"""
import pyautogui
import time


URL = 'http://paper-io.com/'


# main part of the programm
def main():
    start_browser()
    time.sleep(5)
    start_game()
    time.sleep(5)
    close_browser()
    return None


# start browser
def start_browser():
    # TODO: open browser
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    # put the window into full screen / alternative set screen to exact size -> found no solution yet
    pyautogui.press('f11')
    return None


# start game in browser
def start_game():
    # TODO: first select ghost skin
    pyautogui.click(70, 190)
    pyautogui.click(750, 260)
    return None


# close browser
def close_browser():
    # TODO: close browser
    return None


main()
