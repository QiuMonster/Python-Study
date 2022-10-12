#python中的匿名函数是通过lambda表达式实现的
#没有函数名字
#匿名函数冒号后面的表达式只有一个  注意只是一个表达式 不是程序语句
#匿名函数只能实现简单的逻辑功能  可以有三元表达式  a if 条件 else b  条件成立 结果为a  否则结果为b

# lambda 参数:语句

c=lambda a,b:a*b

sum=(lambda a,b:a*b)(12,10)  #自动实现调用的lambda的表达式

print(sum)

print(c(19,2))

change=lambda score:'成绩可以，你可以取参军' if score>80 else '你只能回家修地球'

print(change(99))
print(change(0))