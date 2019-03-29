'''
    - Server端流程
            1. 建立socket，socket是负责具体通信的一个实例
            2. 绑定，为创建的socket指派固定的端口和ip地址
            3. 接受对方发送内容
            4. 给对方发送反馈，此步骤为非必须步骤
'''

# socket模块负值socket
import socket

# 模拟服务器的函数
def serveFunc():
    # 1.建立socket

    #socket.AF_INET：使用ipv4协议族
    #socket.SOCK_DGRAM:使用UDP通信
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2.绑定IP和port
    # 127.0.0.1 这个ip代表的机器本身
    # 7899随便指定的端口号，但不能使用0-1024号
    # IP地址是一个tuple（ip，port）
    addr = ("127.0.0.1",7852)
    sock.bind(addr)

    #接受对方消息
    # 等待方式为死等，没有其他可能性
    # recvfrom接受的返回值是一个元组，前一项表示数据，后一项地址
    # 参数的含义是缓冲区大小
    # rst= sock.recvfrom(500)
    data,addr =sock.recvfrom(500)
    print(data)
    print(type(data))
         # 发生过z来的数据是bytes格式，必须通过解码才能等到str格式的内容
         #decode()默认参数是utf-8
    text = data.decode()

    print(type(text))
    print(text)

    # 给对方返回消息
    rsp = " la la la ha ha ha"
    # 发送的数据需要编码成bytes
    data=rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    print('starting serve...')
    serveFunc()
    print('ending')