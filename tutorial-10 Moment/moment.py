# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:17:34 2017

@author: giray
"""

import cv2
#import numpy as np

img = cv2.imread('C:\\Users\\giray\\Desktop\\Opencv-deneme\\tutorial-1\\test2.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(thresh, contours[0], -1, (255,255,255), 3)
cv2.imshow('image',thresh)
cnt = contours[100]
M = cv2.moments(cnt)
print(M)
cv2.waitKey(0)
cv2.destroyAllWindows()