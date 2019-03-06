#编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
def jianfa(a,b):
    if a < b :
        raise BaseException ('被减数不能小于整数哦')
    else:
        return a-b
try :
    jianfa(3,7)
except BaseException as error :
    print('{}'.format(error))

 #定义一个函数func(filename) filename:文件的路径，
 #函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误
import os
def func(filename):
    try:
        file= open(filename)
    except Exception as error:
            print('出错内容是{}'.format(error))
    else :
        print(file.read())
        file.close()
func('haha.txt')


#自己定义一个异常类，继承Exception类, 捕获下面的过程：判断输入的字符串长度是否小于5
class Error(Exception):
    def __init__(self,str1):
        self.str1=str1
    def process(self):
        if len(self.str1) < 5:
            print('字符串长度小于5')
        else:
            print('OK')
try :
    e = Error('sssssss')
    e.process()
except Error as err:
    print(error)