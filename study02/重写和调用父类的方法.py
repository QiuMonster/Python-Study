class Animal(object):  #Animal类继承一个基类Object
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def eat(self):
        print("{}在吃东西,我是说animal中的eat方法".format(self.name))
        pass

class Cat(Animal):   #实现继承Animal对象
    def __init__(self,name,age):  #自己的属性sex
        super(Cat,self).__init__(name,age)  #使用父类的属性在父类的init方法中进行赋值操作
        super().__init__(name,age)  #简化的调用父类的方法
        pass
    def eat(self):
        # super(Cat, self).eat()  #将本类对象作为参数注入方法中
        super().eat()  #将本类对象作为参数注入方法中

    def walk(self):
        print("正在走路")
    pass

c=Cat('lks',10)
print(c.age,c.name)
c.eat()

