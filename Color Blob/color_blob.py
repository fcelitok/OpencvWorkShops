# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:41:37 2017

@author: giray
"""

# HSV color filter and find center of gravity by calculating moments

# import libraries
import cv2
import numpy as np

# empty function
def nothing(x):
    pass

h = 40 # centimeter
focal_length_x = 685.93*5.25 # focal lenght of camera
focal_length_y = 687.33*5.25/1.3 # focal lenght of camera 

# define windows
cv2.namedWindow('input')
cv2.namedWindow('mask')
cv2.namedWindow('input+mask')
cv2.namedWindow('options', cv2.WINDOW_NORMAL)

# create trackbars for options
cv2.createTrackbar('h_min','options',0,180,nothing)
cv2.createTrackbar('h_max','options',0,255,nothing)
cv2.createTrackbar('s_min','options',0,255,nothing)
cv2.createTrackbar('s_max','options',0,180,nothing)
cv2.createTrackbar('v_min','options',0,255,nothing)
cv2.createTrackbar('v_max','options',0,255,nothing)
cv2.createTrackbar('openKernelSize','options',1,10,nothing)
cv2.createTrackbar('closeKerneSize','options',1,10,nothing)

#open webcam
cap = cv2.VideoCapture(0)

while(1):
    #capture frame
    ret, frame = cap.read()
    #frame = cv2.imread('test2.jpg')
    # convert to HSV color space
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    
    # getting parameter list
    h_min = cv2.getTrackbarPos('h_min','options')
    h_max = cv2.getTrackbarPos('h_max','options')
    s_min = cv2.getTrackbarPos('s_min','options')
    s_max = cv2.getTrackbarPos('s_max','options')
    v_min = cv2.getTrackbarPos('v_min','options')
    v_max = cv2.getTrackbarPos('v_max','options')
    openKernelSize = cv2.getTrackbarPos('openKernelSize','options')
    closeKernelSize = cv2.getTrackbarPos('closeKernelSize','options')

    # define mask    
    low_values =  np.array([h_min, s_min, v_min])
    high_values =  np.array([255-h_max, 255-s_max, 255-v_max])
    mask = cv2.inRange(imgHSV, low_values, high_values)
    
    # morphological openin and closing
    openKernelSize = (abs(openKernelSize)*2+1,abs(openKernelSize)*2+1)
    closeKernelSize = (abs(closeKernelSize)*2+1,abs(closeKernelSize)*2+1)
    openKernel = np.ones(openKernelSize,np.uint8)
    closeKernel = np.ones(closeKernelSize,np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, openKernel)
    mask_ = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, closeKernel)
    
    # final image output
    imgFiltered = cv2.bitwise_and(frame,frame, mask= mask_)
    
    # calculate moments
    moments = cv2.moments(mask_)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    # calculate center of gravity
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)
    ctr = (-1,-1)
    # draw circle on center of gravity and calculate real x and y by pinhole model
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
        cv2.circle(frame, ctr, 10, (255,0,0))
        h, w = mask_.shape
        ctr = (w/2-centroid_x, h/2-centroid_y)
        loc_x = (ctr[0]*h)/focal_length_x
        loc_y = (ctr[1]*h)/focal_length_y
        print(' loc_x  ',loc_x,'cm','\'II  loc_y ',loc_y,'cm', 'pixel_x',ctr[0],'pixel_y',ctr[1])
    
    # display images
    cv2.imshow('input',frame)
    cv2.imshow('mask', mask_)
    cv2.imshow('input+mas',imgFiltered)
    
    # waiting 'q' for exit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()