import cv2 #Imports OpenCV
import numpy as np #Numpy is needed for OpenCV

Video_Source = 0
vid = cv2.VideoCapture(Video_Source)

while (True):
    ret, frame = vid.read()
    cv2.imshow("WebcamFeed", frame)
    if cv2.waitKey(20) == 27: #Press esc to close window.
        break
cv2.destroyAllWindows()