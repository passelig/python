
import matplotlib.pyplot as plt
import numpy as np

# Define the radius
radius = 3

# Create an array of angles from 0 to 2*pi
theta = np.linspace(0, 2*np.pi, 100)

# Calculate the x and y coordinates of the points on the circle
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Plot the circle
plt.figure(figsize=(6,6))  # Set aspect ratio to be equal
plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')  # Set aspect ratio to be equal
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Circle with Radius 3 and Origin at (0,0)')
plt.grid(True)
plt.show()
