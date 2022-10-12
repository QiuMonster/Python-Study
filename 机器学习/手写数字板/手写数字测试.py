import tensorflow as tf
from tensorflow_core.examples.tutorials.mnist import input_data
# from tensorflow.examples.tutorials.mnist import input_data
from PIL import Image
import numpy as np


def produceImage(file_in, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((28, 28), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in1 = './number/1.png'
    file_in2 = './number/2.png'
    file_in5 = './number/5.png'
    file_out1 = './number/1_1.png'
    file_out2 = './number/2_1.png'
    file_out5 = './number/5_1.png'
    produceImage(file_in1, file_out1)
    produceImage(file_in2, file_out2)
    produceImage(file_in5, file_out5)
    im1 = Image.open('./number/1_1.png')
    im2 = Image.open('./number/2_1.png')
    im5 = Image.open('./number/5_1.png')
    L1 = im1.convert("L")
    L2 = im2.convert("L")
    L5 = im5.convert("L")
    L1.save('./number/1_2.png')
    L2.save('./number/2_2.png')
    L5.save('./number/5_2.png')

mnist = input_data.read_data_sets("MNIST/", one_hot=False)
im_1 = Image.open('./number/1_2.png')
im_1 = np.reshape(im_1, [1, 28, 28, 1])
im_2 = Image.open('./number/2_2.png')
im_2 = np.reshape(im_2, [1, 28, 28, 1])
im_5 = Image.open('./number/5_2.png')
im_5 = np.reshape(im_5, [1, 28, 28, 1])
# 调用模型
new_model = tf.keras.models.load_model('./1.hdf5')
# 进行预测
pe_1 = new_model.predict(im_1)
pe_2 = new_model.predict(im_2)
pe_5 = new_model.predict(im_5)
# 把最大的坐标找到，因为new_model.predict返回的是[0,0,1,0,0,0,0,0,0,0]这种格式，
# 所以需要转换为张量的格式
pe_1 = tf.argmax(pe_1, 1)
pe_2 = tf.argmax(pe_2, 1)
pe_5 = tf.argmax(pe_5, 1)
print(pe_1)
print(pe_2)
print(pe_5)