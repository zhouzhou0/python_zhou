import socket

def tcp_srv():
    # 1.建立socket负值具体的通信， 这个socket其实只负责接受对方的请求，真正的通信是链接后新建立的socket
    # 需要用到两个参数
    # AF_INET:含义同udp一致
    # SOCK_STREAM:表明使用tcp进行通信
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定端口和地址
    # 此地址信息是一个元组类型，元组分两部分，一部分是字符串，代表ip,第二部分是数字，代表端口，建议10000以上
    addr=("127.0.0.1",19720)
    sock.bind(addr)
    # 3.监听接入的访问socket
    sock.listen()
    while True:
        # 4.接收访问的socket，可以理解接收访问即建立了一个通讯的链接通路
        # accept 返回的元组第一个元素赋值给skt，第二个赋值给addr
        skt,addr = sock.accept()

        # 5. 接受对方的发送内容，利用接收到的socket接收内容
        # 500代表接收使用的buffersize
        # msg = skt.receive(500)

        msg =skt.recv(500)
        msg = msg.decode()

        # 6. 如果有必要，给对方发送反馈信息
        rst ="Received: msg{0} from{1}".format(msg,addr)
        print(rst)
        skt.send(rst.encode())
        skt.close()

if __name__ == '__main__':
    print('starting...')

    tcp_srv()

    print('ending...')
