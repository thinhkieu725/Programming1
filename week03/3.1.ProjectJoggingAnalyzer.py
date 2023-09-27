"""
COMP.CS.100 Programming 1.
3.1.ProjectJoggingAnalyzer.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def main():
    days = input("Enter the number of days: ")
    days = int(days)

    meanRunning = 0
    check = 0

    for i in range(days):
        run = input(f"Enter day {i+1} running length: ")
        run = float(run)

        if run == 0:
            check += 1
        else:
            check = 0

        if check == 3:
            break

        meanRunning += run

    print()
    if check == 3:
        print("You had too many consecutive lazy days!")
    else:
        meanRunning /= days
        if meanRunning >= 3:
            print(f"You were persistent runner! With a mean of {meanRunning:.2f} km.")
        else:
            print(f"Your running mean of {meanRunning:.2f} km was too low!")

if __name__ == "__main__":
    main()