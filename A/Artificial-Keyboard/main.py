
import cv2
import mediapipe as mp
import numpy as np
from time import sleep
import keyboard
from pynput.keyboard import Controller

kb=Controller()
keys=[['Q','W','E','R','T','Y','U','I','O','P'],
      ['A','S','D','F','G','H','J','K','L',';'],
      ['Z','X','C','V','B','N','M',',','.','/']]


text=''
def draw_all(img, button_list1, hand_landmarks_list,text_):
    for button in button_list1:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 6, y + 43), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 4)

    if hand_landmarks_list:
        for hand_landmarks in hand_landmarks_list:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
            thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            x, y = int(index_finger_tip.x * img.shape[1]), int(index_finger_tip.y * img.shape[0])
            x1, y1 = int(index_finger_mcp.x * img.shape[1]), int(index_finger_mcp.y * img.shape[0])
            x2, y2 = int(thumb_ip.x * img.shape[1]), int(thumb_ip.y * img.shape[0])
            l=np.sqrt(((x2-x1)**2)+((y2-y1)**2))
            for button in button_list1:
                bx, by = button.pos
                bw, bh = button.size
                if bx < x < bx + bw and by < y < by + bh:
                    cv2.rectangle(img, (bx, by), (bx + bw, by + bh), (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (bx + 6, by + 43), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 4)
                    if l <25:
                        text_+=button.text
                        kb.press(button.text)
                        cv2.rectangle(img, (bx, by), (bx + bw, by + bh), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (bx + 6, by + 43), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255),4)
                        sleep(.2)
                    break
    return text_

class Button():
    def __init__(self,pos,text,size=[50,50]):
        self.pos=pos
        self.text=text
        self.size=size





button_list=[]
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        button_list.append(Button([70*j+50, 70*i+50], key))


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Initialize MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3,1200) # Width
cap.set(4,720) # Height
while cap.isOpened():
    # Read frames from webcam
    success, image = cap.read()
    image=cv2.flip(image,180)
    # Convert image to RGB and process with MediaPipe Hands
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    # Extract hand landmarks if detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks and connections on image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    text=draw_all(image, button_list, results.multi_hand_landmarks,text)
    # cv2.rectangle(image,(50,300),(500,380),(255,0,0),cv2.FILLED)
    # cv2.putText(image,text,(50,360),cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 4)
    # Display image with hand landmarks
    cv2.imshow("Hand Detection", image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break



# Release resources
hands.close()
cap.release()
cv2.destroyAllWindows()
