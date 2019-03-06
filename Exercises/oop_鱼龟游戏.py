#定义一个门票系统
#门票的原价是100元
#当周末的时候门票上涨20%
#小孩半价
#计算两个大人和一个小孩平日的门票价格
class ticket():
    def  __init__(self,weekend = False,child=False):
        self.exp= 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc=1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def price(self,num):
        return self.exp*self.inc*self.discount*num
adult=ticket()
child=ticket(child= True)
print('两个成年人和一个小孩子的票价{}'.format(adult.price(2)+child.price(1)))
#### 游戏编程：按一下要求定义一个乌龟类和鱼类并尝试编程
#- 假设游戏场景为范围(x,y)为 0<=x<=10,0<=y<=10
#- 游戏生成1只乌龟和10条鱼
#- 他们的移动方向均随机
#- 乌龟的最大移动能力是2（乌龟可以随机选择移动是1还是2），鱼的最大移动能力是1
#- 当移动到场景边缘，自动向反方向移动
#- 乌龟初始化体力为100（上限）
#- 乌龟每移动一次，体力消耗1
#- 当乌龟和鱼重叠，乌龟吃掉鱼，乌龟体力增加20
#- 鱼不计算体力
#- 当乌龟体力值为0或者鱼的数量为0时，游戏结束

import random as r
class Turtle ():
    def __init__(self):
        self.power = 100
        #初始化乌龟的位置
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        new_x = self.x + r.choice([1,-1,2,-2])
        new_y = self.y + r.choice([1,-1,2,-2])
        #判断乌龟是否超出了边界
        if new_x < 0:
            self.x = 0-(new_x)
        elif new_x >10:
            self.x = 10 - (new_x-10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y)
        elif new_y > 10:
            self.y = 10 - (new_y-10)
        else:
            self.y = new_y

        self.power -=1
        return (self.x,self.y)
    def eat(self):
        self.power+=20
        if self.power >=100:
            self.power=100
class Fish():
    def __init__(self):
        self.x = r.randint(1,10)
        self.y = r.randint(1,10)
    def move(self):
        new_x = self.x + r.choice([1,-1])
        new_y = self.y + r.choice([1,-1])
        if new_x < 0:
            self.x = 0 - (new_x)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        return (self.x,self.y)
turtle = Turtle()
fish=[]
for i in range(10):
    new_fish=Fish()
    fish.append(new_fish)
while True:
    if not len(fish):
        print('鱼被吃完啦，游戏结束')
        break
    if not turtle.power :
        print('乌龟没有体力了，结束游戏')
        break
    pos = turtle.move()
 # 在迭代中做列表的删除元素是非常危险的，经常会出现一些意想不到的问题，
# 因为迭代器是直接引用列表元素的数据做的操作
 # 所以 我们这里把列表拷贝一份传给迭代器，然后再对原列表做操作
    for each_fish in fish [:]:
        if each_fish.move() == pos :
            turtle.eat()
            fish.remove(each_fish)
            print('有一条鱼被吃了')

#### 定义一个点（point）和直线（Line）类，使用getLen方法获取两点构成直线的长度
import math
class point():
    def __init__(self,x=0,y=0):
        self.x =  x
        self.y =  y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
class line():
    def __init__(self,p1,p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()
    def get_line(self):
        line = math.sqrt(self.x*self.x+self.y*self.y)
        return line



p1 = point(6,6)
p2 = point(2,5)
Line = line(p1,p2)
Line.get_line()