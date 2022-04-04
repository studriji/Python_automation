import cv2
from cv2 import ADAPTIVE_THRESH_MEAN_C
import numpy as np 
image = cv2.imread('images.jpg')
#resize
resize_image = cv2.resize(image,(680,480))

cv2.imshow('output',resize_image)


#gray image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

#blur image
blur = cv2.medianBlur(image,21)

#edge detection
imageCanny = cv2.Canny(gray,150,200) # used to detect the edges
#cv2.imshow('canny',imageCanny)
edge_image = cv2.adaptiveThreshold(gray,255,ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow('edge',edge_image)
#Dialation expands the pixel size
kernel = np.ones((5,5),np.uint8)
imageDialation = cv2.dilate(imageCanny,kernel,iterations=1) # increase the thickness of edges,,basically it expands the pixel size, more iteration ,more thickness
#cv2.imshow('dialation',imageDialation)

# Erosion compress the pixel size
imageEroded = cv2.erode(imageDialation,kernel,iterations=1) # decrease the thickness of edges
#cv2.imshow('erosion',imageEroded)


#cropped image
image_cropped = resize_image[0:200,200:500] # [height coordinate,width coordinate]
cv2.imshow('cropped',image_cropped)

cv2.waitKey()

