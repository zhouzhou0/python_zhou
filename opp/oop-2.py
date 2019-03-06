#继承的语法
#在Python中，任何类都有一个共同的父类叫object
#子类中定义的成员和父类成员如果相同，则优先使用子类成员
class Person():
    name="coco"
    age = 20
    _petname="乳名"#是子类可以用但是不能公用
    __score=0# 私有
    def sleep(self):
         print("sleeping....")
    def work(self):
        print("make some money")
#父类写在括号里面
class Teacher(Person):
    name = "xiaoming"
    def make_test(self):
        print("up up up")
    def work(self):
        #1.扩充父类的功能只需要调用父类的相应函数,父类名.父类成员
        Person.work(self)#这个self代表的是Teache自己的实例
        self.make_test()
        #2.扩充的另外一种，super().父类成员的格式来调用
        super().work()
        print("make test")

t=Teacher()
print(t.name)
print(Teacher.name)
t.make_test()
t.sleep()
#私有变量访问
#print(t.__score) 公开访问私有变量，会报错
print(t._petname)
print(t.work())
