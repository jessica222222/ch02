#影像縮放
import numpy as np
import cv2
img1=cv2.imread("photo.jpg",-1)

nr,nc=img1.shape[:2] #原來的長寬
scale=eval(input("Please enter scale:")) #輸入倍數
nr2=int(nr*scale) #新的長寬
nc2=int(nc*scale)
img2=cv2.resize(img1,(nr2,nc2),interpolation=cv2.INTER_LINEAR)
cv2.imshow("Original Image",img1)
cv2.imshow("Image Scaling",img2)
cv2.waitKey(0)

#內插法interpolation
#INTER_NEAREST最近鄰內插法
#INTER_LINEAR雙線性內插法(預設)
#INTER_AREA臨域像素再取樣內插法
#INTER_CUBIC雙立方內插法(4x4補點)
#INTER_LANCZOS4Lanczos內插法(8x8補點)