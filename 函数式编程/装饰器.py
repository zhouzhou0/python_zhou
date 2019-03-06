def hello():
    print('hello world')
hello()
f = hello
f()
#f和hello是同一个函数
print(id(hello))
print(id(f))
# 现在由新的需求：
# 对hello功能进行扩展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# ==>使用装饰器
import time

#高阶函数，以函数作为参数
def printtime(f):
    def wrapper(*args,**kwargs):
        print('Time:',time.ctime())
        return f(*args,**kwargs) #调用f函数，执行它
    return wrapper
#s上面定义了装饰器，使用的时候需要用到@此符号是python的语法糖

@printtime
def hello():
    print('hello world')
hello()

# 装饰器的好处是，一点定义，则可以装饰任意函数
# 一旦被其装饰，则则把装饰器的功能直接添加到定义函数的功能上

print('>'*30)
# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数
def hello3():
    print('我是手动执行的')
hello3=printtime(hello3)
hello3()

print('>'*30)

f = printtime(hello3)
f()