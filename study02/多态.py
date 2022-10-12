class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("{}正在吃饭".format(self.name))
        pass
class Cat(Animal):
    def __init__(self,name):
        super(Cat, self).__init__(name)
        pass

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        pass

listA=[Dog('dog'),Cat('cat')]

for item in listA:  #多态实现对同一方法不同内容的输出
    item.eat()
    pass

d=Dog('小黑')

eval('d.eat()')  #对字符串进行处理执行相应的函数或输出相应的结果