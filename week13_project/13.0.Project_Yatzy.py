"""
COMP.CS.100 Programming 1.
13.0.Project_Yatzy.py

Creator: Thinh Kieu
Student ID number: 152167613
Student ID: dxthki
Email: thinh.kieu@tuni.fi


"""

from tkinter import *

# These image files have to be in the PyCharm project folder.
IMAGE_FILES = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif"]

class Yatzy:
    def __init__(self):
        # ===== INITIALIZE THE WINDOW AND IMAGES =====

        # Initialize the root window
        self.__main_window = Tk()
        self.__main_window.title("Yatzy")

        # Create PhotoImage objects and store them in a list
        self.__dice_images = []
        for image_file in IMAGE_FILES:
            new_image = PhotoImage(file=image_file)
            self.__dice_images.append(new_image)

        # Create an empty PhotoImage object with the size of the dice
        self.__empty_image = PhotoImage(width=100, height=100)

        # ===== DEFINE AND PLACE GUI COMPONENTS =====

        # 1. Dices
        # Define
        self.__dices = []
        for idx in range(5):
            new_dice = Label(self.__main_window, anchor=N)
            self.__dices.append(new_dice)

        # Place
        for idx in range(5):
            self.__dices[idx].grid(row=0, column=idx, rowspan=2,
                                   columnspan=1, padx=10, pady=10,
                                   sticky=W + E + S + N)

        # 2. Checkboxes
        # Define checkbox values
        self.checkbox_value = [IntVar()] * 5

        # Define checkboxes
        self.__checkboxes = []
        for idx in range(5):
            new_checkbox = Checkbutton(self.__main_window,
                        variable=self.checkbox_value[idx], onvalue=1,
                        offvalue=0)
            self.__checkboxes.append(new_checkbox)

        # Place checkboxes
        for idx in range(5):
            self.__checkboxes[idx].grid(row=3, column=idx, sticky=N)

        # 3. Roll button and number-of-roll label
        # Create components
        self.__roll_button = Button(self.__main_window, text="Roll",
                                    command=self.roll)
        self.__x_label = Label(self.__main_window, text="x",
                               anchor=CENTER)
        self.__number_of_rolls = 3
        self.__number_of_rolls_label = Label(self.__main_window,
                                             text=str(self.__number_of_rolls),
                                             anchor=CENTER)

        # Place components
        self.__roll_button.grid(row=3, column=0, rowspan=2,
                                columnsoan=3, sticky=W + E + S + N)
        self.__x_label.grid(row=3, column=3, rowspan=2, columnspan=1)
        self.__number_of_rolls_label.grid(row=3, column=4, rowspan=2,
                                          columnspan=1)

        # 4. Total points text and label
        # Create components
        self.__total_points_text_label = Label(self.__main_window,
                                               text="Total points:")
        self.__total_points = 0
        self.__total_points_label = Label(self.__main_window,
                                          text=str(self.__total_points))

        # Place components
        self.__total_points_text_label.grid(row=5, column=0, rowspan=1,
                                            columnspan=3)
        self.__total_points_label.grid(row=5, column=3, rowspan=1,
                                       columnspan=2)

        # 5. Message box
        # Create message box
        self.__message_box = Label(self.__main_window, text="",
                                   anchor=CENTER)

        # Place message box
        self.__message_box.grid(row=6, column=9, rowspan=3,
                                columnspan=5, sticky=W + E + S + N)

        # 6. Submit point buttons and point text label for each of them
        # TODO: Create buttons

        # TODO: Create point labels

        # TODO: Place buttons

        # TODO: Place point labels

    def roll(self):
        # TODO: Implement the function
        pass

def main():
    Yatzy()


if __name__ == "__main__":
    main()
