"""
COMP.CS.100 Programming 1.
8.5.CalculatingScores.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def main():
    filename = input("Enter the name of the score file: ")
    try:
        file = open(filename, "r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    scores = dict()
    for file_line in file:
        lst = file_line.rstrip().split()
        try:
            lst[1] = int(lst[1])
        except IndexError:
            print("There was an erroneous line in the file:")
            print(file_line.rstrip())
            return
        except ValueError:
            print("There was an erroneous score in the file:")
            print(lst[1])
            return

        if lst[0] in scores:
            scores[lst[0]] += lst[1]
        else:
            scores.update({lst[0]: lst[1]})

    file.close()

    keyList = sorted(scores)
    print("Contestant score:")
    for k in keyList:
        print(k, scores[k])

if __name__ == "__main__":
    main()
