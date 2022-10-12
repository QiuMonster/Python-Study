from PIL import Image
import numpy as np
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in = r'C:\Users\lenovo\Desktop\新建文件夹 (3)\4.jpg'
    width = 28
    height = 28
    file_out = r'C:\Users\lenovo\Desktop\新建文件夹 (3)\4_1.jpg'
    produceImage(file_in, width, height, file_out)
    # 把图像转化为黑白的
    im = Image.open(r'C:\Users\lenovo\Desktop\新建文件夹 (3)\4_1.jpg')
    L = im.convert("L")
    L.save(r'C:\Users\lenovo\Desktop\新建文件夹 (3)\4_2.jpg')
