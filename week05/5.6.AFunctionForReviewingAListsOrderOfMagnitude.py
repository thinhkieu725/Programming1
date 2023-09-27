"""
COMP.CS.100 Programming 1
5.6.AFunctionForReviewingAListsOrderOfMagnitude.py
Creator: Thinh Kieu
Student number: 152167613
"""

def is_the_list_in_order(a):
    """
    decide whether a list is in ascending order
    variables: a _ list
    return: res _ bool
    """
    if len(a) == 0:
        return True
    else:
        return sorted(a) == a

def main():
    test1 = is_the_list_in_order([37, 42, 43])
    test2 = is_the_list_in_order([42, 37, 43])
    print(test1)
    print(test2)

if __name__ == "__main__":
    main()
