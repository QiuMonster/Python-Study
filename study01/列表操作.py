#查找
listA=['ABC',123,23.55,2,'qiunai',True]
print(listA)
print(listA[1:3])
print(listA*2)
for item in listA:
    print("输出每个字符的值:",item)


print("==============================")
#列表插入
print("追加前的列表为：",listA)
listA.append(['qiuiqu',False,789])  #追加列表
listA.insert(1,'lks')  #指定坐标的插入操作
print("追加后的列表为：",listA)

rsData=list(range(10))  #将数字类型转为list类型
print(rsData)
print("=============================")
#list删除操作
del listA[1]  #删除list中的第2个元素
del listA[1:3]  #删除list中的第2到3个元素  批量删除操作

listA.remove(2)  #删除指定list的中的数据  如果无指定的值时会报错
listA.pop(1)  #移除特定的值   参数是索引

print("删除list中的数据后的值：",listA)

print("=============================")
