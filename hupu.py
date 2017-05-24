#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import codecs
import csv

if __name__ == '__main__':
    fist = []
    url = 'https://bbs.hupu.com/vote'
    hupu = requests.get(url)
    # print(hupu.content)

    soup = BeautifulSoup(hupu.content, 'html.parser')
    # print(soup)
    body = soup.body
    aa = body.find('div', attrs={'class':'hp-wrap'})
    # print(aa.tbody)
    for name in aa.find_all('td', attrs={'class':'p_title'}):
        for name2 in name.find_all('a', attrs={'id':''}):
            temp = name2.get_text()
            if not temp.isdigit() and temp != '话题':
                fist.append(temp)
                print(name2.get_text())
            # print(type(name2.get_text()))

    fist2 = filter(lambda x: x != '\xa0', fist)

    # with open('fist.txt','w') as f:
    #     for item in list(fist2):
    #         f.write(item)
    #         if item != '栏目' and item != '篮球场' and item != 'NBA选秀-NCAA':
    #             f.write('\n')
    # with codecs.open('fist.csv','w') as f:
    #     writer = csv.writer(f)
    #     for item in list(fist2):
    #         writer.writerow([item])