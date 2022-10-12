# openfile=open("text.txt", "w",encoding='utf-8')  # 1文件路径  2操作模式 w为写的模式 3指定编码类型
# openfile.write('lks你好呀，我也不理解自己的情感')
# openfile.close() #关闭文件 进行保存

#以二进制流的方式进行文件操作
# openfile1=open('text.txt','wb')  #解释器会将str变为bytes进行文件的传输
# openfile1.write('你在干什么能？'.encode('utf-8'))  #设置将str转为bytes的字节编码
# openfile1.close()

def myfile(url,mode,data,code):
    mfile=open(url,mode,encoding=code)
    mfile.write(data)
    mfile.close()
    pass
#以字节进行操作
def myfileb(url,mode,data,code):
    mfile=open(url,mode)
    for item in data:
        mfile.write(item.encode(code))
    mfile.close()
    pass
# data=['小胖吃屎，大口大口的吃','你好小死字']
# myfileb('text.txt','ab',data,'utf-8')


myfile('text.txt','a','小胖吃屎，大口大口的池','utf-8')

