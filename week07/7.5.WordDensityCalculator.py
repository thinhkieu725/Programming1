"""
COMP.CS.100 Programming 1.
7.5.WordDensityCalculator.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def main():
    wordList = dict()
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        sentence = input()
        if sentence == "":
            break
        sentence = sentence.lower()
        words = sentence.split(" ")
        for word in words:
            if word in wordList:
                wordList[word] += 1
            else:
                wordList.update({word: 1})

    for w in sorted(wordList):
        print(f"{w} : {wordList[w]} times")

if __name__ == "__main__":
    main()
