#### 写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母
import random
import string
#help(string)
code = []
code.append(random.choice(string.ascii_lowercase))
code.append(random.choice(string.ascii_uppercase))
code.append(random.choice(string.digits))
while len(code) <6 :
    code.append(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits))

print(code)
for i in code :
    print(i,end="")

