
#### 写一个用户登录验证程序，文件如下 1234.json

#1234.json
#{"expire_date":"2021-01-01","id":"1234","status":0,"pay_day":22,"password":"abc"}

#- 用户名为json的文件名
#- 判断是否过期，与expire_date做比较
#- 登陆成功后打印登陆成功，三次登陆失败，status值改为1，并且锁定账号
import os
import time
import json

count = 0

exit_flag = False

while count < 3 :
    user = input("请输入用户名：")
    f = user.strip()+'.json' #strip清除空格
    if os.path.exists(f):
        fp = open(f,"r+", encoding="utf-8") #r+ :读写 .
        j_user = json.load(fp)
        if j_user['status']==1:
            print('账号已经锁定')
            break
        else:
            expire_dt = j_user['expire_date']
            current_st = time.time()
            t= time.strptime(expire_dt, "%Y-%m-%d")
            expire_st = time.mktime(t)

            if current_st > expire_st :
                print('用户过期')
                break
            else :
                while count <3 :
                    pwd = input('请输入密码')
                    if pwd.strip() == j_user['password']:
                        print('登入成功')
                        exit_flag=True
                    else:
                        if count==2:
                            print('用户登入超过3次，锁定账号')
                            j_user['status']=1
                            fp.seek(0)
                            fp.truncate()#清空文件内容
                            json.dump(j_user,fp)
                    count +=1
    if exit_flag:
        break
    else:
        print('用户不存在')
        count +=1
