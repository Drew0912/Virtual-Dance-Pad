import cv2
import numpy as np

def listWebcam():
    index = 0 #Camera index
    arr = [] #List
    while True:
        cap = cv2.VideoCapture(index) #Import webcam with selected index.
        if not cap.read()[0]: #If selected webcam cannot be opened.
            break
        else:
            arr.append(index) #Add index to list.
        cap.release() #Releases the selected webcam.
        index += 1 #Increases index.
    return arr

def main():
    print(listWebcam())    

if __name__ == "__main__":
    main()    
