class Person:
    def test(self):
        self.__test1() #通过普通的方法调用类中的私有方法
    def __test1(self):  #我是私有的方法
        print("我是私有的方法，不可在本类的外部直接调用")
        pass


p=Person()
p.test()