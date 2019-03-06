#使用需要先导入
#calendar
import calendar
#calendar :获取一年的日历字符串
#参数
#w = 每个日期之间的间隔字符数
#l = 每周所占用的行数
#c = 每个月之间的间隔字符数
cal=calendar.calendar(2017)
print(type(cal))
print(cal)
cal=calendar.calendar(2018,w=1,l=1,c=1)

#isleap :判断某一年是否为闰年
print(calendar.isleap(2000))
#leapdays:获取指定年份之间的闰年的个数
#ledpdays(y1,y2)  y1>y2 ,且不不含括号右边的年份
print(calendar.leapdays(1990,2020))
#month()获取某个月的日历字符串
#格式：calendar.month(年，月)
#回值：月日历的字符串
print(calendar.month(2019,2))

#monthrange()获取一个月的周几开始即和天数
#格式：calendar.monthrange(年，月)
#回值：元组（周几开始，总天数）
#注意：周默认 0-6 表示周一到周天
w,t=calendar.monthrange(2019,2)
print(w)
print(t)


#monthcalendar()返回一个月每天的矩阵列表
#格式：calendar.monthlendar（年，月）
#回值：二级列表
#注意：矩阵中没有天数用0表示
m=calendar.monthcalendar(2019,2)
for i in m :
     print(i)

#prcal: print calendar 直接打印日历
calendar.prcal(2018)

#prmonth()直接打印整个月的绒里
#格式：calendar.prmonth(年，月)
#返回值：无
calendar.prmonth(2018,2)

#weekday()获取周几
#格式：calendar.weekday(年，月，日)
print(calendar.weekday(2019,2,9))