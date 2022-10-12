MapA={'name':'qiuiqu','pwd':'123'}

print("======================")
#将数据添加到字典中
MapA['age']=22  #添加数据

print(MapA,type(MapA))
print("======================")
#对字典中的数进行输出操作
print(MapA['age'])   #指定输出   通过类似于数组的方式
print(MapA.get('age'))  #通过getKey的方式输出数据值

print(MapA.values())  #获取字典中的所有值
print(MapA.keys())  #获取字典中的所有键值
print(MapA.items())  #获取字典中的所有建和值

for item in MapA.items():  #对键值进行联合输出操作
    print(item)
    pass

for item in MapA.values():  #对字典中的值进行输出
    print("字典中的所有值分别为：",item)
    pass

for key,value in MapA.items():  #对键值进行分别输出
    print("key为：",key,",value为：",value)
    pass

print("======================")
#对字典进行更新操作   update函数
MapA.update({'age':123})  #对key为age的值进行更新
MapA.update({'age1':'345'})  #如果字典中不存在的jkey  就会进行字典数据的添加操作
print(MapA)

print("======================")
#进行字典的删除操作
del MapA['age']  #对key为age的值进行删除   这样del MapA.get('age1')不可删除

MapA.pop('name')  #对字典进行pop操作
print(MapA['age1'])

print(type(MapA['age1']))
print(type(MapA.get('age1')))
print(MapA)

print("======================")
# 对字典进行排序操作  按照key进行排序
sorted(MapA.items(),key=lambda d:d[0])  #d[0]表示按照key的ASCII码进行排序操作
print(MapA)
# 按照value进行排序 前提是value的类型要统一才能正常进行排序操作
sorted(MapA.items(),key=lambda d:d[1])
print(MapA)


print("======================")

