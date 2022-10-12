class Animal(object):  #Animal类继承一个基类Object
    def __init__(self):
        self.name='lks'
        self.age=22
        pass
    def eat(self):
        print("{}在吃东西".format(self.name))
        pass

class Cat(Animal):   #实现继承Animal对象
    pass

c=Cat()
c.eat()  #调用了父类中的方法
print()