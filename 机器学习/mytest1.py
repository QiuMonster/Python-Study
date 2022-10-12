import tensorflow.compat.v1 as tf
import numpy as np
# 训练自己的数据
tf.disable_v2_behavior()
# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3
# create tensorflow struct start
Weights = tf.Variable(tf.random_uniform((1,), -1.0, 1.0))
biases = tf.Variable(tf.zeros((1,)))
y = Weights * x_data + biases
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.initialize_all_variables()
# 创建session
sess = tf.Session()
sess.run(init)
for step in range(10000):
    sess.run(train)
    if step % 500 == 0:
        print(step, sess.run(Weights), sess.run(biases), sess.run(loss))
