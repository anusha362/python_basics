from tkinter import *
root=Tk()
def fun():
    print("files open to write")
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New",command=fun)
submenu.add_command(label="New window")
submenu.add_command(label="Open")
submenu.add_command(label="Save")
submenu.add_command(label="Save As")
submenu.add_separator()
submenu.add_command(label="Page setup")
submenu.add_command(label="Print")
submenu.add_separator()
submenu.add_command(label="exit",command=root.quit)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo")
newmenu.add_separator()
newmenu.add_command(label="Cut")
newmenu.add_command(label="Copy")
newmenu.add_command(label="Paste")
newmenu.add_command(label="Delete")

nextmenu=Menu(mymenu)
mymenu.add_cascade(label="Format",menu=nextmenu)
nextmenu.add_command(label="Word wrap")
nextmenu.add_command(label="Font")

secondmenu=Menu(mymenu)
mymenu.add_cascade(label="View",menu=secondmenu)
secondmenu.add_command(label="Zoom")
secondmenu.add_command(label="Status Bar")

thirdmenu=Menu(mymenu)
mymenu.add_cascade(label="Help",menu=thirdmenu)
thirdmenu.add_command(label="View Help")
thirdmenu.add_command(label="Send feedback")
thirdmenu.add_separator()
thirdmenu.add_command(label="About Notepad")



root.mainloop()