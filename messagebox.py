from tkinter import *
import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo("title: New Nepal was better")
response = tkinter.messagebox.askquestion("Question 1", "Do you agree?")

if response == 'yes':
    print("Thats great")

root.mainloop()