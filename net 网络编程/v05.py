import socket

def tcp_clt():
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('127.0.0.1',19720)
    sock.connect(addr)

    msg= input("输入信息")
    sock.send(msg.encode())
    rst=sock.recv(500)
    print(rst.decode())
    sock.close()


if __name__ == '__main__':
    tcp_clt()