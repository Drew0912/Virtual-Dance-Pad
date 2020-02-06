import cv2 #Imports OpenCV.
import numpy as np #Numpy is needed for OpenCV.

class VidCapture:
    def __init__(self, video_source=0):
        self.Name = "WebcamFeed" #Name for OpenCV Window.

        self.point1 = () #Tuple for first coordinate.
        self.point2 = () #Tuple for second coordinate.
        self.drawing = False #Boolean to know if user is drawing the rectangle.
        self.drawingfinish = False

        self.takepicture = False #Boolean flag for if picture is taken.

        self.setupfinish = False #Boolean flag for if setup is finished.

        self.vid = cv2.VideoCapture(video_source) #Gets the webcam and puts it under the name vid.
        cv2.namedWindow(self.Name) #Initialises an OpenCV Window

    def showFrame(self):
        ret, frame = self.vid.read() #Gets data from webcam.
        if self.point1 and self.point2:
            cv2.rectangle(frame, self.point1, self.point2, (255,255,255)) #Draws Rectangle, colour white.

            self.xlength = abs(self.point1[0] - self.point2[0]) #Horizontal Length
            self.ylength = abs(self.point1[1] - self.point2[1]) #Vertical Length
            self.thirdx = int(self.xlength/3) #Horizontal Length divided by 3
            self.thirdy = int(self.ylength/3) #Vertical Length divided by 3

            self.a = self.point1[0]+self.thirdx
            self.b = self.point2[0]-self.thirdx
            self.c = self.point1[1]+self.thirdy
            self.d = self.point2[1]-self.thirdy

            cv2.line(frame, (self.a, self.point1[1]), (self.a, self.point2[1]), (255,255,255)) #Line from point 1 to 6
            cv2.line(frame, (self.b, self.point1[1]), (self.b, self.point2[1]), (255,255,255)) #Line from point 2 to 5
            cv2.line(frame, (self.point1[0], self.c), (self.point2[0], self.c), (255,255,255)) #Line from point 8 to 3
            cv2.line(frame, (self.point1[0], self.d), (self.point2[0], self.d), (255,255,255)) #Line from point 7 to 4

        if self.takepicture: #Save Control picture when Take picture is pressed.
            filename = "Control_picture.jpg"
            cv2.imwrite(filename, frame)
            self.takepicture = not self.takepicture    

        cv2.imshow(self.Name, frame) #Creates window called WebcamFeed and displays frame from webcam.

    def Click(self, event, x, y, flags, param): #Function that happens on MouseCallback.
        global point1, point2, drawing, drawingfinish
        if self.drawingfinish == False:
            if event == cv2.EVENT_LBUTTONDOWN:
                if self.drawing is False:
                    self.point1 = (x,y)
                    self.drawing = True
                elif self.drawing is True:
                    if x > self.point1[0] and y > self.point1[1]:
                        self.drawing = False
                        self.drawingfinish = True
            elif event == cv2.EVENT_MOUSEMOVE:
                if self.drawing == True:
                    if x > self.point1[0] and y > self.point1[1]:
                        self.point2 = (x,y)
        if event == cv2.EVENT_RBUTTONDOWN: #Temp Function.
            self.Reset()

    def Reset(self): #Reset Rectangle and allow drawing again.
        global point1, point2, drawing, drawingfinish
        self.point1 = ()
        self.point2 = ()
        self.drawing = False
        self.drawingfinish = False

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

    def CropControl(self): #Crop Control Picture.
        im = cv2.imread("Control_picture.jpg") #Imports control picture.

        self.imCrop1 = im[self.point1[1] + 1:self.c, self.a + 1:self.b]
        #cv2.imshow("ImageCrop1", self.imCrop1)

        self.imCrop2 = im[self.c + 1:self.d, self.b + 1:self.point2[0]]
        #cv2.imshow("ImageCrop2", self.imCrop2)

        self.imCrop3 = im[self.d + 1:self.point2[1], self.a + 1:self.b]
        #cv2.imshow("ImageCrop3", self.imCrop3)

        self.imCrop4 = im[self.c + 1:self.d, self.point1[0] + 1:self.a]
        #cv2.imshow("ImageCrop4", self.imCrop4)

    def SetupFinishBool(self): #Boolean Flag.
        self.setupfinish = True                             

def main():
    cameraFeed = VidCapture() #Creates instance of VidCapture called cameraFeed.
    cv2.setMouseCallback(cameraFeed.Name, cameraFeed.Click) #Sets mouse handler for cameraFeed window
    while(True): #Infinite loop.
        cameraFeed.showFrame() #Runs the showFrame function in VidCapture class.
        if cv2.waitKey(20) == 27: #Press esc to close window.
            break
    cv2.destroyAllWindows() #Closes all OpenCV Windows.

if __name__ == "__main__":
    main()