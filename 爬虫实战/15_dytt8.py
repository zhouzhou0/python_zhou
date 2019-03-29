import requests
import random
from threading import Thread

from lxml import etree

BASE_DOMAIN='http://dytt8.net/'

useragent = ["Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
             "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
             "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
             "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
             "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
             "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
             "UCWEB7.0.2.37/28/999",
             "NOKIA5700/ UCWEB7.0.2.37/28/999",
             "Openwave/ UCWEB7.0.2.37/28/999",
             "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999", ]
headers = {'User': random.choice(useragent)}

def get_urls(url):


    response=requests.get(url,headers=headers)
    #response.text
    #response.content
    #resquests库默认会使用自己的猜测编码方式
    #抓取下来的网页进行解码，然后存储到text属性上去
    #在电影天堂网页中，因为编码方式requests库猜错了，所有产生了乱码

    text=response.text #content.decode('gbk')#页面中有特殊符号� �1CD，gbk不能解码，只能使用默认的解码
    html=etree.HTML(text)
    detail_urls=html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls=list(map(lambda url:BASE_DOMAIN+url,detail_urls))
    return detail_urls

def parse_detail_page(url):
    movie={}
    response=requests.get(url,headers=headers)
    text=response.content.decode('gbk')
    html=etree.HTML(text)
    title=html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    Zooms=html.xpath("//div[@id='Zoom']//img/@src")
    poster=Zooms[0]
    screenshot=Zooms[1]
    movie = {'title': title, 'poster': poster, 'screenshot': screenshot}
    infos=html.xpath("//div[@id='Zoom']//text()")

    def parse_info(info,rule):
        return info.replace(rule,'').strip()  #strip去空格
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"): #startswith以什么开头
            info=parse_info(info,"◎年　　代")
            # print(info)
            movie['year']=info
        elif info.startswith('◎产　　地'):
            info=parse_info(info,'◎产　　地')
            movie['country']=info

        elif info.startswith('◎类　　别'):
            info=parse_info(info,'◎类　　别')
            movie['class']=info
        elif info.startswith('◎豆瓣评分'):
            info=parse_info(info,'◎豆瓣评分')
            movie['score']=info
        elif info.startswith('◎片　　长'):
            info=parse_info(info,'◎片　　长')
            movie['Running time']=info
        elif info.startswith('◎导　　演'):
            info=parse_info(info,'◎导　　演')
            movie['director']=info
        elif info.startswith('◎主　　演'):
            info=parse_info(info,'◎主　　演')
            actors=[]
            actors.append(info)
            for x in range(index+1,len(infos)):
                actor=infos[x].strip()

                if actor.startswith('◎'):
                    break
                actors.append(actor)
                # print(actor)
            movie['actors']=actors
        elif info.startswith('◎简　　介 '):
            info=parse_info(info,'◎简　　介 ')
            for x in range(index+1,len(infos)):
                profile=infos[x].strip()

                if profile.startswith('【下载地址】'):
                    break
                # print(profile)
                movie['profile']=profile
    download_url=html.xpath("//td[@bgcolor='#fdfddf']//a/text()")[0]
    movie['download_url']=download_url
    return movie
    # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
    # print(download_url)


def main():
    movies=[]
    for i in range(1,8):
        #第一个for循环是用来控制有多少页
        url='http://dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
        print('第{}页'.format(i))
        detail_urls=get_urls(url)

        for detail_url in detail_urls:
            #第二个for循环是用来遍历一页中所有电影的详情url
            # print(detail_url)
            movie=parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)
            # break
        # break

if __name__ == '__main__':
    main()
