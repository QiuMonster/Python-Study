#可变参数   当参数个数不确定时使用  比较灵活
def getComputer(*args):
    #接收一个元组类型的数据
    print(type(args))
    print(args) #元组类型
    for item in args:
        print(item)
        pass
    pass


a=(1,2,3,4)
getComputer(1)
getComputer(a)


#关键字可变参数  用  **来定义
#在函数体内   参数的关键字是一个字典类型 key是一个字符串
def keyFunc(**kwargs):
    print(type(kwargs))
    print(kwargs)
    pass


dictaA={'name':'qiu','age':22}
#传递字典类型参数时  要写成  **字典类型参数
keyFunc(**dictaA)  #**只能接收字典类型的参数

#使用这样的方式来实现对字典参数的传递
keyFunc(name='qiu',age=22)


#复合参数的顺序必须是  元组类型  字典类型
def complexFunc(*args,**kwargs):
    print(args)
    print(kwargs)
    pass


complexFunc(1,23,4)   #赋值给元组类型参数
complexFunc(name='qiu',age='22')   #赋值给字典类型参数
complexFunc(1,23,4,name='qiu',age='22')  #解决了java中可变参数的限制  只能将可变参数放到形参的最后面
# complexFunc(name='qiu',age='22',1,23,4)   #参数类型的位置不可变化  编译器直接报错
