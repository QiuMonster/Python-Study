import re
#匹配数字  限定匹配的数量

num='11112223333'
a=re.compile('\d{4,6}')  # 尽量多匹配数字
b=re.compile('\d{4,6}?')   #非贪婪模式  尽量少匹配数字

print(a.match(num))
print(b.match(num))
print(re.match('\d{2,5}',num).group())