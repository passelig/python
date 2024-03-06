import numpy as np

def calculateSomething (line):
    value1 = np.cos(np.deg2rad(line[1]))*line[0]
    value2 = np.sin(np.deg2rad(line[1]))*line[0]
    print(f'value1: {value1}, value2: {value2} ')


# Define lines as arrays [length, angle] where angle is in degrees
line1 = [3, 45]  # Line 1 with length 3 and angle 30 degrees

calculateSomething(line1)