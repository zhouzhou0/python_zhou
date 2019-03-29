import requests

from bs4 import BeautifulSoup
import random
from pyecharts import Bar  #Bar柱状图
all_data=[]
def parse_page(url):
    headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    response=requests.get(url,headers=headers)
    text=response.content.decode('utf-8')
    soup=BeautifulSoup(text,'html5lib')#不使用lxml的原因是因为港澳台中table有异常
                                       #html5lib速度慢 容错率高
    conMidtab=soup.find('div',class_='conMidtab') #class下面加下划线class_
    tables=soup.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:] #过滤掉前面两个tr
        for index,tr in enumerate(trs): #enumerate 索引下标
            # print(tr)
            # print('='*100)
            tds=tr.find_all('td')
            if index==0:
                city_td=tds[1]
            else:
                city_td=tds[0]
            city_list=list(city_td.stripped_strings)[0]# stripped_strings所有子孙节点 的文本信息
            weather_td=tds[-4]
            weather=list(weather_td.stripped_strings)[0]
            temp_td=tds[-2]
            min_temp=list(temp_td.stripped_strings)[0]
            all_data.append({"city":city_list,"weather":weather,'min_temp':int(min_temp)})
            # print({"city":city_list,"weather":weather,'min_temp':min_temp})
        # print('='*100)


def main():
    dqs=['hb','db','hd','hz','hn','xb','xn','gat']
    for dq in dqs:
        url='http://www.weather.com.cn/textFC/{0}.shtml'.format(dq)
        # if dq=='hb':
        #     print('华北地区')
        # elif dq=='db':
        #     print('东北地区')
        # elif dq=='hd':
        #     print('华东地区')
        # elif dq=='hz':
        #     print('华中地区')
        # elif dq=='hn':
        #     print('华南地区')
        # elif dq=='xb':
        #     print('西北地区')
        # elif dq=='xn':
        #     print('西南')
        # elif dq=='gat':
        #     print('港澳台')

        parse_page(url)

    #分析数据
    #根据最低气温来进行排序
    # def sory_key(data):
    #     min_temp=data['min_temp']
    #     return int(min_temp)
    all_data.sort(key=lambda data:data['min_temp'] )
    data= all_data[0:10] #取出前十个
    # print(data)
    #pyecharts

    # for city_temp in data:
    #     city=city_temp['city']
    #     cities.append(city)
    cities=list(map(lambda x:x['city'] ,data))
    temps=list(map(lambda x:x['min_temp'],data))
    chart=Bar("中国天气最低气温排行榜")
    chart.add('',cities,temps)
    chart.render('temp.html')

if __name__ == '__main__':
    main()