import tkinter as tk
from tkinter import ttk
import webbrowser, os
import cv2

import VCCB
import threading

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Main")
        self.master.resizable(0,0)

        def StartStop():
            if self.StartStopButton["text"] == "Start":
                self.StartStopButton["text"] = "Stop"
            else:
                self.StartStopButton["text"] = "Start"
        def Help():
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def CalibrationWindow():
            self.newwindow = tk.Toplevel(self.master)
            self.app = Calibration(self.newwindow)

        def Webcam():
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
                    break    
            cv2.destroyAllWindows()


            #VCCB.main() #change so creates class instead of run main.

        def WebcamClick(): #Function to load Webcam function.
            if self.DisplayButton["text"] == "Open Webcam":
                T1.start()
                self.DisplayButton["text"] = "Close Webcam"
            else:
                #VCCB.close = not VCCB.close
                self.DisplayButton["text"] = "Open Webcam"
                          


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
        self.DisplayButton = tk.Button(master, text="Open Webcam", width=30, height=5, command=WebcamClick)
        self.DisplayButton.grid(row=1, column=0, columnspan=2)
        self.StartStopButton = tk.Button(master, text="Start", width=30, height=5, command=StartStop)
        self.StartStopButton.grid(row=3, column=0, columnspan=2,
                                  sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20), padx=10)
        self.HelpButton = tk.Button(master, text="Help", height=5, command=Help)
        self.HelpButton.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10))
        self.CalibrateButton = tk.Button(master, text="Calibrate/Setup", height=5, command=CalibrationWindow)
        self.CalibrateButton.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=(10,0))

        self.master.mainloop()
                
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
            cameraFeed.Reset() #IDK Code
    

        self.Label = tk.Label(root, text="Click on the webcam feed to create 2 corners, \n one in the top left and the other in the botton right of where you want the 3x3 grid.")
        self.Label.grid(row=0, column=0, columnspan=2)
        self.AdjustButton = tk.Button(root, text="Adjust", width=15, height=5, command=OpenAdjust)
        self.AdjustButton.grid(row=2, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S, pady=(20,0))
        self.ResetButton = tk.Button(root, text="Reset", width=15, height=5, command=Reset)
        self.ResetButton.grid(row=3, column=0, padx=(10,0), sticky=tk.W+tk.E+tk.N+tk.S)
        self.BackButton = tk.Button(root, text="Back", command=Back, width=15, height=5)
        self.BackButton.grid(row=3, column=1, padx=(0,10), sticky=tk.W+tk.E+tk.N+tk.S)
        self.NextButton = tk.Button(root, text="Next", width=15, height=5)
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

        self.FirstLabel = tk.Label(root, text="Top Left Corner:")
        self.FirstLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.S)

        self.LeftIncreaseY = tk.Button(root, text="UP", width=8, height=2)
        self.LeftIncreaseY.grid(row=1, column=0, padx=(10,0))
        self.LeftDecreaseY = tk.Button(root, text="DOWN", width=8, height=2)
        self.LeftDecreaseY.grid(row=1, column=1)
        self.LeftIncreaseX = tk.Button(root, text="RIGHT", width=8, height=2)
        self.LeftIncreaseX.grid(row=1, column=2)
        self.LeftDecreaseX = tk.Button(root, text="LEFT", width=8, height=2)
        self.LeftDecreaseX.grid(row=1, column=3, padx=(0,10))

        self.SecondLabel = tk.Label(root, text="Bottom Right Corner:")
        self.SecondLabel.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.S)

        self.RightIncreaseY = tk.Button(root, text="UP", width=8, height=2)
        self.RightIncreaseY.grid(row=3, column=0, padx=(10,0))
        self.RightDecreaseY = tk.Button(root, text="DOWN", width=8, height=2)
        self.RightDecreaseY.grid(row=3, column=1)
        self.RightIncreaseX = tk.Button(root, text="RIGHT", width=8, height=2)
        self.RightIncreaseX.grid(row=3, column=2)
        self.RightDecreaseX = tk.Button(root, text="LEFT", width=8, height=2)
        self.RightDecreaseX.grid(row=3, column=3, padx=(0,10))

        self.HelpButton = tk.Button(root, text="Help", width=8, height=2, command=Help)
        self.HelpButton.grid(row=4, column=2, pady=10)
        self.BackButton = tk.Button(root, text="Back", width=8, height=2, command=Back)
        self.BackButton.grid(row=4, column=3, pady=10, padx=(0,10))

def main():
    root = tk.Tk()
    app = MainWindow(root)

if __name__ =='__main__':
    main()    
