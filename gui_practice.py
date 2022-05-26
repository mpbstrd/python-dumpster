import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *

app = tk.Tk()

app.title("GUI")

# widgets
# Label > Button > Entry > ComboBox > CheckButton > Radio > ScrolledText > SpinBox > MenuBar > NoteBook

# Label
l1 = tk.Label(app,text="Sakura Voice Assistant",font=("Times New Roman",20))
l1.grid(column=0,row=0)

# Button
def clicked():
    l1.configure(text="Recording voice...")

    # Entry part
    res = "Welcome to " + txt.get()
    l1.configure(text=res)

bt = tk.Button(app,text="Record",bg="black",fg="white",command=clicked)
bt.grid(column=0,row=1)

# Entry
txt = tk.Entry(app,width = 10)
txt.grid(column=0,row=2)

# ComboBox
combo = Combobox(app)
combo['values'] = (1,2,3,4,5,"text")
combo.current(5)
combo.grid(column=0,row=3)

# Checkbutton
# check_state = BooleanVar()
# check_state.set(True)
# check = Checkbutton(app, text="Select", var = check_state)
# check.grid(column=0,row=4)

# Radiobutton
r1 = Radiobutton(app,text = "Python", value=1)
r2 = Radiobutton(app,text = "C++", value=2)
r3 = Radiobutton(app,text = "Java", value=3)
r1.grid(column=0,row=4)
r2.grid(column=1,row=4)
r3.grid(column=2,row=4)

# ScrolledTExt
scrtxt = scrolledtext.ScrolledText(app,width=40,height=10)

# MessageBox
def msgbox():
    messagebox.showinfo('Alert','Your computer has been infested with ratch and varkids')
btn = tk.Button(app,text="ALERT",command=msgbox)
btn.grid(column=0,row=5)

# SpinBox
spin = Spinbox(app,from_=0,to=100,width=5)
spin.grid(column=0,row=6)

# Window Sizing
app.geometry('700x300')
app.mainloop()