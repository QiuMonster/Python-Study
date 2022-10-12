#正则中的编译函数  将字符串变为正则匹配对象
import re
str='nihaoshijie'

a=re.compile('n')

print(a.match(str))
