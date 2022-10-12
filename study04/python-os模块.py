import os #导入系统的os模块
import shutil #进行非空文件的删除
#对文件名进行更改
# os.rename('text.txt','text1.txt')

#删除文件
# os.remove('test.py')

#创建文件夹 mkdir只能创建一级目录
# os.mkdir('TestCJ')
#创建多级文件
# os.makedirs('TestPy/test/Python')

#删除文件夹 只能删除空文件夹
# os.rmdir('TestCJ')

#多级删除非空文件夹 shutil
# shutil.rmtree('TestPy')

#获取当前程序目录
# print(os.getcwd())

#路径的拼接操作
# print(os.path)
# print(os.path.join(os.getcwd(),'venv'))

#文件目录的遍历
# for item in os.listdir('./../study03'): #老版本的用法
#     print(item)
#     pass

#with会自动释放所有的资源  上下文管理对象在迭代器遍历完成后可以自动释放资源
# with os.scandir('./../study03') as  entries:
#     for entry in entries:
#         # print(type(entry))
#         print(entry)
#         pass
#     pass

basePath='./../study03'
for entry in os.listdir(basePath):
    # os.path.isfile判断是否为文件
    if os.path.isfile(os.path.join(basePath,entry)):
        print(entry)
        pass
    #判断是否为文件夹
    if os.path.isdir(os.path.join(basePath, entry)):
        print("文件夹",entry)
        pass
    pass
