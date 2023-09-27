"""
COMP.CS.100 Programming 1.
7.7.SortingByPrice.py
Creator: Thinh Kieu
Student id number: 152167613
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}



def main():

    def payload(key):
        """
        return the payload attatched to a key
        :param key: subjected key
        :return: corrsponding payload
        """
        return PRICES.get(key)

    sortedList = sorted(PRICES, key=payload)
    for prod in sortedList:
        print(prod, f"{PRICES[prod]:.2f}")

if __name__ == "__main__":
    main()
