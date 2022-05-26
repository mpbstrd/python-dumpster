from tkinter import *
from tkinter.ttk import *
import tkinter as tk

window = tk.Tk()
window.title("GUI PRACTICE PART 2")

# GEOMETRY MANAGER CLASSES
# pack() - it organizes the widgets in the block, which means it occupies the entire available width
# grid() - it organizes the widgets in a table like structure
# place() - it is used to place the widgets at a specific position you want.

# ORGANIZING LAYOUT AND WIDGETS
# Frame - is used to create the divisions in the window. You can align the frames as 
#          you like with side parameter of pack() method.
# Button - is used to create a button in the window. It takes several parameters like
#          text(Value of the Button), fg and bg.


# top = tk.Frame(window).pack()
# bot = tk.Frame(window).pack(side="bottom")

# b1 = tk.Button(top,text="Button 1", fg = "red").pack()
# b2 = tk.Button(top,text="Button 2", fg = "blue").pack()
# b3 = tk.Button(top,text="Button 3", fg = "yellow").pack(side = "left")
# b4 = tk.Button(top,text="Button 4", fg = "green").pack(side = "left")

##########################################################################################

# BINDING AND EVENT HANDLING
# BINDING - calling functions whenever an event occurs refers to a binding function.
# EVENTS - mouseover, mousemove, clicking, scrolling, etc.
# MOUSE BUTTONS:
#   <Button-1> - Left-click
#   <Button-2> - Middle-click
#   <Button-3> - Right-click

def left_click(event):
    tk.Label(window,text="Clicked left!").pack()
def middle_click(event):
    tk.Label(window,text="Clicked middle!").pack()
def right_click(event):
    tk.Label(window,text="Clicked right!").pack()

window.bind("<Button-1>",left_click)
window.bind("<Button-2>",middle_click)
window.bind("<Button-3>",right_click)


##################################################################################
# ADD IMAGES AND ICONS
icon = tk.PhotoImage(file="img/pepeOK.png")
label = tk.Label(window,image=icon)
label.pack()

window.mainloop()