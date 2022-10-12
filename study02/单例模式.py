#单例模式 确保只有一个类的实例存在
#如果希望一个类在系统中只出现一个实例  就使用单例模式
#创建一个单例对象  基于__new__去实现的【推荐的一种】

class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'): #判断是否存在类的实例对象
            cls._instance = super().__new__(cls, *args, **kwargs)  # 创建一个本类的实例
        return cls._instance #每次都要返回一个同一的实例对象
    pass

d=DataBaseClass()
d1=DataBaseClass()
d2=DataBaseClass()
print(id(d),id(d1),id(d2))