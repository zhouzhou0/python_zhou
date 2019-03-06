from pkg02 import *

stu = p01.Student('coco',19)
stu.say('xixi')

#stu.koko()   #这个就无法调用，因为__init__.py 里面已经设置了__all__,所有只调用了__all__里面的