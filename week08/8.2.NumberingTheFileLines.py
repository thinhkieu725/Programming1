"""
COMP.CS.100 Programming 1.
8.2.NumberingTheFileLines.py
Creator: Thinh Kieu
Student id number: 152167613

This file is also submitted for the next exercise
"""

def main():
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, "r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    idx = 1
    for file_line in file:
        print (idx, file_line.rstrip())
        idx += 1

    file.close()

if __name__ == "__main__":
    main()
