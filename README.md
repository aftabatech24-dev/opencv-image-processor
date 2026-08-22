# 🖼️ Python OpenCV Image Processor & Quadrant Splitter

A Python computer vision application built with OpenCV (`cv2`) that dynamically reads, resizes, crops, and analyzes images. The script uses Object-Oriented Programming (OOP) to break images into four equal quadrants dynamically, ensuring compatibility across different image dimensions.

## 🚀 Features

* **Image Inspection:** Loads image data and retrieves dimensions (height, width, color channels) dynamically using NumPy array shapes.
* **Proportional Resizing:** Scalable image resizing based on percentage dimensions.
* **Dynamic Quadrant Cropping:** Automatically calculates image midpoint coordinates (`mid_x`, `mid_y`) to slice any image into 4 equal quadrants (Top-Left, Top-Right, Bottom-Left, Bottom-Right).
* **Robust File Handling:** Safe image loading with exception checks to handle missing files gracefully.

## 🧠 Python & Computer Vision Concepts

* **OpenCV (`cv2`):** Reading images into BGR format arrays (`cv2.imread`), window management (`imshow`), and keypress waiting.
* **NumPy Slicing:** Cropping region-of-interest (ROI) using array coordinate slicing `img[y1:y2, x1:x2]`.
* **Object-Oriented Programming (OOP):** Encapsulating image operations within an `ImageProcessor` class.
* **Dynamic Calculations:** Calculating dimensions instead of using hardcoded pixel coordinates.

## 💻 Setup & Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/opencv-image-processor.git](https://github.com/your-username/opencv-image-processor.git)
  # opencv-image-processor
