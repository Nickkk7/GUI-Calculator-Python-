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

toolbar=Frame(root,bg="pink")
insertbutton=Button(toolbar,text="Insert file",command=fun)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton= Button(toolbar,text="print",command=fun)
printbutton.pack(side=LEFT,padx=2,pady=3)
toolbar.pack(side=TOP,fill=X)

root.mainloop()