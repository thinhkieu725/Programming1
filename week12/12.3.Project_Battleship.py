"""
COMP.CS.100 Programming 1.
12.3.Project_Battleship.py

Creator: Thinh Kieu
Student ID number: 152167613
Student ID: dxthki
Email: thinh.kieu@tuni.fi

This program establishes a single-player version of the game Battleship.
The player's objective is to sink all enemy (computer's) ship
"""

# Constants storing standard coordinate values for reference.
# X represent columns, Y represent rows.
X_COORDINATES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
Y_COORDINATES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# All marks that denote sunken ships on the board are stored in a dictionary.
SHIP_MARKS = {"battleship": "B", "cruiser": "C", "destroyer": "D",
              "submarine": "S"}

# All the ships in the game are stored in a list.
ships = []
# Establish a nested structure to store the 10x10 game board.
board = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
]


class Ship():
    """
    This class stores the information and methods of every ship on the board.
    """

    def __init__(self, ship_type, ship_coordinate):
        """
        Initialize a ship object
        :param ship_type: str, type of the ship.
        :param ship_coordinate: lst of int, coordinates of the squares that the
        ship occupies.
        :attribute: sunken: bool, True if every square of the ship is hit.
        """
        self.__ship_type = ship_type
        self.__ship_coordinate = ship_coordinate
        self.__sunken = False

    def get_sunken(self):
        """
        Return the state of the ship.
        :return: bool, True if the ship is sunken
        """
        return self.__sunken

    def does_occupy(self, coordinate):
        """
        Check whether a ship occupies a square.
        :param coordinate: str, the prompted coordinate
        :return: bool, True if the ship occupies the square
        """
        coordinate = coordinate.upper()
        if coordinate in self.__ship_coordinate:
            return True
        else:
            return False

    def update_state(self):
        """
        Check if all squares of a ship is attacked.
        If so, update __sunken to true, update the mark on the board
        and print out the notification.
        """
        # Loop through every square that the ship occupies.
        for coord in self.__ship_coordinate:
            x, y = convert_coordinate(coord)
            # If the square has not been shot at, the ship is not sunken.
            # Stop the process
            if board[y][x] == " ":
                return
        # If the ship is sunken, update the state.
        self.__sunken = True
        # Update the mark.
        for coord in self.__ship_coordinate:
            x, y = convert_coordinate(coord)
            board[y][x] = SHIP_MARKS[self.__ship_type]
        # Print out the notification.
        print(f"You sank a {self.__ship_type}!")


def convert_coordinate(coordinate):
    """
    Convert a valid coordinate into the form of integer coordinates.
    :param coordinate: str, the prompted coordinate
    :return: int, int, two numbers that are x and y coordinates
    """
    coordinate = coordinate.upper()
    x = X_COORDINATES.index(coordinate[0])
    y = int(coordinate[1])
    return x, y


def is_occupied_by(coordinate):
    """
    Check whether a square is occupied by any ship.
    :param coordinate: the prompted square
    :return: int, index of the ship that occupies the square; -1 if unoccupied.
    """
    coordinate = coordinate.upper()
    # Loop through all ships using index.
    for idx in range(len(ships)):
        # If the ship occupies the square, return the index.
        if ships[idx].does_occupy(coordinate):
            return idx
    # If no ship occupies the square, return -1
    return -1


def print_board():
    """
    Print out the game board.
    """
    print()
    # Print the top navigating row.
    print("  ", end="")
    for c in X_COORDINATES:
        print(c, end=" ")
    print()
    # Print 10 main rows.
    for y_coord in range(10):
        print(y_coord, end=" ")
        for x_coord in range(10):
            print(board[y_coord][x_coord], end=" ")
        print(y_coord)
    # Print the top navigating row.
    print("  ", end="")
    for c in X_COORDINATES:
        print(c, end=" ")
    print()
    print()


def valid_coordinate(coordinate):
    """
    Check whether a string is a valid coordinate.
    :param coordinate: str, the prompted string
    :return: bool, True if the coordinate is valid.
    """
    coordinate = coordinate.upper()
    # Check if the string has the right length.
    if len(coordinate) != 2:
        return False
    # Check if the characters are valid coordinates.
    if not (coordinate[0] in X_COORDINATES and coordinate[1] in Y_COORDINATES):
        return False
    return True


def win():
    """
    Check whether the player has won, i.e. all ships has been sunken.
    :return: bool, True if all ships are sunken
    """
    # Loop through all ships and check their state.
    for s in ships:
        if s.get_sunken() == False:
            return False
    return True


def main():
    # ========== PROCESSING FILE DATA ==========
    # Prompt the user to enter the file and then read the file.
    file_name = input("Enter file name: ")
    if file_name == "":
        file_name = "input.txt"
    try:
        file_handle = open(file_name, "r")
    except OSError:
        print("File can not be read!")
        return
    # Process the file line by line.
    for file_line in file_handle:
        components = file_line.strip().split(";")
        # Extract ship_type and ship_coordinates.
        ship_type = components[0]
        new_ship_coordinates = []
        for coord in components[1:]:
            new_ship_coordinates.append(coord.upper())
        # Check whether the new ship data is valid.
        for coord in new_ship_coordinates:
            if not valid_coordinate(coord):
                print("Error in ship coordinates!")
                return
            elif is_occupied_by(coord) != -1:
                print("There are overlapping ships in the input file!")
                return
        # Add the new ship to the list.
        ships.append(Ship(ship_type, new_ship_coordinates))

    # ========== GAME RUNNING ==========
    print_board()
    # Game loop
    while True:
        prompt = input("Enter place to shoot (q to quit): ")
        prompt = prompt.upper()
        # Check if the prompt is to quit.
        if prompt == "Q":
            print("Aborting game!")
            break
        # Check if the prompt is valid.
        if not valid_coordinate(prompt):
            print("Invalid command!")
            print_board()
            continue

        # Process the coordinates.
        x_coord, y_coord = convert_coordinate(prompt)
        # Check whether the square has already been shot at.
        if board[y_coord][x_coord] != " ":
            print("Location has already been shot at!")
            print_board()
            continue

        attacked_ship = is_occupied_by(prompt)
        # If the shot does not hit any ship.
        if attacked_ship == -1:
            board[y_coord][x_coord] = "*"
        # If the shot hits a ship.
        else:
            # Mark X at the attacked square
            board[y_coord][x_coord] = "X"
            # Run update_state function for the attacked ship
            ships[attacked_ship].update_state()
        print_board()
        # At the end of each round in which a ship it hit,
        # check whether the player has won the game.
        if win():
            print("Congratulations! You sank all enemy ships.")
            break


if __name__ == "__main__":
    main()
