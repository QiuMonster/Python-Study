#coding:utf-8

from socket import *

print("=====================SocketServer TCP客户端=====================");

HOST = '127.0.0.1'  #本机测试
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)   #创建客户端套接字
    tcpCliSock.connect(ADDR)   #发起TCP连接
    data = input('> ')  #接收用户输入
    if not data:   #如果用户输入为空，直接回车就会发送""，""就是代表false
        break
    tcpCliSock.send(bytes(data+'\n','utf-8'))   #客户端发送消息，必须发送字节数组
    buffer = tcpCliSock.recv(BUFSIZ)  #接收回应消息，接收到的是字节数组
    if not buffer:   #如果接收服务器信息失败，或响应消息为空
        break
    print(str(buffer,'utf-8'))   #打印回应消息
    tcpCliSock.close() #关闭客户端socket

