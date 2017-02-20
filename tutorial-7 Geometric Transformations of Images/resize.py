# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:13:18 2017

@author: giray
"""

import cv2
import numpy as np

img = cv2.imread('C:\\Users\\giray\\Desktop\\Opencv-deneme\\tutorial-1\\test2.jpg')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('orijinal',img)
cv2.imshow('resized',res)

cv2.waitKey(0)
cv2.destroyAllWindows()