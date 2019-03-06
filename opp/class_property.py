#变量的三种用法
class A():
    def __init__(self):
        self.name= "haha"
        self.age = 18
a=A()
#属性的三种用法
#1，赋值 2，读取 3，删除
a.name= "coco"
print(a.name)
del a.name
#print(a.name) 删除了这个属性，打印就会报错
print(">"*30)
#属性类 property
#应用场景：
#对变量除了普通的三种操作，还想增加一些附加的操作，可以通过property完成
class B():
    def __init__(self):
        self.name = "hhahaha"
        self.age = 18
        #此功能是对变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print("读取了")
        return self.name
    #模拟的是对变量进行写操作的时候执行的功能
    def fset(self,name):
        print("写入操作")
        self.name = "名字是："+name
    #fdel 模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass
    name2 = property(fget,fset,fdel,"文档的说明")
b = B()
print(b.name)
print(">"*30)
b.name2="xixi"
print(b.name2)

