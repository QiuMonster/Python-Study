#共有的方法  +   *   in
StrA='人生苦短'
StrB='我用Pyhton'
print(StrA+StrB)  #使用+拼接  字符 列表  元组 字典

listA=list(range(10))
listB=list(range(11,20))
print(listA+listB)  #实现对列表的拼接操作

print(listA*2)  #进行数据的复制操作     数据*num   数据会被复制num倍

print("================================")
#in判断对象是否存在
listC=[1,2,3,4,5,6]  #定义一个列表
print(1 in listC)  #判断数据是否在一个列表中

dictA={'name':'qiunai'}
print("name" in dictA)  #判断name是否在字典中  只能判断键值
print('qiunai' in dictA.values())  #可以实现对value的判断
print('qiunai' in dictA)
