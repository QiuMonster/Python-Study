class Person:
    country='china'
    #定义一个类的方法   实例和类都可以调用
    @classmethod
    def get_country(cls):  #cls代表本类对象  指向同一个地址空间
        return cls.country  #访问类的属性

    #定义一个静态方法 这个方法属于类
    @staticmethod
    def get_home():
        print("我是类的静态方法，实例对象不可调用")
    pass

test=lambda x,y:'你好世界' if x>y else '你不好世界'  #x,y是参数


p=Person()
print("我是通过类的实例来调用的",p.get_country())  #通过实例调用类方法
print("我是通过类名调用的",Person.get_country()) #通过类来调用类方法
Person.get_home() #静态方法
p.get_home() #可调用，但不提倡通过实例对象访问静态方法
print("===============================================")

import time
class TimeTest:
    @staticmethod
    def shwoTime():
        return time.strftime("%Y:%D:%H:%M:%S",time.localtime())
    pass

print(TimeTest.shwoTime())
print(test(1,2))

