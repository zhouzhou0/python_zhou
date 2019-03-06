#包含一个学术类
#一个sayhello函数
#一个打印语句
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name,age)
    def say(self,name):
        print('hello,nice ti meet you,{}'.format(name))

def   sayhello():
    print('hello,hello,hello')
#此判断语句建议一直作为程序的入口
#if __name__=='__main__':
print('这个是模块p01.py')