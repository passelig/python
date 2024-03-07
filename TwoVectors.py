import numpy as np
import matplotlib.pyplot as plt

class Line:
  def __init__(self, length, angle):
    self.length = length
    self.angle = angle

def plot_lines(lines):
    start = [0, 0]
    for line in lines:
        #length, angle = line
        angle_rad = np.deg2rad(line.angle)
        end = [start[0] + line.length * np.cos(angle_rad), start[1] + line.length * np.sin(angle_rad)]
        plt.plot([start[0], end[0]], [start[1], end[1]], label=f'Length: {line.length}, Angle: {line.angle} degrees')
        start = end
    plt.plot([0,end[0]],[0,end[1]])


# Define lines as arrays [length, angle] where angle is in degrees
line1 = Line(3, 70)  # Line 1 with length 3 and angle 30 degrees
line2 = Line( angle=10,length=4)  # Line 2 with length 4 and angle 120 degrees

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

