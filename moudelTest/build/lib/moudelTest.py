#定义一个模块

#限制别的程序使用本模块中的方法
# #通过  from 本模块 import * 方法  导入魔术变量__all__中的方法
__all__=['add','diff']

#普通的函数
def add(x,y):
    return x+y
def diff(x,y):
    return x-y
def printinfor():
    return "这是我自定模块的方法"

#测试   __name__这是魔术变量
if __name__=='__main__':
    print("模块名__name__为%s" % __name__)