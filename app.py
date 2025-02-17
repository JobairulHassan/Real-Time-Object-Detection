import cv2
import tkinter as tk
from tkinter import filedialog, Button, Label
from PIL import Image, ImageTk
from ultralytics import YOLO

class ObjectDetectionApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.model = YOLO("./runs/detect/train2/weights/best.pt") 

        self.cap = None
        self.video_path = None

        # Create Tkinter components
        self.label_video_input = Label(self.window, text="Input Video")
        self.label_video_input.grid(row=0, column=0, padx=10, pady=10)
        self.label_video_output = Label(self.window, text="Processed Video")
        self.label_video_output.grid(row=0, column=1, padx=10, pady=10)

        # Label to show selected video file name
        self.label_selected_file = Label(self.window, text="", wraplength=300)
        self.label_selected_file.grid(row=1, column=0, padx=10, pady=5)

        # Create Canvas
        self.canvas_input = tk.Canvas(self.window, width=640, height=480)
        self.canvas_input.grid(row=2, column=0, padx=10, pady=10)

        self.canvas_output = tk.Canvas(self.window, width=640, height=480)
        self.canvas_output.grid(row=2, column=1, padx=10, pady=10)

        # Load button
        self.button_load_video = Button(self.window, text="Load Video", command=self.load_video)
        self.button_load_video.grid(row=3, column=0, padx=10, pady=10)

        # Confirm button
        self.button_process = Button(self.window, text="Start Processing", command=self.start_processing, state=tk.DISABLED)
        self.button_process.grid(row=3, column=1, padx=10, pady=10)

        self.window.mainloop()

    def load_video(self):
        # Open file dialog 
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])

        if self.video_path:
            # Update label with the selected file name
            file_name = self.video_path.split('/')[-1] 
            self.label_selected_file.config(text=f"Selected File: {file_name}")

            self.cap = cv2.VideoCapture(self.video_path)
            self.button_process.config(state=tk.NORMAL)

    def start_processing(self):
        if self.cap is not None and self.video_path:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break  

                results = self.model(frame)

                result = results[0] 
                frame_with_boxes = result.plot()

                # Convert OpenCV images to PIL format
                img_input = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_output = cv2.cvtColor(frame_with_boxes, cv2.COLOR_BGR2RGB)

                img_input = Image.fromarray(img_input)
                img_output = Image.fromarray(img_output)

                # Resize images for Tkinter window
                img_input = img_input.resize((640, 480), Image.Resampling.LANCZOS)
                img_output = img_output.resize((640, 480), Image.Resampling.LANCZOS)
                img_input_tk = ImageTk.PhotoImage(image=img_input)
                img_output_tk = ImageTk.PhotoImage(image=img_output)

                self.canvas_input.create_image(0, 0, anchor=tk.NW, image=img_input_tk)
                self.canvas_output.create_image(0, 0, anchor=tk.NW, image=img_output_tk)

                # Keep a reference to avoid garbage collection
                self.canvas_input.image = img_input_tk
                self.canvas_output.image = img_output_tk

                self.window.update()

            self.cap.release()

# Tkinter window
root = tk.Tk()
app = ObjectDetectionApp(root, "Object Detection Video Processing")
