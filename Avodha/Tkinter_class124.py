from tkinter import *
root=Tk()
class demo:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.p=Button(frame,text="username",command=self.printmsg)
        self.p.pack()
        Button(frame,text="exit",command=frame.quit).pack()
    def printmsg(self):
        print("enter your username")

obj=demo(root)

root.mainloop()