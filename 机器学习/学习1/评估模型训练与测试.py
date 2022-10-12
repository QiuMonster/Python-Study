import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
# numpy.random.seed 使用随机种子
# seed( ) 函数用于指定随机数生成时所用算法开始的整数值，如果使用相同的 seed() 值，则每次生成的随机数都相同，如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
numpy.random.seed(2)

x=numpy.random.normal(3,1,100)
y=numpy.random.normal(150,40,100)/x
plt.scatter(x, y)
plt.show()

# 训练集应该是原始数据的 80％ 的随机选择。
# 测试集应该是剩余的 20％。
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]
# plt.scatter(train_x, train_y)
# plt.show()
# plt.scatter(test_x, test_y)
# plt.show()

# 绘制多元回归方程
# 构建多项式模型
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y,4))
# 底部范围 0-6 y 的最大值是100
myline = numpy.linspace(0, 6, 100)
# 绘制散点图
plt.scatter(train_x, train_y)
# 绘制多项式回归方程
plt.plot(myline, mymodel(myline))
plt.show()

print("当前训练数据的拟合度:",r2_score(train_y,mymodel(train_x)))

'''引入测试集 进行模型测试'''
# 按照训练的规则 建一个用于测试使用的模型
testmodel=numpy.poly1d(numpy.polyfit(test_x,test_y,4))
testline=numpy.linspace(0,6,100)
plt.scatter(test_x, test_y)
plt.plot(testline,testmodel(testline))
plt.show()
print("当前测试数据的拟合度:",r2_score(test_y,mymodel(test_x)))

print("用户停留5分钟，将花费：",mymodel(5))
