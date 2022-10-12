import socket
import sys
import threading
#消息发送线程
class sendMessThread(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.s=s
    def run(self):
        print('发送消息线程启动')
        temp_data = 'temp:25 h:80'
        self.s.send(temp_data.encode('utf-8'))
        print('send_temp_ok')
        while True:
            dd = input()
            self.s.send(dd.encode('utf-8'))
#图片发送线程
class sendImageThread(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.s=s
    def run(self):
        print('发送图片线程启动')
        filepath = 'img/5.png'  # 输入需要传输的图片名 xxx.jpg
        fp = open(filepath, 'rb')  # 打开要传输的图片
        while True:
            data = fp.read(1024)  # 读入图片数据
            if not data:
                print('{0} send over...'.format(filepath))
                break
            self.s.send(data)  # 以二进制格式发送图片数据
class Client(threading.Thread):
    def __init__(self, ip, port): #定义构造方法
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
    def run(self):
        try:
            s = socket.socket()  # 建立连接
            s.connect((self.ip,self.port))  # 服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))
        #消息线程启动
        sendMess = sendMessThread(s)
        sendMess.start()
        while True:
            rec_data = s.recv(1024) #接收服务端数据
            msg = str(rec_data, 'gbk')
            if(msg=='server saying: ok'):
                s.send('ready_send_image'.encode('utf-8')) #图片传输标志
                #开启图片传输线程
                sendImage = sendImageThread(s)
                sendImage.start()
            else:
                print(msg)
if __name__ == '__main__':
     client =  Client('127.0.0.1',8888)
     client.start()