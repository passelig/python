import numpy as np
import matplotlib.pyplot as plt

class Vector:
  def __init__(self, length=0, angle=0,x=0,y=0):
    if (length):
        self.length = length
        self.angle = angle
    else:
        self.le
  def radianAngle(self):
    return np.deg2rad(self.angle)
  def x(self):
    return self.length * np.cos(self.radianAngle())
  def y(self):
        return self.length * np.sin(self.radianAngle())
        

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def plot_lines(vectors):
    sumVector = Vector()
    for vector in vectors:
        x = vector.x() + sumVector.x()
        y = vector.y() + sumVector.x()
        plt.plot([sumVector.x(), x], [sumVector.y(), y], label=f'Length: {vector.length}, Angle: {vector.angle} degrees')
        sumVector= Vector(x=sumVector.x() + x, y=sumVector.y() + y)
    plt.plot([0,sumVector.x()],[0,sumVector.y])


# Define lines as arrays [length, angle] where angle is in degrees
vector1 = Vector( length=2, angle=70)  # Line 1 with length 3 and angle 30 degrees
vector2 = Vector( length=3,angle=10)  # Line 2 with length 4 and angle 120 degrees

vector1.radianAngle()

# Plot lines
plt.figure()
plot_lines([vector1, vector2])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple robot')
plt.legend()
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

