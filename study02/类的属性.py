class Person:
    name='lks'  #属于类的属性
    def __init__(self,age):
        self.age=age  #age属于实例属性
        pass

p=Person(22)  #p为Person的实例  可以使用类的属性name和实例属性age
print(p.name,p.age)
print(Person.name)  #类名使用类的属性  #后期可以写成类的配置参数
# print(Person.age)  #实例属性不属于类的
