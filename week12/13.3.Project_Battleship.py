"""
COMP.CS.100 Programming 1.
12.3.Project_Battleship.py

Creator: Thinh Kieu
Student ID number: 152167613
Student ID: dxthki
Email: thinh.kieu@tuni.fi

# TODO: Write program description.
"""

# All the ships in the game are stored in a list.
ships = []
# Establish a nested structure to store the 10x10 game board.
board = [[" "] * 10] * 10


class Ship():
    """
    # TODO: Add class description.
    """

    def __init__(self, ship_type, ship_coordinate):
        """
        Initialize a ship object
        :param ship_type: str, type of the ship.
        :param ship_coordinate: lst of int, coordinates of the squares that the
        ship occupies.
        """
        __ship_type = ship_type
        __ship_coordinate = ship_coordinate

    def is_occupied(self, coordinate):
        # TODO: Write function description.
        # TODO: Implement the function.
        pass


def exchange_coordinate(coordinate):
    # TODO: Write function description.
    # TODO: Implement the function.
    pass


def main():
    # Prompt the user to enter the file and then read the file.
    file_name = input("Enter file name: ")
    try:
        file_handle = open(file_name, "r")
    except OSError:
        print("File can not be read!")
        return


if __name__ == "__main__":
    main()
