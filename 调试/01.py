def sayhello(name):
    print('my name is {}'.format(name))
    print('hahaha')
    print('hello'.format(name))


if __name__ =="__main__":
    print('*'*50)
    a = input('please input your name')
    print(sayhello(a ))
    print('@'*20)
