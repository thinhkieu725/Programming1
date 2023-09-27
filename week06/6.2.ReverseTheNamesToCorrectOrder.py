"""
COMP.CS.100 Programming 1
6.2.ReverseTheNameToCorrectOrder.py
Creator: Thinh Kieu
Student number: 152167613
"""

def reverse_name(fullName):
    """
    reverse the full name to its right order
    variables: fullName _ string
    return: reversedName _ string
    """
    names = fullName.split(",")
    if len(names) == 0:
        return ""
    if len(names) == 1:
        return names[0].strip()

    names[0] = names[0].strip()
    names[1] = names[1].strip()

    if names[0] == "":
        return names[1]
    if names[1] == "":
        return names[0]

    reversedName = names[1] + " " + names[0]
    return reversedName

def main():
    print(reverse_name(',X'))
    print(reverse_name(' , Y '))
    print(reverse_name(','))

if __name__ == "__main__":
    main()
