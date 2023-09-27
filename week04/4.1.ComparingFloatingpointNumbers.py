"""
COMP.CS.100 Programming 1
4.1.ComparingFloatingpointNumbers.py
Creator: Thinh Kieu
Student number: 152167613
"""

def compare_floats(a, b, EPSILON):
    """
    compare_floats() function:
    objective: to decide whether 2 floats are equal by comparing the diffrence with an EPSILON number.
    variables:
        a _ int _ first number
        b _ int _ second number
    return: bool _ True if they can be defined equal, otherwise False.
    """
    if abs(a - b) < EPSILON:
        return True
    else:
        return False

def main():
    EPSILON = 1e-9
    print(compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON))
    print(compare_floats(0.0002, 0.0000002, EPSILON))

if __name__ == "__main__":
    main()
