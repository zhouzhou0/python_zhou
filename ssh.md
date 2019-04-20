连接 ：ssh python@192.168.136.137

ssh连接The authenticity of host can't be established

修改/etc/ssh/ssh_config文件的配置，以后则不会再出现此问题

最后面添加：

StrictHostKeyChecking no

UserKnownHostsFile /dev/null

输入 ssh  -o StrictHostKeyChecking=no  192.168.0.xxx　
输入密码
再次scp，正常输入密码，问题解决。



 从一台虚拟机复制文件到另外一台: scp /home/tlxy/all_db.sql python@192.168.136.137:/home/python

# 查询openssl软件
    rpm -qa openssh openssl
# 查询sshd进程
    ps -ef | grep ssh
        --> /usr/sbin/sshd
# 查看ssh端口
    netstat -lntup | grep ssh  
    ss | grep ssh                (效果同上，同下，好用)
    netstat -a | grep ssh(记住这个)
    netstat -lnt | grep 22    ==>  查看22端口有没有开/ssh服务有没有开启
    技巧： netstat -lnt | grep ssh | wc -l -->只要大于2个就是ssh服务就是好的
# 查看ssh的秘钥目录
    ll /root/.ssh/known_hosts  # 当前用户家目录的.ssh目录下
# ssh的配置文件
    cat /etc/ssh/sshd_config   
# ssh服务的关闭
    service sshd stop
# ssh服务的开启：
    service sshd start
# ssh服务的重启
    service sshd reload    [停止进程后重启] ==> 推荐
    service sshd restart   [干掉进程后重启] ==> 不推荐
