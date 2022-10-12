class Person:
    #由双下滑线的方法叫做魔术方法  是python中内置的方法
    def __init__(self,name,age,sex): #进行初始化操作  进行统一的赋值  类似与Java中的构造器
        self.name=name #实例属性
        self.age=age
        self.sex=sex
        pass

    def eat(self,sex): #第一个参数是默认参数  #传参使用
        '''
        吃的行为
        :return:
        '''
        print("{}{}喜欢吃榴莲".format(self.name,sex))  #使用实例属性
    pass

xq=Person('lks',22,'女')  #使用init初始化参数
# xq.name='lks' #添加实例属性
# xq.age=22
xq.eat('女')
print(xq.name,xq.age,xq.sex)