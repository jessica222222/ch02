import numpy as np
x=np.array([1,2,3,4])
y=np.array([4,3,2,1])
print(x+y)
print(x*y)

img=np.zeros([512,512],dtype="uint8")
print(img)

z=np.array([1,2,3,4,5,6,7,8,9])
print(np.mean(z))
print(np.std(z))