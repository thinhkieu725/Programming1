"""
COMP.CS.100 Programming 1.
1.7.Change.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    ten = 0; five = 0; two = 0; one = 0
    price = input("Purchase price: ")
    paid = input("Paid amount of money: ")
    change = int(paid) - int(price)
    if (change > 0):
        while change > 0:
            if change >= 10:
                ten += 1
                change -= 10
            elif change >= 5:
                five += 1
                change -= 5
            elif change >= 2:
                two += 1
                change -= 2
            else:
                one += 1
                change -= 1
        print("Offer change:")
        if ten > 0:
            print(ten, "ten-euro notes")
        if five > 0:
            print(five, "five-euro notes")
        if two > 0:
            print(two, "two-euro coins")
        if one > 0:
            print(one, "one-euro coins")
    else:
        print("No change")

if __name__ == "__main__":
    main()