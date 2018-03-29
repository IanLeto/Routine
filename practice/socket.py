

from socket import *
from time import ctime

'''
    tcp 服务端socket 代码
'''

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# tcpSerSock tcp 套接字(通信端点)
tcpSerSock = socket(socket, AF_INET, SOCK_STREAM)
# 将地址绑定到套接字上
tcpSerSock.bind(ADDR)
# 启动tcp
tcpSerSock.listen()

while True:
    print('waiting for connection')
    # tcpCliSock 一个独立的套接字
    # tcpSerSock 相当于老鸨
    # tcpCliSock 相当于 嘿嘿嘿 (（づ￣3￣）づ╭❤～)
    # accept() 相当于启动循环
    tcpCliSock, addr = tcpSerSock.accept()
    print('....connected from ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(bytes(ctime(), 'utf-8'),data))
    tcpCliSock.close()
tcpSerSock.close()
