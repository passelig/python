import numpy as np
import matplotlib.pyplot as plt
import math

class Vector:
  def __init__(self, length=0, angleDeg=0,x=0,y=0):
    if (length>0):
        self.length = length
        self.angleDeg = angleDeg
        self.angleRad = np.deg2rad(angleDeg)
        self.x = self.length * np.cos(self.angleRad)
        self.y = self.length * np.sin(self.angleRad)
    else:
        self.x = x
        self.y = y
        self.length = math.sqrt(x**2 + y**2)
        self.angleRad = 0 if (y==0) else math.atan(x/y)
        self.angleDeg =  np.rad2deg(self.angleRad)
        

def plot_lines(vectors):
    # plots a list of vectors
    # initialize start point 
    sumVector = Vector()
    for vector in vectors:
        endX = sumVector.x + vector.x
        endY = sumVector.y + vector.y 
        plt.plot([sumVector.x , endX], [sumVector.y,endY], label=f'Length: {vector.length:.2f}, Angle: {vector.angleDeg:.2f} degrees')
        # save endpoints before plotting the next vector
        sumVector= Vector(x=endX, y=endY)
    # finally plot the vector sum
    plt.plot([0,sumVector.x],[0,sumVector.y])


# Define lines as arrays [length, anle] where angle is in degrees
vector1 = Vector(length=3,angleDeg=120 )  # Line 1 with length 3 and angle 30 degrees
vector2 = Vector( length=3,angleDeg=-30)  # Line 2 with length 4 and angle 120 degrees
#vector3 = Vector( length=2,angleDeg=-10)

vector2.angleDeg

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

