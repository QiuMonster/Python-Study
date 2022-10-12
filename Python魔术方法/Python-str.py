class Person:
    def __init__(self):
        self.name='lks'
        self.age=23
    def __str__(self):  #魔术方法可以实现对实例对象的输出  类似与Java中的toString
        return "输出测试{}{}".format(self.name,self.age)
        pass

p=Person()  #定义一个实例对象
p.age=11
print(p)