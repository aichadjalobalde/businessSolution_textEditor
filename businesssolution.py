# import tkinter module 
from tkinter import *        

# Following will import tkinter.ttk module and 
# automatically override all the widgets 
# which are present in tkinter module. 
from tkinter.ttk import *

# Create Object
root = Tk() 

# Initialize tkinter window with dimensions 100x100             

camera = Button(root, text = 'Camera')
text = Button(root, text = 'Text')               
mic = Button(root, text = 'Mic') 
T = Text(root, height = 5, width = 10)
# Set the position of button on the top of window 
camera.pack()   
text.pack()
mic.pack() 
T.pack()  

root.mainloop()
