try:

     num = int(input('请输入一个数字：'))
     rst = 100/num
     print("计算结果是：{}".format(rst))
#捕获异常后，把异常实例化，出信息会在实例里面
#以下语句是捕获ZeroDivisionError异常并实例化实例e

#如果是多种error的情况，需要把越具体的错误，越往前放
#在异常类继承关系中，越是子类的异常，越要往前放
#越是父类的异常，越要往后放

#在处理异常的时候，一旦拦截到某一个异常，则不在继续往下看，直接进行下一个
#代码，即有finally 则执行finally语句块，否则就执行下一个大的语句
except ZeroDivisionError as e:
     print('请输入正确的数字啊！！！！！！！！')
     print(e)
     #exit是退出程序
     exit()
except NameError as e :
    print('name错了')
    print(e)
except AttributeError as e :
    print('属性有问题')
    print(e)
#所有异常都是继承Exception
#如果写 下面这句话，任何异常都会拦截住
except Exception as e:
    print("不知道哪里错了呀")
    print(e)
except ValueError:#因为所有的异常都是继承Exception，所有此条不会执行.
    print('no no no no')

print('hahahah')