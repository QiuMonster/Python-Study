import cv2
import numpy as np
image = cv2.imread('img/justin.png')
cv2.imwrite('img/justin1.png',cv2.Canny(image,200,300))
# cv2.imshow('edges', cv2.imread('img/justin1.png'))