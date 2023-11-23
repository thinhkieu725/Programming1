"""
COMP.CS.100 Programming 1.
12.3.Project_Battleship.py

Creator: Thinh Kieu
Student ID number: 152167613
Student ID: dxthki
Email: thinh.kieu@tuni.fi

# TODO: Write program description.
"""

# Constants storing standard coordinate values for reference.
# X represent columns, Y represent rows.
X_COORDINATES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
Y_COORDINATES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
        :attribute: sunken: bool, True if every square of the ship is hit.
        """
        self.__ship_type = ship_type
        self.__ship_coordinate = ship_coordinate
        self.__sunken = False

    def does_occupy(self, coordinate):
        # TODO: Write function description.
        # TODO: Implement the function.
        pass


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
    # TODO: Implement the function.
    pass


def print_board():
    """
    Print out the game board.
    """
    print()
    # Print the top navigating row.
    print("  ", end="")
    for c in X_COORDINATES:
        print(c, end=" ")
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


def valid_coordinate(coordinate):
    """
    Check whether a string is a valid coordinate.
    :param coordinate: str, the prompted string
    :return: bool, True if the coordinate is valid.
    """
    coordinate = coordinate.upper()
    if len(coordinate) != 2:
        return False
    if not (coordinate[1] in X_COORDINATES and coordinate[2] in Y_COORDINATES):
        return False
    return True


def main():
    # ========== PROCESSING FILE DATA ==========
    # Prompt the user to enter the file and then read the file.
    file_name = input("Enter file name: ")
    try:
        file_handle = open(file_name, "r")
    except OSError:
        print("File can not be read!")
        return
    # Process the file line by line.
    for file_line in file_handle:
        components = file_line.split(";")
        # Extract ship_type and ship_coordinates.
        ship_type = components[0]
        ship_coordinates = []
        for coord in components[1:]:
            ship_coordinates.append(coord.upper())
        # Check whether the new ship data is valid.
        for coord in ship_coordinates:
            if not valid_coordinate(coord):
                print("Error in ship coordinates!")
                return
            elif is_occupied_by(coord) != -1:
                print("There are overlapping ships in the input file!")
                return
        # Add the new ship to the list.
        ships.append(Ship(ship_type, ship_coordinates))

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

        # If the shot does not hit any ship.
        if is_occupied_by(prompt) == -1:
            board[y_coord][x_coord] = "*"
        # If the shot hits a ship.
        else:




if __name__ == "__main__":
    main()
