import tkinter as tk #Imports Tkinter under the name tk.
from tkinter import ttk #ComboBox Widget is part of ttk module in Tkinter.

root = tk.Tk()
root.title("Main Window")

root.resizable(0,0)

WebcamSelect = ttk.Combobox(root, width=30, state='readonly',
                            values=[
                                "Select which Webcam:",
                                "0",
                                "1",
                                "2",
                                "3",])
WebcamSelect.grid(row=0, column=0, columnspan=2, pady=(20,10))
WebcamSelect.current(0)
Message = tk.Label(root, text="") #Error message.
Message.grid(row=1, column=0, columnspan=2)
DisplayButton = tk.Button(root, text="Open Webcam", width=30, height=5)
DisplayButton.grid(row=2, column=0, columnspan=2)
StartStopButton = tk.Button(root, text="Start", width=30, height=5)
StartStopButton.grid(row=4, column=0, columnspan=2,
                    sticky=tk.W+tk.E+tk.N+tk.S, pady=(0,20), padx=10)
HelpButton = tk.Button(root, text="Help", height=5)
HelpButton.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=(0,10))
CalibrateButton = tk.Button(root, text="Calibrate/Setup", height=5)
CalibrateButton.grid(row=3, column=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=(10,0))

root.mainloop()