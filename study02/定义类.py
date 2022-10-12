class Person:
    name='qiu'  #定义了类属性
    age=22

    def __init__(self):
        self.name='lks'  #通过self关键字定义的  为  实例属性  属性为实例对象所属
        pass

    #没有self关键字时，就不是实例方法
    def eat(self):  #我是实例方法  self只是一个关键字   关键字可以不是self
        print("你好",self.name)  #self.name代表实例属性
        pass

    def eat1(para): #实例方法
        print("你好",para.name)
        pass


p=Person()  #对象的创建
# p.name='lks' #赋值操作

print(p.name)

p.eat()