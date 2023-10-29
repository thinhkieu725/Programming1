"""
COMP.CS.100 Programming 1.
13.2.MoreComplexGUI.py
Creator: Thinh Kieu
Student id number: 152167613
"""

from tkinter import *


class Counter:
    def __init__(self):
        """
        self.__current_value_label  # Label displaying the current value of the counter.
        self.__reset_button         # Button which resets counter to zero.
        self.__increase_button      # Button which increases the value of the counter by one.
        self.__decrease_button      # Button which decreases the value of the counter by one.
        self.__quit_button          # Button which quits the program.
        """

        self.__main_window = Tk()

        self.__current_value = 0
        self.__current_value_label = Label(self.__main_window, text=f"{self.__current_value}")
        self.__current_value_label.grid(row=0, column=0, columnspan=4)

        self.__reset_button = Button(self.__main_window, text="Reset", command=self.reset)
        self.__reset_button.grid(row=1, column=0)

        self.__increase_button = Button(self.__main_window, text="Increase", command=self.increase)
        self.__increase_button.grid(row=1, column=1)

        self.__decrease_button = Button(self.__main_window, text="Decrease", command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.grid(row=1, column=3)

        self.__main_window.mainloop()

    def reset(self):
        self.__current_value = 0
        self.__current_value_label.configure(text=f"{self.__current_value}")

    def increase(self):
        self.__current_value += 1
        self.__current_value_label.configure(text=f"{self.__current_value}")

    def decrease(self):
        self.__current_value -= 1
        self.__current_value_label.configure(text=f"{self.__current_value}")

    def quit(self):
        self.__main_window.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
