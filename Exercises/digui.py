#递归案例
#类似于栈的先进后出模式
#1要有递推关系
#传入3，打印3，进入判断，调用本身，然后后面的程序等待不执行，打印2
def digui(num):
    print("$"+str(num))#相加必须要两个相同的类型
    if num > 0:
        digui(num-1)
    else:
        print('>'*30)

    print(num)
digui(3)
print(">"*30)
#汉诺塔
i = 0
def move(n,a,b,c):
    global i

    if n==1:
        i+=1
        print('移动第',i,'次',a,'>>>>',c)
    else:
        #先把n-1个盘子从A移到B上面
        move(n-1,a,c,b)
        #在把最大的那个圆盘从A移到C
        move(1,a,b,c)
       #把B上面的n-1个圆盘在移到C
        move(n-1,b,a,c)
move(4,'A','B','C')