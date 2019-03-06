### filter 函数 案例
#需要定义过滤函数，
#对于一个列表，对其进行过滤，偶数组成一个新的列表

#过滤函数要求有输入，返回布尔值
def xo(a):
    return a % 2 ==0
l = [2,3,4,666,4,3,456,5,5,6645,45]
r = filter(xo,l)
print(filter(xo,l))
print([i for i in r])

#排序的案例
#help(sorted)

a=[21,342,5656,777,453,232,884,4,56,774]
aa = sorted(a) #默认按照从小到大排序
aaa= sorted(a,reverse = True)#为true，为倒序
print(aa)
print(aaa)

#排序案例 2
b = [-45,-556,55,852,20,41,36]
#按照绝对值进行排序，
#abs是求绝对值的意思
#即按照绝对值的倒序排列
bb = sorted(b,key=abs,reverse = True)
print(bb)

#sorted案例
ss = ['xixi','DDom','xiaojing','coco','haha']
str1 = sorted(ss)
print(str1)
str2 = sorted(ss,key=str.upper)
print(str2)

#返回函数
#定义一个普通函数
def mmm(a):
    print('cici')
    return  None
a=mmm(0)
print(a)

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
