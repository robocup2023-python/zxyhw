import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def guassion_kernel(size, sigma):
    GaussKernel = np.zeros((size, size),dtype=np.float64)
    padding = size // 2
    xx=np.arange(-padding,-padding+size,1)
    yy=np.arange(-padding,-padding+size,1)
    for i in range(size):
        for j in range(size):
            xAddy = math.pow(i - padding, 2) + math.pow(j - padding, 2)
            GaussKernel[i, j] = math.exp(-xAddy / (2 * math.pow(sigma, 2))) / 2 * math.pi * math.pow(sigma, 2)
    sum = np.sum(GaussKernel)
    GaussKernel = GaussKernel / sum
    ax1=plt.axes(projection='3d')
    X,Y=np.meshgrid(xx,yy)
    ax1.plot_surface(X,Y,GaussKernel)
    plt.show()
    return GaussKernel
guassion_kernel(5,0.8)
def guassian_filter(img,size,sigma):
    GaussKernel = np.zeros((size, size),dtype=np.float64)
    padding = size // 2
    (H,W,C)=img.shape
    out=np.zeros((H+padding*2,W+padding*2,C),dtype=np.float64)
    out[padding:padding+H,padding:padding+W]=img.copy().astype(np.float64)
    for i in range(size):
        for j in range(size):
            xAddy = math.pow(i - padding, 2) + math.pow(j - padding, 2)
            GaussKernel[i, j] = math.exp(-xAddy / (2 * math.pow(sigma, 2))) / 2 * math.pi * math.pow(sigma, 2)
    sum = np.sum(GaussKernel)
    GaussKernel = GaussKernel / sum
    tmp=out.copy()
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[padding+y,padding+x,c]=np.sum(GaussKernel*tmp[y:y+size,x:x+size,c])
    out=np.clip(out,0,255)
    out=out[padding:padding+H,padding:padding+W].astype(np.uint8)
    return out
image=cv2.imread('img')
out=guassian_filter(image,size=5,sigma=2.0)
cv2.imshow('result',out)
cv2.imwrite('out.jpg',out)
cv2.waitKey()
def zero_pad(img,size):
    pad=size//2
    (H,W,C)=img.shape
    out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float64)
    out[pad:pad+H,pad:pad+W]=img.copy().astype(np.float64)
    out=out.astype(np.uint8)
    return out
def replicate_pad(img,size):
    (H,W,C)=img.shape
    
