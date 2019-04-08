import tkinter as tk
from tkinter import *
from tkinter import ttk



class DropDown:

    def __init__(self,frame):
        self.frame = frame

        text = tk.StringVar()
        dropDownMenu = ttk.Combobox(frame,width = 15, textvariable=text , state = "readonly")
        dropDownMenu['values'] = ("1","2","3","4","5")
        dropDownMenu.grid(column = 0,row = 0)
        dropDownMenu.current(0)

class inputClass:

    def __init__(self,frame):
        self.frame = frame
        
        input1 = ttk.Label(frame,width= 20,text = "input 1").grid(column = 0, row = 0)
        input2 = ttk.Label(frame,width = 20,text = "input 2").grid(column = 0, row = 1)
        input3 = ttk.Label(frame,width= 20 ,text = "input 3").grid(column = 0, row = 2)

        entry1 = ttk.Entry(frame,width=20).grid(column = 1, row = 0)
        entry1 = ttk.Entry(frame,width=20).grid(column = 1, row = 1)
        entry1 = ttk.Entry(frame,width=20).grid(column = 1, row = 2)

class outputClass:

    def __init__(self,frame):
        self.frame = frame

        button1 = ttk.Button(frame,width=10).grid(column = 0 , row = 0)
        button2 = ttk.Button(frame,width=10).grid(column = 1 , row = 0)
        button3 = ttk.Button(frame,width=10).grid(column = 2 , row = 0)
    

if __name__ == "__main__":    
    mainWindow = tk.Tk();
    mainWindow.title("UI")
    mainWindow.geometry("600x500")
    
    mainWindow.grid_rowconfigure(0,weight = 3)
    mainWindow.grid_rowconfigure(1,weight = 2)

    topFrame = tk.Frame(mainWindow , height = 300, width = 600)
    topFrame.grid_rowconfigure(0,weight = 1)
    topFrame.grid_columnconfigure(0,weight = 1)
    topFrame.grid_columnconfigure(1,weight = 1)

    topFrame.grid(column = 0, row = 0, sticky = 'nsew')

    dropDownFrame = tk.Frame(topFrame, height = 300, width = 300, bg = "#FFFFFF")
    dropDownFrame.grid_rowconfigure(0,weight = 1)
    dropDownFrame.grid_columnconfigure(0,weight = 1)
    dropDownFrame.grid(column = 0 , row = 0, sticky = 'nsew')

    inputFrame = tk.Frame(topFrame, height = 300, width = 300, bg = "#FF11FF")

    inputFrame.grid_rowconfigure(0,weight = 1)
    inputFrame.grid_rowconfigure(1,weight = 1)
    inputFrame.grid_rowconfigure(2,weight = 1)
    inputFrame.grid_columnconfigure(0,weight = 1)
    inputFrame.grid_columnconfigure(1,weight = 1)

    inputFrame.grid(column = 1, row = 0, sticky = 'nsew')

    bottomFrame = tk.Frame(mainWindow , height = 300, width = 600)
    bottomFrame.grid_columnconfigure(0,weight=1)
    bottomFrame.grid_rowconfigure(0,weight=1)
    bottomFrame.grid(column = 0, row = 1, sticky = 'nsew')

    outputFrame = tk.Frame(bottomFrame)

    outputFrame.grid_rowconfigure(0,weight = 1)
    outputFrame.grid_columnconfigure(0,weight = 1)
    outputFrame.grid_columnconfigure(1,weight = 1)
    outputFrame.grid_columnconfigure(2,weight = 1)

    outputFrame.grid(column = 0,row = 0, sticky = 'nsew')

    dropDown = DropDown(dropDownFrame)
    inputData = inputClass(inputFrame)
    outputData = outputClass(outputFrame)

    mainWindow.mainloop()