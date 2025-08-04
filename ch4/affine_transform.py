#用控制點仿射轉換
import numpy as np
import cv2

img1=cv2.imread("Cinnamoroll.jpg",-1)
nr,nc=img1.shape[:2]
pts1=np.float32([[160,165],[240,390],[270,125]]) #原圖三個控制點
pts2=np.float32([[190,140],[190,375],[310,140]]) #新的三個控制點座標
T=cv2.getAffineTransform(pts1,pts2) #計算一個仿射轉換矩陣
img2=cv2.warpAffine(img1,T,(nc,nr)) #warpAffine:仿射轉換函數
cv2.imshow("Original Image",img1)
cv2.imshow("Affine Transform",img2)
cv2.waitKey(0)