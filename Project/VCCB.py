import cv2 #OpenCV
import numpy as np #numpy needed for OpenCV
import time #Testing purpose

import threading

import Compare


class VidCapture:
    def __init__(self, video_source=0):
        self.name = "WebcamFeed" #Name of Capture.

        self.point1 = () #Defining variables needed to draw rectangle.
        self.point2 = ()
        self.drawing = False
        self.drawingfinish = False #Flag to limit drawing of rectangle to once until reset.

        self.takepicture = False

        #self.n = 0

        self.setupfinish = False
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0

        self.vid=cv2.VideoCapture(video_source) #Opens the webcam and mounts it.
        cv2.namedWindow(self.name) #Opens a cv2 window.

        

    def showFrame(self): #Function to show Frame. Always in a While True loop.
        ret, frame = self.vid.read()
        if self.point1 and self.point2:
            cv2.rectangle(frame, self.point1, self.point2, (255,255,255)) #Draw Rectangle

            self.xlength = abs(self.point1[0] - self.point2[0])
            self.ylength = abs(self.point1[1] - self.point2[1])
            self.thirdx = int(self.xlength/3)
            self.thirdy = int(self.ylength/3)
            
            self.a = self.point1[0]+self.thirdx
            self.b = self.point2[0]-self.thirdx
            self.c = self.point1[1]+self.thirdy
            self.d = self.point2[1]-self.thirdy

            cv2.line(frame, (self.a, self.point1[1]), (self.a, self.point2[1]), (255,255,255))
            cv2.line(frame, (self.b, self.point1[1]), (self.b, self.point2[1]), (255,255,255))
            cv2.line(frame, (self.point1[0], self.c), (self.point2[0], self.c), (255,255,255))
            cv2.line(frame, (self.point1[0], self.d), (self.point2[0], self.d), (255,255,255)) #Splits into 3x3 grid

        if self.takepicture: #Save Control picture when Yes is pressed.
            filename = "Control_picture.jpg"
            cv2.imwrite(filename, frame)
            self.takepicture = not self.takepicture

        if self.drawingfinish and self.setupfinish:
            #self.n = self.n + 1
            #print("debug")

            self.frameCrop1 = frame[self.point1[1] + 1:self.c, self.a + 1:self.b]
            #cropname1 = "one " + str(self.n) + ".jpg"
            #cv2.imwrite(cropname1, self.frameCrop1)

            self.frameCrop2 = frame[self.c + 1:self.d, self.b + 1:self.point2[0]]
            #cropname2 = "two " + str(self.n) + ".jpg"
            #cv2.imwrite(cropname2, self.frameCrop2)

            self.frameCrop3 = frame[self.d + 1:self.point2[1], self.a + 1:self.b]
            #cropname3 = "three " + str(self.n) + ".jpg"
            #cv2.imwrite(cropname3, self.frameCrop3)

            self.frameCrop4 = frame[self.c + 1:self.d, self.point1[0] + 1:self.a]
            #cropname4 = "four " + str(self.n) + ".jpg"
            #cv2.imwrite(cropname4, self.frameCrop4)

            self.one = Compare.ssim(self.imCrop1, self.frameCrop1)
            #print("one: " + str(self.one))

            self.two = Compare.ssim(self.imCrop2, self.frameCrop2)
            #print("two: " + str(self.two))

            self.three = Compare.ssim(self.imCrop3, self.frameCrop3)
            #print("three: " + str(self.three))

            self.four = Compare.ssim(self.imCrop4, self.frameCrop4)
            #print("four: " + str(self.four))








        cv2.imshow(self.name, frame)
   
    def Click(self, event, x, y, flags, param): #Function that happens on MouseCallback.
        global point1, point2, drawing, drawingcounter
        if self.drawingfinish is False:
            if event == cv2.EVENT_LBUTTONDOWN:
                if self.drawing is False:
                    self.drawing = True
                    self.point1 = (x,y)
                else:
                    self.drawing = False
                    self.drawingfinish = True
            elif event == cv2.EVENT_MOUSEMOVE:
                if self.drawing is True:
                    self.point2 = (x,y)
        if event == cv2.EVENT_RBUTTONDOWN: #Testing purpose since no GUI.
            self.Reset()
            self.TakePicture()        

    def Reset(self): #Resets 3x3 grid and flag.
        global point1, point2, drawingcounter
        self.point1 = ()
        self.point2 = ()
        self.drawingfinish = False

    def Resetout():
        self.Reset()

    def LeftCornerUp(self):
        global point1
        self.point1 = (self.point1[0], self.point1[1] - 1)
    def LeftCornerDown(self):
        global point1
        self.point1 = (self.point1[0], self.point1[1] + 1)
    def LeftCornerLeft(self):
        global point1
        self.point1 = (self.point1[0] - 1, self.point1[1])
    def LeftCornerRight(self):
        global point1
        self.point1 = (self.point1[0] + 1, self.point1[1])
    def RightCornerUp(self):
        global point2
        self.point2 = (self.point2[0], self.point2[1] - 1)
    def RightCornerDown(self):
        global point2
        self.point2 = (self.point2[0], self.point2[1] + 1)
    def RightCornerLeft(self):
        global point2
        self.point2 = (self.point2[0] - 1, self.point2[1])
    def RightCornerRight(self):
        global point2
        self.point2 = (self.point2[0] + 1, self.point2[1])     

    def TakePicture(self):
        self.takepicture = not self.takepicture

    def CropControl(self):
        #start = time.time()

        im = cv2.imread("Control_picture.jpg")
        #cv2.imshow("Image", im)

        self.imCrop1 = im[self.point1[1] + 1:self.c, self.a + 1:self.b]
        #cv2.imshow("ImageCrop1", self.imCrop1)

        self.imCrop2 = im[self.c + 1:self.d, self.b + 1:self.point2[0]]
        #cv2.imshow("ImageCrop2", self.imCrop2)

        self.imCrop3 = im[self.d + 1:self.point2[1], self.a + 1:self.b]
        #cv2.imshow("ImageCrop3", self.imCrop3)

        self.imCrop4 = im[self.c + 1:self.d, self.point1[0] + 1:self.a]
        #cv2.imshow("ImageCrop4", self.imCrop4)

        #end = time.time()
        #print(end - start)

    def SetupFinishBool(self): #have boolean as flag when setup is finished.
        print("...")
        self.setupfinish = True    

               
def main():
    global camerafeed
    cameraFeed = VidCapture() 
    cv2.setMouseCallback(cameraFeed.name, cameraFeed.Click)
    global close
    close = False 
    while(True):
        cameraFeed.showFrame()
        if cv2.waitKey(20) == 27: #Press esc to exit.
                break
        if close:
            close = not close
            break    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
