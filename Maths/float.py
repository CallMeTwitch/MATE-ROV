# Imports
from matplotlib import pyplot as plt
from math import radians, cos, sin
import numpy as np
import cv2

# Load Grid
grid = cv2.imread('Maths/float.png')

# Get Parameters
speed = float(input('Speed (Meters per Second): '))
direction = float(input('Direction (Nautical Degrees): ')) % 360
time = float(input('Time (Hours): '))

# Find Angle & Hypotenuse of Triangle
theta = direction % 90
h = time * speed * 3.6

# Find Width & Height of Triangle
x, y = (h * sin(radians(theta)), h * cos(radians(theta))) if (direction < 90) or (180 <= direction < 270) else (h * cos(radians(theta)), h * sin(radians(theta)))

# Find Number of Boxes Travelled
xbox, ybox = round(x / 2), round(y / 2)

# Define Constants
centre = (608, 389)
pixels_per_box = 52

# Find Final Box
x2 = centre[1] + (xbox * pixels_per_box if direction <= 180 else -xbox * pixels_per_box)
y2 = centre[0] + (ybox * pixels_per_box if 90 < direction < 270 else -ybox * pixels_per_box)

# Plot
grid[(y2 - 23):(y2 + 24), (x2 - 23):(x2 + 24)] = np.array([255, 0, 0])

# Show
plt.title(f'{round(x, 2)}km ({xbox} Boxes) {"East" if direction <= 180 else "West"}, {round(y, 2)}km ({ybox} Boxes) {"South" if 90 < direction < 270 else "North"}')
plt.imshow(grid)
plt.show()
