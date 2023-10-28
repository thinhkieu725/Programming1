"""
COMP.CS.100 Programming 1.
13.1.Basics.py
Creator: Thinh Kieu
Student id number: 152167613

This program is to note down fundamental implementations of a graphic user interface (GUI).
"""

from tkinter import *


class GUI:
    def __init__(self):
        """
        Initialize the window together with the widgets on it and run the event loop
        """
        self.__main_window = Tk()  # Creating a main/root window which is an object of class Tk.

        # Create an object of class Label to form a text field
        self.__text_field = Label(self.__main_window, text="Hello World!", background="green", foreground="red", padx=30, pady=10, relief=RAISED, borderwidth=5)
        # Using a geometry manager to position the label inside the window.
        # :param side: specify which edge of the window the label is located at.
        self.__text_field.pack(expand=TRUE, fill=BOTH)

        # Modifying the Components' Parameters after being created
        self.__text_field.configure(text="Yep!", background="blue", foreground="yellow", padx=80, pady=5, relief=FLAT, borderwidth=1)

        self.__main_window.mainloop()  # Run the event loop. This function only returns when the GUI is closed.


def main():
    gui = GUI()


if __name__ == "__main__":
    main()
