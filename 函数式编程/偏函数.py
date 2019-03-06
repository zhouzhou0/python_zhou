#把字符串转化成十进制的数字
print(int('12345'))

#求八进制的字符串12345，表示成10进制
print(int('12345',base=8))

#新建一个函数 ，此函数是默认输入的字符串是16进制的数字
#把此字符串返回十进制的数字
def int16(x,base=16):
    return int(x,base)
print(int16('12345'))

### 偏函数
#- 参数固定的函数，相当于一个由特定参数的函数体
#- functools.partial的作用是，把一个函数某些函数固定，返回一个新函数

import functools
#实现上面int16的功能
int16_16 = functools.partial(int,base = 16)
print(int16_16('12345'))