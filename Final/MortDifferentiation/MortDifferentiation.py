# Imports
import torch
import cv2

# YOLOv5 Detection Class
class Detection:
    # Initialize Class Variables
    def __init__(self):
        self.video = cv2.VideoWriter('morts.avi', 0, 30, (416, 416))
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path = 'clean/best2.pt', force_reload = False)
        
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # Predict
    def score_frame(self, frame):
        self.model.to(self.device)

        results = self.model([frame])
        return results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

    # Plot Predictions
    def plot(self, results, frame):
        labels, cord = results

        n = len(labels)
        x, y = frame.shape[1], frame.shape[0]
        for q in range(n):
            row = cord[q]

            if row[4] >= 0.5:
                x1, y1, x2, y2 = map(int, (row[0] * x, row[1] * y, row[2] * x, row[3] * y))

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
        return frame
    
    # Run
    def __call__(self):
        cap = cv2.VideoCapture('MortDifferentiation/test.mp4')
        assert cap.isOpened()

        while 1:
            ret, frame = cap.read()

            if (cv2.waitKey(5) & 0xFF == 27) or not ret:
                break

            frame = cv2.resize(frame, (416, 416))

            results = self.score_frame(frame)
            frame = self.plot(results, frame)

            cv2.imshow('', frame)
            self.video.write(frame)            

        cap.release()
        self.video.release()

# Run
detector = Detection()
detector()