#使用tell返回当前指针所在的位置
def open_f():
    with open('text.txt', 'r', encoding='utf-8') as open_f:
        content = open_f.read(3)
        print(content)
        print("光标当前所在的位置", open_f.tell())  # 在utf编码中中文是3个字节  英文是1个字节  #在gbk编码中中文是2个字节 英文为1字节
        print(open_f.read(2))
        print("光标当前所在的位置", open_f.tell())
        pass
    pass



#使用seek来调整光标的位置
with open('text.txt','r',encoding='gbk') as open_f1:
    open_f1.seek(2,0)  #光标从开头开始  向后移动2个字节的位置
    # open_f1.seek(2,1)  #光标在当前位置  向后进行移动
    # open_f1.seek(-2,2)   #光标在末尾 向前移动
    print("当前的光标的位置为",open_f1.tell())  #光标的位置为2
    print(open_f1.read())
    pass

