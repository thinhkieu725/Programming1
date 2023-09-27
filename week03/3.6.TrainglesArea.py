"""
COMP.CS.100 Programming 1.
3.6.TrianglesArea.py
Creator: Thinh Kieu
Student id number: 152167613
"""

from math import sqrt

def area(s1, s2, s3):
    """
    area() function:
    objective: calculate the area of a triangle
    :param s1: string _ length of the first side
    :param s2: string _ length of the second side
    :param s3: string _ length of the third side
    :return: float _ area of the triangle
    """
    s1 = float(s1)
    s2 = float(s2)
    s3 = float(s3)

    p = (s1 + s2 + s3) / 2

    return sqrt(p * (p - s1) * (p - s2) * (p - s3))

def main():
    line1 = input("Enter the length of the first side: ")
    line2 = input("Enter the length of the second side: ")
    line3 = input("Enter the length of the third side: ")

    print("The triangle's area is", f"{area(line1, line2, line3):.1f}")

if __name__ == "__main__":
    main()
