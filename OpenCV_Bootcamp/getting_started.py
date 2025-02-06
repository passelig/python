# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:22:54 2024

@author: gunsto
"""
import cv2

# Load the image
image = cv2.imread('checkerboard_18x18.png')

# Display the image in a window
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
