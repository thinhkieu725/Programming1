"""
COMP.CS.100 Programming 1.
12.1.GameCharacterA.py
Creator: Thinh Kieu
Student id number: 152167613
"""


class Character:
    def __init__(self, name):
        """
        Initialize the character.
        :param name: string, the name of the character
        """
        self.__name = name
        self.__backpack = dict()

    def give_item(self, item):
        """
        Add an item to the character's backpack.
        :param item: the item to be added
        """
        if item in self.__backpack:
            self.__backpack[item] += 1
        else:
            self.__backpack.update({item: 1})

    def remove_item(self, item):
        """
        Remove an item from the character's backpack.
        :param item: the item to be removed
        """
        if item in self.__backpack:
            self.__backpack[item] -= 1
            if self.__backpack[item] == 0:
                self.__backpack.pop(item)
        else:
            print(f"ERROR: There is no {item} to be removed")

    def printout(self):
        """
        Print out the name of the character, the items and their quantities.
        """
        print(f"Name: {self.__name}")
        if len(self.__backpack) == 0:
            print("  --nothing--")
        else:
            for item in sorted(self.__backpack):
                print(f"  {self.__backpack[item]} {item}")

    def get_name(self):
        """
        Return the name of the character.
        :return: string, name of the character
        """
        return self.__name

    def has_item(self, item):
        """
        Check whether the character has the item.
        :param item: string, name of the item
        :return: bool, True if the character has the item
        """
        if item in self.__backpack:
            return True
        else:
            return False

    def how_many(self, item):
        """
        Return the quantity of an item in the character's backpack.
        :param item: string, name of the inquired item
        :return: int, the quantity of the item
        """
        if item in self.__backpack:
            return self.__backpack[item]
        else:
            return 0


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
