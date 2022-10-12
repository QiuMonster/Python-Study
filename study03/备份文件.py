#文件的备份
# def copyfile():
#     #接收用户输入的文件名
#     old_file=input("请输入要备份的文件名")
#     file_list=old_file.split('.') #将文件路径和文件后缀分隔开来
#     #构造新的文件名
#     new_file=file_list[0]+'_备份.'+file_list[1] #新的文件名称
#     #读取旧的文件  写到新的文件中
#     old_f=open(old_file,'r',encoding='utf-8')  #打开需要备份的文件
#     new_f=open(new_file,'w',encoding='utf-8') #打开新的文件  文件不存在  就自动创建
#     content=old_f.read() #读取全部的文件数据
#     new_f.write(content) #将数据写到文件中
#     old_f.close()
#     new_f.close()
#     pass

#处理大文件数据的复制工作
def copyBigFile():
    #接收用户输入的文件名
    old_file=input("请输入要备份的文件名")
    file_list=old_file.split('.') #将文件路径和文件后缀分隔开来
    #构造新的文件名
    new_file=file_list[0]+'_备份.'+file_list[1] #新的文件名称
    try:
        #执行监视的逻辑功能
        with open(old_file,'r',encoding='utf-8') as old_f,\
                open(new_file,'w',encoding='utf-8') as new_f:
            while True:
                content = old_f.read(1024)  # 限制每次读取的文件大小
                new_f.write(content)
                if len(content)<1024: #当读取的字节大小小于1024时 表示文件读取结束
                    break
    except Exception as msg:
        print(msg)  #输出可能出现的异常信息
    pass

#处理图片文件
def copyBigImgFile():
    #接收用户输入的文件名
    old_file=input("请输入要备份的文件名")
    file_list=old_file.split('.') #将文件路径和文件后缀分隔开来
    #构造新的文件名
    new_file=file_list[0]+'_备份.'+file_list[1] #新的文件名称
    try:
        #执行监视的逻辑功能
        with open(old_file,'rb') as old_f,\
                open(new_file,'wb') as new_f:
            while True:
                content = old_f.read(1024)  # 限制每次读取的文件大小
                new_f.write(content)
                if len(content)<1024: #当读取的字节大小小于1024时 表示文件读取结束
                    break
    except Exception as msg:
        print(msg)  #输出可能出现的异常信息
    pass
copyBigImgFile()
