#   [a,b,c]  匹配列表中的任意字符
#  [a-z]  匹配a到z中的任意一个字符
import re
str='hello'
#匹配  hel中的任意一个字符
#找到一个就直接返回
#匹配模式为  被匹配的字符串一个一个与匹配串中放入所欲字符进行匹配返回
print(re.match('[thel]',str).group())