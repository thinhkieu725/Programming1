"""
COMP.CS.100 Programming 1
0.3.CodeTest3.py
Creator: Thinh Kieu
Student number: 152167613

This is the file for testing
"""

# importing tkinter
import tkinter as tk


# defining function


d# 2. Checkboxes
        # Define checkbox values
        self.checkbox_value = [IntVar()] * 5

        # Define checkboxes
        self.__checkboxes = []
        for idx in range(5):
            new_checkbox = Checkbutton(self.__main_window,
                                       variable=self.checkbox_value[
                                           idx], onvalue=1,
                                       offvalue=0)
            self.__checkboxes.append(new_checkbox)

        # Place checkboxes
        for idx in range(5):
            self.__checkboxes[idx].grid(row=2, column=idx, sticky=N)