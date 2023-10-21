"""
COMP.CS.100 Programming 1
0.0.codeTest.py
Creator: Thinh Kieu
Student number: 152167613

This is the file for testing
"""

def main():
    d = {"a":1, "b":2, "c":4}
    print(d)
    dval = d.values()
    print(d.values())

    print(type(d.values()))

    for i in dval:
        print(i)

if __name__ == "__main__":
    main()