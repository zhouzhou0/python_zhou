
#collections模块
#- namedtuple
#- deque


### namedtuple
#- tuple类型
#- 是一个可命名的tuple

import collections
#help(collections.namedtuple)
point = collections.namedtuple('point',['x','y'])

p = point(22,33)
print(p.x)
print(p[0])

Circle = collections.namedtuple('circle',['x','y','r'])
c = Circle(10,10,20)
print(c)
print(type(c))

#想检测以下namedtuple到底属于谁的子类
print(isinstance(c,tuple))


# deque
#- 比较方便的解决了频繁删除插入带来的效率问题
from collections import deque
q = deque(['x','a','b','c'])
q.append('m')
print(q)
q.appendleft('w')
print(q)

#defaultdict
#- 当直接读取dict不存在的属性时，直接返回默认值
from collections import defaultdict
func =lambda: 'coco'
d2 = defaultdict(func)
d2['one'] = 1

print(d2['one'])
print(d2['two'])
print(d2['four'])



#Counter 统计字符串的个数
from collections import Counter

# 为什么下面结果不把abcdefgabced.....作为键值，而是以其中每一个字母作为键值
# 需要括号里内容为可迭代
m = Counter('abcdddabddacajjka')
print(m)

k = ['coco','xiaoming','coco','xiaopang']
a = Counter(k)
print(a)

