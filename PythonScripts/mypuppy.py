import cv2 

img = cv2.imread('Computer-Vision-with-Python/DATA/00-puppy.jpg')


while True: 
    cv2.imshow('Puppy', img)
    
    # if we waited at least 1 millisecond AND we have pressed the esc key.
    if cv2.waitKey(1) & 0xFF == 27: 
        #can also have 0xFF == ord('*insert key from keybaord') to specify the key to close the window.
        break

cv2.destroyAllWindows()