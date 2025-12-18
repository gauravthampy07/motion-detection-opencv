# Real-Time Motion Detection using OpenCV

This project implements a real-time motion detection system using classical computer vision techniques in OpenCV.

## Features
- Live webcam-based motion detection
- Frame differencing for detecting movement
- Noise reduction using Gaussian blur and thresholding
- Morphological operations for stable detection
- Contour-based localization with bounding boxes
- Event-driven snapshot capture with time-based rate limiting

## Tech Stack
- Python
- OpenCV
- Computer Vision

## How it Works
1. Captures consecutive frames from a webcam
2. Computes frame differences to detect motion
3. Filters noise using blur, thresholding, and dilation
4. Detects motion regions using contours
5. Saves snapshots only when meaningful motion is detected

## Usage
Run the script:
```bash
python motion_detector.py

