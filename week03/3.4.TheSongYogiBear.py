"""
COMP.CS.100 Programming 1.
3.4.TheSongYogiBear.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def repeat_name(first, rep):
    """
    repeat_name() function:
    objective: to avoid unnecessary repetitions while printing the lyrics
    :param first: string _ the first word in the name
    :param rep: int _ the number of repetitions
    :return: none
    """
    for i in range(rep):
        print(f"{first}, {first} Bear")

def verse(line, first):
    """
    verse() function:
    objective: to avoid unnecessary repetitions while printing the lyrics
    :param line: string _ the first line of the verse
    :param first: string _ the first word in the name
    :return: none
    """
    print(line)
    print(f"{first}, {first}")
    print(line)
    repeat_name(first, 3)
    print(line)
    repeat_name(first, 1)

def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
