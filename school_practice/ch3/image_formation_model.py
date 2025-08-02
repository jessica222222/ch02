#影像形成模型
import numpy as np
import cv2

def image_formation_model(f,x0,y0,sigma): #f:原始影像 #x0y0:光源中心座標 #光照擴散程度(值越大越柔和)
    g=f.copy() #copy():複製影像 避免修改原圖
    nr,nc=f.shape[:2] #取得影像的高和寬
    illumination=np.zeros([nr,nc],dtype='float32') #建立一個與影像大小相同的2D陣列 儲存每個像素點的光照強度 初始值為0
    for x in range(nr):
        for y in range(nc):
            illumination[x,y]=np.exp(-((x-x0)**2+(y-y0)**2)/(2*sigma*sigma)) #用2D高斯分布計算每個像素的光照強度
    for x in range(nr):
        for y in range(nc):
            for k in range(3): #通道(k=0,1,2對應BGR)
                val=round(illumination[x,y]*f[x,y,k]) #round():四捨五入
                g[x,y,k]=np.uint8(val) #np.uint8():值在[0,255] 
    return g #回傳調整後的影像

def main():
    img=cv2.imread("night.jpg",-1) #-1:讀入完整資料
    nr,nc=img.shape[:2] #取得影像的高和寬
    x0=nr//2
    y0=nc//2
    sigma=100
    img2=image_formation_model(img,x0,y0,sigma)
    cv2.imshow("Original Image",img)
    cv2.imshow("Image Formation Model",img2)
    cv2.waitKey(0)
    
main()