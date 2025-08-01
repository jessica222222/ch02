#讀取與顯示數位影像
import numpy as np #匯入numpy套件並命名為np
import cv2

img=cv2.imread("Cinnamoroll.jpg",-1) #imread:讀取圖片 #-1:原始格式
cv2.imshow("Example",img) #imshow:建立視窗 #Example:視窗名字
cv2.waitKey(0) #等待使用者按按鍵關閉圖片視窗 #0:無限等待
cv2.destroyAllWindows() #關閉所有由cv2.imshow()開啟的視窗