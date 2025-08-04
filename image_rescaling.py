#不同內插法比較
import numpy as np
import cv2

img=cv2.imread("photo.jpg",0) #0:灰階模式載入
nr1,nc1=img.shape[:2]
nr2,nc2=nr1//4 ,nc1//4 #高寬縮小為原來的1/4
img1=cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_NEAREST) #Nearest影像縮小
img1=cv2.resize(img1,(nr1,nc1),interpolation=cv2.INTER_NEAREST) #放大回原大小
img2=cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_LINEAR) #Bilinear影像縮小
img2=cv2.resize(img2,(nr1,nc1),interpolation=cv2.INTER_NEAREST) #放大回原大小
img3=cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_CUBIC) #Bicubic影像縮小
img3=cv2.resize(img3,(nr1,nc1),interpolation=cv2.INTER_NEAREST) #放大回原大小
cv2.imshow("Original Image",img)
cv2.imshow("Nearest Neighbor",img1) #最近鄰
cv2.imshow("Bilinear",img2) #雙線性
cv2.imshow("Bicubic",img3) #雙三次
cv2.waitKey(0)
