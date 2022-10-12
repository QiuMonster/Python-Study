class Person:
    def __init__(self):
        self.__name = 'lks'  # 实例属性私有化
        self.__age = 22
        pass
    #使用装饰器 即在方法上使用装饰器 来实现对私有属性的赋值与获取
    @property  #使用获取的装饰器  提供一个getter方法
    def name(self):
        return self.__name
    @name.setter  #使用setter实现对私有属性的赋值
    def name(self,name):
        self.__name=name


    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
        pass
    #定义一个类属性  实现通过直接访问属性的形式去访问私有属性
    age=property(get_age,set_age)  #将类属性与类中的操作实例私有属性的方法结合
    pass

p=Person()
p.age=12 #直接给私有属性进行赋值操作
print(p.age)  #直接输出私有属性值
p.name='qiuqiu' #直接赋值
print(p.name)
# p.set_age('qiu')
# print(p.get_age())
