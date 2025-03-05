# face_detection/face_detector.py
# using the Haar Cascades for performance
# will see if FR lib give better performance or not

import cv2
import os

class FaceDetector:

    def __init__(self):
    # def __init__(self, cascade_path="./face_detection/haarcascade_frontalface_default.xml"):
        base_path = "./face_detection/"
        # self.face_cascade = cv2.CascadeClassifier(cascade_path)

        self.frontal_cascade = cv2.CascadeClassifier(os.path.join(base_path, "haarcascade_frontalface_default.xml"))
        self.profile_cascade = cv2.CascadeClassifier(os.path.join(base_path, "haarcascade_profileface.xml"))
        self.alt_cascade = cv2.CascadeClassifier(os.path.join(base_path, "haarcascade_frontalface_alt.xml"))
        self.alt2_cascade = cv2.CascadeClassifier(os.path.join(base_path, "haarcascade_frontalface_alt2.xml"))


    # Return the ROI of the face
    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        ## now supporting various face angles
        ## distance needs to be tested // TODO //
        frontal_faces = self.frontal_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        profile_faces = self.profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        alt_faces = self.alt_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
        alt2_faces = self.alt2_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        all_faces = list(frontal_faces) + list(profile_faces) + list(alt_faces) + list(alt2_faces)

        print(frontal_faces)
        print(len(all_faces))
        return frontal_faces
