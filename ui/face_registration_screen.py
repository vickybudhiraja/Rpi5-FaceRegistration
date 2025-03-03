# ui/face_registration_window.py

import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import cv2

from face_detection.camera_manager import CameraManager
from face_detection.face_detector import FaceDetector

class FaceRegistrationWindow(Toplevel):
    def __init__(self, parent, on_save_callback):
        super().__init__(parent)
        self.title("Register New Face")
        # more than 640x480 to fit buttons
        self.geometry("700x600")

        self.parent = parent
        self.on_save_callback = on_save_callback

        self.camera_manager = CameraManager()
        self.face_detector = FaceDetector()
        self.camera_manager.open_camera()

        self.captured_images = []

        # UI Elements ##############################################
        self.preview_label = tk.Label(self, width=640, height=480)
        self.preview_label.pack(pady=10)
        button_frame = tk.Frame(self)
        button_frame.pack()
        capture_btn = tk.Button(button_frame, text="Capture", command=self.capture_frame)
        capture_btn.grid(row=0, column=0, padx=5)
        save_btn = tk.Button(button_frame, text="Save", command=self.save_and_close)
        save_btn.grid(row=0, column=1, padx=5)
        cancel_btn = tk.Button(button_frame, text="Cancel", command=self.cancel)
        cancel_btn.grid(row=0, column=2, padx=5)

        # camera preview
        self.update_preview()

    def update_preview(self):
        frame = self.camera_manager.read_frame()
        if frame is not None:
            faces = self.face_detector.detect_faces(frame)

            # bboxes around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Convert BGR to RGB <-- POSSIBLE ISSUE TODO
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(img)

            self.preview_label.imgtk = imgtk
            self.preview_label.config(image=imgtk)

        self.after(20, self.update_preview)

    def capture_frame(self):
        frame = self.camera_manager.read_frame()
        if frame is not None:
            self.captured_images.append(frame)
            print("Frame img captured!")

    def save_and_close(self):
        self.on_save_callback(self.captured_images)
        self.close_window()

    def cancel(self):
        self.captured_images.clear()
        self.close_window()

    def close_window(self):
        self.camera_manager.close_camera()
        # clean
        self.destroy()
