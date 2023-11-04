"""
COMP.CS.100 Programming 1
0.2.CodeTest2.py
Creator: Thinh Kieu
Student number: 152167613

This is the file for testing
"""

# importing tkinter
import tkinter as tk


# defining function


def func(args):
    print(args)


# create root window
root = tk.Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
root.geometry("380x400")

# creating button
btn = tk.Button(root, text="Press",
                command=lambda: func("See this worked!"))
btn.pack()

# running the main loop
root.mainloop()