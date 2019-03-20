import requests
from bs4 import BeautifulSoup


url='http://www.baidu.com'

rsp=requests.get(url)
text=rsp.content
soup=BeautifulSoup(text,'lxml')
# bs自动转码
content=soup.prettify()
print(content)