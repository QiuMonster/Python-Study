import re
#限定匹配字符数量的规则
#   *是匹配前一个字符出现0次或无限次   返回的是匹配的前一个字符的所有的字符
str='nnihaoshijieoo'
print(re.match('n*',str).group())  #  输出为 nn