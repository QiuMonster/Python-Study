#  . 正则中点的使用  规则是匹配除换行符之外的字符
import re
str='Python is the best language in the world'
res=re.match('P..',str)  #输出 Py 字符串
print(res.group())
print("======================================")
names='李达','李明','小王','小李'
pattern='李.'  #匹配的规则
for name in names:
    res = re.match(pattern, name)
    if res:
        print(res.group())
        pass
    else:
        pass
    pass



