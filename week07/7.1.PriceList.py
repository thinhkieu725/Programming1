"""
COMP.CS.100 Programming 1.
7.1.PriceList.py
Creator: Thinh Kieu
Student id number: 152167613
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    prod = " "
    while prod != "":
        prod = input("Enter product name: ")
        prod = prod.strip()
        if prod in PRICES:
            print(f"The price of {prod} is {PRICES[prod]:.2f} e")
        elif prod == "":
            break
        else:
            print(f"Error: {prod} is unknown.")
    print("Bye!")

if __name__ == "__main__":
    main()
