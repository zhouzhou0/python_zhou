class A():
    name="xiaoming"
    age=18

    def say(self):
        self.name="aaa"
        self.age=100
#此案例说明
#类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向统一变量
#此时，A称为类实例

print(A.name)
print(A.age)
print(id(A.name))
print(id(A.age))
print(A.__dict__)#查看A里面的属性
a=A()#对象实例
print(a.__dict__)#创建对象的时候，类中的成员不会放入对象当中，而是得到一个空对象，没有成员
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("*"*20)
b=A()
b.name="kankan"
b.age=10
print(b.__dict__)#赋值name和age之后多了两个属性
print(id(b.name))
print(id(b.age))


print(">"*60)



class Student():
    name="coco"
    age=22
    def say(self):
        self.name="mimi"
        self.age=16
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("my name is {}".format(__class__.name))#如果类方法中需要访问当前类的成员，可以通过 __class__成员名来访问

    def seeagain(self):
        print("hello,you are nice")
        print("{} is very cool".format(__class__.name))#调用类要用__class__.成员名称
kimi=Student()
kimi.say()
kimi.seeagain()

print(">"*60)

#self 案例
class A():
    name = "xiaohuang"
    age = 18
    def __init__(self):
        self.age = 111
        self.name = "cicici"
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name = "xiaohong"
    age = 66
a=A()
#此时，系统会默认把a作为第一个参数传入函数
a.say()

#此时，self被a替换
A.say(a)
#也可以把A作为参数传入
A.say(A)
#此时，传入的是类实例B，因为B具有name和age属性，不会报错
A.say(B)
#以上代码，利用了鸭子模型

print(">"*60)
#私有变量
class Person():
    name = "lion"
    __age=18   #__age是私有变量,只能在当前类或对象中访问
p=Person()
print(p.name)#name是公有变量
#print(p.__age) __age是私有，这样访问会报错
print(p._Person__age)#这样就可以访问可以使用对象._classname_attributename访












