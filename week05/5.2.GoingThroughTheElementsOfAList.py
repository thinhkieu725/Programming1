"""
COMP.CS.100 Programming 1
5.2.GoingThroughTheElementsOfAList.py
Creator: Thinh Kieu
Student number: 152167613
"""

def main():
    result = []

    print("Give 5 numbers:")
    for i in range(5):
        inp = input("Next number: ")
        inp = int(inp)
        if inp > 0:
            result.append(inp)

    print("The numbers you entered that were greater than zero were:")
    for num in result:
        print(num)

if __name__ == "__main__":
    main()
