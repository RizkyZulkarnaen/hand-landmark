import pyautogui
import time
import cv2
import autopy

screen_width, screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)
cap.set(3, screen_width)
cap.set(4, screen_height)

while cap.isOpened():
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
