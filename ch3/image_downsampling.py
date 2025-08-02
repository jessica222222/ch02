#下取樣
import numpy as np
import cv2

def image_downsampling(f,sampling_rate): #f:原始圖片 #sampling_rate:取樣間隔
    nr,nc=f.shape[:2]
    nr_s,nc_s=nr//sampling_rate ,nc//sampling_rate #計算降解析度後的影像尺寸
    g=np.zeros([nr_s,nc_s],dtype='uint8') #dtype='uint8':像素值範圍是0~255(灰階)
    for x in range(nr_s):
        for y in range(nc_s):
            g[x,y]=f[x*sampling_rate,y*sampling_rate] #取樣!!!
    return g

def main():
    img1=cv2.imread("photo.jpg",cv2.IMREAD_GRAYSCALE) #強制轉為灰階
    img2=image_downsampling(img1,2) #樣間隔為2
    cv2.imshow("Original Image",img1)
    cv2.imshow("Downsampling by 2",img2)
    cv2.waitKey(0)  

main()