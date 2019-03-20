import requests
from bs4 import BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'cache-control':'max-age=0'
}

html=requests.get('https://www.cnblogs.com/cate/python/')
# print(html.text)

soup=BeautifulSoup(html.text,'lxml')

items=soup.select('div[class="post_item_body"]')
# print(items)
for item in items:
    # print(items)
    # 标题
    title=item.select('h3 a[class="titlelnk"]')[0].get_text()
    #详情页链接
    href = item.select('h3 a[class="titlelnk"]')[0].get('href')
    # print(title)
    # print(href)
    #作者
    autor=item.select('div a[class="lightblue"]')[0].get_text()
    #作者的主页链接
    autor_home = item.select('div a[class="lightblue"]')[0].get('href')
    # print(autor+"~"+autor_home)
    # 简要信息
    infos=item.select('p[class="post_item_summary"]')[0].get_text().strip("\n").strip(' ')
    # print(infos)
    dates=item.select('div[class="post_item_foot"]')[0].get_text()
    # print(dates,type(dates))
    dates=dates.split(' ')
    # print(dates, type(dates))
    '''
    ['\n格格_gloria', '\r\n', '', '', '', '发布于', '2019-03-20', '15:40', '\r\n', '', '', '', '\r\n', '', '', '', '', '', '', '',
     '评论(0)阅读(14)'] <class 'list'>
    '''
    # 发布时间
    time=dates[6]+"~"+dates[7]
    # print(time)
    # 评论信息
    pinglun=dates[-1].lstrip('评论(').split(")")[0]
    # print(pinglun)
    #阅读数
    read_num=dates[-1].rstrip(')').split('(')[-1]
    print(read_num)