"""
COMP.CS.100 Programming 1
0.0.codeTest.py
Creator: Thinh Kieu
Student number: 152167613

This is the file for testing
"""

from tkinter import *

root = Tk()

def hello():
    print("hello!")

menubar = Menu(root)
menubar.add_command(label="Hello StudyTonight!", command=hello)
menubar.add_command(label="Quit!", command=root.quit)

root.config(menu=menubar)

root.mainloop()