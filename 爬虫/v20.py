'''
爬去豆瓣电影的数据
了解ajax

Request URL:
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20

start--开始
interval ---好评度

'''

from urllib import request
import json

url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

rsp=request.urlopen(url)
r=rsp.read().decode()
data=json.loads(r)
print(data)