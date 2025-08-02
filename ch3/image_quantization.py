#量化
import numpy as np
import cv2

def image_quantization(f,bits): #bits:要量化的位元數
    g=f.copy()
    nr,nc=f.shape[:2]
    levels=2**bits #計算灰階總等級數
    interval=256/levels #計算每個灰階區間的寬度
    gray_level_interval=255/(levels-1) #每段對應的輸出灰階值間距
    table=np.zeros(256) #建立查詢表 把輸入灰階對應到量化後的輸出灰階
    for k in range(256):
        for l in range(levels):
            if k>=l*interval and k<(l+1)*interval:
                table[k]=round(l*gray_level_interval)
    for x in range(nr): #用查表法處理影像
        for y in range(nc):
            g[x,y]=np.uint8(table[f[x,y]])
    return g

def main():
    img1=cv2.imread("photo.jpg",cv2.IMREAD_GRAYSCALE) #強制轉為灰階
    img2=image_quantization(img1,1)
    cv2.imshow("Original Image",img1)
    cv2.imshow("Quantization",img2)
    cv2.waitKey(0)
    
main()