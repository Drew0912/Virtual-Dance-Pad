import cv2 #OpenCV
import numpy as np #numpy needed for OpenCV


class VidCapture:
    def __init__(self, video_source=0):
        self.name = "WebcamFeed" #Name of Capture.

        self.point1 = () #Defining variables needed to draw rectangle.
        self.point2 = ()
        self.drawing = False
        self.drawingfinish = False #Flag to limit drawing of rectangle to once until reset.

        self.vid=cv2.VideoCapture(video_source) #Opens the webcam and mounts it.
        cv2.namedWindow(self.name) #Opens a cv2 window.

    def showFrame(self): #Function to show Frame.
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
