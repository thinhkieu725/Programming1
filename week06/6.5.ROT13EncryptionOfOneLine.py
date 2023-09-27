"""
COMP.CS.100 Programming 1
6.5.ROT13EncryptionOfOneLine.py
Creator: Thinh Kieu
Student number: 152167613
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    capitalize = False
    if text in regular_chars:
        idx = regular_chars.index(text)
        return encrypted_chars[idx]
    elif text.lower() in regular_chars:
        capitalize = True
        text = text.lower()
        idx = regular_chars.index(text)
        return encrypted_chars[idx].upper()
    else:
         return text

def row_encryption(text):
    """
    Encrypts a row using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    result = ""
    for c in text:
        result += encrypt(c)
    return result

def main():
    print(encrypt("e"))
    print(encrypt("E"))
    print(encrypt("?"))
    print (row_encryption("Happy, happy, joy, joy!"))

if __name__ == "__main__":
    main()
