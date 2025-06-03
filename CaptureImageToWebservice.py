# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:01:39 2025

@author: gunsto
"""

import cv2
import os
from flask import Flask, send_file

app = Flask(__name__)

def capture_image():
    """Captures an image from the camera and saves it."""
    cap = cv2.VideoCapture(0)  # Open camera
    if not cap.isOpened():
        return None
    
    ret, frame = cap.read()  # Capture frame
    cap.release()  # Release camera

    if ret:
        image_path = "captured_image.jpg"
        cv2.imwrite(image_path, frame)  # Save the image
        return image_path
    return None

@app.route('/download')
def download_image():
    """Captures an image and allows it to be downloaded."""
    image_path = capture_image()
    if image_path:
        return send_file(image_path, as_attachment=True)
    return "Failed to capture image", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
