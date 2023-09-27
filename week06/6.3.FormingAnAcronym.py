"""
COMP.CS.100 Programming 1
6.3.FormingAnAcronym.py
Creator: Thinh Kieu
Student number: 152167613
"""

def create_an_acronym(word):
    """
    create an acronym by taking the first letters of each word and capitalize them
    variables: word _ string
    return: acr _ string
    """
    wordlist = word.split(" ")
    acr = ""
    for w in wordlist:
        acr += w[0]
    return acr.upper()

def main():
    print(create_an_acronym("central intelligence agency"))

if __name__ == "__main__":
    main()
