import tkinter as tk #Imports Tkinter under the name tk.
from tkinter import ttk #ComboBox Widget is part of ttk module in Tkinter.

import webbrowser, os

class MainWindow(): #Main Window Class
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.

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

class MainCalibration:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Calibration") #Title of the Window.
        self.root.resizable(0,0) #The window created cannot change size.    

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

        def ConfigureWindow():
            self.ConfigureWindow = tk.Toplevel(self.root)
            self.Configure = Configure(self.ConfigureWindow)

        def SensitivityWindow():
            self.SensitivityWindow = tk.Toplevel(self.root)
            self.Sensitivity = Sensitivity(self.SensitivityWindow)        

        self.debugButton = tk.Button(root, text="Debug")
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
        self.root.title("Calibration")
        self.root.resizable(0,0)

class Configure:
    def __init__(self, root):
        self.root = root
        self.root.title("Configure")
        self.root.resizable(0,0)

class Sensitivity:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensitivity")
        self.root.resizable(0,0)                            

def main():
    root = tk.Tk() #Creates Tkinter window under the name root.
    app = MainWindow(root) #Passes Tkinter window to the MainWindow class and
                            #calls the object app.

if __name__ == "__main__": #Runs when the file is opened directly.
    main() 