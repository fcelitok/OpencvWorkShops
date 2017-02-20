# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:37:21 2017

@author: giray
"""
#Libraries
import numpy as np
import cv2
# to open webcam, change 0 with 1 for changing default cam 
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # capture frame from video
    ret, frame = cap.read()

    # convert color scale image to gray scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the resulting frame to quit press 'q'
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()