# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:06:57 2017

@author: giray
"""

# libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in window
img = cv2.imread('test2.jpg',cv2.WINDOW_NORMAL)

# to show image and wait for keyboark interrupt then close window
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# to show image another way in terminal
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
