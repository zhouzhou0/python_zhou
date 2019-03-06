'''
 定义一个学生类，用来形容学生
'''
 #空的类
class Student():
     #一个空类，pass代表跳过，但是pass不能省略
     pass
 #定义一个对象
xiaoming= Student()

 #在定义一个类，用来描述听python的学生
class PythonStudent():
     # 用None给不确定的值赋值
     name = None
     age = 18
     course = "python"

     # 需要注意
     # 1. def doHomework的缩进层级
     # 2. 系统默认由一个self参数

     def doHomework(self):
         print("i am doing homework")
         # 推荐在函数末尾使用return语句
         return None
xiaoming= PythonStudent()
print(xiaoming.age)
print(xiaoming.name)
xiaoming.doHomework()
# 注意成员函数的调用没有传递进入参数
