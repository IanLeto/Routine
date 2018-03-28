from socket import *

# HOST = 'localhost'
HOST = '::1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock = socket(AF_INET6, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    # 客户端发送数据
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()
# while True:
#     data = input('> ')
#     if not data:
#         break
#     tcpCliSock.send(data.encode())
#     data = tcpCliSock.recv(BUFSIZ).decode()
#     if not data:
#         break
#     print(data)
#
# tcpCliSock.close()
