#抽象类的实现
import abc
#声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    #定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drinking(self):
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def playing(self):
        pass
print(">"*30)
#自己组装一个类
class A():
    pass
def say(self):
        print("saying")
def play(self):
        print("playing")
class B():
    def say(self):
        print("saying")
say(2)
A.say=say
a=A()
a.say()
b=B()
b.say()
print(">"*30)
#组装类的例子2
from types import MethodType
class A():
    pass
def say(self):
    print("saying...")
a=A()
a.say= MethodType(say,A)
a.say()
print(">"*30)
#利用type造一个类
#先定义类应该具有的成员函数
#help(type)
def bi(self):
    print("bi bi bi")
def ci(self):
    print("ci ci ci")
#用type来创一个类   type(name, bases, dict) -> a new type
A = type("A_name",(object,),{"class_bi":bi,"class_ci":ci})
#然后可以像正常访问一样使用类
a=A()
print(dir(a))
a.class_bi()
a.class_ci()

print(">"*30)


#元类演示
#元类写法是固定的，必须继承自type
#元类一般命名以MetaClass(type)结尾
class JimeiMetaClass(type):
    def __new__(cls, name,bases,attrs):
        print("这个为元类")
        attrs['id']='952700'
        attrs['addr']='北京'
        return  type.__new__(cls,name,bases,attrs)
#元类定义完就可以使用
class Teacher(object,metaclass=JimeiMetaClass):
    pass
t=Teacher()
print(t.__dict__)
print(t.id)