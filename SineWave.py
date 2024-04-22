import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 4*pi
# x = np.linspace(0, 2 * np.pi, 10)
x = [0,0.698132,1.39626,2.0944,2.79253,3.49066,4.18879,4.88692,5.58505,6.28319]


# Calculate y values (sine of x)
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
