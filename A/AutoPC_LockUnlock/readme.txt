Face Detection and Screen Lock Automation

This simple Python script uses the OpenCV library to detect faces using your laptop's camera and automates the screen lock and unlock process based on whether your face is in front of the camera or not.

Prerequisites
Before running this script, make sure you have the following installed on your computer:

Python: You can download it from the official Python website at python.org.

OpenCV: Install OpenCV using pip by running the following command:
pip install opencv-python

pyautogui: Install pyautogui using pip by running the following command:
pip install pyautogui

Usage
Clone or download this repository to your local machine.

Connect your laptop's camera.

Run the script by executing the following command in your terminal or command prompt:
python face_detection_and_lock.py

The script will open a camera feed and start detecting faces in real-time.If no faces are detected for 100 consecutive frames, the script will automatically lock your screen.
When you come back in front of the camera, it will unlock your screen.

To exit the script, press 'q' in the terminal where the script is running.

Configuration
You can modify the script by changing the following parameters:
scaleFactor: Adjust the value to change the sensitivity of face detection.
minNeighbors: Increase or decrease this value to fine-tune face detection.
minSize: Change the minimum size of a detected face.

Troubleshooting
If you encounter any issues or errors while running the script, please ensure that you have the required dependencies installed and that your camera is properly connected.

Author:
Atharva Kulkarni