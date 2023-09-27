"""
COMP.CS.100 Programming 1.
2.2.BoredCheckingForErrors.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    ans = "0"
    tempAns = "n"
    while ans == "0":
        tempAns = input("Answer Y or N: ")
        if tempAns == "y" or tempAns == "Y" or tempAns == "n" or tempAns == "N":
            ans = tempAns
        else:
            print("Incorrect entry.")
    print("You answered", ans)

if __name__ == "__main__":
    main()