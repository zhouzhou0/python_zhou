'''
正则Match的使用
'''
import re
# 以下正则分成了两个组，以下括号为单位
s=r'([a-z]+) ([a-z]+)'
pattern = re.compile(s,re.I) #s.I忽略大小写

m=pattern.match("Hello world wide web")

# group（0） 表示返回匹配成功的整个子串
s =m.group(0)
print(s)

a=m.span(0)#返回匹配成功的整个子串的跨度
print(a)

#group(1)表示返回第一个分组匹配的子串匹配
s= m.group(1)
print(s)

a=m.span(1)  #犯囧匹配成功的第一个子串的跨度
print(a)

s=m.groups() #等价与m.group(1),m.group(2).....
print(s)