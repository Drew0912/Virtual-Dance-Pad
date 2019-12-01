import tkinter as tk
import webbrowser, os

from tkinter import PhotoImage
import PIL.Image, PIL.ImageTk
import cv2
import VCCB #Opencv py file

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main")
        self.root.resizable(0,0)
        self.webcam = True #boolean to check if webcam is being used.

        self.vid = VCCB.VidCapture() #from VCCB

        self.canvas = tk.Canvas(root, width=self.vid.width, height=self.vid.height)
        self.canvas.grid(padx=(10,0), pady=10, row=0, column=0,
                         rowspan=5, columnspan=5)

        def StartStop():
            if self.StartStopButton["text"] == "Start":
                self.StartStopButton["text"] = "Stop"
            else:
                self.StartStopButton["text"] = "Start"
        def Help():
            url = 'file://' + os.path.realpath('index.html')
            webbrowser.open(url)

        def CalibrationWindow():
            self.webcam = False
            self.newwindow = tk.Toplevel(self.root)
            self.app = Calibration(self.newwindow)
            
        self.StartStopButton = tk.Button(root, text="Start", width=30, command=StartStop)
        self.StartStopButton.grid(row=4, column=5, columnspan=2,
                                  sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,10), padx=10)
        self.HelpButton = tk.Button(root, text="Help", command=Help)
        self.HelpButton.grid(row=3, column=6, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10))
        self.CalibrateButton = tk.Button(root, text="Calibrate/Setup", command=CalibrationWindow)
        self.CalibrateButton.grid(row=3, column=5, sticky=tk.W+tk.E+tk.N+tk.S, padx=(10,0))
        
        self.delay = 15
        self.update()
        self.root.mainloop()

    def update(self):
        if self.webcam == True:
            ret, frame = self.vid.GetFrame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)                 
            self.root.after(self.delay, self.update)
        else:
            self.vid.removeFrame()        
        
    
class Calibration:
    def __init__(self, root):
        self.vid = VCCB.VidCapture()
        self.vid.showFrame()
        self.root = root
        self.root.title("Calibration")

def main():
    root = tk.Tk()
    app = MainWindow(root)
    #root.mainloop()
    
        
if __name__ =='__main__':
    main()
