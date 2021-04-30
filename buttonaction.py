from tkinter import *

root = Tk()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side = BOTTOM)

def dosomething():
    print("yeah")

button1 = Button(newframe, text = "click here", fg = "Red", command = dosomething)
button2 = Button(otherframe, text = "click here", fg = "Red", command = dosomething)

button1.pack()
button2.pack()

root.mainloop()