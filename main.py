from tkinter import *
from tkinter import ttk
root = Tk()
e = Entry(root, width=50)
e.pack()

def click():
    test = Label(root, text=e.get())
    test.pack()

myButton = Button(root, text="SEND", command = click, fg="blue", bg = "red")
myButton.pack()

root.mainloop()