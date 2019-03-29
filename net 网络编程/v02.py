import socket
'''
    - Client端流程
            1. 建立通信的socket
            2. 发送内容到指定服务器
            3. 接受服务器给定的反馈内容
'''

def clientFunc():
    sock=socket.socket(socket.AF_INET,socket.AF_INET)
    # text="i have have  666"
    text=input('请输入要发送的消息')
    data=text.encode()

    # 发送消息
    sock.sendto(data,("127.0.0.1",7852))

    data,addr = sock.recvfrom(200)

    data = data.decode()
    print(data)

if __name__ == '__main__':
    while True:
        clientFunc()