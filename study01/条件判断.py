import random

def check(a):
    if a <= 100 and a >= 0:
        a = a
        pass
    if a >= 60 and a < 70:
        print("恭喜你及格了，下次继续加油")
        pass  # 空的代码指令
    elif a >= 80 and a < 90:
        print("你成绩已经很好了")
        pass
    elif a >= 90 and a <= 100:
        print("你成绩达到了顶级水平")
        pass
    else:
        print("没有及格，下次更要继续努力")
        pass


# a=int(input("请输入学生的成绩"))
b=random.randint(0,100)  #生成一个从0到100的随机数

print(b)


check(b)
