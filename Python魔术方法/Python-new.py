class Person:
    #new魔术方法是静态方法  是属于类的
    def __new__(cls, *args, **kwargs): #创建对象的魔术方法
        print("开始进行对象的创建")
        return object.__new__(cls)  #手动创建对象实例
        pass

    def __init__(self):  #创建完对象后才能进行数据的初始化工作
        print("开始进行数据的初始化工作")
        pass

p=Person()  #1先进行实例的创建  2进行数据的初始化


