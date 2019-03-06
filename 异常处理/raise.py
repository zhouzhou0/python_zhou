#raise案例
try:
    print('my name is coco')
    print(66666)
    #手动引发一个异常
    #注意语法 raise ErrorClassName,直接跳到指定的异常
    raise ValueError
    print('还没有结束')
except NameError as e :
    print('NameError')
except ValueError as e :
    print('ValueError')
except Exception as e :
    print('所有异常的父类')
finally:
    print('此条语句肯定会被执行的!!!')