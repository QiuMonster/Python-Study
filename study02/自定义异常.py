class MyException(Exception):
    def __init__(self,leng):
        '''
        长度
        '''
        self.len=leng
        pass
    def __str__(self): #会自动执行str输出信息的方法
        print("调用str方法")
        return "您输入的字符串长度是"+str(self.len)+"超出长度了..."
        # if len>10:
        #     return self.len
        # else:
        #     return
    pass

def name_Test():
    name=input("请输入姓名..")
    try:
        if len(name) > 4:
            raise MyException(len(name))  # 使用raise关键字抛出异常
        else:
            print(name)  # 没有异常时输出姓名
            pass
        pass
    except MyException as msg:  #MyException自定义的异常
        print(msg) #输出自定义的异常信息
        pass



    pass

name_Test()