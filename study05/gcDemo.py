import sys
import psutil #获取系统的信息
import os
import gc
def showMenSize(tag):
    pid=os.getpid()  #获得进程的id
    p=psutil.Process(pid)
    info=p.memory_full_info()  #获取当前进程的信息
    memory=info.uss/1024/1024
    print('{} 内存被使用了:{}MB'.format(tag,memory))
    pass

#验证循环引用的情况
def func():
    showMenSize('初始化')
    a=[i for i in range(1000000)]  #生成10万个数据
    b=[i for i in range(1000000)]  #生成10万个数据
    a.append(b)
    b.append(a)
    showMenSize('创建列表对象a b 之后')
    # del a
    # del b
    pass

func()
gc.collect()  #手动释放内存
showMenSize('完成之后的')



#使用系统函数查看对象被引用的次数
# sys.getrefcount()
# a=[]
# del a
# print(sys.getrefcount(a))
# b=a
# print(sys.getrefcount(a))