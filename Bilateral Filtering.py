import cv2
import numpy as np

img=cv2.imread('f1.jpg')

kernel_25=np.ones((25,25),np.float32)/625.0
output_kernel=cv2.filter2D(img,-1,kernel_25)

#Kernel Blur

cv2.imshow('orignal image',img)

#cv2.imshow('kernel blur',output_kernel)

output_blur=cv2.blur(img,(25,25))

output_box=cv2.boxFilter(img,-1,(5,5),normalize=True)

#Gaussian Blur
output_gaussian=cv2.GaussianBlur(img,(5,5),0)

# median blur - reduction of noise
output_med=cv2.medianBlur(img,5)

# bilateral filtering
output_bilateral=cv2.bilateralFilter(img,5,6,6)

cv2.imshow('Bilateral Filtering',output_bilateral)

cv2.imshow('Blur() output',output_blur)

cv2.imshow('Box filter',output_box)

cv2.imshow('gaussian blur',output_gaussian)

cv2.imshow('Median Blur',output_med)

cv2.waitKey(0)

cv2.destroyAllWindows()
