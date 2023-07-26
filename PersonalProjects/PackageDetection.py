import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    flipped_frame = cv2.flip(frame, 1)

    gray_frame = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)
    ret, thresh_frame = cv2.threshold(gray_frame, 220, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        if i == 0:
            continue
    
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        cv2.drawContours(frame, contour, 0, (0,0,0), 4)
        x, y, w, h= cv2.boundingRect(approx)

        x_mid = int(x + (w/3)) 
        y_mid = int(y + (h/1.5)) 

        coords = (x_mid, y_mid)
        colour = (0, 0, 0)
        font = cv2.FONT_HERSHEY_DUPLEX

        if len(approx) == 3:
            cv2.putText(thresh_frame, "Triangle", coords, font, 1, colour, 1)
        elif len(approx) == 4:
            cv2.putText(thresh_frame, "Quadrilateral", coords, font, 1, colour, 1)
        elif len(approx) == 5:
            cv2.putText(thresh_frame, "Pentagon", coords, font, 1, colour, 1)
        elif len(approx) == 6:
            cv2.putText(thresh_frame, "Hexagon", coords, font, 1, colour, 1)
        else:
            cv2.putText(thresh_frame, "Circle", coords, font, 1, colour, 1)

    cv2.imshow("Video", thresh_frame)

    if cv2.waitKey(100) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()