
def bianli(a):
        for i in a:
            print("输出的数据为：{}".format(i),end=" ")
        pass

# range 此函数可以生成一个数据集合列表   range(开始,结束,步长)  默认步长为1   包含开始 不包含结束  [开始,结束)
c=range(0,7,2)  #容器对象
# print(c)
a=[1, 2, 3, 4, 5]
b='qiumonster'

bianli(c)
print()


def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d"%(i,j,i*j),end=' ')
            pass
        print()
        pass
jiujiu()


for item in range(1,10):
    print(item,end=' ')
    if item==5:
        break
    pass
else:
    print("就是在上面的循环中，只要是出现了break,那么else代码将不再执行")
print()


# for-else应用场景   多次失败登录后系统锁定用户账号
userName='qiu'
userPwd='123'
for i in range(3):  #从0开始
    name=input("输入你的用户名")
    pwd=input("输入你的密码")
    if name==userName and pwd==userPwd:
        print("登录成功")
        break #退出登录操作
        pass
    else:
        print("登录失败，继续登录，你还有{}此登录执行次数".format(2-i))
        pass
else:
    print("系统将锁定你的账号")