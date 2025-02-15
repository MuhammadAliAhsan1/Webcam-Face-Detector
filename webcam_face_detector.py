import cv2
from random import randrange

snippet = r"C:\Users\DELL\Desktop\CodeForExe's\haarcascade_frontalface_default.xml"
trained_face_data = cv2.CascadeClassifier(snippet)

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()

    grayscaled_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    coordinates = trained_face_data.detectMultiScale(grayscaled_video)

    for (x, y, w, h) in coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 3)

    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
webcam.release()

print("Code Completed")