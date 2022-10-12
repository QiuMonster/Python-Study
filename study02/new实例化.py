class Animal:
    def __init__(self):
        self.color='虹色'
        pass

    #在python当中如果不重写new方法时
    #默认解释器自动执行创建类的实例代码
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    pass

a=Animal()  #解释器会自动调用new方法  来实现对实例的创建工作  将实例返回给init来进行数据的初始化
#在新式类中new才是实例化的方法，然后调用该框架的构造方法