import matplotlib.pyplot as plt
import numpy
x=numpy.random.uniform(0.0,5.0,250) #1 最小值 2 最大值 3 数据个数
plt.hist(x,5)
plt.show()

x=numpy.random.uniform(0.0,5.0,100000)
plt.hist(x,1000)  #数据分为1000栏
plt.show()

'''典型正太分布数据'''
x = numpy.random.normal(5.0, 1.0, 100000) #1 平均值 2 标准差 3 数据个数
plt.hist(x, 100)
plt.show()

'''散点图绘制''' #汽车似乎越新，驾驶速度就越快，但这可能是一个巧合，毕竟我们只注册了 13 辆汽车。
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()

'''随机数据的散点图绘制'''
x=numpy.random.normal(5.0,1.0,1000)
y=numpy.random.normal(10.0,2.0,1000)
plt.scatter(x,y)
plt.show()

