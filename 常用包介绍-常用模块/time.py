#time模块  需要单独导入
import time

#时间模块的属性
#timezone : 当前时区和UTC时间相差的描述，在没有夏令时的情况下的间隔,东八区的是-28800
#altzone : 获取当前时区与UTA时区相差的秒数，在有夏令时的情况下
#daylight : 测当前是否是夏令时时间状态 ，0 表示是
print(time.timezone)
print(time.altzone)
print(time.daylight)

# 得到时间戳
print(time.time())

#localtime 得到当前时间的时间结构
# 可以通过点号操作符得到相应的属性元素的内容
print(time.localtime())
print(time.localtime().tm_hour)
print(type(time.localtime()))
print('>'*30)
#asctime() 返回元组的正常字符串化之后的时间格式
#格式 ：time.asctime(时间元组)
#返回值 ：字符串 Tue Jun 11:11:00 2019
t= time.localtime()
tt=time.asctime(t)
print(type(tt))
print(tt)
print('*'*50)
#ctime :获取字符串化的当前时间
t=time.ctime()
print(type(t))
print(t)
print('>'*30)
#mktime()使用的时间元组获取的对应的时间戳
#格式：time.mktime(时间元组)
# 返回值：浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)

#clock :获取cpu时间  3.0-3.3版本直接使用  3.6调用有问题

#sleep :  使程序进入睡眠，n秒后继续
#格式： time.sleep(n)
for i in range(1,10):
    print(i)
    time.sleep(1)
    print(time.clock())

#strftime:将时间元组转化为自定义的字符串格式
#strftime
#把时间表示成 2019年2月9日 20：20
t = time.localtime()
ftime = time.strftime('%Y年%m月%d日 %H:%M',t)
print(ftime)

#import timeit










