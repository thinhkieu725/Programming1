"""
COMP.CS.100 Programming 1
5.4.AListAsAReturnValue.py
Creator: Thinh Kieu
Student number: 152167613
"""

def input_to_list(noOfNumbers):
    """
    read the number from the user
    variables: noOfNumbers _ int
    return: res _ a list of numbers enter by the user
    """
    res = []
    print(f"Enter {noOfNumbers} numbers:")
    for i in range(noOfNumbers):
        num = input()
        num = int(num)
        res.append(num)
    return res

def main():
    noOfNumbers = input("How many numbers do you want to process: ")
    noOfNumbers = int(noOfNumbers)

    lst = input_to_list(noOfNumbers)

    ref = input("Enter the number to be searched: ")
    ref = int(ref)
    count = 0
    for i in lst:
        if i == ref:
            count += 1
    if count > 0:
        print(f"{ref} shows up {count} times among the numbers you have entered.")
    else:
        print(f"{ref} is not among the numbers you have entered.")


if __name__ == "__main__":
    main()
