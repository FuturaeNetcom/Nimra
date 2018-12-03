"""
Created on Mon Dec  3 18:52:44 2018

@author: simon

Project: FuturaeNetcom/4chan
"""
import ModelTraining
import Scraping


# main part of the programm
def main(bool_scraping):
    if (bool_scraping):
        scraping()
    else:
        learning()
    return


# starts using ModelTraining.py
def learning():
    ModelTraining.start('data/scraped_material-a-1543749875.txt',
                        None,
                        'floyd',
                        'Start',
                        100)
    return


# starts using Scraping.py
def scraping():
    Scraping.main(['a', 'v'])
    return


main()
