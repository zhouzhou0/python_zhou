# lambda表达式的用法
# 1. 以lambda开头
# 2. 紧跟一定的参数（如果有的话）
# 3. 参数后用冒号和表达式主题隔开
# 4. 只是一个表达式，所以，没有return


# 计算一个数字的100倍数
# 因为就是一个表达式，所以没有return
stm = lambda x : 100*x
print(stm(20))

#多个参数
sss = lambda x,y,z : 100*x + (y+30)+ z
print(sss(1,2,3))

#函数名称就是一个变量
def funa():
    print("funa")
funb=funa
funb()
### 以上代码得出的结论：
#- 函数名称是变量
#- funb 和 funa只是名称不一样而已
#- 既然函数名称是变量，则应该可以被当做参数传入另一个函数
print(">"*30)
#高阶函数举例
#funA是普通函数，返回一个传入数字的100倍数字
def funA(n):
    return n*100
#在写一个函数，把传入参数乘以300倍，利用高阶函数
def funB(n):
    #最终 返回300n
    return funA(n)*3
print(funB(2))

#写一个高阶函数
def funC(n,f):
    #假定函数是把n扩大300倍
    return f(n)*3
print(funC(2,funA))


def funD(n):
#放大30倍
    return n*10
print(funC(2,funD))

#map举例
#有一个列表，想对列表里的每一个元素乘以10，并得到新的列表
l1 = [i for i in range(10)]
print(l1)

l2=[]
for i in l1:
    l2.append(i*10)
print(l2)
#利用map实现
def mm(n):
    return n*10
#map类型是一个可迭代的结构，所以可以使用for遍历
l3=map(mm,l1)
for i in l3:
    print(i,end=" ")

from functools import reduce
#定义一个操作函数
#加入操作函数只是相加

#- reduce([1,2,3,4,5]) == f( f(f(f(1,2),3), 4),5)
def add(x,y):
    return x+y

r = reduce(add,[1,2,3,4,5,6,7])
print(r)



#




