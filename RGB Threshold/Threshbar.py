import cv2
import numpy as np

def nothing(x):
	pass

def color_thresh(image, rgb_thresh=(0,0,0)):
	binary_image = np.zeros_like(image[:,:,0])
	above_threshold = (image[:,:,0] > rgb_thresh[0]) & (image[:,:,1] > rgb_thresh[1]) & (image[:,:,2] > rgb_thresh[2])
	binary_image[above_threshold] = 255
	return binary_image

car_image = cv2.imread('Carpic.png')

# Create a black image, a window
img = np.zeros_like(car_image[:,:,0])
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    
    rgb_threshold = (r,g,b)   
    img = color_thresh(car_image, rgb_threshold)
    #img[:] = [b,g,r]


cv2.destroyAllWindows()
