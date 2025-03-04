# face_detection/camera_manager.py
# single place to manage all the cam settings. On some devices, 
# the camera input turns blue, will be handled here.

import cv2

class CameraManager:
    def __init__(self, width=640, height=480, framerate=30):
        self.width = width
        self.height = height
        self.framerate = framerate
        self.cap = None

    ## my GStreamer pipeline for the Raspberry Pi Cam
    def gstreamer_pipeline(self):
        return (
            f"libcamerasrc ! video/x-raw,format=NV12,width={self.width},height={self.height},framerate={self.framerate}/1 ! "
            "videoconvert ! video/x-raw,format=BGR ! appsink"
        )

    ## open the gs-pipeline
    def open_camera(self):
        self.cap = cv2.VideoCapture(self.gstreamer_pipeline(), cv2.CAP_GSTREAMER)

        if not self.cap.isOpened():
            print("err")
            return False
        return True

    def read_frame(self):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
        return None

    def close_camera(self):
        if self.cap is not None and self.cap.isOpened():
            self.cap.release()
            print("system ended")
