#利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：
# 比如说["ADMAm","LISA","JACk"]
#["Admam","Lisa","Jack"]
def name(s):

    t = s.lower()
    t = t.capitalize()
    print(t)
    return t

#在python3中,map() 生成的是迭代器不是list， 你可以在map前加上list，即list(m)
print(list(map(name,["ADMAm","LISA","JACk"])))

#：回数:从左向右和从右向左读都是一样的数，例如 12321，999，请利用filter()函数
def equal(a,b):
    return a==b
def x(n):
    s = str(n) #先转换成字符串
    for i in range(len(s)-1):
        if equal(s[i],s[len(s)-i-1]):
            continue
        else:
            return False
    return True
output = filter(x,range(1,999))
print(list(output))

#假设，我们用一组tuple来表示学生的名字和成绩，
# L = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
# 用sorted()对上述列表按照名字排序
L= [("Bob",75),("Adam",92),("Bart",66),("List",88)]
def by_name(t):
    t = sorted(t[0],key=str.upper)
    return t
L1 = sorted(L,key=by_name)
print(L1)
#再按成绩高低排序
def by_score(t):
    t =sorted(range(t[1]),key=abs)
    return t
L3 = sorted(L,key=by_score)
print(L3)
#