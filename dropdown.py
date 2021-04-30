from tkinter import *

def function1():
    print("Menu item clicked")

root = Tk()

mymenu = Menu(root)
root.config(menu = mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label = "file", menu = submenu)

submenu.add_command(label = "project", command = function1)
submenu.add_command(label = "save", command = function1)

submenu.add_separator()
submenu.add_command(label = "exit", command = function1)


newmenu = Menu(mymenu)
mymenu.add_cascade(label = "edit", menu = newmenu)
newmenu.add_command(label = "undo", command = function1)

root.mainloop()