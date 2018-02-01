#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time

def activeDeleteBackground(videoFileHistory,N):
	avgPic = np.mean(np.array(videoFileHistory),axis=0).astype(int)
	return 256*abs(videoFileHistory[N-1] - avgPic)

def directionDetect(videoFileHistory):
	#If current frame more focused to the left of previous frame by 10% frame width
		#return "Left"
	#If current frame more focused to the right of previous frame by 10% frame width	
 		#return "Right"
	#Else
		return

def main():
	startTime = time.time()
	videoFile =  '/home/ubuntu/Documents/Background Subtraction/ShortenedCar.mp4'
	N = 3
	tempFrames = []
	j = N
    	
	for i in range(N):
		cap = cv2.VideoCapture(videoFile)
		ret,frame = cap.read()
		tempFrames.append(frame)
	nframes = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	
	print(nframes)
	for i in range(600,N,-1):
		j = j + 1
		improvedFrame = activeDeleteBackground(tempFrames,N)
		tempFrames = tempFrames[1:]
		ret,frame = cap.read()
		tempFrames.append(frame)
		cv2.imshow('frame',improvedFrame)
		if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
			cap.release()
			cv2.destroyAllWindows()
			break
	return
    
if __name__ == "__main__":
    main()

"""
if j == 21:
			print(time.time() - startTime)
"""

"""
print("The video is ")
print(nframes/7)
print("seconds long and took ")
print(time.time() - startTime)
print("seconds to process")
"""
