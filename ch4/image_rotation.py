#影像旋轉
import numpy as np
import cv2

img1=cv2.imread("Cinnamoroll.jpg",-1)
nr2,nc2=img1.shape[:2]
rotation_matrix=cv2.getRotationMatrix2D((nc2/2,nr2/2),30,1)
                                       #旋轉中心點 #旋轉角度(度) #縮放比例 #1:原尺寸
#rotation_matrix會是2×3的仿射轉換矩陣
img2=cv2.warpAffine(img1,rotation_matrix,(nc2,nr2)) #應用仿射轉換
                                        #(nc2,nr2):設定輸出大小與原圖相同
cv2.imshow("Original Image",img1)
cv2.imshow("Image Rotation",img2)
cv2.waitKey(0)
