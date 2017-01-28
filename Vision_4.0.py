import numpy as np
import cv2
import argparse
import cscore as cs

#Start the video.
cap = cs.UsbCamera("usbcam", 0)

#Setting the exposure.
cap.setExposureManual(10)

#Reading each frame.
while True:
    _, frame = cap.read()
     
    #Converting from RGB to HSV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Setting the tolerances for the mask.
    upper_green = np.array ([150/2, 255, 255])
    lower_green = np.array([110/2, 40, 70])
    
    #Making the mask.
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    #Combining the mask with the frame
    res = cv2.bitwise_and(frame, frame, mask= mask)

    #Displaying each step.
    cv2.imshow('frame' ,frame)
    cv2.imshow('mask' ,mask)
    cv2.imshow('res' ,res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
    	break



cv2.destroyAllWindows()