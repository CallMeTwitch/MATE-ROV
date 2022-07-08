# Imports
from matplotlib import pyplot as plt
from imutils import grab_contours
import numpy as np
import cv2

# Define Image Stitching Function
def stitch(img1, img2):
    # Convert to Black & White
    gray1, gray2 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY), cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

    # Find Keypoints using SIFT
    kps1, f1 = cv2.SIFT_create().detectAndCompute(gray1, None)
    kps2, f2 = cv2.SIFT_create().detectAndCompute(gray2, None)

    # Initialize Best Fit Matcher
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = False)

    # Match
    matches = [q for q, w in bf.knnMatch(f1, f2, 2) if q.distance < (w.distance * 0.75)]

    # Prepare
    kps1, kps2 = np.float32([kp.pt for kp in kps1]), np.float32([kp.pt for kp in kps2])

    pts1, pts2 = np.float32([kps1[q.queryIdx] for q in matches]), np.float32([kps2[q.trainIdx] for q in matches])

    # Find Homogrpahy Needed to Combine Images
    homography, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC, 4)

    # Largest Size Possible
    w, h = img1.shape[1] + img2.shape[1], img1.shape[0] + img2.shape[0]

    # Warp Image1 to Fit Image2
    output = cv2.warpPerspective(img1, homography, (w, h))

    # Combine Images
    y_max, x_max = img2.shape[0], img2.shape[1]
    temp = cv2.cvtColor(cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    output[:y_max, :x_max] = np.where(temp < 60, output[:y_max, :x_max], img2)

    # Remove Negative Space & Return
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

    contours = grab_contours(cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_SIMPLE))

    w, h, x, y = cv2.boundingRect(max(contours, key = cv2.contourArea))

    return output[h:(h + y), w:(w + x)]

# Get Images
top_left, top_middle_left, top_middle_right, top_right, bottom_left, bottom_middle_left, bottom_middle_right, bottom_right = cv2.imread('image1.png'), cv2.imread('image2.png'), cv2.imread('image3.png'), cv2.imread('image4.png'), cv2.imread('image5.png'), cv2.imread('image6.png'), cv2.imread('image7.png'), cv2.imread('image8.png')

# Stitch Top from Right to Left
top = stitch(top_right, top_middle_right)
top = stitch(top, top_middle_left)
top = stitch(top, top_left)

# Stitch Bottom from Right to Left
bottom = stitch(bottom_right, bottom_middle_right)
bottom = stitch(bottom, bottom_middle_left)
bottom = stitch(bottom, bottom_left)

# Stitch Bottom to Top
final = stitch(bottom, top)

# Show
plt.imshow(final)
plt.show()