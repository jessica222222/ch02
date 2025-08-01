#顯示像素資訊
import numpy as np
import cv2

global img #全域變數

def onMouse(event,x,y,flags,param):
    x,y=y,x #OpenCV視窗xy軸定義與數位影像xy軸定義不同
    if img.ndim!=3:
        print("(x,y)=(%d,%d)"%(x,y),end=" ")
        print("Gray-Level=%3d"%img[x,y])
    else:
        print("(x,y)=(%d,%d)"%(x,y),end=" ")
        print("(R,G,B)=(%3d,%3d,%3d)"%(img[x,y,2],img[x,y,1],img[x,y,0])) #OpenCV順序是BGR

filename=input("Please enter filename:")
img=cv2.imread(filename,-1)
cv2.namedWindow(filename)
cv2.setMouseCallback(filename,onMouse) #滑鼠的Callback
cv2.imshow(filename,img)
cv2.waitKey(0)