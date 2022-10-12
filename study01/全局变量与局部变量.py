

A=10
b=12
#当全局变量和局部变量同时重复定义时，函数优先使用局部定义的变量(地头蛇)
def sum(a,b):
    sum=a+b
    global A  #global关键字可以实现函数内对全局变量进行修
    A=11
    return sum

print(sum(A,b))
print(A)