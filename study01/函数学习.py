def printInfo():
    '''
    这个函数是对信息的打印  可以展示函数的功能描述
    :return:
    '''
    print("你好世界")
    pass

printInfo()

#使用默认参数   也叫缺省参数  但在调用函数时，赋值的话，函数会使用传入的参数值
def sum(a=10,b=20):
    print("a与b的和是",a+b)
    pass
sum() #结果为 30
sum(1,1)  #结果为2

def sum1(a,b=10):
    print(a+b)
    pass
sum1(10)  #10是a的  不可以写成  a=10,b的形式


