#利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：
# 比如说["ADMAm","LISA","JACk"]
#["Admam","Lisa","Jack"]
#利用lambda函数

ls = ["ADMAm","LISA","JACk"]
new_ls = map(lambda x : x.lower().capitalize(),ls)
print(list(new_ls))

#：回数:从左向右和从右向左读都是一样的数，例如 12321，999，请利用filter()函数
#里面lambda函数
l1 = range(1,1000)
new_l1 = filter(lambda x :str(x)[0]==str(x)[len(str(x))-1],l1 )
print(list(new_l1))


#假设，我们用一组tuple来表示学生的名字和成绩，
# L = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
# 用sorted()对上述列表按照名字排序
#使用lambda函数
L = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
new_L = sorted(L,key=lambda x:x[0],reverse=True)
print(list(new_L))

#利用成绩高低来排序
L1 = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
new_L1 = sorted(L1,key=lambda x : x[1])
print(list(new_L1))