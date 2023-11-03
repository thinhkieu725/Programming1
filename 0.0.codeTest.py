"""
COMP.CS.100 Programming 1
0.0.codeTest.py
Creator: Thinh Kieu
Student number: 152167613

This is the file for testing
"""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('100x100')

l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love anything')
    else:
        l.config(text='I love both')


def print_message():
    if var1.get() == 1:
        label.configure(text="OMG")
        print(1)
    else:
        label.configure(text="Oh no")


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

b = tk.Button(window, text="print", command=print_message)
label = tk.Label(window, text="")

b.pack()
label.pack()

window.mainloop()
