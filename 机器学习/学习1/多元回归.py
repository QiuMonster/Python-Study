import pandas
from sklearn import linear_model

# Pandas 模块允许我们读取 csv 文件并返回一个 DataFrame 对象
df = pandas.read_csv("cars.csv")
# 然后列出独立值，并将这个变量命名为 X。
# 将相关值放入名为 y 的变量中。
X = df[['Weight', 'Volume']]
y = df['CO2']

# 在 sklearn 模块中，我们将使用 LinearRegression() 方法创建一个线性回归对象。
# 该对象有一个名为 fit() 的方法，该方法将独立值和从属值作为参数，并用描述这种关系的数据填充回归对象
regr = linear_model.LinearRegression()
regr.fit(X, y)

print("输出重量排量与释放二氧化碳的系数关系:",regr.coef_)
# 这些值告诉我们，如果重量增加 1g，则 CO2 排放量将增加 0.00755095g。
# 如果发动机尺寸（容积）增加 1 ccm，则 CO2 排放量将增加 0.00780526g。

# 预测重量为 2300kg、排量为 1300ccm 的汽车的二氧化碳排放量：
# 使用多元回归对象regr进行结果的预测
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
