import numpy as np
import matplotlib.pyplot as plt

class Vector:
  def __init__(self,x=0,y=0):
    self.matrix = np.array([[x],
                           [y]],dtype=float)
  @property
  def x(self):
    return self.matrix[0][0]
  @property
  def y(self):
    return  self.matrix[1][0]
  @property
  def angleDeg(self):
    return  np.rad2deg(self.angleRad)
  @property
  def angleRad(self):
    return np.arctan2(self.y,self.x)

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
    # plots a list of vectors
    # initialize start point 
    sumVector = Vector()
    sumVector.matrix
    for vector in vectors:
        endX = sumVector.x + vector.x # save endpoints before plotting the next vector
        endY = sumVector.y + vector.y
        plt.plot([sumVector.x , endX], [sumVector.y,endY], 
                 label=f'Length:  Angle: {vector.angleDeg:.2f} degrees')
        sumVector.matrix += vector.matrix
    return sumVector
    

vector1 = Vector(x=3,y=7 )  
vector2 = Vector( x=3,y=0)  
vector3 = Vector( x=2,y=-2) 
print(vector3.angleDeg)
vector3.rotate(np.pi / 3)
print(vector3.angleDeg)

vectorlist =[vector1, vector2,vector3]

# Plot lines
plt.figure()
sumVector = plot_vectors(vectorlist)

# finally plot the vector sum
plt.plot([0,sumVector.x],[0,sumVector.y])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple robot')
plt.legend()
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()