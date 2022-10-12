#循环实现阶乘
def jiecheng1(n):
    sum=n
    while n>1: #退出循环条件
       n-=1
       sum=sum*n
       pass
    return sum  #将阶乘的数值返回给函数
print(jiecheng1(2))

def jiecheng2(n):
    result=1
    for item in range(1,n+1):  #取数从1到n
        result*=item
        pass
    return result

print(jiecheng2(3))

#递归实现

def jiecheng(n):
    if n==1:
        return n  #函数的出口
    else:
        return n*jiecheng(n-1)
    pass

print(jiecheng(5))


#对系统的文件进行访问操作
import os  #引入文件操作模块
def findFile(file_Path):
    listRs=os.listdir(file_Path)  #获得改路径下的所有文件夹
    print("所有的文件夹:{}".format(listRs))
    for item in listRs:  #对文件夹进行遍历操作
        fullpath=os.path.join(file_Path,item) #获取到文件的绝对路径
        # print(fullpath)
        if os.path.isdir(fullpath): #如果路径是一个文件夹  继续进行递归调用
            # print("存在文件夹")
            findFile(fullpath)  #递归文件夹时需要绝对路径
        else: #是文件类型
            print(item)
            pass
        pass
    else:
        return #结束后进行返回
    pass

findFile('D:\\QiuStudio\\MDStudio')  #二个\\是为了转义

# print(os.path.isdir('D:\\QiuStudio'))



