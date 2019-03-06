#给出提示信息
try:

     num = int(input('请输入一个数字：'))
     rst = 100/num
     print("计算结果是：{}".format(rst))
#捕获异常后，把异常实例化，出信息会在实例里面
#以下语句是捕获ZeroDivisionError异常并实例化实例e
except ZeroDivisionError as e:
     print('请输入正确的数字啊！！！！！！！！')
     print(e)
     #exit是退出程序
     exit()