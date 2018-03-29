#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:38:47 2018

@author: wei
"""


from nbtool import change_page, parse_url
import jieba
from analysis import sentiment_score_list, sentiment_score
import numpy as np
#from snownlp import SnowNLP

#posdict = open_dict(DICT='正面')
#negdict = open_dict(DICT='負面')
#mostdict = open_dict(DICT='most')
#verydict = open_dict(DICT='very')
#moredict = open_dict(DICT='more')
#ishdict = open_dict(DICT='ish')


url = "https://movies.yahoo.com.tw/movieinfo_review.html/id=6953?sort=update_ts&order=desc&page=1" 
item = []
for i in range(10):# 這邊決定換頁換幾次 
    print(url)# 確定當前頁面 
    soup = parse_url(url)

    comment_area = soup.select('ul[class="usercom_list"]')[0]
    comment_blocks = comment_area.select('li')
    for comment_block in comment_blocks:
        comment_block = comment_block.form
        user = comment_block.select('.user_id')[0].text
        score = int(comment_block.select('input[name~=score]')[0]['value'])
        comment = comment_block.select('span')[-1].text.replace('\r\n', '')
        
        # 結巴斷詞處理
        words = jieba.cut(comment, cut_all=False)
        word = [word for word in words]
        comment_sep = '/'.join(word)
#        print(comment, '\n', comment_sep, '\n', sentiment_score(sentiment_score_list(comment)))
        # 426牛人庫
#        s_fi = SnowNLP(comment)
#        s = SnowNLP(s_fi.han)
#        print(user, '\n', score, '\n', comment, '\n')
        
        item.append([user, score, comment, comment_sep, sentiment_score(sentiment_score_list(comment))])
#        item.append({'name' : user,
#                     'score' : score,
#                     'comment' : comment,
#                     'com_sep' : comment_sep}) 
    url = change_page(url)
for i in item:
    print( i[3], '\n', i[4])
    print('\n')
    
#a = [ i[0] for i in item]
#for i in a:
#    if a.count(i) != 1:
#        print (i, a.count(i)) 
#        break