import tkinter as tk #Imports Tkinter under the name tk.
from tkinter import ttk #ComboBox Widget is part of ttk module in Tkinter.

root = tk.Tk() #Creates Tkinter window under the name root.
root.title("Main Window") #Title of the Window.

root.resizable(0,0) #The window created cannot change size.

WebcamSelect = ttk.Combobox(root, width=30, state='readonly',
                            values=[
                                "Select which Webcam:",
                                "0",
                                "1",
                                "2",
                                "3",])
WebcamSelect.grid(row=0, column=0, columnspan=2, pady=(20,10))
WebcamSelect.current(0) #This sets the displayed value of the ComboBox.
Message = tk.Label(root, text="") #Spare Label to give message to user on input.
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

root.mainloop() #Infinite loop that does not end until the window is closed.