import numpy as np
import matplotlib.pyplot as plt

class Vector:
  def __init__(self,x=0,y=0):
    self.matrix = np.array([[x],
                            [y]])
    self.alfaRad = np.arctan2(y,x)
    self.alfaDeg = np.rad2deg(self.alfaRad) 
    self.x = self.matrix[0][0]
    self.y = self.matrix[1][0]

def plot_vectors(vectors):
    # plots a list of vectors
    # initialize start point 
    sumVector = Vector()
    for vector in vectors:
        endX = sumVector.x + vector.x
        endY = sumVector.y + vector.y 
        plt.plot([sumVector.x , endX], [sumVector.y,endY], label=f'Length:  Angle: {vector.alfaDeg:.2f} degrees')
        # save endpoints before plotting the next vector
        sumVector= Vector(x=endX, y=endY)
    # finally plot the vector sum
    plt.plot([0,sumVector.x],[0,sumVector.y])

vector1 = Vector(x=3,y=7 )  # Line 1 with length 3 and angle 30 degrees
vector2 = Vector( x=2,y=-3)  # Line 2 with length 4 and angle 120 degrees
vectorlist =[vector1, vector2]

print(vector1.matrix[1][0])

# Plot lines
plt.figure()
plot_vectors(vectorlist)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple robot')
plt.legend()
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()