from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
def fun():
    print("welcome")
def passed():
    print("enter your password")
Label(root,text="hello world",bg="cyan").pack()
Label(root,text="hello avodha",fg="red").pack()
Button(f,text="login",bg="red",command=fun).pack()
Button(f,text="password",bg="cyan",command=passed).pack()
root.mainloop()