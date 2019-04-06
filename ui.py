import tkinter as tk
from tkinter import ttk

window = tk.Tk();
window.title("User Interface")

ttk.Label(window,text="Select").grid(column=0, row = 0)
text = tk.StringVar()
selectedValue = ttk.Combobox(window,width = 12,textvariable=text, state = 'readonly')
selectedValue['values'] = (1,2,3,4,5,6)
selectedValue.grid(column = 0, row = 1)
selectedValue.current(0);


alabel = ttk.Label(window,text="Hello man")
alabel.grid(column = 0, row = 2)

def btn1():
    action.configure(text="btn1 " + name.get())

name = tk.StringVar()
input1 = ttk.Entry(window,width = 15, textvariable = name)
input1.grid(column = 1 , row = 2)
input1.focus()

action = ttk.Button(window,text="btn 1",command=btn1)
action.grid(column = 2, row = 2);

window.mainloop();