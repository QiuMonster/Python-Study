# import time #导入模块  #如果有同名文件  会找到自己写的文件代码
# print(time.ctime())  #对当前时间进行输出操作
#import 导入模块的时候  会进行如下操作
# 1.打开文件模块
# 2.会执行模块对应的文件，将执行过程中产生的名字都丢到模块的名称空间
# 3.在程序中会有一个模块的名称指向模块的名称空间去

import time as mytime  #给系统中的模块定义别名
print(mytime.ctime())  #通过别名进行函数调用

from time import time,ctime  #从time模块中导入time和ctime模块
print(ctime())  #执行导入的模块方法
print("输出当前的时间戳",time())
#from ... import 首次导入发生的3个步骤
#1 以模块为准创造一个模块的名称空间
#2 会执行模块对应的文件，将执行过程中产生的名字都丢到模块的名称空间
#3在当前执行文件的名称中间中拿到一个名字，该名字直接指向模块的某一名字