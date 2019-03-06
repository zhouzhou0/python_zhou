#属性案例
#创建Student类，描述学生类
#学生具有Student.name属性
#但name格式并不统一
#可以用增加一个函数，然后自动调用的方式
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.setName(name)
     #介绍自己
    def intro(self):
        print("my name is {}".format(self.name))

    def setName(self,name):#把字母都改成大写
        self.name=name.upper()

s1=Student("Zhou Ge",20)
s2=Student("huang ming",20)
s1.intro()
s2.intro()
print(">"*30)
#property案例
#定义一个Person类，有name，age属性
#姓名全部用大写，年龄全部用整数
#x=property(fget,fset,fdel,doc)
class Person:
    '''
    这里是文档的信息
    '''

    #函数名称可以任意
    def fget(self):
        return  self._nam*2
    def fset(self,name):
        self._nam=name.upper()
    def fdel(self,name):
        self._nam = "NO name"
    name = property(fget,fset,fdel,"文件操作")
p=Person()
p.name="zhou zhou "
print(p.name)


print(">"*30)


#upper所有字母都大写，capitalize首字母大写
class Student1():
    def __init__(self,name,age):
        self.name=name.upper()
        self.age=age

     #介绍自己
    def intro(self):
        print("my name is {}".format(self.name))
s=Student1('mbmbm',20)

print(s.name)

#类的内置属性举例
print(Student.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)#查父类

print(">"*30)
#__call__举例
class A():
    def __init__(self):
        print("调用1")
    def __call__(self):
        print("调用2")
    def __str__(self):#当对象被当做字符串使用的时候调用
        return "字符串"
a=A()
a()#把实例当函数来用调用的call函数
print(a)



print(">"*30)
#__getattr__ 访问一个不存在的属性时触发
class A():
    name="coco"
    age=18
    def __getattr__(self,name):
        print("%s没有这个属性"%name)
        print(name)
a=A()
print(a.name)
print(a.age)
print(a.ddd)


print(">"*30)

#__setattr__案例...对成员属性进行设置的时候触发
class Person():
    def __init__(self):
        pass
    def __setattr__(self, key,value):
        print("设置属性：{}".format(key))
        #下面语句会导致死循环
        #self.name = value
        #为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(key,value)
p=Person()
p.age=18
print(p.age)

print(">"*30)

#__gt__进行大于判断的时候触发的函数
class Student():
    def __init__(self,name):
        self._name=name

    def __gt__(self,obj):
        print("{0}会比{1}大吗".format(self._name,obj._name))
        return self._name>obj._name
stu1= Student("two")
stu2= Student("one")
print(stu1>stu2)


print(">"*30)
#类和对象的三种方法
class Person():
    #实例方法
    def eat(self):
        print(self)
        print("eat eat eat")
        #类方法
        #类发放的第一个参数一般命名为cls，区别与self
    @ classmethod
    def play(cls):
        print(cls)
        print("play play play")

    #静态方法
    #不需要用第一个参数表示自身或者类

    @staticmethod
    def say():
        print("say say say")
#实例方法
p=Person()
p.eat()
#类方法
Person.play()
p.play()
#静态方法
Person.say()
p.say()













