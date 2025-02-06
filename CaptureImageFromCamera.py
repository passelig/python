# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:55:28 2025

@author: gunsto
"""

import cv2

# Open the default camera (0)
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a single frame
ret, frame = cap.read()

if ret:
    # Display the captured frame
    cv2.imshow("Captured Image", frame)
    
    # Save the captured frame (optional)
    cv2.imwrite("captured_image.jpg", frame)
    
    # Wait for key press and close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not capture image.")

# Release the camera
cap.release()
