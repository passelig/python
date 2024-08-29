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
    sumVector = np.array([[0], [0]]) 
    for vector in vectors:
        x1 = sumVector[0][0]
        x2 = sumVector[0][0]+vector[0][0]
        y1 =sumVector[1][0]
        y2 =sumVector[1][0]+vector[1][0]
        plt.plot([ x1, x2], [y1,y2], label=f'{vector}')
        # save endpoints before plotting the next vector
        sumVector = sumVector + vector
    # finally plot the vector sum
    plt.plot([0,sumVector[0][0]],[0,sumVector[1][0]])


vector1 = np.array([[2], 
                    [5]]) 

vector2 = np.array([[3],
                    [2]]) 




# Plot lines
plt.figure()
plot_vectors([vector1, vector2])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple robot')
plt.legend()
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()