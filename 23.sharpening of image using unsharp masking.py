import cv2
import numpy as np
img=cv2.imread(r"C:\Users\Teja\Desktop\cv\input\07.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
laplacian=np.array([[0,1,0],[1,-4,1],[0,1,0]])
lap=cv2.filter2D(gray,-1,laplacian)
sharpened=cv2.add(gray,lap)
cv2.imshow('original',gray)
cv2.imshow('shrpened',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
