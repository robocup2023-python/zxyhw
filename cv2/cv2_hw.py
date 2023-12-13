import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
img=cv2.imread('img',0)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
cv2.convertScaleAbs(sobelx)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.convertScaleAbs(sobely)
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
cv2.imshow('sobelxy',sobelxy)
cv2.waitKey()
#Canny
image=cv2.GaussianBlur(img,(5,5),0,0)
x=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
y=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
grad_mag=np.sqrt(x**2+y**2)
grad_dir=np.arctan2(y,x)
grad_mag_max=np.zeros(grad_mag.shape)
for i in range(1,grad_mag.shape[0]-1):
    for j in range(1,grad_mag.shape[1]-1):
        if grad_dir[i,j]<0:
            grad_dir[i,j]+=np.pi
        if np.pi/8<=grad_dir[i,j]<3*np.pi/8:
            if grad_mag[i,j]>grad_mag[i-1,j-1]and grad_mag[i,j]>grad_mag[i+1,j+1]:
                grad_mag_max[i,j]=grad_mag[i,j]
        elif 3*np.pi/8<=grad_dir[i,j]<5*np.pi/8:
            if grad_mag[i,j]>grad_mag[i-1,j]and grad_mag[i,j]>grad_mag[i+1,j]:
                grad_mag_max[i,j]=grad_mag[i,j]
        elif 5*np.pi/8<=grad_dir[i,j]<7*np.pi/8:
            if grad_mag[i,j]>grad_mag[i-1,j+1]and grad_mag[i,j]>grad_mag[i+1,j-1]:
                grad_mag_max[i,j]=grad_mag[i,j]
        else:
            if grad_mag[i,j]>grad_mag[i,j-1]and grad_mag[i,j]>grad_mag[i,j+1]:
                grad_mag_max[i,j]=grad_mag[i,j]
low=10
high=30
edges=np.zeros(grad_mag_max.shape)
strongedges=(grad_mag_max>high)
weakedges=(grad_mag_max>=low)&(grad_mag_max<=high)
edges[strongedges]=1
while np.sum(weakedges)>0:
    i,j=np.unravel_index(weakedges.argmax(),weakedges.shape)
    weakedges[i,j]=0
    if strongedges[i-1:i+2,j-1:j+2].any():
        edges[i,j]=1
        strongedges[i,j]=1
    else:
        edges[i,j]=0
out=edges
cv2.imshow('out',out)
cv2.waitKey()
#Harris
src=img.astype(np.float32)
H=src.shape[0]
W=src.shape[1]
x=cv2.Sobel(src,-1,1,0,3)
y=cv2.Sobel(src,-1,0,1,3)
x2=np.multiply(x,x)
xy=np.multiply(x,y)
y2=np.multiply(y,y)
x2=cv2.GaussianBlur(x2,(5,5),1.3)
xy=cv2.GaussianBlur(xy,(5,5),1.3)
y2=cv2.GaussianBlur(y2,(5,5),1.3)
R=np.zeros((H,W))#定义空的R矩阵
for i in range(H):
    for j in range(W):
        M=np.array([[x2[i,j],xy[i,j]],[xy[i,j],y2[i,j]]])
        R[i,j]= np.linalg.det(M) - 0.04 * ((M.trace())**2)
image1=cv2.imread('img')
image1[R>0.01*R.max()]=[0,0,255]
cv2.imshow('Harris',image1)
cv2.waitKey()
#直方图均衡化
hist=cv2.calcHist([img],[0],None,[256],[0,256])
cdf=hist.cumsum()
mapPixel=255*cdf/cdf[-1]
img1=np.interp(img.ravel(),range(256),mapPixel).reshape(img.shape)
img1=cv2.convertScaleAbs(img1)
cv2.imshow('kun',img1)
cv2.waitKey()