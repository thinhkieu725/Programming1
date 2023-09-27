"""
COMP.CS.100 Programming 1
6.6.SavingAMessage.py
Creator: Thinh Kieu
Student number: 152167613
"""

def read_message():
    """
    read the message from the user until entering an empty row. Return the rows in a list
    param: none
    return: list _ all the lines entered
    """
    line = ""
    lineList = []
    while True:
        line = input()

        if line == "":
            break

        lineList.append(line)
    return lineList

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for line in msg:
        print(line.upper())

if __name__ == "__main__":
    main()
