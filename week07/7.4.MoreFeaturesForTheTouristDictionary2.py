"""
COMP.CS.100 Programming 1.
7.4.MoreFeaturesForTheTouristDictionary2.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def printDictContent(dictionary):
    """
    print out all the keys in alphabetical order
    :param dictionary: the subjected dictionary
    :return: none
    """

    wordList = sorted(dictionary)
    print("Dictionary contents:")
    print(", ".join(wordList))

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {"hola": "hey", "gracias": "thanks", "casa": "home"}

    printDictContent(english_spanish)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            wordAddEng = input("Give the word to be added in English: ")
            wordAddSpain = input("Give the word to be added in Spanish: ")
            english_spanish.update({wordAddEng: wordAddSpain})
            spanish_english.update({wordAddSpain: wordAddEng})
            printDictContent(english_spanish)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "Q":
            print("Adios!")
            return

        elif command == "P":
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
            print()
            print("Spanish-English")
            for word in sorted(spanish_english):
                print(word, spanish_english[word])
            print()

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            wordList = sentence.split(" ")
            translatedWordList = []
            for word in wordList:
                if word in english_spanish:
                    translatedWordList.append(english_spanish[word])
                else:
                    translatedWordList.append(word)
            print("The␣text,␣translated␣by␣the␣dictionary:")
            print(" ".join(translatedWordList))

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
