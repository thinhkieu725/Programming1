"""
COMP.CS.100 Programming 1.
2.11.BoredImprovedVersion.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    tempAns = "n"
    while True:
        tempAns = input("Bored? (y/n) ")
        if tempAns == "y" or tempAns == "Y":
            break
        elif tempAns != "n" and tempAns != "N":
            print("Incorrect entry.")
    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()

