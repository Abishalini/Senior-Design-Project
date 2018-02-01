#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
videoFile = '/home/ubuntu/Documents/Background Subtraction/rellisCar.mp4'
"""
with open(videoFile,'r') as inpFile:
    for line in inpFile:
        data = line.read()
        print(data)
"""
"""
cap = cv2.VideoCapture(videoFile)
ret,frame = cap.read()
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
"""

cap = cv2.VideoCapture(videoFile)
print(cap.isOpened())
cap.open(videoFile)
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
for i in range(1000):

    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
        cap.release()
        cv2.destroyAllWindows()
        break
        break
        break
        break
        break
        
"""
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""
