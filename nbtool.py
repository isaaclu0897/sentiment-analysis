#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:47:38 2018

@author: wei
"""
import requests 
from bs4 import BeautifulSoup

def parse_url(url, specific=False, href=None):
    ''' 解析網頁內容
    
    說明: 將 url 轉換成 html 以便抽取
    -----
    解析給定網頁
    ex: url = 'https://www.ptt.cc/bbs/Beauty/index2102.html'
        pares_url(url)
        
        擷取
        #   <div class="r-ent">
            <div class="nrec"><span class="hl f1">爆</span></div>
            <div class="mark"></div>
            <div class="title">
            <a href="/bbs/Beauty/M.1490441716.A.0CA.html">[正妹] 假日合輯</a>
            </div>
            <div class="meta">
            <div class="date"> 3/25</div>
            <div class="author">Kyle5566</div>
            </div>
            </div>
    解析給定網域及特定子題
    ex: domain = 'https://www.ptt.cc'
        specific_url = '/bbs/Beauty/M.1490441716.A.0CA.html'
        parse_url(domain, specific=True, href=specific_url)
        
        擷取
        #   <a href="http://i.imgur.com/snPJtnI.jpg" rel="nofollow" target="_blank">http://i.imgur.com/snPJtnI.jpg</a>
            <a href="http://i.imgur.com/MGyzVsn.jpg" rel="nofollow" target="_blank">http://i.imgur.com/MGyzVsn.jpg</a>
            <a href="http://i.imgur.com/HsgmPx2.jpg" rel="nofollow" target="_blank">http://i.imgur.com/HsgmPx2.jpg</a>
            <a href="http://i.imgur.com/nBaQ1Rn.jpg" rel="nofollow" target="_blank">http://i.imgur.com/nBaQ1Rn.jpg</a>
            <a href="http://i.imgur.com/L369uMP.jpg" rel="nofollow" target="_blank">http://i.imgur.com/L369uMP.jpg</a>
            <a href="http://i.imgur.com/zlVGsFX.jpg" rel="nofollow" target="_blank">http://i.imgur.com/zlVGsFX.jpg</a>
            <a href="http://i.imgur.com/Psw6R1v.jpg" rel="nofollow" target="_blank">http://i.imgur.com/Psw6R1v.jpg</a>
            <a href="http://i.imgur.com/wMwkOcm.jpg" rel="nofollow" target="_blank">http://i.imgur.com/wMwkOcm.jpg</a>
            <a href="http://i.imgur.com/FpvANo2.jpg" rel="nofollow" target="_blank">http://i.imgur.com/FpvANo2.jpg</a>
    '''
    if specific == True:
        url += href
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    del res
    return soup

# 換頁函數
def change_page(url, jump_page=1): 
    index = [index_num for index_num in url if index_num.isdigit()] 
    index[-1] = str(int(index[-1]) + jump_page) 
    url = url.split('&') 
    url[-1] = ('page={}'.format(index[-1])) 
    url = '&'.join(url) 
    return url 