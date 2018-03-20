#! /usr/bin/python3
# -*- coding: utf8 -*-
#from openpyxl import Workbook
import datetime
import requests
import time
from bs4 import BeautifulSoup
#stockList={'2317':'', '2887':'', '2354':'', '3209':''}
stockList=['2317', '2887', '2354', '3209']
stockValue=[]
content=[]
for _ in stockList:
	res=requests.get('https://tw.stock.yahoo.com/q/q?s='+ _ )
	wes=BeautifulSoup(res.text,"html.parser")
	ss=wes.select("b")
	stockValue.append(ss[0].text)
stockTime=time.strftime("%H:%M:%S", time.localtime())

## Line Notify
for i in range(len(stockList)):
	contentstock = stockList[i] + ' 目前股價為： ' + stockValue[i]
	content.append(contentstock)
	content.append('\n')

msgs=content
lineUrl = "https://notify-api.line.me/api/notify"
token = "RNeFGMxis9g8JTmOQHDBovWR87elsHCzm8Udb2Kvhtr"
headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

payload = {'message':msgs}
r = requests.post(lineUrl, headers = headers, params = payload)
