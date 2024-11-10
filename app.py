import warnings
warnings.filterwarnings("ignore")

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import torch

# Load YOLOv5 model with verification
try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    print("YOLOv5 model loaded successfully.")
except Exception as e:
    print("Error loading YOLOv5 model:", e)

# Capture from webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not access webcam.")
    exit()

# Create the root window using Tkinter
root = tk.Tk()
root.title("Object Detection with YOLOv5")

# Set an initial window size
root.geometry("800x600")  # You can change this to any desired size
root.resizable(True, True)  # Allow window resizing

# Create a canvas to display the video feed
canvas = tk.Label(root)
canvas.pack(fill=tk.BOTH, expand=True)

def update_frame():
    # Read the frame from the webcam
    success, frame = video_capture.read()
    if not success:
        print("Error: Could not read frame.")
        return
    
    # Perform object detection
    try:
        results = model(frame)  # Run the model on the frame

        # Draw bounding boxes and labels
        for result in results.xyxy[0]:  # Iterate through detections
            x1, y1, x2, y2, conf, cls = result
            label = f"{model.names[int(cls)]} {conf:.2f}"
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    except Exception as e:
        print("Error during detection:", e)

    # Resize the frame to fit the window size
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    frame_resized = cv2.resize(frame, (window_width, window_height))

    # Convert the frame to a format that can be displayed by Tkinter
    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    frame_pil = Image.fromarray(frame_rgb)
    frame_tk = ImageTk.PhotoImage(frame_pil)

    # Update the canvas with the new frame
    canvas.config(image=frame_tk)
    canvas.image = frame_tk

    # Repeat the process every 10ms
    canvas.after(10, update_frame)

# Start the frame update loop
update_frame()

# Run the Tkinter event loop
root.mainloop()

# Release the webcam when done
video_capture.release()
