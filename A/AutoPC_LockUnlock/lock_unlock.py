import pyautogui
import time
pyautogui.FAILSAFE=False
import threading
import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Connect to the laptop's camera
camera = cv2.VideoCapture(0)  # Use 0 for the default camera; try different indices if multiple cameras are available
counter = 0
counter2 = 0
locked = False

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        counter += 1
        print("Empty")
        print(counter)
        if counter == 100:
            # Automate the lock screen process
            pyautogui.hotkey('win', 'r')
            pyautogui.typewrite("cmd\n")
            time.sleep(0.5)
            pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")
            locked = True

    else:
        counter = 0
        print("BACK IN FRONT OF CAMERA")
        if locked:
            print("Locked condition in front of camera")
            counter2 += 1
            if counter2 == 50:
                # Automate the unlock screen process
                pyautogui.press('space')
                time.sleep(1)
                pyautogui.press('space')
               
                counter2 = 0
                locked = False
                print(counter2)
                
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
