"""
COMP.CS.100 Programming 1.
3.3.TheSongPuffTheMagicDragon.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def print_verse(animal, sound):
    """
    print_verse() function
    Objective: avoid unnecessary repetition while printing the lyrics
    :param animal: string _ the animal's name
    :param sound: string _ the sound that the animal makes
    :return: none
    """
    print(
f"""Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a {animal}
E-I-E-I-O
With a {sound} {sound} here
And a {sound} {sound} there
Here a {sound}, there a {sound}
Everywhere a {sound} {sound}
Old MacDonald had a farm
E-I-E-I-O"""
    )

def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
