"""
COMP.CS.100 Programming 1
5.7.RubiksCubeSolvingContests.py
Creator: Thinh Kieu
Student number: 152167613
"""

def calc(a):
    """
    calculate the competition score
    variables: a _ list of times in seconds
    return: res _ bool
    """
    res = 0
    for num in a:
        res += num
    res = res - max(a) - min(a)
    res /= 3
    return res

def main():
    time = []
    for i in range(5):
        s = input(f"Enter the time for performance {i+1}: ")
        s = float(s)
        time.append(s)
    finalRes = calc(time)
    print(f"The official competition score is {finalRes:.2f} seconds.")

if __name__ == "__main__":
    main()
