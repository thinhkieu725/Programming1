"""
COMP.CS.100 Programming 1.
1.5.Smileys.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    feel = input("How do you feel? (1-10) ")
    f = int(feel)

    if f > 7 and f <10:
        print("A suitable smiley would be :-)")
    elif f>=4 and f<=7:
        print("A suitable smiley would be :-|")
    elif f>1 and f<=3:
        print("A suitable smiley would be :-(")
    elif f==1:
        print("A suitable smiley would be :'(")
    elif f==10:
        print("A suitable smiley would be :-D")
    else:
        print("Bad input!")

if __name__ == "__main__":
    main()