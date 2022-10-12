tupleA=('abc',123,3.45,'apple',[1,2,3])  #定义一个元组
#元组查询
index=tupleA.index('abc')
print("abc所在的下标是",index)
print(tupleA[::-1])  #反向输出   负号表示反向  1表示步长
print(tupleA[-2::-3])  #步长为3
#  list正向 是0 到 len-1  反向 是-len 到 -1
print(tupleA[-3:])

print("=======================")
#元组不支持赋值操作  只能初始化赋值
# tupleA[0]='wewe'   TypeError: 'tuple' object does not support item assignment

#当元组中只有一个元素时要加上  ,  tupleA=(123,) 这样才能正常显示tupleA为元组类型

#给元组中的列表赋值
tupleA[4][0]=12345
print(tupleA[4][0])


print("=======================")
#使用元组的  count函数对元组中出现相同的元素进行计数操作
tupleB=tuple(range(1,10))
print(tupleB)
print(tupleB.count(8)) #对元组中的8袁术进行计数操作
