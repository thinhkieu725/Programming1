"""
COMP.CS.100 Programming 1.
13.0.Project_Yatzy.py

Creator: Thinh Kieu
Student ID number: 152167613
Student ID: dxthki
Email: thinh.kieu@tuni.fi

This program is expected to be an advanced GUI implementation. It comprises GUI
components that has not been previously introduced in the course: Checkbutton.

This project aims to create a one-player version of the dice game Yahtzee.

=============== RULES OF THE GAME ===============
The objective of the game is to score as many points as possible.
In each round of the game, the player has three rolls of dice. However, they
have the free decision to choose to end their turn after one or two rolls.
After the first roll and the second roll of the round, they can save any of the
five dices and re-roll the other dice. After the third roll, they have to end
the round. The round is ended by choosing one of 13 categories to get the round
score. The score received depends on how well the five dices match the scoring
rule for the category. The categories are:
- Sum of ones: The sum of dices with the number 1;
- Sum of twos: The sum of dices with the number 2;
- Sum of threes: The sum of dices with the number 3;
- Sum of fours: The sum of dices with the number 4;
- Sum of fives: The sum of dices with the number 5;
- Sum of sixes: The sum of dices with the number 6;
- Three of a kind: At least three dices the same, the score is sum of all dices;
- Four of a kind: At least four dices the same, the score is sum of all dices;
- Full house: Three of a kind and a pair, the score is 25;
- Small straight: Four sequential dices, the score is 30;
- Large straight: Five sequential dices, the score is 40;
- Yahtzee: All five dices the same, the score is 50;
- Chance: Any combination, the score is sum of all dices.

If one of the seven last categories are chosen but the dices do not match the
requirements of the category, the score for the round is 0.
Each category can be chosen once per game and the game ends when all 13
categories are chosen.

=============== NOTES ABOUT PROGRAM CONSTRUCTION ===============
In this program, the whole GUI is constructed within the class Yahtzee.
For easier management, the GUI components are divided into 7 categories.
1. Dices
2. Checkboxes
3. Roll button and number-of-roll label
4. Total points text and label
5. Message box
6. Submit point buttons and point text label for each of them
7. New game button and quit button

Other details have been clearly noted in the program.
"""

from tkinter import *
import random
import time

# These image files have to be in the PyCharm project folder.
IMAGE_FILES = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif"]


class Yahtzee:
    def __init__(self):
        # ===== INITIALIZE THE WINDOW AND IMAGES =====

        # Initialize the root window
        self.__main_window = Tk()
        self.__main_window.title("Yahtzee")

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
                "three_of_a_kind": Button(self.__main_window,
                                          text="Three of a kind",
                                          command=self.three_of_a_kind),
                "four_of_a_kind": Button(self.__main_window,
                                         text="Four of a kind",
                                         command=self.four_of_a_kind),
                "full_house": Button(self.__main_window, text="Full house",
                                     command=self.full_house),
                "small_straight": Button(self.__main_window,
                                         text="Small straight",
                                         command=self.small_straight),
                "large_straight": Button(self.__main_window,
                                         text="Large straight",
                                         command=self.large_straight),
                "yahtzee": Button(self.__main_window, text="Yahtzee",
                                  command=self.yahtzee),
                "chance": Button(self.__main_window, text="Chance",
                                 command=self.chance)
            }
        )
        # Set buttons' width and initial relief
        for button in self.submit_buttons:
            self.submit_buttons[button].configure(width=15, relief=RAISED)
        # Each submit button should be clicked only once per game, so a bool
        # dictionary is established to easily manage which button is clicked.
        self.__submit_button_clicked = {
            "ones": False,
            "twos": False,
            "threes": False,
            "fours": False,
            "fives": False,
            "sixes": False,
            "three_of_a_kind": False,
            "four_of_a_kind": False,
            "full_house": False,
            "small_straight": False,
            "large_straight": False,
            "yahtzee": False,
            "chance": False
        }

        # Create point labels
        self.submit_point_labels = {}
        self.submit_point_labels.update(
            {
                "ones": Label(self.__main_window, width=4),
                "twos": Label(self.__main_window, width=4),
                "threes": Label(self.__main_window, width=4),
                "fours": Label(self.__main_window, width=4),
                "fives": Label(self.__main_window, width=4),
                "sixes": Label(self.__main_window, width=4),
                "three_of_a_kind": Label(self.__main_window, width=4),
                "four_of_a_kind": Label(self.__main_window, width=4),
                "full_house": Label(self.__main_window, width=4),
                "small_straight": Label(self.__main_window, width=4),
                "large_straight": Label(self.__main_window, width=4),
                "yahtzee": Label(self.__main_window, width=4),
                "chance": Label(self.__main_window, width=4)
            }
        )

        # Place buttons
        self.submit_buttons["ones"].grid(row=2, column=5, sticky=W)
        self.submit_buttons["twos"].grid(row=3, column=5, sticky=W)
        self.submit_buttons["threes"].grid(row=4, column=5, sticky=W)
        self.submit_buttons["fours"].grid(row=5, column=5, sticky=W)
        self.submit_buttons["fives"].grid(row=6, column=5, sticky=W)
        self.submit_buttons["sixes"].grid(row=7, column=5, sticky=W)
        self.submit_buttons["three_of_a_kind"].grid(row=2, column=7, sticky=W)
        self.submit_buttons["four_of_a_kind"].grid(row=3, column=7, sticky=W)
        self.submit_buttons["full_house"].grid(row=4, column=7, sticky=W)
        self.submit_buttons["small_straight"].grid(row=5, column=7, sticky=W)
        self.submit_buttons["large_straight"].grid(row=6, column=7, sticky=W)
        self.submit_buttons["yahtzee"].grid(row=7, column=7, sticky=W)
        self.submit_buttons["chance"].grid(row=8, column=7, sticky=W)

        # Place point labels
        self.submit_point_labels["ones"].grid(row=2, column=6)
        self.submit_point_labels["twos"].grid(row=3, column=6)
        self.submit_point_labels["threes"].grid(row=4, column=6)
        self.submit_point_labels["fours"].grid(row=5, column=6)
        self.submit_point_labels["fives"].grid(row=6, column=6)
        self.submit_point_labels["sixes"].grid(row=7, column=6)
        self.submit_point_labels["three_of_a_kind"].grid(row=2, column=8)
        self.submit_point_labels["four_of_a_kind"].grid(row=3, column=8)
        self.submit_point_labels["full_house"].grid(row=4, column=8)
        self.submit_point_labels["small_straight"].grid(row=5, column=8)
        self.submit_point_labels["large_straight"].grid(row=6, column=8)
        self.submit_point_labels["yahtzee"].grid(row=7, column=8)
        self.submit_point_labels["chance"].grid(row=8, column=8)

        # 7. New game button and quit button
        # Create components
        self.__new_game_button = Button(self.__main_window, text="NEW GAME",
                                        relief=RAISED, width=40,
                                        command=self.new_game)
        self.__quit_button = Button(self.__main_window, text="QUIT",
                                    relief=RAISED, width=40,
                                    command=self.quit)

        # Place components
        self.__new_game_button.grid(row=0, column=5, rowspan=1, columnspan=4,
                                    sticky=W + E + S + N)
        self.__quit_button.grid(row=1, column=5, rowspan=1, columnspan=4,
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

        # Set the new message
        self.set_message("Rolling the dices...")

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

        # Set the new message
        if self.__number_of_rolls > 0:
            self.set_message("Choose the dices to keep and re-roll or "
                             "choose a category to submit the points.")
        else:
            self.set_message("Choose a category to submit the points.")

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
        self.__submit_button_clicked["ones"] = True
        # b. Determine the number of points for the round
        round_points = self.sum_of(1)
        # c. Display the corresponding point label
        self.submit_point_labels["ones"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
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
        self.__submit_button_clicked["twos"] = True
        # b. Determine the number of points for the round
        round_points = self.sum_of(2)
        # c. Display the corresponding point label
        self.submit_point_labels["twos"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
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
        self.__submit_button_clicked["threes"] = True
        # b. Determine the number of points for the round
        round_points = self.sum_of(3)
        # c. Display the corresponding point label
        self.submit_point_labels["threes"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
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
        self.__submit_button_clicked["fours"] = True
        # b. Determine the number of points for the round
        round_points = self.sum_of(4)
        # c. Display the corresponding point label
        self.submit_point_labels["fours"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
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
        self.__submit_button_clicked["fives"] = True
        # b. Determine the number of points for the round
        round_points = self.sum_of(5)
        # c. Display the corresponding point label
        self.submit_point_labels["fives"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
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
        self.__submit_button_clicked["sixes"] = True
        # b. Determine the number of points for the round
        round_points = self.sum_of(6)
        # c. Display the corresponding point label
        self.submit_point_labels["sixes"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Sum of sixes", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def three_of_a_kind(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["three_of_a_kind"]
        Three of a kind means at least three of the dices have the same value.
        Score for a three of a kind combination: sum of all dices.
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["three_of_a_kind"] = True
        # b. Determine the number of points for the round
        round_points = 0
        for val in range(1, 7):
            if self.__dice_values.count(val) >= 3:
                round_points = self.sum_of_all_dices()
        # c. Display the corresponding point label
        self.submit_point_labels["three_of_a_kind"].configure(
            text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(
            self.get_round_message("Three of a kind", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def four_of_a_kind(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["four_of_a_kind"]
        Four of a kind means at least four of the dices have the same value.
        Score for a four of a kind combination: sum of all dices.
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["four_of_a_kind"] = True
        # b. Determine the number of points for the round
        round_points = 0
        for val in range(1, 7):
            if self.__dice_values.count(val) >= 4:
                round_points = self.sum_of_all_dices()
        # c. Display the corresponding point label
        self.submit_point_labels["four_of_a_kind"].configure(
            text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(
            self.get_round_message("Four of a kind", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def full_house(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["full_house"]
        Full house means a three-of-a-kind combination and a pair.
        Score for a full house: 25.
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["full_house"] = True
        # b. Determine the number of points for the round
        s_dices = sorted(self.__dice_values)
        if (((s_dices[0] == s_dices[1]) and
             (s_dices[2] == s_dices[3]) and (s_dices[3] == s_dices[4]))
                or ((s_dices[0] == s_dices[1] and s_dices[1] == s_dices[2]) and
                    (s_dices[3] == s_dices[4]))):
            round_points = 25
        else:
            round_points = 0
        # c. Display the corresponding point label
        self.submit_point_labels["full_house"].configure(
            text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Full house", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def small_straight(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["small_straight"]
        Small straight means a straight of at least four dices
        ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]).
        Score for a small straight: 30
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["small_straight"] = True
        # b. Determine the number of points for the round
        if (((2 in self.__dice_values and 3 in self.__dice_values) and (
                1 in self.__dice_values or 4 in self.__dice_values)) or
                (3 in self.__dice_values and 4 in self.__dice_values and
                 5 in self.__dice_values and 6 in self.__dice_values)):
            round_points = 30
        else:
            round_points = 0
        # c. Display the corresponding point label
        self.submit_point_labels["small_straight"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(
            self.get_round_message("Small straight", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def large_straight(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["large_straight"]
        Large straight is [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6] in any order.
        Score for a large straight: 40
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["large_straight"] = True
        # b. Determine the number of points for the round
        if (2 in self.__dice_values and 3 in self.__dice_values and
            4 in self.__dice_values and 5 in self.__dice_values) and (
                1 in self.__dice_values or 6 in self.__dice_values):
            round_points = 40
        else:
            round_points = 0
        # c. Display the corresponding point label
        self.submit_point_labels["large_straight"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(
            self.get_round_message("Large straight", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def yahtzee(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["yahtzee"]
        Yahtzee means all dices have the same value.
        Score for a Yahtzee combination: 50.
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["yahtzee"] = True
        # b. Determine the number of points for the round
        round_points = 0
        for val in range(1, 7):
            if self.__dice_values.count(val) == 5:
                round_points = 50
        # c. Display the corresponding point label
        self.submit_point_labels["yahtzee"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Yahtzee", round_points))
        # f. Set up the next round
        self.set_up_next_round()

    def chance(self):
        """
        End a round, update the points and set up the next round.
        Button associated: submit_button["chance"]
        Chance means any combination of dices.
        Score for a chance combination: sum of all dices.
        """
        # a. Mark the button as clicked
        self.__submit_button_clicked["chance"] = True
        # b. Determine the number of points for the round
        round_points = self.sum_of_all_dices()
        # c. Display the corresponding point label
        self.submit_point_labels["chance"].configure(text=round_points)
        # d. Calculate and update the total point label
        self.update_point(round_points)
        # e. Display the message in the messagebox
        self.set_message(self.get_round_message("Chance", round_points))
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
        # state to disabled, submit_button_clicked to False
        # and empty all corresponding point text labels.
        self.disable_available_submit_buttons()
        for b in self.__submit_button_clicked:
            self.__submit_button_clicked[b] = False
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

    def sum_of_all_dices(self):
        """
        Calculate the sum of all dices.
        :return: int, sum of all dices.
        """
        result = 0
        for val in self.__dice_values:
            result += val
        return result

    def update_point(self, round_points):
        """
        Calculate the new total point after a round and update the label.
        :param round_points: the point gained from a round.
        """
        self.__total_points += round_points
        self.__total_points_label.configure(text=self.__total_points)

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
        Enable available submit buttons - whose submit_button_clicked is False.
        """
        for sb_name in self.__submit_button_clicked:
            if self.__submit_button_clicked[sb_name] == False:
                self.submit_buttons[sb_name].configure(relief=RAISED,
                                                       state=NORMAL)

    def game_over(self):
        """
        Check whether the game is over,
        i.e. whether all submit buttons are clicked.
        :return: bool, True if the game is over.
        """
        for sb_name in self.__submit_button_clicked:
            if self.__submit_button_clicked[sb_name] == False:
                return False
        return True

    def get_round_message(self, button_name, round_points):
        """
        Get a round message to display after a round (clicking a submit button)
        :param button_name: the clicked submit button
        :param round_points: the number of points got from that round
        :return: string, the round message to be displayed
        """
        round_message1 = (f"{button_name} is chosen.\n"
                          f"Your score for this round: {round_points}\n")
        if self.game_over() == False:
            round_message2 = "Please roll the dices!"
        else:
            round_message2 = (f"The game is over. Your total points is "
                              f"{self.__total_points}. Congratulations!")
        return round_message1 + round_message2

    def set_up_next_round(self):
        """
        Set up the buttons and checkboxes for the next round.
        """
        if self.game_over() == False:
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
            # Disable checkboxes, roll button and submit buttons
            self.disable_checkboxes()
            self.disable_available_submit_buttons()
            self.__roll_button.configure(relief=SUNKEN, state=DISABLED)
            # Set number of rolls to 0
            self.__number_of_rolls = 0
            self.__number_of_rolls_label.configure(text=self.__number_of_rolls)


def main():
    Yahtzee()


if __name__ == "__main__":
    main()
