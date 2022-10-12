import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

# 如需制作决策树，所有数据都必须是数字 将非数字数据进行转换
df = pandas.read_csv('tree_data.csv')
# Pandas 有一个 map() 方法，该方法接受字典，其中包含有关如何转换值的信息。
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)  # 将字符按照d方式进行替换
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)  # 将字符按照d方式进行替换

# 然后，我们必须将特征列与目标列分开。
# 特征列是我们尝试从中预测的列，目标列是具有我们尝试预测的值的列。
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
# print("特征:")
# print(X)
# print("目标:")
# print(y)
# print(df)

# 创建一个决策树，将其另存为图像，然后显示该图像
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)  # 构建这个决策树
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img = pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
# 我是否应该去看一个由 40 岁的美国喜剧演员主演的节目，该喜剧演员有 10 年的经验，喜剧排名为 7
print(dtree.predict([[40, 10, 7, 1]]))
# 我是否应该去看一个由 40 岁的美国喜剧演员主演的节目，该喜剧演员有 10 年的经验，喜剧排名为 6
print(dtree.predict([[40, 10, 6, 1]]))
