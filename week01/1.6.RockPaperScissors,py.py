"""
COMP.CS.100 Programming 1.
1.6.RockPaperScissors.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    p1 = input("Player 1, enter your choice (R/P/S): ")
    p2 = input("Player 2, enter your choice (R/P/S): ")

    if p1 == p2:
        print("It's a tie!")
    elif p1 == "R" and p2 == "S":
        print("Player 1 won!")
    elif p1 == "S" and p2 == "P":
        print("Player 1 won!")
    elif p1 == "P" and p2 == "R":
        print("Player 1 won!")
    elif p1 == "R" and p2 == "P":
        print("Player 2 won!")
    elif p1 == "P" and p2 == "S":
        print("Player 2 won!")
    elif p1 == "S" and p2 == "R":
        print("Player 2 won!")

if __name__ == "__main__":
    main()