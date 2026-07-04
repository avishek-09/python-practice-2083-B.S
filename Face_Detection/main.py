import cv2 as cv
import os
from datetime import datetime

DIR = "students"
os.makedirs(DIR, exist_ok=True)


camera = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)


while True:
    ret, frame = camera.read()
    if not ret:
        print("camera not found.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=7, minSize=(30, 30)
    )

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv.putText(frame, current_time, (20,40), cv.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0),1)

    # print(faces)
    for x, y, w, h in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow("Camera", frame)

    key = cv.waitKey(1)

    if key == ord("q"):
        break
    elif key == ord("s") and len(faces) > 0:
        name = input("Enter Student Name: ")
        if name:
            x, y, w, h = faces[0]
            face = gray[y : y + h, x : x + h]
            face = cv.resize(face, (200, 200))
            file_name = os.path.join(DIR, f"{name}.jpg")
            cv.imwrite(file_name, face)
camera.release()
cv.destroyAllWindows()
