# ui/main_window.py

import tkinter as tk
from ui.face_registration_screen import FaceRegistrationWindow
#from ui.face_registration_window import FaceRegistrationWindow
from PIL import Image, ImageTk
import cv2

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Face Registration App")
        self.geometry("800x600")

        # top Menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Register New Face", command=self.open_face_registration_window)
        menubar.add_cascade(label="File", menu=file_menu)

        # render captured images
        self.captured_images_frame = tk.Frame(self)
        self.captured_images_frame.pack(fill=tk.BOTH, expand=True)
        self.captured_image_widgets = []

    ## FR popup
    def open_face_registration_window(self):
        FaceRegistrationWindow(self, on_save_callback=self.handle_captured_images)

    def handle_captured_images(self, images):
        for widget in self.captured_image_widgets:
            widget.destroy()
        self.captured_image_widgets.clear()

        for idx, frame in enumerate(images):
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(pil_img)

            lbl = tk.Label(self.captured_images_frame, image=imgtk)
            lbl.imgtk = imgtk
            lbl.grid(row=0, column=idx, padx=5, pady=5)

            self.captured_image_widgets.append(lbl)
