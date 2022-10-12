import numpy as np

'''创建一个ndarray'''
# 一维度数组
x = np.array([1, 2, 3, 4])
print(x)
# 两维度数组
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
print(x[1, 1:])
# 三维数组
x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x)
print(x[0, 1])  # 输出三维数组中第一个二维数组 [3,4]
print(x[0, 1, 1])  # 4

'''最小维度 ndmin 表示这是一个二维数组'''
x = np.array([1, 2, 3, 4], ndmin=2)
print(x)  # [[1 2 3 4]]

'''dtype参数 表示数组的数据类型'''
a = np.array([1 , 2,  3], dtype = complex) #表示复数的数据类型
print (a)