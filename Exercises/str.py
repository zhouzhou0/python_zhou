help(str)



class A():
    def __init__(self,name):

        self.name=name.capitalize()#capitalize字母首写字母大写

p=A('mkmk')

print(p.name)
#capitalize()将首字母变为大写  返回字符串
#title() 将每个单词首字母都变为大写，  返回字符串
#upper()将所有字母都变为大写  返回字符串
s="do you have some apples ?"
print(s.title())
#lower()将所有字母变为小写 返回字符串
#swapcase()  大小写互换，   返回字符串
#len()计算字符长度，不属于字符的内建函数
s="I like dog 对啊"#空格占一位，汉字占一位
print(len(s))
#find()查找指定字符串 ，找不到返回-1,找到返回第一次索引值
#index()查找指定字符串，找不到报错，
print(">"*30)
u="dadasdkasdmldjlas"
s1=u.find("a",0,4)
s2=u.index("d")
print(s1)
print(s2)
#count() 计算字符串出现的次数
#startswith()检测是否以指定字母开头，返回布尔值
#endswith检测是否以指定字母结束
s="adscsafdhjnaskd"
print(s.startswith('a'))
print(s.endswith("a"))
print((s.endswith('d')))

print('>'*30)

#isupper()检测所有字母是否是大写字母
n='fsss'
m='Asss'
k='SSSSSA'
print(n.isupper())
print(m.isupper())
print(k.isupper())
print(">"*30)
#islower()检测所有字母是否是小写字母
print(n.islower())
#istitle() 检测是否以指定标题显示（）每个单词首字母大写
print(m.istitle())
print(n.istitle())
print(">"*30)
#isspace 在S中所有字符都是空格，返回True,在S中至少有一个字符，否则为False
k1="     "
k2='i have a apepl'
k3= ""#至少有一个空格，否则返回false
print(k1.isspace())

print(k2.isspace())
print(k3.isspace())

#isalpha()检测字符串是否是字母组成， 返回布尔值
m1='i like dog狗'
m2='ilikedog狗'
print(m1.isalpha())#空格也算
print(m2.isalpha())

#isalnum()检测字符串是否由字母加数字组成 返回布尔值
a1='i like dog狗321'
a2='ilikedog狗321'
a3='333333'
print(a1.isalnum())#有包含空格，返回fals
print(a2.isalnum())
print(a3.isalnum())
print(">"*30)
#isdigit()检测字符串是否由整数组成的
ss='12315'
print(ss.isdigit())
#isdecimal()检测数字不能检测二进制
#isnumeric()检测数字不能检测二进制

print('>'*20)
#split()用指定字符切割字符串  返回由字符串组成的列表
s='我是谁*我在哪*你又是谁*'
list=s.split("*")
print(list)
#splitlines以换行切割字符串
s='我是谁\n我在哪\n你又是谁'
print(s.splitlines())
#join()将列表按照指定字符串连接 ,返回的是字符串
sss= ['举头望明月','低头思故乡','日照香炉生紫烟']
lll= "+".join(sss)
print(lll)
#ljust指定字符串的长度，内容靠左边，不足的位置用指定字符串填充,默认是为空格,返回字符串
w='abcabc'
print(len(w))
print(w.ljust(10,'@'))
print(w.ljust(10)+'bbb')
#center() 指定字符串长度，内容居中，不足的位置用指定字符串填充，默认空格，返回字符串
print(w.center(10,'*'))
#rjust()指定字符串长度，内容靠右边，不足的位置用指定字符串填充，默认空格，返回字符串
print(w.rjust(10,'#'))
#strip()去掉左右两边指定字符，默认去掉空格
#lstrip()去掉左边指定字符，默认去掉空格
#rstrip()去掉右边指定字符，默认去掉空格
s='    abc   '
print('---',s.strip(),'---')
print('---',s,'---')
s0='aaaaabbcccc'
print(s0.lstrip('a'))
print(s0.lstrip('b'))#b不在左边，就原样输出
print(s0.rstrip('c'))
#zfill()指定字符串长度，内容靠右，不足的位置用0填充
pp='asdf'
print(pp.zfill(9))
#maketrans()生成用于字符串替换的映射表
#translate()进行字符串替换
r='你今年多大啊？你今天吃饭了吗？你多高啊？'
a=r.maketrans('多高','多矮')
print(a)
print(r.translate(a))