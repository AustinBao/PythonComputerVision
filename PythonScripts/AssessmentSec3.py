import cv2
import numpy as np

# Functions
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255), 10)

        
# Create IMG
img = cv2.imread("../DATA/dog_backpack.jpg")

cv2.namedWindow(winname='dog')

cv2.setMouseCallback('dog',draw_circle)


# Stay Open
while True: 
    cv2.imshow('dog',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

