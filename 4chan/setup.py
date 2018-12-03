# -*- coding: utf-8 -*-

# import model_training
# import scraping


def scraping():
    print('scraping')


def learning():
    print('learning')
    import model_training as m
    m.start('data/scraped_material-a-1543749875.txt',
            None,
            'floyd',
            'Start',
            100)


print('Setup: Do you want to start by scraping? (y/n)', end='')
text = input()
if (text == 'y'):
    scraping()
elif (text == 'n'):
    learning()
