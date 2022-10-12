class Animal(object):  #Animal类继承一个基类Object
    def __init__(self):
        self.name='lks'
        self.age=22
        pass
    def eat(self):
        print("{}在吃东西".format(self.name))
        pass
class Pet:
    def eat(self):
        print("小宠物正在吃东西")
        pass
class Cat(Animal):   #实现继承Animal对象
    def eat(self):
        print("{}在大口大口地吃东西".format(self.name))
        pass
    def walk(self):
        print("正在走路")
    pass

class MiniCat(Cat,Animal,Pet):  #实现多继承  继承的顺序与写在括号中的顺序相同
    pass

c=MiniCat()
print(MiniCat.__mro__)  #查看类的继承顺序
c.eat()  #如果在多继承中出现同名方法  会按照继承顺序进行逐一调用 如果没有调用到方法就会报错
c.walk()  #调用了父类中的方法
print()