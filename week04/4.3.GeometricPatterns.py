"""
COMP.CS.100 Programming 1
4.3.GeometricPatterns.py
Creator: Thinh Kieu
Student number: 152167613
"""
from math import pi

def inputSquareSide():
    """
    Get from the user a valid length of square side
    variables: none
    return: float _ a valid length
    """
    side = 0
    while side <= 0:
        side = input("Enter the length of the square's side: ")
        side = float(side)
    return side

def inputRectangleSide(sideNo):
    """
    Get from the user a valid length of rectangle side
    variables: sideNo _ int
    return: float _ a valid length
    """
    side = 0
    while side <= 0:
        side = input(f"Enter the length of the rectangle's side {sideNo}: ")
        side = float(side)
    return side

def inputCircleRadius():
    """
    Get from the user a valid length of circle radius
    variables: none
    return: float _ a valid length
    """
    radius = 0;
    while radius <= 0:
        radius = input("Enter the circle's radius: ")
        radius = float(radius)
    return radius

def printResult(circumference, area):
    """
    Print out the result
    variables: circumference _ float ; area _ float
    return: none
    """
    print(f"The circumference is {circumference:.2f}")
    print(f"The surface area is {area:.2f}")

def printInputError():
    """
    Print out an error notification when the input is invalid
    variables: none
    return: none
    """
    print("Incorrect entry, try again!")

def printGoodbye():
    """
    Print out Goodbye
    variables: none
    return: none
    """
    print("Goodbye!")

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            side = inputSquareSide()
            circumference = side * 4
            area = side * side
            printResult(circumference, area)

        elif answer == "r":
            side1 = inputRectangleSide(1)
            side2 = inputRectangleSide(2)

            circumference = 2 * (side1 + side2)
            area = side1 * side2

            printResult(circumference, area)

        elif answer == "c":
            radius = inputCircleRadius()

            circumference = 2 * radius * pi
            area = radius * radius * pi

            printResult(circumference, area)

        elif answer == "q":
            return

        else:
            printInputError()

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    printGoodbye()

if __name__ == "__main__":
    main()
