#使用shelve创建文件并使用
import  shelve
#打开文件
#shelve相当于一个字典
shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv ['three'] = 3
shv.close()

#shelve案例的读取
shv = shelve.open(r'shv.db')
print(shv['one'])
print(shv['three'])
shv.close()

print('/'*30)

shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['four'])
except Exception as e:
    print('出差错啦')
finally:
    shv.close()

print('@'*30)

#shelve 只读打开
shv = shelve.open(r'shv.db',flag = 'r')
try :
    k1 = shv['one']
    print(k1)
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try :
    shv['one']= {'11':1,'66':1,'77':1}
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()

#shelve忘记写回，需要强行写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
   #此时，一旦shelve关闭，则内容还是存在内存中，没有写会数据库
    k1['11']=100
finally:
    shv.close()

shv = shelve.open(r'shv.db',writeback=True)
try:
    k1 = shv['one']
    print(k1)
   #此时，一旦shelve关闭，则内容还是存在内存中，没有写会数据库
    k1['11']=100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1= shv['one']
    print(k1)
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()


#shelve 使用with管理上下文环境

with shelve.open(r'shv.db',writeback=True) as shv :
    k2 = shv['one']
    print(k2)
    k2['66']=1000
with shelve.open(r'shv.db') as shv :
    print(shv['one'])
    ##