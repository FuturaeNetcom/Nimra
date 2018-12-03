#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 07:11:15 2018

@author: simon

Project: Futurae Netcom
"""


num_START_THREAD = 0


# main part of the program
def main(list_channel):
    for str_channel in list_channel:
        get_channel(str_channel)


# creates .txt file with channel content
def get_channel(str_channel):
    import time
    num_startTime = time.time()
    str_fileName = str_channel + '-' + str(int(num_startTime))
    str_fileName = 'data/scraped_material-' + str_fileName + '.txt'
    with open(str_fileName, 'w') as file_text:
        list_thread = get_thread_numbers(str_channel)
        num_index = 0
        if num_START_THREAD != 0:
            list_thread = list_thread[num_START_THREAD:]
        for num_threadID in list_thread:
            if (num_index >= len(list_thread)):
                break
            num_index = num_index + 1
            edit_thread(str_channel, num_threadID, file_text)
            eta = ETA(num_index, num_startTime, len(list_thread))
            print('channel: ' + str(str_channel) +
                  str(num_index) + '-' + str(eta))
    file_text.close()


# writes thread to channel file
def edit_thread(str_channel, num_thread, file_text):
    list_block = get_block(num_thread, str_channel)
    for str_line in list_block:
        try:
            file_text.write(str_line + '\n')
        except UnicodeEncodeError:
            print("Error: Failed to write line")


# collects all thrad ids for channel
def get_thread_numbers(str_channel):
    import requests
    import bs4
    import re
    url = 'https://boards.4channel.org/' + str_channel + '/archive'
    res = requests.get(url, stream=True)
    try:
        res.raise_for_status()
    except requests.HTTPError:
        return ''
    str_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    str_tbody = str_soup.find('tbody')
    str_td = str(str_tbody.find_all('td'))
    list_match = re.findall(r"[0-9]{9}", str_td)
    del list_match[::2]
    return list_match


# gets block content for thread
def get_block(num_threadID, str_channel):
    import requests
    import bs4
    str_url = str_channel + '/thread/' + num_threadID
    str_url = 'https://boards.4channel.org/' + str_url
    res = requests.get(str_url, stream=True)
    try:
        res.raise_for_status()
    except requests.HTTPError:
        return ''
    str_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    list_ft = str_soup.find_all('span', {'class': 'quote'})
    list_block = list()
    for quote in list_ft:
        string = str(quote.text)
        string = string.split('>')[1]
        list_block.append(string)
    return list_block


# returns ETA
def ETA(num_linesProccesed, num_fullStart, num_length):
    import time
    num_timeTaken = time.time() - num_fullStart
    num_linesLeft = num_length - num_linesProccesed
    num_timeLeft = (num_timeTaken / num_linesProccesed) * num_linesLeft
    num_timeLeft = "%.1f" % (num_timeLeft / 60)
    return "ETA: " + num_timeLeft + "m"
