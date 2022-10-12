class Person:
    def getNum(self):
        return 1
    def getSelf(self):  #self是调用他的实例对象的引用  与实例对象指向同一个地址空间
        print("输出self的地址%d"%(id(self)))
        pass

p=Person()
q=Person()
print("p的地址是%d"%id(p))
print("q的地址是%d"%id(q))
p.getSelf()