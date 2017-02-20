# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:23:37 2017

@author: giray
"""
import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global count
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    print("mouse call back")
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("leftdouble")
        count = count+1
        if count==1.00:
            x1,y1 = x,y
            print("x1 ve y1 tamam",x1,y1,count)
        if count==2.00:
            x2,y2 = x,y
            print("x2 ve y2 tamam",x2,y2,count)
        if count==3.00:
            x3,y3 = x,y
            print("x3 ve y3 tamam",x3,y3,count)
        if count==4.00:
            x4,y4 = x,y
            print("x4 ve y4 tamam",x4,y4,count)
img = cv2.imread('C:\\Users\\giray\\Desktop\\Opencv-deneme\\tutorial-1\\test2.jpg',0)
rows,cols = img.shape
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
count = 0.00
while(1):
    cv2.imshow('image',img)
    if count==4:
        break
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
print(x1,x2,x3,x4,y1,y2,y3,y4)
pts1 = np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()