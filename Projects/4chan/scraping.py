#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 07:11:15 2018

@author: simon

Project: Futurae Netcom
"""




START_THREAD = 0


def main():
    # print('main')
    channel_list = ['a', 'v']
    for channel in channel_list:
        get_channel(channel)


def get_channel(channel):
    # print('get_channel')
    import time
    start_time = time.time()
    filename = channel + '-' + str(int(start_time))
    filename = 'data/scraped_material-' + filename + '.txt'
    with open(filename, 'w') as text_file:
        thread_numbers = get_thread_numbers(channel)
        NUMBER_THREADS = len(thread_numbers)
        index = 0
        if START_THREAD != 0:
            thread_numbers = thread_numbers[START_THREAD:]
        for thread in thread_numbers:
            if (index >= NUMBER_THREADS):
                break
            index = index + 1
            edit_thread(channel, thread, text_file)
            eta = time_needed(index, start_time, NUMBER_THREADS)
            print('CHANNEL: ' + str(channel) + str(index) + '-' + str(eta))
    text_file.close()


def edit_thread(channel, thread, text_file):
    # print('edit_thread(' + str(channel) + ', ' + str(thread) + ')')
    block = get_block(thread, channel)
    for line in block:
        try:
            text_file.write(line + '\n')
        except UnicodeEncodeError:
            print("Error: Failed to write line")


def get_thread_numbers(CHANNEL):
    # print('get_thread_numbers')
    import requests
    import bs4
    import re
    url = 'https://boards.4channel.org/' + CHANNEL + '/archive'
    res = requests.get(url, stream=True)
    try:
        res.raise_for_status()
    except requests.HTTPError:
        return ''
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    tbody = soup.find('tbody')
    td = str(tbody.find_all('td'))
    match = re.findall(r"[0-9]{9}", td)
    del match[::2]
    return match


def get_block(thread_number, CHANNEL):
    # print('get_block')
    import requests
    import bs4
    url = 'https://boards.4channel.org/' + CHANNEL + '/thread/' + thread_number
    res = requests.get(url, stream=True)
    try:
        res.raise_for_status()
    except requests.HTTPError:
        return ''
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    ft = soup.find_all('span', {'class': 'quote'})
    bloeke = list()
    for quote in ft:
        string = str(quote.text)
        string = string.split('>')[1]
        bloeke.append(string)
    return bloeke


def time_needed(lines_proccesed, full_start, length):
    # print('time_needed')
    import time
    time_taken = time.time() - full_start
    lines_left = length - lines_proccesed
    time_left = (time_taken / lines_proccesed) * lines_left
    time_left = "%.1f" % (time_left / 60)
    return "ETA: " + time_left + "m"


main()
