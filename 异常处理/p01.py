#异常案例
try:

     num = int(input('请输入一个数字：'))
     rst = 100/num
     print("计算结果是：{}".format(rst))
except:
     print('请输入正确的数字啊！！！！！！！！')
     #exit是退出程序
     exit()


