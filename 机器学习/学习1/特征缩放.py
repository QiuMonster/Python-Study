# 特征缩放（Scale Features）
# 当您的数据拥有不同的值，甚至使用不同的度量单位时，可能很难比较它们。与米相比，公斤是多少？或者海拔比较时间呢？
# 这个问题的答案是缩放。我们可以将数据缩放为易于比较的新值。
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

'''使用特征缩放进行值的预测'''
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

# 将两个无关的值进行适配缩放
scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

print(scaled)
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
