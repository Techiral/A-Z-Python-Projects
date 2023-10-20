from flask import Flask, render_template,Response
from camera import Video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame +
                b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


# import os
# os.environ["CUDA_VISIBLE_DEVICES"]= "-1"
# import cv2
# from deepface import DeepFace

# face_classifier = cv2.CascadeClassifier()
# face_classifier.load(cv2.samples.findFile("haarcascade_frontalface_default.xml"))

# cap = cv2.VideoCapture(0)

# while True:
    
#     ret, frame = cap.read()
#     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(frame_gray)
    
#     response = DeepFace.analyze(frame, actions=("emotion",), enforce_detection=False)
#     for face in faces:
#         x,y,w,h = face
        
#         cv2.rectangle(frame, (x+10,y+10), (x+w,y+h), color= (238,130,238), thickness=4)
#         cv2.putText(frame, response["dominant_emotion"].upper(), org=(x,y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
#             fontScale=1.2, color=(255,204,153),thickness=4)
#         cv2.imshow("", frame)
#         if(cv2.waitKey(30)==27):
#             break
# cap.release()
# cv2.destroyAllWindows()