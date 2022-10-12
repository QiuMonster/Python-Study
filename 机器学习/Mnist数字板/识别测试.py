import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from PIL import Image
import numpy as np

mnist = input_data.read_data_sets('D:\Program Files (x86)\ANACONDA\Minist_data', one_hot = False)

im_4 = Image.open(r'C:\Users\lenovo\Desktop\新建文件夹 (3)\4_2.jpg')
im_4 = np.reshape(im_4, [1,28,28,1])
im_5 = Image.open(r'C:\Users\lenovo\Desktop\新建文件夹 (3)\5_1.jpg')
im_5 = np.reshape(im_5, [1,28,28,1])
#因为我们5背景是白的，数字是黑的
#我们训练的时候，数字是白的，背景是黑的，所以需要转换
im_5 = 255 - im_5
#调用模型
new_model =tf.keras.models.load_model('D:/研究生资料/tensorflow/tf_cnn_model/cp.hdf5')
#进行预测
pe_4 = new_model.predict(im_4)
pe_5 = new_model.predict(im_5)
#把最大的坐标找到，因为new_model.predict返回的是[0,0,1,0,0,0,0,0,0,0]这种格式，
#所以需要转换为我们熟悉的格式
pe_4 = tf.argmax(pe_4 ,1)
pe_5 = tf.argmax(pe_5 ,1)

with tf.Session() as sess:
    print(sess.run(pe_4))
    print(sess.run(pe_5))
