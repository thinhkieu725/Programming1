"""
COMP.CS.100 Programming 1
0.0.codeTest.py
Creator: Thinh Kieu
Student number: 152167613

This is the file for testing
"""

from tkinter import *

root = Tk()
root.geometry("300x300")

w = Label(root, text='StudyTonight', fg="Blue", font="100")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(root, text="Homepage",
                      variable=Checkbutton1,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10)

Button2 = Checkbutton(root, text="Tutorials",
                      variable=Checkbutton2,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10)

Button3 = Checkbutton(root, text="Contactus",
                      variable=Checkbutton3,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10)

Button1.pack()
Button2.pack()
Button3.pack()

mainloop()