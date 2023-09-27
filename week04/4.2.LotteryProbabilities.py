"""
COMP.CS.100 Programming 1
4.2.LotteryProbabilities.py
Creator: Thinh Kieu
Student number: 152167613
"""

def factorial(a):
    """
    factorial(a) function:
    objective: caltulating the factorial of a number
    variables: a _ int _ number for operation
    return: int _ result of the operation
    """
    res = 1
    if a == 0:
        return res
    for i in range(1, a+1):
        res = res * i
    return res

def calc():
    """
    calc() function:
    objective: caltulating the possibilities
    variables: none
    return: none
    """
    numLot = input("Enter the total number of lottery balls: ")
    numDrawn = input("Enter the number of the drawn balls: ")
    numLot = int(numLot)
    numDrawn = int(numDrawn)
    if (numLot <= 0 or numDrawn <= 0):
        print("The number of balls must be a positive number.")
        return
    if (numLot < numDrawn):
        print("At most the total number of balls can be drawn.")
        return

    possibilities = factorial(numLot) / factorial(numLot - numDrawn) / factorial(numDrawn)
    print(f"The probability of guessing all {numDrawn} balls correctly is 1/{possibilities:.0f}")

def main():
    calc()

if __name__ == "__main__":
    main()
