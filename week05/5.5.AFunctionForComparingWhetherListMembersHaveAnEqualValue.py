"""
COMP.CS.100 Programming 1
5.5.AFunctionForComparingWhetherListMembersHaveAnEqualValue.py
Creator: Thinh Kieu
Student number: 152167613
"""

def are_all_members_same(a):
    """
    decide whether a has the same elements
    variables: a _ list
    return: res _ bool
    """
    if len(a) == 0:
        return True
    else:
        return a.count(a[0]) == len(a)

def main():
    test1 = are_all_members_same([42, 42, 42, 43, 42])
    test2 = are_all_members_same([42, 42, 42, 42, 42])
    print(test1)
    print(test2)

if __name__ == "__main__":
    main()
