import tensorflow as tf

from tensorflow.keras import layers ,models
from tensorflow.examples.tutorials.mnist import input_data
# from tensorflow_core.examples.tutorials.mnist import input_data
#读取模型
mnist = input_data.read_data_sets('./MNIST', one_hot = False)

#创建网络
model = models.Sequential()
#第一个卷积层 28x28x1 change to 24x24x32
model.add(layers.Conv2D(32,kernel_size = [5,5],activation='relu',input_shape=(28,28,1)))
#第一个池化层层24x24x32 change to 12x12x32
model.add(layers.MaxPooling2D([2,2]))
#第二个卷积层 12x12x32 change to 8x8x64
model.add(layers.Conv2D(64,kernel_size = [5,5],activation='relu'))
#第二个池化层 8x8x64 change to 4x4x64
model.add(layers.MaxPooling2D([2,2]))
 #全连接层 4*4*64(每一个特征图4*4，共有64个)，变化成一行4*4*64，便于全连接
model.add(layers.Flatten())
#这个就是全连接层的计算 [1,4x4x64] change to [1, 1024]
model.add(layers.Dense(1024,activation = 'relu'))
model.add(layers.Dense(10, activation = 'softmax'))
# [1,1024] change to [1, 10]
model.summary()

#把最有最优算的参数
check_path = './1.hdf5'
        # period 每隔5epoch保存一次
save_model_cb = tf.keras.callbacks.ModelCheckpoint(
     check_path,save_best_only=False ,monitor='val_acc',save_weights_only=False, verbose=1, period=1)
#设置模型的优化类型
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#填充数据，总共循环10次
model.fit(mnist.train.images.reshape((55000,28,28,1)),mnist.train.labels, epochs = 2, callbacks = [save_model_cb])

#根据算的权值，计算准确率
test_loss, test_acc = model.evaluate(mnist.test.images.reshape(10000,28,28,1)
            , mnist.test.labels)
print('\n')
print('测试集的准确率：')
print("准确率: %.4f，共测试了%d张图片 " % (test_acc,len(mnist.test.images)))
