"""
COMP.CS.100 Programming 1.
3.7.PrintingABoxAndCheckingTheInputs.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def read_input(dim):
    """
    read_input() function:
    objective: read and check whether the inputs for width and height are valid
    :param dim: string _ question for the inquired dimension
    :return: int, int _ valid width, height

    :return:
    """

    res = 0
    while res <= 0:
        tempRes = input(dim)
        res = int(tempRes)

    return res

def print_box(x, y, mark):
    """
    print_box() function:
    objective: print out a box with declared dimensions and mark
    :param x: string _ number of columns
    :param y: string _ number of rows
    :param mark: string _ mark used to print out
    :return:none
    """
    x = int(x)
    y = int(y)
    for i in range(y):
        for j in range(x):
            print(mark, end = "")
        if i < y - 1:
            print()

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
