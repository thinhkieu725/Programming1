"""
COMP.CS.100 Programming 1
6.8.HowManyAbbas.py
Creator: Thinh Kieu
Student number: 152167613
"""

def count_abbas(text):
    """
    count the number of string "abba" that the parameter string contains
    param: text
    return: int _ the number of "abba" strings
    """
    result = 0

    for idx in range(len(text) - 4 + 1):
        if text[idx : idx + 4] == "abba":
            result += 1

    return result


def main():
    print(count_abbas("abbabbabba"))

if __name__ == "__main__":
    main()
