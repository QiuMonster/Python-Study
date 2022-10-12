# -*- coding: utf-8 -*-
import socket
import threading

# 目标地址IP/URL及端口
from past.builtins import raw_input

target_host = "127.0.0.1"
target_port = 9999
# 创建一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接主机
client.connect((target_host, target_port))


def handle_send():
    while True:
        content = raw_input()
        client.send(content)


def handle_receive():
    while True:
        response = client.recv(4096)
        print(response)


send_handler = threading.Thread(target=handle_send, args=())
send_handler.start()
receive_handler = threading.Thread(target=handle_receive, args=())
receive_handler.start()
