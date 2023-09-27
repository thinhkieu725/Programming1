"""
COMP.CS.100 Programming 1
5.8.ReplacingCourseGrades.py
Creator: Thinh Kieu
Student number: 152167613
"""

def convert_grades(listOfGrades):
    """
    convert all the grades to pass/fail (0/6)
    variables: listOfGrades _ list
    return: none
    """
    if len(listOfGrades) > 0:
        for i in range(len(listOfGrades)):
            if listOfGrades[i] in [1, 2, 3, 4, 5]:
                listOfGrades[i] = 6

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
