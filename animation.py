# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:11:17 2024

@author: gunsto
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to update the plot with rotation
def update(frame):
    # Clear previous plot
    #plt.cla()
    
    # Rotate the line by 10 degrees
    angle = np.radians(10 * frame)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    rotated_vector = rotation_matrix.dot(initial_vector)
    
    # Plot the rotated line
    plt.plot([0, rotated_vector[0]], [0, rotated_vector[1]], color='b')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.title(f'Rotation Angle: {10 * frame} degrees')

# Initial vector
initial_vector = np.array([1, 0])

# Create a figure
fig = plt.figure()

# Start the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 36), interval=1000)

# Show the plot
plt.show()