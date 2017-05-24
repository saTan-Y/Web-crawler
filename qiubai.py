#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from lxml import etree
import os

if __name__ == '__main__':
    direc = '.\\Qiubai\\'
    if not os.path.exists(direc):
        os.mkdir(direc)
    qiubai = open(direc+'qiubai.txt', mode='w')

    for page in range(1, 3):
        url = 'http://www.qiushibaike.com/8hr/page/' + str(page)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        f = requests.get(url, headers=headers)
        f.encoding = 'gbk'
        # print(f.text)
        html = f.content
        context = etree.HTML(html)
        # temp = wenzi.xpath('//*[@class="article block untagged mb15"]/div/a/h2/text() | //*[@class="article block untagged mb15"]/a[1]/div/span/text() | '
        #                    '//*[@class="article block untagged mb15"]/div/span/i/text() | //*[@class="article block untagged mb15"]/div/span[@class="stats-vote"]/text() | '
        #                    '//*[@class="article block untagged mb15"]/div/span/a/i/text() | //*[@class="article block untagged mb15"]/div/span/a/text()')

        for div in context.xpath('//*[@class="article block untagged mb15"]'):
            id = div.xpath('./div/a/h2/text()')
            content = div.xpath('./a[1]/div/span/text()')
            pos = div.xpath('./div/span[@class="stats-vote"]')[0]
            fun = pos.xpath('string(.)')
            pos2 = div.xpath('./div/span[@class="stats-comments"]/a')[0]
            comment = pos2.xpath('string(.)')
            print(''.join(content))
            # print(id, '\n', content, '\n', fun.strip(), comment.strip(), '\n\n')
            qiubai.write(''.join(id))
            qiubai.write('\n')
            qiubai.write(''.join(content))
            qiubai.write('\n')
            qiubai.write(fun+comment)
            qiubai.write('\n\n')


        # //*[@id="qiushi_tag_118829420"]/a[1]/div/span //*[@id="qiushi_tag_118829420"]/div[2]/span[1]/i

    qiubai.close()
