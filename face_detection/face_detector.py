# face_detection/face_detector.py
# using the Haar Cascades for performance
# will see if FR lib give better performance or not

import cv2

class FaceDetector:
    def __init__(self, cascade_path="./face_detection/haarcascade_frontalface_default.xml"):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    # Return the ROI of the face
    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        print(faces)
        return faces
