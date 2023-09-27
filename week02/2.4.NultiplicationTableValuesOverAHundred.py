"""
COMP.CS.100 Programming 1.
2.4.MultiplicationTableValuesOverAHundred.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    num = input("Choose a number: ")
    num = int(num)
    for i in range(1, 100//num+2):
        print(i, "*", num, "=", i*num)

if __name__ == "__main__":
    main()