"""
COMP.CS.100 Programming 1.
2.5.NumberSeriesGameZipBoing.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    num = input("How many numbers would you like to have? ")
    num = int(num)
    for i in range(1, num + 1):
        if i % 3 != 0 and i % 7 != 0:
            print(i)
        if i % 3 == 0 and i % 7 != 0:
            print("zip")
        if i % 3 != 0 and i % 7 == 0:
            print("boing")
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")

if __name__ == "__main__":
    main()