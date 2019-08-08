from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title","this is awesome")
response = tkinter.messagebox.askquestion("Question 1","Do you like Tea")
if response=="yes":
    print("here tea for you")




root.mainloop() 