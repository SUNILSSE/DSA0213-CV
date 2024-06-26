import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path=r"C:\Users\Teja\Desktop\cv\input\02.jpg"
img=cv2.imread(path)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),0)
imgcanny=cv2.Canny(imgblur,100,200)
imgdilation=cv2.dilate(imgcanny,kernel,iterations=10)
imgeroded=cv2.erode(imgdilation,kernel,iterations=2)
cv2.imshow("img erosion",imgeroded)
cv2.waitKey(0)
