# from socket import *
# from time import ctime
#
# HOST = ''
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)
#
# while True:
#     print('waiting...')
#     tcpCliSocket, addr = tcpSerSock.accept()
#     print()
#
#     while True:
#         data = tcpCliSocket.recv(BUFSIZ)
#         if not data:
#             break
#             tcpCliSocket.send('[%s] %s' %(bytes(ctime(), 'utf-8'), data))
#         tcpCliSocket.close()



from socket import *
from time import ctime

'''
    tcp 服务端socket 代码
'''

# 空白行,对bind()方法的标识,表示它可以使用任何可用的地址
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# tcpSerSock tcp 套接字(通信端点)
# 换句话说创建服务器套接字
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock = socket(AF_INET6, SOCK_STREAM)
# 将地址绑定到套接字上
# 因为服务器需要占用一个端口并等待客户端的请求,so 必须要绑定到一个地址上
tcpSerSock.bind(ADDR)
# 启动tcp(开始监听连接)
tcpSerSock.listen()

while True:
    print('waiting for connection')
    # tcpSerSock 相当于老鸨
    # tcpCliSock 一个独立的套接字
    # tcpCliSock 相当于 嘿嘿嘿 (（づ￣3￣）づ╭❤～)
    # accept() 相当于启动循环-- 接收客户端连接 单线程
    # 一旦建立连接,客户拿好牌子,老鸨开始招待下一个 客户
    # 即服务器会创建一个新的通信端口来直接与客户端进行通信,并空出主要端口
    tcpCliSock, addr = tcpSerSock.accept()
    print('....connected from ', addr)
    # 通信循环
    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        # 当客户端关闭or发送空字符串时,会话终止
        if not data:
            break
        # 客户端返回参数
        tcpCliSock.send(('[%s] 传入data为: %s' %(bytes(ctime(), 'utf-8'), data)).encode())
    tcpCliSock.close()
tcpSerSock.close()
