import cv2
import numpy as np

img=cv2.imread('f1.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.GaussianBlur(gray,(5,5),0)
sharp=cv2.addWeighted(gray,1.5,blur,-0.5,0)


cv2.imshow('f1.jpg',img)
cv2.imshow('enhanced_f1_1.jpg',sharp)
cv2.imwrite('enhanced_f1_1.jpg',sharp)

cv2.waitKey(0)

cv2.destroyAllWindows()
