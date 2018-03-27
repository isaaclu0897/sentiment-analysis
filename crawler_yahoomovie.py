#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:38:47 2018

@author: wei
"""

import requests 
from bs4 import BeautifulSoup 
import jieba
from nbtool import change_page, parse_url

url = "https://movies.yahoo.com.tw/movieinfo_review.html/id=6953?sort=update_ts&order=desc&page=1" 
for i in range(3):# 這邊決定換頁換幾次 
     
    print(url)# 確定當前頁面 
    res = requests.get(url) 
    soup = BeautifulSoup(res.text, "lxml") 
     
    articles = [] 
# comment_block = soup.select('.usercom_list') 
# print(comment_block) 
     
    divs = soup.find_all('div', 'usercom_inner _c') 
    for item in divs: #soup.select('#form_good1'):# :.string.text.text  
        user = item.find('div', 'user_id unuser').text 
        #print (user) 
        scor = item.find('input',{'name':"score"})['value'] 
        score = int(scor) 
        #print (score) 
# articles.append({'user':user, 
# 'score':score,}) 
        a = item.find_all('span') 
        for comment in a: 
            if comment.text == '': 
                continue 
            com = (comment.text).replace('\r\n', '')
            coms_sep = jieba.cut(com, cut_all=False)
            word = [com_sep for com_sep in coms_sep]
            # 同一個人做的事，儲忖在同一dict比較能體現效果 
            articles.append({'user':user, 
                             'score':score, 
                             'comment':(comment.text).replace('\r\n', ''),
                             'comment_sep':word,
                             'com':coms_sep}) 
# print (comment.text) 
    url = change_page(url) # 頁面資訊分析完後，換頁 
    # 依次打印每個頁面 
    for i in (articles): 
        print('評論：\n', i['comment'])
        print('切割後的評論：\n', i['comment_sep'])
        print('111', i['com'])