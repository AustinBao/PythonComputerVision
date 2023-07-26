import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    frame = cv2.flip(frame, 1)

    cv2.imshow("Video", frame)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()