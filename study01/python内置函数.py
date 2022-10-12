#绝对值函数  abs(数值)
import random

print(abs(-100))
print("==========================================")

#取值函数  round(数值,精度)
print(round(8.59))  #不完全根据四舍五入来进行取值  与python的浮点数的精度有关
print(round(4.55,1))  #可以指定精度来进行取值操作
print("==========================================")

#指数运算  pow(x,y)  返回x^y   pow(x,y,z)  是先求取 x^y 后对 z 求余数

print(pow(2,3))  #2^3
print(pow(2,3,2)) #2^3%2

print("==========================================")


#求最大值  max(a,b,c,...)
print(max(1,2,3,4))


#求和运算   sum(可迭代的对象,start)  start是一个额外相加的值   列表(list)、元组(tuple)、集合(set)、字典(dictionary)
print("==========================================")
print(sum((1,2,3),10))  #默认是从0开始
print(sum([0,1,2,3,4],11))  #从第二个开始进行求和操作

listA=list({1,2})  #将set结合转为list列表
print("sum求和set集合{}".format(sum(listA,1)))  #{a,b,c..}  set集合不允许有重复元素存在
#问题  start不可以超出可迭代对象的元素范围
print("sum对dist求和{}".format(sum({1:5,2:6,3:7},1)))  #是对字典的key值进行求和操作

print("==========================================")
#执行字符串表达式  eval()  函数执行一个字符串表达式，并返表达式的值
print(eval('a+b',{'a':12,'b':11}))  #eval函数执行 a+b => 12+11  返回执行后的数据

def evaltest():
    print("这是eval函数执行函数字符串的结果")
    pass

eval('evaltest()')  #执行evaltest函数  执行函数的字符串是  函数名()

print("==========================================")
#chr(i)函数范围在range(0,256) 0-255的ASCII码对应的字符  i可以是10进制  也可以是16进制数
print(chr(random.randint(0,256)))  #随机产生一个字符

print("==========================================")
#进制转换  bin()转2进制  hex()转16进制
print(bin(10))  #10进制转2进制
print(hex(10))  #10进制转16进制

print("==========================================")
#类型转换  创建字典
dicA={'name':'lks','age':22}
print(dicA)

print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))  # 映射函数方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))    # 可迭代对象方式来构造字典
print(dict([{'one', 1}, ('two', 2), ('three', 3)]))  #可以实现
dic=dict(name='qiu',age=22)  #使用dict()函数实现字典的创建
print(dic)
print(dict([('name','qiu')]))  #dict中是一个list中存在的元组(key,value)或{key,value}

print("==========================================")
#bytes()转为字节数组  返回一个字节数组

print(bytes('中国世界'.encode('utf-8')))

print("==========================================")
#字符串转换
a=('name','age')
print(str(a))

print("==========================================")
#序列操作函数
print(all([1,2,3])) #all()函数类似与  如果元素中存在 False 0 ''(空)  会返回false 否则返回true
print(all([0,False,''])) #False
print(all([0,False,121])) #False
print(all([]))  #Ture

#any函数  元素中都为 0 False ''(空)  时返回False  否则返回True
print(any([1,2,3])) #True
print(any([1,2,''])) #True
print(any(['',0,False])) #False
print("==========================================")
#序列操作  sorted() 与sort区别  sort是在原有的函数上进行更改 应用与list上使用   sorted是返回一个排好序的可迭代对象
listB=[2,5,3,6,1]
listB.sort()
print(listB)  #对原来的列表进行操作处理

listC=[2,5,3,6,1]
print(sorted(listC)) #返回一个排好序的列表

print(sorted(['tr','ee','ds'],reverse=True))  #进行序列的降序操作
print("==========================================")
listD=[5,4,3,2,1]
listD.reverse()  #对列表中的元素进行反向输出  无返回值  在原有的列表中进行修改
print(listD)
print("==========================================")
#zip函数将元素打包成一个元组
a=list(zip([1,2,3],['name','lks','wlb']))  #进行转换一下
print(a)
print(dict(zip(['name','age'],['lks',22])))  #转为字典数据  只能是二个list 一个对应key 一个对应value
print(tuple(zip(['name','age'],['lks',22])))  #转为元组数据
print(tuple(zip(['name','age'],['lks',22],['lks',22])))  #转为元组数据
print("==========================================")
#enumerate(list数据,start)  将可迭代的对象遍历后组合成一个带有索引的元组  start是枚举的开始值
listE=['name','age','height']
print(list(enumerate(listE)))  #带有索引的list元组数据
print(list(enumerate(listE,5)))  #带有索引的list元组数据  5表示枚举的开始值
print("==========================================")
