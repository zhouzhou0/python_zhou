#构造函数的概念
class Dog():
    #__init__就是构造函数
    #每次在实例化的时候，第一个被自动调用
    #因为主要工作是在进行初始化，所以得名

    def __init__(self):
        print("i am init in dog")
xiaohuang=Dog()

print(">"*60)
#继承中的构造函数

class Animal():
    pass
class pangxingAnimal(Animal):
    pass
class Dog(pangxingAnimal):
    def __init__(self):
        print("dog is very cute")
#实例化自动调用Dog的构造函数
huang = Dog()
print(">"*60)

#2.
class Animal():
    def __init__(self):
        print("Animal")
class PaxingAni(Animal):
    def __init__(self):
        print("paxing")
class Dog(PaxingAni):
    def __init__(self):
        print("i am init in dog")
class cat(PaxingAni):
    pass
#此时自动调用构造函数，cat里面没构造函数，所以自动调用父类的构造函数
#在paxingAni中找到了构造函数，则停止向上查找

c=cat()
#3.
class Animal():
    def __init__(self):
        print("Animal")
class PaxingAni(Animal):
    def __init__(self,name):
        print("paxing{0}".format(name))
class Dog(PaxingAni):
    def __init__(self):
        print("i am init in dog")
class cat(PaxingAni):
    pass
#c=cat() 这样就会报错，因为paxingAni里面的构造函数需要两个参数
#4.

print(">"*60)
class Animal():
    def __init__(self):
        print("Animal")
class PaxingAni(Animal):
    pass
class Dog(PaxingAni):
    pass
class cat(PaxingAni):
    pass
#一直向上找构造函数
c=cat()
print(">"*30)
#构造函数
class Person():
    def __init__(self):
        self.name="lala"
        self.age=18
        self.address= "beijing"
        print("i am funing")
p=Person()
#构造函数的调用顺序
#如果子类没有写构造函数，则自动向上查找，直到找到为止
class A():
    def __init__(self):
        print("A")
class B():
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    pass
c=C("lala")#向上查找，然后参数要和构造函数的参数相同