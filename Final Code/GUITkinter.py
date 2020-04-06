#-------------------------------------------
#Andrew Lee
#File name: GUITkinter.py
#-------------------------------------------


#Imports
import tkinter as tk #Imports Tkinter under the name tk.
from tkinter import ttk #ComboBox Widget is part of ttk module in Tkinter.
from tkinter import StringVar #Tkinter string variable.
import webbrowser, os #Open web browser.
import CheckFloat #CheckFloat function.
import WebcamCV2 #Webcam feed python file.
import threading #Python Threading module.
import cv2 #OpenCV.
from PIL import Image, ImageTk #Python Imaging Library.
import time #Time functions.
from pyautogui import keyDown, keyUp #Keyboard inputs.
import WebcamList #List of webcams.
from pyautogui import alert #Message box.
import tkinter.font as font #Font variable.

#Main Window Class
class MainWindow():
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

        self.Started = False #Boolean to tell if the program has been started.

        #Boolean values for if a key is pressed down or not.
        self.OnePress = False
        self.TwoPress = False
        self.ThreePress = False
        self.FourPress = False

        #Validation boolean values.
        global SetupFinished, SensitivityFinished
        SetupFinished = False
        SensitivityFinished = False

        #Start/Stop button function
        def StartStop():
            if self.StartStopButton["text"] == "Start":
                if SensitivityFinished == True:
                    self.Started = True
                    self.StartStopButton["text"] = "Stop"
                    #print("Started")
                else:
                    alert(text="Setup Sensitivity first.", title="Start", button="OK") #Message box    
            else:
                self.Started = False
                self.StartStopButton["text"] = "Start"
                #print("Stopped")

        #Help button function
        def Help(): 
            url = 'file://' + os.path.realpath('Help.html')
            webbrowser.open(url) #Opens HTML file.

        #Calibration/Setup button function
        def CalibrationWindow(): 
            if self.WebcamOpen:
                self.newwindow = tk.Toplevel(self.root)
                self.app = MainCalibration(self.newwindow) #Open Main Calibration window
            else:
                #self.Message["text"] = "Open Webcam first."
                alert(text='Open Webcam first.', title='Webcam', button='OK') #Message box.   

        def Webcam():
            self.WebcamOpen = True
            global cameraFeed
            cameraFeed = WebcamCV2.VidCapture(int(self.WebcamSelect.get()))
            cv2.setMouseCallback(cameraFeed.Name, cameraFeed.Click)
            global close
            close = False
            while(True):
                cameraFeed.showFrame() #showFrame function from webcam feed python file.

                #Keyboard marcros

                #Main box 1. Back
                if self.Started: 
                    if cameraFeed.one >= float(LowerOne) and cameraFeed.one <= float(UpperOne) and not self.OnePress:
                        keyDown('s')
                        self.OnePress = not self.OnePress
                    elif self.OnePress:
                        if cameraFeed.one < float(LowerOne) or cameraFeed.one > float(UpperOne):
                            keyUp('s')
                            self.OnePress = not self.OnePress

                #Main box 2. Right            
                if self.Started: 
                    if cameraFeed.two >= float(LowerTwo) and cameraFeed.two <= float(UpperTwo) and not self.TwoPress:
                        keyDown('d')
                        self.TwoPress = not self.TwoPress
                    elif self.TwoPress:
                        if cameraFeed.two < float(LowerTwo) or cameraFeed.two > float(UpperTwo):
                            keyUp('d')
                            self.TwoPress = not self.TwoPress

                #Main box 3. Front
                if self.Started: 
                    if cameraFeed.three >= float(LowerThree) and cameraFeed.three <= float(UpperThree) and not self.ThreePress:
                        keyDown('w')
                        self.ThreePress = not self.ThreePress
                    elif self.ThreePress:
                        if cameraFeed.three < float(LowerThree) or cameraFeed.three > float(UpperThree):
                            keyUp('w')
                            self.ThreePress = not self.ThreePress

                #Main box 4. Left
                if self.Started: 
                    if cameraFeed.four >= float(LowerFour) and cameraFeed.four <= float(UpperFour) and not self.FourPress:
                        keyDown('a')
                        self.FourPress = not self.FourPress
                    elif self.FourPress:
                        if cameraFeed.four < float(LowerFour) or cameraFeed.four > float(UpperFour):
                            keyUp('a')
                            self.FourPress = not self.FourPress                                     

                if cv2.waitKey(20) == 27: #Press esc to exit.
                    self.WebcamOpen = not self.WebcamOpen
                    break
                if close: #Exit if close is true.
                    close = not close
                    self.WebcamOpen = not self.WebcamOpen
                    break
            cv2.destroyAllWindows()

        def WebcamClick(): #Function to load Webcam function.
            if self.WebcamSelect.get() == "Select which Webcam:":
                #self.Message["text"] = "Select which webcam to use."
                alert(text='Select which webcam to use from the drop down menu.', title='Select Webcam', button='OK') #Message box
            elif self.DisplayButton["text"] == "Open Webcam":
                T1.start() #Start thread.
                self.DisplayButton["text"] = "Close Webcam. \n Requires restart after close."
            else:
                global close
                close = not close
                self.DisplayButton["text"] = "Open Webcam"

        #Threading
        T1 = threading.Thread(target=Webcam) #Thread for Webcam feed
        T1.daemon = True #Close Webcam if GUi is closed

        #Global font variable
        global myFont
        myFont = font.Font(size='26', family='Comic Sans MS')                            

        #Webcam drop down menu
        self.WebcamSelect = ttk.Combobox(root, state='readonly', values=WebcamList.listWebcam())
        self.WebcamSelect['font'] = font.Font(size='20', family='Comic Sans MS')                   
        self.WebcamSelect.grid(row=0, column=0, columnspan=2, pady=(20,10), padx=10)
        self.WebcamSelect.current(0) #This sets the displayed value of the ComboBox.

        #self.Message = tk.Label(root, text="") #Spare Label to give message to user on input.
        #self.Message.grid(row=1, column=0, columnspan=2)

        #Open Webcam button
        self.DisplayButton = tk.Button(root, text="Open Webcam", height=2, command=WebcamClick)
        self.DisplayButton['font'] = myFont
        self.DisplayButton.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=10)

        #Start/Stop button
        self.StartStopButton = tk.Button(root, text="Start", height=2, command=StartStop)
        self.StartStopButton['font'] = myFont
        self.StartStopButton.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20), padx=10)

        #Help button
        self.HelpButton = tk.Button(root, text="Help", height=2, command=Help)
        self.HelpButton['font'] = myFont
        self.HelpButton.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10))

        #Calibrate/Setup button
        self.CalibrateButton = tk.Button(root, text="Calibrate/Setup", height=2, command=CalibrationWindow)
        self.CalibrateButton['font'] = myFont
        self.CalibrateButton.grid(row=3, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=(10,0))

        self.root.mainloop() #Infinite loop that does not end until the window is closed.

#Main Calibration Window Class
class MainCalibration: 
    def __init__(self, root):
        self.root = root
        self.root.title("Main Calibration") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        #Label with info
        self.Label = tk.Label(root, text="Go through Setup before pressing any other button.")
        self.Label['font'] = font.Font(size='16', family='Comic Sans MS')
        self.Label.grid(row=0, column=0, columnspan=2, pady=(5,10), padx=10)

        #Setup button function
        def SetupWindow(): 
            self.SetupWindow = tk.Toplevel(self.root)
            self.SetupApp = Setup(self.SetupWindow) #Opens Calibration Window.

        #Help button function
        def Help(): 
            url = 'file://' + os.path.realpath('Help.html')
            webbrowser.open(url) #Opens HTML file.

        #Finish button function
        def Finish(): 
            self.root.destroy() #Closes current window.

        #Configure button function
        def ConfigureWindow(): 
            self.ConfigureWindow = tk.Toplevel(self.root)
            self.Configure = Configure(self.ConfigureWindow) #Opens Configure window.

        #Sensitivity button function
        def SensitivityWindow(): 
            if SetupFinished == True: #Check that setup is finished
                self.SensitivityWindow = tk.Toplevel(self.root)
                self.Sensitivity = Sensitivity(self.SensitivityWindow) #Opens Sensitvity window.
            else:
                alert(text="Finish the setup process first.", title="Setup", button="OK") #Message box      

        #Configure button
        self.ConfigureButton = tk.Button(root, text="Configure", height=2, command=ConfigureWindow)
        self.ConfigureButton['font'] = myFont
        self.ConfigureButton.grid(row=1, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)

        #Sensitivity button
        self.SensitivityButton = tk.Button(root, text="Sensitivity", height=2, command=SensitivityWindow)
        self.SensitivityButton['font'] = myFont
        self.SensitivityButton.grid(row=2, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)   

        #Setup button
        self.SetupButton = tk.Button(root, text="Setup", height=2, command=SetupWindow)
        self.SetupButton['font'] = myFont
        self.SetupButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)

        #Finish button
        self.FinishButton = tk.Button(root, text="Finish", height=2, command=Finish)
        self.FinishButton['font'] = myFont
        self.FinishButton.grid(row=3, column=0, padx=(10,0), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)

        #Help button
        self.HelpButton = tk.Button(root, text="Help", height=2, command=Help)
        self.HelpButton['font'] = myFont
        self.HelpButton.grid(row=3, column=1, padx=(0,10), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)

#Setup Window Class
class Setup: 
    def __init__(self, root):
        self.root = root
        self.root.title("Setup") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

        #Back button function
        def Back():
            self.root.destroy() #Closes current window.

        #Help button function
        def Help():
            url = 'file://' + os.path.realpath('Help.html')
            webbrowser.open(url) #Opens HTML file.

        #Adjust button function
        def OpenAdjust():
            self.AdjustWindow = tk.Toplevel(self.root)
            self.Adjust = Adjust(self.AdjustWindow) #Opens Adjust Window

        #Next button function
        def Next():
            if cameraFeed.drawingfinish == True: #3x3 grid must be drawn. 
                self.ControlWindow = tk.Toplevel(self.root)
                self.Control = ControlPictureWindow(self.ControlWindow) #Opens Control Picture Window
            else:
                alert(text="Create the 3x3 grid first.", title="3x3 Grid", button="OK") #Message box    

        #Reset button function
        def ResetGrid():
            cameraFeed.Reset() #Reset function from webcam feed python file
            alert(text='The webcam feed has been reset.', title='Reset', button='OK') #Message box    

        #Label with info
        self.Label = tk.Label(root, text="Click on the webcam feed to create 2 corners. \n One in the top left and the other in the bottom right of where you want the 3x3 grid.")
        self.Label['font'] = font.Font(size='12', family='Comic Sans MS')
        self.Label.grid(row=0, column=0, columnspan=2, pady=(5,0))

        #Adjust button
        self.AdjustButton = tk.Button(root, text="Adjust", height=2, command=OpenAdjust)
        self.AdjustButton['font'] = myFont
        self.AdjustButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S, pady=(20,0))

        #Reset button
        self.ResetButton = tk.Button(root, text="Reset", height=2, command=ResetGrid)
        self.ResetButton['font'] = myFont
        self.ResetButton.grid(row=3, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)

        #Back button
        self.BackButton = tk.Button(root, text="Back", height=2, command=Back)
        self.BackButton['font'] = myFont
        self.BackButton.grid(row=3, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)

        #Next button
        self.NextButton = tk.Button(root, text="Next", height=2, command=Next)
        self.NextButton['font'] = myFont
        self.NextButton.grid(row=4, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20))

        #Help button
        self.HelpButton = tk.Button(root, text="Help", height=2, command=Help)
        self.HelpButton['font'] = myFont
        self.HelpButton.grid(row=4, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20))

        self.root.mainloop() #Infinite loop that does not end until the window is closed.

#Adjust Window Class
class Adjust:
    def __init__(self, root):
        self.root = root
        self.root.title("Adjust") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

        #Help button function
        def Help():
            url = 'file://' + os.path.realpath('Help.html') 
            webbrowser.open(url) #Opens HTML file.

        #Back button function
        def Back():
            self.root.destroy() #Closes current window.

        #Functions to change location of 2 main corners
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

        #Reset button function
        def ResetGrid():
            cameraFeed.Reset() #Reset function from webcam feed python file
            alert(text='The webcam feed has been reset.', title='Reset', button='OK') #Message box

        #Font variable for Adjust Window
        self.adjustFont = font.Font(size='16', family='Comic Sans MS')        

        #First Corner label and buttons
        self.FirstLabel = tk.Label(root, text="Top Left Corner:")
        self.FirstLabel['font'] = self.adjustFont
        self.FirstLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.S)

        self.LeftIncreaseY = tk.Button(root, text="UP", command=LeftCornerUp)
        self.LeftIncreaseY['font'] = myFont
        self.LeftIncreaseY.grid(row=1, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)

        self.LeftDecreaseY = tk.Button(root, text="DOWN", command=LeftCornerDown)
        self.LeftDecreaseY['font'] = myFont
        self.LeftDecreaseY.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        self.LeftIncreaseX = tk.Button(root, text="RIGHT", command=LeftCornerRight)
        self.LeftIncreaseX['font'] = myFont
        self.LeftIncreaseX.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        self.LeftDecreaseX = tk.Button(root, text="LEFT", command=LeftCornerLeft)
        self.LeftDecreaseX['font'] = myFont
        self.LeftDecreaseX.grid(row=1, column=3, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)


        #Second Corner label and buttons
        self.SecondLabel = tk.Label(root, text="Bottom Right Corner:")
        self.SecondLabel['font'] = self.adjustFont
        self.SecondLabel.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.S)

        self.RightIncreaseY = tk.Button(root, text="UP", command=RightCornerUp)
        self.RightIncreaseY['font'] = myFont
        self.RightIncreaseY.grid(row=3, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)

        self.RightDecreaseY = tk.Button(root, text="DOWN", command=RightCornerDown)
        self.RightDecreaseY['font'] = myFont
        self.RightDecreaseY.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        self.RightIncreaseX = tk.Button(root, text="RIGHT", command=RightCornerRight)
        self.RightIncreaseX['font'] = myFont
        self.RightIncreaseX.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        self.RightDecreaseX = tk.Button(root, text="LEFT", command=RightCornerLeft)
        self.RightDecreaseX['font'] = myFont
        self.RightDecreaseX.grid(row=3, column=3, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)

        #Label with info
        self.ResetMessage = tk.Label(root, text="Press the reset button to remove the 3x3 grid.")
        self.ResetMessage['font'] = self.adjustFont
        self.ResetMessage.grid(row=4, column=0, columnspan=4, pady=(10,0))

        #Reset button
        self.ResetButton = tk.Button(root, text="Reset", command=ResetGrid)
        self.ResetButton['font'] = myFont
        self.ResetButton.grid(row=5, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S, pady=10, padx=(10,0))

        #Help button
        self.HelpButton = tk.Button(root, text="Help", command=Help)
        self.HelpButton['font'] = myFont
        self.HelpButton.grid(row=5, column=2, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        #Back button
        self.BackButton = tk.Button(root, text="Back", command=Back)
        self.BackButton['font'] = myFont
        self.BackButton.grid(row=5, column=3, pady=10, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)

        self.root.mainloop #Infinite loop that does not end until the window is closed.

#Control Picture Window Class
class ControlPictureWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Control Picture") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        self.count = 6 #Starting number for countdown

        #Back button function
        def Back():
            self.root.destroy() #Closes current window.

        #Help button function
        def Help():
            url = 'file://' + os.path.realpath('Help.html')
            webbrowser.open(url) #Opens HTML file.

        #Take Picture button function
        def TakePicture():
            cameraFeed.TakePicture() #TakePicture function from webcam feed python file
            time.sleep(1) #Delay by 1 seconds
            self.ConfirmWindow = tk.Toplevel(self.root)
            self.Confirm = ControlPictureConfirmWindow(self.ConfirmWindow) #Opens Control Picture Confirmation Window

        #Countdown function
        def Countdown():
            self.count = self.count - 1 #Starts at 5
            self.CountdownLabel.config(text=str(self.count)) #Updates countdown text.
            if self.count > 0:
                self.CountdownLabel.after(1000,Countdown) #Repeat function every second.
            elif self.count == 0:
                TakePicture() #Run TakePicture function   

        ##Label with info
        self.Label = tk.Label(root, text="Make sure that the image displayed on the webcam feed\n is clear and that the user is standing on the center box of the 3x3 grid.")
        self.Label['font'] = font.Font(size='16', family='Comic Sans MS')
        self.Label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        #Back button
        self.BackButton = tk.Button(root, text="Back", height=2, command=Back)
        self.BackButton['font'] = myFont
        self.BackButton.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,20))

        #Help button
        self.HelpButton = tk.Button(root, text="Help", height=2, command=Help)
        self.HelpButton['font'] = myFont
        self.HelpButton.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,20), pady=(0,20))

        #Take Picture button
        self.TakePictureButton = tk.Button(root, text="Take Picture", height=2, command=Countdown)
        self.TakePictureButton['font'] = myFont
        self.TakePictureButton.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=(20,0), pady=(0,20))

        #Countdown Label
        self.CountdownLabel = tk.Label(root, text="")
        self.CountdownLabel['font'] = font.Font(size='48', family='Comic Sans MS')
        self.CountdownLabel.grid(row=1, column=0)

        self.root.mainloop #Infinite loop that does not end until the window is closed.

#Control Picture Confirmation Window Class
class ControlPictureConfirmWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Confirm") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        self.img = ImageTk.PhotoImage(Image.open("Control_picture.jpg")) #Load Control picture.
        
        #Label showing image.
        self.panel = tk.Label(root, image = self.img) 
        self.panel.image = self.img
        self.panel.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

        #Help button function
        def Help():
            url = 'file://' + os.path.realpath('Help.html')
            webbrowser.open(url) #Opens HTML file.

        #Retake button function
        def Retake():
            self.root.destroy() #Closes current window.

        #Yes button function
        def Yes():
            alert(text='Close all windows but Main Calibration and Main Window', title='Finish', button='OK') #Message box.
            self.TextLabel["text"] = "Close all windows but Main Calibration and Main Window" #Updated text in label
            cameraFeed.CropControl() #Runs CropControl function in webcam feed python file
            cameraFeed.SetupFinishBool() #Runs SetupFinishBool function in webcam feed python file
            global SetupFinished
            SetupFinished = not SetupFinished

        #Font variable for Control Picture Confirmation Window
        self.fontSize = font.Font(size='18', family='Comic Sans MS')            

        #Label with info
        self.TextLabel = tk.Label(root, text="")
        self.TextLabel['font'] = self.fontSize
        self.TextLabel.grid(row=0, column=1, columnspan=2)

        self.Label = tk.Label(root, text="Is this Control picture suitable?")
        self.Label['font'] = self.fontSize
        self.Label.grid(row=1, column=1, columnspan=2)

        #Retake button
        self.RetakeButton = tk.Button(root, text="Retake", height=2, command=Retake)
        self.RetakeButton['font'] = myFont
        self.RetakeButton.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10), pady=(0,10))

        #Yes button
        self.YesButton = tk.Button(root, text="Yes", height=2, command=Yes)
        self.YesButton['font'] = myFont
        self.YesButton.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,10))

        #Help button
        self.HelpButton = tk.Button(root, text="Help", height=2, command=Help)
        self.HelpButton['font'] = myFont
        self.HelpButton.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10), pady=(0,10))

        self.root.mainloop #Infinite loop that does not end until the window is closed.

#Configure Window Class
class Configure:
    def __init__(self, root):
        self.root = root
        self.root.title("Configure") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

        #Front box
        self.FrontLabel = tk.Label(root, text="Front:")
        self.FrontLabel['font'] = myFont
        self.FrontLabel.grid(row=0, column=0)
        self.FrontSelect = ttk.Combobox(root, width=12, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.FrontSelect['font'] = myFont                                     
        self.FrontSelect.grid(row=1, column=0)
        self.FrontSelect.current(0)

        #Right box
        self.RightLabel = tk.Label(root, text="Right:")
        self.RightLabel['font'] = myFont
        self.RightLabel.grid(row=0, column=1)
        self.RightSelect = ttk.Combobox(root, width=12, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.RightSelect['font'] = myFont                                     
        self.RightSelect.grid(row=1, column=1)
        self.RightSelect.current(1)

        #Left box
        self.LeftLabel = tk.Label(root, text="Left:")
        self.LeftLabel['font'] = myFont
        self.LeftLabel.grid(row=2, column=0)
        self.LeftSelect = ttk.Combobox(root, width=12, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.LeftSelect['font'] = myFont                                     
        self.LeftSelect.grid(row=3, column=0)
        self.LeftSelect.current(2)

        #Back box
        self.BackLabel = tk.Label(root, text="Back:")
        self.BackLabel['font'] = myFont
        self.BackLabel.grid(row=2, column=1)
        self.BackSelect = ttk.Combobox(root, width=12, state='readonly',
                                         values=[
                                             "1",
                                             "2",
                                             "3",
                                             "4",])
        self.BackSelect['font'] = myFont                                     
        self.BackSelect.grid(row=3, column=1)
        self.BackSelect.current(3)

        self.root.mainloop #Infinite loop that does not end until the window is closed.

#Sensitivity Window Class
class Sensitivity:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensitivity") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

        #Font variable for Sensitivity Window
        self.SensitivityFontSize = font.Font(size='22', family='Comic Sans MS')

        #First row Labels
        self.BoxLabel = tk.Label(root, text="Box:")
        self.BoxLabel['font'] = self.SensitivityFontSize
        self.BoxLabel.grid(row=0, column=0)

        self.OneLabel = tk.Label(root, text="One")
        self.OneLabel['font'] = self.SensitivityFontSize
        self.OneLabel.grid(row=0, column=1)

        self.TwoLabel = tk.Label(root, text="Two")
        self.TwoLabel['font'] = self.SensitivityFontSize
        self.TwoLabel.grid(row=0, column=2)

        self.ThreeLabel = tk.Label(root, text="Three")
        self.ThreeLabel['font'] = self.SensitivityFontSize
        self.ThreeLabel.grid(row=0, column=3)

        self.FourLabel = tk.Label(root, text="Four")
        self.FourLabel['font'] = self.SensitivityFontSize
        self.FourLabel.grid(row=0, column=4)


        #Update function for Detection Values
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

        #Save button function
        def Save():
            global UpperOne, UpperTwo, UpperThree, UpperFour, LowerOne, LowerTwo, LowerThree, LowerFour
            #Upper limit validation
            if CheckFloat.CheckFloat(self.UpperOneEntry.get()) == True: #Check input is float
                if float(self.UpperOneEntry.get()) >= 0 and float(self.UpperOneEntry.get()) <= 1: #Check between 1 and 0
                    UpperOne = self.UpperOneEntry.get()
                else:
                    alert(text='Value in Upper limit for box one is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Upper limit for box one is not a real number', title='Validation', button='OK')
            if CheckFloat.CheckFloat(self.UpperTwoEntry.get()) == True: #Check input is float
                if float(self.UpperTwoEntry.get()) >= 0 and float(self.UpperTwoEntry.get()) <= 1: #Check between 1 and 0
                    UpperTwo = self.UpperTwoEntry.get()
                else:
                    alert(text='Value in Upper limit for box two is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Upper limit for box two is not a real number', title='Validation', button='OK')
            if CheckFloat.CheckFloat(self.UpperThreeEntry.get()) == True: #Check input is float
                if float(self.UpperThreeEntry.get()) >= 0 and float(self.UpperThreeEntry.get()) <= 1: #Check between 1 and 0
                    UpperThree = self.UpperThreeEntry.get()
                else:
                    alert(text='Value in Upper limit for box three is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Upper limit for box three is not a real number', title='Validation', button='OK')
            if CheckFloat.CheckFloat(self.UpperFourEntry.get()) == True: #Check input is float
                if float(self.UpperFourEntry.get()) >= 0 and float(self.UpperFourEntry.get()) <= 1: #Check between 1 and 0
                    UpperFour = self.UpperFourEntry.get()
                else:
                    alert(text='Value in Upper limit for box four is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Upper limit for box four is not a real number', title='Validation', button='OK')

            #Lower limit validation
            if CheckFloat.CheckFloat(self.LowerOneEntry.get()) == True: #Check input is float
                if float(self.LowerOneEntry.get()) >= 0 and float(self.LowerOneEntry.get()) <= 1: #Check between 1 and 0
                    LowerOne = self.LowerOneEntry.get()
                else:
                    alert(text='Value in Lower limit for box one is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Lower limit for box one is not a real number', title='Validation', button='OK')
            if CheckFloat.CheckFloat(self.LowerTwoEntry.get()) == True: #Check input is float
                if float(self.LowerTwoEntry.get()) >= 0 and float(self.LowerTwoEntry.get()) <= 1: #Check between 1 and 0
                    LowerTwo = self.LowerTwoEntry.get()
                else:
                    alert(text='Value in Lower limit for box two is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Lower limit for box two is not a real number', title='Validation', button='OK')
            if CheckFloat.CheckFloat(self.LowerThreeEntry.get()) == True: #Check input is float
                if float(self.LowerThreeEntry.get()) >= 0 and float(self.LowerThreeEntry.get()) <= 1: #Check between 1 and 0
                    LowerThree = self.LowerThreeEntry.get()
                else:
                    alert(text='Value in Lower limit for box three is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Lower limit for box three is not a real number', title='Validation', button='OK')
            if CheckFloat.CheckFloat(self.LowerFourEntry.get()) == True: #Check input is float
                if float(self.LowerFourEntry.get()) >= 0 and float(self.LowerFourEntry.get()) <= 1: #Check between 1 and 0
                    LowerFour = self.LowerFourEntry.get()
                else:
                    alert(text='Value in Lower limit for box four is not between 1 and 0', title='Validation', button='OK')
            else:
                alert(text='Value in Lower limit for box four is not a real number', title='Validation', button='OK')
            global SensitivityFinished
            SensitivityFinished = True    

        #Second row Labels
        self.DetectionLabel = tk.Label(root, text="Detection Value:")
        self.DetectionLabel['font'] = self.SensitivityFontSize
        self.DetectionLabel.grid(row=1, column=0)

        self.DetectionOneLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionOneLabel['font'] = self.SensitivityFontSize
        self.DetectionOneLabel.grid(row=1, column=1)

        self.DetectionTwoLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionTwoLabel['font'] = self.SensitivityFontSize
        self.DetectionTwoLabel.grid(row=1, column=2)

        self.DetectionThreeLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionThreeLabel['font'] = self.SensitivityFontSize
        self.DetectionThreeLabel.grid(row=1, column=3)

        self.DetectionFourLabel = tk.Label(root, text="...", borderwidth=2, relief='ridge')
        self.DetectionFourLabel['font'] = self.SensitivityFontSize
        self.DetectionFourLabel.grid(row=1, column=4)

        #Third row Labels and Entry widgets
        self.UpperLimitLabel = tk.Label(root, text="Upper Limit:")
        self.UpperLimitLabel['font'] = self.SensitivityFontSize
        self.UpperLimitLabel.grid(row=2, column=0)

        self.UpperOneEntryText = StringVar()
        self.UpperOneEntry = tk.Entry(root, textvariable=self.UpperOneEntryText)
        self.UpperOneEntryText.set(UpperOne)
        self.UpperOneEntry['font'] = self.SensitivityFontSize
        self.UpperOneEntry.grid(row=2, column=1)

        self.UpperTwoEntryText = StringVar()
        self.UpperTwoEntry = tk.Entry(root, textvariable=self.UpperTwoEntryText)
        self.UpperTwoEntryText.set(UpperTwo)
        self.UpperTwoEntry['font'] = self.SensitivityFontSize
        self.UpperTwoEntry.grid(row=2, column=2)
        
        self.UpperThreeEntryText = StringVar()
        self.UpperThreeEntry = tk.Entry(root, textvariable=self.UpperThreeEntryText)
        self.UpperThreeEntryText.set(UpperThree)
        self.UpperThreeEntry['font'] = self.SensitivityFontSize
        self.UpperThreeEntry.grid(row=2, column=3)

        self.UpperFourEntryText = StringVar()
        self.UpperFourEntry = tk.Entry(root, textvariable=self.UpperFourEntryText)
        self.UpperFourEntryText.set(UpperFour)
        self.UpperFourEntry['font'] = self.SensitivityFontSize
        self.UpperFourEntry.grid(row=2, column=4)

        #Fourth row Labels and Entry widgets
        self.LowerLimitLabel = tk.Label(root, text="Lower Limit:")
        self.LowerLimitLabel['font'] = self.SensitivityFontSize
        self.LowerLimitLabel.grid(row=3, column=0)

        self.LowerOneEntryText = StringVar()
        self.LowerOneEntry = tk.Entry(root, textvariable=self.LowerOneEntryText)
        self.LowerOneEntryText.set(LowerOne)
        self.LowerOneEntry['font'] = self.SensitivityFontSize
        self.LowerOneEntry.grid(row=3, column=1)

        self.LowerTwoEntryText = StringVar()
        self.LowerTwoEntry = tk.Entry(root, textvariable=self.LowerTwoEntryText)
        self.LowerTwoEntryText.set(LowerTwo)
        self.LowerTwoEntry['font'] = self.SensitivityFontSize
        self.LowerTwoEntry.grid(row=3, column=2)

        self.LowerThreeEntryText = StringVar()
        self.LowerThreeEntry = tk.Entry(root, textvariable=self.LowerThreeEntryText)
        self.LowerThreeEntryText.set(LowerThree)
        self.LowerThreeEntry['font'] = self.SensitivityFontSize
        self.LowerThreeEntry.grid(row=3, column=3)

        self.LowerFourEntryText = StringVar()
        self.LowerFourEntry = tk.Entry(root, textvariable=self.LowerFourEntryText)
        self.LowerFourEntryText.set(LowerFour)
        self.LowerFourEntry['font'] = self.SensitivityFontSize
        self.LowerFourEntry.grid(row=3, column=4)

        self.SaveButton = tk.Button(root, text="Save", command=Save)
        self.SaveButton['font'] = self.SensitivityFontSize
        self.SaveButton.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, pady=(10))

        #Start update functions.
        self.DetectionOneLabel.after(500,UpdateOne)
        self.DetectionTwoLabel.after(500,UpdateTwo)
        self.DetectionThreeLabel.after(500,UpdateThree)
        self.DetectionFourLabel.after(500,UpdateFour)

        self.root.mainloop() #Infinite loop that does not end until the window is closed.                             

def main():
    root = tk.Tk() #Creates Tkinter window under the name root.
    app = MainWindow(root) #Passes Tkinter window to the MainWindow class and
                            #calls the object app.

if __name__ == "__main__": #Runs when the file is opened directly.
    main() 