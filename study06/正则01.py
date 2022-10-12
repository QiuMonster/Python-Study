import re
str='Python is the best language in the world'

#   (.*) is (.*?) .*  进行全字段匹配

#    group(num) 函数可以获取元组中的参数

res=re.match('(.*) is (.*?) .*',str,re.I|re.M)

print(res.groups()) #以元组的形式进输出

print(res.group(1))  #打印第一个元组中的元素
print(res.group(2))