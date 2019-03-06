#raise案例2
#自己定义异常
#需要注意  ： 自定义异常必须是系统异常的子类
class QwaError(ValueError):
    pass
try:
    print('my name is coco')
    print(66666)
    #手动引发一个异常
    #注意语法 raise ErrorClassName,直接跳到指定的异常
    raise QwaError
    print('还没有结束')
except NameError as e :
    print('NameError')

except ValueError as e :
    print('ValueError')
except Exception as e :
    print('所有异常的父类')
finally:
    print('此条语句肯定会被执行的!!!')