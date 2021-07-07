from tkinter import *
import tkinter.messagebox
root=Tk()
# tkinter.messagebox.showinfo("title","this is information")
# tkinter.messagebox.showwarning("WARNING","This is warning")
# tkinter.messagebox.showerror("ERROR","404 error is found")

msgbox=tkinter.messagebox.askquestion("Main","Do you need to continue?")
if msgbox=='yes':
    print("yes I want to continue")
else:
    print("No I dont want to continue")
root.mainloop()