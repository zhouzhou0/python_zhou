import math
#math.ceil()向上取整
print(math.ceil(5.001))
print(math.ceil(5.96))

#math.floor()向下取整操作
print(math.floor(5.001))
print(math.floor(5.9))

print('*'*30)

'''
#查看系统保留关键字，不可用来当做变量的名称
import keyword
print(keyword.kwlist)
'''

#round()四舍五入操作 内置函数
print(round(5.4))
print(round(5.5))

#math.sqrt()开平方 , 返回浮点数
print(math.sqrt(4))

#math.pow(x,y) 与幂运算差不多，计算一个数的几次方,两个参数，x为底数，y为指数
#返回浮点型
print(math.pow(4,3))#4的3次方

#幂运算 返回整型
print(4**3)

#math.fabs() 对一个数获取他的绝对值  返回浮点数
print(math.fabs(-2))
print(math.fabs(3))

#abs()#获取绝对值 ，不是数学模块当中，是python内置函数
#返回值 本身类型而定
print(abs(-1))
print(abs(-2.5))
print(abs(0))

#fsum()对整个序列求和 返回浮点数
print(math.fsum([1,2,3,5,7]))

#sum()python 内置求和  返回本身类型而定
print(sum([1,2,3,5.0,7]))

#math.modf()将一个浮点数拆分成整数部分和小数部分组成元组  小数在前， 整数部分在后
print(math.modf(2.5))
print(math.modf(0))
print(math.modf(3))

#math.copysign() 将第二个数的符号（正负号） 传给第一个数
print(math.copysign(2,-1))
print(math.copysign(-1,3))

#打印自然对数e和π的值
print(math.e)
print(math.pi)