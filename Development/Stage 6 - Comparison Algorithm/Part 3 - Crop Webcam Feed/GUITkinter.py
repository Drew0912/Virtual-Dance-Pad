import tkinter as tk #Imports Tkinter under the name tk.
from tkinter import ttk #ComboBox Widget is part of ttk module in Tkinter.

from tkinter import StringVar

import webbrowser, os #Open browser

import CheckFloat #CheckFloat function
import WebcamCV2 #Webcam feed python file

import threading #Python Threading module
import cv2 #OpenCV

from PIL import Image, ImageTk #Python Imaging Library

import time #Time functions

class MainWindow(): #Main Window Class
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        self.WebcamOpen = False #Boolean so Calibration can only be opened when webcam is open.

        #Sensitivity Values
        global UpperOne, UpperTwo, UpperThree, UpperFour, LowerOne, LowerTwo, LowerThree, LowerFour
        UpperOne = "Set Value"
        UpperTwo = "Set Value"
        UpperThree = "Set Value"
        UpperFour = "Set Value"
        LowerOne = "Set Value"
        LowerTwo = "Set Value"
        LowerThree = "Set Value"
        LowerFour = "Set Value"

        def StartStop(): #Changes text of Button when pressed.
            if self.StartStopButton["text"] == "Start":
                self.StartStopButton["text"] = "Stop"
            else:
                self.StartStopButton["text"] = "Start"

        def Help(): #Opens HTML file.
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def CalibrationWindow(): #Open Main Calibration window
            if self.WebcamOpen:
                self.newwindow = tk.Toplevel(self.root)
                self.app = MainCalibration(self.newwindow)
            else:
                self.Message["text"] = "Open Webcam first."    

        def Webcam():
            self.WebcamOpen = True
            global cameraFeed
            cameraFeed = WebcamCV2.VidCapture()
            cv2.setMouseCallback(cameraFeed.Name, cameraFeed.Click)
            global close
            close = False
            while(True):
                cameraFeed.showFrame()
                if cv2.waitKey(20) == 27: #Press esc to exit.
                    self.WebcamOpen = not self.WebcamOpen
                    break
                if close: #Exit if close is true.
                    close = not close
                    self.WebcamOpen = not self.WebcamOpen
                    break
            cv2.destroyAllWindows()

        def WebcamClick(): #Function to load Webcam function.
            if self.DisplayButton["text"] == "Open Webcam":
                T1.start() #Start thread.
                self.DisplayButton["text"] = "Close Webcam. \n Requires restart after close."
            else:
                global close
                close = not close
                self.DisplayButton["text"] = "Open Webcam"


        #Threading
        T1 = threading.Thread(target=Webcam) #Thread for Webcam feed
        T1.daemon = True #Close Webcam if GUi is closed                            

        self.WebcamSelect = ttk.Combobox(root, width=30, state='readonly',
                            values=[
                                "Select which Webcam:",
                                "0",
                                "1",
                                "2",
                                "3",])
        self.WebcamSelect.grid(row=0, column=0, columnspan=2, pady=(20,10))
        self.WebcamSelect.current(0) #This sets the displayed value of the ComboBox.
        self.Message = tk.Label(root, text="") #Spare Label to give message to user on input.
        self.Message.grid(row=1, column=0, columnspan=2)
        self.DisplayButton = tk.Button(root, text="Open Webcam", width=30, height=5, command=WebcamClick)
        self.DisplayButton.grid(row=2, column=0, columnspan=2)
        self.StartStopButton = tk.Button(root, text="Start", width=30, height=5, command=StartStop)
        self.StartStopButton.grid(row=4, column=0, columnspan=2,
                            sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20), padx=10)
        self.HelpButton = tk.Button(root, text="Help", height=5, command=Help)
        self.HelpButton.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10))
        self.CalibrateButton = tk.Button(root, text="Calibrate/Setup", height=5, command=CalibrationWindow)
        self.CalibrateButton.grid(row=3, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=(10,0))

        self.root.mainloop() #Infinite loop that does not end until the window is closed.

class MainCalibration: #Main Calibration Class
    def __init__(self, root):
        self.root = root
        self.root.title("Main Calibration") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.    

        self.Label = tk.Label(root, text="Go through Setup before pressing any other button.")
        self.Label.grid(row=0, column=0, columnspan=2, pady=(5,10), padx=10)

        def SetupWindow(): #Opens Calibration Window.
            self.SetupWindow = tk.Toplevel(self.root)
            self.SetupApp = Setup(self.SetupWindow)

        def Help(): #Opens HTML file.
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def Finish(): #Closes current window.
            self.root.destroy()

        def ConfigureWindow(): #Opens Configure window.
            self.ConfigureWindow = tk.Toplevel(self.root)
            self.Configure = Configure(self.ConfigureWindow)

        def SensitivityWindow(): #Opens Sensitvity window.
            self.SensitivityWindow = tk.Toplevel(self.root)
            self.Sensitivity = Sensitivity(self.SensitivityWindow)

        def Debug():
            print(UpperOne)            

        self.debugButton = tk.Button(root, text="Debug", command=Debug) #Debug button for testing
        self.debugButton.grid(row=1, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)    

        self.ConfigureButton = tk.Button(root, text="Configure", width=15, height=5, command=ConfigureWindow)
        self.ConfigureButton.grid(row=1, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.SensitivityButton = tk.Button(root, text="Sensitivity", width=15, height=5, command=SensitivityWindow)
        self.SensitivityButton.grid(row=2, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)   
        self.SetupButton = tk.Button(root, text="Setup", width=15, height=5, command=SetupWindow)
        self.SetupButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.FinishButton = tk.Button(root, text="Finish", width=15, height=5, command=Finish)
        self.FinishButton.grid(row=3, column=0, padx=(10,0), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)
        self.HelpButton = tk.Button(root, text="Help", width=15, height=5, command=Help)
        self.HelpButton.grid(row=3, column=1, padx=(0,10), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)

class Setup: 
    def __init__(self, root):
        self.root = root
        self.root.title("Setup") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

        def Back():
            self.root.destroy()

        def Help():
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def OpenAdjust():
            self.AdjustWindow = tk.Toplevel(self.root)
            self.Adjust = Adjust(self.AdjustWindow)

        def Next():
            self.ControlWindow = tk.Toplevel(self.root)
            self.Control = ControlPictureWindow(self.ControlWindow)

        def ResetGrid():
            cameraFeed.Reset()    

        self.Label = tk.Label(root, text="Click on the webcam feed to create 2 corners. \n One in the top left and the other in the bottom right of where you want the 3x3 grid.")
        self.Label.grid(row=0, column=0, columnspan=2, pady=(5,0))
        self.AdjustButton = tk.Button(root, text="Adjust", width=15, height=5, command=OpenAdjust)
        self.AdjustButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S, pady=(20,0))
        self.ResetButton = tk.Button(root, text="Reset", width=15, height=5, command=ResetGrid)
        self.ResetButton.grid(row=3, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)
        self.BackButton = tk.Button(root, text="Back", width=15, height=5, command=Back)
        self.BackButton.grid(row=3, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.NextButton = tk.Button(root, text="Next", width=15, height=5, command=Next)
        self.NextButton.grid(row=4, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20))
        self.HelpButton = tk.Button(root, text="Help", width=15, height=5, command=Help)
        self.HelpButton.grid(row=4, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20))

        self.root.mainloop()

class Adjust:
    def __init__(self, root):
        self.root = root
        self.root.title("Adjust") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

        def Help():
            url = 'file://' + os.path.realpath('index.html') #change url
            webbrowser.open(url)

        def Back():
            self.root.destroy()

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

        def ResetGrid():
            cameraFeed.Reset()    

        #First Corner
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

        #Second Corner
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

        #Buttons
        self.ResetButton = tk.Button(root, text="Reset", width=24, height=3, command=ResetGrid)
        self.ResetButton.grid(row=5, column=0, columnspan=2)
        self.HelpButton = tk.Button(root, text="Help", width=12, height=3, command=Help)
        self.HelpButton.grid(row=5, column=2, pady=10)
        self.BackButton = tk.Button(root, text="Back", width=12, height=3, command=Back)
        self.BackButton.grid(row=5, column=3, pady=10, padx=(0,10))

class ControlPictureWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Control Picture") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        def Back():
            self.root.destroy()

        def Help():
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def TakePicture():
            cameraFeed.TakePicture()

            time.sleep(2) #Delay by 2 seconds
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
        self.root.title("Confirm") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        self.img = ImageTk.PhotoImage(Image.open("Control_picture.jpg")) #Load Control picture.

        self.panel = tk.Label(root, image = self.img) #Label showing image.
        self.panel.image = self.img
        self.panel.grid(row=0, column=0, rowspan=4)

        def Help():
            url = 'file://' + os.path.realpath('index.html') #change url
            webbrowser.open(url)

        def Retake():
            self.root.destroy()

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
        self.root.title("Configure") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

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
        self.root.title("Sensitivity") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        #First row Labels
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

        def Save(): #Save entry values
            global UpperOne, UpperTwo, UpperThree, UpperFour, LowerOne, LowerTwo, LowerThree, LowerFour
            #Upper limits
            if CheckFloat.CheckFloat(self.UpperOneEntry.get()) == True: #Check input is float
                if float(self.UpperOneEntry.get()) >= 0 and float(self.UpperOneEntry.get()) <= 1: #Check between 1 and 0
                    UpperOne = self.UpperOneEntry.get()
                else:
                    print("Error")
            else:
                print("Error")
            if CheckFloat.CheckFloat(self.UpperTwoEntry.get()) == True: #Check input is float
                if float(self.UpperTwoEntry.get()) >= 0 and float(self.UpperTwoEntry.get()) <= 1: #Check between 1 and 0
                    UpperTwo = self.UpperTwoEntry.get()
                else:
                    print("Error")
            else:
                print("Error")
            if CheckFloat.CheckFloat(self.UpperThreeEntry.get()) == True: #Check input is float
                if float(self.UpperThreeEntry.get()) >= 0 and float(self.UpperThreeEntry.get()) <= 1: #Check between 1 and 0
                    UpperThree = self.UpperThreeEntry.get()
                else:
                    print("Error")
            else:
                print("Error")
            if CheckFloat.CheckFloat(self.UpperFourEntry.get()) == True: #Check input is float
                if float(self.UpperFourEntry.get()) >= 0 and float(self.UpperFourEntry.get()) <= 1: #Check between 1 and 0
                    UpperFour = self.UpperFourEntry.get()
                else:
                    print("Error")
            else:
                print("Error")

            #Lower limits
            if CheckFloat.CheckFloat(self.LowerOneEntry.get()) == True: #Check input is float
                if float(self.LowerOneEntry.get()) >= 0 and float(self.LowerOneEntry.get()) <= 1: #Check between 1 and 0
                    LowerOne = self.LowerOneEntry.get()
                else:
                    print("Error")
            else:
                print("Error")
            if CheckFloat.CheckFloat(self.LowerTwoEntry.get()) == True: #Check input is float
                if float(self.LowerTwoEntry.get()) >= 0 and float(self.LowerTwoEntry.get()) <= 1: #Check between 1 and 0
                    LowerTwo = self.LowerTwoEntry.get()
                else:
                    print("Error")
            else:
                print("Error")
            if CheckFloat.CheckFloat(self.LowerThreeEntry.get()) == True: #Check input is float
                if float(self.LowerThreeEntry.get()) >= 0 and float(self.LowerThreeEntry.get()) <= 1: #Check between 1 and 0
                    LowerThree = self.LowerThreeEntry.get()
                else:
                    print("Error")
            else:
                print("Error")
            if CheckFloat.CheckFloat(self.LowerFourEntry.get()) == True: #Check input is float
                if float(self.LowerFourEntry.get()) >= 0 and float(self.LowerFourEntry.get()) <= 1: #Check between 1 and 0
                    LowerFour = self.LowerFourEntry.get()
                else:
                    print("Error")
            else:
                print("Error")                        

        #Second row Labels
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

        #Third row Labels and Entry widgets
        self.UpperLimitLabel = tk.Label(root, text="Upper Limit:")
        self.UpperLimitLabel.grid(row=2, column=0)
        self.UpperOneEntryText = StringVar()
        self.UpperOneEntry = tk.Entry(root, textvariable=self.UpperOneEntryText)
        self.UpperOneEntryText.set(UpperOne)
        self.UpperOneEntry.grid(row=2, column=1)
        self.UpperTwoEntryText = StringVar()
        self.UpperTwoEntry = tk.Entry(root, textvariable=self.UpperTwoEntryText)
        self.UpperTwoEntryText.set(UpperTwo)
        self.UpperTwoEntry.grid(row=2, column=2)
        self.UpperThreeEntryText = StringVar()
        self.UpperThreeEntry = tk.Entry(root, textvariable=self.UpperThreeEntryText)
        self.UpperThreeEntryText.set(UpperThree)
        self.UpperThreeEntry.grid(row=2, column=3)
        self.UpperFourEntryText = StringVar()
        self.UpperFourEntry = tk.Entry(root, textvariable=self.UpperFourEntryText)
        self.UpperFourEntryText.set(UpperFour)
        self.UpperFourEntry.grid(row=2, column=4)

        #Fourth row Labels and Entry widgets
        self.LowerLimitLabel = tk.Label(root, text="Lower Limit:")
        self.LowerLimitLabel.grid(row=3, column=0)
        self.LowerOneEntryText = StringVar()
        self.LowerOneEntry = tk.Entry(root, textvariable=self.LowerOneEntryText)
        self.LowerOneEntryText.set(LowerOne)
        self.LowerOneEntry.grid(row=3, column=1)
        self.LowerTwoEntryText = StringVar()
        self.LowerTwoEntry = tk.Entry(root, textvariable=self.LowerTwoEntryText)
        self.LowerTwoEntryText.set(LowerTwo)
        self.LowerTwoEntry.grid(row=3, column=2)
        self.LowerThreeEntryText = StringVar()
        self.LowerThreeEntry = tk.Entry(root, textvariable=self.LowerThreeEntryText)
        self.LowerThreeEntryText.set(LowerThree)
        self.LowerThreeEntry.grid(row=3, column=3)
        self.LowerFourEntryText = StringVar()
        self.LowerFourEntry = tk.Entry(root, textvariable=self.LowerFourEntryText)
        self.LowerFourEntryText.set(LowerFour)
        self.LowerFourEntry.grid(row=3, column=4)

        self.SaveButton = tk.Button(root, text="Save", width=5, command=Save)
        self.SaveButton.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S)

        self.root.mainloop()                             

def main():
    root = tk.Tk() #Creates Tkinter window under the name root.
    app = MainWindow(root) #Passes Tkinter window to the MainWindow class and
                            #calls the object app.

if __name__ == "__main__": #Runs when the file is opened directly.
    main() 