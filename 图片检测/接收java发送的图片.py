import socket

HOST = ''
PORT = 8888

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


def saveFile():  # 只能接收英文字母
    filepath = '1.txt'
    request = conn.recv(1024)
    # data = request.decode('UTF-8')
    data = request.decode('UTF-8')
    fp = open(filepath, 'a', encoding='utf-8')
    fp.write(data)
    fp.close()


filepath = '1.txt'
request = conn.recv(1024)
data = request #.decode('utf-8')
# print('request is:', data)
# print(type(data))
fp = open(filepath, 'a', encoding='utf-8')
fp.write(data)
fp.close()

print('Connected by:', addr)

conn.sendall(reply.encode())

conn.close()

# filepath = 'img/testjava.jpg'  # 输入需要传输的图片名 xxx.jpg
#
# fp = open(filepath, 'awb')  # 打开要传输的图片
# fp.write(data)
# print(data, "Java发送来的数据")
# self.wfile.write(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
# filepath = 'img/1.jpg'
# fp=open(filepath,'rw')
# fp.write(data.decode('utf-8'),'00.png')
