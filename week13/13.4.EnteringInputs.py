"""
COMP.CS.100 Programming 1.
13.4.EnteringInputs.py
Creator: Thinh Kieu
Student id number: 152167613

This program is to note down more advanced implementations of a graphic user interface (GUI).
About Entry() component.
"""

from tkinter import *

NAN = float("NaN")  # Not A Number: a value which can be used to
                    # express undefined float numbers in the program.

class GUI:
    def __init__(self):
        self.__float_result = NAN

        self.__main_window = Tk()

        # Creating the components of the GUI
        self.__entryA = Entry(self.__main_window)
        self.__entryB = Entry(self.__main_window)

        self.__labelA = Label(self.__main_window, text="A:")
        self.__labelB = Label(self.__main_window, text="B:")

        self.__result_title = Label(self.__main_window, text="Result:")
        self.__result_label = Label(self.__main_window, text=NAN)  # ✯✯✯

        self.__sum_button = Button(self.__main_window, text="A + B", command=self.sum)
        self.__minus_button = Button(self.__main_window, text="A - B", command=self.minus)
        self.__multiply_button = Button(self.__main_window, text="A * B", command=self.multiply)
        self.__divide_button = Button(self.__main_window, text="A / B", command=self.division)
        self.__move_button = Button(self.__main_window, text="result→A", command=self.move)
        self.__swap_button = Button(self.__main_window, text="A↔B", command=self.swap)
        self.__quit_button = Button(self.__main_window, text="lopeta", command=self.quit)

        # Positioning the components with grid geometry manager
        self.__labelA.grid(row=0, column=0, sticky=E)
        self.__entryA.grid(row=0, column=1, columnspan=2)
        self.__labelB.grid(row=0, column=3, sticky=E)
        self.__entryB.grid(row=0, column=4)

        self.__result_title.grid(row=1, column=3, sticky=E)
        self.__result_label.grid(row=1, column=4)

        self.__sum_button.grid(row=2, column=0, sticky=E + W)
        self.__minus_button.grid(row=2, column=1, sticky=E + W)
        self.__multiply_button.grid(row=3, column=0, sticky=E + W)
        self.__divide_button.grid(row=3, column=1, sticky=E + W)
        self.__move_button.grid(row=2, column=2, sticky=E + W)
        self.__swap_button.grid(row=3, column=2, sticky=E + W)

        self.__quit_button.grid(row=4, column=4, sticky=E)

        self.__main_window.mainloop()

    # Defining the event handlers
    def sum(self):
        (a, b) = self.get_A_and_B_content()
        self.__float_result = a + b
        self.set_result_label_text()

    def minus(self):
        (a, b) = self.get_A_and_B_content()
        self.__float_result = a - b
        self.set_result_label_text()

    def multiply(self):
        (a, b) = self.get_A_and_B_content()
        self.__float_result = a * b
        self.set_result_label_text()

    def division(self):
        (a, b) = self.get_A_and_B_content()
        self.__float_result = a / b
        self.set_result_label_text()

    def swap(self):
        (a, b) = self.get_A_and_B_content()
        self.__entryA.delete(0, END)
        self.__entryA.insert(0, b)  # ✯✯✯
        self.__entryB.delete(0, END)
        self.__entryB.insert(0, a)  # ✯✯✯

    def move(self):
        self.__entryA.delete(0, END)
        self.__entryA.insert(0, self.__float_result)  # ✯✯✯

    def quit(self):
        self.__main_window.destroy()

    # Regular methods (non event handlers)
    def get_A_and_B_content(self):
        try:
            A_value = float(self.__entryA.get())
        except ValueError:
            A_value = NAN

        try:
            B_value = float(self.__entryB.get())
        except ValueError:
            B_value = NAN
        return (A_value, B_value)

    def set_result_label_text(self):
        self.__result_label.configure(text=self.__float_result)  # ✯✯✯


def main():
    gui = GUI()


if __name__ == "__main__":
    main()
