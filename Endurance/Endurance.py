# Imports
import cv2

# Get Base Image
overlay = cv2.imread('Endurance/Right.png')

# Get Video
vid = cv2.VideoCapture(0)
_, temp = vid.read()

# Overlay Video with Base Image
overlay = cv2.resize(overlay, (temp.shape[1], temp.shape[0]))
while 1:
    _, frame = vid.read()
  
    cv2.imshow('frame', cv2.addWeighted(frame, 1, overlay, 0.75, 0))

    if cv2.waitKey(1) & 0xFF == ord('q'): break
