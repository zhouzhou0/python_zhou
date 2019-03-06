# 函数作为返回值返回， 被返回的函数在函数体内定义
#调用mm2，返回一个函数mm3，赋值给f3
def mm2():
    def mm3():
        print('in mm3')
        return 3
    return mm3
f3 = mm2()
print(type(f3))
print(f3)
print(f3())

#案例2
#args:参数收集
#1，f4定义函数，返回内部定义的函数f5
#2，f5使用了外部变量，这个变量是f4的定义参数
def f4(*args):
    def f5():
        rst=0
        for i in args:
            rst+=i
        return rst
    return f5
ff=f4(1,2,3,4,5,6,7,8,9,10)
print(ff())

print('>'*30)

#闭包常见的坑
def count():
    fs = []
    for i in range(1,4):
        #定义一个函数f
        #f是一个结构
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
### 出现的问题：
#- 造成上述状况的原因是,返回函数引用了变量i， i并非立即执行，而是等到三个函数都返回的时候才统一使用，
     # 此时i已经变成了3，最终调用的时候，都返回的是 3*3

#- 此问题描述成：返回闭包时，返回函数不能引用任何循环变量

#- 解决方案： 再创建一个函数，用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何改变，
  #已经绑定的函数参数值不再改变
print('>'*30)
#修改上面函数
def count2():
    def f (j):
        def g ():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        #定义一个函数f
        #f是一个结构

        fs.append(f(i))
    return fs
f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())