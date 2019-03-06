import  random
import math
'''
输入一个三位数与程序的随机数进行比较大小
如果大于程序的随机数，则分别输出这个三位数的个位/十位/百位
如果等于随机数，则提示中奖，记100分
如果小于随机数，则将120个字符输入到文本中
    （规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后八个是数字）
'''
#定义一个变量用于存取分数
class NumGame():
    def num_game():
        source=0
        #定义一个变量总计输入多少次
        total=0
        while 1:
           #程序可以一直执行，不然执行一次，就要重开一次程序


         num= input("请输入一个三位数,输入-1结束:")#输入函数返回的是字符类型，不能与整形直接比较，需要强制类型转换
        #程序随机数
         if num== '-1':
             break
         random_num = random.randrange(100,1000)
          #定义一个空字符串用于拼接
         def line(self):
            str_num =''
            #循环前四个随机字母（用ascii对应的值来随机在转换为字母）
            for i in range(4):
                #随机小写字母的ascii值
                num = random.randrange(97,123)
                #ascii值转换为对应 的字母
                str_s=chr(num)
               #依次等到随机字母
                str_num=str_num+str_s
                #print(str_num)
             #循环后8个随机数字
            for i in range(8):
                num = random.randrange(0,10)
                str_num = str_num+str(num)
            return  str_num

            #print(str_num)
         if num.isdigit() and 100<= int(num)<=999:#判断是否为纯数字
            #计算有效输入了多少次
            total+=1
            print("有效输入了%d次"%total)
            num=int(num)#强制换类型
            random_num=int(random_num)
            #判断随机数与输入数的大小关系
            if num >random_num:
                ge=   num%10
                shi= num%100//10
                bai= num //100
                print("个位是{0},十位是{1},百位是{2}".format(ge,shi,bai))
                #个位，直接对10取摸
                #十位，先取余，再用地板除10
                #求百位地板除100，或用数学模块里面的floor（）


            if num == random_num:
                source +=10
                print("您中奖啦,目前分数为",source)
                print("您中奖的概率是多少",source/total)
            if num <random_num:
                #由于120个字符每行12个，只要输入10行
               for i in range(10):
                  str_line=line(0)
                  print(str_line)
                 #执行文件存入操作
                  with open('str_num.txt','a') as f:
                      f.write(str_line+'\n')


         else:
            print("请输入规范的三位数")


#程序入口
if __name__=='__main__':
    #print(__name__)#在本身模块中__name__==__main__,当第三方导入的时候，__name__=文件名

 NumGame.num_game()
#