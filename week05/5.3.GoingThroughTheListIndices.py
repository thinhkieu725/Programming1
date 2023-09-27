"""
COMP.CS.100 Programming 1
5.3.GoingThroughTheListIndices.py
Creator: Thinh Kieu
Student number: 152167613
"""

def main():
    result = []

    print("Give 5 numbers:")
    for i in range(5):
        inp = input("Next number: ")
        inp = int(inp)
        result.append(inp)

    print("The numbers you entered, in reverse order:")
    for i in range(4, -1, -1):
        print(result[i])


if __name__ == "__main__":
    main()
