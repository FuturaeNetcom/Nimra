"""
Created on Sun Dec  9 12:39:26 2018

@author: Simon

Project: FuturaeNetcom/4chan
"""


# main part of the programm
def main():
    return


# waits for [num_length] seconds
def count_down(num_length):
    import time
    for i in list(range(num_length))[::-1]:
        print(i+1)
        time.sleep(1)
    return None
