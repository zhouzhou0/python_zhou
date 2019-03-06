#打印字母A
class zimu_game:
    def A(self):
        #控制行
        for i in range(1,6):
                #判断开始输入的位置
            for k in range(6-i):
                print(" ",end="")#两个空格代表一个字符
            #控制列
            for j in range(1,i+1):
                if i ==1 or i==3 or j==1 or j==i:
                   print("*",end=" ")
                else:
                  print("  ",end="")
            print( )
        print(">"*30)
    def B(self):
        #打印字母B
        for i in range(1,4):
            for j in range(1,4):
                if i==1 or i==4 or j==1 :
                    if j<3:
                        print("*",end=" ")
                elif j==3:
                    if i==2 or i==3:
                        print("*",end=" ")

                else:
                   print(" ",end=" ")
            print()
        for i in range(1,5):
            for j in range(1,4):
                if  i==1 or i==4 or j==1 :
                    if j<3:
                        print("*",end=" ")
                elif j==3:
                    if i==2 or i==3:
                        print("*",end=" ")

                else:
                   print(" ",end=" ")
            print()
        print(">"*30)
    def D(self):
        #打印字母D
        for i in range(1,5):
            for j in range(1,4):
                if  i==1 or i==4 or j==1 :
                    if j<3:
                        print("*",end=" ")
                elif j==3:
                    if i==2 or i==3:
                        print("*",end=" ")

                else:
                   print(" ",end=" ")
            print()
        print(">"*30)
    def C(self):
        #打印字母C
        for i in range(1,5):
            for j in range(1,4):
                if j ==1:
                    if i==2 or i==3:
                        print("*",end=" ")
               # elif i==1 or i==4:
                    #print(" ",end=" ")
                if j==2:
                    if i==1 or i==4:
                        print("*",end=" ")
                if j==3:
                    if i == 1 or i == 4:
                        print("*", end="")
                else:
                   print(" ",end=" ")

            print()
    def E(self):
        #字母E
        for m in range(1,8):
            for n in range(1,4):
                if m==1 or m==4 or m ==7 or n==1:
                   print("*",end=" ")
                else:
                  print(" ",end="")
            print()
        print(">"*30)
    def F(self):
        #字母F
        for m in range(1,8):
            for n in range(1,4):
                if m==1 or m==4  or n==1:
                   print("*",end=" ")
                else:
                  print(" ",end="")
            print()
        print(">"*30)
    def G(self):
        #字母G
        for m in range(1,6):
            for n in range(1,6):
                if m==1 or m==5 or n==1:
                    print("*", end=" ")
                if m==3 :
                    if n==3 or n==4 or n==2:
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
                if  m==4:
                    if n==4:
                        print("*", end=" ")
                    else:
                        print(" ",end=" ")
            else:
                print(" ", end="")
            print()


