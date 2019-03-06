#元类演示
#元类写法是固定的，必须继承自type
#元类一般命名以MetaClass(type)结尾
class JimeiMetaClass(type):
    def __new__(cls, name,bases,attrs):
        print("这个为元类")
        attrs['id']='000000'
        attrs['addr']='北京'
        return  type.__new__(cls,name,bases,attrs)
#元类定义完就可以使用
class Teacher(object,metaclass=JimeiMetaClass):
    pass
t=Teacher()

print(t.id)
print(t.addr)