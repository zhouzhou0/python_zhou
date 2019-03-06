import random

#random.random()  获取0-1之间的随机小数,包含0，不包含1
for i in range(10):
    print(random.random())

#random.randint()随机指定开始和结束的整数值
for m in range(10):
    print(random.randint(1,10)) #包含1和包含10
#random.randrange() 获取指定开始和结束之间的整数值，可以指定间隔值
    print(random.randrange(1,10))
    print(random.randrange(1,10,3))#随机打印1 4 7 10
print('*'*50)
#random.choice() 随机获取列表中的值
print(random.choice([1,5,36,77,12,10]))

#shuffle()随机打乱序列 ,返回值是None
l = [1,3,5,10]
print(l)
random.shuffle(l)
print(l)

#uniform()随机获取指定范围的值(包括小数)
for k in range(10) :
    print(random.uniform(1,10))

