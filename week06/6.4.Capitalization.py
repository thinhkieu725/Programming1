"""
COMP.CS.100 Programming 1
6.4.Capitalization.py
Creator: Thinh Kieu
Student number: 152167613
"""

def capitalize_initial_letters(word):
    """
    capitalize the initial letters of a word
    variables: word _ string
    return: capWord _ string
    """
    capWord = ""
    wordList = word.split(" ")
    for i in range(len(wordList)):
        wordList[i]  = wordList[i].capitalize()
    capWord = " ".join(wordList)
    return capWord

def main():
    print(capitalize_initial_letters("central intelligence agency"))

if __name__ == "__main__":
    main()
