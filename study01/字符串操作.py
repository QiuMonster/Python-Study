Test='qiumonster'
print(Test[0])
#实现字符串首字母大写
DTest=Test.capitalize();  #首字母大写函数
print(DTest)


print("=================================")
#出去字符串中的空格
a='     hello      '
print(a)
print(a.strip())  #出去字符串的空格
print(a.lstrip());  #出去字符串左侧空格
print(a.rstrip());  #出去字符串右侧空格

print("=================================")
#复制字符串
b=a  #进行字符串复制时  变量名共同指向值的地址(公用一个地址空间)
print("a的内存地址是%d"%id(a))
print("b的内存地址是%d"%id(b))

print("=================================")
#字符串的查找操作
dataStr='I love lks almosttime'
print(dataStr.find('o'))  #find()返回的是目标字符所在的下标  没有时返回 -1
print(dataStr.find('A'))
print(dataStr.index('s'))  #index()也是返回下标  但是在未找到字符时 会报错

print("=================================")
#判断字符以什么开头  以什么结尾  返回值时bool类型
dataStr1='I aplep you'
print(dataStr1.startswith('I'))  #以什么开头
print(dataStr.endswith('d')) #以什么结尾

print("=================================")
#字符串大小写转换
strtr='i love apple'
str1='I LOVE LKS'
print(strtr.upper())  #字符串变大写
print(str1.lower())  #字符串变小写

print("=================================")
strMsg='hello world'
#对字符串进行切片处理   可以把字符串看成一个列表(数组)
print(strMsg[:3])  #元素从1到3输出字符
print(strMsg[4:])  #元素从5到最后的元素输出字符
print(strMsg[1:4])  #元素从2到4输出字符   数组从1到3
print(strMsg[::-1])  #反向打印输出字符



