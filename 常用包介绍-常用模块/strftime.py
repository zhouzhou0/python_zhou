import time
#strftime
#把时间表示成 2019年2月9日 20：20
t = time.localtime()
ftime = time.strftime('%Y年%m月%d日 %H:%M',t)
print(ftime)