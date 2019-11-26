import tkinter as tk
import webbrowser, os

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main")
        self.root.resizable(0,0)
        self.canvas = tk.Canvas(root, width=350, height=350,
                                highlightthickness=1, highlightbackground='black')
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
            self.newwindow = tk.Toplevel(self.root)
            self.app = Calibration(self.newwindow)
            
        self.StartStopButton = tk.Button(root, text="Start", width=30, command=StartStop)
        self.StartStopButton.grid(row=4, column=5, columnspan=2,
                                  sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,10), padx=10)
        self.HelpButton = tk.Button(root, text="Help", command=Help)
        self.HelpButton.grid(row=3, column=6, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10))
        self.CalibrateButton = tk.Button(root, text="Calibrate/Setup", command=CalibrationWindow)
        self.CalibrateButton.grid(row=3, column=5, sticky=tk.W+tk.E+tk.N+tk.S, padx=(10,0))
        
    
class Calibration:
    def __init__(self, root):
        self.root = root
        self.root.title("Calibration")

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
    
        
if __name__ =='__main__':
    main()
