# 图片检测
import sys,PIL.Image as Image

img = Image.open('img/2.png').convert('YCbCr')

w, h = img.size

data = img.getdata()

cnt = 0

for i, ycbcr in enumerate(data):

  y, cb, cr = ycbcr

  if 86 <= cb <= 117 and 140 <= cr <= 168:

    cnt += 1

print ('%s %s a porn image.'%('./2.png', 'is' if cnt > w * h * 0.3 else 'is not'))