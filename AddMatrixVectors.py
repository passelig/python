"""
Created on Thu Aug 22 13:51:28 2024

This program plots two vectors and the resulting sum of these

@author: gunsto
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_vectors(vectors):
    # plots a list of vectors
    # initialize start point 
    sumVector = np.array([0, 0])# null vector
    for vector in vectors: 
        plt.plot([sumVector[0] , sumVector[0]+vector[0]], [sumVector[1],sumVector[1]+vector[1]], label='Vectors')
        # save endpoints before plotting the next vector
        sumVector= sumVector + vector
    # finally plot the vector sum
    plt.plot([0,sumVector[0]],[0,sumVector[1]])


def createCanvasAndPlotVectors():    
    # Plot lines
    plt.figure()
    plot_vectors([vector1,vector2])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Simple robot')
    plt.legend()
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    
    
# Define lines as arrays [length, anle] where angle is in degrees
vector1 = np.array([2, 5])  # Line 1 with length 3 and angle 30 degrees
vector2 = np.array([3, 3])  # Line 2 with length 4 and angle 120 degrees
# vector3 = Vector( x=3.5,y=2.6)

createCanvasAndPlotVectors()