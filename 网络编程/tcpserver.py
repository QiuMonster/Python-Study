# -*- coding: utf-8 -*-
import socket
import threading
# 监听的IP及端口
from past.builtins import raw_input

bind_ip = "127.0.0.1"
bind_port = 9999
# socket 服务器初始化
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# 定义函数handle_client,输入参数client_socket
def handle_client():
    while True:
        request = client_socket.recv(1024)
        print("[*] Received:%s" % request)


def handle_send():
    while True:
        content = raw_input()
        client_socket.send(content);


# 阻塞在这里，等待接收客户端的数据
client_socket, addr = server.accept()
print("[*] Accept connection from:%s:%d" % (addr[0], addr[1]))
# 创建一个线程
client_handler = threading.Thread(target=handle_client, args=())
client_handler.start()
send_handler = threading.Thread(target=handle_send, args=())
send_handler.start()
