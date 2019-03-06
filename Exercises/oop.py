#习题1
#定义一个学生类，有下面的类属性
#1.姓名 2年龄 3成绩（语文，数学，英语）每课成绩类型为整数类方法
#4.获取学生姓名：get_name()返回类型：str
#5.获取学生的年龄：get_age()返回类型：int
#6. 返回3们科目中的最高成绩，get_course()返回类型：int
class Student(object):
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return  max(self.scores)
z= Student('小周',20,[80,85,90])
print(z.get_name())
print(z.get_age())
print(z.get_course())

print('>'*30)

#2.习题2
#定义一个字典类：DictClass
#1.删除某个key del_dict(key)，
#2.判断某个键是否在字典里面，如果在返回值对应的值，不在则返回not found get_dict()
#3.返回键组成的列表：返回类型：list get_key()
#4.合并字典，并且返回合并后字典的values组成的列表，返回类型list update_dict()
class DictClass():
    def __init__(self,dict):
        self.dict=dict
    def del_dict(self,key):
        #判断key是否在字典里面
        if key in self.dict.keys():
            self.dict.pop(key)
            return '删除成功'
        else:
            return '字典里面没有这个key'

    def get_dict(self,key):
        if key not in self.dict.keys():
            return 'not found'
        else:
            return self.dict[key]
    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict2):
        self.dict=dict(self.dict,**dict2)
        return  self.dict
d=DictClass({'a':1,'b':2,'c':3})

print(d.update_dict({'d':4}))

print('>'*30)

#定义一个列表的操作类ListInfo   包括方法
#1.列表元素添加：add_key() 添加的必须是数字或者是字符串
#2.列表元素取值：get_key()
#3.列表合并：update_list(list)
#4.删除并且返回最后一个元素：del_key()
class ListInfo():
    def __init__(self,list_val):
        self.list=list_val
    def add_key(self,key_name):
        #添加的key必须是数字或者字符串
        if isinstance(key_name,(str,int)):
            self.list.append(key_name)
            #print(self.list)
            return  self.list
        else:
            return '请输入字符串或者数字'
    def get_key(self,index):
        #判断传入的索引是否超出了列表
        if index >= 0 and index < len(self.list):
            return self.list[index]
        else:
            return '超出范围'
    def upadte_list(self,new_list):

        self.list.extend(new_list)
        return self.list
    def del_key(self):
        #首先是要判断我们列表里面还有元素
        if len(self.list) >=0 :
            return self.list.pop(-1)
        else:
            return '列表为空'

l=ListInfo([1,2,3,4,5,6])
print(l.add_key(99))
print(l.get_key(2))
print(l.upadte_list([8,9,10,11,12]))
print(l.del_key())



print('>'*30)

#定义一个列表的操作类   包括方法
#1.集合元素添加：add_setinfo()
#2.集合的交集：get_intersection()
#3.集合的并集：get_union()
#4.集合的差集：get_difference()
class SetInfo():
    def __init__(self,my_set):
        self.seit=my_set
    def add_setinfo(self,keyname):
        self.seit.add(keyname)

        return self.seit
    def get_intersection(self,union):
        if isinstance(union,set):
            return self.seit & union
        else:
            return '输入的不是集合'
    def  get_union(self,union):
        if isinstance(union, set):
            return  self.seit | union
        else:
            return '输入的不是集合'
    def get_difference(self,union):
        if isinstance(union, set):
            return self.seit - union
        else:
            return '输入的不是集合'
my_set= SetInfo({1,2,3,4,5,6})
print(my_set.get_union('111'))

print(my_set.get_difference({5,6,7,8}))

