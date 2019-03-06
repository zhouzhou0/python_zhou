#多继承
class Fish():
    def __init__(self):

        pass
    def smim(self):
        print("i can swinming...")
class Bird():
    def _init__(self):
        pass
    def fly(self):
        print("i can flying")
class Person():
    def __init__(self):
        pass
    def work(self):
        print("i can working")
class Superman(Person,Fish,Bird):
    def _init__(self):
        pass
    def magic(self):
        print("i hava magic")
p=Superman()
p.smim()
p.fly()
p.work()
p.magic()
print(">"*30)
#单继承
class Student(Person):
    def __init__(self):
        pass
stu=Student()
stu.work()
print(">"*30)

#菱形继承
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(">"*30)
#issubclass检测一个类是否是另一个类的子类
class A():
    pass
class B(A):
    pass
class C():
    pass
print(issubclass(B,A))
print(issubclass(C,A))
print(issubclass(C,object))#所有东西都是obje的子类
#dir获取对象的成员列表
class A():
    pass
dir(A)
a=A()
dir(a)