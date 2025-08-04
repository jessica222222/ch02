#影像翻轉
import numpy as np
import cv2

img=cv2.imread("Cinnamoroll.jpg",-1)
img1=cv2.flip(img,0) #0:垂直
img2=cv2.flip(img,1) #負數:水平
cv2.imshow("Original Image",img)
cv2.imshow("Flip Vertically",img1)
cv2.imshow("Flip Horizontally",img2)
cv2.waitKey(0)