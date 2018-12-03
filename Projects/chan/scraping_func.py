# -*- coding: utf-8 -*-
import requests
import bs4
import re
import time


def getBlock(thread_number, CHANNEL):
    url = 'https://boards.4channel.org/' + CHANNEL + '/thread/' + thread_number
    res = requests.get(url, stream=True)
    try:
        res.raise_for_status()
    except:
        return ''
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    ft = soup.find_all('span', {'class': 'quote'})
    bloeke = list()
    for quote in ft:
        string = str(quote.text)
        string = string.split('>')[1]
        bloeke.append(string)
    return bloeke


def getThreadNumbers(CHANNEL):
    url = 'https://boards.4channel.org/' + CHANNEL + '/archive'
    res = requests.get(url, stream=True)
    try:
        res.raise_for_status()
    except:
        return ''
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    tbody = soup.find('tbody')
    td = str(tbody.find_all('td'))
    match = re.findall(r"[0-9]{9}", td)
    del match[::2]
    return match


def time_needed(lines_proccesed, full_start, length):
    time_taken = time.time() - full_start
    lines_left = length - lines_proccesed
    time_left = (time_taken / lines_proccesed) * lines_left
    time_left = "%.1f" % (time_left / 60)
    return "ETA: " + time_left + "m"
