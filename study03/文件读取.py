def readfile(url,mode,code,exception):
    read=open(url,mode,encoding=code)
    print(eval(exception)) #使用字符串解析后执行相应功能
    read.close()
    pass

# readfile('text.txt','r','utf-8','read.read()')
# readfile('text.txt','r','utf-8','read.read(4)')  #读取固定个数的文件数据
# readfile('text.txt','r','utf-8','read.readline()') #实现读取一行数据
# readfile('text.txt','r','utf-8','read.readlines(3)') #实现读取固定行的数据

#以二进制的模式进行读取
def readfileb(url,mode,exception,code):
    with open(url,mode) as read:  #使用with句柄来实现自动释放为文件对象
        data = eval(exception)  # 将二进制赋给data
        # 将data进行解码
        print(data.decode(code))  # 进行数据的解码操作
        # read.close()
    pass

readfileb('text.txt','rb','read.read()','utf-8') #实现读取固定行的数据

