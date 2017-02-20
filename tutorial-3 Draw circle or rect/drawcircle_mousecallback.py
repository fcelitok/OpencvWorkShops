# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:44:26 2017

@author: giray
"""

import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,255,255),-1)

# create a black empty image
img = np.zeros((512,512,3), np.uint8)
# create empty window in the name of 'image'
cv2.namedWindow('image')
# set mouse callback function which is draw_circle
#when you move your mouse in the window interrupt occur
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27: # exit from while loop press 'esc'
        break
cv2.destroyAllWindows()
