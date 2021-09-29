# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:57:00 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url = 'https://shopee.tw/search?keyword=iphone'
header = {'cookie':'Googlebot','user-agent':'Googlebot'}
data = requests.get(url,headers = header)
data.encoding = 'UTF-8'
data = data.text
results = (data,'html.parser')
products = results.find_all('div',class_='col-xs-2-4 shopee-search-item-result__item') 
for i in products:
    name = i.find_all('')
    