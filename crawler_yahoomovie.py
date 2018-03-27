#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:38:47 2018

@author: wei
"""

import jieba
from nbtool import change_page, parse_url

url = "https://movies.yahoo.com.tw/movieinfo_review.html/id=6953?sort=update_ts&order=desc&page=1" 
item = []
for i in range(1):# 這邊決定換頁換幾次 
    print(url)# 確定當前頁面 
    soup = parse_url(url)

    comment_area = soup.select('ul[class="usercom_list"]')[0]
    comment_blocks = comment_area.select('li')
    for comment_block in comment_blocks:
        comment_block = comment_block.form
        user = comment_block.select('.user_id')[0].text
        score = int(comment_block.select('input[name~=score]')[0]['value'])
        comment = comment_block.select('span')[-1].text.replace('\r\n', '')
        words = jieba.cut(comment, cut_all=False)
        word = [word for word in words]
        comment_sep = '/'.join(word)
#        print(user, '\n', score, '\n', comment, '\n')
        
        item.append([user, score, comment, comment_sep])
#        item.append({'name' : user,
#                     'score' : score,
#                     'comment' : comment,
#                     'com_sep' : comment_sep}) 
    url = change_page(url)
for i in item:
    print(i[2], '\n', i[3])
    print('\n')
        