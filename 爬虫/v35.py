from bs4 import BeautifulSoup
import requests

url='http://www.baidu.com'

req=requests.get(url)
soup=BeautifulSoup(req.content,'lxml')
print(soup.prettify())

print('='*60)
title=soup.select('title')
print(title[0])

print('='*60)
meta=soup.select('meta[content="always"]')
print(meta)