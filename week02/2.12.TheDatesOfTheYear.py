"""
COMP.CS.100 Programming 1.
2.12.TheDatesOfTheYear.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    for month in range(1, 13):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            for day in range(1, 32):
                print(f"{day}.{month}.")
        elif month == 2:
            for day in range(1, 29):
                print(f"{day}.{month}.")
        else:
            for day in range(1, 31):
                print(f"{day}.{month}.")

if __name__ == "__main__":
    main()

