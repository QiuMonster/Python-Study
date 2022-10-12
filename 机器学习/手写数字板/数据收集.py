import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt

# 一些参数
batch_size = 128
epochs = 1
num_classes = 10

# 获取数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 加载mnist数据集

# 归一化，0-255不太方便神经网络进行计算，因此将范围缩小到0—1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# 改变数据形状，格式为(n_samples, vector)，将其转化为向量
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# 控制台打印输出样本数量信息
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# 样本标签转化为one-hot编码格式（one hot编码是将变量转换为机器学习算法易于利用的一种形式的过程）
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# 创建一个神经网络训练模型
model = Sequential()
# 添加一个全连接层；神经元units=512；该层使用的激活函数activation=relu；输入格式input_dim=784
model.add(Dense(units=512, activation='relu', input_dim=784))
# Dropout通过随机（概率0.2）断开神经网络之间的连接，减少每次训练时实际参与计算的模型的参数量，
# 从而减少了模型的实际容量，来防止过拟合。
model.add(Dropout(rate=0.2))
# 添加一个全连接层；神经元units=512；该层使用的激活函数activation=relu
model.add(Dense(units=512, activation='relu'))
# Dropout通过随机（概率0.2）断开神经网络之间的连接，减少每次训练时实际参与计算的模型的参数量，
# 从而减少了模型的实际容量，来防止过拟合
model.add(Dropout(rate=0.2))
# 添加一个全连接层；将最终的输出结果分成10类
model.add(Dense(num_classes, activation='softmax'))
# 在控制台输出模型参数信息
model.summary()
# 配置训练时各指标的评测标准；损失函数loss：多分类交叉熵损失函数，RMS优化器，
# 评价函数 metrics：真实值与预测值皆为int型
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
# 训练模型：batch_size：一次训练所取样本数，epochs：迭代次数，verbose：
# 进度条模式的日志展示（整数），validation_data：真实值.
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))
# 预测
n = 4  # 给出需要预测的图片数量，为了方便，只取前4张图片
print(x_test[:n])
print('/n')
predicted_number = model.predict(x_test[:n], n)
# 画图
plt.figure(figsize=(10, 3))
for i in range(n):
    plt.subplot(1, n, i + 1)
    t = x_test[i].reshape(28, 28)  # 向量需要reshape为矩阵
    plt.imshow(t, cmap='gray')  # 以灰度图显示
    plt.subplots_adjust(wspace=2)  # 调整子图间的间距，挨太紧了不好看
    # 第一个数字是真实标签，第二个数字是预测数值
    # 如果预测正确，绿色显示，否则红色显示
    # 预测结果是one-hot编码，需要转化为数字
    if y_test[i].argmax() == predicted_number[i].argmax():
        plt.title('%d,%d' % (y_test[i].argmax(), predicted_number[i].argmax()), color='green')
    else:
        plt.title('%d,%d' % (y_test[i].argmax(), predicted_number[i].argmax()), color='red')
    plt.xticks([])  # 取消x轴刻度
    plt.yticks([])
plt.show()
