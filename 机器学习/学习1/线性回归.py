import scipy.stats as stats
from matplotlib import pyplot as plt

'''线性回归'''
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# 执行一个方法，该方法返回线性回归的一些重要键值：
'''slope  斜率'''
'''intercept y轴交点'''
'''r 数据在线性回归中的拟合度  r 平方值的范围是 0 到 1，其中 0 表示不相关，而 1 表示 100％ 相关。'''
slope, intercept, r, p, std_err = stats.linregress(x, y)
print("斜率",slope,"y轴交点",intercept)
# 创建一个使用 slope 和 intercept 值的函数返回新值。这个新值表示相应的 x 值将在 y 轴上放置的位置：
def myfunc(x): # slope斜率 intercept y轴交点值
    return slope * x + intercept

# 通过函数运行 x 数组的每个值。这将产生一个新的数组，其中的 y 轴具有新值：
mymodel = list(map(myfunc, x))
# 绘制原始散点图
plt.scatter(x, y)
# 绘制线性回归线  plot 绘制折线图
plt.plot(x, mymodel)
plt.show()

'''使用线性回归函数预测数据'''
'''预测一辆拥有 10 年历史的汽车的速度'''
speed = myfunc(10)
print(speed)

'''糟糕的拟合度 表示数据集不适合使用线性回归'''
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(r)
print(r2_score(y,mymodel)) #输出数据的拟合度
