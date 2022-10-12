#coding:utf-8

import socketserver
from socket import socket
from time import ctime

print("=====================SocketServer TCP服务器=====================");

HOST = '127.0.0.1'  #主机号为空白表示可以使用任何可用的地址。
PORT = 21567  #端口号
ADDR = (HOST, PORT)

class MyRequestHandler(socketserver.StreamRequestHandler):  #StreamRequestHandler实现TCP/UDP服务器的服务处理器
    def handle(self):  #重写接收响应函数
        print('连接到:', self.client_address)
        data = self.rfile.readline().strip()
        print(data)
        self.wfile.write(bytes('[%s] %s' % (ctime(), data.decode('utf-8')),'utf-8'))

tcpSerSock = socketserver.TCPServer(ADDR, MyRequestHandler)
print('等待连接...')
tcpSerSock.serve_forever()

BUFSIZ = 1024
ADDR = (HOST, PORT)


