"""
COMP.CS.100 Programming 1.
2.3.MultiplicationTableSchoolVersion.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    num = input("Choose a number: ")
    num = int(num)
    for i in range(1, 11):
        print(i, "*", num, "=", i*num)

if __name__ == "__main__":
    main()