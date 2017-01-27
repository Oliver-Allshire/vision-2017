#Function 'Module Identifier Rtape
#This code takes an image, seperates the green band and binary thresholds
#the green band.
#The binary threshold keeps all green values above 100 while turning all green
#values below 99 off.
#The output is a black image with two white rectangles in the center of the image.
#21st January 2017
#Author: Bevan Tsui
#This code is licensed CC-BY-SA

#Loading required modules and image.
import numpy as np
import cv2
import argparse
img = cv2.VideoCapture(0)



#Splitting the image into RGB bands.
while True:
    _, frame = img.read()
    cv2.CV_LOAD_IMAGE_COLOR = 1
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green = frame[:,:,1]
    ret, thresh1 = cv2.threshold(green,240,255,cv2.THRESH_BINARY)
    cv2.imshow('Preview2', thresh1)
    im2, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cv2.destroyAllWindows()