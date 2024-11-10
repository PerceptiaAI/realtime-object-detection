# YOLOv5 Object Detection with Real-Time Webcam Feed

![YOLOv5 Object Detection](https://img.shields.io/badge/YOLOv5-Object%20Detection-blue?style=flat-square)

## Overview

This project demonstrates real-time object detection using the YOLOv5 deep learning model, displayed via a **resizable** Tkinter window. The application leverages a webcam feed to detect objects and overlay bounding boxes and labels in real-time.

**Key Features:**
- Real-time object detection with YOLOv5.
- Webcam feed displayed in a resizable window.
- Bounding boxes and object labels overlaid on detected objects.
- Full compatibility with any system that supports Python and OpenCV.

## Requirements

To run this application, you need to install the following Python dependencies:

- **Python 3.x**
- `torch` (for YOLOv5)
- `opencv-python-headless`
- `Pillow` (for image processing)
- `tkinter` (for GUI)

### Install Dependencies

Use `pip` to install the required packages:

```bash
pip install torch opencv-python-headless Pillow
```

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PerceptiaAI/realtime-object-detection.git
   cd realtime-object-detection.git
   ```

2. **Run the application:**

   ```bash
   python app.py
   ```

   This will launch a Tkinter window where the webcam feed will appear with real-time object detection. You can resize the window to fit the video feed.

3. **Interact with the GUI:**
   - The window will automatically adjust the video feed size to fit within the window.
   - Detected objects will be highlighted with bounding boxes, and each object will be labeled with its class and confidence score.

## How It Works

- The application uses **YOLOv5**, a state-of-the-art object detection model from **Ultralytics**.
- It captures frames from your computer’s webcam using **OpenCV**.
- Each frame is passed through the YOLOv5 model, which detects objects and draws bounding boxes around them.
- The processed frame is then displayed in a **Tkinter** window, dynamically adjusting to the window's size.

## Customization

Feel free to customize the application to suit your needs:
- Modify the `app.py` script to use different YOLOv5 models (e.g., `yolov5m`, `yolov5l`, `yolov5x`).
- Change the initial window size in the script by adjusting the `root.geometry()` values.
- You can also explore adding new features such as saving detection results, adding user controls, or improving the GUI's look.

## Contributing

We welcome contributions! Feel free to fork this repository and submit a pull request with improvements or bug fixes.

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to your branch (`git push origin feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---