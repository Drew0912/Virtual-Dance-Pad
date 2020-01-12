import cv2 #Imports OpenCV
import numpy as np #Numpy is needed for OpenCV

Video_Source = 0 #Webcam Index
vid = cv2.VideoCapture(Video_Source) #Gets the webcam and puts it under the name vid

while (True): #Infinite loop.
    ret, frame = vid.read() #Gets data from webcam
    cv2.imshow("WebcamFeed", frame) #Creates window called WebcamFeed and displays frame from webcam.
    if cv2.waitKey(20) == 27: #Press esc to close window.
        break
cv2.destroyAllWindows() #Closes all OpenCV Windows.