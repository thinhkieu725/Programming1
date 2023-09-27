"""
COMP.CS.100 Programming 1.
2.9.FixingFieldWidth.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

if __name__ == "__main__":
    main()

