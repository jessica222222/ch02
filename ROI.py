#擷取ROI影像
import numpy as np
import cv2

filename=input("Please enter filename:")
ROI_x,ROI_y=eval(input("Enter(x,y)for ROI:")) #要擷取位置的左上角座標
ROI_nr,ROI_nc=eval(input("Enter(rows,columns)for ROI:")) #ROI的行數列數
img=cv2.imread(filename,-1)
ROI=img[ROI_x:ROI_x+ROI_nr,ROI_y:ROI_y+ROI_nc]#將擷取的東西存在ROI
cv2.imwrite("Cinnamoroll_01.jpg",ROI)