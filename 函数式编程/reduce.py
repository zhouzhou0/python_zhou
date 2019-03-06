### reduce
#- 原意是归并，缩减
###- reduce([1,2,3,4,5]) == f( f(f(f(1,2),3), 4),5)
#- reduce 需要导入functools包




from functools import reduce
#定义一个操作函数
#加入操作函数只是相加
def add(x,y):
    return x+y

r = reduce(add,[1,2,3,4,5,6,7])
print(r)


