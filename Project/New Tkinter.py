import tkinter as tk
from tkinter import ttk
import webbrowser, os
import cv2

import VCCB
import threading

from PIL import Image, ImageTk

import time

from tkinter import StringVar #String Variable for Entry widget.

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Main")
        self.master.resizable(0,0)

        self.WebcamOpen = False #Bool so Calibration can only be opened when webcam is open.

        def StartStop(): #Add code to start program as controller (macros?).
            if self.StartStopButton["text"] == "Start":
                self.StartStopButton["text"] = "Stop"
            else:
                self.StartStopButton["text"] = "Start"
        
        def Help():
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def CalibrationWindow(): #Update to use new Main Calibration window
            if self.WebcamOpen:
                self.newwindow = tk.Toplevel(self.master)
                self.app = MainCalibration(self.newwindow)
            else:
                self.Message["text"] = "Open Webcam first."


        def Webcam():
            self.WebcamOpen = True
            global cameraFeed
            cameraFeed = VCCB.VidCapture() 
            cv2.setMouseCallback(cameraFeed.name, cameraFeed.Click)
            global close
            close = False 
            while(True):
                cameraFeed.showFrame()
                if cv2.waitKey(20) == 27: #Press esc to exit.
                    break
                if close:
                    close = not close
                    self.WebcamOpen = not self.WebcamOpen
                    break    
            cv2.destroyAllWindows()

        def WebcamClick(): #Function to load Webcam function.
            if self.DisplayButton["text"] == "Open Webcam":
                T1.start()
                self.DisplayButton["text"] = "Close Webcam. \n Requires restart after close."
            else:
                global close
                close = not close
                self.DisplayButton["text"] = "Restart program to open Webcam"
                          
        #Threading
        T1 = threading.Thread(target=Webcam) #thread for OpenCV
        T1.daemon = True #Close Webcam if GUi is closed
        
        self.WebcamSelect = ttk.Combobox(master, width=30, state='readonly',
                                         values=[
                                             "Select which Webcam:",
                                             "0",
                                             "1",
                                             "2",
                                             "3",])
        self.WebcamSelect.grid(row=0, column=0, columnspan=2, pady=(20,10))
        self.WebcamSelect.current(0)
        self.Message = tk.Label(master, text="") #Error message.
        self.Message.grid(row=1, column=0, columnspan=2)
        self.DisplayButton = tk.Button(master, text="Open Webcam", width=30, height=5, command=WebcamClick)
        self.DisplayButton.grid(row=2, column=0, columnspan=2)
        self.StartStopButton = tk.Button(master, text="Start", width=30, height=5, command=StartStop)
        self.StartStopButton.grid(row=4, column=0, columnspan=2,
                                  sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20), padx=10)
        self.HelpButton = tk.Button(master, text="Help", height=5, command=Help)
        self.HelpButton.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10))
        self.CalibrateButton = tk.Button(master, text="Calibrate/Setup", height=5, command=CalibrationWindow)
        self.CalibrateButton.grid(row=3, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=(10,0))

        self.master.mainloop()

class MainCalibration:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Calibration")
        self.root.resizable(0,0)

        self.Label = tk.Label(root, text="Go through Setup before pressing any other button.")
        self.Label.grid(row=0, column=0, columnspan=2, pady=(5,10), padx=10)

        def Setup():
            self.SetupWindow = tk.Toplevel(self.root)
            self.Setup = Calibration(self.SetupWindow)

        def Help():
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def Finish():
            self.root.destroy()
            self.root.update() #???

        def ConfigureWindow():
            self.ConfigureWindow = tk.Toplevel(self.root)
            self.Configure = Configure(self.ConfigureWindow)

        def SensitivityWindow():
            self.SensitivityWindow = tk.Toplevel(self.root)
            self.Sensitivity = Sensitivity(self.SensitivityWindow)

        def Debug():
            print(cameraFeed.one)    
 

        self.debugButton = tk.Button(root, text="Debug", command=Debug)
        self.debugButton.grid(row=1, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)    

        self.ConfigureButton = tk.Button(root, text="Configure", width=15, height=5, command=ConfigureWindow)
        self.ConfigureButton.grid(row=1, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.SensitivityButton = tk.Button(root, text="Sensitivity", width=15, height=5, command=SensitivityWindow)
        self.SensitivityButton.grid(row=2, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)   
        self.SetupButton = tk.Button(root, text="Setup", width=15, height=5, command=Setup)
        self.SetupButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.FinishButton = tk.Button(root, text="Finish", width=15, height=5, command=Finish)
        self.FinishButton.grid(row=3, column=0, padx=(10,0), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)
        self.HelpButton = tk.Button(root, text="Help", width=15, height=5, command=Help)
        self.HelpButton.grid(row=3, column=1, padx=(0,10), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)     
                
class Calibration:
    def __init__(self, root):
        self.root = root
        self.root.title("Calibration/Setup")
        self.root.resizable(0,0)

        def Back():
            self.root.destroy()
            self.root.update() #???

        def Help():
            url = 'file://' + os.path.realpath('index.html') #change url
            webbrowser.open(url)

        def OpenAdjust():
            self.AdjustWindow = tk.Toplevel(self.root)
            self.Adjust = Adjust(self.AdjustWindow)

        def Reset():
            cameraFeed.Reset() #IDK Code, works

        def Next():
            self.ControlWindow = tk.Toplevel(self.root)
            self.Control = ControlPictureWindow(self.ControlWindow)    
    

        self.Label = tk.Label(root, text="Click on the webcam feed to create 2 corners. \n One in the top left and the other in the botton right of where you want the 3x3 grid.")
        self.Label.grid(row=0, column=0, columnspan=2, pady=(5,0))
        self.AdjustButton = tk.Button(root, text="Adjust", width=15, height=5, command=OpenAdjust)
        self.AdjustButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S, pady=(20,0))
        self.ResetButton = tk.Button(root, text="Reset", width=15, height=5, command=Reset)
        self.ResetButton.grid(row=3, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)
        self.BackButton = tk.Button(root, text="Back", command=Back, width=15, height=5)
        self.BackButton.grid(row=3, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.NextButton = tk.Button(root, text="Next", width=15, height=5, command=Next)
        self.NextButton.grid(row=4, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20))
        self.HelpButton = tk.Button(root, text="Help", command=Help, width=15, height=5)
        self.HelpButton.grid(row=4, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20))

        self.root.mainloop()

class Adjust:
    def __init__(self, root):
        self.root = root
        self.root.title("Adjust")
        self.root.resizable(0,0)

        def Help():
            url = 'file://' + os.path.realpath('index.html') #change url
            webbrowser.open(url)

        def Back():
            self.root.destroy()
            self.root.update() #???

        def LeftCornerUp():
            cameraFeed.LeftCornerUp()
        def LeftCornerDown():
            cameraFeed.LeftCornerDown()
        def LeftCornerRight():
            cameraFeed.LeftCornerRight()
        def LeftCornerLeft():
            cameraFeed.LeftCornerLeft()
        def RightCornerUp():
            cameraFeed.RightCornerUp()
        def RightCornerDown():
            cameraFeed.RightCornerDown()
        def RightCornerRight():
            cameraFeed.RightCornerRight()
        def RightCornerLeft():
            cameraFeed.RightCornerLeft()                        

        self.FirstLabel = tk.Label(root, text="Top Left Corner:")
        self.FirstLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.S)

        self.LeftIncreaseY = tk.Button(root, text="UP", width=12, height=3, command=LeftCornerUp)
        self.LeftIncreaseY.grid(row=1, column=0, padx=(10,0))
        self.LeftDecreaseY = tk.Button(root, text="DOWN", width=12, height=3, command=LeftCornerDown)
        self.LeftDecreaseY.grid(row=1, column=1)
        self.LeftIncreaseX = tk.Button(root, text="RIGHT", width=12, height=3, command=LeftCornerRight)
        self.LeftIncreaseX.grid(row=1, column=2)
        self.LeftDecreaseX = tk.Button(root, text="LEFT", width=12, height=3, command=LeftCornerLeft)
        self.LeftDecreaseX.grid(row=1, column=3, padx=(0,10))

        self.SecondLabel = tk.Label(root, text="Bottom Right Corner:")
        self.SecondLabel.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.S)

        self.RightIncreaseY = tk.Button(root, text="UP", width=12, height=3, command=RightCornerUp)
        self.RightIncreaseY.grid(row=3, column=0, padx=(10,0))
        self.RightDecreaseY = tk.Button(root, text="DOWN", width=12, height=3, command=RightCornerDown)
        self.RightDecreaseY.grid(row=3, column=1)
        self.RightIncreaseX = tk.Button(root, text="RIGHT", width=12, height=3, command=RightCornerRight)
        self.RightIncreaseX.grid(row=3, column=2)
        self.RightDecreaseX = tk.Button(root, text="LEFT", width=12, height=3, command=RightCornerLeft)
        self.RightDecreaseX.grid(row=3, column=3, padx=(0,10))

        self.ResetMessage = tk.Label(root, text="Press the reset button to remove the 3x3 grid.")
        self.ResetMessage.grid(row=4, column=0, columnspan=4, pady=(10,0))

        self.HelpButton = tk.Button(root, text="Help", width=12, height=3, command=Help)
        self.HelpButton.grid(row=5, column=2, pady=10)
        self.BackButton = tk.Button(root, text="Back", width=12, height=3, command=Back)
        self.BackButton.grid(row=5, column=3, pady=10, padx=(0,10))

class ControlPictureWindow:
    def __init__ (self, root):
        self.root = root
        self.root.title("Control Picture")
        self.root.resizable(0,0)


        def Back():
            self.root.destroy()
            self.root.update() #???

        def Help():
            url = 'file://' + os.path.realpath('index.html') #change url
            webbrowser.open(url)

        def TakePicture():
            cameraFeed.TakePicture()

            time.sleep(2) #Delay to save photo before displaying   
            self.ConfirmWindow = tk.Toplevel(self.root)
            self.Confirm = ControlPictureConfirmWindow(self.ConfirmWindow)        

        self.Label = tk.Label(root, text="Makes sure that the image displayed on the webcam feed\n is clear and that the user is standing on the center box of the 3x3 grid.")
        self.Label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        self.BackButton = tk.Button(root, text="Back", width=15, height=5, command=Back)
        self.BackButton.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,20))
        self.HelpButton = tk.Button(root, text="Help", width=15, height=5, command=Help)
        self.HelpButton.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,20), pady=(0,20))
        self.TakePictureButton = tk.Button(root, text="Take Picture", width=15, height=5, command=TakePicture)
        self.TakePictureButton.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=(20,0), pady=(0,20))

class ControlPictureConfirmWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Confirm")
        self.root.resizable(0,0)

        self.img = ImageTk.PhotoImage(Image.open("Control_picture.jpg"))

        self.panel = tk.Label(root, image = self.img)
        self.panel.image = self.img
        self.panel.grid(row=0, column=0, rowspan=4)

        def Help():
            url = 'file://' + os.path.realpath('index.html') #change url
            webbrowser.open(url)

        def Retake():
            self.root.destroy()
            self.root.update() #???

        def Yes():
            self.TextLabel["text"] = "Close all windows but Main Calibration and Main Window"
            cameraFeed.CropControl()
            cameraFeed.SetupFinishBool()
   
            
        self.TextLabel = tk.Label(root, text="")
        self.TextLabel.grid(row=0, column=1, columnspan=2)    
        self.Label = tk.Label(root, text="Is this Control picture suitable?")
        self.Label.grid(row=1, column=1, columnspan=2)
        self.RetakeButton = tk.Button(root, text="Retake", width=15, height=5, command=Retake)
        self.RetakeButton.grid(row=2, column=2)
        self.YesButton = tk.Button(root, text="Yes", width=15, height=5, command=Yes)
        self.YesButton.grid(row=3, column=1)
        self.HelpButton = tk.Button(root, text="Help", width=15, height=5, command=Help)
        self.HelpButton.grid(row=3, column=2)

class Configure:
    def __init__(self, root):
        self.root = root
        self.root.title("Configure")
        self.root.resizable(0,0)

        self.FrontLabel = tk.Label(root, text="Front:")
        self.FrontLabel.grid(row=0, column=0)
        self.FrontSelect = ttk.Combobox(root, width=15, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.FrontSelect.grid(row=1, column=0)
        self.FrontSelect.current(0)

        self.RightLabel = tk.Label(root, text="Right:")
        self.RightLabel.grid(row=0, column=1)
        self.RightSelect = ttk.Combobox(root, width=15, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.RightSelect.grid(row=1, column=1)
        self.RightSelect.current(1)

        self.LeftLabel = tk.Label(root, text="Left:")
        self.LeftLabel.grid(row=2, column=0)
        self.LeftSelect = ttk.Combobox(root, width=15, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.LeftSelect.grid(row=3, column=0)
        self.LeftSelect.current(2)

        self.BackLabel = tk.Label(root, text="Back:")
        self.BackLabel.grid(row=2, column=1)
        self.BackSelect = ttk.Combobox(root, width=15, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.BackSelect.grid(row=3, column=1)
        self.BackSelect.current(3)

class Sensitivity:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensitivity")
        self.root.resizable(0,0)

        self.BoxLabel = tk.Label(root, text="Box:")
        self.BoxLabel.grid(row=0, column=0)

        self.OneLabel = tk.Label(root, text="One")
        self.OneLabel.grid(row=0, column=1)
        self.TwoLabel = tk.Label(root, text="Two")
        self.TwoLabel.grid(row=0, column=2)
        self.ThreeLabel = tk.Label(root, text="Three")
        self.ThreeLabel.grid(row=0, column=3)
        self.FourLabel = tk.Label(root, text="Four")
        self.FourLabel.grid(row=0, column=4)

        #self.text = StringVar()
        #self.text.set("...") #String variable for text

        def UpdateOne():
            self.DetectionOneLabel.config(text=str(cameraFeed.one))
            self.DetectionOneLabel.after(500,UpdateOne)

        def UpdateTwo():
            self.DetectionTwoLabel.config(text=str(cameraFeed.two))
            self.DetectionTwoLabel.after(500,UpdateTwo)

        def UpdateThree():
            self.DetectionThreeLabel.config(text=str(cameraFeed.three))
            self.DetectionThreeLabel.after(500,UpdateThree)

        def UpdateFour():
            self.DetectionFourLabel.config(text=str(cameraFeed.four))
            self.DetectionFourLabel.after(500,UpdateFour)            


        self.DetectionLabel = tk.Label(root, text="Detection Value:")
        self.DetectionLabel.grid(row=1, column=0)

        self.DetectionOneLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionOneLabel.grid(row=1, column=1)
        self.DetectionTwoLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionTwoLabel.grid(row=1, column=2)
        self.DetectionThreeLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionThreeLabel.grid(row=1, column=3)
        self.DetectionFourLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionFourLabel.grid(row=1, column=4)

        #self.DetectionOneLabel["text"] = str(cameraFeed.one)
        #self.text.set(str(cameraFeed.one))

        self.UpperLimitLabel = tk.Label(root, text="Upper Limit:")
        self.UpperLimitLabel.grid(row=2, column=0)

        self.UpperOneEntryText = StringVar()
        self.UpperOneEntry = tk.Entry(root, textvariable=self.UpperOneEntryText)
        self.UpperOneEntryText.set("1")
        self.UpperOneEntry.grid(row=2, column=1)
        self.UpperTwoEntryText = StringVar()
        self.UpperTwoEntry = tk.Entry(root, textvariable=self.UpperTwoEntryText)
        self.UpperTwoEntryText.set("2")
        self.UpperTwoEntry.grid(row=2, column=2)
        self.UpperThreeEntryText = StringVar()
        self.UpperThreeEntry = tk.Entry(root, textvariable=self.UpperThreeEntryText)
        self.UpperThreeEntryText.set("3")
        self.UpperThreeEntry.grid(row=2, column=3)
        self.UpperFourEntryText = StringVar()
        self.UpperFourEntry = tk.Entry(root, textvariable=self.UpperFourEntryText)
        self.UpperFourEntryText.set("4")
        self.UpperFourEntry.grid(row=2, column=4)

        self.LowerLimitLabel = tk.Label(root, text="Lower Limit:")
        self.LowerLimitLabel.grid(row=3, column=0)

        self.LowerOneEntryText = StringVar()
        self.LowerOneEntry = tk.Entry(root, textvariable=self.LowerOneEntryText)
        self.LowerOneEntryText.set("1")
        self.LowerOneEntry.grid(row=3, column=1)
        self.LowerTwoEntryText = StringVar()
        self.LowerTwoEntry = tk.Entry(root, textvariable=self.LowerTwoEntryText)
        self.LowerTwoEntryText.set("2")
        self.LowerTwoEntry.grid(row=3, column=2)
        self.LowerThreeEntryText = StringVar()
        self.LowerThreeEntry = tk.Entry(root, textvariable=self.LowerThreeEntryText)
        self.LowerThreeEntryText.set("3")
        self.LowerThreeEntry.grid(row=3, column=3)
        self.LowerFourEntryText = StringVar()
        self.LowerFourEntry = tk.Entry(root, textvariable=self.LowerFourEntryText)
        self.LowerFourEntryText.set("4")
        self.LowerFourEntry.grid(row=3, column=4)

        self.DetectionOneLabel.after(500,UpdateOne)
        self.DetectionTwoLabel.after(500,UpdateTwo)
        self.DetectionThreeLabel.after(500,UpdateThree)
        self.DetectionFourLabel.after(500,UpdateFour)

        self.root.mainloop()


def main():
    root = tk.Tk()
    app = MainWindow(root)
    
    
if __name__ =='__main__':
    main()    
