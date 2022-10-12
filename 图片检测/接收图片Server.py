import threading
import socket
class SaveImg(threading.Thread):
    def __init__(self, t):
        # 将将线程作为参数进行传递使用
        threading.Thread.__init__(self)
        self.t = t

    def run(self):
        # print('发送图片线程启动')
        filepath = '1.mp4'  # 输入需要传输的图片名 xxx.jpg
        # fp = open(filepath, 'rb')  # 打开要传输的图片
        # fp = open(filepath, 'a', encoding='utf-8')
        fp = open(filepath, 'ab')
        while True:
            rec_data = self.t.recv(1024)  # 接收服务端数据
            # data = fp.read(1024)  # 读入图片数据
            # data = rec_data.decode('UTF-8')
            data = rec_data
            fp.write(data)
        fp.close()
            # if not data:
            #     print('{0} send over...'.format(filepath))
            #     break
            # self.s.send(data)  # 以二进制格式发送图片数据


class ImgServer(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self) #使用父类的构造方法 super
        self.host = host
        self.port = port

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))  # 进行绑定
        server.listen(3) #监听等待时间
        conn, addr = server.accept() #接收客户端传递的套接字
        # while True:
        #     rec_data = server.recv(1024) #接收服务端数据
        #     msg = str(rec_data, 'gbk')
        #     if(msg=='server saying: ok'):
        #         server.send('ready_send_image'.encode('utf-8')) #图片传输标志
        # 开启图片接收线程
        sendImage = SaveImg(conn)
        sendImage.start()
    # else:
    # print(msg)
if __name__=='__main__':
    server=ImgServer('127.0.0.1',8888)
    server.start()
