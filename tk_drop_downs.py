from tkinter import *

def fun():
    print("menu item clicked")

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Project", command=fun)
submenu.add_command(label="Save", command=fun)

root.mainloop()