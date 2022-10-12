class Animal(object):  #Animal类继承一个基类Object
    def __init__(self):
        self.name='lks'
        self.age=22
        pass
    def eat(self):
        print("{}在吃东西,我是说animal中的eat方法".format(self.name))
        pass

class Cat(Animal):   #实现继承Animal对象
    def walk(self):
        print("正在走路")
    pass

class MiniCat(Cat,Animal):  #实现多继承  继承的顺序与写在括号中的顺序相同
    pass

c=MiniCat()
print(MiniCat.__mro__)  #查看类的继承顺序
c.eat()  #实现了对父类的父类的方法调用
c.walk()  #调用了父类中的方法
print()