# 绘制简单的折线
# import matplotlib.pyplot as plt
#
# x_data = [1,2,3,4,5,6,7,8,12] # X轴坐标点
# y_data = [1,2,3,4,5,6,7,8,9]  # Y轴坐标点
#
# plt.plot(x_data,y_data)
# plt.show()

#1. 导入TensorFlow
import tensorflow as tf
#1.2 matplotlib
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist #2. 通过keras使用数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data() # 载入数据

#3. 显示第一张图
plt.figure()
plt.imshow(x_train[0])
# plt.imshow(y_train[0])
plt.show()
