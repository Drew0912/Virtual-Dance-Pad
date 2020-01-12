import cv2 #Imports OpenCV.
import numpy as np #Numpy is needed for OpenCV.

class VidCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source) #Gets the webcam and puts it under the name vid.

    def showFrame(self):
        ret, frame = self.vid.read() #Gets data from webcam.
        cv2.imshow("WebcamFeed", frame) #Creates window called WebcamFeed and displays frame from webcam.

def main():
    cameraFeed = VidCapture() #Creates instance of VidCapture called cameraFeed.
    while (True): #Infinite loop.
        cameraFeed.showFrame() #Runs the showFrame function in VidCapture class.
        if cv2.waitKey(20) == 27: #Press esc to close window.
            break
    cv2.destroyAllWindows() #Closes all OpenCV Windows.

if __name__ == "__main__":
    main()