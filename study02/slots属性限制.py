#slots属性限制是用于限制动态添加属性或方法的
class Student(object):
    __slots__ = ('name','age')  #元组类型  只允许动态添加的属性 #定义时不存在__dict__了，属性字典不存在了
    def __str__(self):
        return "{}。。。{}".format(self.name,self.age)
    pass

s=Student()
s.name='lks'
s.age=22
# s.score=96
#此方法可以查看实例对象中的全部属性信息  前提是没有设置__slots__属性限制属性的范围

# print(s.__dict__) #以字典类型进行显示  不足的是占用空间大

print(s)

#在继承关系中__slots__的属性限制关系是不存在的
#子类可以随意设置属性
class subStudent(Student):
    __slots__ = ('pro') #在父类中限制的属性进行限制属性的追加限制属性
    def __init__(self):
        super(subStudent, self).__init__()
        pass

    # def __str__(self):
    #     return super(subStudent, self).__str__()
    pass

sub1=subStudent()
sub1.pro='lkjs'
sub1.name='lks'
sub1.age=12
print(sub1)
