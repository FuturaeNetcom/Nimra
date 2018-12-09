"""
Created on Sat Dec  8 17:16:32 2018

@author: simon

Project: FuturaeNetcom/4chan
"""
import paperio_ScreenCapture as screenCapture
import paperio_Tools as tools
# import paperio_Control as control


# main part of the programm
def main():
    tools.count_down(5)
    while (True):
        screenCapture.main()
    return


main()
