a=input("请输入一个值")
b=int(input("请输入一个数值"))  #进行强制类型转换为int型
d=12
c='qiumonster'
print("输入的a的值为：%s"%a)  #使用%来对a的值进行输出操作
print("输入的b的值为：{}".format(b))   #使用format函数来实现对数据值的输出


#多个值的输出操作
print("使用百分号进行多个值的输出操作:%s+%d"%(c,b))
print("使用format进行多个值的输出操作：{}+{}".format(c,b))