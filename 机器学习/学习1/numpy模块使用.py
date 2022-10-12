import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)
print("speed的平均值是:", x)

x = numpy.median(speed)  # median先对数据进行排序了
print("数据的中位数是:", x)

x = numpy.max(speed)
print("最大值:", x)

x = numpy.min(speed)
print("最小值:", x)

x = stats.mode(speed)

print("数据的众数是:", x.mode[0], "出现的次数:", x.count[0])

'''标准差计算'''
speed = [86, 87, 88, 86, 87, 85, 86]
y = numpy.mean(speed)
x = numpy.std(speed)
print("当前数据的标准差是:", x, "平均值为:", y)

speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.std(speed)
print("当前数据的标准差是:", x)

'''方差计算'''
x = numpy.var(speed)
y = numpy.std(speed)
print("当前数据的方差是:", x, "标准差是:", y)

'''百分位数'''
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x = numpy.percentile(ages, 75)
y=numpy.percentile(ages,33.4)
print("75百分位数:", x,y)

'''使用random.uniform生成大量数据'''
x=numpy.random.uniform(0.0,5.0,250)
print("生成的数据为:",x)
