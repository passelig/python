# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:20:39 2024

@author: gunsto
"""
import numpy as np
import matplotlib.pyplot as plt

class Vector:
    def __init__(self, x=0, y=0):
        # Ensure matrix is initialized as float to prevent type casting issues
        self.matrix = np.array([[x],
                                [y]], dtype=float)
    @property
    def x(self):
        return self.matrix[0][0]
    @property
    def y(self):
        return self.matrix[1][0]
    @property
    def angleDeg(self):
        return np.rad2deg(self.angleRad)
    @property
    def angleRad(self):
        return np.arctan2(self.y, self.x)
    def rotate(self, radianRotation):
        """Rotates the vector by the specified angle in radians."""
        # Define the rotation matrix
        rotation_matrix = np.array([
            [np.cos(radianRotation), -np.sin(radianRotation)],
            [np.sin(radianRotation), np.cos(radianRotation)]
        ])
        # Apply the rotation matrix to the vector
        self.matrix = rotation_matrix @ self.matrix


def plot_vectors(vectors):
    # Plots a list of vectors and returns the sum vector
    _sumVector = Vector()
    for vector in vectors:
        endX = _sumVector.x + vector.x  # Save endpoints before plotting the next vector
        endY = _sumVector.y + vector.y
        plt.plot([_sumVector.x, endX], [_sumVector.y, endY],
                 label=f'Length: {np.sqrt(vector.x**2 + vector.y**2):.2f}, Angle: {vector.angleDeg:.2f} degrees')
        _sumVector.matrix += vector.matrix  # Sum vectors
    # Return the vector sum
    return _sumVector