#顯示影像資訊
import numpy as np
import cv2

filename=input("Please enter filename:")
img=cv2.imread(filename,-1) #imread:讀取圖片 #-1:原始格式#imread:讀取圖片 #-1:原始格式
nr,nc=img.shape[:2] #分別存行數與列數
print("Number of Rows=",nr)
print("Number of Columns=",nc)
if img.ndim!=3: #img.ndim維度數 #彩色:3 #灰階:2
    print("Gray-Level Image")
else:
    print("Color Image")