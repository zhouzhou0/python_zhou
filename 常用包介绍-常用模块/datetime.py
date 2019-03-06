# datetime模块
#- datetinme提供日期和时间的运算和表示
# datetime常见属性
# datetime.date : 一个理想和的日期，提供year，monthday属性
import time


import datetime
dt = datetime.date(2019,2,9)
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)

# datetime.time: 提供一个理想和的时间， 居于hour， minute，sec，microsec等内容
# datetime.datetime: 提供日期跟时间的组合
# datetime.timedelta: 提供一个时间差，时间长度

print('>'*30)

# datetime.datetime: 提供日期跟时间的组合
from datetime import datetime
#常用类方法
#today now   utcnow
#fromtimestamp:从时间戳中返回本地时间
dt =datetime(2019,2,9)

print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))



# datetime.timedelta: 提供一个时间差，时间长度
#datetime.timedelta  表示一个时间间隔
from datetime import datetime, timedelta
t1 =datetime.now()
print(t1.strftime('%Y-%m-%d  %H:%M:%S'))
#t2 表示一小时的时间长度
t2 = timedelta(hours=1)
#当前时间加上时间间隔后，把得到的一个小时后的时间格式输出
print((t1+t2).strftime('%Y-%m-%d  %H:%M:%S'))

