import matplotlib.pyplot as plt
import math

x0,y0,x1,y1,x2,y2 = 0,0,8,10,16,12
redLength = math.sqrt((x1-x0)**2+(y1-y0)**2)
redTethaAngle = math.degrees(math.atan((y1-y0)/(x1-x0)))

# Plot the line
plt.plot([x0, x1], [y0, y1], color='red')
plt.plot([x1, x2], [y1, y2], color='blue')


# Add labels and title
plt.xlabel('redLength='+ str(round(redLength,1))+'cm,    redTethaAngle='+ str(round(redTethaAngle,1))  )
plt.ylabel('Y-centimeter')
plt.title('Min robotarm')

# Show plot
plt.grid(True)
plt.show()


