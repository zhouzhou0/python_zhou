import requests
from bs4 import BeautifulSoup


url='http://www.baidu.com'

rsp=requests.get(url)
text=rsp.content
soup=BeautifulSoup(text,'lxml')
# bs自动转码
content=soup.prettify()
print(content)
print('*'*60)

# print(soup.head)
print('*'*60)
# print(soup.meta)
print('*'*60)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
soup.link.attrs['type']='hahahaha' #已得到的内容放入内存，就可以进行修改
print(soup.link.attrs['type'])

print('*'*60)
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print('*'*60)
print(soup.name)
print(soup.attrs)
print(soup.name)

print('='*60)
for node in soup.head.contents:
    if node.name =='meta':
        print(node)
    if node.name=='title':
        print(node.string)
print('='*60)

tags=soup.find_all(name='meta')
print(tags)

print('='*60)
import re
tagss=soup.find_all(re.compile('^me'),content='always')
for t in tagss:
    print(t)

print('='*60)