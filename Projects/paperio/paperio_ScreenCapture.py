"""
Created on Sat Dec  8 17:17:06 2018

@author: simon

Project: FuturaeNetcom/4chan
"""
from mss.linux import MSS as mss
import PIL.Image
import PIL.ImageTk
import tkinter
import cv2


MONITOR = {"top": 160, "left": 160, "width": 160, "height": 135}


# main part of the programm
def main():
    screen_record()
    return


# used as an example.
def screen_record():
    # TODO: screen_record from the sentdex gta tutorial doesn't work for linux
    # TODO: screen_record has to work for both linux and windows
    # Create a window
    window = tkinter.Tk()
    # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
    with mss() as sct:
        sct.shot(output='file.png')
    cv_img = cv2.imread("file.png")
    height, width, no_channels = cv_img.shape
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack()
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    window.mainloop()
    return


main()
