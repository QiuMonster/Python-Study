try:
    # print(b)
    # print(a)
    listA=[1,2,3]
    print(listA[5])
    pass
# except SyntaxError as msg:
#     print(msg,"编译错误")
#     pass
except NameError as msg: #NameError是错误的类型
    #进行错误的处理操作  上面的try中代码出现错误时，会执行except中的代码
    print("出错了")
    print(msg) #将错误信息显示出来
    pass
except IndexError as msg: #可以写多个错误处理 程序
    print(msg)
    pass
except Exception as result:  #Exception捕获一般的异常
    print(result)  #输出全部的错误信息
    pass
else:
    print("我是没有异常的时候才会调用")
    #在try代码块中不存在异常时 此else中的代码调用
    pass
finally:
    print("无论如何我最后都会执行")


# print(dir(Exception))
# except  需要具体的错误类型来处理

# if __name__=='__main__':  #使用main函数
#     print("数的撒大")