# Imports
from matplotlib import pyplot as plt
import numpy as np
import cv2

# Settings
plt.ion()

# Show Picture Function
def show(image, figure):
    plt.figure(figure)

    plt.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1)
    plt.axis('off')

    plt.imshow(image)
    plt.show()

# Get Base & Test Case
tail, centre, head = cv2.imread('FishMeasuring/tail.png'), cv2.imread('FishMeasuring/centre.png'), cv2.imread('FishMeasuring/head.png')
test_case = cv2.imread('FishMeasuring/test.jpg')

# Show Cases
show(np.concatenate((tail, centre, head), axis = 1), 1)
show(test_case, 2)

# if Inverted: Flip
if input('Would you like to flip? ').lower() == 'y':
    test_case = cv2.flip(test_case, 1)
    show(test_case, 2)

# Start Coordimates
x0, y0, x1, y1 = 0, 0, test_case.shape[1], test_case.shape[0]

# Define Pixels per Centimeter in Base Case
pixels_per_cm = 20.316

# Resize Test Case to Base Case
done = input('Finished resizing? ')
while done.lower() != 'y':
    print(f'x0:{x0}, x1:{x1}, y0:{y0}, y1:{y1}')
    x0, x1, y0, y1 = map(int, [input('x0: '), input('x1: '), input('y0: '), input('y1: ')])

    show(np.concatenate((tail, centre, head), axis = 1), 1)
    show(test_case[y0:y1, x0:x1], 2)

    done = input('Finished resizing? ')

# Fit Length of Base Case to Test Case
total_delta = 0

done = input('Finished fitting? ')
while done.lower() != 'y':
    total_delta += (delta := int(input('Delta: ')))

    centre = cv2.resize(centre, (centre.shape[1] + delta, centre.shape[0]))

    show(np.concatenate((tail, centre, head), axis = 1), 1)
    show(test_case[y0:y1, x0:x1], 2)

    done = input('Finished fitting? ')

# Return Final Length Estimate
print(f'\nEstimated Fish Length: {round(38 + (total_delta / pixels_per_cm), 2)}cm')
