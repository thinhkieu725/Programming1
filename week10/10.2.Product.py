"""
COMP.CS.100 Programming 1.
10.2.Product.py
Creator: Thinh Kieu
Student id number: 152167613
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    __sale_percentage: float

    def __init__(self, name, price):
        """
        A product is initialized with its name and its price.
        The sale_percentage by default is set to 0

        :param name: string, name of the product
        :param price: float, normal price of the product

        :attribute sale_percentage: float, the sale percentage of the product
        """
        self.__name = name
        self.__price = price
        self.__sale_percentage = 0

    def printout(self):
        """
        Print out the information about the product
        """
        print(self.__name)
        print("  price:", f"{self.__price:.2f}")
        print("  sale%:", f"{self.__sale_percentage:.2f}")

    def get_price(self):
        """
        Return the price of the product after considering the sale percentage

        :return: the price after applying sale (if any)
        """
        return self.__price * (1 - self.__sale_percentage/100)

    def set_sale_percentage(self, sale_percentage):
        """
        Set a new percentage for the product

        :param sale_percentage: float, the new percentage to be updated
        """
        self.__sale_percentage = sale_percentage

def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk": 1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
