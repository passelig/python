import numpy as np
import matplotlib.pyplot as plt

def plot_lines(lines):
    """
    Plot lines defined by their lengths and angles.
    
    Parameters:
        lines (list of arrays): List of arrays where each array represents a line with its length and angle.
                                Each array should have two elements representing the length and angle in degrees.
    """
    start = [0, 0]
    for line in lines:
        length, angle = line
        angle_rad = np.deg2rad(angle)
        end = [start[0] + length * np.cos(angle_rad), start[1] + length * np.sin(angle_rad)]
        plt.plot([start[0], end[0]], [start[1], end[1]], label=f'Length: {length}, Angle: {angle} degrees')
        start = end

# Define lines as arrays [length, angle] where angle is in degrees
line1 = [3, 70]  # Line 1 with length 3 and angle 30 degrees
line2 = [4, 45]  # Line 2 with length 4 and angle 120 degrees

# Plot lines
plt.figure()
plot_lines([line1, line2])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Plot')
plt.legend()
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

