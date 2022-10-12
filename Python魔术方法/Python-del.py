class Person:
    def __init__(self):
        self.name='lks'
        self.age=22
        pass
    #利用析构函数进行内存资源的回收
    def __del__(self):#魔术方法中销毁实例对象的方法    也叫析构方法
        print("实例对象已经被销毁了")
        pass

p=Person()
print(p.name,p.age)
input("请输入参数。。。")
del p  #主动销毁实例对象