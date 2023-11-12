"""
COMP.CS.100 Programming 1.
13.0.Project_Yatzy.py

Creator: Thinh Kieu
Student ID number: 152167613
Student ID: dxthki
Email: thinh.kieu@tuni.fi

# TODO: Add program description
"""

from tkinter import *
import random
import time

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
        self.__dice_labels = []
        self.__dice_values = [0, 0, 0, 0, 0]
        for idx in range(5):
            new_dice = Label(self.__main_window, image=self.__empty_image,
                             anchor=N)
            self.__dice_labels.append(new_dice)

        # Place
        for idx in range(5):
            self.__dice_labels[idx].grid(row=0, column=idx, rowspan=2,
                                         columnspan=1, padx=10, pady=10,
                                         sticky=W + E + S + N)

        # 2. Checkboxes
        # Define checkbox values
        self.checkbox_values = [IntVar(), IntVar(), IntVar(), IntVar(),
                                IntVar()]

        # Define checkboxes
        self.__checkboxes = []
        for idx in range(5):
            new_checkbox = Checkbutton(self.__main_window,
                                       variable=self.checkbox_values[idx],
                                       onvalue=1, offvalue=0)
            self.__checkboxes.append(new_checkbox)

        # Place checkboxes
        for idx in range(5):
            self.__checkboxes[idx].grid(row=2, column=idx, sticky=N)

        # 3. Roll button and number-of-roll label
        # Create components
        self.__roll_button = Button(self.__main_window, text="Roll",
                                    command=self.roll)
        self.__x_label = Label(self.__main_window, text="x",
                               anchor=CENTER)
        self.__number_of_rolls = 3
        self.__number_of_rolls_label = Label(self.__main_window,
                                             text=str(
                                                 self.__number_of_rolls),
                                             anchor=CENTER)

        # Place components
        self.__roll_button.grid(row=3, column=0, rowspan=2,
                                columnspan=3, sticky=W + E + S + N)
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
        self.__message_box.grid(row=6, column=0, rowspan=3, columnspan=5,
                                sticky=W + E + S + N)

        # 6. Submit point buttons and point text label for each of them
        # Create buttons
        self.submit_buttons = {}
        self.submit_buttons.update(
            {
                "ones": Button(self.__main_window, text="Sum of ones",
                               command=self.sum_of_ones),
                "twos": Button(self.__main_window, text="Sum of twos",
                               command=self.sum_of_twos),
                "threes": Button(self.__main_window, text="Sum of threes",
                                 command=self.sum_of_threes),
                "fours": Button(self.__main_window, text="Sum of fours",
                                command=self.sum_of_fours),
                "fives": Button(self.__main_window, text="Sum of fives",
                                command=self.sum_of_fives),
                "sixes": Button(self.__main_window, text="Sum of sixes",
                                command=self.sum_of_sixes),
                "straight": Button(self.__main_window, text="Straight",
                                   command=self.straight),
                "three_of_a_kind": Button(self.__main_window,
                                          text="Three of a kind",
                                          command=self.three_of_a_kind),
                "four_of_a_kind": Button(self.__main_window,
                                         text="Four of a kind",
                                         command=self.four_of_a_kind)
            }
        )
        # Set buttons' width and initial relief
        for button in self.submit_buttons:
            self.submit_buttons[button].configure(width=15, relief=RAISED)
        # Each submit button should be clicked only once per game, so a bool
        # dictionary is established to easily manage which button is clicked.
        self.__submit_button_clicked = {
            "ones": FALSE,
            "twos": FALSE,
            "threes": FALSE,
            "fours": FALSE,
            "fives": FALSE,
            "sixes": FALSE,
            "straight": FALSE,
            "three_of_a_kind": FALSE,
            "four_of_a_kind": FALSE
        }

        # Create point labels
        self.submit_point_labels = {}
        self.submit_point_labels.update(
            {
                "ones": Label(self.__main_window, text="   "),
                "twos": Label(self.__main_window, text="   "),
                "threes": Label(self.__main_window, text="   "),
                "fours": Label(self.__main_window, text="   "),
                "fives": Label(self.__main_window, text="   "),
                "sixes": Label(self.__main_window, text="   "),
                "straight": Label(self.__main_window, text="   "),
                "three_of_a_kind": Label(self.__main_window, text="   "),
                "four_of_a_kind": Label(self.__main_window, text="   ")
            }
        )

        # Place buttons
        self.submit_buttons["ones"].grid(row=2, column=5, sticky=W)
        self.submit_buttons["twos"].grid(row=3, column=5, sticky=W)
        self.submit_buttons["threes"].grid(row=4, column=5, sticky=W)
        self.submit_buttons["fours"].grid(row=5, column=5, sticky=W)
        self.submit_buttons["fives"].grid(row=6, column=5, sticky=W)
        self.submit_buttons["sixes"].grid(row=7, column=5, sticky=W)
        self.submit_buttons["straight"].grid(row=8, column=5, sticky=W)
        self.submit_buttons["three_of_a_kind"].grid(row=9, column=5, sticky=W)
        self.submit_buttons["four_of_a_kind"].grid(row=10, column=5, sticky=W)

        # Place point labels
        self.submit_point_labels["ones"].grid(row=2, column=6)
        self.submit_point_labels["twos"].grid(row=3, column=6)
        self.submit_point_labels["threes"].grid(row=4, column=6)
        self.submit_point_labels["fours"].grid(row=5, column=6)
        self.submit_point_labels["fives"].grid(row=6, column=6)
        self.submit_point_labels["sixes"].grid(row=7, column=6)
        self.submit_point_labels["straight"].grid(row=8, column=6)
        self.submit_point_labels["three_of_a_kind"].grid(row=9, column=6)
        self.submit_point_labels["four_of_a_kind"].grid(row=10, column=6)

        # 7. New game button and quit button
        # Create components
        self.__new_game_button = Button(self.__main_window, text="NEW GAME",
                                        relief=RAISED, width=20,
                                        command=self.new_game)
        self.__quit_button = Button(self.__main_window, text="QUIT",
                                    relief=RAISED, width=20,
                                    command=self.quit)

        # Place components
        self.__new_game_button.grid(row=0, column=5, rowspan=1, columnspan=2,
                                    sticky=W + E + S + N)
        self.__quit_button.grid(row=1, column=5, rowspan=1, columnspan=2,
                                sticky=W + E + S + N)

        self.new_game()
        self.__main_window.mainloop()

    # ==== MAIN FUNCTIONS WHICH ARE ASSIGNED TO BUTTONS ====
    # 1. Roll button
    def roll(self):
        """
        Roll the dice, display dice animations and prevent clicking other
        buttons that may cause errors while rolling.
        """
        # Decrease number_of_rolls and configure the label
        self.__number_of_rolls -= 1
        self.__number_of_rolls_label.configure(text=self.__number_of_rolls)
        # Disable available submit buttons and the roll button during the roll
        self.disable_available_submit_buttons()
        self.__roll_button.configure(relief=SUNKEN, state=DISABLED)

        # Check which dices are to be rolled
        rolling_dices = []
        for idx in range(5):
            if self.checkbox_values[idx].get() == 0:
                rolling_dices.append(idx)
        # Disable the checkboxes during the roll
        self.disable_checkboxes()

        # Roll the dices that are not selected to be kept
        for idx1 in range(10):
            for idx2 in rolling_dices:
                self.__dice_values[idx2] = random.randint(1, 6)
                self.__dice_labels[idx2].configure(image=self.__dice_images[
                    self.__dice_values[idx2] - 1])
            self.__main_window.update_idletasks()
            time.sleep(0.05)

        # Enable available submit buttons and the roll button
        # (if number_of_rolls is greater than 0) after the roll
        self.enable_available_submit_buttons()
        if self.__number_of_rolls > 0:
            self.__roll_button.configure(relief=RAISED, state=NORMAL)
        # Enable checkboxes while keeping initial check state
        if self.__number_of_rolls > 0:
            self.enable_checkboxes()

    # 2. Submit buttons
    # Basically, for each submit button, the function goes through 6 steps:
    # a. Mark the button as clicked
    # b. Determine the number of points for the round
    # c. Display the corresponding point label
    # d. Calculate and update the total point label
    # e. Display the message in the messagebox
    # f. Set up the next round
    def sum_of_ones(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["ones"]
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["ones"] = TRUE
        # b. Determine the number of points for the round
        round_points = self.sum_of(1)
        # c. Display the corresponding point label
        self.submit_point_labels["ones"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Sum of ones", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def sum_of_twos(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["twos"]
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["twos"] = TRUE
        # b. Determine the number of points for the round
        round_points = self.sum_of(2)
        # c. Display the corresponding point label
        self.submit_point_labels["twos"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Sum of twos", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def sum_of_threes(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["threes"]
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["threes"] = TRUE
        # b. Determine the number of points for the round
        round_points = self.sum_of(3)
        # c. Display the corresponding point label
        self.submit_point_labels["threes"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Sum of threes", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def sum_of_fours(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["fours"]
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["fours"] = TRUE
        # b. Determine the number of points for the round
        round_points = self.sum_of(4)
        # c. Display the corresponding point label
        self.submit_point_labels["fours"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Sum of fours", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def sum_of_fives(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["fives"]
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["fives"] = TRUE
        # b. Determine the number of points for the round
        round_points = self.sum_of(5)
        # c. Display the corresponding point label
        self.submit_point_labels["fives"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Sum of fives", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def sum_of_sixes(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["sixes"]
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["sixes"] = TRUE
        # b. Determine the number of points for the round
        round_points = self.sum_of(6)
        # c. Display the corresponding point label
        self.submit_point_labels["sixes"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Sum of sixes", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def straight(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["straight"]
        Straight is defined as [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6] in any order.
        Score for a straight: 25
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["straight"] = TRUE
        # b. Determine the number of points for the round
        if (2 in self.__dice_values and 3 in self.__dice_values and
            4 in self.__dice_values and 5 in self.__dice_values) and (
                1 in self.__dice_values or 6 in self.__dice_values):
            round_points = 25
        else:
            round_points = 0
        # c. Display the corresponding point label
        self.submit_point_labels["straight"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Straight", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def three_of_a_kind(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["three of a kind"]
        Three of a kind means at least three of the dices have the same value.
        Score for a three of a kind combination: 20
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["three_of_a_kind"] = TRUE
        # b. Determine the number of points for the round
        round_points = 0
        for val in range(1, 7):
            if self.__dice_values.count(val) >= 3:
                round_points = 20
        # c. Display the corresponding point label
        self.submit_point_labels["three_of_a_kind"].configure(
            text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(
            self.get_round_message("Three of a kind", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def four_of_a_kind(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["three of a kind"]
        Four of a kind means at least four of the dices have the same value.
        Score for a four of a kind combination: 30
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["four_of_a_kind"] = TRUE
        # b. Determine the number of points for the round
        round_points = 0
        for val in range(1, 7):
            if self.__dice_values.count(val) >= 4:
                round_points = 30
        # c. Display the corresponding point label
        self.submit_point_labels["four_of_a_kind"].configure(
            text=round_points)
        # d. Calculate and update the total point label
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)
        # e. Display the message in the messagebox
        self.set_message(
            self.get_round_message("Four of a kind", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    # 3. New game button and Quit button
    def new_game(self):
        """
        Set all components to the initial state.
        """
        # 1. Dices: Set the images to empty_image and dice_values to 0.
        for dice in self.__dice_labels:
            dice.configure(image=self.__empty_image)
        self.__dice_values = [0, 0, 0, 0, 0]

        # 2. Checkboxes: Deselect all checkboxes and set state to DISABLED
        for cb in self.__checkboxes:
            cb.deselect()
            cb.configure(state=DISABLED)

        # 3. Roll button and number-of-roll label: Set the roll_button's state
        # to normal and set the number_of_rolls to 3.
        self.__roll_button.configure(relief=RAISED, state=NORMAL)
        self.__number_of_rolls = 3
        self.__number_of_rolls_label.configure(text=self.__number_of_rolls)

        # 4. Total points text and label: set total points to 0.
        self.__total_points = 0
        self.__total_points_label.configure(text=self.__total_points)

        # 5. Message box: Set messagebox content
        new_game_content = "New game started. Please roll the dices!"
        self.set_message(new_game_content)

        # 6. Submit point buttons and point text label: Set all submit_buttons'
        # state to disabled, submit_button_clicked to FALSE
        # and empty all corresponding point text labels.
        self.disable_available_submit_buttons()
        for b in self.__submit_button_clicked:
            self.__submit_button_clicked[b] = FALSE
        for spl in self.submit_point_labels.values():
            spl.configure(text="   ")

    def quit(self):
        """
        Quits the game.
        """
        self.__main_window.destroy()

    # ==== SIDE FUNCTIONS TO SUPPORT THE IMPLEMENTATION OF MAIN FUNCTIONS ====
    def sum_of(self, number):
        """
        Calculate the sum of dices that has the inquired number.
        :param number: the reference number
        :return: int, sum of the dices whose number is the reference number.
        """
        result = 0
        for val in self.__dice_values:
            if val == number:
                result += number
        return result

    def set_message(self, new_text):
        """
        Configure new text for the message box.
        :param new_text: str, text to be displayed
        """
        self.__message_box.configure(text=new_text)

    def disable_checkboxes(self):
        """
        Disable all checkboxes while keeping the check state.
        """
        for cb in self.__checkboxes:
            cb.configure(state=DISABLED)

    def enable_checkboxes(self):
        """
        Enable all checkboxes while keeping the check state before disabled.
        """
        for cb in self.__checkboxes:
            cb.configure(state=NORMAL)

    def clear_checkboxes(self):
        """
        Clear all checkboxes.
        """
        for cb in self.__checkboxes:
            cb.deselect()

    def disable_available_submit_buttons(self):
        """
        Disable all (available) submit buttons.
        """
        for sb in self.submit_buttons.values():
            sb.configure(relief=SUNKEN, state=DISABLED)

    def enable_available_submit_buttons(self):
        """
        Enable available submit buttons - whose submit_button_clicked is FALSE.
        """
        for sb_name in self.__submit_button_clicked:
            if self.__submit_button_clicked[sb_name] == FALSE:
                self.submit_buttons[sb_name].configure(relief=RAISED,
                                                       state=NORMAL)

    def game_over(self):
        """
        Check whether the game is over,
        i.e. whether all submit buttons are clicked.
        :return: bool, TRUE if the game is over.
        """
        for sb_name in self.__submit_button_clicked:
            if self.__submit_button_clicked[sb_name] == FALSE:
                return FALSE
        return TRUE

    def get_round_message(self, button_name, round_points):
        """
        Get a round message to display after a round (clicking a submit button)
        :param button_name: the clicked submit button
        :param round_points: the number of points got from that round
        :return: string, the round message to be displayed
        """
        round_message1 = (f"{button_name} is chosen.\n"
                          f"Your score for this round: {round_points}\n")
        if self.game_over() == FALSE:
            round_message2 = "Please roll the dices!"
        else:
            round_message2 = (f"The game is over. Your total points is "
                              f"{self.__total_points}. Congratulations!")
        return round_message1 + round_message2

    def set_up_next_round(self):
        """
        Set up the buttons and checkboxes for the next round.
        """
        if self.game_over() == FALSE:
            # Roll button and number of rolls
            self.__number_of_rolls = 3
            self.__number_of_rolls_label.configure(text=self.__number_of_rolls)
            self.__roll_button.configure(relief=RAISED, state=NORMAL)
            # Checkboxes
            self.clear_checkboxes()
            self.disable_checkboxes()
            # Submit buttons
            self.disable_available_submit_buttons()
        # If the game is over
        else:
            # Disable checkboxes and roll button
            self.disable_checkboxes()
            self.__roll_button.configure(relief=SUNKEN, state=DISABLED)
            # Set number of rolls to 0
            self.__number_of_rolls = 0
            self.__number_of_rolls_label.configure(text=self.__number_of_rolls)


def main():
    Yatzy()


if __name__ == "__main__":
    main()
