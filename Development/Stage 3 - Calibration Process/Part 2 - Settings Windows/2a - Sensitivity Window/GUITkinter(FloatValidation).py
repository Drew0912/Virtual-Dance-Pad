import tkinter as tk #Imports Tkinter under the name tk.
from tkinter import ttk #ComboBox Widget is part of ttk module in Tkinter.

from tkinter import StringVar

import webbrowser, os

import CheckFloat

class MainWindow(): #Main Window Class
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

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
            self.newwindow = tk.Toplevel(self.root)
            self.app = MainCalibration(self.newwindow)            

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
        self.DisplayButton = tk.Button(root, text="Open Webcam", width=30, height=5)
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

        def Setup(): #Opens Calibration Window.
            self.SetupWindow = tk.Toplevel(self.root)
            self.Setup = Calibration(self.SetupWindow)

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
        self.SetupButton = tk.Button(root, text="Setup", width=15, height=5, command=Setup)
        self.SetupButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.FinishButton = tk.Button(root, text="Finish", width=15, height=5, command=Finish)
        self.FinishButton.grid(row=3, column=0, padx=(10,0), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)
        self.HelpButton = tk.Button(root, text="Help", width=15, height=5, command=Help)
        self.HelpButton.grid(row=3, column=1, padx=(0,10), pady=(0,20), sticky=tk.W+tk.E+tk.N+tk.S)

class Calibration: 
    def __init__(self, root):
        self.root = root
        self.root.title("Calibration") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

class Configure:
    def __init__(self, root):
        self.root = root
        self.root.title("Configure") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size. 

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
            if CheckFloat.CheckFloat(self.UpperOneEntry.get()) == True:
                if float(self.UpperOneEntry.get()) >= 0 and float(self.UpperOneEntry.get()) <= 1:
                    UpperOne = self.UpperOneEntry.get()
                    print("Works")
                else:
                    print("Error")
            else:
                print("Error")            

            #UpperTwo = self.UpperTwoEntry.get()
            #UpperThree = self.UpperThreeEntry.get()
            #UpperFour = self.UpperFourEntry.get()

            #LowerOne = self.LowerOneEntry.get()
            #LowerTwo = self.LowerTwoEntry.get()
            #LowerThree = self.LowerThreeEntry.get()
            #LowerFour = self.LowerFourEntry.get() 

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