#opencv繪圖
import numpy as np
import cv2

img=np.zeros([400,500,3],dtype='uint8') #定義數位影像
text="Hello World"
fontFace=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,text,(10,50),fontFace,1.0,(255,255,255))
          #影像 #字串 #左下座標 #字體  #大小  #顏色
fontFace=cv2.FONT_HERSHEY_PLAIN
cv2.putText(img,text,(10,90),fontFace,1.0,(255,255,255))

fontFace=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,text,(10,130),fontFace,1.0,(255,255,255))

fontFace=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text,(10,170),fontFace,1.0,(255,255,255))

fontFace=cv2.FONT_HERSHEY_TRIPLEX #COMPLEX加粗版
cv2.putText(img,text,(10,210),fontFace,1.0,(255,255,255))

fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img,text,(10,250),fontFace,1.0,(255,255,255))

fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX #手寫字體
cv2.putText(img,text,(10,290),fontFace,1.0,(255,255,255))

fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img,text,(10,330),fontFace,1.0,(255,255,255))

cv2.imshow("Example",img)
cv2.waitKey(0)