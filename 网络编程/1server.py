

import socket

HOST = ''
PORT = 8000

reply = 'Yes'

'''
socket.socket()创建一个socket对象，
并说明socket使用的是IPv4(AF_INET，IP version 4)
和TCP协议(SOCK_STREAM)。
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(3)

conn, addr = s.accept()

request = conn.recv(1024)

print('request is:', request.decode())
print('Connected by:', addr)

conn.sendall(reply.encode())

conn.close()


