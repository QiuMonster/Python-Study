import numpy as np
'''使用标量对象''' #默认就是int32
dt=np.dtype(np.int32)
print(dt)

'''int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替'''
dt=np.dtype('i1') # 使用字符串进行代替
print(dt)

'''字节顺序标注'''
dt=np.dtype('<i4') # i4 int32
print(dt)

'''创建结构化数据类型'''
dt=np.dtype(['age',np.int16])
print(dt)