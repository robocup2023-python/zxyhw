import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('img',0)
img1=np.float32(img)
dft=cv2.dft(img1,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_sh=np.fft.fftshift(dft)
mag=20*np.log(cv2.magnitude(dft_sh[:,:,0],dft_sh[:,:,1]))
plt.subplot(122)
plt.imshow(mag,cmap='gray')
plt.title('kun'),plt.xticks([]),plt.yticks([])
plt.show()
xw= np.angle(dft_sh)
xwimg= 20*np.log(cv2.magnitude(xw[:,:,0],xw[:,:,1]))
plt.subplot(122)
plt.imshow(xwimg,cmap='gray')
plt.title('kun'),plt.xticks([]),plt.yticks([])
plt.show()
rows,cols=img.shape
crow,ccol=int(rows/2),int(cols/2)
mask=np.ones((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-100:ccol-100]=0
fshift=dft_sh*mask
ffshift=np.fft.ifftshift(fshift)
img_back=cv2.idft(ffshift)
img_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(122)
plt.imshow(img_back,cmap='gray')
plt.title('kun'),plt.xticks([]),plt.yticks([])
plt.show()