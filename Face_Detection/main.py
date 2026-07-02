import cv2 as cv

camera = cv.VideoCapture(0)  ## this specifies which camera to use of the laptop - 0 means default camera

while True: 
    ret, frame = camera.read()
    if not ret:
        print("Camera not accessed.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("Camera", gray)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindow()