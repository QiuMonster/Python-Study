#引入正则表达式模块
import re
a='你好世界'


#使用  match函数来匹配字符串  返回匹配的字符串  match从字符串的开始位置进行匹配操作
result=re.match('你',a,re.I|re.M)  #默认是精确匹配  这个模式只能匹配以什么字符来开头  你  你好  你好世
#     re.I表示忽略大小写  re.M表示多行匹配

if result:
    print("匹配成功")
    pass


print(result)  #参1是匹配的字符串  a是被匹配的字符串
print(result.group())  #使用group来取出匹配成功的字符串