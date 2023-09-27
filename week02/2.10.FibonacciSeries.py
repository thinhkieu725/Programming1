"""
COMP.CS.100 Programming 1.
2.10.FibonacciSeries.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def main():
    num = input("How many Fibonacci numbers do you want? ")
    num = int(num)

    temp1 = 0
    temp2 = 1
    temp3 = 0

    for i in range(1, num + 1):
        if i == 1:
            print(f"{i}. 1")
        else:
            temp1 = temp2 + temp3
            temp3 = temp2
            temp2 = temp1
            print(f"{i}. {temp1}")

if __name__ == "__main__":
    main()

