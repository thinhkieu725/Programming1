"""
COMP.CS.100 Programming 1.
3.5.PrintingABox.py
Creator: Thinh Kieu
Student id number: 152167613
"""

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
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
