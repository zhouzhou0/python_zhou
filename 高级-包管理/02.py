import importlib
#相当于导入了一个叫01的模块并把导入模块赋值给了kkk
kkk= importlib.import_module('01')
sss=kkk.Student('coco',18)
sss.say('coco')