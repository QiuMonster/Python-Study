a=1
#变量实际上只是实现了对数据地址的引用
b=1
print(id(b))  #不会重复定义相同数值的地址
b=2
print(id(b))  #b只是将变量中的数值地址换成了2的地址而已
def func(x):
    print("x的地址为{}".format(id(x)))
    x=2
    print("x修改后的地址为{}".format(id(x)))
    print(x)
    pass

print("a的地址为{}".format(id(a)))
func(a)
print(a)

