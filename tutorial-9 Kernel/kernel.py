# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:47:40 2017

@author: giray
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\giray\\Desktop\\Opencv-deneme\\tutorial-1\\test2.jpg',0)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()