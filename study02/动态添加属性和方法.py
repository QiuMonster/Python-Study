import types #实现动态添加方法的库


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __str__(self):
        return "{}今年{}岁了".format(self.name,self.age)
    pass

s=Student('lks',22)
s.weight=80 #动态添加实例属性
#动态添加类的属性
Student.school='安徽大学' #类与实例对象所拥有
print(s)
print(s.weight)
print(s.school) #可以调用类中动态添加的属性
print("================================")
#动态添加实例方法
def run(self):
    print("{}正在奔跑".format(self.name))
    pass

#注意方法的名字不要重复
s.startrun=types.MethodType(run,s) #进行方法与实例对象的绑定操作
s.startrun()

print("======================================================")
@classmethod #类方法
def classTest(cls): #类方法需要类对象
    print("这是一个动态绑定的类方法")
    pass
@staticmethod
def statictest():
    print("我是动态绑定的静态方法")
    pass


#把类方法动态绑定到类中
Student.addclassTest=classTest  #将定义的类方法动态添加到类中
Student.addstaticTest=statictest #将静态方法动态添加到类中
Student.addstaticTest()
Student.addclassTest()