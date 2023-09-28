"""
COMP.CS.100 Programming 1.
8.4.WritingNumberedLinesToAFile.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def main():
    filename = input("Enter the name of the file: ")
    try:
        saveFile = open(filename, "w")
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    idx = 1
    inputLine = " "

    print("Enter rows of text. Quit by entering an empty row.")
    while True:
        inputLine = input()
        if inputLine == "":
            break
        print(idx, inputLine, file=saveFile)
        idx += 1

    print(f"File {filename} has been written.")
    saveFile.close()

if __name__ == "__main__":
    main()
