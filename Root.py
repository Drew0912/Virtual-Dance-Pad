#Outdated no longer needed.
from tkinter import *

root = Tk()
root.resizable(0,0) #Removes the Maximise button.

w = Label(root, text="Hello World!")
w.pack()

button = Button(root, text="Button", width='40')
button.pack()

root.mainloop()