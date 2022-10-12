class Person:
    # __name='lks'  #定义 一个私有属性
    # __age=22
    __hobby='唱歌'  #私有的类属性
    def __init__(self):
        self.__name='lks' #实例属性私有化
        self.__age=22
        pass

    def __str__(self):
            return '姓名：{}，年龄：{},爱好是:{}'.format(self.__name,self.__age,Person.__hobby)
    pass

class Student(Person):
    def printinfo(self):
        print(self.__name)
    pass

s=Student()
print(s)  #子类无法直接访问实例的私有属性
# print(s.printinfo())

p=Person()
# print(p.name)  #在类外部访问  无法访问类实例的私有属性
print(p)  #私有化的实例属性  可以通过内部方法传递出来使用