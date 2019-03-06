# 给大家补充几个高级函数
# zip
#- 把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
print(z)
for i in z :
    print(i)

print('*'*60)

l3 = ['xiaoming','kangkang','coco']
l4 = [88,92,100]
m = zip(l3,l4)
for k in m:
    print(k)

#enumerate 对可迭代对象里的每一元素，配上一个索引，
l5 = ['coco','mimi','rita']
en = enumerate(l5)
l6 = [k for k in en]
print(l6)

#enumerate 指定开始的索引
em = enumerate(l5,start=100)
l7 = [w for w in em]
print(l7)