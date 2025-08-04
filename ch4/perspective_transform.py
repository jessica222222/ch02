#透視轉換
import numpy as np
import cv2

img1=cv2.imread("Cinnamoroll.jpg",-1)
nr,nc=img1.shape[:2]
pts1=np.float32([[100,50],[400,30],[420,300],[80,320]]) #要變形的區域
pts2=np.float32([[0,0],[300,0],[300,400],[0,400]]) #對齊後的矩形區域
T=cv2.getPerspectiveTransform(pts1,pts2)
img2=cv2.warpPerspective(img1,T,(300,400))
                                #輸出影像的寬高
cv2.imshow("Original Image",img1)
cv2.imshow("PerspectiveTransform",img2)
cv2.waitKey(0)