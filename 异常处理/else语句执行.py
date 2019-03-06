#else 语句案例

try:
    num = int (input('输入一个数字'))
    rst = 100/num
    print('结果是{}'.format(rst))
except Exception as e :
    print('Exception')

else:
    print('No Exception')
finally:
    print('finally语句一定会被执行的')