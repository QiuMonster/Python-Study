# 多项式回归
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# NumPy 有一种方法可以让我们建立多项式模型
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# 然后指定行的显示方式，我们从位置 1 开始，到位置 22 结束 y 的最大值是100
myline = numpy.linspace(1, 22, 100)
# print(myline)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline)) # 绘制线性回归方程
plt.show()

'''Python 和 Sklearn 模块将为您计算该值，您所要做的就是将 x 和 y 数组输入：'''

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print("当前数据的拟合度:",r2_score(y, mymodel(x))) # 输出多项式中的数据拟合度

'''预测下午 17 点过车的速度'''
speed = mymodel(17)
print("下午 17 点过车的速度",speed)


'''极为糟糕拟合度的数据'''
import numpy
import matplotlib.pyplot as plt
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
print(r2_score(y,mymodel(x)))