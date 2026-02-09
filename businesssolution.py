# import tkinter module 
from tkinter import *        

# Following will import tkinter.ttk module and 
# automatically override all the widgets 
# which are present in tkinter module. 
from tkinter.ttk import *

# Create Object
root = Tk() 

# dev
def blah():
	with open("demofile.txt", "w") as f:
		f.write(T.get("1.0",END))

def blahblah():
	with open("demofile.txt", "r") as f:
		T.insert("1.0",f.read())

# #idk



# print("You entered:")
# print(text)

# buttons
write_button = Button(root, text="Write To File", command=blah)
read_button = Button(root, text="Read From File", command=blahblah)


# Place widgets in window (with pack function!)(order matters)
write_button.pack()
read_button.pack()
#Tk.pack()

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
