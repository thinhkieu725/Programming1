"""
COMP.CS.100 Programming 1
6.1.VowelsAndConsonants.py
Creator: Thinh Kieu
Student number: 152167613
"""

def main():
    vowels = ["a", "e", "i", "o", "u", "y"]
    word = input("Enter a word: ")
    v = 0; c = 0
    for char in word:
        if char in vowels:
            v += 1
        else:
            c += 1
    print(f"The word \"{word}\" contains {v} vowels and {c} consonants.", end = "")

if __name__ == "__main__":
    main()
