import requests
from lxml import etree

headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',

         'Referer':'https://www.douban.com/'}
url='https://movie.douban.com/cinema/nowplaying/xiamen/'

response=requests.get(url,headers=headers)
# print(response.text)
#response.text 返回的的一个经过解码之后的字符串，是str(unicode)类型
#response.content返回的是一个原生 的字符串，就是网页上抓取下来的，没有经过处理的字符串，是bytes类型
text=response.text

html=etree.HTML(text)
ul=html.xpath('//ul[@class="lists"]')[0]
# print(etree.tostring(ul,encoding='utf-8').decode("utf-8"))#有乱码，用decode解码
#etree.tostring  把element格式转换str
lis=ul.xpath('./li')
movies=[]
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title=li.xpath('./@data-title')[0]
    score=li.xpath('./@data-score')[0]
    director=li.xpath('./@data-director')[0]
    # print('title:',title,'score:',score,'director:',director)
    img=li.xpath('.//img/@src')[0]
    move={
        'title':title,
        'score':score,
        'director':director,
        'haibao:':img
    }
    movies.append(move)
print(movies)